# Content from: https://www.pythonguis.com/faq/image-viewer-using-qt-model-view-architecture/

[](https://www.pythonguis.com/faq/image-viewer-using-qt-model-view-architecture/#menu)
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
# Image viewer using Qt Model View architecture
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PySide2 [ FAQ ](https://www.pythonguis.com/faq/)
fjp | 2020-12-07 09:14:44 UTC | #1
Hi, I followed this https://www.pythonguis.com/tutorials/modelview-architecture/ tutorial, and I am trying to display an image depending on the currently selected image path from the QTableView.
I think a possible approach is to create a custom QAbstractItemView to display the currently selected image.
The `ImageModel` and main window class (in `image_app.py`) look like this
python ```
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QFileDialog
from PySide2.QtCore import Qt
from MainWindow import Ui_MainWindow
class ImageModel(QtCore.QAbstractListModel):
  def __init__(self, images=None):
    super().__init__()
    self.images = images or []
  def data(self, index, role):
    if role == Qt.DisplayRole:
      _, text = self.images[index.row()]
      return text
  def rowCount(self, index):
    return len(self.images)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.model = ImageModel()
    self.tableView.setModel(self.model)
    self.imageView.setModel(self.model)
    self.tableView.selectionModel().selectionChanged.connect(self.imageView.selectionChanged)
    self.actionImport.triggered.connect(self.onImportImageClicked)

  def onImportImageClicked(self, s):
    self.open_file()
  def open_file(self):
    filename, _ = QFileDialog.getOpenFileName(
      self,
      "Open file",
      "",
      "Ok Image (*.png *.jpg *.bmp *.jpeg);;" "All files(*.*)",
    )
    if filename:
      self.add(filename)
  def add(self, image_filename):
    # Access the list via the model.
    self.model.images.append((False, image_filename))
    # Trigger refresh.
    self.model.layoutChanged.emit()

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  window = MainWindow()
  window.show()
  app.exec_()

```

And my custom QAbstractItemView should display the image using a QLabel (defined in `image_view.py`):
python ```
class ImageView(QtWidgets.QLabel, QtWidgets.QAbstractItemView):
  def __init__(self, parent) -> None:
    print(parent)
    QtWidgets.QLabel.__init__(self, parent)
    QtWidgets.QAbstractItemView.__init__(self, parent)
    #super().__init__()
    #self.label = QtWidgets.QLabel()
  def selectionChanged(self, selected, deselected):
    print("selectionChanged", type(selected))
    indexes = selected.indexes()
    print(indexes)
    if not indexes:
      return
    image_filename = self.model().data(indexes[0], Qt.DisplayRole)
    print(image_filename)
    pixmap = QtGui.QPixmap(image_filename).scaled(128, 128, QtCore.Qt.KeepAspectRatio)
    self.setPixmap(pixmap)

```

The GUI is designed with Qt Designer and looks like this
[![enter image description here](https://i.stack.imgur.com/mD9E8.png)](https://i.stack.imgur.com/mD9E8.png)
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
I have promoted a QWidget in the Input tab to the `ImageView` class in the `image_view.py`
It can display images when one is selected from the QTableListView, but after I run the MainWindow I get this console output:
python ```
<PySide2.QtWidgets.QWidget(0x7f8cd002cad0, name="tabInput") at 0x7f8ceaebc980>
QObject::connect: No such slot ImageView::_q_modelDestroyed()
QObject::connect: No such slot ImageView::dataChanged(QModelIndex,QModelIndex,QVector<int>)
QObject::connect: No such slot ImageView::_q_headerDataChanged()
QObject::connect: No such slot ImageView::rowsInserted(QModelIndex,int,int)
QObject::connect: No such slot ImageView::_q_rowsInserted(QModelIndex,int,int)
QObject::connect: No such slot ImageView::rowsAboutToBeRemoved(QModelIndex,int,int)
QObject::connect: No such slot ImageView::_q_rowsRemoved(QModelIndex,int,int)
QObject::connect: No such slot ImageView::_q_rowsMoved(QModelIndex,int,int,QModelIndex,int)
QObject::connect: No such slot ImageView::_q_columnsAboutToBeRemoved(QModelIndex,int,int)
QObject::connect: No such slot ImageView::_q_columnsRemoved(QModelIndex,int,int)
QObject::connect: No such slot ImageView::_q_columnsInserted(QModelIndex,int,int)
QObject::connect: No such slot ImageView::_q_columnsMoved(QModelIndex,int,int,QModelIndex,int)
QObject::connect: No such slot ImageView::reset()
QObject::connect: No such slot ImageView::_q_layoutChanged()
QObject::connect: No such slot ImageView::selectionChanged(QItemSelection,QItemSelection)
QObject::connect: No such slot ImageView::currentChanged(QModelIndex,QModelIndex)
selectionChanged <class 'PySide2.QtCore.QItemSelection'>
[]
selectionChanged <class 'PySide2.QtCore.QItemSelection'>
[<PySide2.QtCore.QModelIndex(0,0,0x0,TodoModel(0x1b10c90)) at 0x7f8ceaec24c0>]
/home/fjp/Pictures/motor.png

```

It seems also that the QLabel is displayed above the pixmap and when I click it, the app crashes: 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
python ```
[1]  150858 segmentation fault (core dumped) python image_app.py

```

How to avoid these warnings and crashing the app? Whats the correct way to display an image with the currently selected file name in the QTableView? Should I avoid the QAbstractItemView and just use a QLabel to update its pixmap when the selection changes?
**Edit**
Here is the pyside2 generated gui `MainWindow.py`, used in `image_app.py` to better reproduce this issue: 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyside2-book/) _by Martin Fitzpatrick_ — (PySide2 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside2-book/) [Get the book](https://secure.pythonguis.com/01hf778jyaajk5vk1q6824sd44/)
python ```
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from image_view import ImageView

class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    if not MainWindow.objectName():
      MainWindow.setObjectName(u"MainWindow")
    MainWindow.resize(800, 600)
    self.actionImport = QAction(MainWindow)
    self.actionImport.setObjectName(u"actionImport")
    self.centralwidget = QWidget(MainWindow)
    self.centralwidget.setObjectName(u"centralwidget")
    self.verticalLayout = QVBoxLayout(self.centralwidget)
    self.verticalLayout.setObjectName(u"verticalLayout")
    self.splitter = QSplitter(self.centralwidget)
    self.splitter.setObjectName(u"splitter")
    self.splitter.setOrientation(Qt.Vertical)
    self.tabWidget = QTabWidget(self.splitter)
    self.tabWidget.setObjectName(u"tabWidget")
    self.tabInput = QWidget()
    self.tabInput.setObjectName(u"tabInput")
    self.verticalLayout_2 = QVBoxLayout(self.tabInput)
    self.verticalLayout_2.setObjectName(u"verticalLayout_2")
    self.imageView = ImageView(self.tabInput)
    self.imageView.setObjectName(u"imageView")
    self.verticalLayout_2.addWidget(self.imageView)
    self.tabWidget.addTab(self.tabInput, "")
    self.splitter.addWidget(self.tabWidget)
    self.tableView = QTableView(self.splitter)
    self.tableView.setObjectName(u"tableView")
    self.splitter.addWidget(self.tableView)
    self.verticalLayout.addWidget(self.splitter)
    MainWindow.setCentralWidget(self.centralwidget)
    self.menubar = QMenuBar(MainWindow)
    self.menubar.setObjectName(u"menubar")
    self.menubar.setGeometry(QRect(0, 0, 800, 22))
    self.menuFile = QMenu(self.menubar)
    self.menuFile.setObjectName(u"menuFile")
    MainWindow.setMenuBar(self.menubar)
    self.statusbar = QStatusBar(MainWindow)
    self.statusbar.setObjectName(u"statusbar")
    MainWindow.setStatusBar(self.statusbar)
    self.menubar.addAction(self.menuFile.menuAction())
    self.menuFile.addAction(self.actionImport)
    self.retranslateUi(MainWindow)
    self.tabWidget.setCurrentIndex(0)
    QMetaObject.connectSlotsByName(MainWindow)
  # setupUi
  def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInput), QCoreApplication.translate("MainWindow", u"Input", None))
    self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
  # retranslateUi

```

Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Image viewer using Qt Model View architecture** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/image-viewer-using-qt-model-view-architecture/Python books) on the subject. 
**Image viewer using Qt Model View architecture** was published in [faq](https://www.pythonguis.com/faq/) on December 07, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyside2](https://www.pythonguis.com/topics/pyside2/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
