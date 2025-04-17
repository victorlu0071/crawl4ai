# Content from: https://www.pythonguis.com/faq/is-there-a-way-to-make-a-model-view-table-automatically-open-to-show-the-whole-table/

[](https://www.pythonguis.com/faq/is-there-a-way-to-make-a-model-view-table-automatically-open-to-show-the-whole-table/#menu)
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
# Is there a way to make a Model View Table automatically open to show the whole table?
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Virginia | 2020-05-13 11:54:30 UTC | #1
I have been working on this tutorial: https://www.pythonguis.com/courses/model-views/qtableview-modelviews-numpy-pandas/ and in order to get the app to open up showing the whole table right away without having to resize it, I added window.resize(500,300) before window.show() at the end. However, I am wondering if this is the best way to do it. In particular, is there a way to get a QAbstractTableModel table to open showing the whole table regardless of size? I have searched the web for an example and tried adding a layout, but have had no success. I appreciate any insight into how to do this - it seems like it should be possible, but I am not sure how to do it yet.
martin | 2020-05-17 11:24:01 UTC | #2
[quote="Virginia, post:1, topic:195"] s there a way to get a QAbstractTableModel table to open showing the whole table regardless of size [/quote]
The following will do the trick --
python ```
  def resize_table_to_contents(self):
    vh = self.table.verticalHeader()
    hh = self.table.horizontalHeader()
    size = QtCore.QSize(hh.length(), vh.length()) # Get the length of the headers along each axis.
    size += QtCore.QSize(vh.size().width(), hh.size().height()) # Add on the lengths from the *other* header
    size += QtCore.QSize(20, 20) # Extend further so scrollbars aren't shown.
    self.resize(size)

```

Note that it resizes the _window_ since the tableview is constrained by the window it is in.
The first `+=` line is needed since the vertical header actually adds a bit of width to the horizontal header (and vice versa) where they overlap at the square in the top. The `hh.size()` returns the current visible dimensions not the size of the entire header, so we can only use it for the height on the horizontal, and width on the vertical. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
The final adjustment is neccessary to push the window large enough that scrollbars aren't triggered. If scrollbars are shown they cover part of the content. The values are arbitrary, but work.
Virginia | 2020-05-17 11:57:31 UTC | #3
Thank you very much for this. It works fine. Just to make sure that I understand, I still have to resize the window using this new method (which belongs to the MainWindow class) just before I call window.show()?
How would I go about making the table fill the whole window when the window is resized? I've played around a bit with resizeEvents without success, and the QAbstractTableModel seems to work differently in terms of sizing and size policies.
Thank you very much for your help!
martin | 2020-05-20 21:36:11 UTC | #4
Yep that's right. You should be able to call the resize method whenever you like -- e.g. if you change the content of the table, you can re-update the window again (will need to wait til after the table as updated).
If the table is in a layout (on a QWidget) or set as the central widget (on a QMainWindow) the table should fill the available space automatically -- so resizing the window, will also resize the table.
The key thing is that widgets are constrained by the window (or layout) they are in. Rather than the window resizing to fit its contents, the content fits the window. So you have to resize the outermost thing.
(This is probably worth making more explicit in the tutorials with some examples, since it can be counter-intuitive).
Virginia | 2020-05-20 21:58:08 UTC | #5
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
If the content is supposed to fit the window, then why doesn't the Model Views Table expand when I expand the window? I tried adding a resize event incorporating the resize_table_to_contents method but then the main window wouldn't resize at all.
martin | 2020-05-20 22:38:19 UTC | #6
If the window resize event is triggering the resize_table_to_contents then the window won't be able to resize, as every time it tries it's overruled by that method.
But the table should fill the window without that. Can you post a code snippet maybe?
Virginia | 2020-05-21 15:38:57 UTC | #7
Thank you for helping me with this. I had just added the resize_table_to_contents method to the final set of code which used Pandas.
import sys from PyQt5 import QtCore, QtGui, QtWidgets from PyQt5.QtCore import Qt import pandas as pd
class TableModel(QtCore.QAbstractTableModel):
python ```
def __init__(self, data):
  super().__init__()
  self._data = data
def data(self, index, role):
  if role == Qt.DisplayRole:
    value = self._data.iloc[index.row(), index.column()]
    return str(value)
def rowCount(self, index):
  return self._data.shape[0]
def columnCount(self, index):
  return self._data.shape[1]
def headerData(self, section, orientation, role):
  # section is the index of the column/row.
  if role == Qt.DisplayRole:
    if orientation == Qt.Horizontal:
      return str(self._data.columns[section])
    if orientation == Qt.Vertical:
      return str(self._data.index[section])

```

class MainWindow(QtWidgets.QMainWindow):
python ```
def __init__(self):
  super().__init__()
  self.table = QtWidgets.QTableView()
  data = pd.DataFrame([
   [1, 9, 2],
   [1, 0, -1],
   [3, 5, 2],
   [3, 3, 2],
   [5, 8, 9],
  ], columns = ['A', 'B', 'C'], index=['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5'])
  self.model = TableModel(data)
  self.table.setModel(self.model)
  self.setCentralWidget(self.table)
def resize_table_to_contents(self):
  vh = self.table.verticalHeader()
  hh = self.table.horizontalHeader()
  size = QtCore.QSize(hh.length(), vh.length()) # Get the length of the headers along each axis.
  size += QtCore.QSize(vh.size().width(), hh.size().height()) # Add on the lengths from the *other* header
  size += QtCore.QSize(20, 20) # Extend further so scrollbars aren't shown.
  self.resize(size)

```

app=QtWidgets.QApplication(sys.argv) window=MainWindow() window.resize_table_to_contents() window.show() app.exec_()
Thank you for your help. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Is there a way to make a Model View Table automatically open to show the whole table?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/is-there-a-way-to-make-a-model-view-table-automatically-open-to-show-the-whole-table/Python books) on the subject. 
**Is there a way to make a Model View Table automatically open to show the whole table?** was published in [faq](https://www.pythonguis.com/faq/) on May 13, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [qabstracttablemodel](https://www.pythonguis.com/topics/qabstracttablemodel/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
