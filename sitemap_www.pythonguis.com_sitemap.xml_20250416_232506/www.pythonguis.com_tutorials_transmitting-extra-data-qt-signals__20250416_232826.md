# Content from: https://www.pythonguis.com/tutorials/transmitting-extra-data-qt-signals/

[](https://www.pythonguis.com/tutorials/transmitting-extra-data-qt-signals/#menu)
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
# Transmitting Extra Data With Qt Signals in PyQt5
Modifying widget signals to pass contextual information to slots
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Mar 15 PyQt5 [ Extended UI features with PyQt5 ](https://www.pythonguis.com/pyqt5-tutorial/#advanced-ui-features)
#### [ PyQt5 Tutorial ](https://www.pythonguis.com/pyqt5-tutorial/) — [Extended UI features with PyQt5](https://www.pythonguis.com/pyqt5-tutorial/#advanced-ui-features)
  * [Transmitting Extra Data With Qt Signals in PyQt5](https://www.pythonguis.com/tutorials/transmitting-extra-data-qt-signals/)
  * [System Tray & Mac Menu Bar Applications in PyQt5](https://www.pythonguis.com/tutorials/system-tray-mac-menu-bar-applications-pyqt/)


This tutorial is also available for [PySide6](https://www.pythonguis.com/tutorials/pyside6-transmitting-extra-data-qt-signals/) , [PyQt6](https://www.pythonguis.com/tutorials/pyqt6-transmitting-extra-data-qt-signals/) and [PySide2](https://www.pythonguis.com/tutorials/pyside-transmitting-extra-data-qt-signals/)
Signals are a neat feature of Qt that allow you to pass messages between different components in your applications.
Signals are connected to _slots_ which are functions (or methods) which will be run every time the signal fires. Many signals also transmit data, providing information about the state change or widget that fired them. The receiving slot can use this data to perform different actions in response to the same signal.
However, there is a limitation: the signal can only emit the data it was designed to. So for example, a `QAction` has a `.triggered` that fires when that particular action has been activated. The triggered signal emits a single piece of data -- the _checked_ state of the action after being triggered.
For non-checkable actions, this value will always be `False`
The receiving function does not know _which_ `QAction` triggered it, or receiving any other data about it.
This is usually fine. You can tie a particular action to a unique function which does precisely what that action requires. Sometimes however you need the _slot_ function to know more than that `QAction` is giving it. This could be the object the signal was triggered on, or some other associated metadata which your slot needs to perform the intended result of the signal.
This is a powerful way to extend or modify the built-in signals provided by Qt. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Table of Contents
  * [Intercepting the signal](https://www.pythonguis.com/tutorials/transmitting-extra-data-qt-signals/#intercepting-the-signal)
  * [Trouble with loops](https://www.pythonguis.com/tutorials/transmitting-extra-data-qt-signals/#trouble-with-loops)


## Intercepting the signal
Instead of connecting signal directly to the target function, you instead use an intermediate function to intercept the signal, modify the signal data and forward that on to your actual slot function.
This slot function must accept the value sent by the signal (here the `checked` state) and then call the _real_ slot, passing any additional data with the arguments.
python ```
def fn(checked):
  self.handle_trigger(checked, <additional args>)

```

Rather than defining this intermediate function, you can also achieve the same thing using a `lambda` function. As above, this accepts a single parameter `checked` and then calls the real slot.
python ```
lambda checked: self.handle_trigger(checked, <additional args>)

```

In both examples the `<additional args>` can be replaced with anything you want to forward to your slot. In the example below we're forwarding the `QAction` object `action` to the receiving slot.
python ```
action = QAction()
action.triggered.connect( lambda checked: self.handle_trigger(checked, action) )

```

Our `handle_trigger` slot method will receive both the original `checked` value and the `QAction` object. Or receiving slot can look something like this
python ```
# a class method.
def handled_trigger(self, checked, action):
  # do something here.

```

Below are a few examples using this approach to modify the data sent with the `MainWindow.windowTitleChanged` signal.
python ```
from PyQt5.QtWidgets import (
  QApplication, QMainWindow
)
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    # SIGNAL: The connected function will be called whenever the window
    # title is changed. The new title will be passed to the function.
    self.windowTitleChanged.connect(self.on_window_title_changed)
    # SIGNAL: The connected function will be called whenever the window
    # title is changed. The new title is discarded and the
    # function is called without parameters.
    self.windowTitleChanged.connect(lambda x: self.on_window_title_changed_no_params())
    # SIGNAL: The connected function will be called whenever the window
    # title is changed. The new title is discarded and the
    # function is called without parameters.
    # The function has default params.
    self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
    # SIGNAL: The connected function will be called whenever the window
    # title is changed. The new title is passed to the function
    # and replaces the default parameter. Extra data is passed from
    # within the lambda.
    self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))
    # This sets the window title which will trigger all the above signals
    # sending the new title to the attached functions or lambdas as the
    # first parameter.
    self.setWindowTitle("My Signals App")
  # SLOT: This accepts a string, e.g. the window title, and prints it
  def on_window_title_changed(self, s):
    print(s)
  # SLOT: This is called when the window title changes.
  def on_window_title_changed_no_params(self):
    print("Window title changed.")
  # SLOT: This has default parameters and can be called without a value
  def my_custom_fn(self, a="HELLLO!", b=5):
    print(a, b)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

```

The `.setWindowTitle` call at the end of the `__init__` block changes the window title and triggers the `.windowTitleChanged` signal, which emits the new window title as a `str`. We've attached a series of intermediate slot functions (as `lambda` functions) which modify this signal and then call our custom slots with different parameters.
Running this produces the following output.
bash ```
My Signals App
Window title changed.
HELLLO! 5
My Signals App 5
My Signals App 25

```

The intermediate functions can be as simple or as complicated as you like -- as well as discarding/adding parameters, you can also perform lookups to _modify_ signals to different values.
In the following example a checkbox signal `Qt.Checked` or `Qt.Unchecked` is modified by an intermediate slot into a `bool` value.
python ```
from PyQt5.QtWidgets import (
  QApplication, QMainWindow, QCheckBox
)
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    checkbox = QCheckBox("Check?")
    # Option 1: conversion function
    def checkstate_to_bool(state):
      if state == Qt.Checked:
        return self.result(True)
      return self.result(False)
    checkbox.stateChanged.connect(checkstate_to_bool)
    # Option 2: dictionary lookup
    _convert = {
      Qt.Checked: True,
      Qt.Unchecked: False
    }
    checkbox.stateChanged.connect(
      lambda v: self.result(_convert[v])
    )
    self.setCentralWidget(checkbox)
  # SLOT: Accepts the check value.
  def result(self, v):
    print(v)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

```

In this example we've connected the `.stateChange` signal to `result` in two ways -- a) with a intermediate function which calls the `.result` method with `True` or `False` depending on the signal parameter, and b) with a dictionary lookup within an intermediate `lambda`.
Running this code will output `True` or `False` to the command line each time the state is changed (once for each time we connect to the signal).
![QCheckbox triggering 2 slots, with modified signal data](https://www.pythonguis.com/static/tutorials/qt/transmitting-extra-data-qt-signals/checkbox.png) _QCheckbox triggering 2 slots, with modified signal data_
## Trouble with loops
One of the most common reasons for wanting to connect signals in this way is when you're building a series of objects and connecting signals programmatically in a loop. Unfortunately then things aren't always so simple.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
If you try and construct intercepted signals while looping over a variable, and want to pass the loop variable to the receiving slot, you'll hit a problem. For example, in the following code we create a series of buttons, and use a intermediate function to pass the buttons _value_ (0-9) with the pressed signal.
python ```
from PyQt5.QtWidgets import (
  QApplication, QMainWindow, QAction, QPushButton,
  QWidget, QLabel, QVBoxLayout, QHBoxLayout
)
import sys
class Window(QWidget):
  def __init__(self):
    super().__init__()
    v = QVBoxLayout()
    h = QHBoxLayout()
    for a in range(10):
      button = QPushButton(str(a))
      button.pressed.connect(
        lambda: self.button_pressed(a)
      )
      h.addWidget(button)
    v.addLayout(h)
    self.label = QLabel("")
    v.addWidget(self.label)
    self.setLayout(v)
  def button_pressed(self, n):
    self.label.setText(str(n))

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec_()

```

If you run this you'll see the problem -- no matter which button you click on you get the same number (9) shown on the label. Why 9? It's the last value of the loop.
The problem is the line `lambda: self.button_pressed(a)` where we pass `a` to the final `button_pressed` slot. In this context, `a` is bound to the loop.
python ```
for a in range(10):
  # .. snip ...
  button.pressed.connect(
    lambda: self.button_pressed(a)
  )
  # .. snip ...

```

We are not passing the _value_ of `a` when the button is created, but whatever value `a` has when the signal fires. Since the signal fires after the loop is completed -- we interact with the UI after it is created -- the value of `a` for _every_ signal is the final value that `a` had in the loop: 9.
So clicking any of them will send 9 to `button_pressed`
The solution is to pass the value in as a (re-)named parameter. This binds the parameter to the _value_ of `a` at that point in the loop, creating a new, un-connected variable. The loop continues, but the bound variable is not altered.
This ensures the correct value whenever it is called.
python ```
lambda val=a: self.button_pressed(val)

```

You don't _have_ to rename the variable, you could also choose to use the same name for the bound value.
python ```
lambda a=a: self.button_pressed(a)

```

The important thing is to use _named parameters_. Putting this into a loop, it would look like this:
python ```
for a in range(10):
  button = QPushButton(str(a))
  button.pressed.connect(
    lambda val=a: self.button_pressed(val)
  )

```

Running this now, you will see the expected behavior -- with the label updating to a number matching the button which is pressed.
The working code is as follows:
python ```
from PyQt5.QtWidgets import (
  QApplication, QMainWindow, QAction, QPushButton,
  QWidget, QLabel, QVBoxLayout, QHBoxLayout
)
import sys

class Window(QWidget):
  def __init__(self):
    super().__init__()
    v = QVBoxLayout()
    h = QHBoxLayout()
    for a in range(10):
      button = QPushButton(str(a))
      button.pressed.connect(
        lambda val=a: self.button_pressed(val)
      )
      h.addWidget(button)
    v.addLayout(h)
    self.label = QLabel("")
    v.addWidget(self.label)
    self.setLayout(v)
  def button_pressed(self, n):
    self.label.setText(str(n))

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec_()

```

[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
Mark As Complete 
Continue with [ PyQt5 Tutorial ](https://www.pythonguis.com/tutorials/system-tray-mac-menu-bar-applications-pyqt/ "Continue to next part")
Return to [Create Desktop GUI Applications with PyQt5 ](https://www.pythonguis.com/pyqt5-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Transmitting Extra Data With Qt Signals in PyQt5** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/transmitting-extra-data-qt-signals/Python books) on the subject. 
**Transmitting Extra Data With Qt Signals in PyQt5** was published in [tutorials](https://www.pythonguis.com/tutorials/) on May 22, 2020 (updated March 15, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qt](https://www.pythonguis.com/topics/qt/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [python](https://www.pythonguis.com/topics/python/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
