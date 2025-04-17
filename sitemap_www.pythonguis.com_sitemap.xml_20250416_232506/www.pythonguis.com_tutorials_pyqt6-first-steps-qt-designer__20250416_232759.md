# Content from: https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/

[](https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/#menu)
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
# First Steps With Qt Designer and PyQt6
Use Qt Designer's drag and drop interface to design your PyQt6 GUI
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Mar 15 PyQt6 [ Creating applications with Qt Designer and PyQt6 ](https://www.pythonguis.com/pyqt6-tutorial/#pyqt6-qt-designer)
#### [ PyQt6 Tutorial ](https://www.pythonguis.com/pyqt6-tutorial/) — [Creating applications with Qt Designer and PyQt6](https://www.pythonguis.com/pyqt6-tutorial/#pyqt6-qt-designer)
  * [First Steps With Qt Designer and PyQt6](https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/)
  * [Laying Out Your PyQt6 GUIs With Qt Designer](https://www.pythonguis.com/tutorials/pyqt6-qt-designer-gui-layout/)
  * [Creating Dialogs With Qt Designer and PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-dialogs-qt-designer/)
  * [Embedding Custom Widgets from Qt Designer in PyQt6](https://www.pythonguis.com/tutorials/pyqt6-embed-pyqtgraph-custom-widgets-qt-app/)


This tutorial is also available for [PySide6](https://www.pythonguis.com/tutorials/pyside6-first-steps-qt-designer/) , [PySide2](https://www.pythonguis.com/tutorials/pyside-first-steps-qt-designer/) and [PyQt5](https://www.pythonguis.com/tutorials/first-steps-qt-creator/)
So far we have been creating apps using Python code. This works great in many cases, but as your applications get larger or interfaces more complicated, it can get a bit cumbersome to define all widgets programmatically. The good news is that Qt comes with a graphical editor — _Qt Designer_ — which contains a drag-and-drop UI editor. Using _Qt Designer_ you can define your UIs visually and then simply hook up the application logic later.
In this tutorial we'll cover the basics of creating UIs with _Qt Designer_. The principles, layouts and widgets are identical, so you can apply everything you've already learnt. You'll also need your knowledge of the Python API to hook up your application logic later.
This tutorial requires Qt Creator to be installed — you can download it free from the Qt website. Go to <https://www.qt.io/download> and download the Qt package. You can opt to install only Creator during the installation.
Open up Qt Creator and you will be presented with the main window. The designer is available via the tab on the left hand side. However, to activate this you first need to start creating a `.ui` file.
![The Qt Creator interface, with the Design section shown on the left.](https://www.pythonguis.com/static/tutorials/qt/first-steps-qt-creator/qt-creator-start.png) _The Qt Creator interface, with the Design section shown on the left._
To create a `.ui` file go to File -> New File or Project... In the window that appears select _Qt_ under _Files and Classes_ on the left, then select _Qt Designer Form_ on the right. You'll notice the icon has "ui" on it, showing the type of file you're creating.
![Create a new Qt .ui file.](https://www.pythonguis.com/static/tutorials/qt/first-steps-qt-creator/qt-creator-create-ui-file1.png) _Create a new Qt .ui file._
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
In the next step you'll be asked what type of widget you want to create. If you are starting an application then _Main Window_ is the right choice. However, you can also create `.ui` files for dialog boxes, forms and custom compound widgets.
![Select the type of widget to create, for most applications this will be Main Window.](https://www.pythonguis.com/static/tutorials/qt/first-steps-qt-creator/qt-creator-create-ui-file2.png) _Select the type of widget to create, for most applications this will be Main Window._
Next choose a filename and save folder for your file. Save your `.ui` file with the same name as the class you'll be creating, just to make make subsequent commands simpler.
![Choose save name and folder your your file.](https://www.pythonguis.com/static/tutorials/qt/first-steps-qt-creator/qt-creator-create-ui-file3.png) _Choose save name and folder your your file._
Finally, you can choose to add the file to your version control system if you're using one. Feel free to skip this step — it doesn't affect your UI.
![Optionally add the file to your version control, e.g. Git.](https://www.pythonguis.com/static/tutorials/qt/first-steps-qt-creator/qt-creator-create-ui-file4.png) _Optionally add the file to your version control, e.g. Git._
## Laying out your Main Window
You'll be presented with your newly created main window in the UI designer. There isn't much to see to begin with, just a grey working area representing the window, together with the beginnings of a window menu bar.
![The initial view of the created main window.](https://www.pythonguis.com/static/tutorials/qt/first-steps-qt-creator/qt-creator-main-window.png) _The initial view of the created main window._
You can resize the window by clicking the window and dragging the blue handles on each corner.
![The initial view of the created main window.](https://www.pythonguis.com/static/tutorials/qt/first-steps-qt-creator/qt-creator-layout-start.png) _The initial view of the created main window._
The first step in building an application is to add some widgets to your window. In our first applications we learnt that to set the central widget for a `QMainWindow` we need to use `.setCentralWidget()`. We also saw that to add multiple widgets with a layout, we need an intermediary `QWidget` to apply the layout to, rather than adding the layout to the window directly.
Qt Creator takes care of this for you automatically, although it's not particularly obvious about it.
To add multiple widgets to the main window with a layout, first drag your widgets onto the `QMainWindow`. Here we're dragging 3 labels. It doesn't matter where you drop them.
![Main window with 1 labels and 1 button added.](https://www.pythonguis.com/static/tutorials/qt/first-steps-qt-creator/qt-creator-layout1.png) _Main window with 1 labels and 1 button added._
We've created 2 widgets by dragging them onto the window, made them children of that window. We can now apply a layout.
Find the `QMainWindow` in the right hand panel (it should be right at the top). Underneath you see _centralwidget_ representing the window's central widget. The icon for the central widget show the current layout applied. Initially it has a red circle-cross through it, showing that there is no layout active.
Right click on the `QMainWindow` object, and find 'Layout' in the resulting dropdown.
![Right click on the main window, and choose layout.](https://www.pythonguis.com/static/tutorials/qt/first-steps-qt-creator/qt-creator-layout2.png) _Right click on the main window, and choose layout._
Next you'll see a list of layouts which you can apply to the window. Select _Lay Out Horizontally_ and the layout will be applied to the widget.
![Select layout to apply to the main window.](https://www.pythonguis.com/static/tutorials/qt/first-steps-qt-creator/qt-creator-layout3.png) _Select layout to apply to the main window._
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
The selected layout is applied to the the _centralwidget_ of the `QMainWindow` and the widgets are added the layout, being laid out depending on the selected layout. Note that in Qt Creator you can actually drag and re-order the widgets within the layout, or select a different layout, as you like. This makes it especially nice to prototyping and trying out things.
![Vertical layout applied to widgets on the main window.](https://www.pythonguis.com/static/tutorials/qt/first-steps-qt-creator/qt-creator-layout4.png) _Vertical layout applied to widgets on the main window._
## Using your generated .ui file
We've created a very simple UI. The next step is to get this into Python and use it to construct a working application.
First save your `.ui` file — by default it will save at the location you chosen while creating it, although you can choose another location if you like.
The `.ui` file is in XML format. To use our UI from Python we have two alternative methods available —
  1. load into into a class using the `.loadUI()` method
  2. convert it to Python using the `pyuic6` tool.


These two approaches are covered below. Personally I prefer to convert the UI to a Python file to keep things similar from a programming & packaging point of view.
### Loading the .ui file directly
To load `.ui` files we can use the `uic` module included with PyQt6, specifically the `uic.loadUI()`method. This takes the filename of a UI file and loads it creating a fully-functional PyQt6 object.
python ```
import sys
from PyQt6 import QtWidgets, uic
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("mainwindow.ui")
window.show()
app.exec()

```

![A \(very\) simple UI designed in Qt Creator](https://www.pythonguis.com/static/tutorials/qt/first-steps-qt-creator/Screenshot_2019-05-29_at_22.42.25.png) _A (very) simple UI designed in Qt Creator_
As the `uid.loadUI()` method turns an instance object you cannot attach custom `__init__()` code. You can however handle this through a custom setup function
To load a UI from the `__init__` block of an existing widget (e.g. a `QMainWindow`) you can use `uic.loadUI(filename, self)` for PyQt6.
python ```
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    uic.loadUi("mainwindow.ui", self)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

### Converting your .ui file to Python
To generate a Python output file run `pyuic6` from the command line, passing the `.ui` file and the target file for output, with a `-o` parameter. The following will generate a Python file named `MainWindow.py` which contains our created UI.
bash ```
pyuic6 mainwindow.ui -o MainWindow.py

```

If you're using PyQt5 the tool is named `pyuic4`, but is otherwise completely identical.
You can open the resulting `MainWindow.py` file in an editor to take a look, although you should _not_ edit this file. The power of using Qt Creator is being able to edit, tweak and update your application while you develop. Any changes made to this file will be lost when you update it. However, you _can_ override and tweak anything you like when you import and use the file in your applications.
Importing the resulting Python file works as for any other. You can import your class as follows. The `pyuic6` tool appends `Ui_` to the name of the object defined in _Qt Creator_ , and it is this object you want to import.
python ```
from MainWindow import Ui_MainWindow

```

To create the main window in your application, create a class as normal but subclassing from both `QMainWindow` and your imported `Ui_MainWindow` class. Finally, call `self.setupUi(self)` from within the `__init__` to trigger the setup of the interface.
python ```
import sys
from PyQt6 import QtWidgets, uic
from MainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self, *args, obj=None, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

This produces exactly the same result as before.
![A \(very\) simple UI designed in Qt Creator](https://www.pythonguis.com/static/tutorials/qt/first-steps-qt-creator/Screenshot_2019-05-29_at_22.42.25.png) _A (very) simple UI designed in Qt Creator_
That's it. Your window is now fully set up. Since the use of a .ui file abstracts out the UI-specific code, you can use this same pattern to load any interface you design.
## Adding application logic
You can interact with widgets created through Qt Creator just as you would those created with code. To make things simpler `uic` adds all child widgets to the window object by their id name as specified in Qt Creator. We'll cover how to work with these in the next part.
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Mark As Complete 
Continue with [ PyQt6 Tutorial ](https://www.pythonguis.com/tutorials/pyqt6-qt-designer-gui-layout/ "Continue to next part")
Return to [Create Desktop GUI Applications with PyQt6 ](https://www.pythonguis.com/pyqt6-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**First Steps With Qt Designer and PyQt6** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/Python books) on the subject. 
**First Steps With Qt Designer and PyQt6** was published in [tutorials](https://www.pythonguis.com/tutorials/) on April 15, 2021 (updated March 15, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qt](https://www.pythonguis.com/topics/qt/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ qt-designer](https://www.pythonguis.com/topics/qt-designer/) [qt-creator](https://www.pythonguis.com/topics/qt-creator/) [ pyqt6-qt-designer](https://www.pythonguis.com/topics/pyqt6-qt-designer/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
