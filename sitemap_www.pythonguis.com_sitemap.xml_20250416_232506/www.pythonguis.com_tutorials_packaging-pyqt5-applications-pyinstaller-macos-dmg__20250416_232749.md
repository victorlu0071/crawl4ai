# Content from: https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/

[](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PyQt5 ](https://www.pythonguis.com/pyqt5/)
  * [PyQt5 Tutorial ](https://www.pythonguis.com/pyqt5-tutorial/)
  * Basics
  * [Create a PyQt5 app](https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/)
  * [PyQt5 Signals](https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/)
  * [PyQt5 Widgets](https://www.pythonguis.com/tutorials/pyqt-basic-widgets/)
  * [PyQt5 Layouts](https://www.pythonguis.com/tutorials/pyqt-layouts/)
  * [PyQt5 Menus](https://www.pythonguis.com/tutorials/pyqt-actions-toolbars-menus/)
  * [PyQt5 Dialogs](https://www.pythonguis.com/tutorials/pyqt-dialogs/)
  * [Multi-window PyQt5](https://www.pythonguis.com/tutorials/creating-multiple-windows/)
  * Qt Designer
  * [First Qt Designer app](https://www.pythonguis.com/tutorials/first-steps-qt-creator/)
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/creating-dialogs-qt-designer/)
  * [The QResource System in PyQt5](https://www.pythonguis.com/tutorials/qresource-system/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/)
  * Plotting
  * [Plotting With PyQtGraph and PyQt5](https://www.pythonguis.com/tutorials/plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PyQt5](https://www.pythonguis.com/tutorials/plotting-matplotlib/)
  * QGraphics
  * [Vector Graphics](https://www.pythonguis.com/tutorials/pyqt-qgraphics-vector-graphics/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/qpropertyanimation/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/system-tray-mac-menu-bar-applications-pyqt/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/)
  * [Packaging for Linux](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-linux-pyinstaller/)
  * [Packaging QResources](https://www.pythonguis.com/tutorials/packaging-data-files-pyqt5-with-qresource-system/)
  * [Packaging with fbs](https://www.pythonguis.com/tutorials/packaging-pyqt5-apps-fbs/)
  * Resources
  * [Books](https://www.pythonguis.com/books/)
  * Services
  * [Consulting](https://www.pythonguis.com/hire/)
  * [1:1 Coaching](https://www.pythonguis.com/live/)
  * [Contact](https://www.pythonguis.com/contact/)
  * [About](https://www.pythonguis.com/about/)
  * Libraries
  * [PyQt6](https://www.pythonguis.com/pyqt6/)
  * [PySide6](https://www.pythonguis.com/pyside6/)
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Packaging PyQt5 applications into a macOS app with PyInstaller
Turn your PyQt5 application into a distributable app
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Mar 10 This article has been updated for 2022. PyQt5 [ Packaging and Distributing PyQt5 Applications ](https://www.pythonguis.com/pyqt5-tutorial/#packaging-and-distribution)
[ Example PyInstaller Source files ](https://downloads.pythonguis.com/DemoAppPyInstaller.zip) [ Example macOS Disk Image ](https://downloads.pythonguis.com/DemoAppMacOS.dmg)
#### [ PyQt5 Tutorial ](https://www.pythonguis.com/pyqt5-tutorial/) — [Packaging and Distributing PyQt5 Applications](https://www.pythonguis.com/pyqt5-tutorial/#packaging-and-distribution)
  * [Packaging PyQt5 applications for Windows with PyInstaller & InstallForge](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/)
  * [Packaging PyQt5 applications into a macOS app with PyInstaller](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/)
  * [Packaging PyQt5 applications for Linux with PyInstaller & fpm](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-linux-pyinstaller/)
  * [Using QResource to Package Data Files With PyInstaller and PyQt5](https://www.pythonguis.com/tutorials/packaging-data-files-pyqt5-with-qresource-system/)
  * [Packaging PyQt5 apps with fbs](https://www.pythonguis.com/tutorials/packaging-pyqt5-apps-fbs/)


This tutorial is also available for [PyQt6](https://www.pythonguis.com/tutorials/packaging-pyqt6-applications-pyinstaller-macos-dmg/) , [PySide6](https://www.pythonguis.com/tutorials/packaging-pyside6-applications-pyinstaller-macos-dmg/) and [PySide2](https://www.pythonguis.com/tutorials/packaging-pyside2-applications-pyinstaller-macos-dmg/)
There is not much fun in creating your own desktop applications if you can't share them with other people — whether than means publishing it commercially, sharing it online or just giving it to someone you know. Sharing your apps allows other people to benefit from your hard work!
The good news is there are tools available to help you do just that with your Python applications which work well with apps built using PyQt5. In this tutorial we'll look at the most popular tool for packaging Python applications: _PyInstaller_.
This tutorial is broken down into a series of steps, using _PyInstaller_ to build first simple, and then more complex PyQt5 applications into distributable macOS app bundles. You can choose to follow it through completely, or skip to the parts that are most relevant to your own project.
We finish off by building a macOS _Disk Image_ , the usual method for distributing applications on macOS.
You always need to compile your app on your target system. So, if you want to create a Mac .app you need to do this on a Mac, for an EXE you need to use Windows.
[![Example Disk Image for macOS](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/macos_disk_image.png)](https://downloads.pythonguis.com/DemoAppMacOS.dmg) _Example Disk Image Installer for macOS_
If you're impatient, you can download the [Example Disk Image for macOS](https://downloads.pythonguis.com/DemoAppMacOS.dmg) first.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Table of Contents
  * [Requirements](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#requirements)
    * [Install in virtual environment (optional)](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#install-in-virtual-environment-optional)
  * [Getting Started](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#getting-started)
  * [Building a basic app](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#building-a-basic-app)
  * [The Spec file](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#the-spec-file)
  * [Tweaking the build](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#tweaking-the-build)
    * [Naming your app](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#naming-your-app)
    * [Application icon](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#application-icon)
  * [Data files and Resources](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#data-files-and-resources)
    * [Dealing with relative paths](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#dealing-with-relative-paths)
    * [Packaging the icons](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#packaging-the-icons)
    * [Bundling data files with PyInstaller](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#bundling-data-files-with-pyinstaller)
    * [Bundling data folders](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#bundling-data-folders)
  * [Building the App bundle into a Disk Image](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#building-the-app-bundle-into-a-disk-image)
  * [Making sure the build is ready.](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#making-sure-the-build-is-ready)
  * [Creating an Disk Image](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#creating-an-disk-image)
    * [Running the installer](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#running-the-installer)
  * [Repeating the build](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#repeating-the-build)
  * [Wrapping up](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/#wrapping-up)


## Requirements
_PyInstaller_ works out of the box with PyQt5 and as of writing, current versions of _PyInstaller_ are compatible with Python 3.6+. Whatever project you're working on, you should be able to package your apps.
You can install _PyInstaller_ using `pip`.
bash ```
pip3 install PyInstaller

```

If you experience problems packaging your apps, your first step should _always_ be to update your _PyInstaller_ and _hooks package_ the latest versions using
bash ```
pip3 install --upgrade PyInstaller pyinstaller-hooks-contrib

```

The _hooks_ module contains package-specific packaging instructions for _PyInstaller_ which is updated regularly.
### Install in virtual environment (optional)
You can also opt to install PyQt5 and _PyInstaller_ in a virtual environment (or your applications virtual environment) to keep your environment clean.
bash ```
python3 -m venv packenv

```

Once created, activate the virtual environment by running from the command line —
bash ```
call packenv\scripts\activate.bat

```

Finally, install the required libraries. For PyQt5 you would use —
python ```
pip3 install PyQt5 PyInstaller

```

## Getting Started
It's a good idea to start packaging your application _from the very beginning_ so you can confirm that packaging is still working as you develop it. This is particularly important if you add additional dependencies. If you only think about packaging at the end, it can be difficult to debug exactly _where_ the problems are.
For this example we're going to start with a simple skeleton app, which doesn't do anything interesting. Once we've got the basic packaging process working, we'll extend the application to include icons and data files. We'll confirm the build as we go along.
To start with, create a new folder for your application and then add the following skeleton app in a file named `app.py`. You can also [download the source code and associated files](https://downloads.pythonguis.com/DemoAppPyInstaller.zip)
python ```
from PyQt5 import QtWidgets
import sys
class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Hello World")
    l = QtWidgets.QLabel("My simple app.")
    l.setMargin(10)
    self.setCentralWidget(l)
    self.show()
if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  w = MainWindow()
  app.exec()

```

This is a basic bare-bones application which creates a custom `QMainWindow` and adds a simple widget `QLabel` to it. You can run this app as follows.
bash ```
python app.py

```

This should produce the following window (on macOS).
![Simple skeleton app in PyQt5](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/basic_app.png) _Simple skeleton app in PyQt5_
## Building a basic app
Now we have our simple application skeleton in place, we can run our first build test to make sure everything is working.
Open your terminal (command prompt) and navigate to the folder containing your project. You can now run the following command to run the _PyInstaller_ build.
python ```
pyinstaller --windowed app.py

```

The `--windowed` flag is necessary to tell PyInstaller to build a macOS `.app` bundle.
You'll see a number of messages output, giving debug information about what _PyInstaller_ is doing. These are useful for debugging issues in your build, but can otherwise be ignored. The output that I get for running the command on my system is shown below.
bash ```
martin@MacBook-Pro pyqt5 % pyinstaller --windowed app.py
74 INFO: PyInstaller: 4.8
74 INFO: Python: 3.9.9
83 INFO: Platform: macOS-10.15.7-x86_64-i386-64bit
84 INFO: wrote /Users/martin/app/pyqt5/app.spec
87 INFO: UPX is not available.
88 INFO: Extending PYTHONPATH with paths
['/Users/martin/app/pyqt5']
447 INFO: checking Analysis
451 INFO: Building because inputs changed
452 INFO: Initializing module dependency graph...
455 INFO: Caching module graph hooks...
463 INFO: Analyzing base_library.zip ...
3914 INFO: Processing pre-find module path hook distutils from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks/pre_find_module_path/hook-distutils.py'.
3917 INFO: distutils: retargeting to non-venv dir '/usr/local/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/lib/python3.9'
6928 INFO: Caching module dependency graph...
7083 INFO: running Analysis Analysis-00.toc
7091 INFO: Analyzing /Users/martin/app/pyqt5/app.py
7138 INFO: Processing module hooks...
7139 INFO: Loading module hook 'hook-PyQt6.QtWidgets.py' from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks'...
7336 INFO: Loading module hook 'hook-xml.etree.cElementTree.py' from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks'...
7337 INFO: Loading module hook 'hook-lib2to3.py' from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks'...
7360 INFO: Loading module hook 'hook-PyQt6.QtGui.py' from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks'...
7397 INFO: Loading module hook 'hook-PyQt6.QtCore.py' from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks'...
7422 INFO: Loading module hook 'hook-encodings.py' from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks'...
7510 INFO: Loading module hook 'hook-distutils.util.py' from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks'...
7513 INFO: Loading module hook 'hook-pickle.py' from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks'...
7515 INFO: Loading module hook 'hook-heapq.py' from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks'...
7517 INFO: Loading module hook 'hook-difflib.py' from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks'...
7519 INFO: Loading module hook 'hook-PyQt6.py' from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks'...
7564 INFO: Loading module hook 'hook-multiprocessing.util.py' from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks'...
7565 INFO: Loading module hook 'hook-sysconfig.py' from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks'...
7574 INFO: Loading module hook 'hook-xml.py' from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks'...
7677 INFO: Loading module hook 'hook-distutils.py' from '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks'...
7694 INFO: Looking for ctypes DLLs
7712 INFO: Analyzing run-time hooks ...
7715 INFO: Including run-time hook '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks/rthooks/pyi_rth_subprocess.py'
7719 INFO: Including run-time hook '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks/rthooks/pyi_rth_pkgutil.py'
7722 INFO: Including run-time hook '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks/rthooks/pyi_rth_multiprocessing.py'
7726 INFO: Including run-time hook '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks/rthooks/pyi_rth_inspect.py'
7727 INFO: Including run-time hook '/usr/local/lib/python3.9/site-packages/PyInstaller/hooks/rthooks/pyi_rth_pyqt6.py'
7736 INFO: Looking for dynamic libraries
7977 INFO: Looking for eggs
7977 INFO: Using Python library /usr/local/Cellar/python@3.9/3.9.9/Frameworks/Python.framework/Versions/3.9/Python
7987 INFO: Warnings written to /Users/martin/app/pyqt5/build/app/warn-app.txt
8019 INFO: Graph cross-reference written to /Users/martin/app/pyqt5/build/app/xref-app.html
8032 INFO: checking PYZ
8035 INFO: Building because toc changed
8035 INFO: Building PYZ (ZlibArchive) /Users/martin/app/pyqt5/build/app/PYZ-00.pyz
8390 INFO: Building PYZ (ZlibArchive) /Users/martin/app/pyqt5/build/app/PYZ-00.pyz completed successfully.
8397 INFO: EXE target arch: x86_64
8397 INFO: Code signing identity: None
8398 INFO: checking PKG
8398 INFO: Building because /Users/martin/app/pyqt5/build/app/PYZ-00.pyz changed
8398 INFO: Building PKG (CArchive) app.pkg
8415 INFO: Building PKG (CArchive) app.pkg completed successfully.
8417 INFO: Bootloader /usr/local/lib/python3.9/site-packages/PyInstaller/bootloader/Darwin-64bit/runw
8417 INFO: checking EXE
8418 INFO: Building because console changed
8418 INFO: Building EXE from EXE-00.toc
8418 INFO: Copying bootloader EXE to /Users/martin/app/pyqt5/build/app/app
8421 INFO: Converting EXE to target arch (x86_64)
8449 INFO: Removing signature(s) from EXE
8484 INFO: Appending PKG archive to EXE
8486 INFO: Fixing EXE headers for code signing
8496 INFO: Rewriting the executable's macOS SDK version (11.1.0) to match the SDK version of the Python library (10.15.6) in order to avoid inconsistent behavior and potential UI issues in the frozen application.
8499 INFO: Re-signing the EXE
8547 INFO: Building EXE from EXE-00.toc completed successfully.
8549 INFO: checking COLLECT
WARNING: The output directory "/Users/martin/app/pyqt5/dist/app" and ALL ITS CONTENTS will be REMOVED! Continue? (y/N)y
On your own risk, you can use the option `--noconfirm` to get rid of this question.
10820 INFO: Removing dir /Users/martin/app/pyqt5/dist/app
10847 INFO: Building COLLECT COLLECT-00.toc
12460 INFO: Building COLLECT COLLECT-00.toc completed successfully.
12469 INFO: checking BUNDLE
12469 INFO: Building BUNDLE because BUNDLE-00.toc is non existent
12469 INFO: Building BUNDLE BUNDLE-00.toc
13848 INFO: Moving BUNDLE data files to Resource directory
13901 INFO: Signing the BUNDLE...
16049 INFO: Building BUNDLE BUNDLE-00.toc completed successfully.

```

If you look in your folder you'll notice you now have two new folders `dist` and `build`.
![build & dist folders created by PyInstaller](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/build_dist_folders.png) _build & dist folders created by PyInstaller_
Below is a truncated listing of the folder content, showing the `build` and `dist` folders.
bash ```
.
├── app.py
├── app.spec
├── build
│   └── app
│     ├── Analysis-00.toc
│     ├── COLLECT-00.toc
│     ├── EXE-00.toc
│     ├── PKG-00.pkg
│     ├── PKG-00.toc
│     ├── PYZ-00.pyz
│     ├── PYZ-00.toc
│     ├── app
│     ├── app.pkg
│     ├── base_library.zip
│     ├── warn-app.txt
│     └── xref-app.html
└── dist
  ├── app
  │  ├── libcrypto.1.1.dylib
  │  ├── PyQt5
  │  ...
  │  ├── app
  │  └── Qt5Core
  └── app.app

```

The `build` folder is used by _PyInstaller_ to collect and prepare the files for bundling, it contains the results of analysis and some additional logs. For the most part, you can ignore the contents of this folder, unless you're trying to debug issues.
The `dist` (for "distribution") folder contains the files to be distributed. This includes your application, bundled as an executable file, together with any associated libraries (for example PyQt5) and binary `.so` files.
Since we provided the `--windowed` flag above, PyInstaller has actually created _two_ builds for us. The folder `app` is a simple folder containing everything you need to be able to run your app. PyInstaller also creates an app bundle `app.app` which is what you will usually distribute to users.
The `app` folder is a useful debugging tool, since you can easily see the libraries and other packaged data files.
You can try running your app yourself now, either by double-clicking on the app bundle, or by running the executable file, named `app.exe` from the `dist` folder. In either case, after a short delay you'll see the familiar window of your application pop up as shown below.
![Simple app, running after being packaged](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/basic_app.png) _Simple app, running after being packaged_
In the same folder as your Python file, alongside the `build` and `dist` folders _PyInstaller_ will have also created a `.spec` file. In the next section we'll take a look at this file, what it is and what it does.
## The Spec file
The `.spec` file contains the build configuration and instructions that _PyInstaller_ uses to package up your application. Every _PyInstaller_ project has a `.spec` file, which is generated based on the command line options you pass when running `pyinstaller`.
When we ran `pyinstaller` with our script, we didn't pass in anything other than the name of our Python application file and the `--windowed` flag. This means our spec file currently contains only the default configuration. If you open it, you'll see something similar to what we have below.
python ```
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['app.py'],
       pathex=[],
       binaries=[],
       datas=[],
       hiddenimports=[],
       hookspath=[],
       hooksconfig={},
       runtime_hooks=[],
       excludes=[],
       win_no_prefer_redirects=False,
       win_private_assemblies=False,
       cipher=block_cipher,
       noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
       cipher=block_cipher)
exe = EXE(pyz,
     a.scripts,
     [],
     exclude_binaries=True,
     name='app',
     debug=False,
     bootloader_ignore_signals=False,
     strip=False,
     upx=True,
     console=False,
     disable_windowed_traceback=False,
     target_arch=None,
     codesign_identity=None,
     entitlements_file=None )
coll = COLLECT(exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='app')
app = BUNDLE(coll,
       name='app.app',
       icon=None,
       bundle_identifier=None)

```

The first thing to notice is that this is a Python file, meaning you can edit it and use Python code to calculate values for the settings. This is mostly useful for complex builds, for example when you are targeting different platforms and want to conditionally define additional libraries or dependencies to bundle.
Because we used the `--windowed` command line flag, the `EXE(console=)` attribute is set to `False`. If this is `True` a console window will be shown when your app is launched -- not what you usually want for a GUI application.
Once a `.spec` file has been generated, you can pass this to `pyinstaller` instead of your script to repeat the previous build process. Run this now to rebuild your executable.
bash ```
pyinstaller app.spec

```

The resulting build will be identical to the build used to generate the `.spec` file (assuming you have made no changes). For many _PyInstaller_ configuration changes you have the option of passing command-line arguments, or modifying your existing `.spec` file. Which you choose is up to you.
## Tweaking the build
So far we've created a simple first build of a very basic application. Now we'll look at a few of the most useful options that _PyInstaller_ provides to tweak our build. Then we'll go on to look at building more complex applications.
### Naming your app
One of the simplest changes you can make is to provide a proper "name" for your application. By default the app takes the name of your source file (minus the extension), for example `main` or `app`. This isn't usually what you want.
You can provide a nicer name for _PyInstaller_ to use for the app (and `dist` folder) by editing the `.spec` file to add a `name=` under the EXE, COLLECT and BUNDLE blocks.
python ```
exe = EXE(pyz,
     a.scripts,
     [],
     exclude_binaries=True,
     name='Hello World',
     debug=False,
     bootloader_ignore_signals=False,
     strip=False,
     upx=True,
     console=False
     )
coll = COLLECT(exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='Hello World')
app = BUNDLE(coll,
       name='Hello World.app',
       icon=None,
       bundle_identifier=None)

```

The name under EXE is the name of the _executable file_ , the name under BUNDLE is the name of the app bundle.
Alternatively, you can re-run the `pyinstaller` command and pass the `-n` or `--name` configuration flag along with your `app.py` script.
bash ```
pyinstaller -n "Hello World" --windowed app.py
# or
pyinstaller --name "Hello World" --windowed app.py

```

The resulting app file will be given the name `Hello World.app` and the unpacked build placed in the folder `dist\Hello World\`.
![Application with custom name "Hello World"](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/app_name_kz1bTZt.png) _Application with custom name "Hello World"_
The name of the `.spec` file is taken from the name passed in on the command line, so this will _also_ create a new spec file for you, called `Hello World.spec` in your root folder.
Make sure you delete the old `app.spec` file to avoid getting confused editing the wrong one.
### Application icon
By default _PyInstaller_ app bundles come with the following icon in place.
![Default PyInstaller application icon, on app bundle](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/application_icon_default.png) _Default PyInstaller application icon, on app bundle_
You will probably want to customize this to make your application more recognisable. This can be done easily by passing the `--icon` command line argument, or editing the `icon=` parameter of the BUNDLE section of your `.spec` file. For macOS app bundles you need to provide an `.icns` file.
python ```
app = BUNDLE(coll,
       name='Hello World.app',
       icon='Hello World.icns',
       bundle_identifier=None)

```

To create macOS icons from images you can use [the image2icon tool](https://apps.apple.com/us/app/image2icon-make-your-own-icons/id992115977).
If you now re-run the build (by using the command line arguments, or running with your modified `.spec` file) you'll see the specified icon file is now set on your application bundle.
![Custom application icon \(a hand\) on the app bundle](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/application_icon_custom.png) _Custom application icon on the app bundle_
On macOS application icons are taken from the application bundle. If you repackage your app and run the bundle you will see your app icon on the dock!
![Custom application icon in the dock](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/application_icon_dock.png) _Custom application icon on the dock_
## Data files and Resources
So far our application consists of just a single Python file, with no dependencies. Most real-world applications a bit more complex, and typically ship with associated data files such as icons or UI design files. In this section we'll look at how we can accomplish this with PyInstaller, starting with a single file and then bundling complete folders of resources.
First let's update our app with some more buttons and add icons to each.
python ```
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QIcon
import sys
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Hello World")
    layout = QVBoxLayout()
    label = QLabel("My simple app.")
    label.setMargin(10)
    layout.addWidget(label)
    button1 = QPushButton("Hide")
    button1.setIcon(QIcon("icons/hand.png"))
    button1.pressed.connect(self.lower)
    layout.addWidget(button1)
    button2 = QPushButton("Close")
    button2.setIcon(QIcon("icons/lightning.png"))
    button2.pressed.connect(self.close)
    layout.addWidget(button2)
    container = QWidget()
    container.setLayout(layout)
    self.setCentralWidget(container)
    self.show()
if __name__ == '__main__':
  app = QApplication(sys.argv)
  w = MainWindow()
  app.exec_()

```

In the folder with this script, add a folder `icons` which contains two icons in PNG format, `hand.png` and `lightning.png`. You can create these yourself, or get them from the [source code download](https://downloads.pythonguis.com/DemoAppPyInstaller.zip) for this tutorial.
Run the script now and you will see a window showing two buttons with icons.
![Window with two icons](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/basic_app_icons2.png) _Window with two buttons with icons._
Even if you _don't_ see the icons, keep reading!
### Dealing with relative paths
There is a gotcha here, which might not be immediately apparent. To demonstrate it, open up a shell and change to the folder where our script is located. Run it with
bash ```
python3 app.py

```

If the icons are in the correct location, you should see them. Now change to the parent folder, and try and run your script again (change `<folder>` to the name of the folder your script is in). 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
bash ```
cd ..
python3 <folder>/app.py

```

![Window with two icons missing](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/basic_app_icons2_missing.png) _Window with two buttons with icons missing._
The icons _don't_ appear. What's happening?
We're using _relative_ paths to refer to our data files. These paths are relative to the _current working directory_ -- not the folder your script is in. So if you run the script from elsewhere it won't be able to find the files.
One common reason for icons not to show up, is running examples in an IDE which uses the project root as the current working directory.
This is a minor issue before the app is packaged, but once it's installed it will be started with it's _current working directory_ as the root `/` folder -- your app won't be able to find anything. We need to fix this before we go any further, which we can do by making our paths relative to _our application folder_.
In the updated code below, we define a new variable `basedir`, using `os.path.dirname` to get the containing folder of `__file__` which holds the full path of the current Python file. We then use this to build the relative paths for icons using `os.path.join()`.
Since our `app.py` file is in the root of our folder, all other paths are relative to that.
python ```
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QIcon
import sys, os
basedir = os.path.dirname(__file__)
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Hello World")
    layout = QVBoxLayout()
    label = QLabel("My simple app.")
    label.setMargin(10)
    layout.addWidget(label)
    button1 = QPushButton("Hide")
    button1.setIcon(QIcon(os.path.join(basedir, "icons", "hand.png")))
    button1.pressed.connect(self.lower)
    layout.addWidget(button1)
    button2 = QPushButton("Close")
    button2.setIcon(QIcon(os.path.join(basedir, "icons", "lightning.png")))
    button2.pressed.connect(self.close)
    layout.addWidget(button2)
    container = QWidget()
    container.setLayout(layout)
    self.setCentralWidget(container)
    self.show()
if __name__ == '__main__':
  app = QApplication(sys.argv)
  w = MainWindow()
  app.exec_()

```

Try and run your app again from the parent folder -- you'll find that the icons now appear as expected on the buttons, no matter where you launch the app from.
### Packaging the icons
So now we have our application showing icons, and they work wherever the application is launched from. Package the application again with `pyinstaller "Hello World.spec"` and then try and run it again from the `dist` folder as before. You'll notice the icons are missing again.
![Window with two icons missing](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/basic_app_icons2_missing.png) _Window with two buttons with icons missing._
The problem now is that the icons haven't been copied to the `dist/Hello World` folder -- take a look in it. Our script expects the icons to be a specific location relative to it, and if they are not, then nothing will be shown.
This same principle applies to any other data files you package with your application, including Qt Designer UI files, settings files or source data. You need to ensure that relative path structures are replicated after packaging.
### Bundling data files with PyInstaller
For the application to continue working after packaging, the files it depends on need to be in the same relative locations.
To get data files into the `dist` folder we can instruct _PyInstaller_ to copy them over. _PyInstaller_ accepts a list of individual paths to copy, together with a folder path relative to the `dist/<app name>` folder where it should to copy them _to_. As with other options, this can be specified by command line arguments or in the `.spec` file.
Files specified on the command line are added using `--add-data`, passing the source file and destination folder separated by a colon `:`.
The path separator is platform-specific: Linux or Mac use `:`, on Windows use `;`
bash ```
pyinstaller --windowed --name="Hello World" --icon="Hello World.icns" --add-data="icons/hand.png:icons" --add-data="icons/lightning.png:icons" app.py

```

Here we've specified the destination location as `icons`. The path is relative to the root of our application's folder in `dist` -- so `dist/Hello World` with our current app. The path `icons` means a folder named `icons` under this location, so `dist/Hello World/icons`. Putting our icons right where our application expects to find them!
You can also specify data files via the `datas` list in the Analysis section of the spec file, shown below.
python ```
a = Analysis(['app.py'],
       pathex=[],
       binaries=[],
       datas=[('icons/hand.png', 'icons'), ('icons/lightning.png', 'icons')],
       hiddenimports=[],
       hookspath=[],
       runtime_hooks=[],
       excludes=[],
       win_no_prefer_redirects=False,
       win_private_assemblies=False,
       cipher=block_cipher,
       noarchive=False)

```

Then rebuild from the `.spec` file with
bash ```
pyinstaller "Hello World.spec"

```

In both cases we are telling _PyInstaller_ to copy the specified files to the location `./icons/` in the output folder, meaning `dist/Hello World/icons`. If you run the build, you should see your `.png` files are now in the in `dist` output folder, under a folder named icons.
![The icon file copied to the dist folder](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/application_icon_build_in_dest.png) _The icon file copied to the dist folder_
If you run your app from `dist` you should now see the icon icons in your window as expected!
![Window with two icons](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/basic_app_icons2_missing.png) _Window with two buttons with icons, finally!_
### Bundling data folders
Usually you will have more than one data file you want to include with your packaged file. The latest PyInstaller versions let you bundle folders just like you would files, keeping the sub-folder structure.
Let's update our configuration to bundle our icons folder in one go, so it will continue to work even if we add more icons in future.
To copy the `icons` folder across to our build application, we just need to add the folder to our `.spec` file `Analysis` block. As for the single file, we add it as a tuple with the source path (from our project folder) and the destination folder under the resulting folder in `dist`.
python ```
# ...
a = Analysis(['app.py'],
       pathex=[],
       binaries=[],
       datas=[('icons', 'icons')],  # tuple is (source_folder, destination_folder)
       hiddenimports=[],
       hookspath=[],
       hooksconfig={},
       runtime_hooks=[],
       excludes=[],
       win_no_prefer_redirects=False,
       win_private_assemblies=False,
       cipher=block_cipher,
       noarchive=False)
# ...

```

If you run the build using this spec file you'll see the `icons` folder copied across to the `dist\Hello World` folder. If you run the application from the folder, the icons will display as expected -- the relative paths remain correct in the new location.
Alternatively, you can bundle your data files using Qt's QResource architecture. See [our tutorial](https://www.pythonguis.com/tutorials/qresource-system/) for more information.
## Building the App bundle into a Disk Image
So far we've used _PyInstaller_ to bundle the application into macOS app, along with the associated data files. The output of this bundling process is a folder and an macOS app bundle, named `Hello World.app`.
If you try and distribute this app bundle, you'll notice a problem: the app bundle is actually just a special folder. While macOS displays it as an application, if you try and share it, you'll actually be sharing hundreds of individual files. To distribute the app properly, we need some way to package it into a single file.
The _easiest_ way to do this is to use a `.zip` file. You can _zip_ the folder and give this to someone else to unzip on their own computer, giving them a complete app bundle they can copy to their _Applications_ folder.
However, if you've install macOS applications before you'll know this isn't the _usual_ way to do it. Usually you get a _Disk Image_ `.dmg` file, which when opened shows the application bundle, and a link to your _Applications_ folder. To install the app, you just drag it across to the target.
To make our app look as professional as possible, we should copy this expected behaviour. Next we'll look at how to take our app bundle and package it into a macOS _Disk Image_.
## Making sure the build is ready.
If you've followed the tutorial so far, you'll already have your app ready in the `/dist` folder. If not, or yours isn't working you can also download the [source code files for this tutorial](https://downloads.pythonguis.com/DemoAppPyInstaller.zip) which includes a sample `.spec` file. As above, you can run the same build using the provided `Hello World.spec` file.
bash ```
pyinstaller "Hello World.spec"

```

This packages everything up as an app bundle in the `dist/` folder, with a custom icon. Run the app bundle to ensure everything is bundled correctly, and you should see the same window as before with the icons visible.
![Two icons](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/basic_app_icons2.png) _Window with two icons, and a button._
## Creating an _Disk Image_
Now we've successfully bundled our application, we'll next look at how we can take our app bundle and use it to create a macOS _Disk Image_ for distribution.
To create our _Disk Image_ we'll be using the [create-dmg](https://github.com/create-dmg/create-dmg) tool. This is a command-line tool which provides a simple way to build disk images automatically. If you are using Homebrew, you can install create-dmg with the following command.
bash ```
brew install create-dmg

```

...otherwise, see the [Github repository](https://github.com/create-dmg/create-dmg) for instructions.
The `create-dmg` tool takes a _lot_ of options, but below are the most useful.
bash ```
create-dmg --help
create-dmg 1.0.9
Creates a fancy DMG file.
Usage: create-dmg [options] <output_name.dmg> <source_folder>
All contents of <source_folder> will be copied into the disk image.
Options:
 --volname <name>
   set volume name (displayed in the Finder sidebar and window title)
 --volicon <icon.icns>
   set volume icon
 --background <pic.png>
   set folder background image (provide png, gif, or jpg)
 --window-pos <x> <y>
   set position the folder window
 --window-size <width> <height>
   set size of the folder window
 --text-size <text_size>
   set window text size (10-16)
 --icon-size <icon_size>
   set window icons size (up to 128)
 --icon file_name <x> <y>
   set position of the file's icon
 --hide-extension <file_name>
   hide the extension of file
 --app-drop-link <x> <y>
   make a drop link to Applications, at location x,y
 --no-internet-enable
   disable automatic mount & copy
 --add-file <target_name> <file>|<folder> <x> <y>
   add additional file or folder (can be used multiple times)
 -h, --help
    display this help screen

```

The most important thing to notice is that the command requires a `<source folder>` and all contents of that folder will be copied to the _Disk Image_. So to build the image, we first need to put our app bundle in a folder by itself.
Rather than do this manually each time you want to build a _Disk Image_ I recommend creating a shell script. This ensures the build is reproducible, and makes it easier to configure.
Below is a working script to create a _Disk Image_ from our app. It creates a temporary folder `dist/dmg` where we'll put the things we want to go in the _Disk Image_ -- in our case, this is just the app bundle, but you can add other files if you like. Then we make sure the folder is empty (in case it still contains files from a previous run). We copy our app bundle into the folder, and finally check to see if there is already a `.dmg` file in `dist` and if so, remove it too. Then we're ready to run the `create-dmg` tool.
bash ```
#!/bin/sh
# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r "dist/Hello World.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/Hello World.dmg" && rm "dist/Hello World.dmg"
create-dmg \
 --volname "Hello World" \
 --volicon "Hello World.icns" \
 --window-pos 200 120 \
 --window-size 600 300 \
 --icon-size 100 \
 --icon "Hello World.app" 175 120 \
 --hide-extension "Hello World.app" \
 --app-drop-link 425 120 \
 "dist/Hello World.dmg" \
 "dist/dmg/"

```

The options we pass to `create-dmg` set the dimensions of the _Disk Image_ window when it is opened, and positions of the icons in it.
Save this shell script in the root of your project, named e.g. `builddmg.sh`. To make it possible to run, you need to set the _execute bit_ with.
bash ```
chmod +x builddmg.sh

```

With that, you can now build a _Disk Image_ for your Hello World app with the command.
bash ```
./builddmg.sh

```

This will take a few seconds to run, producing quite a bit of output.
bash ```
 No such file or directory
Creating disk image...
...............................................................
created: /Users/martin/app/dist/rw.Hello World.dmg
Mounting disk image...
Mount directory: /Volumes/Hello World
Device name:   /dev/disk2
Making link to Applications dir...
/Volumes/Hello World
Copying volume icon file 'Hello World.icns'...
Running AppleScript to make Finder stuff pretty: /usr/bin/osascript "/var/folders/yf/1qvxtg4d0vz6h2y4czd69tf40000gn/T/createdmg.tmp.XXXXXXXXXX.RvPoqdr0" "Hello World"
waited 1 seconds for .DS_STORE to be created.
Done running the AppleScript...
Fixing permissions...
Done fixing permissions
Blessing started
Blessing finished
Deleting .fseventsd
Unmounting disk image...
hdiutil: couldn't unmount "disk2" - Resource busy
Wait a moment...
Unmounting disk image...
"disk2" ejected.
Compressing disk image...
Preparing imaging engine…
Reading Protective Master Boot Record (MBR : 0)…
  (CRC32 $38FC6E30: Protective Master Boot Record (MBR : 0))
Reading GPT Header (Primary GPT Header : 1)…
  (CRC32 $59C36109: GPT Header (Primary GPT Header : 1))
Reading GPT Partition Data (Primary GPT Table : 2)…
  (CRC32 $528491DC: GPT Partition Data (Primary GPT Table : 2))
Reading (Apple_Free : 3)…
  (CRC32 $00000000: (Apple_Free : 3))
Reading disk image (Apple_HFS : 4)…
...............................................................................
  (CRC32 $FCDC1017: disk image (Apple_HFS : 4))
Reading (Apple_Free : 5)…
...............................................................................
  (CRC32 $00000000: (Apple_Free : 5))
Reading GPT Partition Data (Backup GPT Table : 6)…
...............................................................................
  (CRC32 $528491DC: GPT Partition Data (Backup GPT Table : 6))
Reading GPT Header (Backup GPT Header : 7)…
...............................................................................
  (CRC32 $56306308: GPT Header (Backup GPT Header : 7))
Adding resources…
...............................................................................
Elapsed Time: 3.443s
File size: 23178950 bytes, Checksum: CRC32 $141F3DDC
Sectors processed: 184400, 131460 compressed
Speed: 18.6Mbytes/sec
Savings: 75.4%
created: /Users/martin/app/dist/Hello World.dmg
hdiutil does not support internet-enable. Note it was removed in macOS 10.15.
Disk image done

```

While it's building, the _Disk Image_ will pop up. Don't get too excited yet, it's still building. Wait for the script to complete, and you will find the finished `.dmg` file in the `dist/` folder.
![The Disk Image in the dist folder](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/disk_image_in_build_folder.png) _The Disk Image created in the dist folder_
### Running the installer
Double-click the _Disk Image_ to open it, and you'll see the usual macOS install view. Click and drag your app across the the `Applications` folder to install it.
![The Disk Image containing your file](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/macos_disk_image.png) _The Disk Image contains the app bundle and a shortcut to the applications folder_
If you open the _Showcase_ view (press F4) you will see your app installed. If you have a lot of apps, you can search for it by typing "Hello"
![The app is installed!](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-pyinstaller-macos-dmg/macos_app_installed.png) _The app installed on macOS_
## Repeating the build
Now you have everything set up, you can create a new app bundle & _Disk Image_ of your application any time, by running the two commands from the command line.
bash ```
pyinstaller "Hello World.spec"
./builddmg.sh

```

It's that simple!
## Wrapping up
In this tutorial we've covered how to build your PyQt5 applications into a macOS app bundle using _PyInstaller_ , including adding data files along with your code. Then we walked through the process of creating a _Disk Image_ to distribute your app to others. Following these steps you should be able to package up your own applications and make them available to other people.
For a complete view of all _PyInstaller_ bundling options take a look at the [PyInstaller usage documentation](https://pyinstaller.readthedocs.io/en/stable/usage.html).
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
Mark As Complete 
Continue with [ PyQt5 Tutorial ](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-linux-pyinstaller/ "Continue to next part")
Return to [Create Desktop GUI Applications with PyQt5 ](https://www.pythonguis.com/pyqt5-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Packaging PyQt5 applications into a macOS app with PyInstaller** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/Python books) on the subject. 
**Packaging PyQt5 applications into a macOS app with PyInstaller** was published in [tutorials](https://www.pythonguis.com/tutorials/) on February 07, 2022 (updated March 10, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [setup](https://www.pythonguis.com/topics/setup/) [package](https://www.pythonguis.com/topics/package/) [pyinstaller](https://www.pythonguis.com/topics/pyinstaller/) [macos](https://www.pythonguis.com/topics/macos/) [app](https://www.pythonguis.com/topics/app/) [ packaging](https://www.pythonguis.com/topics/packaging/) [installer](https://www.pythonguis.com/topics/installer/) [mac](https://www.pythonguis.com/topics/mac/) [qt](https://www.pythonguis.com/topics/qt/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt5-packaging](https://www.pythonguis.com/topics/pyqt5-packaging/) [python](https://www.pythonguis.com/topics/python/) [qt5](https://www.pythonguis.com/topics/qt5/)
  * [](https://www.pythonguis.com/ "Python GUIs")
  * [Databases & SQL](https://www.pythonguis.com/topics/databases/)
  * [Learn the fundamentals](https://www.pythonguis.com/topics/foundation/)
  * [Where do I begin?](https://www.pythonguis.com/topics/getting-started/)
  * [Data Science](https://www.pythonguis.com/topics/data-science/)
  * [Packaging & Distribution](https://www.pythonguis.com/topics/packaging/)
  * [QML/QtQuick](https://www.pythonguis.com/topics/qml/)
  * [Raspberry Pi](https://www.pythonguis.com/topics/raspberry-pi/)
  * [Games](https://www.pythonguis.com/topics/games/)
  * [Intermediate Tutorials](https://www.pythonguis.com/topics/intermediate/)


  * **Sections**
  * [Installation](https://www.pythonguis.com/installation/)
  * [First steps with PySide6](https://www.pythonguis.com/tutorials/pyside6-creating-your-first-window/)
  * [First steps with PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/)
  * [Example Python Apps](https://www.pythonguis.com/examples/)
  * [Widget Library](https://www.pythonguis.com/widgets/)
  * [Simple PyQt6 & PySide6 documentation](https://www.pythonguis.com/docs/)
  * [Reusable code & snippets](https://www.pythonguis.com/code/)
  * [Frequently Asked Questions](https://www.pythonguis.com/faq/)


  * **Tutorials**
  * [Which Python GUI library?](https://www.pythonguis.com/faq/which-python-gui-library/)
  * [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/)
  * [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/)
  * [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/)
  * [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/)
  * [Tkinter tutorial](https://www.pythonguis.com/tkinter-tutorial/)
  * [Latest articles](https://www.pythonguis.com/blog/)


  * **Books & Downloads**
  * [ Your Downloads](https://www.martinfitzpatrick.com/library/)
  * [PyQt5 Book](https://www.pythonguis.com/pyqt5-book/) / [PySide2 Book](https://www.pythonguis.com/pyside2-book/)
  * [PyQt6 Book](https://www.pythonguis.com/pyqt6-book/) / [PySide6 Book](https://www.pythonguis.com/pyside6-book/)
  * [Python Packaging Book](https://www.pythonguis.com/packaging-book/)
  * [ Book Source Code](https://www.pythonguis.com/books/downloads/)
  * [ PyQt6 Video Course](https://www.martinfitzpatrick.com/pyqt6-crash-course/)


  * **Community & Consulting**
  * [ Python GUIS Forum ](https://forum.pythonguis.com/)
  * [ Feedback & Corrections](https://tally.so/r/wbvxNE)
  * [Consulting](https://www.pythonguis.com/hire/)
  * [Mentoring](https://www.pythonguis.com/live/)
  * [Contact me](https://www.martinfitzpatrick.com/contact)
  * [Licensing, Privacy & Legal](https://www.martinfitzpatrick.com/legal)


[](https://twitter.com/pythonguis) [](https://github.com/pythonguis) [](https://www.facebook.com/pythonguis) [](https://www.youtube.com/channel/UCMW4KwSlygaDef0tgqPjbRQ) [](https://www.linkedin.com/company/pythonguis/)
[Python GUIs](https://www.pythonguis.com/) Copyright ©2014-2025 [ Martin Fitzpatrick](https://www.martinfitzpatrick.com)
Tutorials CC-BY-NC-SA [Sitemap](https://www.pythonguis.com/sitemap/) [Changelog](https://www.pythonguis.com/changelog/) Public code [BSD](https://opensource.org/licenses/BSD-2-Clause) & [MIT](https://opensource.org/licenses/MIT)
