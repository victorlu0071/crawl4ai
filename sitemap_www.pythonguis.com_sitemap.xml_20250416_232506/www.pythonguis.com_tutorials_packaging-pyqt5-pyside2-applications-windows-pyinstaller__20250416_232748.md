# Content from: https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/

[](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
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
  * [PyQt5](https://www.pythonguis.com/pyqt5/)
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Packaging PyQt5 applications for Windows with PyInstaller & InstallForge
Turn your PyQt5 application into a distributable installer for Windows
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Oct 18 This article has been updated for 2022. [ Packaging and Distributing PyQt5 Applications ](https://www.pythonguis.com/pyqt5-tutorial/#packaging-and-distribution)
[ Example PyInstaller Source files ](https://downloads.pythonguis.com/DemoAppPyInstaller.zip) [ Example Windows Installer ](https://downloads.pythonguis.com/DemoAppInstallforge.exe)
#### [ PyQt5 Tutorial ](https://www.pythonguis.com/pyqt5-tutorial/) — [Packaging and Distributing PyQt5 Applications](https://www.pythonguis.com/pyqt5-tutorial/#packaging-and-distribution)
  * [Packaging PyQt5 applications for Windows with PyInstaller & InstallForge](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/)
  * [Packaging PyQt5 applications into a macOS app with PyInstaller](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/)
  * [Packaging PyQt5 applications for Linux with PyInstaller & fpm](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-linux-pyinstaller/)
  * [Using QResource to Package Data Files With PyInstaller and PyQt5](https://www.pythonguis.com/tutorials/packaging-data-files-pyqt5-with-qresource-system/)
  * [Packaging PyQt5 apps with fbs](https://www.pythonguis.com/tutorials/packaging-pyqt5-apps-fbs/)


There is not much fun in creating your own desktop applications if you can't share them with other people — whether than means publishing it commercially, sharing it online or just giving it to someone you know. Sharing your apps allows other people to benefit from your hard work!
The good news is there are tools available to help you do just that with your Python applications which work well with apps built using PyQt5. In this tutorial we'll look at the most popular tool for packaging Python applications: _PyInstaller_.
This tutorial is broken down into a series of steps, using _PyInstaller_ to build first simple, and then increasingly complex PyQt5 applications into distributable EXE files on Windows. You can choose to follow it through completely, or skip ahead to the examples that are most relevant to your own project.
We finish off by using _InstallForge_ to create a distributable Windows installer.
You always need to compile your app on your target system. So, if you want to create a Mac .app you need to do this on a Mac, for an EXE you need to use Windows.
[![Example Installer for Windows](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/installforge_app_packaged.png)](https://downloads.pythonguis.com/DemoAppInstallforge.exe) _Example Installer for Windows_
If you're impatient, you can download the [Example Installer for Windows](https://downloads.pythonguis.com/DemoAppInstallforge.exe) first.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Table of Contents
  * [Requirements](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#requirements)
    * [Install in virtual environment (optional)](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#install-in-virtual-environment-optional)
  * [Getting Started](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#getting-started)
  * [Building a basic app](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#building-a-basic-app)
  * [The Spec file](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#the-spec-file)
  * [Tweaking the build](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#tweaking-the-build)
    * [Naming your app](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#naming-your-app)
    * [Hiding the console window](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#hiding-the-console-window)
    * [One File Build](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#one-file-build)
    * [Setting an application Icon](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#setting-an-application-icon)
    * [Dealing with relative paths](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#dealing-with-relative-paths)
    * [Taskbar Icons](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#taskbar-icons)
  * [Data files and Resources](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#data-files-and-resources)
    * [Bundling data files with PyInstaller](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#bundling-data-files-with-pyinstaller)
    * [Bundling data folders](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#bundling-data-folders)
  * [Building a Windows Installer with InstallForge](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#building-a-windows-installer-with-installforge)
  * [Making sure the build is ready.](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#making-sure-the-build-is-ready)
  * [Creating an installer](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#creating-an-installer)
    * [General](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#general)
    * [Setup](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#setup)
    * [Dialogs](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#dialogs)
    * [System](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#system)
    * [Build](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#build)
    * [Running the installer](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#running-the-installer)
  * [Wrapping up](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/#wrapping-up)


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

This should produce the following window (on Windows 11).
![Simple skeleton app in PyQt5](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/basic_app.png) _Simple skeleton app in PyQt5_
## Building a basic app
Now we have our simple application skeleton in place, we can run our first build test to make sure everything is working.
Open your terminal (command prompt) and navigate to the folder containing your project. You can now run the following command to run the _PyInstaller_ build.
python ```
pyinstaller app.py

```

You'll see a number of messages output, giving debug information about what _PyInstaller_ is doing. These are useful for debugging issues in your build, but can otherwise be ignored. The output that I get for running the command on Windows 11 is shown below.
bash ```
U:\home\martin\helloworld>pyinstaller app.py
INFO: PyInstaller: 3.6
INFO: Python: 3.7.6
INFO: Platform: Windows-10-10.0.18362-SP0
INFO: wrote U:\home\martin\helloworld\app.spec
INFO: UPX is not available.
INFO: Extending PYTHONPATH with paths
['U:\\home\\martin\\helloworld', 'U:\\home\\martin\\helloworld']
INFO: checking Analysis
INFO: Building Analysis because Analysis-00.toc is non existent
INFO: Initializing module dependency graph...
INFO: Caching module graph hooks...
INFO: Analyzing base_library.zip ...
INFO: Caching module dependency graph...
INFO: running Analysis Analysis-00.toc
INFO: Adding Microsoft.Windows.Common-Controls to dependent assemblies of final executable
 required by c:\users\gebruiker\appdata\local\programs\python\python37\python.exe
INFO: Analyzing U:\home\martin\helloworld\app.py
INFO: Processing module hooks...
INFO: Loading module hook "hook-encodings.py"...
INFO: Loading module hook "hook-pydoc.py"...
INFO: Loading module hook "hook-PyQt5.py"...
WARNING: Hidden import "sip" not found!
INFO: Loading module hook "hook-PyQt5.QtWidgets.py"...
INFO: Loading module hook "hook-xml.py"...
INFO: Loading module hook "hook-PyQt5.QtCore.py"...
INFO: Loading module hook "hook-PyQt5.QtGui.py"...
INFO: Looking for ctypes DLLs
INFO: Analyzing run-time hooks ...
INFO: Including run-time hook 'pyi_rth_pyqt5.py'
INFO: Looking for dynamic libraries
INFO: Looking for eggs
INFO: Using Python library c:\users\gebruiker\appdata\local\programs\python\python37\python37.dll
INFO: Found binding redirects:
[]
INFO: Warnings written to U:\home\martin\helloworld\build\app\warn-app.txt
INFO: Graph cross-reference written to U:\home\martin\helloworld\build\app\xref-app.html
INFO: checking PYZ
INFO: Building PYZ because PYZ-00.toc is non existent
INFO: Building PYZ (ZlibArchive) U:\home\martin\helloworld\build\app\PYZ-00.pyz
INFO: Building PYZ (ZlibArchive) U:\home\martin\helloworld\build\app\PYZ-00.pyz completed successfully.
INFO: checking PKG
INFO: Building PKG because PKG-00.toc is non existent
INFO: Building PKG (CArchive) PKG-00.pkg
INFO: Building PKG (CArchive) PKG-00.pkg completed successfully.
INFO: Bootloader c:\users\gebruiker\appdata\local\programs\python\python37\lib\site-packages\PyInstaller\bootloader\Windows-64bit\run.exe
INFO: checking EXE
INFO: Building EXE because EXE-00.toc is non existent
INFO: Building EXE from EXE-00.toc
INFO: Appending archive to EXE U:\home\martin\helloworld\build\app\app.exe
INFO: Building EXE from EXE-00.toc completed successfully.
INFO: checking COLLECT
INFO: Building COLLECT because COLLECT-00.toc is non existent
INFO: Building COLLECT COLLECT-00.toc
INFO: Building COLLECT COLLECT-00.toc completed successfully.

```

If you look in your folder you'll notice you now have two new folders `dist` and `build`.
![build & dist folders created by PyInstaller](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/2_Folders_Created_NAmCBkI.png) _build & dist folders created by PyInstaller_
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
│     ├── app.exe
│     ├── app.exe.manifest
│     ├── base_library.zip
│     ├── warn-app.txt
│     └── xref-app.html
└── dist
  └── app
    ├── MSVCP140.dll
    ├── PyQt5
    ├── app.exe
    ├── app.exe.manifest
    ├── Qt5Core.dll
    ...

```

The `build` folder is used by _PyInstaller_ to collect and prepare the files for bundling, it contains the results of analysis and some additional logs. For the most part, you can ignore the contents of this folder, unless you're trying to debug issues.
The `dist` (for "distribution") folder contains the files to be distributed. This includes your application, bundled as an executable file, together with any associated libraries (for example PyQt5) and binary `.dll` files.
Everything necessary to run your application will be in this folder, meaning you can take this folder and "distribute" it to someone else to run your app.
You can try running your app yourself now, by running the executable file, named `app.exe` from the `dist` folder. After a short delay you'll see the familiar window of your application pop up as shown below.
![Simple app, running after being packaged](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/basic_app.png) _Simple app, running after being packaged_
You may also notice a console/terminal window pop up as your application runs. We'll cover how to stop that happening shortly.
In the same folder as your Python file, alongside the `build` and `dist` folders _PyInstaller_ will have also created a `.spec` file. In the next section we'll take a look at this file, what it is and what it does.
## The Spec file
The `.spec` file contains the build configuration and instructions that _PyInstaller_ uses to package up your application. Every _PyInstaller_ project has a `.spec` file, which is generated based on the command line options you pass when running `pyinstaller`.
When we ran `pyinstaller` with our script, we didn't pass in anything other than the name of our Python application file. This means our spec file currently contains only the default configuration. If you open it, you'll see something similar to what we have below.
python ```
# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(['app.py'],
       pathex=[],
       binaries=[],
       datas=[],
       hiddenimports=[],
       hookspath=[],
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
     console=True )
coll = COLLECT(exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='app')

```

The first thing to notice is that this is a Python file, meaning you can edit it and use Python code to calculate values for the settings. This is mostly useful for complex builds, for example when you are targeting different platforms and want to conditionally define additional libraries or dependencies to bundle.
If you generate a `.spec` file on Windows the path separator will be `\\`. To use this same `.spec` file on macOS you'll need to switch the separators to `/`. Thankfully `/` also works on Windows.
Once a `.spec` file has been generated, you can pass this to `pyinstaller` instead of your script to repeat the previous build process. Run this now to rebuild your executable.
bash ```
pyinstaller app.spec

```

The resulting build will be identical to the build used to generate the `.spec` file (assuming you have made no changes). For many _PyInstaller_ configuration changes you have the option of passing command-line arguments, or modifying your existing `.spec` file. Which you choose is up to you.
## Tweaking the build
So far we've created a simple first build of a very basic application. Now we'll look at a few of the most useful options that _PyInstaller_ provides to tweak our build. Then we'll go on to look at building more complex applications.
### Naming your app
One of the simplest changes you can make is to provide a proper "name" for your application. By default the app takes the name of your source file (minus the extension), for example `main` or `app`. This isn't usually what you want.
You can provide a nicer name for _PyInstaller_ to use for the executable (and `dist` folder) either by editing the `.spec` file to add a `name=` under the app block.
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
     console=False # False = do not show console.
     )

```

Alternatively, you can re-run the `pyinstaller` command and pass the `-n` or `--name` configuration flag along with your `app.py` script.
bash ```
pyinstaller -n "Hello World" app.py
# or
pyinstaller --name "Hello World" app.py

```

The resulting EXE file will be given the name `Hello World.exe` and placed in the folder `dist\Hello World\`.
![Application with custom name "Hello World"](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/app_name_kz1bTZt.png) _Application with custom name "Hello World"_
The name of the `.spec` file is taken from the name passed in on the command line, so this will _also_ create a new spec file for you, called `Hello World.spec` in your root folder.
### Hiding the console window
When you run your packaged application you will notice that a console window runs in the background. If you try and close this console window your application will also close. You almost never want this window in a GUI application and _PyInstaller_ provides a simple way to turn this off.
![Application running with terminal in background](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/Terminal_and_App_boJR82s.png) _Application running with terminal in background_
You can fix this in one of two ways. Firstly, you can edit the previously created `.spec` file setting `console=False` under the EXE block as shown below.
python ```
exe = EXE(pyz,
     a.scripts,
     [],
     exclude_binaries=True,
     name='app',
     debug=False,
     bootloader_ignore_signals=False,
     strip=False,
     upx=True,
     console=False # False = do not show console.
     )

```

Alternatively, you can re-run the `pyinstaller` command and pass the `-w`, `--noconsole` or `--windowed` configuration flag along with your `app.py` script.
bash ```
pyinstaller -w app.py
# or
pyinstaller --windowed app.py
# or
pyinstaller --noconsole app.py

```

There is no difference between any of the options.
Re-running `pyinstaller` will re-generate the `.spec` file. If you've made any other changes to this file these will be lost.
### One File Build
On Windows _PyInstaller_ has the ability to create a one-file build, that is, a single EXE file which contains all your code, libraries and data files in one. This can be a convenient way to share simple applications, as you don't need to provide an installer or zip up a folder of files.
To specify a one-file build provide the `--onefile` flag at the command line.
bash ```
pyinstaller --onefile app.py

```

![Result of a one-file build](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/Onefile_Build_qT3pPFe.png) _Result of a one-file build_
Note that while the one-file build is easier to distribute, it is slower to execute than a normally built application. This is because every time the application is run it must create a temporary folder to unpack the contents of the executable. Whether this trade-off is worth the convenience for your app is up to you!
Using the `--onefile` option makes quite a few changes to the `.spec` file. You _can_ make these changes manually, but it's much simpler to use the command line switch when first creating your `.spec`
Since debugging a one file app is much harder, you should make sure everything is working with a normal build before you create a one-file package. We're going to continue this tutorial with a folder-based build for clarity.
### Setting an application Icon
By default _PyInstaller_ EXE files come with the following icon in place.
![Default PyInstaller application icon, on app.exe](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/application_icon_default.png) _Default PyInstaller application icon, on app.exe_
You will probably want to customize this to make your application more recognisable. This can be done easily using the `--icon=<filename>` command-line switch to _PyInstaller_. On Windows the icon should be provided as an `.ico` file.
bash ```
pyinstaller --windowed --icon=hand.ico app.py

```

The [portable version of IcoFx](https://portableapps.com/apps/graphics_pictures/icofx_portable) is a good free tool to create icons on Windows.
Or, by adding the `icon=` parameter to your `.spec` file.
python ```
exe = EXE(pyz,
     a.scripts,
     [],
     exclude_binaries=True,
     name='blarh',
     debug=False,
     bootloader_ignore_signals=False,
     strip=False,
     upx=True,
     console=False,
     icon='hand.ico')

```

If you now re-run the build (by using the command line arguments, or running with your modified `.spec` file) you'll see the specified icon file is now set on your application's EXE file.
![Custom application icon \(a hand\) on app.exe](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/application_icon_custom.png) _Custom application icon (a hand) on app.exe_
However, if you run your application, you're going to be disappointed.
![The custom EXE icon is not applied to the window](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/application_icon_custom_not_shown.png) _The custom EXE icon is not applied to the window_
The specified icon is not showing up on the window, and it will also not appear on your taskbar.
Why not? Because the icon used for the window isn't determined by the icons in the executable file, but by the application itself. To show an icon on our window we need to modify our simple application a little bit, to add a call to `.setWindowIcon()`.
python ```
from PyQt5 import QtWidgets, QtGui
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
  app.setWindowIcon(QtGui.QIcon('hand.ico'))
  w = MainWindow()
  app.exec()

```

Here we've added the `.setWindowIcon` call to the `app` instance. This defines a _default_ icon to be used for all windows of our application. You _can_ override this on a per-window basis if you like, by calling `.setWindowIcon` on the window itself.
If you run the above application you should now see the icon appears on the window.
![Window showing the custom hand icon](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/window_icon_custom.png) _Window showing the custom hand icon_
Even if you _don't_ see the icons, keep reading!
### Dealing with relative paths
There is a gotcha here, which might not be immediately apparent. To demonstrate it, open up a shell and change to the folder where our script is located. Run it with
bash ```
python3 app.py

```

If the icons are in the correct location, you should see them. Now change to the parent folder, and try and run your script again (change `<folder>` to the name of the folder your script is in).
bash ```
cd ..
python3 <folder>/app.py

```

![Window with icon missing](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/basic_app.png) _Window with icon missing._
The icons _don't_ appear. What's happening?
We're using _relative_ paths to refer to our data files. These paths are relative to the _current working directory_ -- not the folder your script is in. So if you run the script from elsewhere it won't be able to find the files.
One common reason for icons not to show up, is running examples in an IDE which uses the project root as the current working directory.
This is a minor issue before the app is packaged, but once it's installed you don't know what the _current working directory_ will be when it is run -- if it's wrong your app won't be able to find anything. We need to fix this before we go any further, which we can do by making our paths relative to _our application folder_.
In the updated code below, we define a new variable `basedir`, using `os.path.dirname` to get the containing folder of `__file__` which holds the full path of the current Python file. We then use this to build the relative paths for icons using `os.path.join()`.
Since our `app.py` file is in the root of our folder, all other paths are relative to that.
python ```
from PyQt5 import QtWidgets, QtGui
import sys, os
basedir = os.path.dirname(__file__)

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
  app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'hand.ico')))
  w = MainWindow()
  app.exec_()

```

Try and run your app again from the parent folder -- you'll find that the icon now appear as expected, no matter where you launch the app from. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
### Taskbar Icons
Unfortunately, even if the icon is showing on the window, it may still not show on the taskbar.
If it does for you, great! But it may not work when you distribute your application, so it's probably a good idea to follow the next steps anyway.
![Custom icon is not shown on the toolbar](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/taskbar_icon_custom_not_showing.png) _Custom icon is not shown on the toolbar_
The final tweak we need to make to get the icon showing on the taskbar is to add some cryptic incantations to the top of our Python file.
When you run your application, Windows looks at the executable and tries to guess what "application group" it belongs to. By default, any Python scripts (including your application) are grouped under the same "Python" group, and so will show the Python icon. To stop this happening, we need to provide Windows with a different application identifier.
The code below does this, by calling `ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID()` with a custom application id.
python ```
from PyQt5 import QtWidgets, QtGui
import sys, os
basedir = os.path.dirname(__file__)
try:
  from ctypes import windll # Only exists on Windows.
  myappid = 'mycompany.myproduct.subproduct.version'
  windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
  pass

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
  app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'hand.ico')))
  w = MainWindow()
  app.exec()

```

The listing above shows a generic `mycompany.myproduct.subproduct.version` string, but you _should_ change this to reflect your actual application. It doesn't really matter what you put for this purpose, but the convention is to use reverse-domain notation, `com.mycompany` for the company identifier.
With this added to your script, running it should now show the icon on your window and taskbar. The final step is to ensure that this icon is correctly packaged with your application and continues to be shown when run from the `dist` folder.
Try it, it wont.
The issue is that our application now has a dependency on a _external data file_ (the icon file) that's not part of our source. For our application to work, we now need to distribute this data file along with it. _PyInstaller_ can do this for us, but we need to tell it what we want to include, and where to put it in the output.
In the next section we'll look at the options available to you for managing data files associated with your app.
## Data files and Resources
So far we successfully built a simple app which had no external dependencies. However, once we needed to load an external file (in this case an icon) we hit upon a problem. The file wasn't copied into our `dist` folder and so could not be loaded.
In this section we'll look at the options we have to be able to bundle external resources, such as icons or Qt Designer `.ui` files, with our applications.
### Bundling data files with PyInstaller
The simplest way to get these data files into the `dist` folder is to just tell _PyInstaller_ to copy them over. _PyInstaller_ accepts a list of individual file paths to copy over, together with a folder path relative to the `dist/<app name>` folder where it should to copy them _to_.
As with other options, this can be specified by command line arguments, `--add-data`
bash ```
pyinstaller --windowed --icon=hand.ico --add-data="hand.ico;." app.py

```

You can provide `--add-data` multiple times. Note that the path separator is platform-specific, on Windows use `;` while on Linux or Mac use `:`
Or via the `datas` list in the Analysis section of the spec file, shown below.
python ```
a = Analysis(['app.py'],
       pathex=[],
       binaries=[],
       datas=[('hand.ico', '.')],
       hiddenimports=[],
       hookspath=[],
       runtime_hooks=[],
       excludes=[],
       win_no_prefer_redirects=False,
       win_private_assemblies=False,
       cipher=block_cipher,
       noarchive=False)

```

And then execute the `.spec` file with
bash ```
pyinstaller app.spec

```

In both cases we are telling _PyInstaller_ to copy the specified file `hand.ico` to the location `.` which means the output folder `dist`. We could specify other locations here if we wanted. On the command line the source and destination are separated by the path separator `;`, whereas in the `.spec` file, the values are provided as a 2-tuple of strings.
If you run the build, you should see your `.ico` file now in the output folder `dist` ready to be distributed with your application.
![The icon file copied to the dist folder](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/application_icon_build_in_dest.png) _The icon file copied to the dist folder_
If you run your app from `dist` you should now see the icon on the window, and on the taskbar as expected.
![The hand icon showing on the toolbar](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/taskbar_icon_custom.png) _The hand icon showing on the toolbar_
The file must be loaded in Qt using a _relative path_ , and be in the same relative location to the EXE as it was to the `.py` file for this to work.
If your icon looks blurry it means you don't have large-enough icon variations in your `.ico` file. An `.ico` file can contain multiple different sized icons in the same file. Ideally you want to have 16x16, 32x32, 48x48 and 256x256 pixel sizes included, although fewer will still work.
### Bundling data folders
Usually you will have more than one data file you want to include with your packaged file. The latest PyInstaller versions let you bundle folders just like you would files, keeping the sub-folder structure. For example, lets extend our app to add some additional icons, and put them under a folder.
python ```
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QIcon
import sys, os
basedir = os.path.dirname(__file__)
try:
  from ctypes import windll # Only exists on Windows.
  myappid = 'mycompany.myproduct.subproduct.version'
  windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
  pass

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Hello World")
    layout = QVBoxLayout()
    label = QLabel("My simple app.")
    label.setMargin(10)
    layout.addWidget(label)
    button = QPushButton("Push")
    button.setIcon(QIcon(os.path.join(basedir, "icons", "lightning.png")))
    button.pressed.connect(self.close)
    layout.addWidget(button)
    container = QWidget()
    container.setLayout(layout)
    self.setCentralWidget(container)
    self.show()
if __name__ == '__main__':
  app = QApplication(sys.argv)
  app.setWindowIcon(QIcon(os.path.join(basedir, "icons", "hand.ico")))
  w = MainWindow()
  app.exec_()

```

The icons (PNG files and an ICO file for the Windows file icon) are stored under a subfolder named 'icons'.
bash ```
.
├── app.py
└── icons
  └── lightning.png
  └── hand.png
  └── hand.ico

```

If you run this you'll see the following window, with a Window icon and a button icon.
![Two icons](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/basic_app_icons2.png) _Window with two icons, and a button._
The paths are using the Unix forward-slash `/` convention, so they are cross-platform for macOS. If you're only developing for Windows, you can use `\\`
To copy the `icons` folder across to our build application, we just need to add the folder to our `.spec` file `Analysis` block. As for the single file, we add it as a tuple with the source path (from our project folder) and the destination folder under the resulting `dist` folder.
python ```
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

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

```

If you run the build using this spec file you'll see the `icons` folder copied across to the `dist` folder. If you run the application from the folder, the icons will display as expected -- the relative paths remain correct in the new location.
Alternatively, you can bundle your data files using Qt's QResource architecture. See [our tutorial](https://www.pythonguis.com/tutorials/qresource-system/) for more information.
## Building a Windows Installer with InstallForge
So far we've used _PyInstaller_ to bundle applications for distribution, along with the associated data files. The output of this bundling process is a folder, named `dist` which contains all the files our application needs to run.
While you _could_ share this folder with your users as a ZIP file it's not the best user experience. Desktop applications are normally distributed with _installers_ which handle the process of putting the executable (and any other files) in the correct place, adding _Start Menu_ shortcuts and the like.
Now we've successfully bundled our application, we'll next look at how we can take our `dist` folder and use it to create a Windows installer.
## Making sure the build is ready.
If you've followed the tutorial so far, you'll already have your app ready in the `/dist` folder. If not, or yours isn't working you can also download the [source code files for this tutorial](https://downloads.pythonguis.com/DemoAppPyInstaller.zip) which includes a sample `.spec` file. As above, you can run the same build using the provided `app.spec` file.
bash ```
pyinstaller app.spec

```

This packages everything up ready to distribute in the `dist/app` folder. Run the executable `app.exe` to ensure everything is bundled correctly, and you should the same window as before with icons visible.
![Two icons](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/basic_app_icons2.png) _Window with two icons, and a button._
The `EXE` section in the `.spec` has a `name` parameter where you can specify the name of the resulting EXE file. You may want to change this to the name of your application.
## Creating an installer
Now we've successfully bundled our application, we'll next look at how we can take our `dist` folder and use it to create a functioning Windows installer.
To create our installer we'll be using a tool called [InstallForge](https://installforge.net/). InstallForge is free and you can download the installer from [this page](https://installforge.net/download/).
We'll now walk through the basic steps of creating an installer with _InstallForge_. If you're impatient, you can download the [finished Installforge Installer here](https://downloads.pythonguis.com/DemoAppInstallforge.exe).
### General
When you first run _InstallForge_ you'll be presented with this General tab. Here you can enter the basic information about your application, including the name, program version, company and website.
![InstallForge initial view, showing General settings](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/installforge_basic.png) _InstallForge initial view, showing General settings_
You can also select the target platforms for the installer, from various versions of Windows that are available. For desktop applications you currently _probably_ only want to target Windows 7, 8 and 10.
### Setup
Click on the left sidebar to open the "Files" page under "Setup". Here you can specify the files to be bundled in the installer.
Use "Add Files…" and select _all the files_ in the `dist/app` folder produced by _PyInstaller_. The file browser that pops up allows multiple file selections, so you can add them all in a single go, however you need to add folders separately. Click "Add Folder…" and add any folders under `dist/app` such as the `PyQt5` folder and `icons`
![InstallForge Files view, add all files & folders to be packaged](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/installforge_files.png) _InstallForge Files view, add all files & folders to be packaged_
Once you're finished scroll through the list to the bottom and ensure that the folders are listed to be included. You want all files and folders _under_ `dist/app` to be present. But the folder `dist/app` itself _should not_ be listed.
The default install path can be left as-is. The values between angled brackets, e.g. `<company>` , are variables and will be filled automatically.
Next, it's nice to allow your users to uninstall your application. Even though it's undoubtedly awesome, they may want to remove it at some time in the future. You can do this under the "Uninstall" tab, simply by ticking the box. This will also make the application appear in "Add or Remove Programs".
![InstallForge add Uninstaller for your app](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/installforge_uninstall.png) _InstallForge add Uninstaller for your app_
### Dialogs
The "Dialogs" section can be used to show custom messages, splash screens or license information to the user. The "Finish" tab lets you control what happens once the installer is complete, and it's helpful here to give the user the _option_ to run your program.
To do this you need to tick the box next to "Run program" and add your own application EXE into the box. Since `<installpath>\` is already specified, we can just add `app.exe`.
![InstallForge configure optional run program on finish install](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/installforge_finish.png) _InstallForge configure optional run program on finish install_
### System
Under "System" select "Shortcuts" to open the shortcut editor. Here you can specify shortcuts for both the Start Menu and Desktop if you like.
![InstallForge configure Shortcuts, for Start Menu and Desktop](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/installforge_shortcuts.png) _InstallForge configure Shortcuts, for Start Menu and Desktop_
Click "Add…" to add new shortcuts for your application. Choose between Start menu and Desktop shortcuts, and fill in the name and target file. This is the path your application EXE will end up at once installed. Since `<installpath>\` is already specified, you simply need to add your application's EXE name onto the end, here `app.exe`
![InstallForge, adding a Shortcut](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/installforge_shortcut_settings.png) _InstallForge, adding a Shortcut_
### Build
With the basic settings in place, you can now build your installer.
At this point you can save your _InstallForge_ project so you can re-build the installer from the same settings in future.
Click on the "Build" section at the bottom to open the build panel.
![InstallForge, ready to build](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/installforge_build.png) _InstallForge, ready to build_
Click on the large icon button to start the build process. If you haven't already specified a setup file location you will be prompted for one. This is the location where you want the _completed installer_ to be saved.
**Don't** save it in your `dist` folder.
The build process will began, collecting and compressing the files into the installer.
![InstallForge, build complete](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/installforge_build_done.png) _InstallForge, build complete_
Once complete you will be prompted to run the installer. This is entirely optional, but a handy way to find out if it works.
### Running the installer
The installer itself shouldn't have any surprises, working as expected. Depending on the options selected in _InstallForge_ you may have extra panels or options.
![InstallForge, running the resulting installer](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/installforge_installing.png) _InstallForge, running the resulting installer_
Step through the installer until it is complete. You can optionally run the application from the last page of the installer, or you can find it in your start menu.
![Our demo app in the Start Menu on Windows 11](https://www.pythonguis.com/static/tutorials/qt/packaging-applications-windows-pyinstaller-installforge/installforge_installed_in_start_menu.png) _Our demo app in the Start Menu in the Start Menu on Windows 11_
## Wrapping up
In this tutorial we've covered how to build your PyQt5 applications into a distributable EXE using _PyInstaller_ , including adding data files along with your code. Then we walked through the process of building the application into a Windows Installer using InstallForge. Following these steps you should be able to package up your own applications and make them available to other people.
For a complete view of all _PyInstaller_ bundling options take a look at the [PyInstaller usage documentation](https://pyinstaller.readthedocs.io/en/stable/usage.html).
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
Mark As Complete 
Continue with [ PyQt5 Tutorial ](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/ "Continue to next part")
Return to [Create Desktop GUI Applications with PyQt5 ](https://www.pythonguis.com/pyqt5-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Packaging PyQt5 applications for Windows with PyInstaller & InstallForge** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/Python books) on the subject. 
**Packaging PyQt5 applications for Windows with PyInstaller & InstallForge** was published in [tutorials](https://www.pythonguis.com/tutorials/) on January 29, 2022 (updated October 18, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [setup.exe](https://www.pythonguis.com/topics/setupexe/) [installforge](https://www.pythonguis.com/topics/installforge/) [setup](https://www.pythonguis.com/topics/setup/) [package](https://www.pythonguis.com/topics/package/) [pyinstaller](https://www.pythonguis.com/topics/pyinstaller/) [exe](https://www.pythonguis.com/topics/exe/) [ packaging](https://www.pythonguis.com/topics/packaging/) [installer](https://www.pythonguis.com/topics/installer/) [windows](https://www.pythonguis.com/topics/windows/) [qt](https://www.pythonguis.com/topics/qt/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt5-packaging](https://www.pythonguis.com/topics/pyqt5-packaging/) [python](https://www.pythonguis.com/topics/python/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
