# Content from: https://www.pythonguis.com/faq/treeview-selectedindexes-returns-same-item-multiple-times/

[](https://www.pythonguis.com/faq/treeview-selectedindexes-returns-same-item-multiple-times/#menu)
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
# treeView.selectedIndexes() returns same item multiple times
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Cody_Jackson | 2021-03-11 18:42:16 UTC | #1
Trying to get the indexes from multi-selection of items in a treeView. But each item is returned multiple times. ![Screenshot from 2021-03-11 08-35-28|333x500](https://www.pythonguis.com/static/faq/forum/treeview-selectedindexes-returns-same-item-multiple-times/hMOuGImXMsUwWVtJGFTVOT3qaNR.png)
Looking at the raw returned items, each one has a different memory address, so it's not simply calling the same object multiple times, but creating multiple instances and returning each one. ![Screenshot from 2021-03-11 08-37-14|389x500](https://www.pythonguis.com/static/faq/forum/treeview-selectedindexes-returns-same-item-multiple-times/sp1DIxNJjlQojkWKS7PnvnHHepC.png)
I've tried to use a for loop to try and eliminate all but one of the responses, but it doesn't work.
python ```
    def get_items(self):
       indexes = self.treeView.selectedIndexes()
       seen = []
       for item in indexes:
        if item not in seen:
          self.console.on_update_text(str(item))
          self.console.on_update_text("\n")
          seen.append(item)

```

(Sorry. I can't seem to get the code tags to actually present the code correctly.)
Cody_Jackson | 2021-03-11 19:12:30 UTC | #2
I think I might have solved it.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
python ```
  def get_items(self):
    indexes = self.treeView.selectedIndexes()
    items = []
    for index in indexes:
      item = self.fileSystemModel.filePath(index)
      items.append(item)
    seen = []
    for item in items:
      if item not in seen:
        seen.append(item)
        self.console.on_update_text(item)
        self.console.on_update_text("\n")

```

Using this results in the following: ![Screenshot from 2021-03-11 09-13-22|483x500](https://www.pythonguis.com/static/faq/forum/treeview-selectedindexes-returns-same-item-multiple-times/blw019qQpJNYolFFrsMoR7Ny1oj.png)
If someone has a better way of doing this, please let me know. Also, if someone can tell me why Qt seems to quadruple the results of selectedIndexes(), I would appreciate it.
martin | 2021-03-11 18:47:18 UTC | #3
Hey @Cody_Jackson based on [this Qt forum post](https://www.qtcentre.org/threads/1165-QT4-Selecting-indices-from-a-QTreeView-multiple-duplicates?s=5e27d11b3afcbe7fb80db125593457c7&p=6851#post6851) on a multi-column treeview `.selectedIndexes()` will return an index for each column.
I only see 2 column in your screenshot, but perhaps you have some hidden?
Cody_Jackson | 2021-03-11 18:56:08 UTC | #4
@martin I didn't even realize that. Yes, I have the default columns created by a File Explorer example I found. So I need to figure out how to set only one column, as I don't need the other columns.
Thank you. That really helps a lot.
FWIW, here is the File Explorer code: class ProjectExplorerTree(QTreeView): """Project Explorer box""" 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
python ```
def __init__(self, tree: QTreeView, console) -> None:
  super().__init__()
  self.treeView = tree
  self.default_dir = f"{str(Path.home())}/opencpi" # May have to change this later
  self.console_output = console
  self.fileSystemModel = QFileSystemModel(self.treeView)
  self.fileSystemModel.setReadOnly(False)
  root: Optional[QModelIndex] = self.fileSystemModel.setRootPath(f"{self.default_dir}/projects")
  self.treeView.setModel(self.fileSystemModel)
  self.treeView.setRootIndex(root)
  self.treeView.setSelectionMode(self.treeView.ExtendedSelection)
  self.treeView.setRootIsDecorated(True)
  self.treeView.setAlternatingRowColors(True)
  self.treeView.setDragEnabled(True) # Allow items to be dragged from this panel

```

Cody_Jackson | 2021-03-11 19:13:47 UTC | #5
Had to add `self.treeView.hideColumn(int)` to the **init**() method.
python ```
  self.treeView.setModel(self.fileSystemModel)
  self.treeView.hideColumn(1)
  self.treeView.hideColumn(2)
  self.treeView.hideColumn(3)
  self.treeView.setRootIndex(root)

```

martin | 2021-03-11 19:13:32 UTC | #6
Great! This has caught me out before, don't really think of the treeview as 2d model.
If you can't limit the selection to a single column on the view/model, you could filter out a single column in your method e.g.
python ```
indexes = [i for i in indexes if i.column() == 0]
# or
indexes = filter(lambda i: i.column() == 0, indexes)

```

Cody_Jackson | 2021-03-11 19:19:42 UTC | #7
I think what's most painful with Qt is that there are so many places to look due to inheritance, and there is some naming inconsistency between the classes, e.g. headers vs. columns.
For example, to add a column, you use `setHeader()`, or maybe `setHeaderData()`, but to remove columns, you use `hideColumn()`, but there's also `setHeaderHidden()`.
For me, it's a lot of trial and error, plus hours of searching for tutorials. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**treeView.selectedIndexes() returns same item multiple times** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/treeview-selectedindexes-returns-same-item-multiple-times/Python books) on the subject. 
**treeView.selectedIndexes() returns same item multiple times** was published in [faq](https://www.pythonguis.com/faq/) on March 11, 2021 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
