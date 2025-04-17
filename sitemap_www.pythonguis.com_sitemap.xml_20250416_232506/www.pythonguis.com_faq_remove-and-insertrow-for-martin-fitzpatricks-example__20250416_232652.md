# Content from: https://www.pythonguis.com/faq/remove-and-insertrow-for-martin-fitzpatricks-example/

[](https://www.pythonguis.com/faq/remove-and-insertrow-for-martin-fitzpatricks-example/#menu)
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
# Remove and insertrow for Martin Fitzpatricks example
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Heads up! You've already completed this tutorial. 
David_Hansson | 2020-06-30 11:46:58 UTC | #1
Hello, how would remove and insertrow look like for Martin Fitzpatricks example above?
First one needs `def removeRows()`/`def InserRows()` for the `QAbstractTableModel` class and also some behaviour inside the `QMainwindow` class
python ```
  # This I have for my QAbstractTabelModel class
  def insertRows(self, position, rows, QModelIndex, parent):
    self.beginInsertRows(QModelIndex(), position, position+rows-1)
    for i in range(rows):
      default_row = ['']*len(self._headers)
      self_data.insert(position, default_row)
    self.endInsertRows()
    return true

  def removeRows(self, position, rows, QModelIndex, parent):
    self.beginRemoveRows(QModelIndex(), position, position+rows-1)
    for i in range(rows):
      del(self._data[position])
    self.endRemoveRows()
    return true

```

Not sure if that is correct, Its what I've pieced together from examples on other sites.
For the `QMainwindow` class I'm not relay sure how to proceed, the examples on other sites are not very clear to understand.
Some structured extra explanation on this subject for Martins example of this would be helpful.
The row of data should be removed for both the model and the view. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
mike2750 | 2020-06-20 19:16:07 UTC | #2
Not sure if this is what your looking for but this is what I have working for my sqlite tableview setup.
python ```
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
  db.close()

```

To clear all the rows or content you can do something like the below.
python ```
self.w_tablewidget.clearContents()
self.w_tablewidget.setRowCount(0)

```

David_Hansson | 2020-06-28 10:23:26 UTC | #3
This is how I have set up my QTableView(not subclassed) and QAbstractTableModel (subclassed as TableModel):
python ```
  self.model = TableModel(data)
  self.proxyModel = QSortFilterProxyModel()
  self.proxyModel.setSourceModel(self.model)
  self.table_clients.setSortingEnabled(True)
  self.table_clients.setModel(self.proxyModel)
  self.selectionModel = self.table_clients.selectionModel()
  self.table_clients.setSelectionBehavior(QTableView.SelectRows)

```

I for the QAbstractTableModel class I know have this:
python ```
def removeRows(self, position, rows, parent):
  print("passed def removingrows")
  #print "\n\t\t ...removeRows() Starting position: '%s'"%position, 'with the total rows to be deleted: ', rows
  self.beginRemoveRows(parent or QModelIndex(), position, position + rows - 1)
  print("passed beginremovingrows")
  for i in range(rows):
    del(self._data[position])
    print("passed deleted row")
  self.endRemoveRows()
  print("passed endRemoveRows")
  return true

```

For the Mainwindow class I have this:
python ```
def removerow(self):
  #self.table_clients.model().layoutAboutToBeChanged.emit()
  print("passed def removerow")
  proxy_index = self.table_clients.selectedIndexes()[0]
  print("passed proxyindex = " + str(proxy_index))
  #convert
  source_index = self.proxyModel.mapToSource(proxy_index)
  print("passed sorceindex = " + str(source_index))
  #delete row in source model
  self.model.removeRow(source_index.row())
  # ---- --- something is wrong after this passage - it crashes here ----
  print("passed modelremoveRow source index")
  #self.model.layoutChanged.emit()
  self.table_clients.clearSelection()

```

It crahes after self.model.removeRow(source:index.row()) because the promt prints this: _= RESTART: C:\Users\svart\Documents\Python\Pythonprojects\AIXCRM\PRM_AIX_200629.py_ _passed def removerow_ _passed proxyindex =_ _passed sorceindex =_ _passed def removingrows_ _passed beginremovingrows_ _passed deleted row_ _passed endRemoveRows_
This might be something basic thing that is escaping me? And it doesnt change anything if I remove the # from the lines with layoutAboutToBeChanged/layoutChanged, it still crashes at the same place.
David_Hansson | 2020-06-28 10:25:33 UTC | #4 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
And thank you Mike2750 for the reply but I couldnt make anthing of that advice, partially I guess becouse my program is setup a bit different.
martin | 2020-06-30 12:10:51 UTC | #5
Hi @David_Hansson welcome to the forum! I've written up a small example with two actions which trigger add/remove of rows on the table model. One important thing is to notify the view that the layout of the data has changed after doing this, otherwise it won't update.
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
      value = self._data[index.row()][index.column()]
      return str(value)
  def rowCount(self, index):
    return len(self._data)
  def columnCount(self, index):
    return len(self._data[0])
  def insertRows(self, position, rows, QModelIndex, parent):
    self.beginInsertRows(QModelIndex, position, position+rows-1)
    default_row = ['']*len(self._data[0]) # or _headers if you have that defined.
    for i in range(rows):
      self._data.insert(position, default_row)
    self.endInsertRows()
    self.layoutChanged.emit()
    return True
  def removeRows(self, position, rows, QModelIndex):
    self.beginRemoveRows(QModelIndex, position, position+rows-1)
    for i in range(rows):
      del(self._data[position])
    self.endRemoveRows()
    self.layoutChanged.emit()
    return True
class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.insertaction = QtWidgets.QAction("Insert")
    self.insertaction.triggered.connect(self.insert_row)
    self.deletedaction = QtWidgets.QAction("Delete")
    self.deletedaction.triggered.connect(self.delete_row)
    toolbar = QtWidgets.QToolBar("Edit")
    toolbar.addAction(self.insertaction)
    toolbar.addAction(self.deletedaction)
    self.addToolBar(toolbar)

    self.table = QtWidgets.QTableView()
    data = [
     [1, 9, 2],
     [1, 0, -1],
     [3, 5, 2],
     [3, 3, 2],
     [5, 8, 9],
    ]
    self.model = TableModel(data)
    self.table.setModel(self.model)
    self.setCentralWidget(self.table)
  def insert_row(self):
    index = self.table.currentIndex()
    print(index)
    self.model.insertRows(index.row(), 1, index, None)
  def delete_row(self):
    index = self.table.currentIndex()
    self.model.removeRows(index.row(), 1, index)

app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()

```

David_Hansson | 2020-07-23 12:51:02 UTC | #6
Thank you Martin, this worked for me. Great help.
For others that like me have a proxy model in between the Model and the QTableView I found out that I had to add self.layoutAboutToBeChanged.emit() in the begining of the def insertRows() or def removeRows(). Without that I found out that I could only delete one row or insert one row before the application would be non-responsive, or the delete or insert didnt work at alla after one row insert or delete.
so final code for QSortFilterProxyModel In the sub-classed QAbstractTableModel
python ```
def insertRows(self, position, rows, QModelIndex, parent):
  self.layoutAboutToBeChanged.emit()
  self.beginInsertRows(QModelIndex, position, position+rows-1)
  default_row = ['']*len(self._data[0])
  for i in range(rows):
    self._data.insert(position, default_row)
  self.endInsertRows()
  self.layoutChanged.emit()
  return True
def removeRows(self, position, rows, QModelIndex):
  self.layoutAboutToBeChanged.emit()
  self.beginRemoveRows(QModelIndex, position, position+rows-1)
  for i in range(rows):
    del(self._data[position])
  self.endRemoveRows()
  self.layoutChanged.emit()
  return True

```

In the Mainwindow the delete_row() would be like this
python ```
def delete_row(self):
  proxy_index = self.table.currentIndex()
  index = self.proxyModel.mapToSource(proxy_index)
  self.model.removeRows(index.row(), 1, index)

```

mike2750 | 2020-07-23 03:21:53 UTC | #7
@David_Hansson Nice thanks for the tip. I'm probably going to need that snippet soon. Saved.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[ ![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png) ](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
[[ discount.discount_pc ]]% OFF for the next [[ discount.duration ]] [[discount.description ]] with the code [[ discount.coupon_code ]]
####  Purchasing Power Parity
Developers in [[ country ]] get [[ discount.discount_pc ]]% OFF on all books & courses with code [[ discount.coupon_code ]]
Well done, you've finished this tutorial!  Mark As Complete 
[[ user.completed.length ]] completed [[ user.streak+1 ]] day streak
[ ![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg) ](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Remove and insertrow for Martin Fitzpatricks example** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/remove-and-insertrow-for-martin-fitzpatricks-example/Python books) on the subject. 
**Remove and insertrow for Martin Fitzpatricks example** was published in [faq](https://www.pythonguis.com/faq/) on June 20, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
