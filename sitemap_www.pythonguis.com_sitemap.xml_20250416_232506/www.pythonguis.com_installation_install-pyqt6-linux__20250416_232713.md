# Content from: https://www.pythonguis.com/installation/install-pyqt6-linux/

[](https://www.pythonguis.com/installation/install-pyqt6-linux/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PyQt6 ](https://www.pythonguis.com/pyqt6/)
  * [PyQt6 Tutorial ](https://www.pythonguis.com/pyqt6-tutorial/)
  * Basics
  * [Create a PyQt6 app](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/)
  * [PyQt6 Signals](https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/)
  * [PyQt6 Widgets](https://www.pythonguis.com/tutorials/pyqt6-widgets/)
  * [PyQt6 Layouts](https://www.pythonguis.com/tutorials/pyqt6-layouts/)
  * [PyQt6 Menus](https://www.pythonguis.com/tutorials/pyqt6-actions-toolbars-menus/)
  * [PyQt6 Dialogs](https://www.pythonguis.com/tutorials/pyqt6-dialogs/)
  * [Multi-window PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/)
  * Qt Designer
  * [First Qt Designer app](https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/)
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/pyqt6-qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/pyqt6-creating-dialogs-qt-designer/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyqt6-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/pyqt6-qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/pyqt6-qtableview-modelviews-numpy-pandas/)
  * Plotting
  * [Plotting With PyQtGraph and PyQt6](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PyQt6](https://www.pythonguis.com/tutorials/pyqt6-plotting-matplotlib/)
  * QGraphics
  * [Vector Graphics](https://www.pythonguis.com/tutorials/pyqt6-qgraphics-vector-graphics/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/pyqt6-bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/pyqt6-creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/pyqt6-embed-pyqtgraph-custom-widgets-qt-app/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/pyqt6-transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/pyqt6-system-tray-mac-menu-bar-applications/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyqt6-applications-windows-pyinstaller/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyqt6-applications-pyinstaller-macos-dmg/)
  * Resources
  * [Books](https://www.pythonguis.com/books/)
  * Services
  * [Consulting](https://www.pythonguis.com/hire/)
  * [1:1 Coaching](https://www.pythonguis.com/live/)
  * [Contact](https://www.pythonguis.com/contact/)
  * [About](https://www.pythonguis.com/about/)
  * Libraries
  * [PySide6](https://www.pythonguis.com/pyside6/)
  * [PyQt5](https://www.pythonguis.com/pyqt5/)
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Install PyQt6 on Ubuntu Linux
Install PyQt6 on Ubuntu and other Debian-based Linux distributions
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 08 PyQt6 [ Installation Guides ](https://www.pythonguis.com/installation/)
This tutorial is also available for [PySide2](https://www.pythonguis.com/installation/install-pyside2-linux/) , [PySide6](https://www.pythonguis.com/installation/install-pyside6-linux/) , [PyQt5](https://www.pythonguis.com/installation/install-pyqt5-linux/) and [Tkinter](https://www.pythonguis.com/installation/install-tkinter-linux/)
Before you start creating GUI applications with [PyQt6](https://www.pythonguis.com/pyqt6-tutorial/), you need to have a working installation of PyQt6 on your system. In this short tutorial, you'll find the steps that will guide you through installing PyQt6 on Ubuntu Linux.
This guide is also available for [macOS](https://www.pythonguis.com/installation/install-pyqt6-mac/) and [Windows](https://www.pythonguis.com/installation/install-pyqt6-windows/).
Note that the following instructions are for installing the PyQt6 version registered under the _GPL license_. If you need to use PyQt in a non-GPL project, then you will need to purchase an alternative license from [Riverbank Computing](https://www.riverbankcomputing.com) to release your software.
Table of Contents
  * [Preparing Ubuntu to Install PyQt6](https://www.pythonguis.com/installation/install-pyqt6-linux/#preparing-ubuntu-to-install-pyqt6)
    * [Installing the venv and pip](https://www.pythonguis.com/installation/install-pyqt6-linux/#installing-the-venv-and-pip)
    * [Creating a Virtual Environment](https://www.pythonguis.com/installation/install-pyqt6-linux/#creating-a-virtual-environment)
  * [Install PyQt6 in a Virtual Environment With pip](https://www.pythonguis.com/installation/install-pyqt6-linux/#install-pyqt6-in-a-virtual-environment-with-pip)
  * [Install PyQt6 System-wise Using apt](https://www.pythonguis.com/installation/install-pyqt6-linux/#install-pyqt6-system-wise-using-apt)
  * [Check the Installation](https://www.pythonguis.com/installation/install-pyqt6-linux/#check-the-installation)


## Preparing Ubuntu to Install PyQt6
Before installing PyQt6, we need to prepare our operating system and install a couple of tools. Python best practices recommend using [virtual environments](https://www.pythonguis.com/tutorials/python-virtual-environments/) to isolate our Python projects and manage their dependencies.
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

First, we create a new working directory named `project/` as a root for a hypothetical PyQt6 project. Then, we create a new virtual environment with `venv` and activate it. Note how the prompt indicator changes to signal that we're in an active virtual environment.
## Install PyQt6 in a Virtual Environment With `pip`
Once we've created and activated our virtual environment, we can install PyQt6 with the following command:
bash ```
(venv) $ pip3 install pyqt6

```

This command downloads PyQt6 from the [Python package index (PyPI)](https://pypi.org/) and installs it in our virtual environment.
## Install PyQt6 System-wise Using `apt`
Sometimes, we may need to install PyQt6 in the operating system rather than in a virtual environment. In Ubuntu's repositories, we'll find packages for PyQt6, although they may be out of date. Check first to ensure you're getting a version that meets your requirements, and if not, use the `pip` method above. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
In Ubuntu, we can install either from the command line with the `apt` command or via the Software Center. The package we are looking for is `python3-pyqt6`.
To install PyQt6 from the command line, execute the following command:
bash ```
$ sudo apt install python3-pyqt6

```

## Check the Installation
After the PyQt6 installation is finished, we can start a Python interactive session and import the library as shown below to test your installation:
python ```
>>> import PyQt6

```

If you're using the `pip` installation, make sure you are in the terminal session with the active virtual environment. If you are using the `apt` installation, you can import the library from any terminal session.
Now that you've completed the installation in your Ubuntu Linux system, you can start [creating Python GUI applications with PyQt6](https://www.pythonguis.com/pyqt6-tutorial/).
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Install PyQt6 on Ubuntu Linux** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) with contributions from [Lalin Paranawithana](https://www.pythonguis.com/authors/lalin-paranawithana/) and [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/installation/install-pyqt6-linux/Python books) on the subject. 
**Install PyQt6 on Ubuntu Linux** was published in [installation](https://www.pythonguis.com/installation/) on May 21, 2021 (updated April 08, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[installation](https://www.pythonguis.com/topics/installation/) [linux](https://www.pythonguis.com/topics/linux/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
