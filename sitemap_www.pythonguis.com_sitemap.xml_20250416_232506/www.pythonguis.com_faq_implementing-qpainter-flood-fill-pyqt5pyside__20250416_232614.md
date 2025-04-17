# Content from: https://www.pythonguis.com/faq/implementing-qpainter-flood-fill-pyqt5pyside/

[](https://www.pythonguis.com/faq/implementing-qpainter-flood-fill-pyqt5pyside/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
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
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Implementing QPainter flood fill in PyQt5/PySide
Filling irregular regions in a QPainter canvas
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ FAQ ](https://www.pythonguis.com/faq/)
Building [Piecasso](https://github.com/mfitzp/15-minute-apps/blob/master/paint/) (a PyQt5 Paint clone) I was disappointed to discover that while [QPainter](https://doc.qt.io/qt-5/qpainter.html) comes with a huge number of paint methods, ranging from pixels and lines to fully-filled polygons, it _doesn't_ include a method for flood filling regions of an image.
That makes a lot of sense, firstly because flood-filling is slow to do — requiring a pixel-by-pixel search through an image — and it's _not that useful_ when drawing a UI, since you usually (and probably should) know what you're drawing and where.
Still, I was disappointed there wasn't one, because I _needed_ one for my app. What's Paint without being able to fill raggedy shapes in horrible colours?
![Raggedy fill](https://www.pythonguis.com/static/faq/implementing-qpainter-flood-fill-pyqt5pyside/raggedy.png) _Raggedy fill_
In this short walkthrough I'll cover the process of implementing a basic flood-fill algorithm in PyQt5, using `QImage.pixel()`. If you find yourself needing flood fill in your own apps, this will do the trick.
## Flood fill algorithm
The implementation here uses a basic [Forest Fire](https://en.wikipedia.org/wiki/Flood_fill) flood fill algorithm. In this approach we start from any given pixel, and iteratively check if any adjacent pixels match, and then any adjacent pixels of those pixels, and …so on. Once we've tested a given pixel we don't need to return to it so we can colour it with our target colour.
This is analogous to a forest fire which starts from a given point and spreads outwards, but will not return to areas it's already "burnt" (changed colour). The following animation gives a good visualisation of the process. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
![Flood fill visualisation](https://i.imgur.com/GlhwcMc.gif)
The steps of the algorithm are explained below.
  1. Start with our start pixel, _fill_ colour, and two empty lists `seen` and `queue`.
  2. Look at our current pixel's colour. This is the _target_ for our fill. Store this initial location in `queue`.
  3. Taking the first item from `queue` (initially our start (x,y) location) look at each of the 4 pixels surrounding our location (cardinal points)
  4.     1. If they have not been previously _seen_ — compare their colour to the one we're looking for.
  5. If they match, add the (x,y) location to `queue` and update the pixel with the _fill_ colour.
  6. Add the (x,y) location to `seen` to keep track of where we've looked before (and avoid the overhead of looking again).
  7. Repeat from step 3, until the queue is empty.


You _can_ opt to check 8 directions, if you want to be able to fill through diagonal gaps.
The order you visit pixels will change depending on whether you add new locations to the beginning or end of your `queue` list. But this won't affect the result.
Below we'll look at implementing this algorithm in Python, using PyQt5/PySide2. The `fill` methods described below can each be inserted into the following app skeleton if you want to test them yourself.
  * PyQt5
  * PySide2


python ```
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import QPoint
FILL_COLOR = '#ff0000'
class Window(QtWidgets.QLabel):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    p = QtGui.QPixmap(dim, 500)
    p.fill(QtGui.QColor('#ffffff')) # Fill entire canvas.
    self.setPixmap(p)
    self.fill(0, 0)
  def fill(x, y):
    # ... see below ..

app = QtWidgets.QApplication(sys.argv)
w = Window()
w.show()
app.exec_()

```

python ```
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QPainter, QPen, QColor
from PySide2.QtCore import QPoint
FILL_COLOR = '#ff0000'
class Window(QtWidgets.QLabel):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    p = QtGui.QPixmap(dim, 500)
    p.fill(QtGui.QColor('#ffffff')) # Fill entire canvas.
    self.setPixmap(p)
    self.fill(0, 0)
  def fill(x, y):
    # ... see below ..

app = QtWidgets.QApplication(sys.argv)
w = Window()
w.show()
app.exec_()

```

## `QImage.pixel()`
To identify which pixels are filled with the correct colour we can use `QImage.pixel()`. This accepts an `x` and `y` coordinate and returns the colour at the given coordinates. There are two methods available — one to return the colour of the pixel as `QRgb` object, one as a `QColor`.
python ```
QImage.pixel(x, y)    # returns a QRgb object
QImage.pixelColor(x, y) # returns a QColor object

```

Below is an implementation of the fill algorithm described above using direct pixel access via `QImage.pixel`. We'll use this to generate some timings.
python ```
image = self.pixmap().toImage()
w, h = image.width(), image.height()
# Get our target color from origin.
target_color = image.pixel(x,y)
have_seen = set()
queue = [(x, y)]
def get_cardinal_points(have_seen, center_pos):
  points = []
  cx, cy = center_pos
  for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    xx, yy = cx + x, cy + y
    if (xx >= 0 and xx < w and
      yy >= 0 and yy < h and
      (xx, yy) not in have_seen):
      points.append((xx, yy))
      have_seen.add((xx, yy))
  return points
# Now perform the search and fill.
p = QPainter(self.pixmap())
p.setPen(QColor(FILL_COLOR))
while queue:
  x, y = queue.pop()
  if image.pixel(x, y) == target_color:
    p.drawPoint(QPoint(x, y))
    # Prepend to the queue
    queue[0:0] = get_cardinal_points(have_seen, (x, y))
    # or append,
    # queue.extend(get_cardinal_points(have_seen, (x, y))
self.update()

```

This code fragment will work as-is on a `QLabel` widget which is displaying a `QPixmap` image (returned by `self.pixmap()`). However you can modify it to work on any `QPixmap`.
First we get an image representation of the `QPixmap`, so we can perform the `.pixel()` lookup operation. Then we get the dimensions, to determine the limits of our search, and finally, the target colour — taken from the pixel where we start the fill.
python ```
image = self.pixmap().toImage()
w, h = image.width(), image.height()
# Get our target color from origin.
target_color = image.pixel(x,y)
have_seen = set()
queue = [(x, y)]

```

The `set()` named `have_seen` is used to track pixels that we've already visited, and therefore do not need to revisit. This is technically not _necessary_ since pixels we've visited will be recolored and no longer match the original point, but it's quicker.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt5](https://www.pythonguis.com/static/theme/images/products/pyside2-book.png)](https://www.pythonguis.com/pyside2-book/)
[Take a look ](https://www.pythonguis.com/pyside2-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/create-gui-applications-pyside/) and [Amazon Paperback](https://www.amazon.com/dp/B08R92BW7R/)
The `queue` holds a list of `(x, y)` tuples of all locations that we _still need to visit_. The `queue` is set to our initial fill position, and `have_seen` is reset to an empty set.
To determine what to put in the queue, we call the method `get_cardinal_points` which for a given position looks at all surrounding positions — if they haven't been looked at yet — and tests whether it is a _hit_ or a _miss_.
python ```
def get_cardinal_points(have_seen, center_pos):
  points = []
  cx, cy = center_pos
  for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    xx, yy = cx + x, cy + y
    if (xx >= 0 and xx < w and
      yy >= 0 and yy < h and
      (xx, yy) not in have_seen):
      points.append((xx, yy))
      have_seen.add((xx, yy))
  return points

```

If it's a hit, we return that pixel to look and fill later. The result of this method is added to the `queue` in the main loop of the search.
python ```
while queue:
  x, y = queue.pop()
  if image.pixel(x, y) == target_color:
    p.drawPoint(QPoint(x, y))
    # Prepend to the queue
    queue[0:0] = get_cardinal_points(have_seen, (x, y))

```

This loops over the current queue, which is constantly expanding. Each loop it removes the first element `x` and `y` positions, checking the pixel at that location. If it is a match, we draw our fill colour. Finally, we check all cardinal points of the current location, updating the `queue` and `have_seen` as appropriate.
Below is a table showing the time taken to fill an area of the given size (in pixels) using this algorithm.
x | y | Area | Time (s)  
---|---|---|---  
500 | 10 | 5000 | 0.0145067  
500 | 50 | 25000 | 0.0726196  
500 | 100 | 50000 | 0.1422842  
500 | 500 | 250000 | 0.7466553  
500 | 1000 | 500000 | 1.5315427  
500 | 5000 | 2500000 | 7.8900651  
As you can see, at smaller fill areas the speed is reasonable, later it gets quite slow. If you run the code, you'll see the following image only (the final 500x10 run).
![Flood fill result at 500x10 pixels](https://www.pythonguis.com/static/faq/implementing-qpainter-flood-fill-pyqt5pyside/window.png) _Flood fill result at 500x10 pixels_
You can opt to save the images on each iteration if you like, in order to check they are working.
python ```
self.pixmap().save(<filename>)

```

Filling an area of 500 x 100 pixels takes > 100 _ms_ while a 500 x 5000 pixel region takes almost 8 seconds. So don't use flood fills in parts of your application that are performance-dependent, such as when drawing custom widgets.
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Implementing QPainter flood fill in PyQt5/PySide** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/implementing-qpainter-flood-fill-pyqt5pyside/Python books) on the subject. 
**Implementing QPainter flood fill in PyQt5/PySide** was published in [faq](https://www.pythonguis.com/faq/) on April 14, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [python](https://www.pythonguis.com/topics/python/)
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
