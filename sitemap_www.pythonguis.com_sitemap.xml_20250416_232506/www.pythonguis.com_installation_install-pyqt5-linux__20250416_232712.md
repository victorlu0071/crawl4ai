# Content from: https://www.pythonguis.com/installation/install-pyqt5-linux/

[](https://www.pythonguis.com/installation/install-pyqt5-linux/#menu)
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
# Install PyQt5 on Ubuntu Linux
Install PyQt5 on Ubuntu and other Debian-based Linux distributions
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 08 PyQt5 [ Installation Guides ](https://www.pythonguis.com/installation/)
This tutorial is also available for [PyQt6](https://www.pythonguis.com/installation/install-pyqt6-linux/) , [PySide2](https://www.pythonguis.com/installation/install-pyside2-linux/) , [PySide6](https://www.pythonguis.com/installation/install-pyside6-linux/) and [Tkinter](https://www.pythonguis.com/installation/install-tkinter-linux/)
Before you start creating GUI applications with [PyQt5](https://www.pythonguis.com/pyqt5-tutorial/), you need to have a working installation of PyQt5 on your system. In this short tutorial, you'll find the steps that will guide you through installing PyQt5 on Ubuntu Linux.
This guide is also available for [macOS](https://www.pythonguis.com/installation/install-pyqt5-mac/) and [Windows](https://www.pythonguis.com/installation/install-pyqt5-windows/).
Note that the following instructions are for installing the PyQt5 version registered under the _GPL license_. If you need to use PyQt in a non-GPL project, then you will need to purchase an alternative license from [Riverbank Computing](https://www.riverbankcomputing.com) to release your software.
Table of Contents
  * [Preparing Ubuntu to Install PyQt5](https://www.pythonguis.com/installation/install-pyqt5-linux/#preparing-ubuntu-to-install-pyqt5)
    * [Installing the venv and pip](https://www.pythonguis.com/installation/install-pyqt5-linux/#installing-the-venv-and-pip)
    * [Creating a Virtual Environment](https://www.pythonguis.com/installation/install-pyqt5-linux/#creating-a-virtual-environment)
  * [Install PyQt5 in a Virtual Environment With pip](https://www.pythonguis.com/installation/install-pyqt5-linux/#install-pyqt5-in-a-virtual-environment-with-pip)
  * [Install PyQt5 System-wise Using apt](https://www.pythonguis.com/installation/install-pyqt5-linux/#install-pyqt5-system-wise-using-apt)
  * [Check the Installation](https://www.pythonguis.com/installation/install-pyqt5-linux/#check-the-installation)


## Preparing Ubuntu to Install PyQt5
Before installing PyQt5, we need to prepare our operating system and install a couple of tools. Python best practices recommend using [virtual environments](https://www.pythonguis.com/tutorials/python-virtual-environments/) to isolate our Python projects and manage their dependencies.
Unfortunately, the default Ubuntu installation doesn't include tools like the `venv` module, which allows us to create virtual environments, and the `pip` command, which lets us install external packages. So, we need to install them from the distro's repositories.
### Installing the `venv` and `pip`
To install the `venv` module and the `pip` command in Ubuntu, we can run the following commands:
bash ```
$ sudo apt update
$ sudo apt install python3-venv python3-pip

```

The first command updates the package information from all sources of software we are using in our Ubutu system. The second command downloads and installs the `venv` module and the `pip` command. Now, we are ready to create and activate a Python virtual environment. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
### Creating a Virtual Environment
Once we've installed the `venv` module, we can proceed to create and activate a Python virtual environment:
bash ```
$ mkdir project/ && cd project/
$ python3 -m venv ./venv
$ source venv/bin/activate
(venv) $

```

First, we create a new working directory named `project/` as a root for a hypothetical PyQt5 project. Then, we create a new virtual environment with `venv` and activate it. Note how the prompt indicator changes to signal that we're in an active virtual environment.
## Install PyQt5 in a Virtual Environment With `pip`
Once we've created and activated our virtual environment, we can install PyQt5 with the following command:
bash ```
(venv) $ pip3 install pyqt5

```

This command downloads PyQt5 from the [Python package index (PyPI)](https://pypi.org/) and installs it in our virtual environment.
## Install PyQt5 System-wise Using `apt`
Sometimes, we may need to install PyQt5 in the operating system rather than in a virtual environment. In Ubuntu's repositories, we'll find packages for PyQt5, although they may be out of date. Check first to ensure you're getting a version that meets your requirements, and if not, use the `pip` method above.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt5](https://www.pythonguis.com/static/theme/images/products/pyqt5-book.png)](https://www.pythonguis.com/pyqt5-book/)
[Take a look ](https://www.pythonguis.com/pyqt5-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/create-simple-gui-applications/) and [Amazon Paperback](https://www.amazon.com/dp/B08RB2HRS1/)
In Ubuntu, we can install either from the command line with the `apt` command or via the Software Center. The package we are looking for is `python3-pyqt5`.
To install PyQt5 from the command line, execute the following command:
bash ```
$ sudo apt install python3-pyqt5

```

## Check the Installation
After the PyQt5 installation is finished, we can start a Python interactive session and import the library as shown below to test your installation:
python ```
>>> import PyQt5

```

If you're using the `pip` installation, make sure you are in the terminal session with the active virtual environment. If you are using the `apt` installation, you can import the library from any terminal session.
Now that you've completed the installation in your Ubuntu Linux system, you can start [creating Python GUI applications with PyQt5](https://www.pythonguis.com/pyqt5-tutorial/). 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Install PyQt5 on Ubuntu Linux** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) with contributions from [Lalin Paranawithana](https://www.pythonguis.com/authors/lalin-paranawithana/) and [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/installation/install-pyqt5-linux/Python books) on the subject. 
**Install PyQt5 on Ubuntu Linux** was published in [installation](https://www.pythonguis.com/installation/) on May 21, 2019 (updated April 08, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[installation](https://www.pythonguis.com/topics/installation/) [linux](https://www.pythonguis.com/topics/linux/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
