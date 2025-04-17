# Content from: https://www.pythonguis.com/tutorials/pyside6-plotting-pyqtgraph/

[](https://www.pythonguis.com/tutorials/pyside6-plotting-pyqtgraph/#menu)
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
# Plotting With PyQtGraph and PySide6
Create custom plots in PySide6 with PyQtGraph
by [John Lim](https://www.pythonguis.com/authors/john-lim/) Last updated Mar 15 PySide6 [ Graphics and Plotting in PySide6 ](https://www.pythonguis.com/pyside6-tutorial/#pyside6-plotting)
#### [ PySide6 Tutorial ](https://www.pythonguis.com/pyside6-tutorial/) — [Graphics and Plotting in PySide6](https://www.pythonguis.com/pyside6-tutorial/#pyside6-plotting)
  * [Plotting With PyQtGraph and PySide6](https://www.pythonguis.com/tutorials/pyside6-plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PySide6](https://www.pythonguis.com/tutorials/pyside6-plotting-matplotlib/)


This tutorial is also available for [PyQt6](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/) , [PyQt5](https://www.pythonguis.com/tutorials/plotting-pyqtgraph/) and [PySide2](https://www.pythonguis.com/tutorials/pyside-plotting-pyqtgraph/)
One of the major strengths of Python is in exploratory data science and visualization, using tools such as Pandas, numpy, sklearn for data analysis and matplotlib plotting. Buiding GUI applications with PySide6 gives you access to all these Python tools directly from within your app, allowing you to build complex data-driven apps and interactive dashboards.
While it is possible to embed `matplotlib` plots in PySide the experience does not feel entirely _native_. For simple and highly interactive plots you may want to consider using PyQtGraph instead. PyQtGraph is built on top of Qt's native `QGraphicsScene` giving better drawing performance, particularly for live data, as well as providing interactivity and the ability to easily customize plots with Qt graphics widgets.
In this tutorial we'll walk through the first steps of creating a plot widget with PyQtGraph and then demonstrate plot customization using line colours, line type, axis labels, background colour and plotting multiple lines.
## Getting started
To be able to use PyQtGraph with PySide you first need to install the package to your Python environment. You can do this as normal using `pip`.
bash ```
pip install pyqtgraph

```

Once the installation is complete you should be able to import the module as normal.
## Creating a PyQtGraph widget
In PyQtGraph all plots are created using the `PlotWidget` widget. This widget provides a contained _canvas_ on which plots of any type can be added and configured. Under the hood, this plot widget uses Qt native `QGraphicsScene` meaning it fast and efficient yet simple to integrate with the rest of your app. You can create a `PlotWidget` as for any other widget.
The basic template app, with a single `PlotWidget` in a `QMainWindow` is shown below. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
In the following examples we'll create the PyQtGraph widget in code. Want to know how to embed PyQtGraph when using Qt Designer? See [Embedding custom widgets from Qt Designer](https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/)
python ```
from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import sys
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.graphWidget = pg.PlotWidget()
    self.setCentralWidget(self.graphWidget)
    hour = [1,2,3,4,5,6,7,8,9,10]
    temperature = [30,32,34,32,33,31,29,32,35,45]
    # plot data: x, y values
    self.graphWidget.plot(hour, temperature)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

```

In all our examples below we import PyQtGraph using `import pyqtgraph as pg`. This is a common convention in PyQtGraph examples to keep things tidy & reduce typing. You an import and use it as `import pyqtgraph` if you prefer.
![The custom PyQtGraph widget showing dummy data.](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/Image5_2JH5D3E.png) _The custom PyQtGraph widget showing dummy data._
The default plot style of PyQtGraph is quite bare — a black background with a thin (barely visible) white line. In the next section we'll look at what options we have available to us in PyQtGraph to improve the appearance and usability of our plots.
## Styling plots
PyQtGraph uses Qt's `QGraphicsScene` to render the graphs. This gives us access to all the standard Qt line and shape styling options for use in plots. However, PyQtGraph provides an API for using these to draw plots and manage the plot canvas.
Below we'll go through the most common styling features you'll need to create and customize your own plots.
### Background Colour
Beginning with the app skeleton above, we can change the background colour by calling `.setBackground` on our `PlotWidget` instance (in `self.graphWidget`). The code below will set the background to white, by passing in the string 'w'.
python ```
self.graphWidget.setBackground('w')

```

You can set (and update) the background colour of the plot at any time.
python ```
from PySide6.QtWidgets import QMainWindow, QApplication
import pyqtgraph as pg
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.graphWidget = pg.PlotWidget()
    self.setCentralWidget(self.graphWidget)
    hour = [1,2,3,4,5,6,7,8,9,10]
    temperature = [30,32,34,32,33,31,29,32,35,45]
    self.graphWidget.setBackground('w')
    self.graphWidget.plot(hour, temperature)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()

```

![Change PyQtGraph Plot Background to White](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/Image1_TJCnkSp.png) _Change PyQtGraph Plot Background to White_
There are a number of simple colours available using single letters, based on the standard colours used in `matplotlib`. They're pretty unsurprising -- r is red, b is blue -- except that 'k' is used for black. In addition to these single letter codes, you can also set more complex colours using hex notation eg. #672922 as a string.
python ```
self.graphWidget.setBackground('#bbccaa')     # hex

```

RGB and RGBA values can be passed in as a 3-tuple or 4-tuple respectively, using values 0-255.
python ```
self.graphWidget.setBackground((100,50,255))   # RGB each 0-255
self.graphWidget.setBackground((100,50,255,25))  # RGBA (A = alpha opacity)

```

Lastly, you can also specify colours using Qt's `QColor` type directly.
python ```
from PySIde2 import QtGui # Place this at the top of your file.
self.graphWidget.setBackground(QtGui.QColor(100,50,254,25))

```

This can be useful if you're using specific `QColor` objects elsewhere in your application, or to set your plot background to the default GUI background colour.
python ```
color = self.palette().color(QtGui.QPalette.Window) # Get the default window background,
self.graphWidget.setBackground(color)

```

### Line Colour, Width & Style
Lines in PyQtGraph are drawn using standard Qt `QPen` types. This gives you the same full control over line drawing as you would have in any other `QGraphicsScene` drawing. To use a pen to plot a line, you simply create a new `QPen` instance and pass it into the `plot` method.
Below we create a `QPen` object, passing in a 3-tuple of `int` values specifying an RGB value (of full red). We could also define this by passing 'r', or a `QColor` object. Then we pass this into `plot` with the _pen_ parameter.
python ```
pen = pg.mkPen(color=(255, 0, 0))
self.graphWidget.plot(hour, temperature, pen=pen)

```

The complete code is shown below.
python ```
from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.graphWidget = pg.PlotWidget()
    self.setCentralWidget(self.graphWidget)
    hour = [1,2,3,4,5,6,7,8,9,10]
    temperature = [30,32,34,32,33,31,29,32,35,45]
    self.graphWidget.setBackground('w')
    pen = pg.mkPen(color=(255, 0, 0))
    self.graphWidget.plot(hour, temperature, pen=pen)

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()

```

![Changing Line Colour](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/Changing_Line_Colour.png) _Changing Line Colour_
By changing the `QPen` object we can change the appearance of the line, including both line width in pixels and style (dashed, dotted, etc.) using standard Qt line styles. For example, the following example creates a 15px width dashed line in red.
python ```
pen = pg.mkPen(color=(255, 0, 0), width=15, style=QtCore.Qt.DashLine)

```

The result is shown below, giving a 15px dashed red line.
![Changing Line Width and Style](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/Changing_Line_Width_and_Style.png) _Changing Line Width and Style_
The standard Qt line styles can all be used, including `Qt.SolidLine`, `Qt.DashLine`, `Qt.DotLine`, `Qt.DashDotLine` and `Qt.DashDotDotLine`. Examples of each of these lines are shown in the image below, and you can read more in the [Qt Documentation](https://doc.qt.io/qt-5/qpen.html#pen-style).
![Qt Line Types](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/Qt_Line_Types.png) _Qt Line Types_
### Line Markers
For many plots it can be helpful to place markers in addition or instead of lines on the plot. To draw a marker on the plot, pass the symbol to use as a marker when calling `.plot` as shown below.
python ```
self.graphWidget.plot(hour, temperature, symbol='+')

```

In addition to `symbol` you can also pass in `symbolSize`, `symbolBrush` and `symbolPen` parameters. The value passed as `symbolBrush` can be any colour, or `QBrush` type, while `symbolPen` can be passed any colour or a `QPen` instance. The _pen_ is used to draw the outline of the shape, while _brush_ is used for the fill.
For example the below code will give a blue cross marker of size 30, on a thick red line.
python ```
pen = pg.mkPen(color=(255, 0, 0), width=15, style=QtCore.Qt.DashLine)
self.graphWidget.plot(hour, temperature, pen=pen, symbol='+', symbolSize=30, symbolBrush=('b'))

```

![Adding Symbols on Line](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/Adding_Symbols_on_Line.png) _Adding Symbols on Line_
In addition to the `+` plot marker, PyQtGraph supports the following standard markers shown in the table below. These can all be used in the same way.
If you have more complex requirements you can also pass in any `QPainterPath` object, allowing you to draw completely custom marker shapes.
## Plot Titles
Chart titles are important to provide context to what is shown on a given chart. In PyQtGraph you can add a main plot title using the `setTitle()` method on the `PlotWidget`, passing in your title string.
python ```
self.graphWidget.setTitle("Your Title Here")

```

You can apply text styles, including colours, font sizes and weights to your titles (and any other labels in PyQtGraph) by passing additional arguments. The available style arguments are shown below.
The code below sets the color to blue with a font size of 30px.
python ```
self.graphWidget.setTitle("Your Title Here", color="b", size="30pt")

```

You can also style your headers with HTML tag syntax if you prefer, although it's less readable.
python ```
self.graphWidget.setTitle("<span style=\"color:blue;font-size:30pt\">Your Title Here</span>")

```

![Adding Chart Title](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/Adding_Chart_Title.png) _Adding Chart Title_
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
## Axis Labels
Similar to titles, we can use the `setLabel()` method to create our axis titles. This requires two parameters, _position_ and _text_. The _position_ can be any one of `'left,'right','top','bottom'` which describe the position of the axis on which the text is placed. The 2nd parameter _text_ is the text you want to use for the label.
You can pass additional style parameters into the method. These differ slightly than for the title, in that they need to be valid CSS name-value pairs. For example, the size is now `font-size`. Because the name `font-size` has a hyphen in it, you cannot pass it directly as a parameter, but must use the `**dictionary` method.
python ```
styles = {'color':'r', 'font-size':'20px'}
self.graphWidget.setLabel('left', 'Temperature (°C)', **styles)
self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)

```

These also support HTML syntax for styling if you prefer.
python ```
self.graphWidget.setLabel('left', "<span style=\"color:red;font-size:20px\">Temperature (°C)</span>")
self.graphWidget.setLabel('bottom', "<span style=\"color:red;font-size:20px\">Hour (H)</span>")

```

![Add Axis Labels](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/Add_Axis_Labels.png) _Add Axis Labels_
## Legends
In addition to the axis and plot titles you will often want to show a legend identifying what a given line represents. This is particularly important when you start adding multiple lines to a plot. Adding a legend to a plot can be accomplished by calling `.addLegend` on the `PlotWidget`, however before this will work you need to provide a name for each line when calling `.plot()`.
The example below assigns a name "Sensor 1" to the line we are plotting with `.plot()`. This name will be used to identify the line in the legend.
python ```
self.graphWidget.plot(hour, temperature, name = "Sensor 1", pen = NewPen, symbol='+', symbolSize=30, symbolBrush=('b'))
self.graphWidget.addLegend()

```

![Add Legend](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/Add_Legend.png) _Add Legend_
The legend appears in the top left by default. If you would like to move it, you can easily drag and drop the legend elsewhere. You can also specify a default offset by passing a 2-tuple to the `offset` parameter when creating the legend.
## Background Grid
Adding a background grid can make your plots easier to read, particularly when trying to compare relative x & y values against each other. You can turn on a background grid for your plot by calling `.showGrid` on your `PlotWidget`. You can toggle x and y grids independently.
The following with create the grid for both the X and Y axis.
python ```
self.graphWidget.showGrid(x=True, y=True)

```

![Add Grid](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/Add_Grid.png) _Add Grid_
## Setting Axis Limits
Sometimes it can be useful to restrict the range of data which is visible on the plot, or to lock the axis to a consistent range regardless of the data input (e.g. a known min-max range). In PyQtGraph this can be done using the `.setXRange()` and `.setYRange()` methods. These force the plot to only show data within the specified ranges on each axis.
Below we set two ranges, one on each axis. The 1st argument is the minimum value and the 2nd is the maximum.
python ```
self.graphWidget.setXRange(5, 20, padding=0)
self.graphWidget.setYRange(30, 40, padding=0)

```

A optional padding argument causes the range to be set larger than specified by the specified fraction (this between 0.02 and 0.1 by default, depending on the size of the ViewBox). If you want to remove this padding entirely, pass 0.
python ```
self.graphWidget.setXRange(5, 20, padding=0)
self.graphWidget.setYRange(30, 40, padding=0)

```

The complete code so far is shown below:
python ```
from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
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

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()

```

![Set Axis Range](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/Set_Axis_Range.png) _Set Axis Range_
## Plotting multiple lines
It is common for plots to involve more than one line. In PyQtGraph this is as simple as calling `.plot()` multiple times on the same `PlotWidget`. In the following example we're going to plot two lines of similar data, using the same line styles, thicknesses etc. for each, but changing the line colour.
To simplify this we can create our own custom `plot` method on our `MainWindow`. This accepts `x` and `y` parameters to plot, the name of the line (for the legend) and a colour. We use the colour for both the line and marker colour.
python ```
  def plot(self, x, y, plotname, color):
    pen = pg.mkPen(color=color)
    self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))

```

To plot separate lines we'll create a new array called `temperature_2` and populate it with random numbers similar to `temperature` (now `temperature_1`). Plotting these alongside each other allows us to compare them together.
Now, you can call plot function twice and this will generate 2 lines on the plot.
python ```
self.plot(hour, temperature_1, "Sensor1", 'r')
self.plot(hour, temperature_2, "Sensor2", 'b')

```

python ```
from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.graphWidget = pg.PlotWidget()
    self.setCentralWidget(self.graphWidget)
    hour = [1,2,3,4,5,6,7,8,9,10]
    temperature_1 = [30,32,34,32,33,31,29,32,35,45]
    temperature_2 = [50,35,44,22,38,32,27,38,32,44]
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
    self.plot(hour, temperature_1, "Sensor1", 'r')
    self.plot(hour, temperature_2, "Sensor2", 'b')
  def plot(self, x, y, plotname, color):
    pen = pg.mkPen(color=color)
    self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))

app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()

```

![2 Line Graph](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/Screenshot_from_2019-10-11_22-52-29.png) _2 Line Graph_
Play around with this function, customising your markers, line widths, colours and other parameters.
## Clearing the plot
Finally, sometimes you might want to clear and refresh the plot periodically. You can easily do that by calling `.clear()`.
python ```
self.graphWidget.clear()

```

This will remove the lines from the plot but keep all other attributes the same.
## Updating the plot
While you _can_ simply clear the plot and redraw all your elements again, this means Qt has to destroy and recreate all your `QGraphicsScene` objects. For small or simple plots this is probably not noticeable, but if you want to create high-peformance streaming plots it is much better to update the data in place. PyQtGraph takes the new data and updates the plotted line to match without affecting any other elements in the plot.
To update a line we need a reference to the line object. This reference is returned when first creating the line using `.plot` and we can simply store this in a variable. Note that this is a reference to the _line_ not to the plot.
python ```
my_line_ref = graphWidget.plot(x, y)

```

Once we have the reference, updating the plot is simply a case of calling `.setData` on the reference to apply the new data. In the example below we've taken our simple plot demo and expanded it to take a reference to the line.
python ```
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
import pyqtgraph as pg
import sys
from random import randint
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.graphWidget = pg.PlotWidget()
    self.setCentralWidget(self.graphWidget)
    self.x = list(range(100)) # 100 time points
    self.y = [randint(0,100) for _ in range(100)] # 100 data points
    self.graphWidget.setBackground('w')
    pen = pg.mkPen(color=(255, 0, 0))
    self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())

```

We're going to update our data every 50ms, although PyQtGraph can plot data much more quickly than this it can get hard to watch! To do this we define a Qt timer, and set it to call a custom method `update_plot_data` where we'll change the data. We define this timer in the `__init__` block so it is automatically started. Add the following to the window class:
python ```
    # ... init continued ...
    self.timer = QtCore.QTimer()
    self.timer.setInterval(50)
    self.timer.timeout.connect(self.update_plot_data)
    self.timer.start()
  def update_plot_data(self):
    self.x = self.x[1:] # Remove the first y element.
    self.x.append(self.x[-1] + 1) # Add a new value 1 higher than the last.
    self.y = self.y[1:] # Remove the first
    self.y.append( randint(0,100)) # Add a new random value.
    self.data_line.setData(self.x, self.y) # Update the data.

```

If you run the app you will see a plot with random data scrolling rapidly to the left, with the X values also updating and scrolling in time, as if streaming data. You can replace the random data with your own real data, taken for example from a live sensor readout or API. PyQtGraph is performant enough to support multiple simultaneous plots using this method.
The complete code is shown below.
python ```
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
import pyqtgraph as pg
import sys
from random import randint
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.graphWidget = pg.PlotWidget()
    self.setCentralWidget(self.graphWidget)
    self.x = list(range(100)) # 100 time points
    self.y = [randint(0,100) for _ in range(100)] # 100 data points
    self.graphWidget.setBackground('w')
    pen = pg.mkPen(color=(255, 0, 0))
    self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)
    self.timer = QTimer()
    self.timer.setInterval(50)
    self.timer.timeout.connect(self.update_plot_data)
    self.timer.start()
  def update_plot_data(self):
    self.x = self.x[1:] # Remove the first y element.
    self.x.append(self.x[-1] + 1) # Add a new value 1 higher than the last.
    self.y = self.y[1:] # Remove the first
    self.y.append( randint(0,100)) # Add a new random value.
    self.data_line.setData(self.x, self.y) # Update the data.
app = QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()

```

## Conclusion
In this tutorial we've discovered how to draw simple plots with PyQtGraph and customize lines, markers and labels. For a complete overview of PyQtGraph methods and capabilities see the [PyQtGraph Documentation & API Reference](https://pyqtgraph.readthedocs.io/en/latest/). The [PyQtGraph repository on Github](https://github.com/pyqtgraph/pyqtgraph) also has complete set of more complex example plots in Plotting.py (shown below).
![PyQtGraph Repo Example \(Plotting.py\)](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/PyQtGraph_Repo_Example_Plotting.py.png) _PyQtGraph Repo Example (Plotting.py)_
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
Mark As Complete 
Continue with [ PySide6 Tutorial ](https://www.pythonguis.com/tutorials/pyside6-plotting-matplotlib/ "Continue to next part")
Return to [Create Desktop GUI Applications with PySide6 ](https://www.pythonguis.com/pyside6-tutorial/)
[![John Lim Ji Xiong](https://www.pythonguis.com/static/theme/images/authors/john-lim.jpg)](https://www.pythonguis.com/authors/john-lim/)
**Plotting With PyQtGraph and PySide6** was written by [John Lim](https://www.pythonguis.com/authors/john-lim/) . 
John is a developer from Kuala Lumpur, Malaysia who works as a Senior R&D Engineer. 
**Plotting With PyQtGraph and PySide6** was published in [tutorials](https://www.pythonguis.com/tutorials/) on July 01, 2022 (updated March 15, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[colour](https://www.pythonguis.com/topics/colour/) [qt](https://www.pythonguis.com/topics/qt/) [style](https://www.pythonguis.com/topics/style/) [line](https://www.pythonguis.com/topics/line/) [pyqtgraph](https://www.pythonguis.com/topics/pyqtgraph/) [marker](https://www.pythonguis.com/topics/marker/) [plot](https://www.pythonguis.com/topics/plot/) [pyside](https://www.pythonguis.com/topics/pyside/) [ data-science](https://www.pythonguis.com/topics/data-science/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [ pyside6-data-science](https://www.pythonguis.com/topics/pyside6-data-science/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
