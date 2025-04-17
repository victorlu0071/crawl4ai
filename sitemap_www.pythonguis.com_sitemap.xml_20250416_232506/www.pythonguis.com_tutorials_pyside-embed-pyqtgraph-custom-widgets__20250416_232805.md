# Content from: https://www.pythonguis.com/tutorials/pyside-embed-pyqtgraph-custom-widgets/

[](https://www.pythonguis.com/tutorials/pyside-embed-pyqtgraph-custom-widgets/#menu)
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
# Embedding Custom Widgets from Qt Designer in PySide2
Learn how to use custom widgets in your PySide2 applications when designing with Qt Designer
by [John Lim](https://www.pythonguis.com/authors/john-lim/) Last updated Mar 19 PySide2 [ Tutorials ](https://www.pythonguis.com/tutorials/)
This tutorial is also available for [PySide6](https://www.pythonguis.com/tutorials/pyside6-embed-pyqtgraph-custom-widgets/) , [PyQt6](https://www.pythonguis.com/tutorials/pyqt6-embed-pyqtgraph-custom-widgets-qt-app/) and [PyQt5](https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/)
Qt Designer is a great tool for designing PySide GUIs, allowing you to use the entire range of Qt5 widgets and layouts to construct your apps. As your applications get more complex however you may find yourself creating custom widgets, or using PySide libraries such as _PyQtGraph_ , who's widgets are not available within Designer.
Helpfully, Qt Designer supports a mechanism for using _placeholder_ widgets to represent your custom or external widgets in your design. This tutorial will walk you through the process of using placeholders to include a _PyQtGraph_ plot in your app from within Qt Designer.
Table of Contents
  * [Promoting Widgets](https://www.pythonguis.com/tutorials/pyside-embed-pyqtgraph-custom-widgets/#promoting-widgets)
  * [PyQtGraph](https://www.pythonguis.com/tutorials/pyside-embed-pyqtgraph-custom-widgets/#pyqtgraph)
  * [Qt Designer](https://www.pythonguis.com/tutorials/pyside-embed-pyqtgraph-custom-widgets/#qt-designer)
  * [Loading the .ui file](https://www.pythonguis.com/tutorials/pyside-embed-pyqtgraph-custom-widgets/#loading-the-ui-file)


## Promoting Widgets
The principle of using placeholders in Qt Designer is quite straightforward — 
  1. Create a UI as normal in Qt Designer.
  2. Add a _placeholder_ widget to represent the custom widget you're adding.
  3. Tell Qt to replace your placeholder with your actual widget when building the UI.


In Qt this final step is referred to as _promoting_ (as in _promoting_ a base class).
If the custom widget you are adding is a subclass of an existing Qt widget, you may want to use the base class as your placeholder to promote from. For example, if you have a custom `MyAwesomeButton` button widget subclassed from `QPushButton` use `QPushButton` as the placeholder and promote it to `MyAwesomeButton`. This gives you access to the base class properties, events and actions from within Qt Designer.
If you don't have an obvious base class to use, then you can use `QWidget`, the common base class of all Qt widgets.
## PyQtGraph
Data science is one of the post popular uses of Python, and building dashboards and analysis tools is a common use case of PySide. For all of these being able to add plots to your UI is very useful — and being able to do this from Qt Designer even more so.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
There are a number of plotting libraries available in Python, with _matplotlib_ being the most popular and offering some basic support for PySide. [PyQtGraph](http://www.pyqtgraph.org/) is an popular alternative which uses Qt's native `QGraphicsScene` to provide fast zooming, scaling, drag-drop behaviour that feels a natural part of your application.
Whether you're using _PyQtGraph_ or _maplotlib_ for your plotting needs, the plot canvas widgets are not available from within Qt Designer. In this tutorial I'll walk you through the process of using these custom widgets in your apps.
If you don't have _PyQtGraph_ installed already, you can install it using:
bash ```
pip install pyqtgraph

```

The instructions below aren't specific to _PyQtGraph_ , and you can use the same process to add _matplotlib_ or any other custom widgets to your app.
## Qt Designer
We will be using Qt Designer to create a simple UI design, and adding a placeholder for our PyQtGraph widget. First open Qt Designer and create a new `QMainWindow` as normal.
![Qt Creator — Select MainWindow for widget type](https://www.pythonguis.com/static/tutorials/qt/embed-pyqtgraph-custom-widgets-qt-app/Screenshot_2019-05-30_at_23.01.09.png) _Qt Creator — Select MainWindow for widget type_
We next need to add the _placeholder_ widget. As there is no suitable baseclass for the _PyQtGraph_ plot widget, we'll use the basic `QWidget` as our placeholder. Select the _Widget_ from the left sidebar and place it in the centre of your window.
Give the widget a name, "graphWidget" will do. This is just a tag to reference the element in code.
![Add a widget to the window. Name the widget as "graphWidget"](https://www.pythonguis.com/static/tutorials/qt/embed-pyqtgraph-custom-widgets-qt-app/Image1_K4dflzn.png) _Add a widget to the window. Name the widget as "graphWidget"_
Right click on the widget and select _Promote to_ from the widget's context menu.
_Promoting_ a `QWidget` indicates that it should be replaced with the specified subclass, in our case the _PyQtGraph_ plot widget.
A promoted widget can be reverted back to its base class by right-clicking and choosing Demote to from the widget's context menu.
![Right click to show the promotion menu](https://www.pythonguis.com/static/tutorials/qt/embed-pyqtgraph-custom-widgets-qt-app/Image2_EdOPTIx.png) _Right click to show the promotion menu_
You will be presented with a dialog to specify the custom widget class the placeholder widget will become.
The _header file_ is the name of the Python module used to import the class, which is `pyqtgraph`. Specify `PlotWidget` as the class name of the widget to replace it with.
![Promote the widget by specifying the class name as PlotWidget and header file as pyqtgraph.](https://www.pythonguis.com/static/tutorials/qt/embed-pyqtgraph-custom-widgets-qt-app/Image3_Qt7P7xP.png) _Promote the widget by specifying the class name as PlotWidget and header file as pyqtgraph._
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
The name you use for the file doesn't matter, but it's usually a good idea to name it after the class you're going to create with it.
Voila! The widget is now promoted to a canvas to plot. But you won't be able to see any changes within Qt Designer. Save the window as `mainwindow.ui` in the same directory as your PySide app.
For a complete guide to using Qt Designer .ui files from Python check out [First steps with Qt Creator](https://www.pythonguis.com/tutorials/pyside-first-steps-qt-creator/).
## Loading the .ui file
We now have the `mainwindow.ui` file containing our UI definition. We can load this from Python to show the window and our custom widget.
Let's start from a basic app template.
python ```
import sys
from PySide2.QtWidgets import QApplication
import pyqtgraph as pg
uiclass, baseclass = pg.Qt.loadUiType("mainwindow.ui")
class MainWindow(uiclass, baseclass):
  def __init__(self):
    super().__init__()
    self.setupUi(self)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

```

In this example we're using PyQtGraph's helper method `pg.Qt.loadUiType` to load the UI. This gives us access to the designed UI class and the base class (in this case `QMainWindow`). With these we can create our own custom `QMainWindow` subclass to add our plotting methods to.
Save the code above in the same folder as your `mainwindow.ui` file, and run it as normal.
bash ```
python3 my_app.py

```

![Your graph is now embedded](https://www.pythonguis.com/static/tutorials/qt/embed-pyqtgraph-custom-widgets-qt-app/Image4_4A5iC54.png) _Your graph is now embedded_
You should see a window with your widget transformed into a _PyQtGraph_ plotting widget.
Let's now create a function to make a simple plot of `x` and `y` data.
python ```
import sys
from PySide2.QtWidgets import QApplication
import pyqtgraph as pg
uiclass, baseclass = pg.Qt.loadUiType("mainwindow.ui")
class MainWindow(uiclass, baseclass):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])
  def plot(self, hour, temperature):
    self.graphWidget.plot(hour, temperature)
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

```

So we added the `plot()` method which accepts two arrays, `temp` _Temperature_ and `hour` _Hour_ , then plots the data using the _graph widget_ `.plot()` method.
Run the code, you should see the following.
![The custom PyQtGraph widget showing dummy data.](https://www.pythonguis.com/static/tutorials/qt/embed-pyqtgraph-custom-widgets-qt-app/Image5_2JH5D3E.png) _The custom PyQtGraph widget showing dummy data._
That's it! You have just embedded your first plot with _PyQtGraph_.
The default _PyQtGraph_ plot isn't very pretty, however can play around with the `.plot()` call to change the data shown.
We'll cover more complex _PyQtGraph_ plots and plot customization, including line colours, styles and alternative types of plots in an upcoming tutorial. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
[![John Lim Ji Xiong](https://www.pythonguis.com/static/theme/images/authors/john-lim.jpg)](https://www.pythonguis.com/authors/john-lim/)
**Embedding Custom Widgets from Qt Designer in PySide2** was written by [John Lim](https://www.pythonguis.com/authors/john-lim/) . 
John is a developer from Kuala Lumpur, Malaysia who works as a Senior R&D Engineer. 
**Embedding Custom Widgets from Qt Designer in PySide2** was published in [tutorials](https://www.pythonguis.com/tutorials/) on September 20, 2019 (updated March 19, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[custom-widget](https://www.pythonguis.com/topics/custom-widget/) [widget](https://www.pythonguis.com/topics/widget/) [ qt-designer](https://www.pythonguis.com/topics/qt-designer/) [pyqtgraph](https://www.pythonguis.com/topics/pyqtgraph/) [plot](https://www.pythonguis.com/topics/plot/) [qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [ pyside2-qt-designer](https://www.pythonguis.com/topics/pyside2-qt-designer/) [ data-science](https://www.pythonguis.com/topics/data-science/) [python](https://www.pythonguis.com/topics/python/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
