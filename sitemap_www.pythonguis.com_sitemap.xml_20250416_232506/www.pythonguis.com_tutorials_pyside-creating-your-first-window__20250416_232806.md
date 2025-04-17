# Content from: https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/

[](https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PySide2 ](https://www.pythonguis.com/pyside2/)
  * [PySide2 Tutorial ](https://www.pythonguis.com/pyside2-tutorial/)
  * Basics
  * [Create a PySide2 app](https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/)
  * [PySide2 Signals](https://www.pythonguis.com/tutorials/pyside-signals-slots-events/)
  * [PySide2 Widgets](https://www.pythonguis.com/tutorials/pyside-widgets/)
  * [PySide2 Layouts](https://www.pythonguis.com/tutorials/pyside-layouts/)
  * [PySide2 Menus](https://www.pythonguis.com/tutorials/pyside-actions-toolbars-menus/)
  * [PySide2 Dialogs](https://www.pythonguis.com/tutorials/pyside-dialogs/)
  * [Multi-window PySide2](https://www.pythonguis.com/tutorials/pyside-creating-multiple-windows/)
  * Qt Designer
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/)
  * [The QResource System in PySide2](https://www.pythonguis.com/tutorials/pyside-qresource-system/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/pyside-qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/pyside-modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/pyside-qtableview-modelviews-numpy-pandas/)
  * Plotting
  * [Plotting With PyQtGraph and PySide2](https://www.pythonguis.com/tutorials/pyside-plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PySide2](https://www.pythonguis.com/tutorials/pyside-plotting-matplotlib/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/pyside-bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/pyside-creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/pyside-animated-widgets/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/pyside-embed-pyqtgraph-custom-widgets/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/pyside-transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/pyside-system-tray-mac-menu-bar-applications/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyside2-applications-windows-pyinstaller/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyside2-applications-pyinstaller-macos-dmg/)
  * [Packaging QResources](https://www.pythonguis.com/tutorials/packaging-data-files-pyside2-with-qresource-system/)
  * [Packaging with fbs](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/)
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


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Creating your first app with PySide2
A simple Hello World! application with Python and Qt
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 26 PySide2 [ Getting started with PySide ](https://www.pythonguis.com/pyside2-tutorial/#pyside-getting-started)
#### [ PySide2 Tutorial ](https://www.pythonguis.com/pyside2-tutorial/) — [Getting started with PySide](https://www.pythonguis.com/pyside2-tutorial/#pyside-getting-started)
  * [Creating your first app with PySide2](https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/)
  * [PySide2 Signals, Slots & Events](https://www.pythonguis.com/tutorials/pyside-signals-slots-events/)
  * [PySide2 Widgets](https://www.pythonguis.com/tutorials/pyside-widgets/)
  * [PySide2 Layouts](https://www.pythonguis.com/tutorials/pyside-layouts/)
  * [PySide2 Toolbars & Menus — QAction](https://www.pythonguis.com/tutorials/pyside-actions-toolbars-menus/)
  * [PySide2 Dialogs and Alerts](https://www.pythonguis.com/tutorials/pyside-dialogs/)
  * [Creating Additional Windows in PySide2](https://www.pythonguis.com/tutorials/pyside-creating-multiple-windows/)


This tutorial is also available for [PySide6](https://www.pythonguis.com/tutorials/pyside6-creating-your-first-window/) , [PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/) and [PyQt5](https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/)
In this tutorial we'll learn how to use PySide to create desktop applications with Python. First we'll create a series of simple windows on your desktop to ensure that PySide is working and introduce some of the basic concepts. Then we'll take a brief look at the event loop and how it relates to GUI programming in Python. Finally we'll look at Qt's `QMainWindow` which offers some useful common interface elements such as toolbars and menus. These will be explored in more detail in the subsequent tutorials.
Table of Contents
  * [Creating an application](https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/#creating-an-application)
    * [Stepping through the code](https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/#stepping-through-the-code)
  * [What's the event loop?](https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/#whats-the-event-loop)
  * [QMainWindow](https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/#qmainwindow)
  * [Sizing windows and widgets](https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/#sizing-windows-and-widgets)


## Creating an application
Let's create our first application! To start create a new Python file — you can call it whatever you like (e.g. `app.py`) and save it somewhere accessible. We'll write our simple app in this file.
We'll be editing within this file as we go along, and you may want to come back to earlier versions of your code, so remember to keep regular backups.
The source code for the application is shown below. Type it in verbatim, and be careful not to make mistakes. If you do mess up, Python will let you know what's wrong.
python ```
from PySide2.QtWidgets import QApplication, QWidget
# Only needed for access to command line arguments
import sys
# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)
# Create a Qt widget, which will be our window.
window = QWidget()
window.show() # IMPORTANT!!!!! Windows are hidden by default.
# Start the event loop.
app.exec_()

# Your application won't reach here until you exit and the event
# loop has stopped.

```

First, launch your application. You can run it from the command line like any other Python script, for example --
bash ```
python3 app.py

```

_Run it!_ You will now see your window. Qt automatically creates a window with the normal window decorations and you can drag it around and resize it like any window.
What you'll see will depend on what platform you're running this example on. The image below shows the window as displayed on Windows, macOS and Linux (Ubuntu). 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
![Our window, as seen on Windows, macOS and Linux.](https://www.pythonguis.com/static/tutorials/qt/creating-your-first-window/window.png) _Our window, as seen on Windows, macOS and Linux._
### Stepping through the code
Let's step through the code line by line, so we understand exactly what is happening.
First, we import the PySide classes that we need for the application. Here we're importing `QApplication`, the application handler and `QWidget`, a basic _empty_ GUI widget, both from the `QtWidgets` module.
python ```
from PySide2.QtWidgets import QApplication, QWidget

```

The main modules for Qt are `QtWidgets`, `QtGui` and `QtCore`.
You could do `from <module> import *` but this kind of global import is generally frowned upon in Python, so we'll avoid it here.
Next we create an instance of `QApplication`, passing in `sys.argv`, which is Python `list` containing the command line arguments passed to the application.
python ```
app = QApplication(sys.argv)

```

If you know you won't be using command line arguments to control Qt you can pass in an empty list instead, e.g.
python ```
app = QApplication([])

```

Next we create an instance of a `QWidget` using the variable name `window`.
python ```
window = QWidget()
window.show()

```

In Qt _all_ top level widgets are windows -- that is, they don't have a _parent_ and are not nested within another widget or layout. This means you can technically create a window using any widget you like.
Widgets _without a parent_ are invisible by default. So, after creating the `window` object, we must _always_ call `.show()` to make it visible. You can remove the `.show()` and run the app, but you'll have no way to quit it!
What is a window? - Holds the user-interface of your application - Every application needs at least one (...but can have more) - Application will (by default) exit when last window is closed
Finally, we call `app.exec_()` to start up the event loop.
## What's the event loop?
Before getting the window on the screen, there are a few key concepts to introduce about how applications are organised in the Qt world. If you're already familiar with event loops you can safely skip to the next section.
The core of every Qt Applications is the `QApplication` class. Every application needs one — and only one — `QApplication` object to function. This object holds the _event loop_ of your application — the core loop which governs all user interaction with the GUI.
![The event loop in Qt.](https://www.pythonguis.com/static/tutorials/qt/creating-your-first-window/event-loop.png)
Each interaction with your application — whether a press of a key, click of a mouse, or mouse movement — generates an _event_ which is placed on the _event queue_. In the event loop, the queue is checked on each iteration and if a waiting event is found, the event and control is passed to the specific _event handler_ for the event. The event handler deals with the event, then passes control back to the event loop to wait for more events. There is only _one_ running event loop per application.
The `QApplication` class - `QApplication` holds the Qt event loop - One `QApplication` instance required - Your application sits waiting in the event loop until an action is taken - There is only _one_ event loop at any time
## `QMainWindow`
As we discovered in the last part, in Qt _any_ widgets can be windows. For example, if you replace `QWidget` with `QPushButton`. In the example below, you would get a window with a single push-able button in it.
python ```
import sys
from PySide2.QtWidgets import QApplication, QPushButton
app = QApplication(sys.argv)
window = QPushButton("Push Me")
window.show()
app.exec_()

```

This is neat, but not really very _useful_ -- it's rare that you need a UI that consists of only a single control! But, as we'll discover later, the ability to nest widgets within other widgets using _layouts_ means you can construct complex UIs inside an empty `QWidget`.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
The underscore is in `exec_()` because `exec` was a reserved word in Python 2.7. PySide handles this by appending an underscore to the name used in the Qt library. You'll also see `.print_()` methods on widgets for example.
But, Qt already has a solution for you -- the `QMainWindow`. This is a pre-made widget which provides a lot of standard window features you'll make use of in your apps, including toolbars, menus, a statusbar, dockable widgets and more. We'll look at these advanced features later, but for now, we'll add a simple empty `QMainWindow` to our application.
python ```
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
app = QApplication(sys.argv)
window = QMainWindow()
window.show()
# Start the event loop.
app.exec_()

```

_Run it!_ You will now see your main window. It looks exactly the same as before!
So our `QMainWindow` isn't very interesting at the moment. We can fix that by adding some content. If you want to create a custom window, the best approach is to subclass `QMainWindow` and then include the setup for the window in the `__init__` block. This allows the window behavior to be self contained. We can add our own subclass of `QMainWindow` — call it `MainWindow` to keep things simple.
python ```
import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    button = QPushButton("Press Me!")
    # Set the central widget of the Window.
    self.setCentralWidget(button)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

For this demo we're using a `QPushButton`. The core Qt widgets are always imported from the `QtWidgets` namespace, as are the `QMainWindow` and `QApplication` classes. When using `QMainWindow` we use `.setCentralWidget` to place a widget (here a `QPushButton`) in the `QMainWindow` -- by default it takes the whole of the window. We'll look at how to add multiple widgets to windows in the layouts tutorial.
When you subclass a Qt class you must _always_ call the super `__init__` function to allow Qt to set up the object.
In our `__init__` block we first use `.setWindowTitle()` to change the title of our main window. Then we add our first widget — a `QPushButton` — to the middle of the window. This is one of the basic widgets available in Qt. When creating the button you can pass in the text that you want the button to display.
Finally, we call `.setCentralWidget()` on the window. This is a `QMainWindow` specific function that allows you to set the widget that goes in the middle of the window.
_Run it!_ You will now see your window again, but this time with the `QPushButton` widget in the middle. Pressing the button will do nothing, we'll sort that next.
![Our QMainWindow with a single QPushButton on Windows, macOS and Linux.](https://www.pythonguis.com/static/tutorials/qt/creating-your-first-window/window-button.png) _Our`QMainWindow` with a single `QPushButton` on Windows, macOS and Linux._
We'll cover more widgets in detail shortly but if you're impatient and would like to jump ahead you can take a look at the [QWidget documentation](http://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes). Try adding the different widgets to your window!
## Sizing windows and widgets
The window is currently freely resizable -- if you grab any corner with your mouse you can drag and resize it to any size you want. While it's good to let your users resize your applications, sometimes you may want to place restrictions on minimum or maximum sizes, or lock a window to a fixed size.
In Qt sizes are defined using a `QSize` object. This accepts _width_ and _height_ parameters in that order. For example, the following will create a _fixed size_ window of 400x300 pixels.
python ```
import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    button = QPushButton("Press Me!")
    self.setFixedSize(QSize(400, 300))
    # Set the central widget of the Window.
    self.setCentralWidget(button)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

_Run it!_ You will see a fixed size window -- try and resize it, it won't work.
![Our fixed-size window, notice that the _maximize_ control is disabled on Windows & Linux. On macOS you _can_ maximize the app to fill the screen, but the central widget will not resize.](https://www.pythonguis.com/static/tutorials/qt/creating-your-first-window/window-fixed.png) _Our fixed-size window, notice that the maximize control is disabled on Windows & Linux. On macOS you can maximize the app to fill the screen, but the central widget will not resize._
As well as `.setFixedSize()` you can also call `.setMinimumSize()` and `.setMaximumSize()` to set the minimum and maximum sizes respectively. Experiment with this yourself!
You can use these size methods on _any_ widget.
In this section we've covered the `QApplication` class, the `QMainWindow` class, the event loop and experimented with adding a simple widget to a window. In the next section we'll take a look at the mechanisms Qt provides for widgets and windows to communicate with one another and your own code.
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
Continue with [ PySide2 Tutorial ](https://www.pythonguis.com/tutorials/pyside-signals-slots-events/ "Continue to next part")
Return to [Create Desktop GUI Applications with PySide2 ](https://www.pythonguis.com/pyside2-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Creating your first app with PySide2** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/Python books) on the subject. 
**Creating your first app with PySide2** was published in [tutorials](https://www.pythonguis.com/tutorials/) on May 13, 2021 (updated November 26, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyside2](https://www.pythonguis.com/topics/pyside2/) [app](https://www.pythonguis.com/topics/app/) [window](https://www.pythonguis.com/topics/window/) [tutorial](https://www.pythonguis.com/topics/tutorial/) [qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ getting-started](https://www.pythonguis.com/topics/getting-started/) [ pyside2-getting-started](https://www.pythonguis.com/topics/pyside2-getting-started/) [python](https://www.pythonguis.com/topics/python/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
