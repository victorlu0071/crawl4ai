# Content from: https://www.pythonguis.com/faq/creating-new-windows-on-qtdesigner-based-py-files/

[](https://www.pythonguis.com/faq/creating-new-windows-on-qtdesigner-based-py-files/#menu)
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
# Creating new windows on Qtdesigner based .py files
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
yilmazbah10043 | 2021-02-22 14:23:48 UTC | #1
Hello guys.
I want to open new window from button. But my design comes from Qtdesigner. The question about QtDesigner based codes!!!. The main problem is all those tactics are not working on qtdesigner based .py files.
For examples:
I put one button at Qtdesigner. There is nothing more.
Just i wanted, when i push the button launch the same window. when i translate to python code, it gives me a class and an if structure.
Here i explained with photos: https://forum.qt.io/topic/113427/open-new-window-in-pyqt5/11 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Because of this reason i copied the class and change name class Ui_MainWindow(object): >>>>>>>>>>>>>>>class Ui_MainWindow2(object):
Now i have two classes. In first class i will tried to call second class.
This the first untouched code:(so long :wink: )
python ```
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'x.ui'
# Created by: PyQt5 UI code generator 5.15.2
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again. Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
def setupUi(self, MainWindow):
MainWindow.setObjectName("MainWindow")
MainWindow.resize(260, 226)
self.centralwidget = QtWidgets.QWidget(MainWindow)
self.centralwidget.setObjectName("centralwidget")
self.pushButton = QtWidgets.QPushButton(self.centralwidget)
self.pushButton.setGeometry(QtCore.QRect(90, 120, 75, 23))
self.pushButton.setObjectName("pushButton")
MainWindow.setCentralWidget(self.centralwidget)
self.menubar = QtWidgets.QMenuBar(MainWindow)
self.menubar.setGeometry(QtCore.QRect(0, 0, 260, 21))
self.menubar.setObjectName("menubar")
MainWindow.setMenuBar(self.menubar)
self.statusbar = QtWidgets.QStatusBar(MainWindow)
self.statusbar.setObjectName("statusbar")
MainWindow.setStatusBar(self.statusbar)
  self.retranslateUi(MainWindow)
  QtCore.QMetaObject.connectSlotsByName(MainWindow)
def retranslateUi(self, MainWindow):
  _translate = QtCore.QCoreApplication.translate
  MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
  self.pushButton.setText(_translate("MainWindow", "PushButton"))

if **name** == "**main**":
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

```

I just copied the class. Now i have two. And i added a simple def for calling the other class.
It's offer me build init
[![5c7ff758-d900-4c9d-b168-771fa5302c85-image.png](https://www.pythonguis.com/static/faq/forum/creating-new-windows-on-qtdesigner-based-py-files/ppNTR6H02q0s26dvJmuB0vasKPi.png)](https://ddgobkiprc33d.cloudfront.net/dd467fba-71fa-40d6-ba29-5ca14ca0b071.png)
I accepted
Finally any solution didn't help me. Especially designer based codes hasn't solution.
python ```
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow2(object):
def setupUi(self, MainWindow):
MainWindow.setObjectName("MainWindow")
MainWindow.resize(260, 226)
self.centralwidget = QtWidgets.QWidget(MainWindow)
self.centralwidget.setObjectName("centralwidget")
self.pushButton = QtWidgets.QPushButton(self.centralwidget)
self.pushButton.setGeometry(QtCore.QRect(90, 120, 75, 23))
self.pushButton.setObjectName("pushButton")
MainWindow.setCentralWidget(self.centralwidget)
self.menubar = QtWidgets.QMenuBar(MainWindow)
self.menubar.setGeometry(QtCore.QRect(0, 0, 260, 21))
self.menubar.setObjectName("menubar")
MainWindow.setMenuBar(self.menubar)
self.statusbar = QtWidgets.QStatusBar(MainWindow)
self.statusbar.setObjectName("statusbar")
MainWindow.setStatusBar(self.statusbar)
  self.retranslateUi(MainWindow)
  QtCore.QMetaObject.connectSlotsByName(MainWindow)
def retranslateUi(self, MainWindow):
  _translate = QtCore.QCoreApplication.translate
  MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
  self.pushButton.setText(_translate("MainWindow", "PushButton"))

class Ui_MainWindow(object):
def **init**(self):
self.nextWindow = Ui_MainWindow2()

def setupUi(self, MainWindow):
  MainWindow.setObjectName("MainWindow")
  MainWindow.resize(260, 226)
  self.centralwidget = QtWidgets.QWidget(MainWindow)
  self.centralwidget.setObjectName("centralwidget")
  self.pushButton = QtWidgets.QPushButton(self.centralwidget)
  self.pushButton.setGeometry(QtCore.QRect(90, 120, 75, 23))
  self.pushButton.setObjectName("pushButton")
  MainWindow.setCentralWidget(self.centralwidget)
  self.menubar = QtWidgets.QMenuBar(MainWindow)
  self.menubar.setGeometry(QtCore.QRect(0, 0, 260, 21))
  self.menubar.setObjectName("menubar")
  MainWindow.setMenuBar(self.menubar)
  self.statusbar = QtWidgets.QStatusBar(MainWindow)
  self.statusbar.setObjectName("statusbar")
  MainWindow.setStatusBar(self.statusbar)
  self.retranslateUi(MainWindow)
  QtCore.QMetaObject.connectSlotsByName(MainWindow)
def retranslateUi(self, MainWindow):
  _translate = QtCore.QCoreApplication.translate
  MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
  self.pushButton.setText(_translate("MainWindow", "PushButton"))
  self.pushButton.clicked.connect(self.launcher)
def launcher(self):
  self.nextWindow.show()

if **name** == "**main**":
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
-------------------------
martin | 2021-03-01 07:02:26 UTC | #2
First up, it's not a good idea to edit the Python files generated from Qt Designer. They are automatically generated from the UI file: once you change them, you can no longer change your UI in Qt Designer, without re-applying all the changes you have made.
The best way to do this is to import the class from the generated py file into your own code. For example, say you have a file named `main.py` which imports your `Ui_MainWindow2` like follows (you'll need to change the from import to your own filename).

```

from mainwindow import Ui_MainWindow2
python ```

You can then create a window the same way as you have at the bottom of your file

```

ui = Ui_MainWindow() ui.setupUi(MainWindow) MainWindow.show() sys.exit(app.exec_())
python ```

To add custom behaviour onto your window class you need to subclass it. For example

```

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow): def **init**(self, *args, **kwargs): super().**init**(*args, **kwargs) self.setupUi(self)
window = MyMainWindow() window.show() sys.exit(app.exec_())
python ```

You can add any custom behaviour in this subclass definition. So for example, to add your clicked handler, you could do.

```

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow): def **init**(self, *args, **kwargs): super().**init**(*args, **kwargs) self.setupUi(self)
python ```
  set.pushButton.clicked.connect(self.launcher)

```

def launcher(self): self.nextWindow = QtWidgets.QMainWindow()
window = MyMainWindow() window.show() sys.exit(app.exec_())
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
python ```

If you want to create an identical second window (I wouldn't recommend this for a real app, but...)

```

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow): def **init**(self, *args, **kwargs): super().**init**(*args, **kwargs) self.setupUi(self)
python ```
  set.pushButton.clicked.connect(self.launcher)

```

def launcher(self): self.nextWindow = MyMainWindow2() self.nextWinodw.show()
class MyMainWindow2(QtWidgets.QMainWindow, Ui_MainWindow): def **init**(self, *args, **kwargs): super().**init**(*args, **kwargs) self.setupUi(self)
window = MyMainWindow() window.show() sys.exit(app.exec_()) ```
I think this [introduction to using Qt Designer UIs will be useful](https://www.pythonguis.com/tutorials/first-steps-qt-creator/) as it has a few other options for using your UI files.
yilmazbah10043 | 2021-02-23 13:56:22 UTC | #3
IT'S WORKING!!! Thank you too much.
from PyQt5 import QtWidgets import sys
app = QtWidgets.QApplication(sys.argv)
from mainWindow import Ui_MainWindow
class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow): **___ def **init__(self, *args, **kwargs):**___****_super()._ _init**(*args, **kwargs) **___****_self.nextWindow = MyMainWindow2() #PCYCHARM offered to sent_** init__ **___** ___self.setupUi(self)
**___** ___self.pushButton.clicked.connect(self.launcher)
**___ def launcher(self): ****___** _ self.nextWindow.show()
class MyMainWindow2(QtWidgets.QMainWindow, Ui_MainWindow): **___ def **init__(self, *args, **kwargs):**___****_super()._ _init**(*args, **kwargs) **___** ___self.setupUi(self)
window = MyMainWindow() window.show() sys.exit(app.exec_()) 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Creating new windows on Qtdesigner based .py files** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/creating-new-windows-on-qtdesigner-based-py-files/Python books) on the subject. 
**Creating new windows on Qtdesigner based .py files** was published in [faq](https://www.pythonguis.com/faq/) on February 21, 2021 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
