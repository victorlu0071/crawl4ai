# Content from: https://www.pythonguis.com/faq/how-to-show-qmenu-title/

[](https://www.pythonguis.com/faq/how-to-show-qmenu-title/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PyQt5 ](https://www.pythonguis.com/pyqt5/)
  * [PyQt5 Tutorial ](https://www.pythonguis.com/pyqt5-tutorial/)
  * Basics
  * [Create a PyQt5 app](https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/)
  * [PyQt5 Signals](https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/)
  * [PyQt5 Widgets](https://www.pythonguis.com/tutorials/pyqt-basic-widgets/)
  * [PyQt5 Layouts](https://www.pythonguis.com/tutorials/pyqt-layouts/)
  * [PyQt5 Menus](https://www.pythonguis.com/tutorials/pyqt-actions-toolbars-menus/)
  * [PyQt5 Dialogs](https://www.pythonguis.com/tutorials/pyqt-dialogs/)
  * [Multi-window PyQt5](https://www.pythonguis.com/tutorials/creating-multiple-windows/)
  * Qt Designer
  * [First Qt Designer app](https://www.pythonguis.com/tutorials/first-steps-qt-creator/)
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/creating-dialogs-qt-designer/)
  * [The QResource System in PyQt5](https://www.pythonguis.com/tutorials/qresource-system/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/)
  * Plotting
  * [Plotting With PyQtGraph and PyQt5](https://www.pythonguis.com/tutorials/plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PyQt5](https://www.pythonguis.com/tutorials/plotting-matplotlib/)
  * QGraphics
  * [Vector Graphics](https://www.pythonguis.com/tutorials/pyqt-qgraphics-vector-graphics/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/qpropertyanimation/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/system-tray-mac-menu-bar-applications-pyqt/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/)
  * [Packaging for Linux](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-linux-pyinstaller/)
  * [Packaging QResources](https://www.pythonguis.com/tutorials/packaging-data-files-pyqt5-with-qresource-system/)
  * [Packaging with fbs](https://www.pythonguis.com/tutorials/packaging-pyqt5-apps-fbs/)
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
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# How to Show Qmenu Title
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 06 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
tcarson4344 | 2020-05-25 18:03:30 UTC | #1
I am working on a Qdialog with an embedded Matplotlib plot. I have a RMB context menu popup but I want it to show the menu title. I can set the title (line 69) but I am not sure how to make it display.
python ```
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
import numpy as np
import random
class FBPlot(QDialog):
  def __init__(self, parent=None):
    super(FBPlot, self).__init__(parent)
    # a figure instance to plot on
    self.figure = plt.figure()
    # this is the Canvas Widget that displays the `figure`
    # it takes the `figure` instance as a parameter to __init__
    self.canvas = FigureCanvas(self.figure)
    ax = self.figure.add_subplot(111)
    # Capture button press
    self.canvas.mpl_connect('button_press_event', self.on_press)
    self.canvas.mpl_connect('pick_event', self.pick)
    # set the layout
    layout = QVBoxLayout()
    layout.addWidget(self.canvas)
    self.setLayout(layout)
    # self.ax.grid(True)
    self.canvas.draw()
    self.span = SpanSelector(ax,
                 self.spanzoom,
                 'horizontal',
                 useblit=True,
                 rectprops=dict(alpha=0.5, facecolor='red'),
                 button=1)
  def on_press(self, event):
    print(event)
    if event.button == 3:
      canvasSize = event.canvas.geometry()
      Qpoint_click = event.canvas.mapToGlobal(
        QtCore.QPoint(event.x, canvasSize.height()-event.y))
      if event.inaxes != None:
        self.fbMenu = QtWidgets.QMenu()
        self.fbMenu.addSection("Front/Back")
        self.fbMenu.addSeparator()
        self.fbMenu.addAction("Select All Curves")
        self.fbMenu.addAction("Remove All Curves")
        self.fbMenu.addSeparator()
        self.fbMenu.addAction("Legend")
        self.fbMenu.addAction("Cursor Legend")
        self.fbMenu.move(Qpoint_click)
        self.fbMenu.show()
      else:
        # Y Axis Front Area
        self.ylim_menu = QtWidgets.QMenu('&Limits')
        self.ylim_menu.addAction("Fixed")
        self.ylim_menu.addAction("Free")
        self.ylim_menu.addAction("Optimized")
        # y axis main menu
        self.yMenu = QtWidgets.QMenu('&Y Axis')
        self.yMenu.setTitle('sdfj')
        self.yMenu.addMenu(self.ylim_menu)
        self.yMenu.addSeparator()
        self.yMenu.addAction("Visable")
        self.yMenu.addAction("Options...")
        self.yMenu.move(Qpoint_click)
        self.yMenu.show()
        # Y Axis Back Area
        print(self.yMenu.title())
        # X Axis Area
        # Title Area
    else:
      pass
  def pick(self, event):
    print(event)
  def spanzoom(self, xmin, xmax):
    # indmin, indmax = np.searchsorted(x, (xmin, xmax))
    # indmax = min(len(x) - 1, indmax)
    # thisx = x[indmin:indmax]
    # thisy = y[indmin:indmax]
    # fb1.set_data(thisx, thisy)
    self.ax.set_xlim(xmin, xmax)
    #ax1.set_ylim(thisy.min(), thisy.max())
    self.canvas.draw()
  # def plot(self, xdata, ydata):
  #  self.ax.plot(xdata, ydata)
if __name__ == '__main__':
  app = QApplication(sys.argv)
  main = FBPlot()
  # generate data
  # np.random.seed(19680801)
  # x = np.arange(0.0, 5.0, 0.01)
  # y = np.sin(2*np.pi*x) + 0.5*np.random.randn(len(x))
  # fb1, = main.plot(x, y, Label='data')
  main.show()
  sys.exit(app.exec_())

```

Luca | 2020-05-25 14:27:41 UTC | #2
I think the title that you are setting is the one that would be visible if you add that QMenu to a QMenuBar, I'm not sure that internally, it is implemented to be shown as you would.
martin | 2020-05-25 18:29:23 UTC | #3
Yep, unfortunately as @Luca says the menu title is used when displaying the menu on the menubar -- i.e. it's the File, Edit, etc. title.
The menu does provide a `menu.addSection(<str>)` method which might be what you're looking for? But on macOS/Windows themes it is no different to a separator. The only way I can find to actually show it is using the Qt Fusion theme, e.g.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt5](https://www.pythonguis.com/static/theme/images/products/pyqt5-book.png)](https://www.pythonguis.com/pyqt5-book/)
[Take a look ](https://www.pythonguis.com/pyqt5-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/create-simple-gui-applications/) and [Amazon Paperback](https://www.amazon.com/dp/B08RB2HRS1/)
python ```
app = QApplication(sys.argv)
app.setStyle("Fusion")

```

Then using the following
python ```
self.fbMenu.addSection("A menu part")

```

...will give the following results in the menu...
![Screenshot 2020-05-25 at 20.23.57|518x428](https://www.pythonguis.com/static/faq/forum/how-to-show-qmenu-title/uDfionnbsfnw491yeKWQ9fRm8I9.png)
The [Fusion theme](https://doc.qt.io/archives/qt-5.8/gallery-fusion.html) is a cross-platform toolkit, so your app will look the same on all platforms. But it won't look "native" on any.
One other option you have is to add a null `QAction` and disable it, e.g.
python ```
        a = self.fbMenu.addAction("A menu part")
        a.setDisabled(True)

```

This will show up how I suspect you're expecting it to...
![Screenshot 2020-05-25 at 20.11.05|501x500](https://www.pythonguis.com/static/faq/forum/how-to-show-qmenu-title/2dhN9RuWAQl8MtpsNiEwfe63uJr.png)
...but that's potentially confusing for users if it looks otherwise like a disabled entry. I've not found a way to reliably theme individual menu items (e.g. so you could highlight this dummy entry in a different colour).
tcarson4344 | 2020-05-25 18:46:29 UTC | #4 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
thanks,
I ended up adding a label Widget. took more lines of code that I wanted but looks ok I think I need to make it bold and/or color background to change the appearance.
It looks like this: ![context|323x221](https://www.pythonguis.com/static/faq/forum/how-to-show-qmenu-title/jLx8wsdUVJ77o4F78Yph9niT5H8.gif)
My Code (in case someone wants it):
python ```
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QLabel, QWidgetAction, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
import numpy as np
import random
class FBPlot(QDialog):
  def __init__(self, parent=None):
    super().__init__(parent)
    # a figure instance to plot on
    self.figure = plt.figure()
    # this is the Canvas Widget that displays the `figure`
    # it takes the `figure` instance as a parameter to __init__
    self.canvas = FigureCanvas(self.figure)
    ax = self.figure.add_subplot(111)
    # Capture button press
    self.canvas.mpl_connect('button_press_event', self.on_press)
    self.canvas.mpl_connect('pick_event', self.pick)
    # set the layout
    layout = QVBoxLayout()
    layout.addWidget(self.canvas)
    self.setLayout(layout)
    # self.ax.grid(True)
    self.canvas.draw()
    self.span = SpanSelector(ax,
                 self.spanzoom,
                 'horizontal',
                 useblit=True,
                 rectprops=dict(alpha=0.5, facecolor='red'),
                 button=1)
  def on_press(self, event):
    print(event)
    if event.button == 3:
      canvasSize = event.canvas.geometry()
      Qpoint_click = event.canvas.mapToGlobal(
        QtCore.QPoint(event.x, canvasSize.height()-event.y))
      if event.inaxes != None:
        self.fbMenu = QtWidgets.QMenu()
        #Add a title to context menu
        fbtl = QLabel('Front/Back')
        fbtl.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        fbtl.setAlignment(Qt.AlignCenter)
        fbtlAction = QWidgetAction(fbtl)
        fbtlAction.setDefaultWidget(fbtl)
        self.fbMenu.addAction(fbtlAction)
        # Add rest of menu items
        self.fbMenu.addSeparator()
        self.fbMenu.addAction("Select All Curves")
        self.fbMenu.addAction("Remove All Curves")
        self.fbMenu.addSeparator()
        self.fbMenu.addAction("Legend")
        self.fbMenu.addAction("Cursor Legend")
        self.fbMenu.move(Qpoint_click)
        self.fbMenu.show()
      else:
        # Y Axis Front Area
        self.ylim_menu = QtWidgets.QMenu('&Limits')
        self.ylim_menu.addAction("Fixed")
        self.ylim_menu.addAction("Free")
        self.ylim_menu.addAction("Optimized")
        # y axis main menu
        self.yMenu = QtWidgets.QMenu('&Y Axis')
        self.yMenu.setTitle('sdfj')
        self.yMenu.addMenu(self.ylim_menu)
        self.yMenu.addSeparator()
        self.yMenu.addAction("Visable")
        self.yMenu.addAction("Options...")
        self.yMenu.move(Qpoint_click)
        self.yMenu.show()
        # Y Axis Back Area
        print(self.yMenu.title())
        # X Axis Area
        # Title Area
    else:
      pass
  def pick(self, event):
    print(event)
  def spanzoom(self, xmin, xmax):
    # indmin, indmax = np.searchsorted(x, (xmin, xmax))
    # indmax = min(len(x) - 1, indmax)
    # thisx = x[indmin:indmax]
    # thisy = y[indmin:indmax]
    # fb1.set_data(thisx, thisy)
    self.ax.set_xlim(xmin, xmax)
    #ax1.set_ylim(thisy.min(), thisy.max())
    self.canvas.draw()
  # def plot(self, xdata, ydata):
  #  self.ax.plot(xdata, ydata)
if __name__ == '__main__':
  app = QApplication(sys.argv)
  main = FBPlot()
  # generate data
  # np.random.seed(19680801)
  # x = np.arange(0.0, 5.0, 0.01)
  # y = np.sin(2*np.pi*x) + 0.5*np.random.randn(len(x))
  # fb1, = main.plot(x, y, Label='data')
  main.show()
  sys.exit(app.exec_())

```

martin | 2020-05-25 18:46:25 UTC | #5
Nice solution @tcarson4344 hadn't occurred to me to use a widget for this. Thanks for posting! :+1:
cippall | 2021-08-04 07:37:05 UTC | #6
Thanks for posting your solution. Really helped.
Just a note that the QWidgetAction needs as a parent the menu not the label itself. To avoid my app to crash i had to modify these lines: 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
python ```
    fbtlAction = QWidgetAction(self.fbMenu)

```

Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**How to Show Qmenu Title** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/how-to-show-qmenu-title/Python books) on the subject. 
**How to Show Qmenu Title** was published in [faq](https://www.pythonguis.com/faq/) on May 24, 2020 (updated November 06, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
