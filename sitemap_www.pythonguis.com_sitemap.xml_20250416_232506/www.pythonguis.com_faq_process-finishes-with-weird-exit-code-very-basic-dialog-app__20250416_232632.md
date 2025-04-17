# Content from: https://www.pythonguis.com/faq/process-finishes-with-weird-exit-code-very-basic-dialog-app/

[](https://www.pythonguis.com/faq/process-finishes-with-weird-exit-code-very-basic-dialog-app/#menu)
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
# Process finishes with weird exit code (Very basic dialog app)
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
9buzadani6114 | 2020-08-25 06:28:14 UTC | #1
I tried to design a very basic GUI app that shows the entered height on a dialog, but after I press the 'OK' button on the main window, the whole program crashes and the process finishes with this exit code:
> `Process finished with exit code -1073740791 (0xC0000409)`
Here's the full code for the app, the UI files are below:
python ```
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
class My_Dialog(QDialog):
  def __init__(self):
    super().__init__()
    loadUi("dialog.ui", self)
    self.mid_label.setText(My_Window.mid_label_nexttext)
class My_Window(QMainWindow):
  def __init__(self):
    super().__init__()
    loadUi("mainwindow.ui", self)
    self.mid_label_nexttext = None
    self.height_selecter_spinbox.textChanged.connect(lambda x: self.spin_changed(x))
    self.pushButton.clicked.connect(self.onMyPushButtonClick)
  def onMyPushButtonClick(self):
    dlg = My_Dialog()
    if dlg.exec_():
      print("Success!")
    else:
      print("Cancel!")
  def spin_changed(self, s):
    self.mid_label_nexttext = s
    self.update()

def main():
  app = QApplication(sys.argv)
  window = My_Window()
  window.show()
  app.exec_()
if __name__ == "__main__":
  main()

```

The main window's UI:
python ```
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again. Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(513, 171)
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.pushButton = QtWidgets.QPushButton(self.centralwidget)
    self.pushButton.setGeometry(QtCore.QRect(310, 80, 75, 23))
    self.pushButton.setObjectName("pushButton")
    self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
    self.layoutWidget.setGeometry(QtCore.QRect(90, 40, 209, 29))
    self.layoutWidget.setObjectName("layoutWidget")
    self.layout = QtWidgets.QHBoxLayout(self.layoutWidget)
    self.layout.setContentsMargins(0, 0, 0, 0)
    self.layout.setObjectName("layout")
    self.label_firstpart = QtWidgets.QLabel(self.layoutWidget)
    font = QtGui.QFont()
    font.setPointSize(15)
    self.label_firstpart.setFont(font)
    self.label_firstpart.setObjectName("label_firstpart")
    self.layout.addWidget(self.label_firstpart)
    self.height_selecter_spinbox = QtWidgets.QSpinBox(self.layoutWidget)
    font = QtGui.QFont()
    font.setPointSize(13)
    self.height_selecter_spinbox.setFont(font)
    self.height_selecter_spinbox.setMinimum(100)
    self.height_selecter_spinbox.setMaximum(250)
    self.height_selecter_spinbox.setProperty("value", 175)
    self.height_selecter_spinbox.setObjectName("height_selecter_spinbox")
    self.layout.addWidget(self.height_selecter_spinbox)
    self.label_lastpart = QtWidgets.QLabel(self.layoutWidget)
    font = QtGui.QFont()
    font.setPointSize(15)
    self.label_lastpart.setFont(font)
    self.label_lastpart.setObjectName("label_lastpart")
    self.layout.addWidget(self.label_lastpart)
    MainWindow.setCentralWidget(self.centralwidget)
    self.menubar = QtWidgets.QMenuBar(MainWindow)
    self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 21))
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
    self.pushButton.setText(_translate("MainWindow", "OK"))
    self.label_firstpart.setText(_translate("MainWindow", "My height is "))
    self.label_lastpart.setText(_translate("MainWindow", "cm."))

```

The dialog's UI:
python ```
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again. Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
  def setupUi(self, Dialog):
    Dialog.setObjectName("Dialog")
    Dialog.resize(400, 300)
    self.dialog_buttonbox = QtWidgets.QDialogButtonBox(Dialog)
    self.dialog_buttonbox.setGeometry(QtCore.QRect(30, 240, 341, 32))
    self.dialog_buttonbox.setOrientation(QtCore.Qt.Horizontal)
    self.dialog_buttonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
    self.dialog_buttonbox.setObjectName("dialog_buttonbox")
    self.widget = QtWidgets.QWidget(Dialog)
    self.widget.setGeometry(QtCore.QRect(80, 90, 151, 41))
    self.widget.setObjectName("widget")
    self.dialog_layout = QtWidgets.QHBoxLayout(self.widget)
    self.dialog_layout.setContentsMargins(0, 0, 0, 0)
    self.dialog_layout.setObjectName("dialog_layout")
    self.left_label = QtWidgets.QLabel(self.widget)
    font = QtGui.QFont()
    font.setPointSize(12)
    self.left_label.setFont(font)
    self.left_label.setObjectName("left_label")
    self.dialog_layout.addWidget(self.left_label)
    self.mid_label = QtWidgets.QLabel(self.widget)
    font = QtGui.QFont()
    font.setPointSize(12)
    self.mid_label.setFont(font)
    self.mid_label.setObjectName("mid_label")
    self.dialog_layout.addWidget(self.mid_label)
    self.right_label = QtWidgets.QLabel(self.widget)
    font = QtGui.QFont()
    font.setPointSize(12)
    self.right_label.setFont(font)
    self.right_label.setObjectName("right_label")
    self.dialog_layout.addWidget(self.right_label)
    self.retranslateUi(Dialog)
    self.dialog_buttonbox.accepted.connect(Dialog.accept)
    self.dialog_buttonbox.rejected.connect(Dialog.reject)
    QtCore.QMetaObject.connectSlotsByName(Dialog)
  def retranslateUi(self, Dialog):
    _translate = QtCore.QCoreApplication.translate
    Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
    self.left_label.setText(_translate("Dialog", "You are"))
    self.mid_label.setText(_translate("Dialog", "100"))
    self.right_label.setText(_translate("Dialog", "cm tall."))

```

I would appreciate some help on how to fix this error.:slight_smile: 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
Eolinwen | 2020-08-25 17:11:32 UTC | #2
Hi,
At first look, I run into an issue when teh ui file is loading.
python ```
$python superapp.py
Traceback (most recent call last):
 File "superapp.py", line 54, in <module>
  window = My_Window()
 File "superapp.py", line 25, in __init__
  loadUi(ui_file, self)
 File "/usr/lib/python3.8/site-packages/PyQt5/uic/__init__.py", line 238, in loadUi
  return DynamicUILoader(package).loadUi(uifile, baseinstance, resource_suffix)
 File "/usr/lib/python3.8/site-packages/PyQt5/uic/Loader/loader.py", line 66, in loadUi
  return self.parse(filename, resource_suffix)
 File "/usr/lib/python3.8/site-packages/PyQt5/uic/uiparser.py", line 1020, in parse
  document = parse(filename)
 File "/usr/lib/python3.8/xml/etree/ElementTree.py", line 1202, in parse
  tree.parse(source, parser)
 File "/usr/lib/python3.8/xml/etree/ElementTree.py", line 595, in parse
  self._root = parser._parse_whole(source)
xml.etree.ElementTree.ParseError: not well-formed (invalid token): line 1, column 1

```

Did you have all copy correctly ?
I have done that too specifying the loading path. I think that at the same level than yours ui files ?
python ```
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *

class My_Dialog(QDialog):
  def __init__(self):
    super().__init__()
    real_path = "dialog.ui"
    current_dir = os.path.dirname(os.path.realpath(__file__))
    ui_file = os.path.join(current_dir, real_path)
    loadUi(u_file, self)
    self.mid_label.setText(My_Window.mid_label_nexttext)

class My_Window(QMainWindow):
  def __init__(self):
    super().__init__()
    real_path = "mainwindow.ui"
    current_dir = os.path.dirname(os.path.realpath(__file__))
    ui_file = os.path.join(current_dir, real_path)
    loadUi(ui_file, self)
  self.mid_label_nexttext = None
  self.height_selecter_spinbox.textChanged.connect(lambda x: self.spin_changed(x))
  self.pushButton.clicked.connect(self.onMyPushButtonClick)
def onMyPushButtonClick(self):
  dlg = My_Dialog()
  if dlg.exec_():
    print("Success!")
  else:
    print("Cancel!")
def spin_changed(self, s):
  self.mid_label_nexttext = s
  self.update()

# def main():
  # app = QApplication(sys.argv)
  # window = My_Window()
  # window.show()
  # # app.exec_()
  # sys.exit(app.exec_())
if __name__ == "__main__":
  # main()
  app = QApplication(sys.argv)
  window = My_Window()
  window.show()
  # app.exec_()
  sys.exit(app.exec_())

```

9buzadani6114 | 2020-08-26 09:04:35 UTC | #3
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Thanks for your answer, @Eolinwen, I tried it with your version of the code, but still got the same problem. All the files are in the same directory and the copying is also correct.
Eolinwen | 2020-08-27 15:25:15 UTC | #4
I have a bit more free time today than previously. :stuck_out_tongue_winking_eye:
I have tried two or three things without any success.
And this kind of error, is annoying. So, I have tried to open yours files (the both) in Qt Designer (to check if they are okay) and I can not open them. I get this error and confirm what my terminal shout me. They are not very well formatted, something is missing. Look.
[url=http://pix.toile-libre.org/?img=1598546405.png]![](https://www.pythonguis.com/static/faq/forum/process-finishes-with-weird-exit-code-very-basic-dialog-app/oZtBgFRIEsUMhzgKl0cRwNV8IQS.png)[/url] 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Process finishes with weird exit code (Very basic dialog app)** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/process-finishes-with-weird-exit-code-very-basic-dialog-app/Python books) on the subject. 
**Process finishes with weird exit code (Very basic dialog app)** was published in [faq](https://www.pythonguis.com/faq/) on August 24, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
