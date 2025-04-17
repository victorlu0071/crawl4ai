"""
Utility script to help PyInstaller package the data files properly.
This will be called by the PyInstaller hook.
"""

import os
import shutil
import sys

def main():
    """Copy the fake_http_header data files to the correct location."""
    # Get the application directory
    if getattr(sys, 'frozen', False):
        # Running in PyInstaller bundle
        app_dir = os.path.dirname(sys.executable)
    else:
        # Running in normal Python environment
        app_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Source directory in development environment
    source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                             '.venv', 'Lib', 'site-packages', 'fake_http_header', 'data')
    
    # Target directory in PyInstaller bundle
    target_dir = os.path.join(app_dir, 'fake_http_header', 'data')
    
    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    # Copy all files from source to target
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        if os.path.isfile(source_file):
            shutil.copy2(source_file, target_dir)
            print(f"Copied {filename} to {target_dir}")

if __name__ == "__main__":
    main() 