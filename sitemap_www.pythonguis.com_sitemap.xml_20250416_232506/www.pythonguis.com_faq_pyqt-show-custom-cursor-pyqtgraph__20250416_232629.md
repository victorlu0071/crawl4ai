# Content from: https://www.pythonguis.com/faq/pyqt-show-custom-cursor-pyqtgraph/

[](https://www.pythonguis.com/faq/pyqt-show-custom-cursor-pyqtgraph/#menu)
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
# Q&A: How to show a custom cursor on a PyQtGraph plot?
Changing the OS cursor and implementing a custom crosshair
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ FAQ ](https://www.pythonguis.com/faq/)
When working with plots changing the cursor can help with pointing accuracy. For example, if you need to isolate particular points in a scatter plot a cross-hair will give you a more accurate view of where you are pointing than the standard arrow cursor.
## Changing the mouse cursor
Changing the mouse cursor in a PyQtGraph is fairly simple and uses Qt's built-in support for custom cursors over a widget. Since the PyQtGraph `PlotWidget` is a subclass of `QGraphicsWidget` (and therefore `QWidget`) you can use the standard methods.
python ```
  cursor = Qt.CrossCursor
  self.graphWidget.setCursor(cursor)

```

For the complete list of cursor types, [see the Qt documentation](https://doc.qt.io/qt-5/qt.html#CursorShape-enum). The example below shows this in action on a simple PyQtGraph plot.
python ```
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys # We need sys so that we can pass argv to QApplication
import os
class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.graphWidget = pg.PlotWidget()
    self.setCentralWidget(self.graphWidget)
    hour = [1,2,3,4,5,6,7,8,9,10]
    temperature = [30,32,34,32,33,31,29,32,35,45]
    #Add Background colour to white
    self.graphWidget.setBackground('w')
    # Add Title
    self.graphWidget.setTitle("Your Title Here", color="b", size="30pt")
    # Add Axis Labels
    styles = {"color": "#f00", "font-size": "20px"}
    self.graphWidget.setLabel("left", "Temperature (°C)", **styles)
    self.graphWidget.setLabel("bottom", "Hour (H)", **styles)
    #Add legend
    self.graphWidget.addLegend()
    #Add grid
    self.graphWidget.showGrid(x=True, y=True)
    #Set Range
    self.graphWidget.setXRange(0, 10, padding=0)
    self.graphWidget.setYRange(20, 55, padding=0)
    pen = pg.mkPen(color=(255, 0, 0))
    self.graphWidget.plot(hour, temperature, name="Sensor 1", pen=pen, symbol='+', symbolSize=30, symbolBrush=('b'))
    # Set the cursor for the plotwidget. The mouse cursor will change when over the plot.
    cursor = Qt.CrossCursor
    self.graphWidget.setCursor(cursor)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()

```

If you run this you'll see a cross-hair cursor appear when you hover your mouse over the plot.
![Mouse cursor as crosshair](https://www.pythonguis.com/static/faq/cursor-on-pyqtgraph/crosshair-cursor.png) _Crosshair cursor on plot_
## Drawing a custom cursor
If you want to show a completely custom cursor, for example an full-size crosshair over the plot, things are a little trickier. In this case you need to draw the cursor yourself by adding elements to the plot and then listening for mouse events and updating their position.
The code below is an updated version of the plot above, with two crosshair lines added using PyQtGraphs `InfiniteLine` objects. The lines are drawn in the `__init__` method, and then updated in the `mouseMoved` method.
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
You could also add any other _QGraphicsScene_ item here instead.
The important part is the `SignalProxy` which forwards mouse movements to our custom method `update_crosshair`. The `rateLimit` parameter sets the maximum number of signals per second which will be sent, to avoid overloading our handler/app with excessive events.
python ```
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys # We need sys so that we can pass argv to QApplication
import os

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.graphWidget = pg.PlotWidget()
    self.setCentralWidget(self.graphWidget)
    hour = [1,2,3,4,5,6,7,8,9,10]
    temperature = [30,32,34,32,33,31,29,32,35,45]
    #Add Background colour to white
    self.graphWidget.setBackground('w')
    # Add Title
    self.graphWidget.setTitle("Your Title Here", color="b", size="30pt")
    # Add Axis Labels
    styles = {"color": "#f00", "font-size": "20px"}
    self.graphWidget.setLabel("left", "Temperature (°C)", **styles)
    self.graphWidget.setLabel("bottom", "Hour (H)", **styles)
    #Add legend
    self.graphWidget.addLegend()
    #Add grid
    self.graphWidget.showGrid(x=True, y=True)
    #Set Range
    self.graphWidget.setXRange(0, 10, padding=0)
    self.graphWidget.setYRange(20, 55, padding=0)
    pen = pg.mkPen(color=(255, 0, 0))
    self.graphWidget.plot(hour, temperature, name="Sensor 1", pen=pen, symbol='+', symbolSize=30, symbolBrush=('b'))
    # Add crosshair lines.
    self.crosshair_v = pg.InfiniteLine(angle=90, movable=False)
    self.crosshair_h = pg.InfiniteLine(angle=0, movable=False)
    self.graphWidget.addItem(self.crosshair_v, ignoreBounds=True)
    self.graphWidget.addItem(self.crosshair_h, ignoreBounds=True)
    self.proxy = pg.SignalProxy(self.graphWidget.scene().sigMouseMoved, rateLimit=60, slot=self.update_crosshair)
  def update_crosshair(self, e):
    pos = e[0]
    if self.graphWidget.sceneBoundingRect().contains(pos):
      mousePoint = self.graphWidget.getPlotItem().vb.mapSceneToView(pos)
      self.crosshair_v.setPos(mousePoint.x())
      self.crosshair_h.setPos(mousePoint.y())

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec_()


```

If you run this example, in addition to the mouse cursor you'll also see a faint yellow line overlaying the plot.
![Drawing the custom cursor lines](https://www.pythonguis.com/static/faq/cursor-on-pyqtgraph/custom-cursor-with-mouse.png) _The custom cursor with default mouse cursor hidden_
To hide the default mouse cursor over the plot set the curser type to `Qt.BlankCursor`. For example.
python ```
class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # ... rest of __init__ as before
    # Hide the cursor over the plot.
    cursor = Qt.BlankCursor
    self.graphWidget.setCursor(cursor)

```

This will give the following result when hovering over the plot.
![Drawing the custom cursor lines](https://www.pythonguis.com/static/faq/cursor-on-pyqtgraph/custom-cursor.png) _The custom cursor with default mouse cursor hidden_
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Q &A: How to show a custom cursor on a PyQtGraph plot?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyqt-show-custom-cursor-pyqtgraph/Python books) on the subject. 
**Q &A: How to show a custom cursor on a PyQtGraph plot?** was published in [faq](https://www.pythonguis.com/faq/) on August 31, 2021 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[pyqtgraph](https://www.pythonguis.com/topics/pyqtgraph/) [cursor](https://www.pythonguis.com/topics/cursor/) [mouseevent](https://www.pythonguis.com/topics/mouseevent/) [mousemoved](https://www.pythonguis.com/topics/mousemoved/) [ data-science](https://www.pythonguis.com/topics/data-science/)
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
