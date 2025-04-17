"""Resource handler for packaged applications."""

import os
import sys
import importlib.resources
import importlib.abc
from pathlib import Path

class PyInstallerLoader:
    """Custom resource loader for PyInstaller bundles."""
    
    @staticmethod
    def patch_resource_handling():
        """Patch importlib.resources handling for PyInstaller bundles."""
        if not getattr(sys, 'frozen', False):
            # Not running in a bundle, no patching needed
            return
            
        # Determine the base path for resources
        base_path = Path(sys._MEIPASS) if hasattr(sys, '_MEIPASS') else Path(os.path.dirname(sys.executable))
        
        print(f"PyInstaller base path: {base_path}")
        print(f"Current sys.path: {sys.path}")
        
        # Ensure the fake_http_header/data directory is in the path
        fake_http_header_path = base_path / '_internal' / 'fake_http_header'
        if fake_http_header_path.exists():
            print(f"Found fake_http_header at {fake_http_header_path}")
            
            # Add parent directory to path so Python can find the module
            if str(fake_http_header_path.parent) not in sys.path:
                sys.path.insert(0, str(fake_http_header_path.parent))
                print(f"Added {fake_http_header_path.parent} to sys.path")
                
            # Check for data directory
            data_path = fake_http_header_path / 'data'
            if data_path.exists():
                print(f"Found data directory at {data_path}")
                print(f"Contents: {[f.name for f in data_path.iterdir()]}")
        else:
            print(f"WARNING: fake_http_header directory not found at {fake_http_header_path}")
            
def initialize():
    """Initialize resource handling for the application."""
    PyInstallerLoader.patch_resource_handling()
    
if __name__ == "__main__":
    initialize()
    print("Resource handler initialized.") 