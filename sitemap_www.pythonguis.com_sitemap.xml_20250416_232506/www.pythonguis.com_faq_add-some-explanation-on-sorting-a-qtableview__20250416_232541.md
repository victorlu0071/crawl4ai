# Content from: https://www.pythonguis.com/faq/add-some-explanation-on-sorting-a-qtableview/

[](https://www.pythonguis.com/faq/add-some-explanation-on-sorting-a-qtableview/#menu)
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
# Add some explanation on sorting a QTableView
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ FAQ ](https://www.pythonguis.com/faq/)
David_Hansson | 2020-05-23 18:52:34 UTC | #1
https://www.pythonguis.com/courses/model-views/qtableview-modelviews-numpy-pandas/
Above is a great tutorial. Best on the internet on the subject. Both the content itself, the language that explain it, and the graphics itself. But I think it avoids some of the more difficult parts of the subject, like sorting and filtering, so it would be even better if you could add some code on how the QAbstractTableModel should be coded and what needs to be set for the QTableView (if needed some subclassing), and settings in Mainwindow class for everything to be non-crashable when sorting and filtering, all expanded on your example of the list of lists data structure of couse.
Keep up the good work. This is perhaps the only understandable and up to date websight on pyqt5 out there, for those that are not professionally trained coders.
/Best regards, David
Luca | 2020-05-26 00:36:24 UTC | #2
To add the sort and filter functionalities you can create a **QSortFilterProxyModel** object. This new object will be interposed between the model and the view. QSortFilterProxyModel works on the indexes so it will allow adding those functionalities without any modification or duplication of the data at the source.
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
Let me add a string column to the original data of the Martin's tutorial:
python ```
data = pd.DataFrame([
   [1, 9, 2, "door"],
   [1, 0, -1, "dog"],
   [3, 5, 2, "duck"],
   [3, 3, 2, "dog"],
   [5, 8, 9, "air"],
  ], columns = ['A', 'B', 'C', 'D'], index=['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5'])

```

The code was:
python ```
  self.model = TableModel(data)
  self.table.setModel(self.model)

```

For **sorting** it would become:
python ```
  self.model = TableModel(data)
  self.proxyModel = QSortFilterProxyModel()
  self.proxyModel.setSourceModel(self.model)
  self.table.setSortingEnabled(True)
  self.table.setModel(self.proxyModel)

```

The method **setSortingEnabled(True)** must be called because sorting is disabled by default.
While for **filtering** it would become:
python ```
  self.model = TableModel(data)
  self.proxyModel = QSortFilterProxyModel()
  self.proxyModel.setSourceModel(self.model)
  self.proxyModel.setFilterKeyColumn(3)
  self.proxyModel.setFilterFixedString("dog")
  #self.proxyModel.setFilterWildcard("do")
  #self.proxyModel.setFilterRegExp(QRegExp("do.*"))
  self.table.setModel(self.proxyModel)

```

The method **setFilterKeyColumn()** allows you to select the column for the filtering (column indexes start from 0).
For **custom sorting** you can reimplement the **sort()** method in the QAbstractTableModel class.
For **custom filtering** you can reimplement the **filterAcceptsRow()** or **the filterAcceptsColumn()** in the QSortFilterProxyModel class.
mike2750 | 2020-06-05 20:35:25 UTC | #3
Thanks for this advise i actually ended up making a killer implementation of this after alot of trial and error and leaving my example in case its helpful for anyone else.
It was a pita putting all the pieces together from this and other tutorials.
this is a pretty workable building block to both show all columns hide some and adjust alot of stuff. I haven't gotten to the contextual shading and fancy stuff yet but its on my todo.
how it looks in my app now with the sorting and filtering. :) ![Selection_999\(569\)|233x500](https://www.pythonguis.com/static/faq/forum/add-some-explanation-on-sorting-a-qtableview/f56pW0UzmeHgXTtTtza15gwwRSM.png)
python ```
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.db = QSqlDatabase.addDatabase("QSQLITE")
    self.db.setDatabaseName("wizardassistant.db")
    self.db.open()
    self.model = QSqlTableModel()
    self.initializedModel()
    self.tableView = QTableView()
    # turn off row numbers
    self.tableView.verticalHeader().setVisible(False)
    # turn off horizontal headers
    # self.tableView.horizontalHeader().setVisible(False)
    # self.tableView.resizeColumnsToContents()
    # self.tableView.resizeRowsToContents()
    self.tableView.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
    self.source_model = self.model
    # self.initializedModel()
    self.proxy_model = QSortFilterProxyModel(self.source_model)
    self.searchcommands = QLineEdit("")
    self.searchcommands.setObjectName(u"searchcommands")
    self.searchcommands.setAlignment(Qt.AlignLeft)
    self.proxy_model.setSourceModel(self.source_model)
    self.tableView.setModel(self.proxy_model)
    # hide columns from the maintableview
    self.tableView.hideColumn(0)
    self.tableView.hideColumn(3)
    self.tableView.hideColumn(4)
    self.tableView.hideColumn(5)
    self.tableView.hideColumn(6)
    self.tableView.hideColumn(7)
    self.proxy_model.setFilterRegExp(QRegExp(self.searchcommands.text(), Qt.CaseInsensitive,
                         QRegExp.FixedString))
    # search all columns
    self.proxy_model.setFilterKeyColumn(-1)
    # enable sorting by columns
    self.tableView.setSortingEnabled(True)
    # set editing disabled for my use
    self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
    self.tableView.setWordWrap(True)
    self.layout = QVBoxLayout()
    self.command_description = QLabel()
    self.command_description.setWordWrap(True)
    self.command_requires_label = QLabel("Command Requires:")
    self.command_requires_label.setWordWrap(True)
    hLayout = QHBoxLayout()
    hLayout.addWidget(self.command_requires_label)
    self.layout.addWidget(self.tableView)
    self.layout.addWidget(self.searchcommands)
    self.layout.addWidget(self.command_description)
    self.layout.addLayout(hLayout)
    self.setLayout(self.layout)
    self.resize(400, 600)
    self.searchcommands.textChanged.connect(self.searchcommands.update)
    self.searchcommands.textChanged.connect(self.proxy_model.setFilterRegExp)
    self.searchcommands.setText("")
    self.searchcommands.setPlaceholderText(u"search command")
    self.tableView.clicked.connect(self.listclicked)
  def initializedModel(self):
    self.model.setTable("commands")
    # self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
    self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    self.model.select()
    self.model.setHeaderData(0, Qt.Horizontal, "ID")
    self.model.setHeaderData(1, Qt.Horizontal, "Category")
    self.model.setHeaderData(2, Qt.Horizontal, "command_alias")
    self.model.setHeaderData(3, Qt.Horizontal, "command")
    self.model.setHeaderData(4, Qt.Horizontal, "requires")
    self.model.setHeaderData(5, Qt.Horizontal, "description")
    self.model.setHeaderData(6, Qt.Horizontal, "controlpanel")
    self.model.setHeaderData(7, Qt.Horizontal, "verification")
  def onAddRow(self):
    self.model.insertRows(self.model.rowCount(), 1)
    self.model.submit()
  def onDeleteRow(self):
    self.model.removeRow(self.tableView.currentIndex().row())
    self.model.submit()
    self.model.select()
  def closeEvent(self, event):
    self.db.close()
  def listclicked(self, index):
    row = index.row()
    cmd = self.proxy_model.data(self.proxy_model.index(row, 3))
    cmd_requires = self.proxy_model.data(self.proxy_model.index(row, 4))
    cmd_description = self.proxy_model.data(self.proxy_model.index(row, 5))
    print(cmd_description)
    self.command_description.setText(cmd_description)
    self.command_requires_label.setText('This command requires being executed via: ' + cmd_requires.upper())
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

```

David_Hansson | 2020-06-09 06:01:09 UTC | #4
What Luca wrote above worked. Thank you.
delvian | 2020-10-01 09:42:57 UTC | #5
Hi Luca,
Thanks. I'm able to sort my table now, but my app crashes with a segmentation fault when I try to update the source model. I'm not accessing any indexes directly, just updating the source model with a call to the db. What am I doing wrong?
Regards, Delvian
delvian | 2020-10-01 15:47:30 UTC | #6
I figured it out after reading the C++ docs. The Qt for Python docs doesn't mention that you need to emit the layoutAboutToBeChanged signal first.
ERIC_HUYGEN | 2021-02-23 16:21:27 UTC | #7
Hi
I have a question about the QSortFilterProxyModel used here. When I connect a slot to the QTableView to change the formatting of a cell when clicked, that works fine when no filtering is done, but when I have filtered, the QModelIndex that I get back in my slot is not the expected index.row(), but the one from the filtered table. How would I get the row() of the clicked cell in the original unfiltered model?
python ```
    self.table_view.clicked.connect(self.cell_clicked)
  def cell_clicked(self, index: QModelIndex, *args, **kwargs):
    print(f"{index.row()=}, {index.column()=}")
    self.proxy_model.sourceModel().toggleDisplayRole(index)

```

Thanks, Rik
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Add some explanation on sorting a QTableView** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/add-some-explanation-on-sorting-a-qtableview/Python books) on the subject. 
**Add some explanation on sorting a QTableView** was published in [faq](https://www.pythonguis.com/faq/) on May 23, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
