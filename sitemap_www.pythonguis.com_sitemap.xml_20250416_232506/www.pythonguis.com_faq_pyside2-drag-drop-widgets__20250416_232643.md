# Content from: https://www.pythonguis.com/faq/pyside2-drag-drop-widgets/

[](https://www.pythonguis.com/faq/pyside2-drag-drop-widgets/#menu)
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
# Drag & Drop Widgets with PySide2
Sort widgets visually with drag and drop in a container
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Mar 12 PySide2 [ FAQ ](https://www.pythonguis.com/faq/)
This tutorial is also available for [PySide6](https://www.pythonguis.com/faq/pyside6-drag-drop-widgets/) , [PyQt6](https://www.pythonguis.com/faq/pyqt6-drag-drop-widgets/) and [PyQt5](https://www.pythonguis.com/faq/pyqt-drag-drop-widgets/)
I had an interesting question from a reader of my [Pyside2 book](https://www.pythonguis.com/pyside2-book/), about how to handle dragging and dropping of widgets in a container showing the dragged widget as it is moved.
> I'm interested in managing movement of a QWidget with mouse in a container. I've implemented the application with drag & drop, exchanging the position of buttons, but I want to show the motion of `QPushButton`, like what you see in Qt Designer. Dragging a widget should show the widget itself, not just the mouse pointer.
First, we'll implement the simple case which drags widgets without showing anything extra. Then we can extend it to answer the question. By the end of this quick tutorial we'll have a generic drag drop implementation which looks like the following.
Table of Contents
  * [Drag & Drop Widgets](https://www.pythonguis.com/faq/pyside2-drag-drop-widgets/#drag-drop-widgets)
  * [Visual Drag & Drop](https://www.pythonguis.com/faq/pyside2-drag-drop-widgets/#visual-drag-drop)
  * [Generic Drag & Drop Container](https://www.pythonguis.com/faq/pyside2-drag-drop-widgets/#generic-drag-drop-container)
  * [Adding a Visual Drop Target](https://www.pythonguis.com/faq/pyside2-drag-drop-widgets/#adding-a-visual-drop-target)


## Drag & Drop Widgets
We'll start with a simple application which creates a window using `QWidget` and places a series of `QPushButton` widgets into it.
You can substitute `QPushButton` for any other widget you like, e.g. `QLabel`. Any widget can have drag behavior implemented on it, although some input widgets will not work well as we capture the mouse events for the drag.
python ```
from PySide2.QtWidgets import QApplication, QHBoxLayout, QWidget, QPushButton

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.blayout = QHBoxLayout()
    for l in ['A', 'B', 'C', 'D']:
      btn = QPushButton(l)
      self.blayout.addWidget(btn)
    self.setLayout(self.blayout)

app = QApplication([])
w = Window()
w.show()
app.exec_()

```

If you run this you should see something like this. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyside2-book/) _by Martin Fitzpatrick_ — (PySide2 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside2-book/) [Get the book](https://secure.pythonguis.com/01hf778jyaajk5vk1q6824sd44/)
![Widgets in a layout](https://www.pythonguis.com/static/faq/drag-drop-widgets/windows-in-layout.png) _The series of`QPushButton widgets` in a horizontal layout._
Here we're creating a window, but the `Window` widget is subclassed from `QWidget`, meaning you can add this widget to any other layout. See later for an example of a generic object sorting widget.
`QPushButton` objects aren't usually draggable, so to handle the mouse movements and initiate a drag we need to implement a subclass. We can add the following to the top of the file.
python ```
from PySide2.QtWidgets import QApplication, QHBoxLayout, QWidget, QPushButton
from PySide2.QtCore import Qt, QMimeData
from PySide2.QtGui import QDrag

class DragButton(QPushButton):
  def mouseMoveEvent(self, e):
    if e.buttons() == Qt.LeftButton:
      drag = QDrag(self)
      mime = QMimeData()
      drag.setMimeData(mime)
      drag.exec_(Qt.MoveAction)


```

We implement a `mouseMoveEvent` which accepts the single `e` parameter of the event. We check to see if the _left_ mouse button is pressed on this event -- as it would be when dragging -- and then initiate a drag. To start a drag, we create a `QDrag` object, passing in `self` to give us access later to the widget that was dragged. We also _must_ pass in mime data. This is used for including information about what is dragged, particularly for passing data between applications. However, as here, it is fine to leave this empty.
Finally, we initiate a drag by calling `drag.exec_(Qt.MoveAction)`. As with dialogs `exec_()` starts a new event loop, blocking the main loop until the drag is complete. The parameter `Qt.MoveAction` tells the drag handler what type of operation is happening, so it can show the appropriate icon tip to the user.
You can update the main window code to use our new `DragButton` class as follows.
python ```

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setAcceptDrops(True)
    self.blayout = QHBoxLayout()
    for l in ['A', 'B', 'C', 'D']:
      btn = DragButton(l)
      self.blayout.addWidget(btn)
    self.setLayout(self.blayout)

```

If you run the code now, you _can_ drag the buttons, but you'll notice the drag is forbidden.
![Drag forbidden](https://www.pythonguis.com/static/faq/drag-drop-widgets/drag-forbidden.png) _Dragging of the widget starts but is forbidden._
What's happening? The mouse movement is being detected by our `DragButton` object and the drag started, but the main window does not accept drag & drop.
To fix this we need to enable drops on the window and implement `dragEnterEvent` to actually accept them.
python ```
class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setAcceptDrops(True)
    self.blayout = QHBoxLayout()
    for l in ['A', 'B', 'C', 'D']:
      btn = DragButton(l)
      self.blayout.addWidget(btn)
    self.setLayout(self.blayout)
  def dragEnterEvent(self, e):
    e.accept()

```

If you run this now, you'll see the drag is now accepted and you see the move icon. This indicates that the drag has started and been accepted by the window we're dragging onto. The icon shown is determined by the action we pass when calling `drag.exec_()`.
![Drag accepted](https://www.pythonguis.com/static/faq/drag-drop-widgets/drag-accepted.png) _Dragging of the widget starts and is accepted, showing a move icon._
Releasing the mouse button during a drag drop operation triggers a `dropEvent` on the widget you're currently hovering the mouse over (if it is configured to accept drops). In our case that's the window. To handle the move we need to implement the code to do this in our `dropEvent` method.
The drop event contains the position the mouse was at when the button was released & the drop triggered. We can use this to determine where to move the widget to.
To determine where to place the widget, we iterate over all the widgets in the layout, _until_ we find one who's `x` position is _greater_ than that of the mouse pointer. If so then when insert the widget directly to the left of this widget and exit the loop.
If we get to the end of the loop without finding a match, we must be dropping past the end of the existing items, so we increment `n` one further (in the `else:` block below).
python ```
  def dropEvent(self, e):
    pos = e.pos()
    widget = e.source()
    self.blayout.removeWidget(widget)
    for n in range(self.blayout.count()):
      # Get the widget at each index in turn.
      w = self.blayout.itemAt(n).widget()
      if pos.x() < w.x():
        # We didn't drag past this widget.
        # insert to the left of it.
        break
    else:
      # We aren't on the left hand side of any widget,
      # so we're at the end. Increment 1 to insert after.
      n += 1
    self.blayout.insertWidget(n, widget)
    e.accept()

```

The effect of this is that if you drag 1 pixel past the start of another widget the drop will happen to the right of it, which is a bit confusing. To fix this we can adjust the cut off to use the middle of the widget using `if pos.x() < w.x() + w.size().width() // 2:` -- that is x + half of the width.
python ```
  def dropEvent(self, e):
    pos = e.pos()
    widget = e.source()
    self.blayout.removeWidget(widget)
    for n in range(self.blayout.count()):
      # Get the widget at each index in turn.
      w = self.blayout.itemAt(n).widget()
      if pos.x() < w.x() + w.size().width() // 2:
        # We didn't drag past this widget.
        # insert to the left of it.
        break
    else:
      # We aren't on the left hand side of any widget,
      # so we're at the end. Increment 1 to insert after.
      n += 1
    self.blayout.insertWidget(n, widget)
    e.accept()

```

The complete working drag-drop code is shown below.
python ```
from PySide2.QtCore import QMimeData, Qt
from PySide2.QtGui import QDrag
from PySide2.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget

class DragButton(QPushButton):
  def mouseMoveEvent(self, e):
    if e.buttons() == Qt.LeftButton:
      drag = QDrag(self)
      mime = QMimeData()
      drag.setMimeData(mime)
      drag.exec_(Qt.MoveAction)

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setAcceptDrops(True)
    self.blayout = QHBoxLayout()
    for l in ["A", "B", "C", "D"]:
      btn = DragButton(l)
      self.blayout.addWidget(btn)
    self.setLayout(self.blayout)
  def dragEnterEvent(self, e):
    e.accept()
  def dropEvent(self, e):
    pos = e.pos()
    widget = e.source()
    self.blayout.removeWidget(widget)
    for n in range(self.blayout.count()):
      # Get the widget at each index in turn.
      w = self.blayout.itemAt(n).widget()
      if pos.x() < w.x() + w.size().width() // 2:
        # We didn't drag past this widget.
        # insert to the left of it.
        break
    else:
      # We aren't on the left hand side of any widget,
      # so we're at the end. Increment 1 to insert after.
      n += 1
    self.blayout.insertWidget(n, widget)
    e.accept()

app = QApplication([])
w = Window()
w.show()
app.exec_()

```

## Visual Drag & Drop
We now have a working drag & drop implementation. Next we'll move onto improving the UX by showing the drag visually. First we'll add support for showing the button being dragged next to the mouse point as it is dragged. That way the user knows exactly what it is they are dragging.
Qt's `QDrag` handler natively provides a mechanism for showing dragged objects which we can use. We can update our `DragButton` class to pass a _pixmap_ image to `QDrag` and this will be displayed under the mouse pointer as the drag occurs. To show the widget, we just need to get a `QPixmap` of the widget we're dragging.
python ```
from PySide2.QtCore import QMimeData, Qt
from PySide2.QtGui import QDrag, QPixmap
from PySide2.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget

class DragButton(QPushButton):
  def mouseMoveEvent(self, e):
    if e.buttons() == Qt.LeftButton:
      drag = QDrag(self)
      mime = QMimeData()
      drag.setMimeData(mime)
      pixmap = QPixmap(self.size())
      self.render(pixmap)
      drag.setPixmap(pixmap)
      drag.exec_(Qt.MoveAction)


```

To create the pixmap we create a `QPixmap` object passing in the size of the widget this event is fired on with `self.size()`. This creates an empty _pixmap_ which we can then pass into `self.render` to _render_ -- or draw -- the current widget onto it. That's it. Then we set the resulting pixmap on the `drag` object.
If you run the code with this modification you'll see something like the following --
![Drag visual](https://www.pythonguis.com/static/faq/drag-drop-widgets/drag-visual.png) _Dragging of the widget showing the dragged widget._
## Generic Drag & Drop Container
We now have a working drag and drop behavior implemented on our window. We can take this a step further and implement a _generic_ drag drop widget which allows us to sort arbitrary objects. In the code below we've created a new widget `DragWidget` which can be added to any window.
You can add _items_ -- instances of `DragItem` -- which you want to be sorted, as well as setting data on them. When items are re-ordered the new order is emitted as a signal `orderChanged`.
python ```
from PySide2.QtCore import QMimeData, Qt, Signal
from PySide2.QtGui import QDrag, QPixmap
from PySide2.QtWidgets import (
  QApplication,
  QHBoxLayout,
  QLabel,
  QMainWindow,
  QVBoxLayout,
  QWidget,
)

class DragItem(QLabel):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setContentsMargins(25, 5, 25, 5)
    self.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setStyleSheet("border: 1px solid black;")
    # Store data separately from display label, but use label for default.
    self.data = self.text()
  def set_data(self, data):
    self.data = data
  def mouseMoveEvent(self, e):
    if e.buttons() == Qt.LeftButton:
      drag = QDrag(self)
      mime = QMimeData()
      drag.setMimeData(mime)
      pixmap = QPixmap(self.size())
      self.render(pixmap)
      drag.setPixmap(pixmap)
      drag.exec_(Qt.MoveAction)

class DragWidget(QWidget):
  """
  Generic list sorting handler.
  """
  orderChanged = Signal(list)
  def __init__(self, *args, orientation=Qt.Orientation.Vertical, **kwargs):
    super().__init__()
    self.setAcceptDrops(True)
    # Store the orientation for drag checks later.
    self.orientation = orientation
    if self.orientation == Qt.Orientation.Vertical:
      self.blayout = QVBoxLayout()
    else:
      self.blayout = QHBoxLayout()
    self.setLayout(self.blayout)
  def dragEnterEvent(self, e):
    e.accept()
  def dropEvent(self, e):
    pos = e.pos()
    widget = e.source()
    self.blayout.removeWidget(widget)
    for n in range(self.blayout.count()):
      # Get the widget at each index in turn.
      w = self.blayout.itemAt(n).widget()
      if self.orientation == Qt.Orientation.Vertical:
        # Drag drop vertically.
        drop_here = pos.y() < w.y() + w.size().height() // 2
      else:
        # Drag drop horizontally.
        drop_here = pos.x() < w.x() + w.size().width() // 2
      if drop_here:
        break
    else:
      # We aren't on the left hand/upper side of any widget,
      # so we're at the end. Increment 1 to insert after.
      n += 1
    self.blayout.insertWidget(n, widget)
    self.orderChanged.emit(self.get_item_data())
    e.accept()
  def add_item(self, item):
    self.blayout.addWidget(item)
  def get_item_data(self):
    data = []
    for n in range(self.blayout.count()):
      # Get the widget at each index in turn.
      w = self.blayout.itemAt(n).widget()
      data.append(w.data)
    return data

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.drag = DragWidget(orientation=Qt.Orientation.Vertical)
    for n, l in enumerate(["A", "B", "C", "D"]):
      item = DragItem(l)
      item.set_data(n) # Store the data.
      self.drag.add_item(item)
    # Print out the changed order.
    self.drag.orderChanged.connect(print)
    container = QWidget()
    layout = QVBoxLayout()
    layout.addStretch(1)
    layout.addWidget(self.drag)
    layout.addStretch(1)
    container.setLayout(layout)
    self.setCentralWidget(container)

app = QApplication([])
w = MainWindow()
w.show()
app.exec_()

```

![Generic drag drop horizontal](https://www.pythonguis.com/static/faq/drag-drop-widgets/drag-generic-horizontal.png) _Generic drag-drop sorting in horizontal orientation._
You'll notice that when creating the item, you can set the label by passing it in as a parameter (just like for a normal `QLabel` which we've subclassed from). But you can also set a data value, which is the internal value of this item -- this is what will be emitted when the order changes, or if you call `get_item_data` yourself. This separates the visual representation from what is actually being sorted, meaning you can use this to sort _anything_ not just strings.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
In the example above we're passing in the enumerated index as the data, so dragging will output (via the `print` connected to `orderChanged`) something like:
python ```
[1, 0, 2, 3]
[1, 2, 0, 3]
[1, 0, 2, 3]
[1, 2, 0, 3]

```

If you remove the `item.set_data(n)` you'll see the labels emitted on changes.
python ```
['B', 'A', 'C', 'D']
['B', 'C', 'A', 'D']

```

We've also implemented _orientation_ onto the `DragWidget` using the Qt built in flags `Qt.Orientation.Vertical` or `Qt.Orientation.Horizontal`. This setting this allows you sort items either vertically or horizontally -- the calculations are handled for both directions.
![Generic drag drop vertical](https://www.pythonguis.com/static/faq/drag-drop-widgets/drag-generic-vertical.png) _Generic drag-drop sorting in vertical orientation._
## Adding a Visual Drop Target
If you experiment with the drag-drop tool above you'll notice that it doesn't feel completely intuitive. When dragging you don't know where an item will be inserted until you drop it. If it ends up in the wrong place, you'll then need to pick it up and re-drop it again, using _guesswork_ to get it right.
With a bit of practice you can get the hang of it, but it would be nicer to make the behavior immediately obvious for users. Many drag-drop interfaces solve this problem by showing a preview of where the item will be dropped while dragging -- either by showing the item in the place where it will be dropped, or showing some kind of placeholder.
In this final section we'll implement this type of drag and drop preview indicator.
The first step is to define our target indicator. This is just another label, which in our example is empty, with custom styles applied to make it have a solid "shadow" like background. This makes it obviously different to the items in the list, so it stands out as something distinct.
python ```
from PySide2.QtCore import QMimeData, Qt, Signal
from PySide2.QtGui import QDrag, QPixmap
from PySide2.QtWidgets import (
  QApplication,
  QHBoxLayout,
  QLabel,
  QMainWindow,
  QVBoxLayout,
  QWidget,
)

class DragTargetIndicator(QLabel):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setContentsMargins(25, 5, 25, 5)
    self.setStyleSheet(
      "QLabel { background-color: #ccc; border: 1px solid black; }"
    )


```

We've copied the contents margins from the items in the list. If you change your list items, remember to also update the indicator dimensions to match.
The drag item is unchanged, but we need to implement some additional behavior on our `DragWidget` to add the target, control showing and moving it.
First we'll add the drag target indicator to the layout on our `DragWidget`. This is hidden to begin with, but will be shown during the drag.
python ```

class DragWidget(QWidget):
  """
  Generic list sorting handler.
  """
  orderChanged = Signal(list)
  def __init__(self, *args, orientation=Qt.Orientation.Vertical, **kwargs):
    super().__init__()
    self.setAcceptDrops(True)
    # Store the orientation for drag checks later.
    self.orientation = orientation
    if self.orientation == Qt.Orientation.Vertical:
      self.blayout = QVBoxLayout()
    else:
      self.blayout = QHBoxLayout()
    # Add the drag target indicator. This is invisible by default,
    # we show it and move it around while the drag is active.
    self._drag_target_indicator = DragTargetIndicator()
    self.blayout.addWidget(self._drag_target_indicator)
    self._drag_target_indicator.hide()
    self.setLayout(self.blayout)

```

Next we modify the `DragWidget.dragMoveEvent` to show the drag target indicator. We show it by _inserting_ it into the layout and then calling `.show` -- inserting a widget which is already in a layout will move it. We also hide the original item which is being dragged.
In the earlier examples we determined the position on drop by removing the widget being dragged, and then iterating over what is left. Because we now need to calculate the drop location before the drop, we take a different approach.
If we wanted to do it the same way, we'd need to remove the item on drag start, hold onto it and implement re-inserting at it's old position on drag fail. That's a lot of work.
Instead, the dragged item is left in place and hidden during move.
python ```
  def dragMoveEvent(self, e):
    # Find the correct location of the drop target, so we can move it there.
    index = self._find_drop_location(e)
    if index is not None:
      # Inserting moves the item if its alreaady in the layout.
      self.blayout.insertWidget(index, self._drag_target_indicator)
      # Hide the item being dragged.
      e.source().hide()
      # Show the target.
      self._drag_target_indicator.show()
    e.accept()

```

The method `self._find_drop_location` finds the index where the drag target will be shown (or the item dropped when the mouse released). We'll implement that next.
The calculation of the drop location follows the same pattern as before. We iterate over the items in the layout and calculate whether our mouse drop location is to the left of each widget. If it isn't to the left of any widget, we drop on the far right.
python ```
  def _find_drop_location(self, e):
    pos = e.pos()
    spacing = self.blayout.spacing() / 2
    for n in range(self.blayout.count()):
      # Get the widget at each index in turn.
      w = self.blayout.itemAt(n).widget()
      if self.orientation == Qt.Orientation.Vertical:
        # Drag drop vertically.
        drop_here = (
          pos.y() >= w.y() - spacing
          and pos.y() <= w.y() + w.size().height() + spacing
        )
      else:
        # Drag drop horizontally.
        drop_here = (
          pos.x() >= w.x() - spacing
          and pos.x() <= w.x() + w.size().width() + spacing
        )
      if drop_here:
        # Drop over this target.
        break
    return n

```

The drop location `n` is returned for use in the `dragMoveEvent` to place the drop target indicator.
Next wee need to update the `get_item_data` handler to ignore the drop target indicator. To do this we check `w` against `self._drag_target_indicator` and skip if it is the same. With this change the method will work as expected.
python ```
  def get_item_data(self):
    data = []
    for n in range(self.blayout.count()):
      # Get the widget at each index in turn.
      w = self.blayout.itemAt(n).widget()
      if w != self._drag_target_indicator:
        # The target indicator has no data.
        data.append(w.data)
    return data

```

If you run the code a this point the drag behavior will work as expected. But if you drag the widget outside of the window and drop you'll notice a problem: the target indicator will stay in place, but dropping the item won't drop the item in that position (the drop will be cancelled).
To fix that we need to implement a `dragLeaveEvent` which hides the indicator.
python ```
  def dragLeaveEvent(self, e):
    self._drag_target_indicator.hide()
    e.accept()

```

With those changes, the drag-drop behavior should be working as intended. The complete code is shown below.
python ```
from PySide2.QtCore import QMimeData, Qt, Signal
from PySide2.QtGui import QDrag, QPixmap
from PySide2.QtWidgets import (
  QApplication,
  QHBoxLayout,
  QLabel,
  QMainWindow,
  QVBoxLayout,
  QWidget,
)

class DragTargetIndicator(QLabel):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setContentsMargins(25, 5, 25, 5)
    self.setStyleSheet(
      "QLabel { background-color: #ccc; border: 1px solid black; }"
    )

class DragItem(QLabel):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setContentsMargins(25, 5, 25, 5)
    self.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setStyleSheet("border: 1px solid black;")
    # Store data separately from display label, but use label for default.
    self.data = self.text()
  def set_data(self, data):
    self.data = data
  def mouseMoveEvent(self, e):
    if e.buttons() == Qt.LeftButton:
      drag = QDrag(self)
      mime = QMimeData()
      drag.setMimeData(mime)
      pixmap = QPixmap(self.size())
      self.render(pixmap)
      drag.setPixmap(pixmap)
      drag.exec_(Qt.MoveAction)
      self.show() # Show this widget again, if it's dropped outside.

class DragWidget(QWidget):
  """
  Generic list sorting handler.
  """
  orderChanged = Signal(list)
  def __init__(self, *args, orientation=Qt.Orientation.Vertical, **kwargs):
    super().__init__()
    self.setAcceptDrops(True)
    # Store the orientation for drag checks later.
    self.orientation = orientation
    if self.orientation == Qt.Orientation.Vertical:
      self.blayout = QVBoxLayout()
    else:
      self.blayout = QHBoxLayout()
    # Add the drag target indicator. This is invisible by default,
    # we show it and move it around while the drag is active.
    self._drag_target_indicator = DragTargetIndicator()
    self.blayout.addWidget(self._drag_target_indicator)
    self._drag_target_indicator.hide()
    self.setLayout(self.blayout)
  def dragEnterEvent(self, e):
    e.accept()
  def dragLeaveEvent(self, e):
    self._drag_target_indicator.hide()
    e.accept()
  def dragMoveEvent(self, e):
    # Find the correct location of the drop target, so we can move it there.
    index = self._find_drop_location(e)
    if index is not None:
      # Inserting moves the item if its alreaady in the layout.
      self.blayout.insertWidget(index, self._drag_target_indicator)
      # Hide the item being dragged.
      e.source().hide()
      # Show the target.
      self._drag_target_indicator.show()
    e.accept()
  def dropEvent(self, e):
    widget = e.source()
    # Use drop target location for destination, then remove it.
    self._drag_target_indicator.hide()
    index = self.blayout.indexOf(self._drag_target_indicator)
    if index is not None:
      self.blayout.insertWidget(index, widget)
      self.orderChanged.emit(self.get_item_data())
      widget.show()
      self.blayout.activate()
    e.accept()
  def _find_drop_location(self, e):
    pos = e.pos()
    spacing = self.blayout.spacing() / 2
    for n in range(self.blayout.count()):
      # Get the widget at each index in turn.
      w = self.blayout.itemAt(n).widget()
      if self.orientation == Qt.Orientation.Vertical:
        # Drag drop vertically.
        drop_here = (
          pos.y() >= w.y() - spacing
          and pos.y() <= w.y() + w.size().height() + spacing
        )
      else:
        # Drag drop horizontally.
        drop_here = (
          pos.x() >= w.x() - spacing
          and pos.x() <= w.x() + w.size().width() + spacing
        )
      if drop_here:
        # Drop over this target.
        break
    return n
  def add_item(self, item):
    self.blayout.addWidget(item)
  def get_item_data(self):
    data = []
    for n in range(self.blayout.count()):
      # Get the widget at each index in turn.
      w = self.blayout.itemAt(n).widget()
      if w != self._drag_target_indicator:
        # The target indicator has no data.
        data.append(w.data)
    return data

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.drag = DragWidget(orientation=Qt.Orientation.Vertical)
    for n, l in enumerate(["A", "B", "C", "D"]):
      item = DragItem(l)
      item.set_data(n) # Store the data.
      self.drag.add_item(item)
    # Print out the changed order.
    self.drag.orderChanged.connect(print)
    container = QWidget()
    layout = QVBoxLayout()
    layout.addStretch(1)
    layout.addWidget(self.drag)
    layout.addStretch(1)
    container.setLayout(layout)
    self.setCentralWidget(container)

app = QApplication([])
w = MainWindow()
w.show()
app.exec_()

```

If you run this example on macOS you may notice that the widget drag preview (the `QPixmap` created on `DragItem`) is a bit blurry. On high-resolution screens you need to set the _device pixel ratio_ and scale up the pixmap when you create it. Below is a modified `DragItem` class which does this.
Update `DragItem` to support high resolution screens.
python ```
class DragItem(QLabel):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setContentsMargins(25, 5, 25, 5)
    self.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setStyleSheet("border: 1px solid black;")
    # Store data separately from display label, but use label for default.
    self.data = self.text()
  def set_data(self, data):
    self.data = data
  def mouseMoveEvent(self, e):
    if e.buttons() == Qt.LeftButton:
      drag = QDrag(self)
      mime = QMimeData()
      drag.setMimeData(mime)
      # Render at x2 pixel ratio to avoid blur on Retina screens.
      pixmap = QPixmap(self.size().width() * 2, self.size().height() * 2)
      pixmap.setDevicePixelRatio(2)
      self.render(pixmap)
      drag.setPixmap(pixmap)
      drag.exec_(Qt.MoveAction)
      self.show() # Show this widget again, if it's dropped outside.

```

That's it! We've created a generic drag-drop handled which can be added to any projects where you need to be able to reposition items within a list. You should feel free to experiment with the styling of the drag items and targets as this won't affect the behavior.
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Drag & Drop Widgets with PySide2** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyside2-drag-drop-widgets/Python books) on the subject. 
**Drag & Drop Widgets with PySide2** was published in [faq](https://www.pythonguis.com/faq/) on January 07, 2022 (updated March 12, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[drag-drop](https://www.pythonguis.com/topics/drag-drop/) [widgets](https://www.pythonguis.com/topics/widgets/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [drag](https://www.pythonguis.com/topics/drag/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
