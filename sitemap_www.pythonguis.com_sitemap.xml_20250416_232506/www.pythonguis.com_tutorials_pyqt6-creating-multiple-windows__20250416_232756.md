# Content from: https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/

[](https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/#menu)
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
# Creating Additional Windows in PyQt6
Opening new windows for your application
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 01 This article has been updated for PyQt6. PyQt6 [ Getting started with PyQt6 ](https://www.pythonguis.com/pyqt6-tutorial/#pyqt6-start)
#### [ PyQt6 Tutorial ](https://www.pythonguis.com/pyqt6-tutorial/) — [Getting started with PyQt6](https://www.pythonguis.com/pyqt6-tutorial/#pyqt6-start)
  * [Creating your first app with PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/)
  * [PyQt6 Signals, Slots & Events](https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/)
  * [PyQt6 Widgets](https://www.pythonguis.com/tutorials/pyqt6-widgets/)
  * [PyQt6 Layouts](https://www.pythonguis.com/tutorials/pyqt6-layouts/)
  * [PyQt6 Toolbars & Menus — QAction](https://www.pythonguis.com/tutorials/pyqt6-actions-toolbars-menus/)
  * [PyQt6 Dialogs and Alerts](https://www.pythonguis.com/tutorials/pyqt6-dialogs/)
  * [Creating Additional Windows in PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/)


This tutorial is also available for [PySide6](https://www.pythonguis.com/tutorials/pyside6-creating-multiple-windows/) , [PySide2](https://www.pythonguis.com/tutorials/pyside-creating-multiple-windows/) and [PyQt5](https://www.pythonguis.com/tutorials/creating-multiple-windows/)
In an earlier tutorial we've already covered how to open _dialog_ windows. These are special windows which (by default) grab the focus of the user, and run their own event loop, effectively blocking the execution of the rest of your app.
However, quite often you will want to open a second window in an application, without interrupting the main window -- for example, to show the output of some long-running process, or display graphs or other visualizations. Alternatively, you may want to create an application that allows you to work on multiple documents at once, in their own windows.
It's relatively straightforward to open new windows but there are a few things to keep in mind to make sure they work well. In this tutorial we'll step through how to create a new window, and how to show and hide external windows on demand.
Table of Contents
  * [Creating a new window](https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/#creating-a-new-window)
  * [Toggling a window](https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/#toggling-a-window)
  * [Persistent windows](https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/#persistent-windows)
    * [Showing & hiding persistent windows](https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/#showing-hiding-persistent-windows)
  * [Multiple windows](https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/#multiple-windows)


## Creating a new window
In Qt any widget without a parent is a window. This means, to show a new window you just need to create a new instance of a widget. This can be any widget type (technically any subclass of `QWidget`) including another `QMainWindow` if you prefer.
There is no restriction on the number of `QMainWindow` instances you can have. If you _need_ toolbars or menus on your second window you will have to use a `QMainWindow` to achieve this. This can get confusing for users however, so make sure it's necessary.
As with your main window, _creating_ a window is not sufficient, you must also show it.
python ```
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys

class AnotherWindow(QWidget):
  """
  This "window" is a QWidget. If it has no parent, it
  will appear as a free-floating window as we want.
  """
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout()
    self.label = QLabel("Another Window")
    layout.addWidget(self.label)
    self.setLayout(layout)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.button = QPushButton("Push for Window")
    self.button.clicked.connect(self.show_new_window)
    self.setCentralWidget(self.button)
  def show_new_window(self, checked):
    w = AnotherWindow()
    w.show()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

```

![A main window with a button to launch a child window,](https://www.pythonguis.com/static/tutorials/qt/creating-multiple-windows/window1.jpg) _A main window with a button to launch a child window,_
1:1 Coaching & Tutoring for your Python GUIs project
[![Martin Fitzpatrick Python GUIs Coaching & Training](https://www.pythonguis.com/static/theme/images/products/coaching.jpg)](https://calendly.com/martinfitzpatrick/60min-python-guis-coaching)
[60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/) [Book Now](https://www.pythonguis.com/live/)
1:1 Python GUIs Coaching & Training
**Comprehensive code review** • **Bugfixes** & improvements • **Maintainability** advice and **architecture** improvements • **Design and usability** assessment • Suggestions and tips to **expand your knowledge** • **Packaging and distribution** help for Windows, Mac & Linux • [Find out more.](https://www.pythonguis.com/live)
If you run this, you'll see the main window. Clicking the button _may_ show the second window, but if you see it it will only be visible for a fraction of a second. What's happening?
python ```
  def show_new_window(self, checked):
    w = AnotherWindow()
    w.show()

```

Inside this method, we are creating our window (widget) object, storing it in the variable `w` and showing it. However, once we leave the method we no longer have a reference to the `w` variable (it is a _local_ variable) and so it will be cleaned up – and the window destroyed. To fix this we need to keep a reference to the window _somewhere_ , for example on the `self` object.
python ```
  def show_new_window(self, checked):
    self.w = AnotherWindow()
    self.w.show()

```

Now, when you click the button to show the new window, it will persist.
However, what happens if you click the button again? The window will be re-created! This new window will replace the old in the `self.w` variable, and – because there is now no reference to it – the previous window will be destroyed.
You can see this in action if you change the window definition to show a random number in the label each time it is created.
python ```
from random import randint

class AnotherWindow(QWidget):
  """
  This "window" is a QWidget. If it has no parent, it
  will appear as a free-floating window as we want.
  """
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout()
    self.label = QLabel("Another Window % d" % randint(0,100))
    layout.addWidget(self.label)
    self.setLayout(layout)

```

The `__init__` block is only run when _creating_ the window. If you keep clicking the button the number will change, showing that the window is being re-created.
One solution is to simply check whether the window has already being created before creating it. The example below shows this in action.
python ```
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys
from random import randint

class AnotherWindow(QWidget):
  """
  This "window" is a QWidget. If it has no parent, it
  will appear as a free-floating window as we want.
  """
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout()
    self.label = QLabel("Another Window % d" % randint(0,100))
    layout.addWidget(self.label)
    self.setLayout(layout)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.w = None # No external window yet.
    self.button = QPushButton("Push for Window")
    self.button.clicked.connect(self.show_new_window)
    self.setCentralWidget(self.button)
  def show_new_window(self, checked):
    if self.w is None:
      self.w = AnotherWindow()
    self.w.show()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

```

![Child window with a label randomly generated on creation.](https://www.pythonguis.com/static/tutorials/qt/creating-multiple-windows/window2.jpg) _Child window with a label randomly generated on creation._
Using the button you can pop up the window, and use the window controls to close it. If you click the button again, the same window will re-appear.
This approach is fine for windows that you create temporarily – for example if you want to pop up a window to show a particular plot, or log output. However, for many applications you have a number of standard windows that you want to be able to show/hide them on demand.
In the next part we'll look at how to work with these types of windows.
## Toggling a window
Often you'll want to toggle the display of a window using an action on a toolbar or in a menu. As we previously saw, if no reference to a window is kept, it will be discarded (and closed). We can use this behaviour to close a window, replacing the `show_new_window` method from the previous example with –
python ```
  def show_new_window(self, checked):
    if self.w is None:
      self.w = AnotherWindow()
      self.w.show()
    else:
      self.w = None # Discard reference, close window.

```

By setting `self.w` to `None` the reference to the window will be lost, and the window will close. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
If we set it to any other value that `None` the window will still close, but the `if self.w is None` test will not pass the next time we click the button and so we will not be able to recreate a window.
This will only work if you have not kept a reference to this window somewhere else. To make sure the window closes regardless, you may want to explicitly call `.close()` on it. The full example is shown below.
python ```
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys
from random import randint

class AnotherWindow(QWidget):
  """
  This "window" is a QWidget. If it has no parent, it
  will appear as a free-floating window as we want.
  """
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout()
    self.label = QLabel("Another Window % d" % randint(0,100))
    layout.addWidget(self.label)
    self.setLayout(layout)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.w = None # No external window yet.
    self.button = QPushButton("Push for Window")
    self.button.clicked.connect(self.show_new_window)
    self.setCentralWidget(self.button)
  def show_new_window(self, checked):
    if self.w is None:
      self.w = AnotherWindow()
      self.w.show()
    else:
      self.w.close() # Close window.
      self.w = None # Discard reference.

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

```

## Persistent windows
So far we've looked at how to create new windows on demand. However, sometimes you have a number of standard application windows. In this case rather than create the windows when you want to show them, it can often make more sense to create them at start-up, then use `.show()` to display them when needed.
In the following example we create our external window in the `__init__` block for the main window, and then our `show_new_window` method simply calls `self.w.show()` to display it.
python ```
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys
from random import randint

class AnotherWindow(QWidget):
  """
  This "window" is a QWidget. If it has no parent, it
  will appear as a free-floating window as we want.
  """
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout()
    self.label = QLabel("Another Window % d" % randint(0,100))
    layout.addWidget(self.label)
    self.setLayout(layout)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.w = AnotherWindow()
    self.button = QPushButton("Push for Window")
    self.button.clicked.connect(self.show_new_window)
    self.setCentralWidget(self.button)
  def show_new_window(self, checked):
    self.w.show()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

```

If you run this, clicking on the button will show the window as before. However, note that the window is only created once and calling `.show()` on an already visible window has no effect.
### Showing & hiding persistent windows
Once you have created a persistent window you can show and hide it without recreating it. Once hidden the window still exists, but will not be visible and accept mouse/other input. However you can continue to call methods on the window and update it's state -- including changing it's appearance. Once re-shown any changes will be visible.
Below we update our main window to create a `toggle_window` method which checks, using `.isVisible()` to see if the window is currently visible. If it is not, it is shown using `.show()` , if it is already visible we hide it with `.hide()`.
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.w = AnotherWindow()
    self.button = QPushButton("Push for Window")
    self.button.clicked.connect(self.toggle_window)
    self.setCentralWidget(self.button)
  def toggle_window(self, checked):
    if self.w.isVisible():
      self.w.hide()
    else:
      self.w.show()

```

The complete working example of this persistent window and toggling the show/hide state is shown below.
python ```
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys
from random import randint

class AnotherWindow(QWidget):
  """
  This "window" is a QWidget. If it has no parent, it
  will appear as a free-floating window as we want.
  """
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout()
    self.label = QLabel("Another Window % d" % randint(0,100))
    layout.addWidget(self.label)
    self.setLayout(layout)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.w = AnotherWindow()
    self.button = QPushButton("Push for Window")
    self.button.clicked.connect(self.toggle_window)
    self.setCentralWidget(self.button)
  def toggle_window(self, checked):
    if self.w.isVisible():
      self.w.hide()
    else:
      self.w.show()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

```

Note that, again, the window is only created once -- the window's `__init__` block is not re-run (so the number in the label does not change) each time the window is re-shown.
## Multiple windows
You can use the same principle for creating multiple windows -- as long as you keep a reference to the window, things will work as expected. The simplest approach is to create a separate method to toggle the display of each of the windows.
python ```
import sys
from random import randint
from PyQt6.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QWidget,
)

class AnotherWindow(QWidget):
  """
  This "window" is a QWidget. If it has no parent,
  it will appear as a free-floating window.
  """
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout()
    self.label = QLabel("Another Window % d" % randint(0, 100))
    layout.addWidget(self.label)
    self.setLayout(layout)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.window1 = AnotherWindow()
    self.window2 = AnotherWindow()
    l = QVBoxLayout()
    button1 = QPushButton("Push for Window 1")
    button1.clicked.connect(self.toggle_window1)
    l.addWidget(button1)
    button2 = QPushButton("Push for Window 2")
    button2.clicked.connect(self.toggle_window2)
    l.addWidget(button2)
    w = QWidget()
    w.setLayout(l)
    self.setCentralWidget(w)
  def toggle_window1(self, checked):
    if self.window1.isVisible():
      self.window1.hide()
    else:
      self.window1.show()
  def toggle_window2(self, checked):
    if self.window2.isVisible():
      self.window2.hide()
    else:
      self.window2.show()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

```

![A mainwindow with two child windows.](https://www.pythonguis.com/static/tutorials/qt/creating-multiple-windows/window7.jpg) _A mainwindow with two child windows._
However, you can also create a generic method which handles toggling for all windows -- see [transmitting extra data with Qt signals](https://www.pythonguis.com/tutorials/pyqt6-transmitting-extra-data-qt-signals/) for a detailed explanation of how this works. The example below shows that in action, using a `lambda` function to intercept the signal from each button and pass through the appropriate window. We can also discard the `checked` value since we aren't using it.
python ```
import sys
from random import randint
from PyQt6.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QWidget,
)

class AnotherWindow(QWidget):
  """
  This "window" is a QWidget. If it has no parent,
  it will appear as a free-floating window.
  """
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout()
    self.label = QLabel("Another Window % d" % randint(0, 100))
    layout.addWidget(self.label)
    self.setLayout(layout)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.window1 = AnotherWindow()
    self.window2 = AnotherWindow()
    l = QVBoxLayout()
    button1 = QPushButton("Push for Window 1")
    button1.clicked.connect(
      lambda checked: self.toggle_window(self.window1)
    )
    l.addWidget(button1)
    button2 = QPushButton("Push for Window 2")
    button2.clicked.connect(
      lambda checked: self.toggle_window(self.window2)
    )
    l.addWidget(button2)
    w = QWidget()
    w.setLayout(l)
    self.setCentralWidget(w)
  def toggle_window(self, window):
    if window.isVisible():
      window.hide()
    else:
      window.show()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

```

[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Creating Additional Windows in PyQt6** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/Python books) on the subject. 
**Creating Additional Windows in PyQt6** was published in [tutorials](https://www.pythonguis.com/tutorials/) on October 06, 2021 (updated April 01, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[window](https://www.pythonguis.com/topics/window/) [windows](https://www.pythonguis.com/topics/windows/) [qt](https://www.pythonguis.com/topics/qt/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ foundation](https://www.pythonguis.com/topics/foundation/) [ pyqt6-foundation](https://www.pythonguis.com/topics/pyqt6-foundation/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
