# Content from: https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/

[](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/#menu)
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
# Plotting With PyQtGraph and PyQt6
Create Custom Plots in PyQt6 With PyQtGraph
by [John Lim](https://www.pythonguis.com/authors/john-lim/) Last updated Mar 15 PyQt6 [ Graphics and Plotting in PyQt6 ](https://www.pythonguis.com/pyqt6-tutorial/#pyqt6-graphics-plotting)
#### [ PyQt6 Tutorial ](https://www.pythonguis.com/pyqt6-tutorial/) — [Graphics and Plotting in PyQt6](https://www.pythonguis.com/pyqt6-tutorial/#pyqt6-graphics-plotting)
  * [Plotting With PyQtGraph and PyQt6](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PyQt6](https://www.pythonguis.com/tutorials/pyqt6-plotting-matplotlib/)


This tutorial is also available for [PyQt5](https://www.pythonguis.com/tutorials/plotting-pyqtgraph/) , [PySide6](https://www.pythonguis.com/tutorials/pyside6-plotting-pyqtgraph/) and [PySide2](https://www.pythonguis.com/tutorials/pyside-plotting-pyqtgraph/)
One of the major fields where Python shines is in data science. For data exploration and cleaning, Python has many powerful tools, such as [pandas](https://pandas.pydata.org/) and [polar](https://pypi.org/project/polar/). For visualization, Python has Matplotlib.
When you're building GUI applications with PyQt, you can have access to all those tools directly from within your app. While it is possible to embed `matplotlib` plots in PyQt, the experience doesn't feel entirely _native_. So, for highly integrated plots, you may want to consider using the [PyQtGraph](https://www.pyqtgraph.org/) library instead.
PyQtGraph is built on top of Qt's native `QGraphicsScene`, so it gives better drawing performance, particularly for live data. It also provides interactivity and the ability to customize plots according to your needs.
In this tutorial, you'll learn the basics of creating plots with PyQtGraph. You'll also explore the different plot customization options, including background color, line colors, line type, axis labels, and more.
Table of Contents
  * [Installing PyQtGraph](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/#installing-pyqtgraph)
  * [Creating a PlotWidget Instance](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/#creating-a-plotwidget-instance)
  * [Customizing PyQtGraph Plots](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/#customizing-pyqtgraph-plots)
    * [Background Color](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/#background-color)
    * [Line Color, Width, and Style](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/#line-color-width-and-style)
    * [Line Markers](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/#line-markers)
    * [Plot Titles](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/#plot-titles)
    * [Axis Labels](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/#axis-labels)
    * [Plot Legends](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/#plot-legends)
    * [Background Grid](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/#background-grid)
    * [Axis Range](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/#axis-range)
  * [Multiple Plot Lines](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/#multiple-plot-lines)
  * [Creating Dynamic Plots](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/#creating-dynamic-plots)
  * [Conclusion](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/#conclusion)


## Installing PyQtGraph
To use PyQtGraph with PyQt6, you first need to install the library in your Python environment. You can do this using `pip` as follows:
sh ```
$ python -m pip install pyqtgraph

```

Once the installation is complete, you will be able to import the module into your Python code. So, now you are ready to start creating plots.
## Creating a `PlotWidget` Instance
In PyQtGraph, all plots use the [`PlotWidget`](https://pyqtgraph.readthedocs.io/en/latest/api_reference/widgets/plotwidget.html) class. This widget provides a _canvas_ on which we can add and configure many types of plots. Under the hood, `PlotWidget` uses Qt's `QGraphicsScene` class, meaning that it's fast, efficient, and well-integrated with the rest of your app.
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
The code below shows a basic GUI app with a single `PlotWidget` in a `QMainWindow`:
python ```
import pyqtgraph as pg
from PyQt6 import QtWidgets
class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    # Temperature vs time plot
    self.plot_graph = pg.PlotWidget()
    self.setCentralWidget(self.plot_graph)
    minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 30]
    self.plot_graph.plot(minutes, temperature)
app = QtWidgets.QApplication([])
main = MainWindow()
main.show()
app.exec()

```

In this short example, you create a PyQt app with a `PlotWidget` as its central widget. Then you create two lists of sample data for time and temperature. The final step to create the plot is to call the `plot()` methods with the data you want to visualize.
The first argument to `plot()` will be your `x` coordinate, while the second argument will be the `y` coordinate.
In all the examples in this tutorial, we import PyQtGraph using `import pyqtgraph as pg`. This is a common practice in PyQtGraph examples to keep things tidy and reduce typing.
If you run the above application, then you'll get the following window on your screen:
![Basic PyQtGraph plot: Temperature vs time](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/basic-pyqtgraph-plot.png) _Basic PyQtGraph plot: Temperature vs time._
PyQtGraph's default plot style is quite basic — a black background with a thin (barely visible) white line. Fortunately, the library provides several options that will allow us to deeply customize our plots.
In the examples in this tutorial, we'll create the PyQtGraph widget in code. To learn how to embed PyQtGraph plots when using Qt Designer, check out [Embedding custom widgets from Qt Designer](https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/).
In the following section, we'll learn about the options we have available in PyQtGraph to improve the appearance and usability of our plots.
## Customizing PyQtGraph Plots
Because PyQtGraph uses Qt's `QGraphicsScene` to render the graphs, we have access to all the standard Qt line and shape styling options for use in plots. PyQtGraph provides an [API](https://en.wikipedia.org/wiki/API) for using these options to draw plots and manage the plot canvas.
Below, we'll explore the most common styling features that you'll need to create and customize your own plots with PyQtGraph.
### Background Color
Beginning with the app skeleton above, we can change the background color by calling `setBackground()` on our `PlotWidget` instance, `self.graphWidget`. The code below sets the background to white by passing in the string `"w"`:
python ```
from PyQt6 import QtWidgets
import pyqtgraph as pg
class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    # Temperature vs time plot
    self.plot_graph = pg.PlotWidget()
    self.setCentralWidget(self.plot_graph)
    self.plot_graph.setBackground("w")
    minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 30]
    self.plot_graph.plot(minutes, temperature)
app = QtWidgets.QApplication([])
main = MainWindow()
main.show()
app.exec()

```

Calling `setBackground()` with `"w"` as an argument changes the background of your plot to white, as you can see in the following window:
![PyQtGraph plot with a white background](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/pyqtgraph-plot-white-background.png) _PyQtGraph plot with a white background._
There are a number of colors available using single letters, as we did in the example above. They're based on the standard colors used in Matplotlib. Here are the most common codes:
Letter Code | Color  
---|---  
`"b"` | Blue  
`"c"` | Cian  
`"d"` | Grey  
`"g"` | Green  
`"k"` | Black  
`"m"` | Magenta  
`"r"` | Red  
`"w"` | White  
`"y"` | Yellow  
In addition to these single-letter codes, we can create custom colors using the [hexadecimal notation](https://en.wikipedia.org/wiki/Web_colors#Hex_triplet) as a string:
python ```
self.plot_graph.setBackground("#bbccaa") # Hex

```

We can also use [RGB](https://en.wikipedia.org/wiki/RGB_color_model) and [RGBA](https://en.wikipedia.org/wiki/RGBA_color_model) values passed in as 3-value and 4-value tuples, respectively. We must use values in the range from 0 to 255:
python ```
self.plot_graph.setBackground((100, 50, 255)) # RGB each 0-255
self.plot_graph.setBackground((100, 50, 255, 25)) # RGBA (A = alpha opacity)

```

The first call to `setBackground()` takes a tuple representing an RGB color, while the second call takes a tuple representing an RGBA color.
We can also specify colors using Qt's `QColor` class if we prefer it:
python ```
from PyQt6 import QtGui
# ...
self.plot_graph.setBackground(QtGui.QColor(100, 50, 254, 25))

```

Using `QColor` can be useful when you're using specific `QColor` objects elsewhere in your application and want to reuse them in your plots. For example, say that your app has a custom window background color, and you want to use it in the plots as well. Then you can do something like the following:
python ```
color = self.palette().color(QtGui.QPalette.Window)
# ...
self.plot_graph.setBackground(color)

```

In the first line, you get the GUI's background color, while in the second line, you use that color for your plots.
### Line Color, Width, and Style
Plot lines in PyQtGraph are drawn using the Qt `QPen` class. This gives us full control over line drawing, as we would have in any other `QGraphicsScene` drawing. To use a custom pen, you need to create a new `QPen` instance and pass it into the `plot()` method.
In the app below, we use a custom `QPen` object to change the line color to red:
python ```
from PyQt6 import QtWidgets
import pyqtgraph as pg
class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    # Temperature vs time plot
    self.plot_graph = pg.PlotWidget()
    self.setCentralWidget(self.plot_graph)
    self.plot_graph.setBackground("w")
    pen = pg.mkPen(color=(255, 0, 0))
    time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
    self.plot_graph.plot(time, temperature, pen=pen)
app = QtWidgets.QApplication([])
main = MainWindow()
main.show()
app.exec()

```

Here, we create a `QPen` object, passing in a 3-value tuple that defines an RGB red color. We could also define this color with the `"r"` code or with a `QColor` object. Then, we pass the pen to `plot()` with the `pen` argument.
![PyQtGraph plot with a red plot line](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/pyqtgraph-plot-red-plot-line.png) _PyQtGraph plot with a red plot line._
By tweaking the `QPen` object, we can change the appearance of the line. For example, you can change the line width in pixels and the style (dashed, dotted, etc.), using Qt's line styles.
Update the following lines of code in your app to create a red, dashed line with 5 pixels of width:
python ```
from PyQt6 import QtCore, QtWidgets
# ...
pen = pg.mkPen(color=(255, 0, 0), width=5, style=QtCore.Qt.DashLine)

```

The result of this code is shown below, giving a 5-pixel, dashed, red line:
![PyQtGraph plot with a red, dashed, and 5-pixel line](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/pyqtgraph-plot-red-dashed-plot-line.png) _PyQtGraph plot with a red, dashed, and 5-pixel line_
You can use all other Qt's line styles, including `Qt.SolidLine`, `Qt.DotLine`, `Qt.DashDotLine`, and `Qt.DashDotDotLine`. Examples of each of these lines are shown in the image below:
![Qt Line Types](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/Qt_Line_Types.png) _Qt's line styles._
To learn more about Qt's line styles, check the [documentation](https://doc.qt.io/qt-5/qpen.html#pen-style) about pen styles. There, you'll all you need to deeply customize the lines in your PyQtGraph plots.
### Line Markers
For many plots, it can be helpful to use point markers in addition or instead of lines on the plot. To draw a marker on your plot, pass the symbol you want to use as a marker when calling `plot()`. The following example uses the plus sign as a marker:
python ```
self.plot_graph.plot(hour, temperature, symbol="+")

```

In this line of code, you pass a plus sign to the `symbol` argument. This tells PyQtGraph to use that symbol as a marker for the points in your plot.
If you use a custom `symbol`, then you can also use the `symbolSize`, `symbolBrush`, and `symbolPen` arguments to further customize the marker.
The value passed as `symbolBrush` can be any color, or `QBrush` instance, while `symbolPen` can be any color or a `QPen` instance. The pen is used to draw the shape, while the brush is used for the fill.
Go ahead and update your app's code to use a blue marker of size 15, on a red line:
python ```
pen = pg.mkPen(color=(255, 0, 0))
self.plot_graph.plot(
  time,
  temperature,
  pen=pen,
  symbol="+",
  symbolSize=20,
  symbolBrush="b",
)

```

In this code, you pass a plus sign to the `symbol` argument. You also customize the marker size and color. The resulting plot looks something like this:
![PyQtGraph plot with a plus sign as a point marker](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/pyqtgraph-plot-with-point-marker.png) _PyQtGraph plot with a plus sign as a point marker._
In addition to the `+` plot marker, PyQtGraph supports the markers shown in the table below:
Character | Marker Shape  
---|---  
`"o"` | Circle  
`"s"` | Square  
`"t"` | Triangle  
`"d"` | Diamond  
`"+"` | Plus  
`"t1"` | Triangle pointing upwards  
`"t2"` | Triangle pointing right side  
`"t3"` | Triangle pointing left side  
`"p"` | Pentagon  
`"h"` | Hexagon  
`"star"` | Star  
`"x"` | Cross  
`"arrow_up"` | Arrow Up  
`"arrow_right"` | Arrow Right  
`"arrow_down"` | Arrow Down  
`"arrow_left"` | Arrow Left  
`"crosshair"` | Crosshair  
You can use any of these symbols as markers for your data points. If you have more specific marker requirements, then you can also use a `QPainterPath` object, which allows you to draw completely custom marker shapes.
### Plot Titles
Plot titles are important to provide context around what is shown on a given chart. In PyQtGraph, you can add a main plot title using the `setTitle()` method on the `PlotWidget` object. Your title can be a regular Python string: 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
python ```
self.plot_graph.setTitle("Temperature vs Time")

```

You can style your titles and change their font color and size by passing additional arguments to `setTitle()`. The code below sets the color to blue and the font size to 20 points:
python ```
self.plot_graph.setTitle("Temperature vs Time", color="b", size="20pt")

```

In this line of code, you set the title's font color to blue and the size to 20 points using the `color` and `size` arguments of `setTitle()`.
You could've even used CSS style and basic HTML tag syntax if you prefer, although it's less readable:
python ```
self.plot_graph.setTitle(
  '<span style="color: blue; font-size: 20pt">Temperature vs Time</span>'
)

```

In this case, you use a `span` HTML tag to wrap the title and apply some CSS styles on to of it. The final result is the same as suing the `color` and `size` arguments. Your plot will look like this:
![PyQtGraph plot with title](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/pyqtgraph-plot-with-title.png) _PyQtGraph plot with title._
Your plot looks way better now. You can continue customizing it by adding informative lables to both axis.
### Axis Labels
When it comes to axis labels, we can use the `setLabel()` method to create them. This method requires two arguments, `position` and `text`.
python ```
self.plot_graph.setLabel("left", "Temperature (°C)")
self.plot_graph.setLabel("bottom", "Time (min)")

```

The `position` argument can be any one of `"left"`, `"right"`, `"top"`, or `"bottom"`. They define the position of the axis on which the text is placed. The second argument, `text` is the text you want to use for the label.
You can pass an optional `style` argument into the `setLabel()` method. In this case, you need to use valid CSS name-value pairs. To provide these CSS pairs, you can use a dictionary:
python ```
styles = {"color": "red", "font-size": "18px"}
self.plot_graph.setLabel("left", "Temperature (°C)", **styles)
self.plot_graph.setLabel("bottom", "Time (min)", **styles)

```

Here, you first create a dictionary containing CSS pairs. Then you pass this dictionary as an argument to the `setLabel()` method. Note that you need to use the dictionary unpacking operator to unpack the styles in the method call.
Again, you can use basic HTML syntax and CSS for the labels if you prefer:
python ```
self.plot_graph.setLabel(
  "left",
  '<span style="color: red; font-size: 18px">Temperature (°C)</span>'
)
self.plot_graph.setLabel(
  "bottom",
  '<span style="color: red; font-size: 18px">Time (min)</span>'
)

```

This time, you've passed the styles in a `span` HTML tag with appropriate CSS styles. In either case, your plot will look something like this:
![PyQtGraph plot with axis labels](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/pyqtgraph-plot-with-axis-labels.png) _PyQtGraph plot with axis labels._
Having axis labels highly improves the readability of your plots as you can see in the above example. So, it's a good practice that you should keep in mind when creating your plots.
### Plot Legends
In addition to the axis labels and the plot title, you will often want to show a legend identifying what a given line represents. This feature is particularly important when you start adding multiple lines to a plot.
You can add a legend to a plot by calling the `addLegend()` method on the `PlotWidget` object. However, for this method to work, you need to provide a name for each line when calling `plot()`.
The example below assigns the name "Temperature Sensor" to the `plot()` method. This name will be used to identify the line in the legend:
python ```
self.plot_graph.addLegend()
# ...
self.plot_graph.plot(
  time,
  temperature,
  name="Temperature Sensor",
  pen=pen,
  symbol="+",
  symbolSize=15,
  symbolBrush="b",
)

```

Note that you must call `addLegend()` before you call `plot()` for the legend to show up. Otherwise, the plot won't show the legend at all. Now your plot will look like the following:
![PyQtGraph plot with legend](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/pyqtgraph-plot-with-legend.png) _PyQtGraph plot with legend._
The legend appears in the top left by default. If you would like to move it, you can drag and drop the legend elsewhere. You can also specify a default offset by passing a 2-value tuple to the `offset` parameter when calling the `addLegend()` method. This will allow you to specify a custom position for the legend.
### Background Grid
Adding a background grid can make your plots easier to read, particularly when you're trying to compare relative values against each other. You can turn on the background grid for your plot by calling the `showGrid()` method on your `PlotWidget` instance. The method takes two Boolean arguments, `x` and `y`:
python ```
self.plot_graph.showGrid(x=True, y=True)

```

In this call to the `showGrid()` method, you enable the grid lines in both dimensions `x` and `y`. Here's how the plot looks now:
![PyQtGraph plot with grid](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/pyqtgraph-plot-with-grid.png) _PyQtGraph plot with grid._
You can toggle the `x` and `y` arguments independently, according to the dimension on which you want to enable the grid lines.
### Axis Range
Sometimes, it can be useful to predefine the range of values that is visible on the plot or to lock the axis to a consistent range regardless of the data input. In PyQtGraph, you can do this using the `setXRange()` and `setYRange()` methods. They force the plot to only show data within the specified ranges.
Below, we set two ranges, one on each axis. The first argument is the minimum value, and the second is the maximum:
python ```
self.plot_graph.setXRange(1, 10)
self.plot_graph.setYRange(20, 40)

```

The first line of code sets the x-axis to show values between 1 and 10. The second line sets the y-axis to display values between 20 and 40. Here's how this changes the plot:
![PyQtGraph plot with axis ranges](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/pyqtgraph-plot-with-axis-ranges.png) _PyQtGraph plot with axis ranges_
Now your plot looks more consistent. The axis show fix scales that are specifically set for the possible range of input data.
## Multiple Plot Lines
It is common to have plots that involve more than one dependent variable. In PyQtGraph, you can plot multiple variables in a single chart by calling `.plot()` multiple times on the same `PlotWidget` instance.
In the following example, we plot temperatures values from two different sensors. We use the same line style but change the line color. To avoid code repetition, we define a new `plot_line()` method on our window:
python ```
from PyQt6 import QtWidgets
import pyqtgraph as pg
class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    # Temperature vs time plot
    self.plot_graph = pg.PlotWidget()
    self.setCentralWidget(self.plot_graph)
    self.plot_graph.setBackground("w")
    self.plot_graph.setTitle("Temperature vs Time", color="b", size="20pt")
    styles = {"color": "red", "font-size": "18px"}
    self.plot_graph.setLabel("left", "Temperature (°C)", **styles)
    self.plot_graph.setLabel("bottom", "Time (min)", **styles)
    self.plot_graph.addLegend()
    self.plot_graph.showGrid(x=True, y=True)
    self.plot_graph.setXRange(1, 10)
    self.plot_graph.setYRange(20, 40)
    minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 30]
    temperature_2 = [32, 35, 40, 22, 38, 32, 27, 38, 32, 38]
    pen = pg.mkPen(color=(255, 0, 0))
    self.plot_line("Temperature Sensor 1", minutes, temperature_1, pen, "b")
    pen = pg.mkPen(color=(0, 0, 255))
    self.plot_line("Temperature Sensor 2", minutes, temperature_2, pen, "r")
  def plot_line(self, name, minutes, temperature, pen, brush):
    self.plot_graph.plot(
      minutes,
      temperature,
      name=name,
      pen=pen,
      symbol="+",
      symbolSize=15,
      symbolBrush=brush,
    )
app = QtWidgets.QApplication([])
main = MainWindow()
main.show()
app.exec()

```

The custom `plot_line()` method on the main window does the hard work. It accepts a `name` to set the line name for the plot legend. Then it takes the `time` and `temperature` arguments. The `pen` and `brush` arguments allow you to tweak other features of the lines.
To plot separate temperature values, we'll create a new list called `temperature_2` and populate it with random numbers similar to our old `temperature`, which now is `temperature_1`. Here's the plot looks now:
![PyQtGrap plot with two lines](https://www.pythonguis.com/static/tutorials/qt/plotting-pyqtgraph/pyqtgraph-plot-with-multiple-lines.png) _PyQtGrap plot with two lines._
You can play around with the `plot_line()` method, customizing the markers, line widths, colors, and other parameters.
## Creating Dynamic Plots
You can also create dynamic plots with PyQtGraph. The `PlotWidget` can take new data and update the plot in real time without affecting other elements. To update a plot dynamically, we need a reference to the line object that the `plot()` method returns.
Once we have the reference to the plot line, we can call the `setData()` method on the line object to apply the new data. In the example below, we've adapted our temperature vs time plot to accept new temperature measures every minute. Note that we've set the timer to 300 milliseconds so that we don't have to wait an entire minute to see the updates:
python ```
from random import randint
from PyQt6 import QtCore, QtWidgets
import pyqtgraph as pg
class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    # Temperature vs time dynamic plot
    self.plot_graph = pg.PlotWidget()
    self.setCentralWidget(self.plot_graph)
    self.plot_graph.setBackground("w")
    pen = pg.mkPen(color=(255, 0, 0))
    self.plot_graph.setTitle("Temperature vs Time", color="b", size="20pt")
    styles = {"color": "red", "font-size": "18px"}
    self.plot_graph.setLabel("left", "Temperature (°C)", **styles)
    self.plot_graph.setLabel("bottom", "Time (min)", **styles)
    self.plot_graph.addLegend()
    self.plot_graph.showGrid(x=True, y=True)
    self.plot_graph.setYRange(20, 40)
    self.time = list(range(10))
    self.temperature = [randint(20, 40) for _ in range(10)]
    # Get a line reference
    self.line = self.plot_graph.plot(
      self.time,
      self.temperature,
      name="Temperature Sensor",
      pen=pen,
      symbol="+",
      symbolSize=15,
      symbolBrush="b",
    )
    # Add a timer to simulate new temperature measurements
    self.timer = QtCore.QTimer()
    self.timer.setInterval(300)
    self.timer.timeout.connect(self.update_plot)
    self.timer.start()
  def update_plot(self):
    self.time = self.time[1:]
    self.time.append(self.time[-1] + 1)
    self.temperature = self.temperature[1:]
    self.temperature.append(randint(20, 40))
    self.line.setData(self.time, self.temperature)
app = QtWidgets.QApplication([])
main = MainWindow()
main.show()
app.exec()

```

The first step to creating a dynamic plot is to get a reference to the plot line. In this example, we've used a `QTimer` object to set the measuring interval. We've connected the `update_plot()` method with the timer's `timeout` signal.
The`update_plot()` method does the work of updating the data in every interval. If you run the app, then you will see a plot with random data scrolling to the left:
The time scale in the x-axis changes as the stream of data provides new values. You can replace the random data with your own real data. You can take the data from a live sensor readout, API, or from any other stream of data. PyQtGraph is performant enough to support multiple simultaneous dynamic plots using this technique.
## Conclusion
In this tutorial, you've learned how to draw basic plots with PyQtGraph and customize plot components, such as lines, markers, titles, axis labels, and more. For a complete overview of PyQtGraph methods and capabilities, see the PyQtGraph [documentation](https://pyqtgraph.readthedocs.io/en/latest/). The PyQtGraph [repository on Github](https://github.com/pyqtgraph/pyqtgraph) also has a complete set of plot [examples](https://github.com/pyqtgraph/pyqtgraph/tree/master/pyqtgraph/examples). 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
Continue with [ PyQt6 Tutorial ](https://www.pythonguis.com/tutorials/pyqt6-plotting-matplotlib/ "Continue to next part")
Return to [Create Desktop GUI Applications with PyQt6 ](https://www.pythonguis.com/pyqt6-tutorial/)
[![John Lim Ji Xiong](https://www.pythonguis.com/static/theme/images/authors/john-lim.jpg)](https://www.pythonguis.com/authors/john-lim/)
**Plotting With PyQtGraph and PyQt6** was written by [John Lim](https://www.pythonguis.com/authors/john-lim/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
John is a developer from Kuala Lumpur, Malaysia who works as a Senior R&D Engineer. 
**Plotting With PyQtGraph and PyQt6** was published in [tutorials](https://www.pythonguis.com/tutorials/) on February 19, 2024 (updated March 15, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [pyqtgraph](https://www.pythonguis.com/topics/pyqtgraph/) [plot](https://www.pythonguis.com/topics/plot/) [ data-science](https://www.pythonguis.com/topics/data-science/) [ pyqt6-data-science](https://www.pythonguis.com/topics/pyqt6-data-science/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
