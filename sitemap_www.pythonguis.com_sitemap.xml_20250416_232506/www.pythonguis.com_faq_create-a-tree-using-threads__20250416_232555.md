# Content from: https://www.pythonguis.com/faq/create-a-tree-using-threads/

[](https://www.pythonguis.com/faq/create-a-tree-using-threads/#menu)
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
# Create a tree using threads
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PySide6 [ FAQ ](https://www.pythonguis.com/faq/)
GiUnZ | 2021-06-27 18:56:12 UTC | #1
I am trying to create an application that will be getting data through an API and present them in QTreeView, using PySide6. As it takes a long time to get the data I want to retrieve them using a QThread. My example code is the following: import logging import time
python ```
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
logging.basicConfig(
  format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
  level=logging.INFO)
class MainWindow(QMainWindow):
  gettingData = False
  counting = False

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.counter = 0
    layout = QVBoxLayout()

    self.b = QPushButton("Start Counting with a Thread")
    self.bt1 = QPushButton("Generate tree with Thread")
    self.bt2 = QPushButton("Generate tree without a Thread")
    self.tree = QTreeView()
    layout.addWidget(self.b)
    layout.addWidget(self.bt1)
    layout.addWidget(self.bt2)
    layout.addWidget(self.tree)
    self.b.clicked.connect(self.startCounting)
    self.bt1.clicked.connect(self.startGenerating)
    self.bt2.clicked.connect(self.startGenerating2)
    w = QWidget()
    w.setLayout(layout)
    self.setCentralWidget(w)
    self.show()
    self.threadpool = QThreadPool()
    print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
  def startCounting(self):
    thread = Thread(self.counting)
    thread.signal.signal.connect(self.something)
    self.threadpool.start(thread)
  def something(self, signal):
    if signal == "False":
      logging.info("Counting is Complete")
    else:
      logging.info(signal)
  def startGenerating(self):
    thread = DataThread()
    thread.signals.signal_QStandardItemModel(self.treeAction)
    self.threadpool.start(thread)
  def treeAction(self,signal):
    self.tree.setModel(signal)
  def startGenerating2(self):
    start = time.perf_counter()
    siteTreeViewModel = QStandardItemModel()
    rootNode = siteTreeViewModel.invisibleRootItem()
    aItem = TreeStandardItem("A")
    bItem = TreeStandardItem("B")
    cItem = TreeStandardItem("C")
    rootNode.appendRow(aItem)
    time.sleep(3)
    rootNode.appendRow(bItem)
    time.sleep(3)
    bItem.appendRow(cItem)
    self.tree.setModel(siteTreeViewModel)
    end = time.perf_counter() - start
    logging.info("Generated tree in "+str(end))

class Thread(QRunnable):
  def __init__(self, counting):
    super().__init__()
    self.counting = counting
    self.signal = Signal()
  def run(self):
    for x in range(10):
      self.signal.signal.emit(str(x))
      time.sleep(.1)
    counting = False
    self.signal.signal.emit(str(counting))
class Signal(QObject):
  signal = Signal(str)
class DataThread(QRunnable):
  def __init__(self):
    super().__init__()
    self.signals = WorkerSignals()
  def run(self):
    logging.info("Start generating the tree")
    start = time.perf_counter()
    siteTreeViewModel = QStandardItemModel()
    rootNode = siteTreeViewModel.invisibleRootItem()
    aItem = TreeStandardItem("A")
    bItem = TreeStandardItem("B")
    cItem = TreeStandardItem("C")
    rootNode.appendRow(aItem)
    time.sleep(2)
    rootNode.appendRow(bItem)
    time.sleep(2)
    bItem.appendRow(cItem)
    end = time.perf_counter() - start
    self.signals.signal_QStandardItemModel.emit(siteTreeViewModel)
    logging.info("Generated tree in "+str(end))
    self.signals.finished.emit()
class TreeStandardItem(QStandardItem):
  def __init__(self, txt=''):
    super().__init__()
    self.setEditable = False
    self.setForeground(QColor(255, 255, 255))
    self.setText(txt)
class WorkerSignals(QObject):
  signal_QStandardItemModel = Signal()
  finished = Signal()
app = QApplication([])
window = MainWindow()
app.exec()

```

The first counting button works as expected creating a thread. Generating the tree without a thread, confirms that the code I am trying to run using a thread is working Once I try running the tree generation using thread, I get the following error:
python ```
Traceback (most recent call last):
 File "/home/giunz/code/tutorial/threaded-tree-01.py", line 61, in startGenerating
  thread.signals.signal_QStandardItemModel(self.treeAction)
TypeError: 'Signal' object is not callable

```

Any help on how to generate the tree using a thread, would be appreciated.
Thanks in advance
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Create a tree using threads** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/create-a-tree-using-threads/Python books) on the subject. 
**Create a tree using threads** was published in [faq](https://www.pythonguis.com/faq/) on June 27, 2021 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyside6](https://www.pythonguis.com/topics/pyside6/) [threading](https://www.pythonguis.com/topics/threading/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
