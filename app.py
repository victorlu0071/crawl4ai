import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, simpledialog
import threading
import time
import asyncio # Import asyncio
import os # Import os for path manipulation
import re # Import re for filename sanitization
import requests # Import requests
import xml.etree.ElementTree as ET # Import ElementTree
import io # Import io for string parsing
import sys # Import sys
from urllib.parse import urlparse, urljoin # For URL joining
import aiohttp # Ensure aiohttp is imported if needed for fetching
from collections.abc import AsyncIterator # Import AsyncIterator

# Add PyInstaller data directory handling
if getattr(sys, 'frozen', False):
    # We're in a PyInstaller bundle
    try:
        # Initialize the resource handler
        import resource_handler
        resource_handler.initialize()
        print("Resource handler initialized successfully.")
        
        # Try to import our utility module to copy data files
        import copy_data
        copy_data.main()
        print("Data files copied successfully.")
    except ImportError as e:
        print(f"Warning: Module import error: {e}")
        print("Data files may not be properly loaded.")
    except Exception as e:
        print(f"Error during initialization: {e}")
    
    # Ensure fake_http_header.data is properly initialized
    # This helps avoid the importlib.resources error with fake_http_header.data
    fake_http_header_data_dir = os.path.join(os.path.dirname(sys.executable), '_internal', 'fake_http_header', 'data')
    if os.path.exists(fake_http_header_data_dir):
        print(f"Found fake_http_header data directory at {fake_http_header_data_dir}")
        # Add the parent to sys.path so Python can import fake_http_header.data
        fake_http_header_parent = os.path.dirname(os.path.dirname(fake_http_header_data_dir))
        if fake_http_header_parent not in sys.path:
            sys.path.insert(0, fake_http_header_parent)
            print(f"Added {fake_http_header_parent} to sys.path")
    else:
        print(f"WARNING: fake_http_header data directory not found at {fake_http_header_data_dir}")

# Now attempt to import the crawl4ai components
try:
    from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, CrawlResult
    from crawl4ai.deep_crawling import BFSDeepCrawlStrategy # Import the strategy
    print("Successfully imported crawl4ai components")
except ImportError as e:
    print(f"Error importing crawl4ai components: {e}")
    messagebox.showerror("Import Error", f"Failed to import required modules: {e}\nThe application may not function correctly.")

# Attempt to find and import Playwright; handle if not found
try:
    from playwright.async_api import async_playwright, Error as PlaywrightError
    print("Successfully imported Playwright components")
except ImportError:
    PlaywrightError = None # Define PlaywrightError as None if import fails
    print("Playwright not found. Please install it: pip install playwright && playwright install")
    # Optionally raise an error or show a message box here if Playwright is strictly required
    # messagebox.showerror("Dependency Error", "Playwright is not installed. Please run 'pip install playwright && playwright install'")

class CrawlerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crawl4AI Demo")
        self.root.geometry("600x500") # Increased height for progress bar

        # --- Configuration Defaults ---
        self.headless_mode = tk.BooleanVar(value=True)
        self.user_agent_str = tk.StringVar(value="") # Empty means default
        self.max_depth_str = tk.StringVar(value="1") # Default deep crawl depth
        self.max_pages_str = tk.StringVar(value="50") # Default max pages for sitemap/deep
        # --- End Configuration Defaults ---

        # --- State variables (simplified - no hook state needed) ---
        # self.output_dir = "" # Handled locally in function
        # self.processed_count = 0 # Handled locally
        # self.success_count = 0 # Handled locally
        # self.failed_urls = [] # Handled locally
        # --- End State variables ---

        # Style
        self.style = ttk.Style(self.root)
        self.style.theme_use("clam") # You can try other themes like 'alt', 'default', 'classic'

        # Input Type Selection Frame
        self.input_type_frame = ttk.Frame(self.root, padding="10 0 10 10")
        self.input_type_frame.pack(pady=(10,0), padx=10, fill='x')

        self.input_type_label = ttk.Label(self.input_type_frame, text="Input Type:")
        self.input_type_label.pack(side=tk.LEFT, padx=(0, 10))

        self.input_type_var = tk.StringVar(value="website") # Default to website

        self.website_radio = ttk.Radiobutton(self.input_type_frame, text="Website URL", variable=self.input_type_var, value="website")
        self.website_radio.pack(side=tk.LEFT, padx=5)

        self.sitemap_radio = ttk.Radiobutton(self.input_type_frame, text="Sitemap URL", variable=self.input_type_var, value="sitemap")
        self.sitemap_radio.pack(side=tk.LEFT, padx=5)

        # Input Frame
        self.input_frame = ttk.Frame(self.root, padding="10")
        self.input_frame.pack(pady=10, padx=10, fill='x')

        self.url_label = ttk.Label(self.input_frame, text="Website URL:")
        self.url_label.pack(side=tk.LEFT, padx=(0, 5))

        self.url_entry = ttk.Entry(self.input_frame, width=40)
        self.url_entry.pack(side=tk.LEFT, expand=True, fill='x', padx=(0, 5))

        self.crawl_button = ttk.Button(self.input_frame, text="Start Crawl", command=self.start_crawl_thread)
        self.crawl_button.pack(side=tk.LEFT)

        # --- Settings Button ---
        self.settings_button = ttk.Button(self.input_frame, text="Settings", command=self.open_settings)
        self.settings_button.pack(side=tk.LEFT, padx=(5, 0))
        # --- End Settings Button ---

        # Output Area
        self.output_frame = ttk.Frame(self.root, padding="10")
        self.output_frame.pack(pady=10, padx=10, fill='both', expand=True)

        self.output_label = ttk.Label(self.output_frame, text="Crawling Log & Results:")
        self.output_label.pack(anchor='w')

        self.output_text = scrolledtext.ScrolledText(self.output_frame, wrap=tk.WORD, state='disabled', height=15)
        self.output_text.pack(fill='both', expand=True, pady=(5, 0))

        # --- Progress Bar ---
        self.progress_bar = ttk.Progressbar(self.output_frame, orient="horizontal", length=100, mode="determinate")
        self.progress_bar.pack(fill='x', pady=(5, 0))
        # --- End Progress Bar ---

        # Status Bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W, padding="2 5")
        self.status_bar.pack(side=tk.BOTTOM, fill='x')

    def log_message(self, message):
        """Logs a message to the output text area."""
        self.output_text.config(state='normal')
        self.output_text.insert(tk.END, f"{time.strftime('%H:%M:%S')} - {message}\n")
        self.output_text.see(tk.END) # Scroll to the end
        self.output_text.config(state='disabled')
        self.root.update_idletasks() # Update the GUI immediately

    def safe_log_message(self, message):
        """Safely logs a message from any thread."""
        self.root.after(0, self.log_message, message)

    def set_status(self, status):
        """Sets the status bar message."""
        self.status_var.set(status)
        self.root.update_idletasks()

    def safe_set_status(self, status):
        """Safely sets the status bar message from any thread."""
        self.root.after(0, self.set_status, status)

    # --- Progress Bar Update ---
    def safe_update_progress(self, value, maximum):
        """Safely updates the progress bar from any thread."""
        self.root.after(0, self._update_progress, value, maximum)

    def _update_progress(self, value, maximum):
        """Internal method to update progress bar."""
        if maximum > 0:
            self.progress_bar['maximum'] = maximum
            self.progress_bar['value'] = value
        else:
            self.progress_bar['value'] = 0
        self.root.update_idletasks()
    # --- End Progress Bar Update ---

    def safe_enable_button(self):
        """Safely re-enables the crawl button from any thread."""
        self.root.after(0, lambda: self.crawl_button.config(state='normal'))
        self.root.after(0, lambda: self.settings_button.config(state='normal')) # Also enable settings button

    def start_crawl_thread(self):
        """Starts the crawling process in a separate thread to avoid freezing the GUI."""
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a website URL.")
            return

        if not url.startswith(("http://", "https://")):
            if not (self.input_type_var.get() == "website" and url.startswith("file://")): # Allow file:// for single website
                 messagebox.showwarning("Input Error", "Please enter a valid URL (e.g., http://example.com or file:///path/to/file.html).")
                 return

        self.crawl_button.config(state='disabled')
        self.settings_button.config(state='disabled') # Disable settings during crawl
        self.set_status(f"Starting crawl for {url}...")
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', tk.END) # Clear previous logs
        self.output_text.config(state='disabled')
        self.safe_update_progress(0, 0) # Reset progress bar

        # Use threading to run the crawl function
        thread = threading.Thread(target=self._run_crawl_in_thread, args=(self.input_type_var.get(), url))
        thread.daemon = True # Allows the app to exit even if the thread is running
        thread.start()

    def _run_crawl_in_thread(self, input_type, url):
        """Sets up asyncio loop and runs the appropriate async crawl function."""
        print(f"DEBUG: _run_crawl_in_thread received input_type='{input_type}', url='{url}'")
        loop = None # Initialize loop to None
        try:
            # --- Create Config Objects from Settings ---
            browser_args = {
                "headless": self.headless_mode.get()
            }
            user_agent = self.user_agent_str.get()
            if user_agent: # Only add user_agent if it's not empty
                browser_args["user_agent"] = user_agent

            browser_config = BrowserConfig(**browser_args)

            # NOTE: max_depth and max_pages are used within the crawl functions below
            # --- End Create Config Objects ---

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            if input_type == "sitemap":
                print("DEBUG: Entering sitemap block.")
                loop.run_until_complete(self.run_crawl_sitemap(url, browser_config)) # Pass browser_config
            elif input_type == "website":
                print("DEBUG: Entering website block.")
                loop.run_until_complete(self.run_crawl_website(url, browser_config)) # Pass browser_config, RENAMED
        except Exception as e:
            error_msg = f"An error occurred setting up/running the crawl: {e}"
            import traceback
            traceback.print_exc() # Print full traceback to console for debugging
            self.safe_log_message(error_msg)
            self.safe_set_status("Error during crawl setup.")
            self.root.after(0, lambda: messagebox.showerror("Crawl Error", error_msg))
        finally:
            # Ensure the asyncio loop created in this thread is closed
            if loop and not loop.is_closed():
                loop.close()
                print("DEBUG: Closed asyncio loop in thread.") # Add debug print
            self.safe_enable_button()
            self.safe_update_progress(0, 0) # Reset progress bar on finish/error

    def _sanitize_filename(self, url, is_sitemap=False):
        """Creates a safe filename from a URL."""
        # Remove http(s)://
        name = re.sub(r'^https?://', '', url)
        # Replace invalid filename characters with underscores
        name = re.sub(r'[\\/:*?"<>|]', '_', name)
        # Add prefix for sitemap
        prefix = "sitemap_" if is_sitemap else ""
        # Truncate if too long
        max_len = 80 if is_sitemap else 100
        if len(name) > max_len:
            name = name[:max_len]
        # Add timestamp and extension
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        return f"{prefix}{name}_{timestamp}.md"

    def _fetch_sitemap(self, sitemap_url):
        """Fetches the sitemap content."""
        self.safe_log_message(f"Fetching sitemap: {sitemap_url}")
        try:
            headers = {'User-Agent': 'Mozilla/5.0'} # Be a good citizen
            response = requests.get(sitemap_url, headers=headers, timeout=30)
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
            return response.text
        except requests.exceptions.RequestException as e:
            self.safe_log_message(f"Failed to fetch sitemap {sitemap_url}: {e}")
            raise # Re-raise the exception to be caught by the caller

    def _extract_urls_from_sitemap(self, sitemap_content, base_url):
        """Extracts URLs from sitemap XML content. Handles sitemap index files."""
        urls = []
        sitemap_indices = []
        try:
            # Parse XML safely
            tree = ET.parse(io.StringIO(sitemap_content))
            root = tree.getroot()
            namespace = root.tag.split('}')[0] + '}' if '}' in root.tag else ''

            # Check if it's a sitemap index
            if root.tag == f'{namespace}sitemapindex':
                self.safe_log_message("Detected sitemap index. Fetching nested sitemaps...")
                for sitemap in root.findall(f'{namespace}sitemap'):
                    loc = sitemap.find(f'{namespace}loc')
                    if loc is not None and loc.text:
                        # Ensure URL is absolute
                        nested_sitemap_url = urljoin(base_url, loc.text.strip())
                        sitemap_indices.append(nested_sitemap_url)
            # Otherwise, assume it's a URL set
            elif root.tag == f'{namespace}urlset':
                for url_element in root.findall(f'{namespace}url'):
                    loc = url_element.find(f'{namespace}loc')
                    if loc is not None and loc.text:
                         # Ensure URL is absolute
                        absolute_url = urljoin(base_url, loc.text.strip())
                        urls.append(absolute_url)
            else:
                 self.safe_log_message(f"Warning: Unknown root tag in sitemap: {root.tag}")

        except ET.ParseError as e:
            self.safe_log_message(f"Error parsing sitemap XML: {e}")
            # Optionally raise e if parsing failure should stop the process

        # Process nested sitemaps if found
        for index_url in sitemap_indices:
            try:
                nested_content = self._fetch_sitemap(index_url)
                nested_urls, _ = self._extract_urls_from_sitemap(nested_content, index_url)
                urls.extend(nested_urls)
            except Exception as e:
                self.safe_log_message(f"Failed to process nested sitemap {index_url}: {e}")
                # Continue with other URLs even if one nested sitemap fails

        return urls, sitemap_indices # Return both extracted URLs and index URLs found

    async def fetch_sitemap_urls(self, sitemap_url: str) -> list[str]:
        """Fetches and parses sitemap URL(s) to extract page URLs."""
        urls = set()
        urls_to_process = [sitemap_url]
        processed_sitemaps = set()
        self.safe_log_message(f"Fetching sitemap index/URLs from: {sitemap_url}")

        async with aiohttp.ClientSession() as session:
            while urls_to_process:
                current_sitemap_url = urls_to_process.pop(0)
                if current_sitemap_url in processed_sitemaps:
                    continue
                processed_sitemaps.add(current_sitemap_url)
                self.safe_log_message(f"Processing sitemap: {current_sitemap_url}")

                try:
                    async with session.get(current_sitemap_url, timeout=30) as response:
                        if response.status == 200:
                            content = await response.text()
                            # Basic XML parsing to find URLs and nested sitemaps
                            # NOTE: This is a simplified parser. For robust sitemap handling,
                            # consider using a dedicated library like 'ultimate_sitemap_parser'.
                            loc_matches = re.findall(r'<loc>(.*?)</loc>', content)
                            for loc in loc_matches:
                                loc = loc.strip()
                                if loc.endswith('.xml'): # It's a nested sitemap index
                                    if loc not in processed_sitemaps:
                                        urls_to_process.append(loc)
                                else: # It's a page URL
                                    urls.add(loc)
                            self.safe_log_message(f"Found {len(loc_matches)} potential URLs/sitemaps in {current_sitemap_url}. Total unique URLs so far: {len(urls)}")
                        else:
                            self.safe_log_message(f"Failed to fetch sitemap {current_sitemap_url}: Status {response.status}")
                except asyncio.TimeoutError:
                     self.safe_log_message(f"Timeout fetching sitemap: {current_sitemap_url}")
                except aiohttp.ClientError as e:
                     self.safe_log_message(f"HTTP Client error fetching sitemap {current_sitemap_url}: {e}")
                except Exception as e:
                    self.safe_log_message(f"Error processing sitemap {current_sitemap_url}: {e}")
                    import traceback
                    traceback.print_exc()


        self.safe_log_message(f"Finished sitemap processing. Found {len(urls)} unique page URLs.")
        return list(urls)

    async def run_crawl_website(self, url, browser_config: BrowserConfig):
        """Crawls a website starting from a given URL, respecting max_depth, using stream=True."""
        # --- Local state for this run ---
        processed_count = 0
        success_count = 0
        failed_urls = []
        output_dir = "" # Initialize local output dir
        # --- End Local state ---

        # --- Get max_depth from settings ---
        try:
            max_depth = int(self.max_depth_str.get())
            if max_depth < 0:
                 max_depth = 0
                 self.safe_log_message("Warning: Max Depth cannot be negative. Setting to 0.")
        except ValueError:
            max_depth = 1
            self.safe_log_message(f"Invalid Max Depth value: '{self.max_depth_str.get()}'. Defaulting to {max_depth}.")
        # --- End Get max_depth ---

        # --- Get max_pages limit ---
        try:
            max_pages = int(self.max_pages_str.get())
            if max_pages < 0:
                max_pages = 0
                self.safe_log_message("Warning: Max Pages cannot be negative. Setting to 0 (unlimited).")
        except ValueError:
            max_pages = 50
            self.safe_log_message(f"Invalid Max Pages value: '{self.max_pages_str.get()}'. Defaulting to {max_pages}.")
        # --- End Get max_pages ---

        self.safe_set_status(f"Crawling website: {url} (Depth: {max_depth})...")
        self.safe_log_message(f"Starting crawl for {url} with max depth {max_depth}...")
        self.safe_update_progress(0, 0) # Reset progress, total unknown

        # --- Create Output Directory and set local output_dir ---
        try:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc
            if domain.startswith('www.'):
                domain = domain[4:]
            sanitized_domain = re.sub(r'[\\/:*?"<>|.]', '_', domain)
            if parsed_url.scheme == 'file':
               sanitized_domain = "local_files_knowledgebase"
               self.safe_log_message("Using 'local_files_knowledgebase' for local file output directory.")

            output_dir = f"{sanitized_domain}_knowledgebase"
            os.makedirs(output_dir, exist_ok=True)
            self.safe_log_message(f"Saving results to directory: {output_dir}")
        except Exception as e:
            self.safe_log_message(f"Warning: Could not create output directory based on URL '{url}'. Using default. Error: {e}")
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output_dir = f"crawl_results_website_{timestamp}"
            os.makedirs(output_dir, exist_ok=True)
            self.safe_log_message(f"Saving results to fallback directory: {output_dir}")
        # --- End Create Output Directory ---

        try:
            # --- Create Deep Crawl Strategy ---           
            deep_strategy = BFSDeepCrawlStrategy(
                max_depth=max_depth
                # Note: max_pages might not be a param here, handle manually if needed later
            )
            # --- End Deep Crawl Strategy ---
            
            # --- Create CrawlerRunConfig with stream=True and the strategy ---
            run_config = CrawlerRunConfig(
                cache_mode=CacheMode.ENABLED,
                stream=True, # Enable streaming results
                deep_crawl_strategy=deep_strategy # Set the explicit strategy
            )
            # --- End CrawlerRunConfig ---

            # --- Initialize Crawler and run with async for ---
            self.safe_log_message("DEBUG: Initializing AsyncWebCrawler for streaming deep crawl.")
            async with AsyncWebCrawler(config=browser_config) as crawler:
                # Pass config with strategy, but NOT max_depth/max_pages directly to arun
                self.safe_log_message(f"DEBUG: Calling crawler.arun with config='{run_config}' (containing deep strategy), url='{url}'")

                # Iterate over the async generator returned by arun with stream=True and deep_crawl_strategy
                async for result in await crawler.arun(url=url, config=run_config):
                    processed_count += 1
                    self.safe_set_status(f"Processed page {processed_count}...")
                    self.safe_update_progress(processed_count, 0)

                    if result.success:
                        success_count += 1
                        filename = self._sanitize_filename(result.url)
                        filepath = os.path.join(output_dir, filename)
                        try:
                            with open(filepath, "w", encoding="utf-8") as f:
                                f.write(f"# Content from: {result.url}\n\n")
                                f.write(result.markdown)
                        except IOError as e:
                            self.safe_log_message(f"({processed_count}) Error saving {result.url}: {e}")
                            failed_urls.append((result.url, f"File save error: {e}"))
                    else:
                        self.safe_log_message(f"({processed_count}) Failed: {result.url} (Status: {result.status_code}, Error: {result.error_message})")
                        failed_urls.append((result.url, f"Status: {result.status_code}, Error: {result.error_message}"))

                self.safe_log_message(f"Crawler finished streaming {processed_count} results.")
            # --- End Crawler run ---

        except PlaywrightError as e:
             error_msg = f"Playwright error during website crawl: {e}"
             self.safe_log_message(error_msg)
             self.safe_set_status("Playwright Error.")
             self.root.after(0, lambda: messagebox.showerror("Playwright Error", f"A Playwright error occurred: {e}\nCheck browser installation and permissions."))
        except TypeError as e:
             # Catch potential TypeError if on_result is not a valid parameter for AsyncWebCrawler
             error_msg = f"Configuration error initializing crawler (possibly hook parameter): {e}"
             self.safe_log_message(error_msg)
             self.safe_set_status("Crawler Configuration Error.")
             self.root.after(0, lambda: messagebox.showerror("Configuration Error", f"{error_msg}\nCheck AsyncWebCrawler initialization."))
             import traceback
             traceback.print_exc()
        except ImportError as e:
             error_msg = f"Import error during website crawl execution: {e}"
             self.safe_log_message(error_msg)
             self.safe_set_status("Import Error.")
             self.root.after(0, lambda: messagebox.showerror("Import Error", f"A required module could not be imported: {e}"))
        except Exception as e:
            error_msg = f"An unexpected error occurred during website crawl: {e}"
            import traceback
            traceback.print_exc() # Print full traceback to console
            self.safe_log_message(error_msg)
            self.safe_set_status("Unexpected Error during website crawl.")
            self.root.after(0, lambda: messagebox.showerror("Crawl Error", error_msg))
        finally:
            # Final summary log using local counters updated during the loop
            summary_message = f"Website crawl finished. Pages processed: {processed_count}. Success: {success_count}. Failed: {len(failed_urls)}."
            self.safe_log_message("-" * 20)
            self.safe_log_message(summary_message)
            if failed_urls:
                self.safe_log_message("Failed URLs/Errors:")
                max_failures_to_log = 10
                for i, (url, reason) in enumerate(failed_urls):
                    if i >= max_failures_to_log:
                        self.safe_log_message(f"... (logged {max_failures_to_log} failures)")
                        break
                    self.safe_log_message(f"- {url} : {reason}")
            self.safe_set_status(summary_message)
            self.safe_update_progress(processed_count, 0) # Final update

    async def run_crawl_sitemap(self, sitemap_url, browser_config: BrowserConfig):
        """Fetches URLs from a sitemap and crawls them using arun_many."""
        self.safe_set_status("Fetching URLs from sitemap...")
        urls_to_crawl = await self.fetch_sitemap_urls(sitemap_url)

        if not urls_to_crawl:
            self.safe_log_message("No URLs found in the sitemap or failed to fetch.")
            self.safe_set_status("Sitemap crawl failed: No URLs.")
            return

        # Apply max_pages limit if set
        try:
            max_pages = int(self.max_pages_str.get())
            if max_pages > 0 and len(urls_to_crawl) > max_pages:
                self.safe_log_message(f"Limiting crawl to {max_pages} URLs (found {len(urls_to_crawl)}).")
                urls_to_crawl = urls_to_crawl[:max_pages]
        except ValueError:
            self.safe_log_message(f"Invalid Max Pages value: '{self.max_pages_str.get()}'. Using all {len(urls_to_crawl)} URLs.")


        total_urls = len(urls_to_crawl)
        self.safe_set_status(f"Crawling {total_urls} URLs from sitemap...")
        self.safe_log_message(f"Starting crawl for {total_urls} URLs found in sitemap...")
        self.safe_update_progress(0, total_urls)


        # --- Create Output Directory based on Domain Name ---
        try:
            parsed_url = urlparse(sitemap_url)
            domain = parsed_url.netloc
            # Remove www. if it exists
            if domain.startswith('www.'):
                domain = domain[4:]
            # Sanitize domain for directory name (replace dots, etc.)
            sanitized_domain = re.sub(r'[\\/:*?"<>|.]', '_', domain)
            output_dir = f"{sanitized_domain}_knowledgebase"
        except Exception as e:
            self.safe_log_message(f"Warning: Could not parse domain from sitemap URL '{sitemap_url}'. Using default naming. Error: {e}")
            # Fallback to timestamped name if parsing fails
            output_dir = f"crawl_results_sitemap_{time.strftime('%Y%m%d_%H%M%S')}"
        # --- End Create Output Directory ---

        os.makedirs(output_dir, exist_ok=True)
        self.safe_log_message(f"Saving results to directory: {output_dir}")

        processed_count = 0
        success_count = 0
        failed_urls = []

        try:
            # --- Create CrawlerRunConfig for arun_many ---
            run_config = CrawlerRunConfig(
                 cache_mode=CacheMode.ENABLED # Example
                 # Add other relevant CrawlerRunConfig options here
            )
            # --- End CrawlerRunConfig ---

            async with AsyncWebCrawler(config=browser_config) as crawler:
                # arun_many returns an async iterator
                results_iterator = await crawler.arun_many(urls=urls_to_crawl, config=run_config) # Pass run_config, ADD await

                # Check if the returned object is an async iterator
                if not isinstance(results_iterator, AsyncIterator):
                     self.safe_log_message("Error: arun_many did not return an async iterator.")
                     self.safe_set_status("Crawl Error: Invalid iterator.")
                     # Handle the case where results_iterator is maybe a list or None
                     if isinstance(results_iterator, list):
                          # Process as a list if it accidentally returned one
                          results = results_iterator
                          for result in results:
                                processed_count += 1
                                if result.success:
                                     success_count += 1
                                     filename = self._sanitize_filename(result.url)
                                     filepath = os.path.join(output_dir, filename)
                                     try:
                                          with open(filepath, "w", encoding="utf-8") as f:
                                               f.write(f"# Content from: {result.url}\n\n")
                                               f.write(result.markdown)
                                          self.safe_log_message(f"({processed_count}/{total_urls}) Saved: {filepath}")
                                     except IOError as e:
                                          self.safe_log_message(f"({processed_count}/{total_urls}) Error saving {result.url}: {e}")
                                          failed_urls.append((result.url, f"File save error: {e}"))
                                else:
                                     self.safe_log_message(f"({processed_count}/{total_urls}) Failed: {result.url} (Status: {result.status_code}, Error: {result.error_message})")
                                     failed_urls.append((result.url, f"Status: {result.status_code}, Error: {result.error_message}"))
                                self.safe_update_progress(processed_count, total_urls)
                                self.safe_set_status(f"Crawling sitemap... {processed_count}/{total_urls}")
                     else:
                           # Handle other unexpected return types
                           self.safe_log_message(f"Error: Unexpected return type from arun_many: {type(results_iterator)}")
                           self.safe_set_status("Crawl Error: Unexpected return type.")
                     return # Exit the function as we cannot iterate

                # Process results iteratively
                async for result in results_iterator:
                    processed_count += 1
                    if result.success:
                        success_count += 1
                        filename = self._sanitize_filename(result.url)
                        filepath = os.path.join(output_dir, filename)
                        try:
                            with open(filepath, "w", encoding="utf-8") as f:
                                f.write(f"# Content from: {result.url}\n\n")
                                f.write(result.markdown)
                            # Log success minimally during iteration
                            # self.safe_log_message(f"({processed_count}/{total_urls}) Saved: {filepath}")
                        except IOError as e:
                            self.safe_log_message(f"({processed_count}/{total_urls}) Error saving {result.url}: {e}")
                            failed_urls.append((result.url, f"File save error: {e}"))
                    else:
                        self.safe_log_message(f"({processed_count}/{total_urls}) Failed: {result.url} (Status: {result.status_code}, Error: {result.error_message})")
                        failed_urls.append((result.url, f"Status: {result.status_code}, Error: {result.error_message}"))

                    # Update progress and status
                    self.safe_update_progress(processed_count, total_urls)
                    self.safe_set_status(f"Crawling sitemap... {processed_count}/{total_urls}")


        except PlaywrightError as e:
             error_msg = f"Playwright error during sitemap crawl: {e}"
             self.safe_log_message(error_msg)
             self.safe_set_status("Playwright Error.")
             self.root.after(0, lambda: messagebox.showerror("Playwright Error", f"A Playwright error occurred: {e}\nCheck browser installation and permissions."))
        except ImportError as e:
             error_msg = f"Import error during sitemap crawl execution: {e}"
             self.safe_log_message(error_msg)
             self.safe_set_status("Import Error.")
             self.root.after(0, lambda: messagebox.showerror("Import Error", f"A required module could not be imported: {e}"))
        except Exception as e:
            error_msg = f"An unexpected error occurred during sitemap crawl: {e}"
            import traceback
            traceback.print_exc()
            self.safe_log_message(error_msg)
            self.safe_set_status("Unexpected Error during sitemap crawl.")
            self.root.after(0, lambda: messagebox.showerror("Crawl Error", error_msg))
        finally:
            # Final summary log
            summary_message = f"Sitemap crawl finished. Total URLs processed: {processed_count}. Success: {success_count}. Failed: {len(failed_urls)}."
            self.safe_log_message("-" * 20)
            self.safe_log_message(summary_message)
            if failed_urls:
                self.safe_log_message("Failed URLs:")
                for url, reason in failed_urls:
                    self.safe_log_message(f"- {url} : {reason}")
            self.safe_set_status(summary_message)
            self.safe_update_progress(processed_count, total_urls) # Ensure progress bar is full/final

    # --- Settings Window ---
    def open_settings(self):
        """Opens the settings dialog window."""
        settings_win = tk.Toplevel(self.root)
        settings_win.title("Crawler Settings")
        settings_win.geometry("400x250")
        settings_win.transient(self.root) # Keep on top of the main window
        settings_win.grab_set() # Modal behavior

        frame = ttk.Frame(settings_win, padding="15")
        frame.pack(expand=True, fill="both")

        # Validation command for integer entries
        validate_int_cmd = (frame.register(self.validate_integer), '%P') # %P is the value if edit is allowed

        # --- Browser Settings ---
        browser_frame = ttk.LabelFrame(frame, text="Browser Settings", padding="10")
        browser_frame.pack(fill="x", pady=5)

        ttk.Checkbutton(browser_frame, text="Run Headless (no visible browser)", variable=self.headless_mode).pack(anchor="w", pady=2)

        ua_frame = ttk.Frame(browser_frame)
        ua_frame.pack(fill="x", pady=2)
        ttk.Label(ua_frame, text="User Agent (leave blank for default):").pack(side="left", anchor="w")
        ttk.Entry(ua_frame, textvariable=self.user_agent_str, width=30).pack(side="left", expand=True, fill="x", padx=5)


        # --- Crawler Run Settings ---
        run_frame = ttk.LabelFrame(frame, text="Crawler Run Settings", padding="10")
        run_frame.pack(fill="x", pady=5)

        depth_frame = ttk.Frame(run_frame)
        depth_frame.pack(fill="x", pady=2)
        ttk.Label(depth_frame, text="Max Crawl Depth (for deep crawls):").pack(side="left", anchor="w")
        ttk.Entry(
            depth_frame,
            textvariable=self.max_depth_str,
            width=5,
            validate='key', # Validate on key press
            validatecommand=validate_int_cmd
        ).pack(side="left", padx=5)

        pages_frame = ttk.Frame(run_frame)
        pages_frame.pack(fill="x", pady=2)
        ttk.Label(pages_frame, text="Max Pages (for sitemap/deep crawls, 0=unlimited):").pack(side="left", anchor="w")
        ttk.Entry(
             pages_frame,
             textvariable=self.max_pages_str,
             width=5,
             validate='key',
             validatecommand=validate_int_cmd
        ).pack(side="left", padx=5)

        # --- Close Button ---
        button_frame = ttk.Frame(frame, padding="10 0 0 0")
        button_frame.pack(side="bottom", fill="x")
        ttk.Button(button_frame, text="Save & Close", command=settings_win.destroy).pack()

        # Center the window
        settings_win.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - (settings_win.winfo_width() // 2)
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - (settings_win.winfo_height() // 2)
        settings_win.geometry(f"+{x}+{y}")

        settings_win.wait_window() # Wait until the window is closed

    def validate_integer(self, value_if_allowed):
        """Validation function for integer entry fields."""
        if value_if_allowed == "":
            return True # Allow empty string
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False
    # --- End Settings Window ---


if __name__ == "__main__":
    root = tk.Tk()
    app = CrawlerApp(root)
    root.mainloop() 