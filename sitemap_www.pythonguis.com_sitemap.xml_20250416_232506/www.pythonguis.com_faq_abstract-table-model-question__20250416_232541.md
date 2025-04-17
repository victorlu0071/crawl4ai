# Content from: https://www.pythonguis.com/faq/abstract-table-model-question/

[](https://www.pythonguis.com/faq/abstract-table-model-question/#menu)
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
# Checkboxes in Table Views with custom model
Show check boxes for boolean values
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ FAQ ](https://www.pythonguis.com/faq/)
_T Carson wrote_
I found some code with an example of an abstract table model. I got it running with Pyside2 and now I want to add a column of checkboxes. I see where the combo box is made in the AssetDelegate class. Should I make a similar class for a checkbox or somehow add to this class?
python ```
import sys
from PySide2 import QtGui, QtCore, QtWidgets

class AssetDelegate(QtWidgets.QStyledItemDelegate):
  def paint(self, painter, option, index):
    if isinstance(self.parent(), QtWidgets.QAbstractItemView):
      self.parent().openPersistentEditor(index)
    QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)
  def createEditor(self, parent, option, index):
    combobox = QtWidgets.QComboBox(parent)
    combobox.addItems(index.data(AssetModel.ItemsRole))
    combobox.currentIndexChanged.connect(self.onCurrentIndexChanged)
    return combobox
  def onCurrentIndexChanged(self, ix):
    editor = self.sender()
    self.commitData.emit(editor)
    self.closeEditor.emit(editor, QtWidgets.QAbstractItemDelegate.NoHint)
  def setEditorData(self, editor, index):
    ix = index.data(AssetModel.ActiveRole)
    editor.setCurrentIndex(ix)
  def setModelData(self, editor, model, index):
    ix = editor.currentIndex()
    model.setData(index, ix, AssetModel.ActiveRole)

class Asset(object):
  def __init__(self, name, items=[], active=0):
    self.active = active
    self.name = name
    self.items = items
  @property
  def status(self):
    return self.active == len(self.items) - 1

class AssetModel(QtCore.QAbstractTableModel):
  attr = ["Name", "Options", "Extra"]
  ItemsRole = QtCore.Qt.UserRole + 1
  ActiveRole = QtCore.Qt.UserRole + 2
  def __init__(self, *args, **kwargs):
    QtCore.QAbstractTableModel.__init__(self, *args, **kwargs)
    self._items = []
  def flags(self, index):
    fl = QtCore.QAbstractTableModel.flags(self, index)
    if index.column() == 1:
      fl |= QtCore.Qt.ItemIsEditable
    return fl
  def clear(self):
    self.beginResetModel()
    self._items = []
    self.endResetModel()
  def rowCount(self, index=QtCore.QModelIndex()):
    return len(self._items)
  def columnCount(self, index=QtCore.QModelIndex()):
    return len(self.attr)
  def addItem(self, sbsFileObject):
    self.beginInsertRows(QtCore.QModelIndex(),
               self.rowCount(), self.rowCount())
    self._items.append(sbsFileObject)
    self.endInsertRows()
  def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
    if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
      return AssetModel.attr[section]
    return QtCore.QAbstractTableModel.headerData(self, section, orientation, role)
  def data(self, index, role=QtCore.Qt.DisplayRole):
    if not index.isValid():
      return None
    if 0 <= index.row() < self.rowCount():
      item = self._items[index.row()]
      col = index.column()
      if role == AssetModel.ItemsRole:
        return getattr(item, 'items')
      if role == AssetModel.ActiveRole:
        return getattr(item, 'active')
      if 0 <= col < self.columnCount():
        if role == QtCore.Qt.DisplayRole:
          if col == 0:
            return getattr(item, 'name', '')
          if col == 1:
            return getattr(item, 'items')[getattr(item, 'active')]
        elif role == QtCore.Qt.DecorationRole:
          if col == 0:
            status = getattr(item, 'status')
            col = QtGui.QColor(QtCore.Qt.red) if status else QtGui.QColor(
              QtCore.Qt.green)
            px = QtGui.QPixmap(120, 120)
            px.fill(QtCore.Qt.transparent)
            painter = QtGui.QPainter(px)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            px_size = px.rect().adjusted(12, 12, -12, -12)
            painter.setBrush(col)
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 4,
                         QtCore.Qt.SolidLine,
                         QtCore.Qt.RoundCap,
                         QtCore.Qt.RoundJoin))
            painter.drawEllipse(px_size)
            painter.end()
            return QtGui.QIcon(px)
  def setData(self, index, value, role=QtCore.Qt.EditRole):
    if 0 <= index.row() < self.rowCount():
      item = self._items[index.row()]
      if role == AssetModel.ActiveRole:
        setattr(item, 'active', value)
        return True
    return QtCore.QAbstractTableModel.setData(self, index, value, role)

class Example(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()
    self.resize(400, 300)
    # controls
    asset_model = QtCore.QSortFilterProxyModel()
    asset_model.setSortCaseSensitivity(QtCore.Qt.CaseInsensitive)
    asset_model.setSourceModel(AssetModel())
    self.ui_assets = QtWidgets.QTableView()
    self.ui_assets.setEditTriggers(
      QtWidgets.QAbstractItemView.NoEditTriggers)
    self.ui_assets.setModel(asset_model)
    self.ui_assets.verticalHeader().hide()
    self.ui_assets.setItemDelegateForColumn(1, AssetDelegate(self.ui_assets))
    main_layout = QtWidgets.QVBoxLayout()
    main_layout.addWidget(self.ui_assets)
    self.setLayout(main_layout)
    self.unit_test()
  def unit_test(self):
    assets = [
      Asset('Dev1', ['v01', 'v02', 'v03'], 0),
      Asset('Dev2', ['v10', 'v11', 'v13'], 1),
      Asset('Dev3', ['v11', 'v22', 'v53'], 2),
      Asset('Dev4', ['v13', 'v21', 'v23'], 0)
    ]
    self.ui_assets.model().sourceModel().clear()
    for i, obj in enumerate(assets):
      self.ui_assets.model().sourceModel().addItem(obj)

def main():
  app = QtWidgets.QApplication(sys.argv)
  ex = Example()
  ex.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()

```

_Martin Fitzpatrick_
You _can_ use a custom delegate to draw the widget if you like, but you don't have to. There is `Qt.CheckStateRole` which you can use to display a checkbox depending on whether you return `Qt.Checked` or `Qt.Unchecked` in your `.data` method.
python ```
  def data(self, index, role):
    if role == Qt.DisplayRole:
      value = self._data[index.row()][index.column()]
      return str(value)
    if role == Qt.CheckStateRole:
      return Qt.Checked

```

This shows up like this
![checked|690x277](https://www.pythonguis.com/static/faq/todo/abstract-table-model-question/jEZMMnIU6wRy1ORY0NHQmtmVuBA.jpeg)
If you want to allow the user to toggle the checkboxes you need a few things --
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
  1. a data store for the check state
  2. to return `Qt.ItemIsUserCheckable` from the `.flags()` method
  3. to implement the `.setData` method to accept and store the updated data.


The following example implements that. The check state data is stored in a separate table, just for clarity -- 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
python ```
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
  def __init__(self, data, checked):
    super().__init__()
    self._data = data
    self._checked = checked
  def data(self, index, role):
    if role == Qt.DisplayRole:
      value = self._data[index.row()][index.column()]
      return str(value)
    if role == Qt.CheckStateRole:
      checked = self._checked[index.row()][index.column()]
      return Qt.Checked if checked else Qt.Unchecked
  def setData(self, index, value, role):
    if role == Qt.CheckStateRole:
      checked = value == Qt.Checked
      self._checked[index.row()][index.column()] = checked
      return True
  def rowCount(self, index):
    return len(self._data)
  def columnCount(self, index):
    return len(self._data[0])
  def flags(self, index):
    return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsUserCheckable
class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()

    self.table = QtWidgets.QTableView()
    data = [
     [1, 9, 2],
     [1, 0, -1],
     [3, 5, 2],
     [3, 3, 2],
     [5, 8, 9],
    ]
    checked = [
     [True, True, True],
     [False, False, False],
     [True, False, False],
     [True, False, True],
     [False, True, True],
    ]
    self.model = TableModel(data, checked)
    self.table.setModel(self.model)
    self.setCentralWidget(self.table)

app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()

```

If you run this, you'll see you are able to check and toggle the checkboxes next to any value. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Checkboxes in Table Views with custom model** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/abstract-table-model-question/Python books) on the subject. 
**Checkboxes in Table Views with custom model** was published in [faq](https://www.pythonguis.com/faq/) on May 31, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyside](https://www.pythonguis.com/topics/pyside/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
