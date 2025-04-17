# Content from: https://www.pythonguis.com/tutorials/pyqt6-layouts/

[](https://www.pythonguis.com/tutorials/pyqt6-layouts/#menu)
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
# PyQt6 Layouts
Use layouts to effortlessly position widgets within the window
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Mar 28 This article has been updated for PyQt6. PyQt6 [ Getting started with PyQt6 ](https://www.pythonguis.com/pyqt6-tutorial/#pyqt6-start)
#### [ PyQt6 Tutorial ](https://www.pythonguis.com/pyqt6-tutorial/) — [Getting started with PyQt6](https://www.pythonguis.com/pyqt6-tutorial/#pyqt6-start)
  * [Creating your first app with PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/)
  * [PyQt6 Signals, Slots & Events](https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/)
  * [PyQt6 Widgets](https://www.pythonguis.com/tutorials/pyqt6-widgets/)
  * [PyQt6 Layouts](https://www.pythonguis.com/tutorials/pyqt6-layouts/)
  * [PyQt6 Toolbars & Menus — QAction](https://www.pythonguis.com/tutorials/pyqt6-actions-toolbars-menus/)
  * [PyQt6 Dialogs and Alerts](https://www.pythonguis.com/tutorials/pyqt6-dialogs/)
  * [Creating Additional Windows in PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/)


This tutorial is also available for [PySide6](https://www.pythonguis.com/tutorials/pyside6-layouts/) , [PySide2](https://www.pythonguis.com/tutorials/pyside-layouts/) and [PyQt5](https://www.pythonguis.com/tutorials/pyqt-layouts/)
So far we've successfully created a window and added a widget to it. However, we normally want to add more than one widget to a window and have some control over where it ends up. To do this in Qt, we use _layouts_.
Table of Contents
  * [QVBoxLayout vertically arranged widgets](https://www.pythonguis.com/tutorials/pyqt6-layouts/#qvboxlayout-vertically-arranged-widgets)
  * [QHBoxLayout horizontally arranged widgets](https://www.pythonguis.com/tutorials/pyqt6-layouts/#qhboxlayout-horizontally-arranged-widgets)
  * [Nesting layouts](https://www.pythonguis.com/tutorials/pyqt6-layouts/#nesting-layouts)
  * [QGridLayout widgets arranged in a grid](https://www.pythonguis.com/tutorials/pyqt6-layouts/#qgridlayout-widgets-arranged-in-a-grid)
  * [QStackedLayout multiple widgets in the same space](https://www.pythonguis.com/tutorials/pyqt6-layouts/#qstackedlayout-multiple-widgets-in-the-same-space)


There are four basic layouts available in Qt, which are listed in the following table:
Layout | Behavior  
---|---  
`QHBoxLayout` | Linear horizontal layout  
`QVBoxLayout` | Linear vertical layout  
`QGridLayout` | In indexable grid XxY  
`QStackedLayout` | Stacked (z) in front of one another  
You can also design and [lay out your interface graphically using the Qt designer](https://www.pythonguis.com/tutorials/qt-designer-gui-layout/). Here, we're using code so you can understand the underlying system.
As you can see, there are three positional layouts available in Qt. The `QVBoxLayout`, `QHBoxLayout` and `QGridLayout`. In addition, there is also `QStackedLayout`, which allows you to place widgets one on top of the other within the same space, yet showing only one layout at a time.
Before we start we need a simple application outline. Save the following code in a file named `app.py` -- we'll modify this application to experiment with different layouts:
python ```
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

To make it easier to visualize the layouts, we'll first create a simple custom widget that displays a solid color of our choosing. This will help to distinguish widgets that we add to the layout. Create a new file called `layout_colorwidget.py` with the following code:
python ```
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QWidget

class Color(QWidget):
  def __init__(self, color):
    super().__init__()
    self.setAutoFillBackground(True)
    palette = self.palette()
    palette.setColor(QPalette.ColorRole.Window, QColor(color))
    self.setPalette(palette)

```

In this code we subclass `QWidget` to create our own custom widget `Color`. We accept a single parameter when creating the widget — `color` (a `str`). We first set `.setAutoFillBackground` to `True` to tell the widget to automatically fill its background with the window color.
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Next we get the current palette (which is the global desktop palette by default) and change the current `QPalette.Window` color to a new `QColor` described by the value `color` we passed in. Finally we apply this palette back to the widget. The end result is a widget that is filled with a solid color, that we specified when we created it.
If you find the above confusing, don't worry too much. We'll cover custom widgets in more detail later. For now, it's sufficient that you understand that calling you can create a solid-filled red widget by doing the following:
python ```
Color('red')

```

First let's test our new `Color` widget by using it to fill the entire window in a single color. Once it's complete, we can add it to the `QMainWindow` using `.setCentralWidget` and we get a solid red window:
python ```
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from layout_colorwidget import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    widget = Color("red")
    self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

**Run it!** A window will appear, filled completely with the color red. Notice how the widget expands to fill all the available space.
Next, we'll look at each of the available Qt layouts in turn. Note that to add our layouts to the window we will need a dummy `QWidget` to hold the layout.
### `QVBoxLayout` vertically arranged widgets
With `QVBoxLayout` you arrange widgets one above the other linearly. Adding a widget appends it to the bottom of the column.
![A QVBoxLayout, filled from top to bottom.](https://www.pythonguis.com/static/tutorials/qt/layouts/vboxlayout.png) _A QVBoxLayout, filled from top to bottom._
Let's add our widget to a layout. Note that in order to add a layout to the `QMainWindow` we need to apply it to a dummy `QWidget`. This allows us to then use `.setCentralWidget` to apply the widget (and the layout) to the window. Our colored widgets will arrange themselves in the layout, contained within the `QWidget` in the window.
First, we need to import `QVBoxLayout` from `PyQt6.QtWidgets` and then add the red widget as before:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    layout = QVBoxLayout()
    layout.addWidget(Color("red"))
    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)

```

**Run it!** Notice the border now visible around the red widget. This is the layout spacing — we'll see how to adjust that later.
If you add a few more colored widgets to the layout you'll notice that they line themselves up vertically in the order they are added:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    layout = QVBoxLayout()
    layout.addWidget(Color("red"))
    layout.addWidget(Color("green"))
    layout.addWidget(Color("orange"))
    layout.addWidget(Color("blue"))
    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)

```

### `QHBoxLayout` horizontally arranged widgets
`QHBoxLayout` works the same, except for the horizontally arranged widgets. Adding a widget appends it to the right-hand side.
![A QHBoxLayout, filled from left to right.](https://www.pythonguis.com/static/tutorials/qt/layouts/hboxlayout.png) _A QHBoxLayout, filled from left to right._
To use it we can simply change the `QVBoxLayout` to a `QHBoxLayout`. The boxes now flow left to right:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    layout = QHBoxLayout()
    layout.addWidget(Color("red"))
    layout.addWidget(Color("green"))
    layout.addWidget(Color("orange"))
    layout.addWidget(Color("blue"))
    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)

```

### Nesting layouts
For more complex layouts, you can nest layouts inside one another using `.addLayout` on a layout. Below we add a `QVBoxLayout` into the main `QHBoxLayout`. If we add some widgets to the `QVBoxLayout`, they’ll be arranged vertically in the first slot of the parent layout:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    layout1 = QHBoxLayout()
    layout2 = QVBoxLayout()
    layout3 = QVBoxLayout()
    layout2.addWidget(Color("red"))
    layout2.addWidget(Color("yellow"))
    layout2.addWidget(Color("purple"))
    layout1.addLayout(layout2)
    layout1.addWidget(Color("green"))
    layout3.addWidget(Color("red"))
    layout3.addWidget(Color("purple"))
    layout1.addLayout(layout3)
    widget = QWidget()
    widget.setLayout(layout1)
    self.setCentralWidget(widget)

```

**Run it!** The widgets should arrange themselves in three columns horizontally, with the first column also containing three widgets stacked vertically. Experiment!
You can set the spacing around the layout using `.setContentMargins` or set the spacing between elements using `.setSpacing`:
python ```
layout1.setContentsMargins(0,0,0,0)
layout1.setSpacing(20)

```

The following code shows the combination of nested widgets and layout margins and spacing. Experiment with the numbers til you get a feel for them: 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    layout1 = QHBoxLayout()
    layout2 = QVBoxLayout()
    layout3 = QVBoxLayout()
    layout2.addWidget(Color("red"))
    layout2.addWidget(Color("yellow"))
    layout2.addWidget(Color("purple"))
    layout1.setContentsMargins(0,0,0,0)
    layout1.setSpacing(20)
    layout1.addLayout(layout2)
    layout1.addWidget(Color("green"))
    layout3.addWidget(Color("red"))
    layout3.addWidget(Color("purple"))
    layout1.addLayout(layout3)
    widget = QWidget()
    widget.setLayout(layout1)
    self.setCentralWidget(widget)

```

### `QGridLayout` widgets arranged in a grid
As useful as they are, if you try and use `QVBoxLayout` and `QHBoxLayout` for laying out multiple elements, e.g. for a form, you’ll find it very difficult to ensure differently sized widgets line up. The solution to this is `QGridLayout`:
![A QGridLayout showing the grid positions for each location.](https://www.pythonguis.com/static/tutorials/qt/layouts/gridlayout1.png) _A QGridLayout showing the grid positions for each location._
`QGridLayout` allows you to position items specifically in a grid. You specify row and column positions for each widget. You can skip elements, and they will be left empty.
Usefully, for `QGridLayout` you don't need to fill all the positions in the grid:
![A QGridLayout with unfilled slots.](https://www.pythonguis.com/static/tutorials/qt/layouts/gridlayout2.png) _A QGridLayout with unfilled slots._
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    layout = QGridLayout()
    layout.addWidget(Color("red"), 0, 3)
    layout.addWidget(Color("green"), 1, 1)
    layout.addWidget(Color("orange"), 2, 2)
    layout.addWidget(Color("blue"), 3, 0)
    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)

```

### `QStackedLayout` multiple widgets in the same space
The final layout we'll cover is the `QStackedLayout`. As described, this layout allows you to position elements directly in front of one another. You can then select which widget you want to show. You could use this for drawing layers in a graphics application, or for imitating a tab-like interface. Note there is also `QStackedWidget` which is a container widget that works in exactly the same way. This is useful if you want to add a stack directly to a `QMainWindow` with `.setCentralWidget`.
![QStackedLayout — in use only the uppermost widget is visible, which is by default the first widget added to the layout.](https://www.pythonguis.com/static/tutorials/qt/layouts/qstackedlayout1.png) _QStackedLayout — in use only the uppermost widget is visible, which is by default the first widget added to the layout._
![QStackedLayout, with the 2nd \(1\) widget selected and brought to the front.](https://www.pythonguis.com/static/tutorials/qt/layouts/qstackedlayout2.png) _QStackedLayout, with the 2nd (1) widget selected and brought to the front._
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    layout = QStackedLayout()
    layout.addWidget(Color("red"))
    layout.addWidget(Color("green"))
    layout.addWidget(Color("blue"))
    layout.addWidget(Color("yellow"))
    layout.setCurrentIndex(3)
    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)

```

`QStackedWidget` is exactly how tabbed views in applications work. Only one view ('tab') is visible at any one time. You can control which widget to show at any time by using `.setCurrentIndex()` or `.setCurrentWidget()` to set the item by either the index (in order the widgets were added) or by the widget itself.
Below is a short demo using `QStackedLayout` in combination with `QButton` to provide a tab-like interface to an application:
python ```
import sys
from PyQt6.QtWidgets import (
  QApplication,
  QHBoxLayout,
  QMainWindow,
  QPushButton,
  QStackedLayout,
  QVBoxLayout,
  QWidget,
)
from layout_colorwidget import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    pagelayout = QVBoxLayout()
    button_layout = QHBoxLayout()
    self.stacklayout = QStackedLayout()
    pagelayout.addLayout(button_layout)
    pagelayout.addLayout(self.stacklayout)
    btn = QPushButton("red")
    btn.pressed.connect(self.activate_tab_1)
    button_layout.addWidget(btn)
    self.stacklayout.addWidget(Color("red"))
    btn = QPushButton("green")
    btn.pressed.connect(self.activate_tab_2)
    button_layout.addWidget(btn)
    self.stacklayout.addWidget(Color("green"))
    btn = QPushButton("yellow")
    btn.pressed.connect(self.activate_tab_3)
    button_layout.addWidget(btn)
    self.stacklayout.addWidget(Color("yellow"))
    widget = QWidget()
    widget.setLayout(pagelayout)
    self.setCentralWidget(widget)
  def activate_tab_1(self):
    self.stacklayout.setCurrentIndex(0)
  def activate_tab_2(self):
    self.stacklayout.setCurrentIndex(1)
  def activate_tab_3(self):
    self.stacklayout.setCurrentIndex(2)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

![A custom tab-like interface implemented using QStackedLayout.](https://www.pythonguis.com/static/tutorials/qt/layouts/layout8.png) _A custom tab-like interface implemented using QStackedLayout._
Helpfully. Qt actually provides a built-in tab widget that provides this kind of layout out of the box - albeit in widget form. Below the tab demo is recreated using `QTabWidget`:
python ```
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget
from layout_colorwidget import Color

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    tabs = QTabWidget()
    tabs.setTabPosition(QTabWidget.TabPosition.West)
    tabs.setMovable(True)
    for color in ["red", "green", "blue", "yellow"]:
      tabs.addTab(Color(color), color)
    self.setCentralWidget(tabs)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

![A tabbed interface using the QTabWidget.](https://www.pythonguis.com/static/tutorials/qt/layouts/layout9.png) _A tabbed interface using the QTabWidget._
As you can see, it's a little more straightforward — and a bit more attractive! You can set the position of the tabs using the cardinal directions, and toggle whether tabs are moveable with `.setMoveable`.
You'll notice that the macOS tab bar looks quite different from the others -- by default on macOS tabs take on a _pill_ or _bubble_ style. On macOS, this is typically used for tabbed configuration panels. For documents, you can turn on _document mode_ to give slimline tabs similar to what you see on other platforms. This option has no effect on other platforms:
python ```
  tabs = QTabWidget()
  tabs.setDocumentMode(True)

```

![QTabWidget in document mode on macOS.](https://www.pythonguis.com/static/tutorials/qt/layouts/layout9-mac-document.png) _QTabWidget in document mode on macOS._
We'll encounter more of these advanced widgets later.
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
Continue with [ PyQt6 Tutorial ](https://www.pythonguis.com/tutorials/pyqt6-actions-toolbars-menus/ "Continue to next part")
Return to [Create Desktop GUI Applications with PyQt6 ](https://www.pythonguis.com/pyqt6-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PyQt6 Layouts** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/pyqt6-layouts/Python books) on the subject. 
**PyQt6 Layouts** was published in [tutorials](https://www.pythonguis.com/tutorials/) on November 25, 2021 (updated March 28, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qt](https://www.pythonguis.com/topics/qt/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ foundation](https://www.pythonguis.com/topics/foundation/) [ pyqt6-foundation](https://www.pythonguis.com/topics/pyqt6-foundation/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
