# Content from: https://www.pythonguis.com/faq/gui-freezing-for-second-run/

[](https://www.pythonguis.com/faq/gui-freezing-for-second-run/#menu)
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
# GUI freezing for second run
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Ganesh_Gupta | 2021-05-30 15:35:33 UTC | #1
I am creating a GUI which use external Python script function with parramters for calcualtion and updating progressbar.I had used multithreading.It works fine for first run but if I change dropdown and lineedit parameter and click again on calculate button it does not respose. I have three level dropdown on basis of that we select python script for running function by using csv sheet for calcualtion. GUI image is attached [GUI image for calcuation][1] ![software|690x118](https://www.pythonguis.com/static/faq/forum/gui-freezing-for-second-run/aac1bDHBxuhrcwOXGE1WH1fpWk5.png)
This is My code
python ```
import sys
import os
from decimal import Decimal
import time
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from pathlib import Path
from CONNECTDATABASE import*
from RB import*
from UPDATEDATABASEthread import*
import subprocess
from urllib.request import urlopen
qtCreatorFile = "SMOG_COLASCE_DEVELOPER_INTERFACE1.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class Worker(QObject):
  hashed = pyqtSignal(str)
  signal=pyqtSignal(int)
  finished = pyqtSignal()
  @pyqtSlot(str,str,str,str,str,str)
  def cal_functions(self,filter,filter1,IND,OTD,Version,Year):
    if filter=='RB':
      if filter1 =='None':
        x=ARBthread(self,IND,OTD,Version,Year)
        self.hashed.emit(x)
    self.finished.emit()
class Worker1(QObject)  :
  def __init__(self):
    super().__init__()
  hashed1 = pyqtSignal(str)
  signal=pyqtSignal(int)
  finished = pyqtSignal()
  @pyqtSlot(str,str,str,str,str,str,str,str,str)
  def update_database(self,hostname,port,username,password,Database_Name,IND,OTD,Version,Year):
    x1=UPDATEDATABASEthread(self,hostname,port,username,password,Database_Name,IND,OTD,Version,Year)
    self.hashed1.emit(x1)
    self.finished.emit()
class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  cal_requested = pyqtSignal(str,str,str,str,str,str)
  data_requested= pyqtSignal(str,str,str,str,str,str,str,str,str)
  def __init__(self):
    QtWidgets.QMainWindow.__init__(self)
    Ui_MainWindow.__init__(self)
    self.setupUi(self)
    self.setWindowTitle("SMoG-India COALESCE")
    self.Sector.currentIndexChanged.connect(self.comboBox_sector_change)
self.SubSectorLevel1.currentIndexChanged.connect(self.comboBox_subsector_change)
    self.Calculate.clicked.connect(self.calc)
    self.toolButton.clicked.connect(self._open_file_dialog)
    self.toolButton_2.clicked.connect(self._open_file_dialog1)
    self.toolButton_3.clicked.connect(self._open_file_dialog2)
    self.checkBox_2.stateChanged.connect(self.checkedcLS)
    self.checkBox_3.stateChanged.connect(self.checkedcRS)
    self.pushButton_3.clicked.connect(self.Database)
    self.pushButton_4.clicked.connect(self.ConnectDatabase)
    self.lineEdit_5.setReadOnly(True)
    self.lineEdit_6.setReadOnly(True)
    self.lineEdit_7.setReadOnly(True)
    self.lineEdit_8.setReadOnly(True)
    self.lineEdit_9.setReadOnly(True)
    self.pushButton_2.clicked.connect(self.close_event)
    self.pushButton.clicked.connect(self.open_tutorial)
    # Create a worker object and a thread
    self.worker = Worker()
    self.worker_thread = QThread()
    self.worker.hashed.connect(self.messagebox)
    self.worker.signal.connect(self.update_progress_bar)
    self.cal_requested.connect(self.worker.cal_functions)
    self.worker.moveToThread(self.worker_thread)
    self.worker.finished.connect(self.worker_thread.quit)
    self.worker.finished.connect(self.worker.deleteLater)
    self.worker_thread.start()
    self.worker_thread.finished.connect(self.finish)
    self.worker1 = Worker1()
    self.worker1_thread = QThread()
    self.worker1.hashed1.connect(self.messagebox)
    self.worker1.signal.connect(self.update_progress_bar)
    self.worker1.moveToThread(self.worker1_thread)
    self.data_requested.connect(self.worker1.update_database)
    self.worker1.finished.connect(self.worker1_thread.quit)
    self.worker1.finished.connect(self.worker1.deleteLater)
    self.worker1_thread.finished.connect(self.worker1_thread.deleteLater)
    self.worker1_thread.start()
    self.worker1_thread.finished.connect(self.finish)
  def calc(self):
    progressBar = self.progressBar
    self.Calculate.setEnabled(False)
    self.SubSectorLevel1.setEnabled(False)
    self.SubSectorLevel2.setEnabled(False)
    self.Sector.setEnabled(False)
    self.toolButton_2.setEnabled(False)
    self.toolButton_3.setEnabled(False)
    self.lineEdit_10.setReadOnly(True)
    self.lineEdit_4.setReadOnly(True)
    self.toolButton_2.setEnabled(False)
    self.toolButton_3.setEnabled(False)
    filter = self.SubSectorLevel1.currentText()
    filter1 = self.SubSectorLevel2.currentText()
    IND = self.lineEdit.text()
    OTD = self.lineEdit_2.text()
    Version= self.lineEdit_10.text()
    Year=self.lineEdit_4.text()
    self.cal_requested.emit(filter,filter1,IND,OTD,Version,Year)

```

``` if **name** == "**main** ": global app app = QtWidgets.QApplication.instance() if app is None: app = QtWidgets.QApplication(sys.argv) window = MyWindow() window.show() sys.exit(app.exec_())
It will be Great if you help in this
stelaldridge11281 | 2021-06-07 15:01:08 UTC | #2
Hi Ganesh, 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Did you find a solution already or it is still unsolved? 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**GUI freezing for second run** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/gui-freezing-for-second-run/Python books) on the subject. 
**GUI freezing for second run** was published in [faq](https://www.pythonguis.com/faq/) on May 30, 2021 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [multithreading](https://www.pythonguis.com/topics/multithreading/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
