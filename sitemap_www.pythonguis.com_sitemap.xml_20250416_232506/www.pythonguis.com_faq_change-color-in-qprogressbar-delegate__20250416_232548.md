# Content from: https://www.pythonguis.com/faq/change-color-in-qprogressbar-delegate/

[](https://www.pythonguis.com/faq/change-color-in-qprogressbar-delegate/#menu)
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
# Change color in QProgressBar delegate
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ FAQ ](https://www.pythonguis.com/faq/)
Vladislav_Alekseev | 2021-03-24 11:48:38 UTC | #1
Hello everyone! I want to make the progress of the process (QProgressBar)in QTableView, it already worked, but now I want to add a color change when the process stops. I don't understand how to do this with a delegate, I tried installing a new delegate, but it doesn't work (it doesn't redraw the color), I tried installing a standard delegate, but there are no changes. There is no range in the delegate, i.e. SetRange(0, 0) the process is either running (green) or not (red).
Example:
python ```
from PySide2 import QtCore, QtWidgets, QtGui

class ProgressBarDelegate(QtWidgets.QStyledItemDelegate):
  def __init__(self, parent, color):
    super().__init__(parent)
    self.color = color
  def paint(self, painter, option, index):
    if index.column() == 2:
      if (isinstance(self.parent(), QtWidgets.QAbstractItemView)
          and self.parent().model() is index.model()):
        self.parent().openPersistentEditor(index)
      QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)
    else:
      QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)
  def createEditor(self, parent: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem,
           index: QtCore.QModelIndex) -> QtWidgets.QWidget:
    editor = QtWidgets.QProgressBar(parent)
    editor.setRange(0, 0)
    editor.setTextVisible(False)
    editor.setStyleSheet("QProgressBar:chunk {background-color:" + self.color + "; width: 20px; margin: 0.5px}")
    return editor

class PushButtonDelegate(QtWidgets.QStyledItemDelegate):
  clicked = QtCore.Signal(QtCore.QModelIndex)
  def paint(self, painter, option, index):
    if (isinstance(self.parent(), QtWidgets.QAbstractItemView)
        and self.parent().model() is index.model()):
      self.parent().openPersistentEditor(index)
    QtWidgets.QStyledItemDelegate.paint(self, painter, option, index)
  def createEditor(self, parent, option, index):
    button = QtWidgets.QPushButton(parent)
    button.clicked.connect(lambda *args, ix=index: self.clicked.emit(ix))
    return button
  def setEditorData(self, editor, index):
    editor.setText("Start/Stop")
  def updateEditorGeometry(self, editor, option, index):
    editor.setGeometry(option.rect)

class MyWidgetsForm(QtWidgets.QMainWindow):
  def __init__(self, parent=None):
    QtWidgets.QMainWindow.__init__(self, parent)
    self.initUi()
    self.initModel()
    self.pbDelegate.clicked.connect(self.onPBDelegateClicked)
  def onPBDelegateClicked(self, pushRow):
    print(self.tableView.model().index(pushRow.row(), 2).data())
    if self.tableView.model().index(pushRow.row(), 2).data() is None or self.tableView.model().index(pushRow.row(),
                                                     2).data() == 0:
      prbarDelegate = ProgressBarDelegate(self.tableView, "green")
      self.tableView.setItemDelegateForRow(pushRow.row(), prbarDelegate)
      self.tableView.model().setData(self.tableView.model().index(pushRow.row(), 2), 1,
                      QtCore.Qt.DisplayRole)
    elif self.tableView.model().index(pushRow.row(), 2).data() == 1:
      prbarDelegate = ProgressBarDelegate(self.tableView, "red")
      self.tableView.setItemDelegateForRow(pushRow.row(), prbarDelegate)
      self.tableView.model().setData(self.tableView.model().index(pushRow.row(), 2), 0,
                      QtCore.Qt.DisplayRole)
  def initUi(self):
    self.setFixedSize(600, 300)
    self.tableView = QtWidgets.QTableView()
    layout = QtWidgets.QHBoxLayout()
    layout.addWidget(self.tableView)
    cw = QtWidgets.QWidget()
    cw.setLayout(layout)
    self.setCentralWidget(cw)
  def initModel(self):
    headers = ['Путь', 'Управление', 'Прогресс']
    self.pbDelegate = PushButtonDelegate(self.tableView)
    self.stm = QtGui.QStandardItemModel()
    self.stm.setHorizontalHeaderLabels(headers)
    for row in range(5):
      self.stm.setItem(row, 0, QtGui.QStandardItem("some_path" + str(row)))
      self.stm.setItem(row, 1, QtGui.QStandardItem())
    self.tableView.setModel(self.stm)
    self.tableView.clearSpans()
    self.tableView.setItemDelegateForColumn(1, self.pbDelegate)
    self.tableView.resizeColumnsToContents()
    self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

if __name__ == "__main__":
  app = QtWidgets.QApplication()
  myapp = MyWidgetsForm()
  myapp.show()
  app.exec_()

```

The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Change color in QProgressBar delegate** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/change-color-in-qprogressbar-delegate/Python books) on the subject. 
**Change color in QProgressBar delegate** was published in [faq](https://www.pythonguis.com/faq/) on March 24, 2021 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
