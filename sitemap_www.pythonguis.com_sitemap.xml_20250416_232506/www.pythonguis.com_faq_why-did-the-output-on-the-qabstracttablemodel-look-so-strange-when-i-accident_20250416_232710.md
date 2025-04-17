# Content from: https://www.pythonguis.com/faq/why-did-the-output-on-the-qabstracttablemodel-look-so-strange-when-i-accidentally-omitted-if-role-qt-displayrole/

[](https://www.pythonguis.com/faq/why-did-the-output-on-the-qabstracttablemodel-look-so-strange-when-i-accidentally-omitted-if-role-qt-displayrole/#menu)
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
# Why did the output on the QAbstractTableModel look so strange when I accidentally omitted "if role == Qt.DisplayRole:"?
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Virginia | 2020-05-09 13:51:39 UTC | #1
When I was working on the [QAbstractTableModel Tutorial](https://www.pythonguis.com/courses/model-views/qtableview-modelviews-numpy-pandas/) and had just added the block that formats strings into things like dates, floats, and integers, I accidentally omitted the first line of the data method block, `if role == Qt.DisplayRole:`.
The code still ran, but the output looked rather strange and I was wondering why this happened. This was the code that I had just added, but accidentally omitted the first line:
python ```
  def data(self, index, role):
    if role == Qt.DisplayRole: #omitting this accidentally caused the error
    # Get the raw value
      value = self._data[index.row()][index.column()]
      # Perform per-type checks and render accordingly
      if isinstance(value, datetime.date):
        # Render time to YYY-MM-DD.
        return value.strftime("%Y-%m-%d")
      if isinstance(value, float):
        # Render float to 2 dp
        return "%.2f" % value
      if isinstance(value, str):
        # Render strings with quotes
        return '"%s"' % value
      # Default (anything not captured above: e.g. int)
      return value

```

This is what the output looked like:
![image|642x487](https://www.pythonguis.com/static/faq/forum/why-did-the-output-on-the-qabstracttablemodel-look-so-strange-when-i-accidentally-omitted-if-role-qt-displayrole/mHuGMCeGVGhCkChIwvFMA7q2FaP.png)
I am very curious as to why this happened - there are check boxes, check marks, and a square filled in.
Thank you for your insights! 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
martin | 2022-08-08 21:15:37 UTC | #2
Hey @Virginia welcome to the forum. This is a fantastic question because it gets into the details of how this all works.
The `data` method works by receiving an `index` and `role` and responding with instructions for the view to perform. The `index` says _where_ and the `role` says _what_.
In the tutorial we cover in detail roles for outputting data (`Qt.DisplayRole`) and also colours (e.g. `Qt.BackgroundRole`) but there are other roles too, including one for showing checkboxes --- `Qt.CheckStateRole` (there is a complete table in the tutorial).
When you nest your code under `if role == Qt.DisplayRole` you ensure that you _only_ return data for that specific role. Qt is still sending them to your method, but they are being silently ignored (functions return None by default).
When you omit that line, your method is now responding to _all_ roles it receives with the answers that you have defined for `Qt.DisplayRole` -- including `Qt.CheckStateRole`
So why do some checkboxes show empty, some ticked and some filled with a square?
When your method is called with `Qt.CheckStateRole` Qt is expected a `Qt.CheckState` as an answer. [Qt.CheckState](https://doc.qt.io/qt-5/qt.html#CheckState-enum) is an Qt enum which contains the following values.
Value | State  
---|---  
Qt.Unchecked | 0 | The item is unchecked.  
Qt.PartiallyChecked | 1 | The item is partially checked. Items in hierarchical models may be partially checked if some, but not all, of their children are checked.  
Qt.Checked | 2 | The item is checked.  
Note that these enums are just friendly ways to keep track of "magic numbers" that have special meaning in specific circumstances. But the value of `Qt.Unchecked` is literally just `0`, if you test `Qt.Unchecked == 0` you'll find it is `True`.
So if you created the following `data` method, and responded to every `Qt.CheckStateRole` with 2 you'll find that all fields are checked.
python ```
def data(self, index, role):
  if role == Qt.CheckStateRole:
    return 2

```

If you returned 1 for them all they would all appear "partially checked" --
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
python ```
def data(self, index, role):
  if role == Qt.CheckStateRole:
    return 1

```

--- which just so happens to appear as a square in the checkbox.
Coming back to your screenshot, we can now explain why certain boxes are checked and others aren't.
![Screenshot](https://www.pythonguis.com/static/faq/forum/why-did-the-output-on-the-qabstracttablemodel-look-so-strange-when-i-accidentally-omitted-if-role-qt-displayrole/mHuGMCeGVGhCkChIwvFMA7q2FaP.png)
The checked cells are, labeled by (row, column).
  * (1, 3) -- this cell has a value of 2, which is equal to `Qt.Checked`
  * (2, 1) -- this cell has a value of 1, which is equal to `Qt.PartiallyChecked`


All the rest are returning something other than 0, 1, 2 but not `None` and are defaulting to an unchecked state.
Hope that clears it up?
Virginia | 2020-05-09 19:19:20 UTC | #3
Thank you very much @martin ! This is exactly the kind of information I was looking for - an explanation of what happens in the background, and it provides insight into how Model Views work in general. It's fascinating, and very helpful - I'm sort of glad I made this error because this might not have occurred to me otherwise.
Eolinwen | 2020-05-12 16:08:15 UTC | #4
@martin Great explanation that I hope will be in the next version of the book. I keep it in a corner because it was a question that tapped my mind. :slight_smile:
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Why did the output on the QAbstractTableModel look so strange when I accidentally omitted "if role == Qt.DisplayRole:"?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/why-did-the-output-on-the-qabstracttablemodel-look-so-strange-when-i-accidentally-omitted-if-role-qt-displayrole/Python books) on the subject. 
**Why did the output on the QAbstractTableModel look so strange when I accidentally omitted "if role == Qt.DisplayRole:"?** was published in [faq](https://www.pythonguis.com/faq/) on May 09, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [qabstracttablemodel](https://www.pythonguis.com/topics/qabstracttablemodel/) [modelview](https://www.pythonguis.com/topics/modelview/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
