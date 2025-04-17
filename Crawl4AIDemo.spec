# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files, collect_submodules
import os
from pathlib import Path

# Root of the project - use absolute path
project_root = os.path.abspath('.')

# Get the absolute path to the site-packages directory
site_packages = os.path.join(project_root, '.venv', 'Lib', 'site-packages')

# Explicitly specify the data paths
fake_http_header_dir = os.path.join(site_packages, 'fake_http_header')
fake_http_header_data_dir = os.path.join(fake_http_header_dir, 'data')

# All fake_http_header data files
fake_http_header_data_files = [
    (os.path.join(fake_http_header_data_dir, f), os.path.join('fake_http_header', 'data')) 
    for f in os.listdir(fake_http_header_data_dir) 
    if os.path.isfile(os.path.join(fake_http_header_data_dir, f))
]

# Add all the necessary modules as hidden imports
hidden_imports = [
    # fake_http_header modules
    'fake_http_header',
    'fake_http_header.constants',
    'fake_http_header.fake_http_header',
    'fake_http_header.data',
    'fake_http_header.data_import',
    
    # importlib modules needed
    'importlib',
    'importlib.resources',
    'importlib.resources._common',
    'importlib.resources._itertools',
    'importlib.resources._adapters',
    'importlib.resources.abc',
    'importlib.abc',
    'importlib.metadata',
    'json',
]

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Base directories
        ('.venv\\Lib\\site-packages\\crawl4ai', 'crawl4ai'),
        (fake_http_header_dir, 'fake_http_header'),
        
        # Add all data files explicitly
        *fake_http_header_data_files,
    ],
    hiddenimports=hidden_imports + collect_submodules('fake_http_header'),
    hookspath=['hooks'],
    hooksconfig={},
    runtime_hooks=['runtime_hook.py'],  # Add our runtime hook
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Crawl4AIDemo',
    debug=True,  # Keep debug for now
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # Keep console for debugging
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Crawl4AIDemo',
)
