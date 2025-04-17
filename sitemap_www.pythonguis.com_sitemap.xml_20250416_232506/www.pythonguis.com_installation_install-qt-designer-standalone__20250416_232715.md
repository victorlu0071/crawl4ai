# Content from: https://www.pythonguis.com/installation/install-qt-designer-standalone/

[](https://www.pythonguis.com/installation/install-qt-designer-standalone/#menu)
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
# Install Qt Designer Standalone
Qt Designer Download for Windows, Mac and Linux
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Feb 05 [ Installation Guides ](https://www.pythonguis.com/installation/)
Qt Designer is a cross-platform drag and drop GUI designer, which can be used to build UIs for both PyQt and PySide. It is a great tool to simplify the process of building interfaces for your applications.
While Qt Designer is distributed by Qt as part of the Qt Creator integrated IDE, most of that IDE is not useful or helpful for Python development -- primarily being designed for C++ developers. If you just want the Designer application, this is not currently available from Qt. But helpfully, other people have stepped up to make this available.
In this guide we'll look at the various options available for installing Qt Designer as a standalone application on your system.
Since the Qt Designer software is free software, these alternative distributions of Qt Designer are permitted.
## PyQt Command line launcher
_Qt Designer_ is available on PyPi via the `pyqt5-tools` package. This can be `pip` installed just like any other Python package. This wrapper will download and install _Qt Designer_ for you and provide a command-line launcher to start the program.
  * PyQt6
  * PyQt5


bash ```
pip install pyqt6-tools

```

bash ```
pip install pyqt5-tools

```

After installation you can run _Qt Designer_ from the command line using the built-in launcher.
  * PyQt6
  * PyQt5


bash ```
pyqt6-tools designer

```

bash ```
pyqt5-tools designer

```

If this doesn't work check your Python `scripts` folder is in your `PATH`. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyside2-book/) _by Martin Fitzpatrick_ — (PySide2 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside2-book/) [Get the book](https://secure.pythonguis.com/01hf778jyaajk5vk1q6824sd44/)
## PySide6 Command line launcher
In recent versions of PySide6 _Qt Designer_ is installed automatically when you install PySide6 with `pip`. After installation you can run _Qt Designer_ from the command line using the built-in launcher.
bash ```
pyside6-designer

```

If this doesn't work check your Python `scripts` folder is in your `PATH`.
## Installing from Qt Package
If the above installation options don't work for you, you can instead follow the following instructions to install _Qt Creator_ or _Qt Designer_ depending on your platform.
If you install Qt Creator you can access Qt Designer through it, even if you don't use any of the other functionality.
### Windows
_Qt Designer_ is available in the installation packages for Qt available from [the Qt downloads page](https://www.qt.io/download-qt-installer). Download and run the appropriate installer for your system and follow the platform-specific instructions below. Installing _Qt Designer_ will not affect your Python PyQt5/6 or PySide2/6 installation.
_Qt Designer_ is not mentioned in the Windows Qt installer, but is automatically installed when you install any version of the Qt core libraries. For example, in the following screenshot we've opted to install the _MSVC 2017 64-bit_ version of Qt -- what you choose will have no effect on your _Designer_ install.
![Installing Qt, will also install Qt Designer.](https://www.pythonguis.com/static/installation/installation-designer/installation-windows.png) _Installing Qt, will also install Qt Designer._
If you want to install _Qt Creator_ it is listed under "Developer and Designer Tools". Rather confusingly, _Qt Designer_ isn't in here.
![Installing the Qt Creator component.](https://www.pythonguis.com/static/installation/installation-designer/installation-windows-creator.png) _Installing the Qt Creator component._
### macOS
_Qt Designer_ is available in the installation packages for Qt available from [the Qt downloads page](https://www.qt.io/download-qt-installer). Download and run the appropriate installer for your system and follow the platform-specific instructions below. Installing _Qt Designer_ will not affect your Python PyQt5/6 or PySide2/6 installation. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
_Qt Designer_ is not mentioned in the macOS Qt installer, but is automatically installed when you install any version of the Qt core libraries. Download the installer from the Qt website -- you can opt for the open source version.
![Inside the downloaded .dmg file you'll find the installer.](https://www.pythonguis.com/static/installation/installation-designer/installation-mac-dmg.png) _Inside the downloaded`.dmg` file you'll find the installer._
Open the installer to start the installation. Go through to where it asks you to choose which components to install. Select the _macOS_ package under the latest version of Qt.
![You only need the macOS package under the latest version.](https://www.pythonguis.com/static/installation/installation-designer/installation-mac-select.png) _You only need the macOS package under the latest version._
Once the installation is complete, open the folder where you installed Qt. The launcher for _Designer_ is under `<version>/clang_64/bin`. You'll notice that _Qt Creator_ is also installed in the root of the Qt installation folder.
![You can find the Designer launcher under the <version>/clang_64/bin folder.](https://www.pythonguis.com/static/installation/installation-designer/installation-mac-launch.png) _You can find the Designer launcher under the /clang_64/bin folder._
You can run _Designer_ from where it is located, or move it into your Applications folder so it is available to launch from the macOS Launchpad.
### Linux (Ubuntu & Debian)
You can install _Qt Designer_ using your package manager. Depending on your distribution and version you will have either _Qt5 Designer_ or _Qt6 Designer_ available..
  * Qt5
  * Qt6


bash ```
sudo apt-get install qttools5-dev-tools

```

bash ```
sudo apt-get install designer-qt6

```

Once installed, _Qt Designer_ will be available in the launcher.
![Qt Designer in Ubuntu launcher.](https://www.pythonguis.com/static/installation/installation-designer/installation-linux.png) _Qt Designer in Ubuntu launcher._
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Install Qt Designer Standalone** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/installation/install-qt-designer-standalone/Python books) on the subject. 
**Install Qt Designer Standalone** was published in [installation](https://www.pythonguis.com/installation/) on May 21, 2022 (updated February 05, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[installation](https://www.pythonguis.com/topics/installation/) [linux](https://www.pythonguis.com/topics/linux/) [macos](https://www.pythonguis.com/topics/macos/) [windows](https://www.pythonguis.com/topics/windows/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [ qt-designer](https://www.pythonguis.com/topics/qt-designer/) [qt-creator](https://www.pythonguis.com/topics/qt-creator/) [ pyqt5-qt-designer](https://www.pythonguis.com/topics/pyqt5-qt-designer/) [ pyqt6-qt-designer](https://www.pythonguis.com/topics/pyqt6-qt-designer/) [ pyside2-qt-designer](https://www.pythonguis.com/topics/pyside2-qt-designer/) [ pyside6-qt-designer](https://www.pythonguis.com/topics/pyside6-qt-designer/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
