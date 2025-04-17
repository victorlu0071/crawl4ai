# Content from: https://www.pythonguis.com/tutorials/pyside6-qgraphics-vector-graphics/

[](https://www.pythonguis.com/tutorials/pyside6-qgraphics-vector-graphics/#menu)
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
# Introduction to the QGraphics Framework in PySide6
Creating vector interfaces using the QGraphics View framework
by [Salem Al Bream](https://www.pythonguis.com/authors/salem-al-bream/) Last updated Mar 15 PySide6 [ QGraphics Framework in PySide6 ](https://www.pythonguis.com/pyside6-tutorial/#pyside6-qgraphics)
#### [ PySide6 Tutorial ](https://www.pythonguis.com/pyside6-tutorial/) — [QGraphics Framework in PySide6](https://www.pythonguis.com/pyside6-tutorial/#pyside6-qgraphics)
  * [Introduction to the QGraphics Framework in PySide6](https://www.pythonguis.com/tutorials/pyside6-qgraphics-vector-graphics/)


This tutorial is also available for [PyQt6](https://www.pythonguis.com/tutorials/pyqt6-qgraphics-vector-graphics/) , [PyQt5](https://www.pythonguis.com/tutorials/pyqt-qgraphics-vector-graphics/) and [PySide2](https://www.pythonguis.com/tutorials/pyside2-qgraphics-vector-graphics/)
The Qt Graphics View Framework allows you to develop _fast_ and _efficient_ 2D vector graphic scenes. Scenes can contain _millions_ of items, each with their own features and behaviors. By using the Graphics View via PySide6 you get access to this highly performant graphics layer in Python. Whether you're integrating vector graphics views into an existing PySide6 application, or simply want a powerful vector graphics interface for Python, Qt's Graphics View is what you're looking for.
Some common uses of the Graphics View include data visualization, mapping applications, 2D design tools, modern data dashboards and even 2D games.
In this tutorial we'll take our first steps looking at the Qt Graphics View framework, building a scene with some simple vector items. This will allow us to familiarize ourselves with the API and coordinate system, which we'll use later to build more complex examples.
Table of Contents
  * [The Graphics View Framework](https://www.pythonguis.com/tutorials/pyside6-qgraphics-vector-graphics/#the-graphics-view-framework)
  * [A simple scene](https://www.pythonguis.com/tutorials/pyside6-qgraphics-vector-graphics/#a-simple-scene)
    * [Adding items](https://www.pythonguis.com/tutorials/pyside6-qgraphics-vector-graphics/#adding-items)
    * [Making items moveable](https://www.pythonguis.com/tutorials/pyside6-qgraphics-vector-graphics/#making-items-moveable)
  * [Another way to create objects.](https://www.pythonguis.com/tutorials/pyside6-qgraphics-vector-graphics/#another-way-to-create-objects)
  * [Building a more complex scene](https://www.pythonguis.com/tutorials/pyside6-qgraphics-vector-graphics/#building-a-more-complex-scene)
  * [Adding graphics views to Qt layouts](https://www.pythonguis.com/tutorials/pyside6-qgraphics-vector-graphics/#adding-graphics-views-to-qt-layouts)


## The Graphics View Framework
The Graphics View framework consists of 3 main parts `QGraphicsView`, `QGraphicsScene`, and `QGraphicsItem`, each with different responsibilities.
The framework can be interpreted using the Model-View paradigm, with the `QGraphicsScene` as the _Model_ and the `QGraphicsView` as the _View_. Each scene can have multiple views. The _QGraphicsItems_ within the scene can be considered as items within the model, holding the visual data that the scene combines to define the complete image.
`QGraphicsScene` is the central component that glues everything together. It acts as a _whiteboard_ on which all items are drawn (circles, rectangles, lines, pixmaps, etc). The `QGraphicsView` has the responsibility of rendering a given scene -- or part of it, with some transformation (scaling, rotating, shearing) -- to display it to the user. The view is a standard Qt widget and can be placed inside any Qt layout.
`QGraphicsScene` provides some important functionalities out of the box, so we can use them to develop advanced applications without struggling with low-level details. For example --
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
  * **Collision Detection** , detect a graphics item is collided with another item.
  * **Item Selection** , gives us the ability to deal with multiple items at the same time, for example, the user can select multiple items, and when pressing delete, a function asks the scene to give the list for all selected items, and then delete them.
  * **Items discovery** , the scene can tell us what items are present (or part of them) at a specific point or inside some defined region, for example, if the user adds an item that intersects with a forbidden area, the program will detect them and give them another (mostly red) color.
  * **Events Propagation** , the scene receives the events and then propagates them to items.


To define a `QGraphicsScene` you define it's boundaries or _sceneRect_ which defines the x & y origins and dimensions of the scene. If you don't provide a _sceneRect_ it will default to the minimum bounding rectangle for all child items -- updating as items are added, moved or removed. This is flexible but less efficient.
Items in the scene are represented by `QGraphicsItem` objects. These are the basic building block of any 2D scene, representing a shape, pixmap or SVG image to be displayed in the scene. Each item has a relative position inside the `sceneRect` and can have different transformation effects (scale, translate, rotate, shear).
Finally, the `QGraphicsView` is the renderer of the scene, taking the scene and displaying it -- either wholly or in part -- to the user. The view itself can have transformations (scale, translate, rotate and shear) applied to modify the display without affecting the underlying scene. By default the view will forward mouse and keyboard events to the scene allowing for user interaction. This can be disabled by calling `view.setInteractive(False)`.
## A simple scene
Let's start by creating a simple scene. The following code creates `QGraphicsScene`, defining a 400 x 200 scene, and then displays it in a `QGraphicsView`.
python ```
import sys
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QApplication
app = QApplication(sys.argv)
# Defining a scene rect of 400x200, with it's origin at 0,0.
# If we don't set this on creation, we can set it later with .setSceneRect
scene = QGraphicsScene(0, 0, 400, 200)
view = QGraphicsView(scene)
view.show()
app.exec()

```

If you run this example you'll see an empty window.
![Empty Scene displayed in a window](https://www.pythonguis.com/static/tutorials/qt/introduction-to-qgraphics/scene-empty.png) _The empty graphics scene, shown in a QGraphicsView window._
Not very exciting yet -- but this is our `QGraphicsView` displaying our _empty_ scene.
As mentioned earlier, `QGraphicsView` is a _widget_. In Qt any widgets without a parent display as windows. This is why our `QGraphicsView` appears as a window on the desktop.
### Adding items
Let's start adding some items to the scene. There are a number of built-in _graphics items_ which you can customize and add to your scene. In the example below we use `QGraphicsRectItem` which draws a rectangle. We create the item passing in it's dimensions, and then set it's position pen and brush before adding it to the scene.
python ```
import sys
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem, QApplication
from PySide6.QtGui import QBrush, QPen
from PySide6.QtCore import Qt
app = QApplication(sys.argv)
# Defining a scene rect of 400x200, with it's origin at 0,0.
# If we don't set this on creation, we can set it later with .setSceneRect
scene = QGraphicsScene(0, 0, 400, 200)
# Draw a rectangle item, setting the dimensions.
rect = QGraphicsRectItem(0, 0, 200, 50)
# Set the origin (position) of the rectangle in the scene.
rect.setPos(50, 20)
# Define the brush (fill).
brush = QBrush(Qt.red)
rect.setBrush(brush)
# Define the pen (line)
pen = QPen(Qt.cyan)
pen.setWidth(10)
rect.setPen(pen)
scene.addItem(rect)
view = QGraphicsView(scene)
view.show()
app.exec()

```

Running the above you'll see a single, rather ugly colored, rectangle in the scene.
![A single rectangle in the scene](https://www.pythonguis.com/static/tutorials/qt/introduction-to-qgraphics/scene-single-item.png) _A single rectangle in the scene_
Adding more items is simply a case of creating the objects, customizing them and then adding them to the scene. In the example below we add an circle, using `QGraphicsEllipseItem` -- a circle is just an ellipse with equal height and width.
python ```
import sys
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsEllipseItem, QApplication
from PySide6.QtGui import QBrush, QPen
from PySide6.QtCore import Qt
app = QApplication(sys.argv)
# Defining a scene rect of 400x200, with it's origin at 0,0.
# If we don't set this on creation, we can set it later with .setSceneRect
scene = QGraphicsScene(0, 0, 400, 200)
# Draw a rectangle item, setting the dimensions.
rect = QGraphicsRectItem(0, 0, 200, 50)
# Set the origin (position) of the rectangle in the scene.
rect.setPos(50, 20)
# Define the brush (fill).
brush = QBrush(Qt.red)
rect.setBrush(brush)
# Define the pen (line)
pen = QPen(Qt.cyan)
pen.setWidth(10)
rect.setPen(pen)
ellipse = QGraphicsEllipseItem(0, 0, 100, 100)
ellipse.setPos(75, 30)
brush = QBrush(Qt.blue)
ellipse.setBrush(brush)
pen = QPen(Qt.green)
pen.setWidth(5)
ellipse.setPen(pen)
# Add the items to the scene. Items are stacked in the order they are added.
scene.addItem(ellipse)
scene.addItem(rect)

view = QGraphicsView(scene)
view.show()
app.exec()

```

The above code will give the following result.
![Scene with two items](https://www.pythonguis.com/static/tutorials/qt/introduction-to-qgraphics/scene-two-items.png) _A scene with two items_
The order you add items affects the stacking order in the scene -- items added later will always appear _on top_ of items added first. However, if you need more control you can _set_ the stacking order using `.setZValue`.
python ```
ellipse.setZValue(500)
rect.setZValue(200)

```

Now the circle (ellipse) appears above the rectangle.
![Using Zvalue to order items in the scene](https://www.pythonguis.com/static/tutorials/qt/introduction-to-qgraphics/scene-two-items-zvalue.png) _Using Zvalue to order items in the scene_
Try experimenting with setting the Z value of the two items -- you can set it _before_ or _after_ the items are in the scene, and can change it at any time.
Z in this context refers to the Z coordinate. The X & Y coordinates are the horizontal and vertical position in the scene respectively. The Z coordinate determines the relative position of items toward the front and back of the scene -- coming "out" of the screen towards the viewer.
There are also the convenience methods `.stackBefore()` and `.stackAfter()` which allow you to stack your `QGraphicsItem` behind, or in front of another item in the scene.
python ```
ellipse.stackAfter(rect)

```

### Making items moveable
Our two `QGraphicsItem` objects are currently fixed in position where we place them, but they don't have to be! As already mentioned Qt's Graphics View framework allows items to respond to user input, for example allowing them to be dragged and dropped around the scene at will. Simple functionality like is actually already built in, you just need to enable it on each `QGraphicsItem`. To do that we need to set the flag `QGraphicsItem.GraphicsItemFlags.ItemIsMoveable` on the item.
The full list of [graphics item flags is available here](https://doc.qt.io/qt-5/qgraphicsitem.html#GraphicsItemFlag-enum).
python ```
import sys
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsRectItem, QGraphicsEllipseItem, QApplication
from PySide6.QtGui import QBrush, QPen
from PySide6.QtCore import Qt
app = QApplication(sys.argv)
# Defining a scene rect of 400x200, with it's origin at 0,0.
# If we don't set this on creation, we can set it later with .setSceneRect
scene = QGraphicsScene(0, 0, 400, 200)
# Draw a rectangle item, setting the dimensions.
rect = QGraphicsRectItem(0, 0, 200, 50)
# Set the origin (position) of the rectangle in the scene.
rect.setPos(50, 20)
# Define the brush (fill).
brush = QBrush(Qt.red)
rect.setBrush(brush)
# Define the pen (line)
pen = QPen(Qt.cyan)
pen.setWidth(10)
rect.setPen(pen)
ellipse = QGraphicsEllipseItem(0, 0, 100, 100)
ellipse.setPos(75, 30)
brush = QBrush(Qt.blue)
ellipse.setBrush(brush)
pen = QPen(Qt.green)
pen.setWidth(5)
ellipse.setPen(pen)
# Add the items to the scene. Items are stacked in the order they are added.
scene.addItem(ellipse)
scene.addItem(rect)
ellipse.setFlag(QGraphicsItem.ItemIsMovable)
view = QGraphicsView(scene)
view.show()
app.exec()

```

In the above example we've set `ItemIsMovable` on the _ellipse_ only. You can drag the ellipse around the scene -- including behind the rectangle -- but the rectangle itself will remain locked in place. Experiment with adding more items and configuring the moveable status.
If you want an item to be _selectable_ you can enable this by setting the `ItemIsSelectable` flag, for example here using `.setFlags()` to set multiple flags at the same time. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
python ```
ellipse.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)

```

If you click on the ellipse you'll now see it surrounded by a dashed line to indicate that it is selected. We'll look at how to use item selection in more detail in a later tutorial.
![A selected item](https://www.pythonguis.com/static/tutorials/qt/introduction-to-qgraphics/scene-two-items-selectable.png) _A selected item in the scene, highlighted with dashed lines_
## Another way to create objects.
So far we've been creating items by creating the objects and _then_ adding them to the scene. But you can also create an object _in_ the scene directly by calling one of the helper methods on the scene itself, e.g. `scene.addEllipse()`. This _creates_ the object and _returns_ it so you can modify it as before.
python ```
import sys
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem, QApplication
from PySide6.QtGui import QBrush, QPen
from PySide6.QtCore import Qt
app = QApplication(sys.argv)
scene = QGraphicsScene(0, 0, 400, 200)
rect = scene.addRect(0, 0, 200, 50)
rect.setPos(50, 20)
# Define the brush (fill).
brush = QBrush(Qt.red)
rect.setBrush(brush)
# Define the pen (line)
pen = QPen(Qt.cyan)
pen.setWidth(10)
rect.setPen(pen)
view = QGraphicsView(scene)
view.show()
app.exec()

```

Feel free to use whichever form you find most comfortable in your code.
You can only use this approach for the built-in `QGraphicsItem` object types.
## Building a more complex scene
So far we've built a simple scene using the basic `QGraphicsRectItem` and `QGraphicsEllipseItem` shapes. Now let's use some other `QGraphicsItem` objects to build a more complex scene, including lines, text and `QPixmap` (images).
python ```
from PySide6.QtCore import QPointF, Qt
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsScene, QGraphicsView, QApplication
from PySide6.QtGui import QBrush, QPainter, QPen, QPixmap, QPolygonF
import sys
app = QApplication(sys.argv)
scene = QGraphicsScene(0, 0, 400, 200)
rectitem = QGraphicsRectItem(0, 0, 360, 20)
rectitem.setPos(20, 20)
rectitem.setBrush(QBrush(Qt.red))
rectitem.setPen(QPen(Qt.cyan))
scene.addItem(rectitem)
textitem = scene.addText("QGraphics is fun!")
textitem.setPos(100, 100)
scene.addPolygon(
  QPolygonF(
    [
      QPointF(30, 60),
      QPointF(270, 40),
      QPointF(400, 200),
      QPointF(20, 150),
    ]),
  QPen(Qt.darkGreen),
)
pixmap = QPixmap("cat.jpg")
pixmapitem = scene.addPixmap(pixmap)
pixmapitem.setPos(250, 70)
view = QGraphicsView(scene)
view.setRenderHint(QPainter.Antialiasing)
view.show()
app.exec()

```

If you run the example above you'll see the following scene.
![Scene with multiple items](https://www.pythonguis.com/static/tutorials/qt/introduction-to-qgraphics/scene-multiple-items.png) _Scene with multiple items including a rectangle, polygon, text and a pixmap._
Let's step through the code looking at the interesting bits.
Polygons are defined using a series of `QPointF` objects which give the coordinates relative to the _items_ position. So, for example if you create a polygon object with a point at 30, 20 and then move this polygon object X & Y coordinates 50, 40 then the point will be displayed at 80, 60 in the scene.
Points inside an item are always relative to the item itself, and item coordinates are always relative to the scene -- or the item's parent, if it has one. We'll take a closer look at the Graphics View coordinate system in the next tutorial.
To add an image to the scene we can open it from a file using `QPixmap()`. This creates a `QPixmap` object, which can then in turn add to the scene using `scene.addPixmap(pixmap)`. This returns a `QGraphicsPixmapItem` which is the `QGraphicsItem` type for the pixmap -- a wrapper than handles displaying the pixmap in the scene. You can use this object to perform any changes to item in the scene.
The multiple layers of objects can get confusing, so it's important to choose sensible variable names which make clear the distinction between, e.g. the _pixmap_ itself and the _pixmap item_ that contains it.
Finally, we set the flag `RenderHint,Antialiasing` on the view to _smooth_ the edges of diagonal lines. You almost _always_ want to enable this on your views as otherwise any rotated objects will look very ugly indeed. Below is our scene without antialiasing enabled, you can see the jagged lines on the polygon.
![Scene with multiple items](https://www.pythonguis.com/static/tutorials/qt/introduction-to-qgraphics/scene-multiple-items-noa.png) _Scene with antialiasing disabled._
Antialiasing has a (small) performance impact however, so if you are building scenes with millions of rotated items it may in some cases make sense to turn it off.
## Adding graphics views to Qt layouts
The `QGraphicsView` is subclassed from `QWidget`, meaning it can be placed in layouts just like any other widget. In the following example we add the view to a simple interface, with buttons which perform a basic effect on the view -- raising and lowering selected item's ZValue. This has the effect of allowing us to move items in front and behind other objects.
The full code is given below.
python ```
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QPainter, QPen
from PySide6.QtWidgets import (
  QApplication,
  QGraphicsEllipseItem,
  QGraphicsItem,
  QGraphicsRectItem,
  QGraphicsScene,
  QGraphicsView,
  QHBoxLayout,
  QPushButton,
  QSlider,
  QVBoxLayout,
  QWidget,
)

class Window(QWidget):
  def __init__(self):
    super().__init__()
    # Defining a scene rect of 400x200, with it's origin at 0,0.
    # If we don't set this on creation, we can set it later with .setSceneRect
    self.scene = QGraphicsScene(0, 0, 400, 200)
    # Draw a rectangle item, setting the dimensions.
    rect = QGraphicsRectItem(0, 0, 200, 50)
    rect.setPos(50, 20)
    brush = QBrush(Qt.red)
    rect.setBrush(brush)
    # Define the pen (line)
    pen = QPen(Qt.cyan)
    pen.setWidth(10)
    rect.setPen(pen)
    ellipse = QGraphicsEllipseItem(0, 0, 100, 100)
    ellipse.setPos(75, 30)
    brush = QBrush(Qt.blue)
    ellipse.setBrush(brush)
    pen = QPen(Qt.green)
    pen.setWidth(5)
    ellipse.setPen(pen)
    # Add the items to the scene. Items are stacked in the order they are added.
    self.scene.addItem(ellipse)
    self.scene.addItem(rect)
    # Set all items as moveable and selectable.
    for item in self.scene.items():
      item.setFlag(QGraphicsItem.ItemIsMovable)
      item.setFlag(QGraphicsItem.ItemIsSelectable)
    # Define our layout.
    vbox = QVBoxLayout()
    up = QPushButton("Up")
    up.clicked.connect(self.up)
    vbox.addWidget(up)
    down = QPushButton("Down")
    down.clicked.connect(self.down)
    vbox.addWidget(down)
    rotate = QSlider()
    rotate.setRange(0, 360)
    rotate.valueChanged.connect(self.rotate)
    vbox.addWidget(rotate)
    view = QGraphicsView(self.scene)
    view.setRenderHint(QPainter.Antialiasing)
    hbox = QHBoxLayout(self)
    hbox.addLayout(vbox)
    hbox.addWidget(view)
    self.setLayout(hbox)
  def up(self):
    """ Iterate all selected items in the view, moving them forward. """
    items = self.scene.selectedItems()
    for item in items:
      z = item.zValue()
      item.setZValue(z + 1)
  def down(self):
    """ Iterate all selected items in the view, moving them backward. """
    items = self.scene.selectedItems()
    for item in items:
      z = item.zValue()
      item.setZValue(z - 1)
  def rotate(self, value):
    """ Rotate the object by the received number of degrees """
    items = self.scene.selectedItems()
    for item in items:
      item.setRotation(value)

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec()

```

If you run this, you will get a window like that shown below. By selecting an item in the graphics view and then clicking either the "Up" or "Down" button you can move items up and down within the scene -- behind and in front of one another. The items are all moveable, so you can drag them around too. Clicking on the slider will rotate the currently selected items by the set number of degrees.
![A graphics scene with some custom controls](https://www.pythonguis.com/static/tutorials/qt/introduction-to-qgraphics/scene-controls.png) _A graphics scene with some custom controls_
The raising and lowering is handled by our custom methods `up` and `down`, which work by iterating over the _currently selected_ items in the scene -- retrieved using `scene.selectedItems()` and then getting the items z value and increasing or decreasing it respectively.
python ```
  def up(self):
    """ Iterate all selected items in the view, moving them forward. """
    items = self.scene.selectedItems()
    for item in items:
      z = item.zValue()
      item.setZValue(z + 1)

```

While rotation is handled using the `item.setRotation` method. This receives the current angle from the `QSlider` and again, applies it to any currently selected items in the scene.
python ```

  def rotate(self, value):
    """ Rotate the object by the received number of degrees. """
    items = self.scene.selectedItems()
    for item in items:
      item.setRotation(value)

```

Take a look at the [QGraphicsItem documentation](https://doc.qt.io/qt-5/qgraphicsitem.html) for some other properties you can control with widgets and try extending the interface to allow you to change them dynamically.
Hopefully this quick introduction to the Qt Graphics View framework has given you some ideas of what you can do with it. In the next tutorials we'll look at how events and user interaction can be handled on items and how to create custom & compound items for your own scenes. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Salem Al Bream](https://www.pythonguis.com/static/theme/images/authors/salem-al-bream.jpg)](https://www.pythonguis.com/authors/salem-al-bream/)
**Introduction to the QGraphics Framework in PySide6** was written by [Salem Al Bream](https://www.pythonguis.com/authors/salem-al-bream/) with contributions from [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
**Introduction to the QGraphics Framework in PySide6** was published in [tutorials](https://www.pythonguis.com/tutorials/) on September 27, 2024 (updated March 15, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[python](https://www.pythonguis.com/topics/python/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [desktop-application](https://www.pythonguis.com/topics/desktop-application/) [qgraphics](https://www.pythonguis.com/topics/qgraphics/) [qgraphicsitem](https://www.pythonguis.com/topics/qgraphicsitem/) [qgraphicsview](https://www.pythonguis.com/topics/qgraphicsview/) [vector-graphics](https://www.pythonguis.com/topics/vector-graphics/) [pyside6-vector-graphics](https://www.pythonguis.com/topics/pyside6-vector-graphics/) [qt](https://www.pythonguis.com/topics/qt/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
