# Content from: https://www.pythonguis.com/faq/tableview-delete-rows-works-only-one-time/

[](https://www.pythonguis.com/faq/tableview-delete-rows-works-only-one-time/#menu)
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
# Tableview delete rows works only one time
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Aashish_Gogna | 2022-08-09 11:10:54 UTC | #1
Hello Team,
I have created Qtreeview and Qtableview and set their models to respective Abstract classes. Functionality is: doubleclclicking on an element present in the treeview will create a new row in the tableview with some additional columns. One function in My code is to delete these entries when a button is clicked, which successfully deletes the entire table only once per run, and gives no result for further clicks on delete button even if the entries are present.
delete rows code is:
python ```
model.removeRows(position=0, rows=model.rowCount(0))

```

where removeRows function in tablemodel is written as:
python ```
  def removeRows(self, position, rows=1, index=QtCore.QModelIndex()):
    print(
      "\n\t\t ...removeRows() Starting position: '%s'" % position, 'with the total rows to be deleted: ', rows)
    self.beginRemoveRows(QtCore.QModelIndex(), position, position + rows - 1)
    self.endRemoveRows()

```

Please suggest why the deletion activity deletes the rows only once per run and why the rowcount is always an increasing number even though the rows have already been deleted?
the code is :slight_smile: 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
python ```
class TableModel(QtCore.QAbstractTableModel):
  def __init__(self, data, data_header):
    super().__init__()
    self._data = data
    self.header = data_header
  def data(self, index, role):
    if role == Qt.DisplayRole:
      # See below for the nested-list data structure.
      # .row() indexes into the outer list,
      # .column() indexes into the sub-list
      return self._data[index.column()][index.row()]
    elif role == Qt.EditRole:
      return self._data[index.column()][index.row()]
    elif role == Qt.BackgroundRole:
      # See below for the data structure.
      value = self._data[index.column()][index.row()]
      if index.column() == 6:
        if value == "Not Started":
          return QtGui.QColor("yellow")
        elif value == "Started":
          return QtGui.QColor("orange")
        elif value == "Passed":
          return QtGui.QColor("green")
        elif value == "Failed":
          return QtGui.QColor("red")
    elif role == Qt.TextAlignmentRole:
      value = self._data[index.column()][index.row()]
      if isinstance(value, int) or isinstance(value, float):
        # Align right, vertical middle.
        return Qt.AlignVCenter + Qt.AlignRight
    elif role == Qt.ForegroundRole:
      value = self._data[index.column()][index.row()]
      if (
          (isinstance(value, int) or isinstance(value, float))
          and value < 0
      ):
        return QtGui.QColor('red')
    else:
      return QtCore.QVariant()
  def flags(self, index):
    if index.column() == 0 or index.column() == 1 or index.column() == 6 or index.column() == 7:
      return Qt.ItemIsSelectable | Qt.ItemIsEnabled
    else:
      return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
  def update(self, dataIn, data_header):
    print('Updating Model')
    self._data = dataIn
    self.header = data_header
    print('Datatable : {0}'.format(self._data))
  def rowCount(self, index):
    # The length of the outer list.
    return len(self._data[0])
  def columnCount(self, index):
    # The following takes the first sub-list, and returns
    # the length (only works if all rows are an equal length)
    return len(self._data)
  def headerData(self, col, orientation, role):
    if orientation == Qt.Horizontal and role == Qt.DisplayRole:
      return self.header[col]
    return None
  def setData(self, index, value, role=QtCore.Qt.EditRole):
    if index.isValid() and 0 <= index.row():
      if role == QtCore.Qt.EditRole:
        self._data[index.column()][index.row()] = value
        print("edit", value)
        self.dataChanged.emit(index, index) # NOT WORKING
        return True
      else:
        return False
    else:
      return False
  @QtCore.pyqtSlot()
  def addrow(self):
    # print(self.rowCount(0))
    self.beginInsertRows(QtCore.QModelIndex(), 0, 0)
    ret = (self.insertRows(self.rowCount(0), 1))
    self.endInsertRows()
    # print(ret)
  def removeRows(self, position, rows=1, index=QtCore.QModelIndex()):
    print(
      "\n\t\t ...removeRows() Starting position: '%s'" % position, 'with the total rows to be deleted: ', rows)
    self.beginRemoveRows(QtCore.QModelIndex(), position, position + rows - 1)
    # del self._data[position]
    # self.items = self.items[:position] + self.items[position + rows:]
    self.endRemoveRows()
  def delete_row(self, index):
    self.removeRows(index.row(), 1, QtCore.QModelIndex())

```

martin | 2021-07-23 14:47:09 UTC | #2
Hey! I'm a bit confused by your example code as there is nothing there to actually remove the data from the model. In the second (larger block) there are lines to do this, but they are commented out.
1:1 Coaching & Tutoring for your Python GUIs project
[![Martin Fitzpatrick Python GUIs Coaching & Training](https://www.pythonguis.com/static/theme/images/products/coaching.jpg)](https://calendly.com/martinfitzpatrick/60min-python-guis-coaching)
[60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/) [Book Now](https://www.pythonguis.com/live/)
1:1 Python GUIs Coaching & Training
**Comprehensive code review** • **Bugfixes** & improvements • **Maintainability** advice and **architecture** improvements • **Design and usability** assessment • Suggestions and tips to **expand your knowledge** • **Packaging and distribution** help for Windows, Mac & Linux • [Find out more.](https://www.pythonguis.com/live)
The `beginRemoveRows` and `endRemoveRows` is just there to notify the view that the data is being modified, you still need to make the modifications to the data yourself.
For a list of rows, you can just delete the start index n times (since subsequent elements will shift up). For example... 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
python ```
self.beginRemoveRows(QtCore.QModelIndex(), position, position + rows - 1)
for _ in range(rows):
  del self._data[position]
self.endRemoveRows()

```

Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Tableview delete rows works only one time** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/tableview-delete-rows-works-only-one-time/Python books) on the subject. 
**Tableview delete rows works only one time** was published in [faq](https://www.pythonguis.com/faq/) on July 19, 2021 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [qtableview](https://www.pythonguis.com/topics/qtableview/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
