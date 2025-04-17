# Content from: https://www.pythonguis.com/tutorials/pyside6-widget-search-bar/

[](https://www.pythonguis.com/tutorials/pyside6-widget-search-bar/#menu)
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
# Creating Searchable Widget Dashboards in PySide6
Make dashboard UIs easier to use with widget search & text prediction
by [John Lim](https://www.pythonguis.com/authors/john-lim/) Last updated Mar 15 PySide6 [ Tutorials ](https://www.pythonguis.com/tutorials/)
This tutorial is also available for [PyQt6](https://www.pythonguis.com/tutorials/pyqt6-widget-search-bar/) , [PySide2](https://www.pythonguis.com/tutorials/pyside-widget-search-bar/) and [PyQt5](https://www.pythonguis.com/tutorials/widget-search-bar/)
Dashboard applications are a popular way to display live data and user controls, whether interacting with APIs or controlling locally attached devices. However, as more controls are added, dashboards can quickly get out of control, making it hard to find the controls you want when you want them. One common solution is to provide the user with a way to filter the displayed widgets, allowing them to zero-in on the information and tools that are important to them right now.
There are many ways to filter lists, including dropdowns and facets, but one of the most intuitive is a simple, live, search box. As long as elements are well named, or tagged with appropriate metadata, this can be both fast and easy to understand.
In this tutorial we'll build a simple search based widget filter, which can be used to filter a custom compound control widget. This could be an app to control the electrical sensors/gadgets around your home. The finished example is shown below —
The interface includes a search bar with autocomplete, a scrollable region list, and a series of independent custom widgets.
Table of Contents
  * [Basic application template](https://www.pythonguis.com/tutorials/pyside6-widget-search-bar/#basic-application-template)
  * [Building our custom compound widget](https://www.pythonguis.com/tutorials/pyside6-widget-search-bar/#building-our-custom-compound-widget)
  * [Building our main application layout](https://www.pythonguis.com/tutorials/pyside6-widget-search-bar/#building-our-main-application-layout)
  * [Adding search functionality](https://www.pythonguis.com/tutorials/pyside6-widget-search-bar/#adding-search-functionality)
  * [Adding text prediction](https://www.pythonguis.com/tutorials/pyside6-widget-search-bar/#adding-text-prediction)
  * [Conclusion](https://www.pythonguis.com/tutorials/pyside6-widget-search-bar/#conclusion)


### Basic application template
We start from our basic application template, shown below, which you can **save to file** as _app.py_ —
python ```
# app.py
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    container = QWidget()
    containerLayout = QVBoxLayout()
    container.setLayout(containerLayout)
    self.setCentralWidget(container)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())

```

If you run this, it will display a blank window. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
bash ```
python app.py

```

In this template we have created a `MainWindow` class subclassed from `QMainWindow`. In the `__init__` block we've added a container `QWidget` and applied a vertical layout with `QVBoxLayout`. This container widget is then set as the central widget of the window.
Any widgets we subsequently add to this layout will be laid out vertically in the window. Next we'll define our control widgets, which we can then add to the layout.
### Building our custom compound widget
For our control panel widgets we'll be creating a _compound widget_ , that is, a widget created by combining 2 or more standard widgets together. By adding our own logic to these widgets we can create our custom behaviours.
If you're interested in creating more complex custom widgets, take a look at our [custom widgets tutorials](https://www.pythonguis.com/courses/custom-widgets/).
**Create a new file** called `customwidgets.py` in the same folder as `app.py`. We will define our custom widget here, then import it into our main application code.
The custom widget is a simple On/Off toggle widget, so we've given it the slightly uninspired name `OnOffWidget`.
Start by adding the imports and creating a basic stub for the widget class. The widget accepts a single parameter `name` which we store in `self.name` to use for searching later. This is also be used to create a label for the widget later.
python ```
# customwidgets.py
from PySide6.QtWidgets import (QWidget, QLabel, QPushButton, QHBoxLayout)

class OnOffWidget(QWidget):
  def __init__(self, name):
    super().__init__()
    self.name = name # Name of widget used for searching.
    self.is_on = False # Current state (true=ON, false=OFF)

```

Note that we've also added an attribute `self.is_on` which holds the widget's current state, with `True` for ON and `False` for OFF. We'll add logic to update this later.
In _app.py_ we can import this custom widget as follows —
python ```
from customwidgets import OnOffWidget

```

For development purposes create a single instance of `OnOffWidget` and add it to the `containerLayout` in the parent app. This will allow you to see the effects of your changes to the widgets code by running _app.py_.
python ```
# app.py
import sys
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QMainWindow, QApplication)
from customwidgets import OnOffWidget
class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    container = QWidget()
    containerLayout = QVBoxLayout()
    container.setLayout(containerLayout)
    onoff = OnOffWidget('Testing')
    containerLayout.addWidget(onoff)
    self.setCentralWidget(container)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())

```

Running this will produce a window containing a single `OnOffWidget`. However, since the widget does not display anything itself, the window will appear empty. We'll fix that now by specifying the layout of our custom widget and adding some contents.
`OnOffWidget` is a custom widget containing a label and two On/Off toggle buttons, that could for example be used to control lights or gadgets in your home.
python ```
class OnOffWidget(QWidget):
  def __init__(self, name):
    super().__init__()
    self.name = name # Name of widget used for searching.
    self.is_on = False # Current state (true=ON, false=OFF)
    self.lbl = QLabel(self.name)  # The widget label
    self.btn_on = QPushButton("On")   # The ON button
    self.btn_off = QPushButton("Off")  # The OFF button
    self.hbox = QHBoxLayout()    # A horizontal layout to encapsulate the above
    self.hbox.addWidget(self.lbl)  # Add the label to the layout
    self.hbox.addWidget(self.btn_on)  # Add the ON button to the layout
    self.hbox.addWidget(self.btn_off)  # Add the OFF button to the layout
    self.setLayout(self.hbox)

```

The passed in name (already stored in `self.name`) is now used to create a `QLabel` to identify the widget. Next we create two buttons labelled On and Off respectively to act as toggles, and then add the label and the two buttons into a layout for display.
![OnOffWidget plain, without toggle styles](https://www.pythonguis.com/static/tutorials/qt/widget-search-bar/OnOffWidget.png) _OnOffWidget plain, without toggle styles_
As it currently stands, the widget can be created and the buttons clicked, however they don't do anything. Next we'll hook up the button signals and use them to toggle the state of the widget from ON to OFF.
#### Updating widget state
The current state of the widget will be displayed by changing the colour of the two buttons. When in the ON state the _On_ button will be highlighted green, when OFF the _Off_ button will be highlighted in red.
We do this by defining two methods `.on` and `.off` which are called to turn the widget to ON and OFF state respectively. We also add a `update_button_state` method which updates the appearance of the buttons to indicate the current state.
python ```
class OnOffWidget(QWidget):
  def __init__(self, name):
    super().__init__()
    # ... rest of __init__ hidden for clarity.
    self.btn_on.clicked.connect(self.on)
    self.btn_off.clicked.connect(self.off)
    self.update_button_state()
  def off(self):
    self.is_on = False
    self.update_button_state()
  def on(self):
    self.is_on = True
    self.update_button_state()
  def update_button_state(self):
    """
    Update the appearance of the control buttons (On/Off)
    depending on the current state.
    """
    if self.is_on == True:
      self.btn_on.setStyleSheet("background-color: #4CAF50; color: #fff;")
      self.btn_off.setStyleSheet("background-color: none; color: none;")
    else:
      self.btn_on.setStyleSheet("background-color: none; color: none;")
      self.btn_off.setStyleSheet("background-color: #D32F2F; color: #fff;")

```

Notice that we call `update_button_state` at the end of the `__init__` block to set the initial state of the buttons, and the `.on` and .`off` methods both call `update_button_state` after changing `.is_on`.
In this simple example you could combine the `update_button_state` code into the `.on` and `.off` methods, but as you build more complex controls it is a good idea to keep a central _update display state_ method to ensure consistency.
The `.on` and `.off` methods are connected to the button `.clicked` signals as follows —
python ```
self.btn_on.clicked.connect(self.on)

```

For a refresher on using Qt signals and slots, head over to the [Signals & Slots tutorial](https://www.pythonguis.com/tutorials/pyside-signals-slots-events/).
With these signals connected up, clicking the buttons will now toggle the widget `is_on` state and update the buttons' appearance.
### Building our main application layout
Now we have completed our custom control widget, we can finish the layout of the main application. The full code is shown at first, and then explained in steps below.
python ```
# app.py
import sys
from PySide6.QtWidgets import (
  QWidget, QLineEdit, QScrollArea, QMainWindow,
  QApplication, QVBoxLayout, QSpacerItem, QSizePolicy
  )
from PySide6.QtCore import Qt

from customwidgets import OnOffWidget

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__()
    self.controls = QWidget() # Controls container widget.
    self.controlsLayout = QVBoxLayout()  # Controls container layout.
    # List of names, widgets are stored in a dictionary by these keys.
    widget_names = [
      "Heater", "Stove", "Living Room Light", "Balcony Light",
      "Fan", "Room Light", "Oven", "Desk Light",
      "Bedroom Heater", "Wall Switch"
    ]
    self.widgets = []
    # Iterate the names, creating a new OnOffWidget for
    # each one, adding it to the layout and
    # and storing a reference in the self.widgets list
    for name in widget_names:
      item = OnOffWidget(name)
      self.controlsLayout.addWidget(item)
      self.widgets.append(item)
    spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
    self.controlsLayout.addItem(spacer)
    self.controls.setLayout(self.controlsLayout)
    # Scroll Area Properties.
    self.scroll = QScrollArea()
    self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.scroll.setWidgetResizable(True)
    self.scroll.setWidget(self.controls)
    # Search bar.
    self.searchbar = QLineEdit()
    # Add the items to VBoxLayout (applied to container widget)
    # which encompasses the whole window.
    container = QWidget()
    containerLayout = QVBoxLayout()
    containerLayout.addWidget(self.searchbar)
    containerLayout.addWidget(self.scroll)
    container.setLayout(containerLayout)
    self.setCentralWidget(container)
    self.setGeometry(600, 100, 800, 600)
    self.setWindowTitle('Control Panel')

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())

```

We'll now step through the sections of the above code, explaining how each of the key parts works in turn.
We start first by creating our `OnOffWidget` widget instances. The list of widgets to generate is coded as a `list` of names, each as a `str`. To generate the widgets we iterate this list, passing the names into to the `OnOffWidget` constructor. This creates a new `OnOffWidget` with the name as a `QLabel` (see the widget definition above). This same name will be used for searching later.
python ```
# List of names, widgets are stored in a dictionary by these keys.
widget_names = [
  "Heater", "Stove", "Living Room Light", "Balcony Light",
  "Fan", "Room Light", "Oven", "Desk Light",
  "Bedroom Heater", "Wall Switch"
]
self.widgets = []
# Iterate the names, creating a new OnOffWidget for
# each one, adding it to the layout and
# and storing a reference in the self.widgets list
for name in widget_names:
  item = OnOffWidget(name)
  self.controlsLayout.addWidget(item)
  self.widgets.append(item)

```

Once the widget is created it is added to our layout and also appended to our widget list in `self.widgets`. We can iterate this list later to perform our search.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
In addition to the `OnOffWidgets` that we've added to our `controlsLayout` we also need to add a spacer. Without a spacer the widgets in the window will spread out to take up all the available space, rather than remaining compact and consistently sized.
The following spacer is set to a 1x1 default dimension, with the y-dimension set as _expanding_ so it will expand vertically to fill all available space.
python ```
spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
self.controlsLayout.addItem(spacer)
self.controls.setLayout(self.controlsLayout)

```

As we're adding this to a `QVBoxLayout` the x dimension of the spacer is irrelevant.
Next we setup a scrolling area, adding the `self.controls` widget to it, and setting the vertical scrollbar to always on, and the horizontal to always off.
python ```
# Scroll Area Properties.
self.scroll = QScrollArea()
self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
self.scroll.setWidgetResizable(True)
self.scroll.setWidget(self.controls)

```

If you're unfamiliar with adding scrolling regions to your applications you can take a look at our earlier [QScrollArea tutorial](https://www.pythonguis.com/tutorials/pyside-qscrollarea/).
Finally, we assemble our widgets for the view. The `container` widget holds our entire layout (and will be set using `.setCentralWidget` on the window). To this we first add our `QLineEdit` search bar, and the scroll widget.
python ```
# Search bar.
self.searchbar = QLineEdit()
# Add the items to VBoxLayout (applied to container widget)
# which encompasses the whole window.
container = QWidget()
containerLayout = QVBoxLayout()
containerLayout.addWidget(self.searchbar)
containerLayout.addWidget(self.scroll)

```

Running the code you'll see the following window, with a search bar on top and a list of our custom `OnOffWidget` widgets below.
![Search Bar and Widget list](https://www.pythonguis.com/static/tutorials/qt/widget-search-bar/SearchBar1.png) _Search Bar and Widget list_
However, if you try typing in the box you'll notice that the search is not working and none of the widgets are filtered. In the next part we'll step through the process of adding search functionality, along with autocomplete hints, to the app.
### Adding search functionality
Finally, we get to the main objective of this article — adding the search functionality! This can be accomplished with a single method, along with some small tweaks to our `OnOffWidget` class. Make the following additions to the `MainWindow` class —
python ```
class MainWindow(QWidget):
  def __init__(self, *args, **kwargs):
    super().__init__()
    # ... rest of __init__ ommitted for clarity.
    # Search bar.
    self.searchbar = QLineEdit()
    self.searchbar.textChanged.connect(self.update_display)
    # ... rest of __init__ omitted for clarity.

  # ... other MainWindow methods ommitted for clarity.
  def update_display(self, text):
    for widget in self.widgets:
      if text.lower() in widget.name.lower():
        widget.show()
      else:
        widget.hide()

```

As shown, the `searchbar.textChanged` signal can be attached in the `__init__` after the creation of the `searchbar`. This connects the `QLineEdit.textChanged` signal to our custom `update_display` method. The `textChanged` signal fires every time the text in the box changes, and sends the current text to any connected slots.
We then create a method `update_display` which performs the following —
  1. Iterate through each `OnOffWidget` in `self.widgets`
  2. Determine whether the (lowercased) name of the widget `widget.name` contains the (lowercased) `text` entered by the user in the search bar.
  3. If there is a match (name contains the text), show the widget by calling `widget.show()`; if it doesn't match, hide the widget by calling `widget.hide()`


By lowercasing both the widget name and the the search string we do a case-insensitive search, making it easier to find our widgets.
If you think back to the `OnOffWidget` definition you'll remember that we assigned the name passed when creating the widget to `self.name`, it is this value we're checking now on each of our widgets as `widget.name`.
Now, as you type text in the box, the current text is sent to `update_widgets`, the widgets are then iterated, matched and shown or hidden as appropriate. Or, at least they would be, if those methods were defined…. we'll do that next.
#### Toggling widget visibility
Open _customwidgets.py_ add the following two methods to the `OnOffWidget` class.
python ```
  def show(self):
    """
    Show this widget, and all child widgets.
    """
    for w in [self, self.lbl, self.btn_on, self.btn_off]:
      w.setVisible(True)
  def hide(self):
    """
    Hide this widget, and all child widgets.
    """
    for w in [self, self.lbl, self.btn_on, self.btn_off]:
      w.setVisible(False)

```

Each Qt widget has a `.setVisible` method which can be used to toggle that widget's visibility. However, compound or nested widgets can only become invisible when _all their child widgets_ are also invisible.
In our case, that means even if we call `.setVisible(False)` on our `OnOffWidget` the widget will not become invisible, _until_ the nested `.lbl`, `.btn_on` and `.btn_off` are also `.setVisible(False)`. These custom `.show` and `.hide` methods handle this for us, by setting `self` (the current widget) and all child widgets to visible, or invisible, respectively.
With these methods in place, if you now run the complete application you should see the text search and filtering working as expected.
### Adding text prediction
Being able to search to find widgets is a handy shortcut, but we can make things even more convenient for the user by adding text completion to speed up the search. This is particularly handy when you have a number of widgets with similar names. With prediction it is possible to jump to the correct widgets by typing only a few letters and then selecting one of the suggested options with the keyboard.
Qt has support for text completion built in, through the `QCompleter` class. Add the code below to the `__init__` block of the `MainWindow` after the search bar is created as `self.searchbar`. The basic completer requires only 2 lines of code, one to create the completer, and a second to attach it to the `QLineEdit`. Here we've also set the search case sensitivity mode to _case insensitive_ to match the search.
python ```
    # Adding Completer.
    self.completer = QCompleter(widget_names)
    self.completer.setCaseSensitivity(Qt.CaseInsensitive)
    self.searchbar.setCompleter(self.completer)

```

The complete `app.py` and `customwidgets.py` code is shown below.
python ```
# app.py
import sys
from PySide6.QtWidgets import (
  QWidget, QLineEdit, QScrollArea, QMainWindow,
  QApplication, QVBoxLayout, QSpacerItem, QSizePolicy, QCompleter
)
from PySide6.QtCore import Qt
from customwidgets import OnOffWidget

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__()
    self.controls = QWidget() # Controls container widget.
    self.controlsLayout = QVBoxLayout()  # Controls container layout.
    # List of names, widgets are stored in a dictionary by these keys.
    widget_names = [
      "Heater", "Stove", "Living Room Light", "Balcony Light",
      "Fan", "Room Light", "Oven", "Desk Light",
      "Bedroom Heater", "Wall Switch"
    ]
    self.widgets = []
    # Iterate the names, creating a new OnOffWidget for
    # each one, adding it to the layout and
    # and storing a reference in the self.widgets dict
    for name in widget_names:
      item = OnOffWidget(name)
      self.controlsLayout.addWidget(item)
      self.widgets.append(item)
    spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
    self.controlsLayout.addItem(spacer)
    self.controls.setLayout(self.controlsLayout)
    # Scroll Area Properties.
    self.scroll = QScrollArea()
    self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.scroll.setWidgetResizable(True)
    self.scroll.setWidget(self.controls)
    # Search bar.
    self.searchbar = QLineEdit()
    self.searchbar.textChanged.connect(self.update_display)
    # Adding Completer.
    self.completer = QCompleter(widget_names)
    self.completer.setCaseSensitivity(Qt.CaseInsensitive)
    self.searchbar.setCompleter(self.completer)
    # Add the items to VBoxLayout (applied to container widget)
    # which encompasses the whole window.
    container = QWidget()
    containerLayout = QVBoxLayout()
    containerLayout.addWidget(self.searchbar)
    containerLayout.addWidget(self.scroll)
    container.setLayout(containerLayout)
    self.setCentralWidget(container)
    self.setGeometry(600, 100, 800, 600)
    self.setWindowTitle('Control Panel')
  def update_display(self, text):
    for widget in self.widgets:
      if text.lower() in widget.name.lower():
        widget.show()
      else:
        widget.hide()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())

```

And the `customwidgets.py` file below.
python ```
# customwidgets.py
from PySide6.QtWidgets import (QWidget, QLabel, QPushButton,
               QHBoxLayout)

class OnOffWidget(QWidget):
  def __init__(self, name):
    super().__init__()
    self.name = name
    self.is_on = False
    self.lbl = QLabel(self.name)
    self.btn_on = QPushButton("On")
    self.btn_off = QPushButton("Off")
    self.hbox = QHBoxLayout()
    self.hbox.addWidget(self.lbl)
    self.hbox.addWidget(self.btn_on)
    self.hbox.addWidget(self.btn_off)
    self.btn_on.clicked.connect(self.on)
    self.btn_off.clicked.connect(self.off)
    self.setLayout(self.hbox)
    self.update_button_state()
  def show(self):
    """
    Show this widget, and all child widgets.
    """
    for w in [self, self.lbl, self.btn_on, self.btn_off]:
      w.setVisible(True)
  def hide(self):
    """
    Hide this widget, and all child widgets.
    """
    for w in [self, self.lbl, self.btn_on, self.btn_off]:
      w.setVisible(False)
  def off(self):
    self.is_on = False
    self.update_button_state()
  def on(self):
    self.is_on = True
    self.update_button_state()
  def update_button_state(self):
    """
    Update the appearance of the control buttons (On/Off)
    depending on the current state.
    """
    if self.is_on == True:
      self.btn_on.setStyleSheet("background-color: #4CAF50; color: #fff;")
      self.btn_off.setStyleSheet("background-color: none; color: none;")
    else:
      self.btn_on.setStyleSheet("background-color: none; color: none;")
      self.btn_off.setStyleSheet("background-color: #D32F2F; color: #fff;")

```

## Conclusion
By adding a search bar we've made it easier for users to navigate and filter through lists of controls. This same approach could be used to filter through a list of status panels, or graphs, or any other Qt widgets. This allows you to build complex dashboards without the interface becoming overwhelming for the user.
As a next step you could experiment with adding "favorite" widgets, with the ability to mark particular widgets to appear at the top. You'll need to re-sort the widgets when the favorite state is updated, but otherwise things stay much the same. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![John Lim Ji Xiong](https://www.pythonguis.com/static/theme/images/authors/john-lim.jpg)](https://www.pythonguis.com/authors/john-lim/)
**Creating Searchable Widget Dashboards in PySide6** was written by [John Lim](https://www.pythonguis.com/authors/john-lim/) . 
John is a developer from Kuala Lumpur, Malaysia who works as a Senior R&D Engineer. 
**Creating Searchable Widget Dashboards in PySide6** was published in [tutorials](https://www.pythonguis.com/tutorials/) on August 06, 2021 (updated March 15, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[widget](https://www.pythonguis.com/topics/widget/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [filter](https://www.pythonguis.com/topics/filter/) [search](https://www.pythonguis.com/topics/search/) [qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
