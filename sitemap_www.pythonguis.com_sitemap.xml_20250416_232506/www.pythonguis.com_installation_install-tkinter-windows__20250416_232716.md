# Content from: https://www.pythonguis.com/installation/install-tkinter-windows/

[](https://www.pythonguis.com/installation/install-tkinter-windows/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [Tkinter ](https://www.pythonguis.com/tkinter/)
  * [Tkinter Tutorial ](https://www.pythonguis.com/tkinter-tutorial/)
  * Basics
  * [First Tkinter GUI](https://www.pythonguis.com/tutorials/create-gui-tkinter/)
  * [Design Tkinter Layout](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/)
  * [Buttons in Tkinter](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/)
  * [Pack Layouts](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/)
  * [Grid Layouts](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/)
  * [Place Layouts](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-place-layout-manager/)
  * [Radio & Check Buttons](https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-tkinter-applications-windows-pyinstaller/)
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
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Install Tkinter on Windows
Install Tkinter on Windows 8, 10 & 11
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Feb 28 Tkinter [ Installation Guides ](https://www.pythonguis.com/installation/)
This tutorial is also available for [PyQt6](https://www.pythonguis.com/installation/install-pyqt6-windows/) , [PySide6](https://www.pythonguis.com/installation/install-pyside6-windows/) , [PyQt5](https://www.pythonguis.com/installation/install-pyqt5-windows/) and [PySide2](https://www.pythonguis.com/installation/install-pyside2-windows/)
Before you start building GUI applications with Tkinter you will need a working installation of Python & Tkinter on your computer. Helpfully, **Tkinter is installed by default with every Python installation** on Windows, so you don't need to install it separately. Just download and install Python and you will have Tkinter available to you.
See below for instructions on how to install Python if you do not already have it set up.
## Installing Python on Windows
Go to the official Python website's [Windows downloads page](https://www.python.org/downloads/windows/) and download one of the Stable Releases of Python.
![Download the latest version of Python](https://www.pythonguis.com/static/images/python/python-windows-downloads.png) _You can download any of the stable versions._
You typically want to download the **Windows Installer (64-bit)** for modern hardware. Unless you _know_ you need the 32 bit version, try the 64-bit first.
Once the download is complete, double click the installer to launch it.
![The Python for Windows installer](https://www.pythonguis.com/static/images/python/installer.png) _The Python for Windows installer. Ensure sure Add python.exe to PATH is checked._
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
You'll see the installer welcome screen which describes what the installer will do.
Make sure that Add python.exe to PATH is checked in the installer. This makes it easier to use Python from the command prompt -- you just need to enter "python" to start, rather than the full path to the executable.
When you are ready to being the installation you can click _Install Now_.
![Installing Python](https://www.pythonguis.com/static/images/python/installing.png) _Installing Python._
The install will proceed as normal, installing all the required libraries (including Tcl/Tk for Tkinter). Once complete you can exit the installer.
Open a command prompt and start python by entering `python`. This will start the Python REPL, where you can enter interactive Python code.
![The Python REPL](https://www.pythonguis.com/static/images/python/python.png) _The Python REPL for our newly installed Python installation._
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
You can enter `from tkinter import *` to confirm that Tkinter has been installed and create a window with `Window = Tk()` to confirm it is usable.
![Importing Tkinter and creating a window in the Python REPL](https://www.pythonguis.com/static/images/python/python-import-tkinter.png) _Importing Tkinter and creating a window in the Python REPL._
You can run Python scripts from the command prompt by entering `python` followed by the script name. Create a file in your code editor and enter the following simple Tkinter example:
python ```
from tkinter import *
Window = Tk()
Window.mainloop()

```

Save the file as `my_tkinter_app.py` in your home folder `/Users/<your username>`. You can now launch this from the command prompt -- as long as you are in the same folder as the script -- using `python my_tkinter_app.py`.
![Running a Tkinter script from the command line](https://www.pythonguis.com/static/images/python/python-tkinter-script.png) _Running a Tkinter script from the command line._
That's it! You can now continue to the [Tkinter tutorial](https://www.pythonguis.com/www.pythonguis.com/tkinter-tutorial) to start creating your own Tkinter applications!
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Install Tkinter on Windows** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/installation/install-tkinter-windows/Python books) on the subject. 
**Install Tkinter on Windows** was published in [installation](https://www.pythonguis.com/installation/) on May 21, 2019 (updated February 28, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[installation](https://www.pythonguis.com/topics/installation/) [windows](https://www.pythonguis.com/topics/windows/) [tkinter](https://www.pythonguis.com/topics/tkinter/) [tk](https://www.pythonguis.com/topics/tk/)
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
