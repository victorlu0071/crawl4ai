# Content from: https://www.pythonguis.com/faq/programmatically-select-multiple-rows-in-qtableview/

[](https://www.pythonguis.com/faq/programmatically-select-multiple-rows-in-qtableview/#menu)
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
# Programmatically select multiple rows in Qtableview
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Paul_Inkenbrandt | 2020-10-10 16:43:49 UTC | #1
I am creating an app with three different tableviews that are on three tabs. All three tables have a "join" field that could be used to connect them. I brought in the tables from pandas using the very useful tutorial on the subject (https://www.pythonguis.com/courses/model-views/qtableview-modelviews-numpy-pandas/). I want my script to automatically select rows in the other tables (based on the common field) if I select a row in the third table.
How would I programmatically select multiple rows given their indices? I want to select rows from one table automatically when I select rows from the other table.
Here is a link to my repository for those who are curious: https://github.com/inkenbrandt/wqxsde
Here is my best attempt to do what I am asking about, but it only appears to select one row in the other table, and not all the rows with a matching field:
python ```
def stationsel(self,s):
    self.stationselection = self.StationTableView.selectionModel()
    indexes = self.stationselection.selectedRows(column=2)
    df = self.ResultModel._data
    role = Qt.DisplayRole
    dg = df[df['monitoringlocationid'].isin([self.StationModel.data(i, role) for i in indexes])]
    print(dg)
    mode = QItemSelectionModel.Select | QtCore.QItemSelectionModel.Rows
    for i in dg.index:
      self.ResultTableView.selectRow(i)
    #for i in dg.index:
    #  self.ResultTableView.selectRow(i)

```

![GUICapture|690x477](https://www.pythonguis.com/static/faq/forum/programmatically-select-multiple-rows-in-qtableview/u7ROhuWeh8qmjcoscXVdeWlB4Ig.png)
This is the closest thing I can find in Stack Exchange: https://stackoverflow.com/questions/9678138/how-to-select-next-row-in-qtableview-programmatically/9678278 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
martin | 2020-10-11 15:56:46 UTC | #2
Hey @Paul_Inkenbrandt I think you're very close here.
The `.selectRow()` method on the view is a convenience method for single selection. For selecting multiple rows it looks as though you need to do this via the view's selection model. You've already got the selection model in `self.stationselection` here, so it should be fairly straightforward.
`QSelectionModel` has two `.select()` methods -- one which takes individual `QModelIndex` objects (single selection) and another that accepts a [QItemSelection](https://doc.qt.io/qt-5/qitemselection.html).
> A QItemSelection is basically a list of selection ranges, see [QItemSelectionRange](https://doc.qt.io/qt-5/qitemselectionrange.html)
You can either build `QItemSelectionRange` objects, or use the simpler method of passing a top left and bottom right `QModelIndex` to `QItemSelection.select(topLeft, bottomRight)`. Each additional call adds a new selection. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
If you have non-contiguous selection blocks, what I think you're looking for is something like the following (code untested) --
python ```
def stationsel(self,s):
  self.stationselection = self.StationTableView.selectionModel()
  indexes = self.stationselection.selectedRows(column=2)
  df = self.ResultModel._data
  role = Qt.DisplayRole
  dg = df[df['monitoringlocationid'].isin([self.StationModel.data(i, role) for i in indexes])]
  model = self.StationTableView.model() # get data model for indexes.
  selection = QItemSelection()
  for i in dg.index:
    # Get the model index for selection.
    # Column shouldn't matter for row-wise.
    model_index = model.index(i, 0)
    # Select single row.
    selection.select(model_index, model_index) # top left, bottom right identical
  mode = QItemSelectionModel.Select | QtCore.QItemSelectionModel.Rows
  # Apply the selection, using the row-wise mode.
  self.stationselection.select(selection, mode)

```

If that doesn't do it let me know and I'll put together a complete example.
Paul_Inkenbrandt | 2020-10-11 16:04:07 UTC | #3
That worked! Thanks Martin! Here is my revised code.
> python ```
def stationsel(self,s):
  self.stationselection = self.StationTableView.selectionModel()
  indexes = self.stationselection.selectedRows(column=2)
  df = self.ResultModel._data
  role = Qt.DisplayRole
  dg = df[df['monitoringlocationid'].isin([self.StationModel.data(i, role) for i in indexes])]
  print(dg)
  model = self.ResultTableView.model() # get data model for indexes.
  selection = QItemSelection()
  for i in dg.index:
    self.ResultTableView.selectRow(i)
    model_index = model.index(i, 0)
    # Select single row.
    selection.select(model_index, model_index) # top left, bottom right identical
  mode = QItemSelectionModel.Select | QtCore.QItemSelectionModel.Rows
  # Apply the selection, using the row-wise mode.
  self.resultselection = self.ResultTableView.selectionModel()
  self.resultselection.select(selection, mode)

```

By the way, thank you for providing these resources. I bought the book and access to the videos, and I love it. The best resource for pyqt5 that I can find.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Programmatically select multiple rows in Qtableview** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/programmatically-select-multiple-rows-in-qtableview/Python books) on the subject. 
**Programmatically select multiple rows in Qtableview** was published in [faq](https://www.pythonguis.com/faq/) on October 10, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [qtableview](https://www.pythonguis.com/topics/qtableview/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
