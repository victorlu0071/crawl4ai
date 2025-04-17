# Content from: https://www.pythonguis.com/tutorials/pyside6-embed-pyqtgraph-custom-widgets/

[](https://www.pythonguis.com/tutorials/pyside6-embed-pyqtgraph-custom-widgets/#menu)
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
# Embedding Custom Widgets from Qt Designer in PySide6
Learn how to use custom widgets in your PySide6 applications when designing with Qt Designer
by [John Lim](https://www.pythonguis.com/authors/john-lim/) Last updated Mar 19 PySide6 [ Tutorials ](https://www.pythonguis.com/tutorials/)
This tutorial is also available for [PyQt6](https://www.pythonguis.com/tutorials/pyqt6-embed-pyqtgraph-custom-widgets-qt-app/) , [PySide2](https://www.pythonguis.com/tutorials/pyside-embed-pyqtgraph-custom-widgets/) and [PyQt5](https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/)
Qt Designer is a great tool for designing PySide6 GUIs, allowing you to use the entire range of Qt widgets and layouts to construct your apps. As your applications get more complex, however, you may find yourself creating custom widgets or using PySide6 libraries such as _PyQtGraph_ , whose widgets are not available within Designer.
Helpfully, Qt Designer supports a mechanism for using _placeholder_ widgets to represent your custom or external widgets in your design. This tutorial will walk you through the process of using placeholders to include a _PyQtGraph_ plot in your app from within Qt Designer.
Table of Contents
  * [Promoting Widgets](https://www.pythonguis.com/tutorials/pyside6-embed-pyqtgraph-custom-widgets/#promoting-widgets)
  * [PyQtGraph](https://www.pythonguis.com/tutorials/pyside6-embed-pyqtgraph-custom-widgets/#pyqtgraph)
  * [Qt Designer](https://www.pythonguis.com/tutorials/pyside6-embed-pyqtgraph-custom-widgets/#qt-designer)
  * [Loading the .ui File](https://www.pythonguis.com/tutorials/pyside6-embed-pyqtgraph-custom-widgets/#loading-the-ui-file)


## Promoting Widgets
The principle of using placeholders in Qt Designer is quite straightforward:
  1. Create a UI as usual in Qt Designer.
  2. Add a _placeholder_ widget to represent the custom widget you're adding.
  3. Tell Qt to replace your placeholder with your actual widget when building the UI.


In Qt, this final step is referred to as _promoting_ (as in _promoting_ a base class).
If the custom widget you are adding is a subclass of an existing Qt widget, you may want to use the base class as your placeholder to promote from. For example, if you have a custom `MyAwesomeButton` button widget subclassed from `QPushButton`, use `QPushButton` as the placeholder and promote it to `MyAwesomeButton`. This gives you access to the base class properties, events, and actions from within Qt Designer.
If you don't have an obvious base class to use, then you can use `QWidget`, the common base class of all Qt widgets.
## PyQtGraph
Data science is one of the most popular use cases of Python, and building dashboards and analysis tools is a common use case of PySide. For all of these, being able to add plots to your UI is very useful — and being able to do this from Qt Designer is even more so. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
There are a number of plotting libraries available in Python, with _matplotlib_ being the most popular and offering some basic support for PySide. [PyQtGraph](http://www.pyqtgraph.org/) is a popular alternative that uses Qt's native `QGraphicsScene` to provide fast zooming, scaling, and drag-drop behavior that feels like a natural part of your application.
Whether you're using _PyQtGraph_ or _maplotlib_ for your plotting needs, the plot canvas widgets are not available from within Qt Designer. In this tutorial, we'll go through the process of using these custom widgets in your apps.
If you don't have PyQtGraph installed already, you can install it using the following command:
bash ```
$ python -m pip install pyqtgraph

```

The instructions below aren't specific to PyQtGraph, and you can use a similar command to add [Matplotlib](https://www.pythonguis.com/tutorials/pyqt6-plotting-matplotlib/) or any other custom widgets to your app.
## Qt Designer
We will be using Qt Designer to create a simple UI design and add a placeholder for our PyQtGraph widget. First, open Qt Designer and create a new `QMainWindow` as usual.
![Qt Creator — Select MainWindow for widget type](https://www.pythonguis.com/static/tutorials/qt/embed-pyqtgraph-custom-widgets-qt-app/Screenshot_2019-05-30_at_23.01.09.png) _Qt Creator — Select MainWindow for widget type_
We next need to add the _placeholder_ widget. As there is no suitable baseclass for the _PyQtGraph_ plot widget, we'll use the basic `QWidget` as our placeholder. Select the _Widget_ from the left sidebar and place it in the center of your window.
Give the widget a name, `graphWidget` will do. This is just a tag to reference the element in your code.
![Add a widget to the window. Name the widget as "graphWidget"](https://www.pythonguis.com/static/tutorials/qt/embed-pyqtgraph-custom-widgets-qt-app/Image1_K4dflzn.png) _Add a widget to the window. Name the widget as "graphWidget"_
Right-click the widget and select the _Promote to_ option from the widget's context menu.
Promoting a `QWidget` indicates that it should be replaced with the specified subclass, in our case, the PyQtGraph plot widget.
A promoted widget can be reverted back to its base class by right-clicking and choosing _Demote to_ from the widget's context menu.
![Right click to show the promotion menu](https://www.pythonguis.com/static/tutorials/qt/embed-pyqtgraph-custom-widgets-qt-app/Image2_EdOPTIx.png) _Right click to show the promotion menu_
You will be presented with a dialog to specify the custom widget class the placeholder widget will become.
The _header file_ is the name of the Python module used to import the class, which is `pyqtgraph`. Specify `PlotWidget` as the class name of the widget to replace it with.
![Promote the widget by specifying the class name as PlotWidget and the header file as pyqtgraph.](https://www.pythonguis.com/static/tutorials/qt/embed-pyqtgraph-custom-widgets-qt-app/Image3_Qt7P7xP.png) _Promote the widget by specifying the class name as PlotWidget and the header file as pyqtgraph._
The name you use for the file doesn't matter, but it's usually a good idea to name it after the class you're going to create with it. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Voila! The widget is now promoted to a canvas to plot. But you won't be able to see any changes within Qt Designer. Save the window as `mainwindow.ui` in the same directory as your PySide app.
For a complete guide to using Qt Designer's `.ui` files in Python, check out [First steps with Qt Creator](https://www.pythonguis.com/tutorials/pyside-first-steps-qt-creator/).
## Loading the `.ui` File
We now have the `mainwindow.ui` file containing our UI definition. We can load this from Python to show the window and our custom widget.
Let's start from a basic app template.
python ```
import sys
from PySide6.QtWidgets import QApplication
import pyqtgraph as pg
uiclass, baseclass = pg.Qt.loadUiType("mainwindow.ui")
class MainWindow(uiclass, baseclass):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

In this example, we're using PyQtGraph's helper method `pg.Qt.loadUiType` to load the UI. This gives us access to the designed UI class and the base class (in this case `QMainWindow`). With these, we can create our own custom `QMainWindow` subclass to add our plotting methods to.
PyQtGraph supports [PyQt and PySide](https://pyqtgraph.readthedocs.io/en/latest/getting_started/how_to_use.html#pyqt-and-pyside). We can manually define which library to use by importing it before importing `pyqtgraph`. In this tutorial, we're forcing PyQtGraph to use PySide6. Note that if you use some import-sorting tools like [isort](https://pycqa.github.io/isort/), then the code above may not work correctly because those tools swap the import order, which means that PyQtGraph will be imported before PySide6.
Save the code above in the same folder as your `mainwindow.ui` file, and run it as normal:
bash ```
$ python my_app.py

```

![Your graph is now embedded](https://www.pythonguis.com/static/tutorials/qt/embed-pyqtgraph-custom-widgets-qt-app/Image4_4A5iC54.png) _Your graph is now embedded_
You'll see a window with your widget transformed into a PyQtGraph plotting widget.
Let's now create a method to make a plot of hours vs temperature data:
python ```
import sys
from PySide6.QtWidgets import QApplication
import pyqtgraph as pg
uiclass, baseclass = pg.Qt.loadUiType("mainwindow.ui")
class MainWindow(uiclass, baseclass):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.plot(
      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], # Hours
      [30, 32, 34, 32, 33, 31, 29, 32, 35, 45], # Temperature
    )
  def plot(self, hour, temperature):
    self.graphWidget.plot(hour, temperature)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

So we added the `plot()` method, which accepts two arrays, `hour` and `temperature`. Then it plots the data using the `.plot()` method on `graphWidget`.
Run the code, you should see the following.
![The custom PyQtGraph widget showing dummy data.](https://www.pythonguis.com/static/tutorials/qt/embed-pyqtgraph-custom-widgets-qt-app/Image5_2JH5D3E.png) _The custom PyQtGraph widget showing dummy data._
That's it! You have just embedded your first plot with _PyQtGraph_.
The default PyQtGraph plot doesn't look quite polished. You can play around with the `.plot()` call to change the data and see how the plot changes.
In upcoming tutorials, we'll learn how to create more elaborated PyQtGraph plots and how to customize your plots, including line colors, styles, and alternative types of plots.
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Mark As Complete 
[![John Lim Ji Xiong](https://www.pythonguis.com/static/theme/images/authors/john-lim.jpg)](https://www.pythonguis.com/authors/john-lim/)
**Embedding Custom Widgets from Qt Designer in PySide6** was written by [John Lim](https://www.pythonguis.com/authors/john-lim/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
John is a developer from Kuala Lumpur, Malaysia who works as a Senior R&D Engineer. 
**Embedding Custom Widgets from Qt Designer in PySide6** was published in [tutorials](https://www.pythonguis.com/tutorials/) on September 20, 2021 (updated March 19, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[custom-widget](https://www.pythonguis.com/topics/custom-widget/) [widget](https://www.pythonguis.com/topics/widget/) [ qt-designer](https://www.pythonguis.com/topics/qt-designer/) [pyqtgraph](https://www.pythonguis.com/topics/pyqtgraph/) [plot](https://www.pythonguis.com/topics/plot/) [qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [ pyside6-qt-designer](https://www.pythonguis.com/topics/pyside6-qt-designer/) [ data-science](https://www.pythonguis.com/topics/data-science/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
