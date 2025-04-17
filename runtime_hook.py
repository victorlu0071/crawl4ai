"""
PyInstaller runtime hook to patch importlib.resources for fake_http_header

This hook patches the import system to handle dynamic resource loading
by fake_http_header package.
"""

import os
import sys
import importlib
import importlib.abc
import importlib.machinery
from pathlib import Path
import json

# Setup paths for the frozen application
if getattr(sys, 'frozen', False):
    # Running in PyInstaller bundle
    base_dir = Path(sys._MEIPASS)
    
    # Debug output
    print(f"PyInstaller MEIPASS: {base_dir}")
    print(f"Current sys.path: {sys.path}")
    
    # Add fake_http_header data directory to paths
    fake_http_header_dir = base_dir / '_internal' / 'fake_http_header'
    
    if fake_http_header_dir.exists():
        print(f"Found fake_http_header at {fake_http_header_dir}")
        
        # Check if data directory exists
        data_dir = fake_http_header_dir / 'data'
        if data_dir.exists():
            print(f"Found data directory at {data_dir}")
            
            # List contents of data directory for debugging
            data_files = list(data_dir.glob('*'))
            print(f"Data files: {[f.name for f in data_files]}")
            
            # Create an empty module for fake_http_header.data if it doesn't exist
            try:
                importlib.import_module('fake_http_header.data')
                print("Successfully imported fake_http_header.data")
            except ImportError:
                print("Creating fake_http_header.data module")
                # Create the module manually
                import types
                data_module = types.ModuleType('fake_http_header.data')
                sys.modules['fake_http_header.data'] = data_module
                
            # Create in-memory JSON data to work around importlib.resources issue
            # We're creating the module data directly in memory
            constants_module = None
            try:
                constants_module = importlib.import_module('fake_http_header.constants')
                print("Successfully imported fake_http_header.constants")
            except ImportError:
                print("Failed to import fake_http_header.constants - will try to patch")
            
            # If the constants module exists, try to load the JSON data directly
            if constants_module is not None:
                # Load all JSON files into memory
                json_data = {}
                for json_file in data_dir.glob('*.json'):
                    try:
                        with open(json_file, 'r', encoding='utf-8') as f:
                            json_data[json_file.stem] = json.load(f)
                            print(f"Loaded {json_file.name} into memory")
                    except Exception as e:
                        print(f"Error loading {json_file.name}: {e}")
                
                # Create a function to replace the importlib.resources.read_text
                def patched_read_text(package, resource):
                    print(f"Patched read_text called for {package}.{resource}")
                    if package == 'fake_http_header.data':
                        resource_name = resource.replace('.json', '')
                        if resource_name in json_data:
                            print(f"Returning cached JSON for {resource}")
                            return json.dumps(json_data[resource_name])
                    
                    # Fallback to original implementation
                    original_read_text = getattr(importlib.resources, '_original_read_text', None)
                    if original_read_text:
                        return original_read_text(package, resource)
                    
                    raise FileNotFoundError(f"Resource {resource} not found in package {package}")
                
                # Save original read_text and patch it
                if not hasattr(importlib.resources, '_original_read_text'):
                    importlib.resources._original_read_text = importlib.resources.read_text
                    importlib.resources.read_text = patched_read_text
                    print("Patched importlib.resources.read_text")
        else:
            print(f"WARNING: fake_http_header/data directory not found")
    else:
        print(f"WARNING: fake_http_header directory not found in _internal") 