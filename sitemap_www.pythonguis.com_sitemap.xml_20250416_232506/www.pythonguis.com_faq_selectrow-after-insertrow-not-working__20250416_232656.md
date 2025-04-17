# Content from: https://www.pythonguis.com/faq/selectrow-after-insertrow-not-working/

[](https://www.pythonguis.com/faq/selectrow-after-insertrow-not-working/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
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
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# selectRow after insertRow not working
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ FAQ ](https://www.pythonguis.com/faq/)
allenwjohnson11084 | 2021-05-14 14:39:58 UTC | #1
I am new to PyQt and having to really dig to understand how the objects fit together. I am probably overlooking some basic things at this point. I have started building my application, but keep tripping into things that don't work the way I want. Please be understanding if I am missing basic concepts. Doing this as retirement project, no longer being paid to code. The problem is that I want to add a row to a tableView and have it selected. This code is extracted from a more complex environment. What am I doing wrong?
python ```
import sys
from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
"""
  Model: based on QAbstractTableModel
  View: QTable view
  data: simple table of integers (3 columns)
  Implemented insert and remove row methods.
    I want an inserted table row to be selected
  Problem: selectRow after insert of table row works only
    if I have just deleted the next to last entry in the table
"""
# Model +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class TableModel(qtc.QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
  def data(self, index, role):
    if role == qtc.Qt.DisplayRole:
      value = self._data[index.row()][index.column()]
      return str(value)
  def setData(self, index, value, role):
    if role == qtc.Qt.EditRole:
      self._data[index.row()][index.column()] = value
      return True
  def rowCount(self, index):
    rows = len(self._data)
    return rows
  def columnCount(self, index):
    cols = len(self._data[0])
    return cols
  def flags(self, index):
    flags = qtc.Qt.ItemIsSelectable|qtc.Qt.ItemIsEnabled|qtc.Qt.ItemIsEditable
    return flags
  def removeRow(self, row):
    self.rowsAboutToBeRemoved.emit(qtc.QModelIndex(), row, row)
    self._data.pop(row)
    self.rowsRemoved.emit(qtc.QModelIndex(), row, row)
  def insertRow(self, data)->int:
    row = len(self._data) + 1
    self.rowsAboutToBeInserted.emit(qtc.QModelIndex(), row, row)
    self._data.append(data)
    self.rowsInserted.emit(qtc.QModelIndex(), row, row)
    return row
# end class TableModel
class MainWindow(qtw.QMainWindow):
  def __init__(self):
    super().__init__()
    self.setMinimumSize(qtc.QSize(350, 200))
    self.cIndex = None   # current selection
    self.pIndex = None   # previous selection
    self.rowData = 10    # for generated adds
    self.sm = None     # selection model
    # view +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    self.table = qtw.QTableView()
    self.table.setSelectionMode(qtw.QAbstractItemView.SingleSelection)
    self.table.setSelectionBehavior(qtw.QAbstractItemView.SelectRows)
    # model +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    data = [ [1, 9, 2] ]  # start with 1 row
    self.model = TableModel(data)
    self.table.setModel(self.model)
    sm = self.table.selectionModel()
    sm.currentRowChanged.connect(self.currentRowChanged)
    self.sm = sm
    # buttons ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    buttons = qtw.QHBoxLayout()
    self.pbAdd = qtw.QPushButton('Add')
    self.pbDelete = qtw.QPushButton('Delete')
    self.pbAdd.clicked.connect(self.pbAddClicked)
    self.pbDelete.clicked.connect(self.pbDeleteClicked)
    # layout ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    vBox = qtw.QVBoxLayout()
    vBox.addWidget(self.table)
    buttons.addWidget(self.pbAdd)
    buttons.addWidget(self.pbDelete)
    vBox.addLayout(buttons)
    # complete main window
    self.widget = qtw.QWidget()
    self.widget.setLayout(vBox)
    self.setCentralWidget(self.widget)
    self.show()
  def currentRowChanged(self, cIndex, pIndex):
    self.cIndex = cIndex
    self.pIndex = pIndex
  # add row
  def pbAddClicked(self):
    col = self.rowData
    data = [col, col+1, col+2]
    self.rowData += 10
    row = self.model.insertRow(data)
    # select the inserted row
    # *** this only works when the next to last entry has been deleted ???
    self.table.selectRow(row)
  # remove row
  def pbDeleteClicked(self):
    row = self.cIndex.row()
    self.model.removeRow(row)
# end class MainWindow
app=qtw.QApplication([])
window=MainWindow()
app.exec_()

```

allenwjohnson11084 | 2021-05-19 07:06:37 UTC | #2
I found my own very basic problem. It wasn't related to the interaction between the view, selection model and model. Which thanks to my problem and hours spent looking at the documentation and drawing diagrams I now understand much better. I was using an invalid index for my selectRow call. I would expect an error, but apparently the call is just ignored. No additional responses are needed.
martin | 2021-05-19 11:55:24 UTC | #3
Thanks for the update @allenwjohnson11084 glad you got it sorted!
When you say invalid index, was the index out of bounds or was `index.isValid()` returning `False`? There are quite a few methods that will return an "invalid index" if something isn't there, but it's not considered an error -- e.g. the parent of a top-level item in a tree will return an invalid parent index. In a lot of cases you can consider it the model equivalent of Python's `None` -- a valid empty value.
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
Not sure if it's relevant to the issue but when overriding methods on your subclass you should follow the same signature as the superclass, e.g. `insertRow` should accept both the data and the location to insert it, and return a `bool` for success/failure, rather than the index.
python ```
insertRow(int row, const QModelIndex &parent = QModelIndex())

```

Since selections are handled by the view, and inserts on the model, to do what you're trying to achieve (auto select inserted rows) I'd probably use the model `.rowsInserted` and hook that into the selection model for the table view.
P.S. Apologies for the delay in replying I'm out of office (house being renovated) so checking in less frequently for the next 2 weeks.
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**selectRow after insertRow not working** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/selectrow-after-insertrow-not-working/Python books) on the subject. 
**selectRow after insertRow not working** was published in [faq](https://www.pythonguis.com/faq/) on May 13, 2021 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
