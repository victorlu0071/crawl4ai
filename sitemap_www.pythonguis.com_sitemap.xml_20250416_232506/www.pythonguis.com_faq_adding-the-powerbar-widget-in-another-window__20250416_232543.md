# Content from: https://www.pythonguis.com/faq/adding-the-powerbar-widget-in-another-window/

[](https://www.pythonguis.com/faq/adding-the-powerbar-widget-in-another-window/#menu)
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
# Debugging widgets not appearing in Qt applications
How to figure things out when something goes wrong
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 02 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
_Christian Schultz wrote_
I'm trying to add the `PowerBar` widget created in the "Custom Widgets" tutorial in a window made in Qt Creator, but it is not appearing. I made a file named "power_bar.py" with the exact content from the tutorial page, and tested it following the tutorial.
Then, I created a new `MainWindow` form in Qt Creator, following the "Embedding custom widgets from Qt Designer" tutorial, put there a widget, and promoted it to `PowerBar` from include file `power_bar`. The ui content can be seen here: https://pastebin.com/v5i2n0Jr
I then compiled the ui to a file named `main_window.py`, which can be seen here:
python ```
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(364, 634)
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.powerbarWidget = PowerBar(5)
    self.powerbarWidget.setGeometry(QtCore.QRect(30, 40, 291, 541))
    self.powerbarWidget.setObjectName("powerbarWidget")
    MainWindow.setCentralWidget(self.centralwidget)
    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
  def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
from power_bar import PowerBar

```

I had to edit this file, in the line where it instantiates the `PowerBar`, I put a number there because by default it instantiates passing `self.centralWidget` as the parameter. Then I made a file to show the `MainWindow`, the content can be seen here:
python ```
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
import sys
from main_window import Ui_MainWindow
class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
if __name__ == "__main__":
  app = QApplication(sys.argv)
  w = Window()
  w.show()
  sys.exit(app.exec_())

```

When I run the code, it shows a window, but it doesn't show the widget. If I put a line after the setupUi like: self.ui.powerbarWidget.show() it shows the widget, but it creates another window.
How can I use this widget in a window, like did in the pyqtgraph example?
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
_Luca_
I guess that you see two windows because at the end of the power_bar.py you have an example of usage not protected by an if statement.
python ```
from power_bar import PowerBar
from PyQt5.Qt import *
import sys
class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.powerbarWidget = PowerBar(5)
    self.setCentralWidget(self.powerbarWidget)
if __name__ == "__main__":
  app = QApplication(sys.argv)
  w = Window()
  w.show()
  sys.exit(app.exec_())

```

Add the if statement at the end of the power_bar.py:
python ```
if __name__ == "__main__":
  app = QtWidgets.QApplication([])
  volume = PowerBar()
  volume.show()
  app.exec_()

```

Else that code will be executed too whenever you import it. The line of code:
python ```
from power_bar import PowerBar

```

shows the first window and enter in the first mainloop. When you close that first window the code after the import is executed, showing another window and entering in another mainloop.
_Christian Schultz_
Hello Luca, thank you for your answer, but I didn't understand what I did wrong. To facilitate a bit I uploaded my code in a zip file to this address: https://gofile.io/d/a5jRAf There you all the files I made. I started creating the main_window.ui, where it have only a main window with a widget, which I promoted to PowerBar and pointing the include file to pwer_bar. The file power_bar is there too, and this file onle have the two classes needed (PowerBar and _Bar), and it have no code outside the classes. I compiled the main_window.ui to main_window.py, and I had to edit this file to be able to instatiate the PowerBar class, and as far as I could understand, this code adds this widget to the main window widget. Then I made the main.py file, which instantiates the MainWindow, and there I put a line with self.ui.powerbarWidget.show(), which shows the widget in another window. If I comment out this file, the main window opens but it shows nothing inside.
So, I still don't understand what I did wrong in this code, so I'm asking if anyone can point what I did wrong.
Thank you
_Luca_
When you notice something strange for example:
  * You can't see your widget
  * You see your widget in the wrong place
  * You see the widget in another window


always check the parent of that widget because the problem could be over there, in particular if you are not using the Qt designer.
Opening the _main_window.py_ file and looking for the instantiation of the PowerBar widget I see:
python ```
self.powerbarWidget = PowerBar(5)

```

The default value for the parent parameter is None, so I've tried to change it in:
python ```
self.powerbarWidget = PowerBar(5, parent = self.centralWidget)

```

And remove the line: 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
python ```
self.ui.powerbarWidget.show()

```

from the file _main.py._
In this way it works so the problem is somewhere else.
In the Object inspector of the Qt designer you should see the widget as a child of the centralwidget.
I've tried to generate it and it set the parent correctly.
Could you better describe all the steps that you do before the conversion and after it? Do you manually edit the main_window.py?
_Martin Fitzpatrick_
As you said, it is passing `self.centralWidget` as the parameter. You can modify the power bar class to accept a parent (I should have done this, will fix). But the reason the window floats is that it isn't contained within a layout (which sets the parent automatically).
![nestedwidget|690x156](https://www.pythonguis.com/static/faq/todo/adding-the-powerbar-widget-in-another-window/dL4imwXwOECqREyLGL2X9WScu9X.png)
You can see in the panel that both of these have the red cross through the layout, meaning that there is no layout applied, so the widget won't be contained in the window. If you don't set a parent on it, it will free-float as it's own window. Set a layout on the `centralWidget` to avoid this.
The working compiled UI -- had to make the change to the steps param as you noted.
python ```
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(364, 634)
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.powerbarWidget = PowerBar(5)
    self.powerbarWidget.setObjectName("powerbarWidget")
    self.horizontalLayout.addWidget(self.powerbarWidget)
    MainWindow.setCentralWidget(self.centralwidget)
    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
  def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
from power_bar import PowerBar

```

_Christian Schultz_
Thank you Martin for your help, it worked perfectly. I did another try, where I put another widget and promoted it to PowerBar, edited the compiled ui file (changing one widget to have 5 bars and another to 7 bars) and it worked perfectly.
If I may suggest you, you could add this instructions on the tutorial explaining how to include the custom widget in a window with other widgets (buttons, labels) interacting with the custom widget, it would be awesome.
Other thing that would be awesome is a tutorial explaining how to create a composite widget (meaning, a widget made from other widgets), designing this composite in Qt Designer. Your tutorial explains how to do it using only code, and arranging the widgets using only code sometimes is a bit boring. I am (trying) to make a program where I have a "block" of widgets, and this block I will use in other parts of my application. This block is made of some checkboxes, spin boxes and labels. In order to do it (after reading lots of texts and a lot of try and error) I made it to work, where I create a widget in Qt Designer, arrange them the way I want, then I compile them to a py file, then I copy and paste the contets to another class, edit most of the declarations to make them work, and then I can create methods and signals to interact with the composite widget. It worked, but I need to do a lot of work, and probably there is better ways to do it. If you know how to do it and add this information in the tutorial, it would amazing!
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Debugging widgets not appearing in Qt applications** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/adding-the-powerbar-widget-in-another-window/Python books) on the subject. 
**Debugging widgets not appearing in Qt applications** was published in [faq](https://www.pythonguis.com/faq/) on June 10, 2020 (updated September 02, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
