# Content from: https://www.pythonguis.com/faq/pyqt6-vs-pyside6/

[](https://www.pythonguis.com/faq/pyqt6-vs-pyside6/#menu)
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
# PyQt6 vs PySide6
What's the difference between the two Python Qt libraries? ...and what's exactly the same (most of it)
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 01 [ FAQ ](https://www.pythonguis.com/faq/)
There is a new version of Qt (version 6) and with it new versions of PyQt and PySide -- now named PyQt6 & PySide6 respectively. In preparation for the Qt6 editions of my PyQt5 & PySide2 books I've been looking at the latest versions of the libraries to identify the differences between them and find solutions for writing portable code.
Interested in an in-depth guide? My [PySide6 book](https://www.pythonguis.com/pyside6-book) and [the PyQt6 book](https://www.pythonguis.com/pyqt6-book/) are available now!
In this short guide I'll run through why there are two libraries, whether you need to care (spoiler: you don't), what the differences are and how to work around them. By the end you should be comfortable re-using code examples from both PyQt6 and PySide6 tutorials to build your apps, regardless of which package you're using yourself.
## Background
Why are there two libraries?
PyQt is developed by Phil Thompson of [Riverbank Computing Ltd.](https://www.riverbankcomputing.com/software/pyqt/intro) and has existed for a very long time — supporting versions of Qt going back to 2.x. In 2009 Nokia, who owned Qt toolkit at the time, wanted to make the Python bindings for Qt available in a more permissive LGPL license.
It's called _PySide_ because "side" is Finnish for "binder".
The two interfaces were basically equivalent, but over time development of PySide lagged behind PyQt. This was particularly noticeable following the release of Qt 5 — the Qt5 version of PyQt (PyQt5) has been available since mid-2016, while the first stable release of PySide was 2 years later. However, the Qt project has recently adopted PySide as the official [Qt for Python release](https://www.qt.io/qt-for-python) which should ensure its viability going forward. When Qt6 was released, both Python bindings were available shortly after. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
PyQt6 | PySide6  
---|---  
First stable release | Jan 2021 | Dec 2020  
Developed by | Riverbank Computing Ltd. | Qt  
License | GPL or commercial | LGPL  
Platforms | Python 3 | Python 3  
Which should you use? Well, honestly, it doesn't really matter.
Both packages are wrapping the same library — Qt6 — and so have 99.9% identical APIs (see below for the few differences). Anything you learn with one library will be easily applied to a project using the other. Also, no matter with one you choose to use, it's worth familiarizing yourself with the other so you can make the best use of all available online resources — using PyQt6 tutorials to build your PySide6 applications for example, and _vice versa_.
In this short overview I'll run through the few notable differences between the two packages and explain how to write code which works seamlessly with both. After reading this you should be able to take any PyQt6 example online and convert it to work with PySide6.
## Licensing
The main notable difference between the two versions is licensing — with PyQt6 being available under a GPL or commercial license, and PySide6 under a LGPL license.
If you are planning to release your software itself under the GPL, or you are developing software which will not be _distributed_ , the GPL requirement of PyQt6 is unlikely to be an issue. However, if you want to distribute your software but not share your source code you will need to purchase a commercial license from Riverbank for PyQt6 or use PySide6.
Qt itself is available under a _Qt Commercial License_ , GPL 2.0, GPL 3.0 and LGPL 3.0 licenses.
For more information see my FAQ on [the implications of GPL vs LGPL licensing in PyQt/PySide apps](https://www.pythonguis.com/faq/pyqt-vs-pyside/).
## Namespaces & Enums
One of the major changes introduced for PyQt6 is the need to use fully qualified names for enums and flags. Previously, in both PyQt5 and PySide2 you could make use of shortcuts -- for example `Qt.DecorationRole`, `Qt.AlignLeft`. In PyQt6 these are now `Qt.ItemDataRole.DisplayRole` and `Qt.Alignment.AlignLeft` respectively. This change affects all enums and flag groups in Qt. In PySide6 both long and short names remain supported.
The situation is complicated somewhat by the fact that PyQt6 and PySide6 use subtly different naming conventions for _flags_. In PySide6 (and v5) flags are grouped under flag objects with the "Flag" suffix, for example `Qt.AlignmentFlag` -- the _align left_ flag is `Qt.AlignmentFlag.AlignLeft`. The same flag group in PyQt6 is named just "Qt.Alignment". This means that you can't simply choose long or short form and retain compatibility between PyQt6 & PySide6.
## UI files
Another major difference between the two libraries is in their handling of loading `.ui` files exported from Qt Creator/Designer. PyQt6 provides the `uic` submodule which can be used to load UI files directly, to produce an object. This feels pretty Pythonic (if you ignore the camelCase).
python ```
import sys
from PyQt6 import QtWidgets, uic
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("mainwindow.ui")
window.show()
app.exec()

```

The equivalent with PySide6 is one line longer, since you need to create a `QUILoader` object first. Unfortunately the API of these two interfaces is different too (`.load` vs `.loadUI`).
python ```
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
window = loader.load("mainwindow.ui", None)
window.show()
app.exec_()

```

To load a UI onto an existing object in PyQt6, for example in your `QMainWindow.__init__` you can call `uic.loadUI` passing in `self`(the existing widget) as the second parameter.
python ```
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    uic.loadUi("mainwindow.ui", self)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

The PySide6 loader does not support this — the second parameter to `.load` is the _parent_ widget of the widget you're creating. This prevents you adding custom code to the `__init__` block of the widget, but you can work around this with a separate function.
python ```
import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
loader = QUiLoader()
def mainwindow_setup(w):
  w.setWindowTitle("MainWindow Title")
app = QtWidgets.QApplication(sys.argv)
window = loader.load("mainwindow.ui", None)
mainwindow_setup(window)
window.show()
app.exec()

```

## Converting UI files to Python
Both libraries provide identical scripts to generate Python importable modules from Qt Designer `.ui` files. For PyQt6 the script is named `pyuic6` —
bash ```
pyuic6 mainwindow.ui -o MainWindow.py

```

You can then import the `UI_MainWindow` object, subclass using multiple inheritance from the base class you're using (e.g. `QMainWIndow`) and then call `self.setupUI(self)` to set the UI up.
python ```
import sys
from PyQt6 import QtWidgets
from MainWindow import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

For PySide6 it is named `pyside6-uic` —
bash ```
pyside6-uic mainwindow.ui -o MainWindow.py

```

The subsequent setup is identical.
python ```
import sys
from PySide6 import QtWidgets
from MainWindow import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

PyQt's UI compiler features an `-x` flag which can be used to build an executable demo from a UI file. This isn't available in PySide's version.
## exec() or exec_()
The `.exec()` method is used in Qt to start the event loop of your `QApplication` or dialog boxes. In Python 2.7 `exec` was a keyword, meaning it could not be used for variable, function or method names. The solution used in both PyQt4 and PySide was to rename uses of `.exec` to `.exec_()` to avoid this conflict.
Python 3 removed the `exec` keyword, freeing the name up to be used. As a result from PyQt6 `.exec()` calls are named just as in Qt. However, PySide6 still uses `.exec_()`.
## Slots and Signals
Defining custom slots and signals uses slightly different syntax between the two libraries. PySide6 provides this interface under the names `Signal` and `Slot` while PyQt6 provides these as `pyqtSignal` and `pyqtSlot` respectively. The behavior of them both is identical for defining and slots and signals. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
The following PyQt6 and PySide6 examples are identical —
python ```
my_custom_signal = pyqtSignal() # PyQt6
my_custom_signal = Signal() # PySide6
my_other_signal = pyqtSignal(int) # PyQt6
my_other_signal = Signal(int) # PySide6

```

Or for a slot —
python ```
@pyqtslot
def my_custom_slot():
  pass
@Slot
def my_custom_slot():
  pass

```

If you want to ensure consistency across PyQt6 and PySide6 you can use the following import pattern for PyQt6 to use the `Signal` and `@Slot` style there too.
python ```
from PyQt6.QtCore import pyqtSignal as Signal, pyqtSlot as Slot

```

You could of course do the reverse `from PySide6.QtCore import Signal as pyqtSignal, Slot as pyqtSlot` although that's a bit confusing.
## QMouseEvent
In PyQt6 `QMouseEvent` objects no longer have the `.pos()`, `.x()` or `.y()` shorthand property methods for accessing the position of the event. You must use the `.position()` property to get a `QPoint` object and access the `.x()` or `.y()` methods on that. The `.position()` method is also available in PySide6.
## Features in PySide6 but not in PyQt6
As of Qt 6 PySide supports two Python `__feature__` flags to help make code more _Pythonic_ with `snake_case` variable names and the ability to assign and access properties directly, rather than using getter/setter functions. The example below shows the impact of these changes on code --
python ```
table = QTableWidget()
table.setColumnCount(2)
button = QPushButton("Add")
button.setEnabled(False)
layout = QVBoxLayout()
layout.addWidget(table)
layout.addWidget(button)

```

The same code, but with `snake_case` and `true_property` enabled.
python ```
from __feature__ import snake_case, true_property
table = QTableWidget()
table.column_count = 2
button = QPushButton("Add")
button.enabled = False
layout = QVBoxLayout()
layout.add_widget(table)
layout.add_widget(button)

```

These feature flags are a nice improvement for code readability, however as they are not supported in PyQt6 it makes writing portable code more difficult.
## Supporting both in libraries
You don't need to worry about this if you're writing a standalone app, just use whichever API you prefer.
If you're writing a library, widget or other tool you want to be compatible with both PyQt6 and PySide6 you can do so easily by adding both sets of imports.
python ```
import sys
if 'PyQt6' in sys.modules:
  # PyQt6
  from PyQt6 import QtGui, QtWidgets, QtCore
  from PyQt6.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
else:
  # PySide6
  from PySide6 import QtGui, QtWidgets, QtCore
  from PySide6.QtCore import Signal, Slot

```

This is the approach used in our custom widgets library, where we support for PyQt6 and PySide6 with a single library import. The only caveat is that you must ensure PyQt6 is imported before (as in on the line above or earlier) when importing this library, to ensure it is in `sys.modules`.
To account for the lack of shorthand enum and flags in PyQt6 you can generate these yourself. For example, the following code will copy references for each of the enum objects elements up to their parent object, making them accessible as in PyQt5, PySide2 & PySide6. The code would only need to be run under PyQt6.
python ```
enums = [
  (QtCore.Qt, 'Alignment'),
  (QtCore.Qt, 'ApplicationAttribute'),
  (QtCore.Qt, 'CheckState'),
  (QtCore.Qt, 'CursorShape'),
  (QtWidgets.QSizePolicy, 'Policy'),
]
# Look up using the long name (e.g. QtCore.Qt.CheckState.Checked, used
# in PyQt6) and store under the short name (e.g. QtCore.Checked, used
# in PyQt5, PySide2 & accepted by PySide6).
for module, enum_name in enums:
  for entry in getattr(module, enum_name):
    setattr(module, entry.name, entry)

```

Alternatively, you can define a custom function to handle the namespace lookup.
python ```
def _enum(obj, name):
  parent, child = name.split('.')
  result = getattr(obj, child, False)
  if result: # Found using short name only.
    return result
  obj = getattr(obj, parent) # Get parent, then child.
  return getattr(obj, child)

```

When passed an object and a PyQt6 compatible long-form name, this function will return the correct enum or flag on both PyQt6 and PySide6.
python ```
>>> _enum(PySide6.QtCore.Qt, 'Alignment.AlignLeft')
PySide6.QtCore.Qt.AlignmentFlag.AlignLeft
>>> _enum(PyQt6.QtCore.Qt, 'Alignment.AlignLeft')
<Alignment.AlignLeft: 1>

```

The final complication is the mismatch in the `exec_()` and `exec()` method calls. You can work around this by implementing a function to check the presence of each method and call whichever exists.
python ```
def _exec(obj):
  if hasattr(obj, 'exec'):
    return obj.exec()
  else:
    return obj.exec_()

```

You can then use this function to _exec_ objects like `QApplication` and `QDialog` in a portable way on both PyQt6 and PySide6.
python ```
app = QApplication(sys.argv)
_exec(app)

```

If you're doing this in multiple files it can get a bit cumbersome. A nice solution to this is to move the import logic and custom shim methods to their own file, e.g. named `qt.py` in your project root. This module imports the Qt modules (`QtCore`, `QtGui`, `QtWidgets`, etc.) from one of the two libraries, and then you import into your application from there.
The contents of the `qt.py` are the same as we used earlier —
python ```
import sys
if 'PyQt6' in sys.modules:
  # PyQt6
  from PyQt6 import QtGui, QtWidgets, QtCore
  from PyQt6.QtCore import pyqtSignal as Signal, pyqtSlot as Slot

else:
  # PySide6
  from PySide6 import QtGui, QtWidgets, QtCore
  from PySide6.QtCore import Signal, Slot

def _enum(obj, name):
  parent, child = name.split('.')
  result = getattr(obj, child, False)
  if result: # Found using short name only.
    return result
  obj = getattr(obj, parent) # Get parent, then child.
  return getattr(obj, child)

def _exec(obj):
  if hasattr(obj, 'exec'):
    return obj.exec()
  else:
    return obj.exec_()

```

You must remember to add any other PyQt6 modules you use (browser, multimedia, etc.) in both branches of the if block. You can then import _Qt6_ into your own application as follows —
python ```
from .qt import QtGui, QtWidgets, QtCore, _enum, _exec

```

...and it will work seamlessly across either library.
## That's really it
There's not much more to say — the two libraries really are that similar. However, if you do stumble across any other PyQt6/PySide6 examples or features which you can't easily convert, drop me a note.
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PyQt6 vs PySide6** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyqt6-vs-pyside6/Python books) on the subject. 
**PyQt6 vs PySide6** was published in [faq](https://www.pythonguis.com/faq/) on March 12, 2021 (updated April 01, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [pyside](https://www.pythonguis.com/topics/pyside/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [qt](https://www.pythonguis.com/topics/qt/) [qt6](https://www.pythonguis.com/topics/qt6/) [python](https://www.pythonguis.com/topics/python/)
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
