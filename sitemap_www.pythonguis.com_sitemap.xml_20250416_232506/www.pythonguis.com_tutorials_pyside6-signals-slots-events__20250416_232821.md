# Content from: https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/

[](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PySide6 ](https://www.pythonguis.com/pyside6/)
  * [PySide6 Tutorial ](https://www.pythonguis.com/pyside6-tutorial/)
  * Basics
  * [Create a PySide6 app](https://www.pythonguis.com/tutorials/pyside6-creating-your-first-window/)
  * [PySide6 Signals](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/)
  * [PySide6 Widgets](https://www.pythonguis.com/tutorials/pyside6-widgets/)
  * [PySide6 Layouts](https://www.pythonguis.com/tutorials/pyside6-layouts/)
  * [PySide6 Menus](https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/)
  * [PySide6 Dialogs](https://www.pythonguis.com/tutorials/pyside6-dialogs/)
  * [Multi-window PySide6](https://www.pythonguis.com/tutorials/pyside6-creating-multiple-windows/)
  * Qt Designer
  * [First Qt Designer app](https://www.pythonguis.com/tutorials/pyside6-first-steps-qt-designer/)
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/pyside6-qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/pyside6-creating-dialogs-qt-designer/)
  * [The QResource System in PySide6](https://www.pythonguis.com/tutorials/pyside6-qresource-system/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/pyside6-qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/pyside6-modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/pyside6-qtableview-modelviews-numpy-pandas/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/pyside6-bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/pyside6-creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/pyside6-animated-widgets/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/pyside6-embed-pyqtgraph-custom-widgets/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/pyside6-transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/pyside6-system-tray-mac-menu-bar-applications/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyside6-applications-windows-pyinstaller-installforge/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyside6-applications-pyinstaller-macos-dmg/)
  * [Packaging QResources](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/)
  * Resources
  * [Books](https://www.pythonguis.com/books/)
  * Services
  * [Consulting](https://www.pythonguis.com/hire/)
  * [1:1 Coaching](https://www.pythonguis.com/live/)
  * [Contact](https://www.pythonguis.com/contact/)
  * [About](https://www.pythonguis.com/about/)
  * Libraries
  * [PyQt6](https://www.pythonguis.com/pyqt6/)
  * [PyQt5](https://www.pythonguis.com/pyqt5/)
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# PySide6 Signals, Slots & Events
Triggering actions in response to user behaviors and GUI events
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 14 This article has been updated for PySide6. PySide6 [ Getting started with PySide6 ](https://www.pythonguis.com/pyside6-tutorial/#pyside6-getting-started)
#### [ PySide6 Tutorial ](https://www.pythonguis.com/pyside6-tutorial/) — [Getting started with PySide6](https://www.pythonguis.com/pyside6-tutorial/#pyside6-getting-started)
  * [Creating your first app with PySide6](https://www.pythonguis.com/tutorials/pyside6-creating-your-first-window/)
  * [PySide6 Signals, Slots & Events](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/)
  * [PySide6 Widgets](https://www.pythonguis.com/tutorials/pyside6-widgets/)
  * [PySide6 Layouts](https://www.pythonguis.com/tutorials/pyside6-layouts/)
  * [PySide6 Toolbars & Menus — QAction](https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/)
  * [PySide6 Dialogs and Alerts](https://www.pythonguis.com/tutorials/pyside6-dialogs/)
  * [Creating Additional Windows in PySide6](https://www.pythonguis.com/tutorials/pyside6-creating-multiple-windows/)


This tutorial is also available for [PyQt6](https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/) , [PySide2](https://www.pythonguis.com/tutorials/pyside-signals-slots-events/) and [PyQt5](https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/)
So far, we've created a window and added a simple _push button_ widget to it, but the button doesn't do anything. That's not very useful at all -- when you create GUI applications, you typically want them to do something! What we need is a way to connect the action of _pressing the button_ to make something happen. In Qt, this is provided by _signals_ and _slots_ or _events_.
Table of Contents
  * [Signals & Slots](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/#signals-slots)
    * [QPushButton Signals](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/#qpushbutton-signals)
    * [Receiving data](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/#receiving-data)
    * [Storing data](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/#storing-data)
    * [Changing the interface](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/#changing-the-interface)
    * [Connecting widgets together directly](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/#connecting-widgets-together-directly)
  * [Events](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/#events)
    * [Mouse events](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/#mouse-events)
    * [Context menus](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/#context-menus)
    * [Event hierarchy](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/#event-hierarchy)


## Signals & Slots
_Signals_ are notifications emitted by widgets when _something_ happens. That something can be any number of things, from pressing a button, to the text of an input box changing, to the text of the window changing. Many signals are initiated by user action, but this is not a rule.
In addition to notifying about something happening, signals can also send data to provide additional context about what happened.
You can also create your own custom signals, which we'll explore later.
_Slots_ is the name Qt uses for the receivers of signals. In Python, any function (or method) in your application can be used as a slot -- simply by connecting the signal to it. If the signal sends data, then the receiving function will receive that data too. Many Qt widgets also have their own built-in slots, meaning you can hook Qt widgets together directly.
Let's take a look at the basics of Qt signals and how you can use them to hook widgets up to make things happen in your apps.
Save the following app outline to a file named `app.py`: 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
python ```
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

### `QPushButton` Signals
Our simple application currently has a `QMainWindow` with a `QPushButton` set as the central widget. Let's start by hooking up this button to a custom Python method. Here we create a simple custom slot named `the_button_was_clicked()` which accepts the `clicked` signal from the `QPushButton` object:
python ```
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    button = QPushButton("Press Me!")
    button.setCheckable(True)
    button.clicked.connect(self.the_button_was_clicked)
    # Set the central widget of the Window.
    self.setCentralWidget(button)
  def the_button_was_clicked(self):
    print("Clicked!")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

_Run it!_ If you click the button, you'll see the text "Clicked!" on the console:
python ```
Clicked!
Clicked!
Clicked!
Clicked!

```

### Receiving data
That's a good start! We've heard already that signals can also send _data_ to provide more information about what has just happened. The `clicked` signal is no exception, also providing a _checked_ (or toggled) state for the button. For normal buttons, this is always `False`, so our first slot ignored this data. However, we can make our button _checkable_ and see the effect.
In the following example, we add a second slot that outputs the _checkstate_ :
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    button = QPushButton("Press Me!")
    button.setCheckable(True)
    button.clicked.connect(self.the_button_was_clicked)
    button.clicked.connect(self.the_button_was_toggled)
    self.setCentralWidget(button)
  def the_button_was_clicked(self):
    print("Clicked!")
  def the_button_was_toggled(self, checked):
    print("Checked?", checked)

```

_Run it!_ If you press the button, you'll see it highlighted as _checked_. Press it again to release it. Look for the _check state_ in the console:
python ```
Clicked!
Checked? True
Clicked!
Checked? False
Clicked!
Checked? True
Clicked!
Checked? False
Clicked!
Checked? True

```

You can connect as many slots to a signal as you like and can respond to different versions of signals at the same time on your slots.
### Storing data
Often it is useful to store the current _state_ of a widget in a Python variable. This allows you to work with the values like any other Python variable without accessing the original widget. You can either store these values as individual variables or use a dictionary if you prefer. In the next example, we store the _checked_ value of our button in a variable called `button_is_checked` on `self`:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.button_is_checked = True
    self.setWindowTitle("My App")
    button = QPushButton("Press Me!")
    button.setCheckable(True)
    button.clicked.connect(self.the_button_was_toggled)
    button.setChecked(self.button_is_checked)
    self.setCentralWidget(button)
  def the_button_was_toggled(self, checked):
    self.button_is_checked = checked
    print(self.button_is_checked)

```

First, we set the default value for our variable (to `True`), then use the default value to set the initial state of the widget. When the widget state changes, we receive the signal and update the variable to match.
You can use this same pattern with any PySide widgets. If a widget does not provide a signal that sends the current state, you will need to retrieve the value from the widget directly in your handler. For example, here we're checking the checked state in a _pressed_ handler:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.button_is_checked = True
    self.setWindowTitle("My App")
    self.button = QPushButton("Press Me!")
    self.button.setCheckable(True)
    self.button.released.connect(self.the_button_was_released)
    self.button.setChecked(self.button_is_checked)
    self.setCentralWidget(self.button)
  def the_button_was_released(self):
    self.button_is_checked = self.button.isChecked()
    print(self.button_is_checked)

```

We need to keep a reference to the button on `self` so we can access it in our slot.
The _released_ signal fires when the button is released but does not send the check state, so instead, we use `isChecked()` to get the check state from the button in our handler.
### Changing the interface
So far, we've seen how to accept signals and print output to the console. But how about making something happen in the interface when we click the button? Let's update our slot method to modify the button, changing the text and disabling the button so it is no longer clickable. We'll also turn off the _checkable_ state for now:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    self.button = QPushButton("Press Me!")
    self.button.clicked.connect(self.the_button_was_clicked)
    self.setCentralWidget(self.button)
  def the_button_was_clicked(self):
    self.button.setText("You already clicked me.")
    self.button.setEnabled(False)
    # Also change the window title.
    self.setWindowTitle("My Oneshot App")

```

Again, because we need to be able to access the `button` in our `the_button_was_clicked` method, we keep a reference to it on `self`. The text of the button is changed by passing a string to `setText()`. To disable a button, call `setEnabled()` with `False`.
_Run it!_ If you click the button, the text will change, and the button will become unclickable.
You're not restricted to changing the button that triggers the signal, you can do _anything you want_ in your slot methods. For example, try adding the following line to `the_button_was_clicked()` method to also change the window title:
python ```
self.setWindowTitle("A new window title")

```

Most widgets have their own signals -- and the `QMainWindow` we're using for our window is no exception. In the following more complex example, we connect the `windowTitleChanged` signal on the `QMainWindow` to a custom slot method.
In the following example, we connect the `windowTitleChanged` signal on the `QMainWindow` to a method slot, `the_window_title_changed()`. This slot also receives the new window title:
python ```
import sys
from random import choice
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
window_titles = [
  "My App",
  "My App",
  "Still My App",
  "Still My App",
  "What on earth",
  "What on earth",
  "This is surprising",
  "This is surprising",
  "Something went wrong",
]
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.n_times_clicked = 0
    self.setWindowTitle("My App")
    self.button = QPushButton("Press Me!")
    self.button.clicked.connect(self.the_button_was_clicked)
    self.windowTitleChanged.connect(self.the_window_title_changed)
    self.setCentralWidget(self.button)
  def the_button_was_clicked(self):
    print("Clicked.")
    new_window_title = choice(window_titles)
    print("Setting title: %s" % new_window_title)
    self.setWindowTitle(new_window_title)
  def the_window_title_changed(self, window_title):
    print("Window title changed: %s" % window_title)
    if window_title == "Something went wrong":
      self.button.setDisabled(True)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

First, we set up a list of window titles -- we'll select one at random from this list using Python's built-in `random.choice()`. We hook our custom slot method, `the_window_title_changed()`, to the window's `windowTitleChanged` signal.
When we click the button, the window title will change at random. If the new window title equals "Something went wrong" the button will be disabled.
_Run it!_ Click the button repeatedly until the title changes to "Something went wrong", and the button will become disabled.
There are a few things to notice in this example.
Firstly, the `windowTitleChanged` signal is not _always_ emitted when setting the window title. The signal only fires if the new title is _changed_ from the previous one. If you set the same title multiple times, the signal will only be fired the first time. It is important to double-check the conditions under which signals fire, to avoid being surprised when using them in your app.
Secondly, notice how we are able to _chain_ things together using signals. One thing happening -- a button press -- can trigger multiple other things to happen in turn. These subsequent effects do not need to know _what_ caused them, but simply follow as a consequence of simple rules. This _decoupling_ of effects from their triggers is one of the key concepts to understand when building GUI applications.
In this section, we've covered signals and slots. We've demonstrated some simple signals and how to use them to pass data and state around your application. Next, we'll look at the widgets which Qt provides for use in your applications -- together with the signals they provide.
### Connecting widgets together directly
So far, we've seen examples of connecting widget signals to Python methods. When a signal is fired from the widget, our Python method is called and receives the data from the signal. But you don't _always_ need to use a Python function to handle signals -- you can also connect Qt widgets directly to one another.
In the following example, we add a `QLineEdit` widget and a `QLabel` to the window. In the `__init__()` for the window, we connect our line edit `textChanged` signal to the `setText()` method on the `QLabel`. Now any time the text changes in the `QLineEdit` the `QLabel` will receive that text to its `setText()` method:
python ```
import sys
from PySide6.QtWidgets import (
  QApplication,
  QLabel,
  QLineEdit,
  QMainWindow,
  QVBoxLayout,
  QWidget,
)
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    self.label = QLabel()
    self.input = QLineEdit()
    self.input.textChanged.connect(self.label.setText)
    layout = QVBoxLayout()
    layout.addWidget(self.input)
    layout.addWidget(self.label)
    container = QWidget()
    container.setLayout(layout)
    self.setCentralWidget(container)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

Notice that in order to connect the input to the label, the input and label must both be defined. This code adds the two widgets to a layout and sets that on the window. We'll cover layouts in detail later, you can ignore it for now.
_Run it!_ Type some text in the upper box, and you'll see it appear immediately on the label.
![Any text typed in the input immediately appears on the label](https://www.pythonguis.com/static/tutorials/qt/signals-slots-events/signals-direct.png) _Any text typed in the input immediately appears on the label._
Most Qt widgets have _slots_ available, to which you can connect any signal that emits the same _type_ that it accepts. The widget documentation has the slots for each widget listed under "Public Slots". For example, see the [`QLabel`](https://doc.qt.io/qt-5/qlabel.html#public-slots) documentation.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
## Events
Every interaction the user has with a Qt application is an _event_. There are many types of events, each representing a different type of interaction. Qt represents these events using _event objects_ which package up information about what happened. These events are passed to specific _event handlers_ on the widget where the interaction occurred.
By defining custom, or extended _event handlers_ , you can alter the way your widgets respond to these events. Event handlers are defined just like any other method, but the name is specific for the type of event they handle.
One of the main events which widgets receive is the `QMouseEvent`. QMouseEvent events are created for each and every mouse movement and button click on a widget. The following event handlers are available for handling mouse events:
Event handler | Event type moved  
---|---  
`mouseMoveEvent()` | Mouse moved  
`mousePressEvent()` | Mouse button pressed  
`mouseReleaseEvent()` | Mouse button released  
`mouseDoubleClickEvent()` | Double click detected  
For example, clicking on a widget will cause a `QMouseEvent` to be sent to the `mousePressEvent()` event handler on that widget. This handler can use the event object to find out information about what happened, such as what triggered the event and where specifically it occurred.
You can intercept events by sub-classing and overriding the handler method on the class. You can choose to filter, modify, or ignore events, passing them up to the normal handler for the event by calling the parent class function with `super()`. These could be added to your main window class as follows. In each case, `e` will receive the incoming event:
python ```
import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.label = QLabel("Click in this window")
    self.setCentralWidget(self.label)
  def mouseMoveEvent(self, e):
    self.label.setText("mouseMoveEvent")
  def mousePressEvent(self, e):
    self.label.setText("mousePressEvent")
  def mouseReleaseEvent(self, e):
    self.label.setText("mouseReleaseEvent")
  def mouseDoubleClickEvent(self, e):
    self.label.setText("mouseDoubleClickEvent")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

_Run it!_ Try moving and clicking (and double-clicking) in the window and watch the events appear.
You'll notice that mouse move events are only registered when you have the button pressed down. You can change this by calling `self.setMouseTracking(True)` on the window. You may also notice that the press (click) and double-click events both fire when the button is pressed down. Only the release event fires when the button is released. Typically, to register a click from a user, you should watch for both the mouse down _and_ the release.
Inside the event handlers, you have access to an event object. This object contains information about the event and can be used to respond differently depending on what exactly has occurred. We'll look at the mouse event objects next.
### Mouse events
All mouse events in Qt are tracked with the `QMouseEvent` object, with information about the event being readable from the following event methods:
Method | Returns  
---|---  
`.button()` | Specific button that triggered this event  
`.buttons()` | State of all mouse buttons (OR'ed flags)  
`.globalPos()` | Application-global position as a `QPoint`  
`.globalX()` | Application-global _horizontal_ X position  
`.globalY()` | Application-global _vertical_ Y position  
`.pos()` | Widget-relative position as a `QPoint` _integer_  
`.posF()` | Widget-relative position as a `QPointF` _float_  
You can use these methods within an event handler to respond to different events differently or ignore them completely. The positional methods provide both _global_ and _local_ (widget-relative) position information as `QPoint` objects, while buttons are reported using the mouse button types from the `Qt.MouseButton` namespace.
For example, the following allows us to respond differently to a left, right or middle click on the window:
python ```
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.label = QLabel("Click in this window")
    self.setCentralWidget(self.label)
  def mousePressEvent(self, e):
    if e.button() == Qt.MouseButton.LeftButton:
      # handle the left-button press in here
      self.label.setText("mousePressEvent LEFT")
    elif e.button() == Qt.MouseButton.MiddleButton:
      # handle the middle-button press in here.
      self.label.setText("mousePressEvent MIDDLE")
    elif e.button() == Qt.MouseButton.RightButton:
      # handle the right-button press in here.
      self.label.setText("mousePressEvent RIGHT")
  def mouseReleaseEvent(self, e):
    if e.button() == Qt.MouseButton.LeftButton:
      self.label.setText("mouseReleaseEvent LEFT")
    elif e.button() == Qt.MouseButton.MiddleButton:
      self.label.setText("mouseReleaseEvent MIDDLE")
    elif e.button() == Qt.MouseButton.RightButton:
      self.label.setText("mouseReleaseEvent RIGHT")
  def mouseDoubleClickEvent(self, e):
    if e.button() == Qt.MouseButton.LeftButton:
      self.label.setText("mouseDoubleClickEvent LEFT")
    elif e.button() == Qt.MouseButton.MiddleButton:
      self.label.setText("mouseDoubleClickEvent MIDDLE")
    elif e.button() == Qt.MouseButton.RightButton:
      self.label.setText("mouseDoubleClickEvent RIGHT")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

The button identifiers are defined in the `Qt.MouseButton` namespace, as follows:
Identifier | Value (binary) | Represents  
---|---|---  
`Qt.MouseButton.NoButton` | 0 (`000`) | No button pressed, or the event is not related to a button press.  
`Qt.MouseButton.LeftButton` | 1 (`001`) | The left button is pressed  
`Qt.MouseButton.RightButton` | 2 (`010`) | The right button is pressed.  
`Qt.MouseButton.MiddleButton` | 4 (`100`) | The middle button is pressed.  
On left-handed mice, the left and right button positions are reversed, i.e. pressing the right-most button will return `Qt.MouseButton.LeftButton`. This means you don't need to account for the mouse orientation in your code.
### Context menus
Context menus are small context-sensitive menus that typically appear when right-clicking on a window. Qt has support for generating these menus, and widgets have a specific event used to trigger them. In the following example, we're going to intercept the `contextMenuEvent()` in a `QMainWindow`. This event is fired whenever a context menu is _about to be_ shown and is passed a single value `event` of type `QContextMenuEvent`.
To intercept the event, we simply override the object method with our new method of the same name. So, in this case, we can create a method on our `MainWindow` subclass with the name `contextMenuEvent()`, and it will receive all events of this type:
python ```
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
  def contextMenuEvent(self, e):
    context = QMenu(self)
    context.addAction(QAction("test 1", self))
    context.addAction(QAction("test 2", self))
    context.addAction(QAction("test 3", self))
    context.exec(e.globalPos())
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

If you run the above code and right-click within the window, you'll see a context menu appear. You can set up `triggered` slots on your menu actions as normal (and re-use actions defined for menus and toolbars).
When passing the initial position to the `exec()` method, this must be relative to the parent passed in while defining. In this case, we pass `self` as the parent, so we can use the global position.
Just for completeness, there is actually a signal-based approach to creating context menus:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.show()
    self.setContextMenuPolicy(Qt.CustomContextMenu)
    self.customContextMenuRequested.connect(self.on_context_menu)
  def on_context_menu(self, pos):
    context = QMenu(self)
    context.addAction(QAction("test 1", self))
    context.addAction(QAction("test 2", self))
    context.addAction(QAction("test 3", self))
    context.exec(self.mapToGlobal(pos))

```

It's entirely up to you which you choose.
### Event hierarchy
In PySide6, every widget is part of two distinct hierarchies: the Python object hierarchy and the Qt layout hierarchy. How you respond or ignore events can affect how your UI behaves.
#### Python inheritance forwarding
Often you may want to intercept an event and do something with it, yet still trigger the default event-handling behavior. If your object is inherited from a standard widget, it will likely have sensible behavior implemented by default. You can trigger this by calling up the parent's implementation using `super()`.
This is the Python parent class, not the PySide `parent()` class:
python ```
def mousePressEvent(self, event):
  print("Mouse pressed!")
  super().mousePressEvent(event)

```

The event will continue to behave as normal, yet you've added some non-interfering behavior.
#### Layout forwarding
When you add a widget to your application, it also gets another _parent_ from the layout. The parent of a widget can be found by calling `.parent()`. Sometimes you specify these parents manually, such as for `QMenu` or `QDialog`, often it is automatic. When you add a widget to your main window, for example, the main window will become the widget's parent.
When events are created for user interaction with the UI, these events are passed to the _uppermost_ widget in the UI. So, if you have a button on a window and click the button, then the button will receive the event first.
If the first widget cannot handle the event or chooses not to, then the event will _bubble up_ to the parent widget, which will be given a turn. This _bubbling_ continues all the way up nested widgets until the event is handled or it reaches the main window.
In your own event handlers, you can choose to mark an event as _handled_ by calling the `accept()` method:
python ```
class CustomButton(QPushButton)
  def mousePressEvent(self, e):
    e.accept()

```

Alternatively, you can mark it as _unhandled_ by calling `ignore()` on the event object. In this case, the event will continue to bubble up the hierarchy:
python ```
class CustomButton(QPushButton)
  def event(self, e):
    e.ignore()

```

If you want your widget to appear transparent to events, you can safely ignore events that you've actually responded to in some way. Similarly, you can choose to accept events you are not responding to in order to silence them.
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
Continue with [ PySide6 Tutorial ](https://www.pythonguis.com/tutorials/pyside6-widgets/ "Continue to next part")
Return to [Create Desktop GUI Applications with PySide6 ](https://www.pythonguis.com/pyside6-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PySide6 Signals, Slots & Events** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/Python books) on the subject. 
**PySide6 Signals, Slots & Events** was published in [tutorials](https://www.pythonguis.com/tutorials/) on January 27, 2022 (updated April 14, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [ foundation](https://www.pythonguis.com/topics/foundation/) [ pyside6-foundation](https://www.pythonguis.com/topics/pyside6-foundation/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
