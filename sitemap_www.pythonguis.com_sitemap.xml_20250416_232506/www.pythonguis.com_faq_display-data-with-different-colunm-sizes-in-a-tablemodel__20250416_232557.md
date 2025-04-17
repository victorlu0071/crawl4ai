# Content from: https://www.pythonguis.com/faq/display-data-with-different-colunm-sizes-in-a-tablemodel/

[](https://www.pythonguis.com/faq/display-data-with-different-colunm-sizes-in-a-tablemodel/#menu)
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
# Display data with different colunm sizes in a TableModel?
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
ushu | 2021-04-28 20:15:55 UTC | #1
Hi, first thank for this book and clear examples, I learnt a lot!
I try to code a window to load data from a *txt file and preview it into a TableView (after to select, using combobox, some row and column as headers containing data on which to perform analyses).
How to display into the example of TableView from your TableModel you provide p.295 a table that has some row and column of different sizes / number of elements?
What I naively tried: 1- calculate the max number of columns in the file, then send to columnCount this max number for every column 2- and add a test if element is void, and return a string with a space or another char
But it doesn't work, and I don't understand how this Tablemodel works to succeed. I think solution is in indexing row and column but still don't understand how this class does that?
python ```
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDir
class TableModel(QtCore.QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
    self.maxcolumn = max([len(i) for i in self._data])
  def data(self, index, role):
    if role == Qt.TextAlignmentRole:
      return Qt.AlignCenter
    if role == Qt.DisplayRole:
      if not self._data[index.row()][index.column()]:
        print("sad!")
        return " "
      else:
        value = self._data[index.row()][index.column()]
        if isinstance(value, float):
          return "%.2f" % value
      return value
  def rowCount(self, index):
    return len(self._data)
  def columnCount(self, index):
    return self.maxcolumn

class MainWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.data1 = []
    self.button = QPushButton('Upload data')
    self.button.clicked.connect(self.get_text_file)
    self.table = QtWidgets.QTableView()
    layout = QVBoxLayout()
    layout.addWidget(self.table)
    layout.addWidget(self.button)
    self.setLayout(layout)
  def get_text_file(self):
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.AnyFile)
    dialog.setFilter(QDir.Files)
    if dialog.exec_():
      file_name = dialog.selectedFiles()
      if file_name[0].endswith('.txt'):
        with open(file_name[0], 'r') as f:
          self.data1 = f.readlines()
          for x in range(len(self.data1)) :
              a = self.data1[x]
              b = a.split()
              self.data1[x] = b
          self.model = TableModel(self.data1)
          self.table.setModel(self.model)
          f.close()
      else:
        pass

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

```

ushu | 2021-04-29 10:14:56 UTC | #2 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
ok, I solved my problem by creating a dataview, adding empty string to row with less column than maxcolumn, abnd send this dataview to TableModel.
Here is the code above with modifications
python ```
  import sys, copy
  from PyQt5 import QtCore, QtGui, QtWidgets
  from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout)
  from PyQt5.QtCore import Qt
  from PyQt5.QtCore import QDir
  class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
      super().__init__()
      self._data = data
    def data(self, index, role):
      if role == Qt.TextAlignmentRole:
        return Qt.AlignCenter
      if role == Qt.DisplayRole:
        return self._data[index.row()][index.column()]
    def rowCount(self, index):
      return len(self._data)
    def columnCount(self, index):
      return len(self._data[0])

  class MainWindow(QWidget):
    def __init__(self):
      super().__init__()
      self.data1 = []
      self.dataview = []
      self.button = QPushButton('Upload data')
      self.button.clicked.connect(self.get_text_file)
      self.table = QtWidgets.QTableView()
      layout = QVBoxLayout()
      layout.addWidget(self.table)
      layout.addWidget(self.button)
      self.setLayout(layout)
    def get_text_file(self):
      dialog = QFileDialog()
      dialog.setFileMode(QFileDialog.AnyFile)
      dialog.setFilter(QDir.Files)
      if dialog.exec_():
        file_name = dialog.selectedFiles()
        if file_name[0].endswith('.txt'):
          with open(file_name[0], 'r') as f:
            self.data1 = f.readlines()
            for x in range(len(self.data1)) :
                a = self.data1[x]
                b = a.split()
                self.data1[x] = b
            self.maxcolumn = max([len(i) for i in self.data1]) # compute maximum number of column
            self.dataview = copy.deepcopy(self.data1) # create a drtaview for TableModel
            for i,x in enumerate(self.dataview) :
              index=len(x)
              while index < self.maxcolumn:
                x.append(' ') # add a empty/space string to row with less column than maxcolumn
                index+=1
              self.dataview[i] = x
            self.model = TableModel(self.dataview) # send self.dataview to Tablemodel rather than data with different number of columns
            self.table.setModel(self.model)
            f.close()
        else:
          pass

  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

```

martin | 2021-04-29 10:27:10 UTC | #3
Hi @ushu welcome to the forum! Nice work on finding the solution -- what you've done is fine. In case it's helpful, I'll explain a bit more what's happening.
The table model is designed around the assumption that a table of data has a consistent number of columns and rows -- that is, every row has the same number of columns (and vice versa). When you specify the `rowCount` and `columnCount` these are taken to apply to _all_ columns and rows respectively.
If you have a data table where some rows are shorter than others, Qt will still request data for those missing columns, by passing an index into the `data` method. If you take that index and try do a lookup into your Python lists, it will fail with an index error because it is out of bounds.
In your code below, I think you're trying to check the existence of a column using `if not self._data[index.row()][index.column()]:` -- however, that is _still_ attempting to index using the values. The `not` only comes into effect _after_ the value is returned from the list, and that will fail.
python ```
  def data(self, index, role):
    if role == Qt.DisplayRole:
      if not self._data[index.row()][index.column()]:
        print("sad!")
        return " "
      else:
        value = self._data[index.row()][index.column()]
        if isinstance(value, float):
          return "%.2f" % value

```

Indexing beyond the end of a list throws an `IndexError`
python ```
>>> a = [1,2,3]
>>> a[4]
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
IndexError: list index out of range

```

So what we can do instead, is catch that `IndexError` and then return an empty string, e.g.
python ```
  def data(self, index, role):
    if role == Qt.DisplayRole:
      try:
        value = self._data[index.row()][index.column()]
      except IndexError:
        return "" # invalid index, return empty string
      # Value was found, return it formatted.
      if isinstance(value, float):
        return "%.2f" % value

```

This should give the same result you have now, but without needing to modify the loaded data. You can also use this trick to highlight cells in the table a certain way, e.g. shade missing cells grey.
ushu | 2021-04-29 10:53:50 UTC | #4 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Thank you for your answer and explanations, more elegant method indeed.
I would love to find a more develop part about Table widget in your book (for a next version or a small additional DLC? ;) ): how to change background color of a row or a column or a header, how to manipulate row/column headers, if possible, how to allow user editing values within a Table widget, linking values from a row to a combobox .. and so on.
martin | 2021-04-29 12:36:43 UTC | #5
Here's a small example of setting header styles on a tableview based off the examples on the site. You just need to implement a `headerData` method which responds to calls with index (int) orientation (horizontal or vertical, for top and left headers respectively) and the role, which work the same as in `data`.
There is a gotcha though -- you cannot set the background using `Qt.BackgroundRole` on all platforms. On Windows it has no effect. You can get around this by using a cross-platform style, although this means your applications won't look native -- in the example below I do this using `app.setStyle("fusion")`
Changing the text colour and formatting of the numbers, etc. all works as expected.
python ```
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
  def data(self, index, role):
    if role == Qt.DisplayRole:
      # See below for the nested-list data structure.
      # .row() indexes into the outer list,
      # .column() indexes into the sub-list
      return self._data[index.row()][index.column()]
  def headerData(self, index, orientation, role):
    if orientation == Qt.Horizontal:
      if role == Qt.ForegroundRole and index == 1:
        return QtGui.QColor("red")
      if role == Qt.BackgroundRole and index == 0:
        return QtGui.QColor("red")
      if role == Qt.DisplayRole:
        return "%.2f" % index
    if orientation == Qt.Vertical:
      if role == Qt.DisplayRole:
        return index
  def rowCount(self, index):
    # The length of the outer list.
    return len(self._data)
  def columnCount(self, index):
    # The following takes the first sub-list, and returns
    # the length (only works if all rows are an equal length)
    return len(self._data[0])

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.table = QtWidgets.QTableView()
    data = [
      [4, 9, 2],
      [1, 0, 0],
      [3, 5, 0],
      [3, 3, 2],
      [7, 8, 9],
    ]
    self.model = TableModel(data)
    self.table.setModel(self.model)
    self.setCentralWidget(self.table)

app = QtWidgets.QApplication(sys.argv)
app.setStyle("fusion") # without this the BackgroundRole will not work in headers
window = MainWindow()
window.show()
app.exec_()

```

The screenshots below show how it looks in Windows and on Windows with Fusion style.
![headerdatawindows|485x353](https://www.pythonguis.com/static/faq/forum/display-data-with-different-colunm-sizes-in-a-tablemodel/j2DUHIJrPqMXHs2RmrGYUBzRFJP.png)
![headerdatafusion|498x360](https://www.pythonguis.com/static/faq/forum/display-data-with-different-colunm-sizes-in-a-tablemodel/3WyqzJWourY9VOdrc2GslcPmekC.png)
ushu | 2021-04-30 06:19:44 UTC | #6
Thank you again for your nice explanations and this pedagogic code. I learnt so much in few days about pyQt (after spending 2 weeks on tkinter that finished in a dead end for me). Best
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Display data with different colunm sizes in a TableModel?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/display-data-with-different-colunm-sizes-in-a-tablemodel/Python books) on the subject. 
**Display data with different colunm sizes in a TableModel?** was published in [faq](https://www.pythonguis.com/faq/) on April 28, 2021 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
