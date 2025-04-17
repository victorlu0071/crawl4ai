# Content from: https://www.pythonguis.com/faq/file-image-browser-app-with-thumbnails/

[](https://www.pythonguis.com/faq/file-image-browser-app-with-thumbnails/#menu)
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
# File Image Browser App with thumbnails
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Rafael_Lago | 2020-11-10 20:14:45 UTC | #1
Hey there,
I'm trying to develop some image viewer in the same vein as KDE's Gwenview, but with some very specific features for my actual application. I'll be using python 3.8 and PyQt5.
The question is: is there already any widget for browsing files in icon-mode, showing thumbnails of images, or would I have to implement that whole jazz from the scratch?
martin | 2020-11-24 10:28:12 UTC | #2
Hi @Rafael_Lago welcome to the forum, sorry for the delay in replying
Unfortunately, there isn't a ready-to-go widget for this, but it's fairly straightforward to implement. See a quick example below, which is used the [model view framework](https://www.pythonguis.com/courses/model-views/) to render thumbnails for image files in a folder. Here we're using a table view to layout the items, and a custom delegate to draw the thumbnails (you can add anything else you like). 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
python ```
import glob
import math
import sys
from collections import namedtuple
from PyQt5.QtCore import QAbstractTableModel, Qt, QSize
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QStyledItemDelegate
# Create a custom namedtuple class to hold our data.
preview = namedtuple("preview", "id title image")
NUMBER_OF_COLUMNS = 4
CELL_PADDING = 20 # all sides
class PreviewDelegate(QStyledItemDelegate):
  def paint(self, painter, option, index):
    # data is our preview object
    data = index.model().data(index, Qt.DisplayRole)
    if data is None:
      return
    width = option.rect.width() - CELL_PADDING * 2
    height = option.rect.height() - CELL_PADDING * 2
    # option.rect holds the area we are painting on the widget (our table cell)
    # scale our pixmap to fit
    scaled = data.image.scaled(
      width,
      height,
      aspectRatioMode=Qt.KeepAspectRatio,
    )
    # Position in the middle of the area.
    x = CELL_PADDING + (width - scaled.width()) / 2
    y = CELL_PADDING + (height - scaled.height()) / 2
    painter.drawImage(option.rect.x() + x, option.rect.y() + y, scaled)
  def sizeHint(self, option, index):
    # All items the same size.
    return QSize(300, 200)

class PreviewModel(QAbstractTableModel):
  def __init__(self, todos=None):
    super().__init__()
    # .data holds our data for display, as a list of Preview objects.
    self.previews = []
  def data(self, index, role):
    try:
      data = self.previews[index.row() * 4 + index.column() ]
    except IndexError:
      # Incomplete last row.
      return
    if role == Qt.DisplayRole:
      return data  # Pass the data to our delegate to draw.
    if role == Qt.ToolTipRole:
      return data.title
  def columnCount(self, index):
    return NUMBER_OF_COLUMNS
  def rowCount(self, index):
    n_items = len(self.previews)
    return math.ceil(n_items / NUMBER_OF_COLUMNS)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.view = QTableView()
    self.view.horizontalHeader().hide()
    self.view.verticalHeader().hide()
    self.view.setGridStyle(Qt.NoPen)
    delegate = PreviewDelegate()
    self.view.setItemDelegate(delegate)
    self.model = PreviewModel()
    self.view.setModel(self.model)
    self.setCentralWidget(self.view)
    # Add a bunch of images.
    for n, fn in enumerate(glob.glob("*.jpg")):
      image = QImage(fn)
      item = preview(n, fn, image)
      self.model.previews.append(item)
    self.model.layoutChanged.emit()
    self.view.resizeRowsToContents()
    self.view.resizeColumnsToContents()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

If you drop this file in any folder containing jpeg files (extension "*.jpg") they'll be shown in a list.
![fileimagebrowser.PNG|690x388](https://www.pythonguis.com/static/faq/forum/file-image-browser-app-with-thumbnails/eBABHRgFnUe2cXMUUv1hwMdSg3L.jpeg)
Rafael_Lago | 2020-11-24 10:28:12 UTC | #3
Thank you very much! I was actually trying to develop it using QTableView, but I am not very familiar with this part of Qt5 (yet). Your code is very helpful!
Rafael_Lago | 2020-11-24 10:28:07 UTC | #4
So, I extended the concept, but using QFilesystemModel and QListView in IconMode with a given gridSize:
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
modUI.py: https://pastebin.com/q5jzz7S8 main.py: https://pastebin.com/Mes6cVZt
One of the remaining problems is that the position of the icons is not updated when I resize the window, which gives some funny results (see attached image).
I assume I have to connect some signal to some slot (i.e. resize of window to QListView.update?) but I'm not very familiar with Qt at this point to know which signal to what. Can anyone shed some light?
![ksnip_20201113-163506|690x414](https://www.pythonguis.com/static/faq/forum/file-image-browser-app-with-thumbnails/lEm8cNJT5tjpLzP7yskw4853k3v.png)
EDIT#1: nevermind, I just found about setResizeMode(QtWidgets.QListView.Adjust)
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**File Image Browser App with thumbnails** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/file-image-browser-app-with-thumbnails/Python books) on the subject. 
**File Image Browser App with thumbnails** was published in [faq](https://www.pythonguis.com/faq/) on October 30, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyqtgraph](https://www.pythonguis.com/topics/pyqtgraph/) [thumbnail](https://www.pythonguis.com/topics/thumbnail/) [browser](https://www.pythonguis.com/topics/browser/) [images](https://www.pythonguis.com/topics/images/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [ data-science](https://www.pythonguis.com/topics/data-science/)
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
