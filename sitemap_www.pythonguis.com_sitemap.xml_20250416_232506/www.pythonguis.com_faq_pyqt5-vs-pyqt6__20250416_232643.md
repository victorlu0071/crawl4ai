# Content from: https://www.pythonguis.com/faq/pyqt5-vs-pyqt6/

[](https://www.pythonguis.com/faq/pyqt5-vs-pyqt6/#menu)
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
# PyQt5 vs PyQt6
What are the differences, and is it time to upgrade?
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Oct 12 [ FAQ ](https://www.pythonguis.com/faq/)
If you are already developing Python GUI apps with PyQt5, you might be asking yourself whether it's time to upgrade to PyQt6 and use the latest version of the Qt library. In this article we'll look at the main differences between PyQt5 and PyQt6, benefits of upgrading and problems you might encounter when doing so.
If you're starting out and having trouble deciding, don't worry! I have both a [PyQt5 ebook](https://www.pythonguis.com/pyqt5-book/) and [PyQt6 ebook](https://www.pythonguis.com/pyqt6-book/) available. If you get both, you get a heavy discount since they're fundamentally the same.
## Background
Qt is a GUI _framework_ written in the C++ programming language created by _Trolltech_ , now developed by The Qt Company. There are two Python bindings: _PySide_ and _PyQt_. The former is developed in-house by The Qt Company while _PyQt_ is developed independently by Riverbank Computing Ltd. The first version of PyQt6 was released on January 4th, 2021, just one month after the release of Qt6 itself.
For more information on the differences between the latest versions of the two bindings, take a look at [PyQt6 vs PySide6](https://www.pythonguis.com/faq/pyqt6-vs-pyside6/).
## Upgrading from PyQt5 to PyQt6
The upgrade path from _PyQt5_ to _PyQt6_ is fairly straightforward, with one main gotcha. For some applications, just renaming the imports from `PyQt5` to `PyQt6` will be enough to convert your application to work with the new library. For most however, you will need to account for changes in both PyQt and Qt itself.
Let’s get acquainted with a few differences between the two versions to know how to write code that works seamlessly with both. After reading this, you should be able to take any PyQt5 example online and convert it to work with PyQt6.
### Enums
The change mostly likely to impact your projects is the removal of the short-form names for enum members. In PyQt6 all enum members must be named using their fully qualified names. This applies to all enums and flags, including those in the `QtCore.Qt` namespace. For example the `Qt.Checked` flag in PyQt6 becomes `Qt.CheckState.Checked`. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
  * PyQt5
  * PyQt6


python ```
widget = QCheckBox("This is a checkbox")
widget.setCheckState(Qt.Checked)

```

python ```
widget = QCheckBox("This is a checkbox")
widget.setCheckState(Qt.CheckState.Checked)

```

There are too many updated values to mention them all here. But if you're converting a codebase you can usually just search online for the short-form and the longer form will be in the results.
The _good news_ is that the change is backwards compatible: the fully-qualified names also work in PyQt5. So you can make the changes in your PyQt5 code _before_ beginning the upgrade progress.
### `.exec()` or `.exec_()`?
The `.exec()` method in Qt starts the event loop of your `QApplication` or dialog boxes. In Python 2.7, `exec` was a keyword, meaning that it could not be used as a variable name, a function name, or a method name. In earlier versions of PyQt the method was renamed as `.exec_()` – adding a trailing underscore – to avoid a conflict.
Python 3.0 removed the `exec` keyword, freeing up the name to be used. And since PyQt6 targets only Python 3.x versions, the underscored names have been removed. These were previously _deprecated_ in PyQt5, and the `.exec()` method will work there too.
### No more QResources
PyQt6 has removed support for Qt's Resource Framework. For packaging data files with your applications, you can use [PyInstaller's data file support](https://www.pythonguis.com/tutorials/packaging-pyqt6-applications-windows-pyinstaller/).
## Differences in Qt6
In addition to the changes above there are many other minor changes that reflect underlying differences in Qt6 vs. Qt5 and aren't unique to PyQt itself.
### `QAction` moved
In Qt6 the `QAction` class, which is used for creation toolbars and menus, has been moved from the _QtWidgets_ to the _QtGui_ module.
  * PyQt5
  * PyQt6


python ```
from PyQt5.QtWidgets import QAction

```

python ```
from PyQt6.QtGui import QAction

```

This may seem strange, but the move makes sense since _actions_ can also be used in QML (non-widgets) applications.
### High DPI Scaling
The high DPI (_dots per inch_) scaling attributes `Qt.AA_EnableHighDpiScaling`, `Qt.AA_DisableHighDpiScaling` and `Qt.AA_UseHighDpiPixmaps` have been deprecated because high DPI is enabled by default in PyQt6 and can’t be disabled.
### QMouseEvent
`QMouseEvent.pos()` and `QMouseEvent.globalPos()` methods returning a `QPoint` object as well as `QMouseEvent.x()` and `QMouseEvent.y()` returning an `int` object have been deprecated – use `QMouseEvent.position()` and `QMouseEvent.globalPosition()` returning a `QPointF` object instead, so like `QMouseEvent.position().x()` and `QMouseEvent.position().y()`.
`Qt.MidButton` has been renamed to `Qt.MiddleButton`
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
### Platform specific
Finally, platform-specific methods in the `QtWin` and `QtMac` modules have been deprecated, in favor of using the native calls instead. In PyQt applications the only likely consequence of this will be the `setCurrentProcessExplicitAppUserModelID` call to set an application ID, for taskbar icon grouping on Windows.
  * QtWin
  * Native


python ```
try:
  # Include in try/except block if you're also targeting Mac/Linux
  from PyQt5.QtWinExtras import QtWin
  myappid = 'com.learnpyqt.examples.helloworld'
  QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
  pass

```

python ```
try:
  # Include in try/except block if you're also targeting Mac/Linux
  from ctypes import windll # Only exists on Windows.
  myappid = 'mycompany.myproduct.subproduct.version'
  windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
  pass

```

### Miscellaneous
  * `QDesktopWidget` has been removed – use `QScreen` instead, which can be retrieved using `QWidget.screen()`, `QGuiApplication.primaryScreen()`, or `QGuiApplication.screens()`.
  * `.width()` of `QFontMetrics` has been renamed to `.horizontalAdvance()`.
  * `.get()` of `QOpenGLVersionFunctionsFactory()` has been recommended to be used instead of `.versionFunctions()` of `QOpenGLContext()` when obtaining any functions of the _Open GL_ library.
  * `QRegularExpression` has replaced `QRegExp`.
  * `QWidget.mapToGlobal()` and `QWidget.mapFromGlobal()` now accept and return a `QPointF` object.


## Missing modules
This isn’t a concern anymore, but when Qt6 was new, not _all_ of the Qt modules had been ported yet, and so were not available in PyQt. If you needed any of these modules, the upgrade to PyQt6 was not previously workable. Fast forward to Qt 6.2 and PyQt 6.2, the good news is that _all_ of those missing modules are now back, so you can upgrade without problems.
## Is it time to upgrade?
Whether or not it's time to upgrade depends on your project. If you're starting out learning PyQt (or GUI programming in general), you may prefer to stick with PyQt5 for the time being as there are far more examples available online. While the differences are relatively minor, anything not working is confusing when you are learning something new. Anything you learn with PyQt5 will carry over to PyQt6, so you can switch once you're a bit more confident.
If you're starting a new project however, or are reasonably familiar with PyQt, I'd recommend jumping into PyQt6 now.
If you want to get started with PyQt6, the [PyQt6 book](https://www.pythonguis.com/pyqt6-book?aid=139759) is available with all code examples updated for this latest edition of PyQt.
## `PyQt` Backwards compatibility
If you're developing software that's targeting both PyQt5 and PyQt6 you can use conditional imports to import the classes from whichever module is loaded.
python ```
try:
  from PyQt6 import QtWidgets, QtGui, QtCore # ...
except ImportError:
  from PyQt5 import QtWidgets, QtGui, QtCore # ...

```

If you add these imports to a file in the root of your project named `qt.py`. You can then, in your own code files import use `from qt import QtWidgets` and the available library will be imported automatically.
If you use the fully-qualified names for enums and `exec()` then many applications previously written in PyQt5 will work as-is. However, importing in this way won't work around any of the differences between Qt5 and Qt6 mentioned above. For that, we recommend using the _QtPy_ library.
## Universal compatibility
If you need to support _all_ Python Qt libraries (PyQt5, PyQt6, PySide2, PySide6) or are dependent on features which have changed between versions of Qt, then you should consider using [QtPy](https://github.com/spyder-ide/qtpy). This package is a small abstraction layer around all versions of the Qt libraries, which allows you to use them interchangeably (as far as possible) in your applications.
If you're developing Python libraries or applications that need to be portable across different versions it is definitely worth a look.
## Conclusion
As we've discovered, there are no major differences between PyQt5 and PyQt6. The changes that are there can be easily worked around. If you are new to Python GUI programming with Qt you may find it easier to start with PyQt5 still, but for any new project I'd suggest [starting with PyQt6](https://www.pythonguis.com/pyqt6-tutorial/). 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PyQt5 vs PyQt6** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) with contributions from [Boštjan Mejak](https://www.pythonguis.com/authors/bostjan-mejak/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyqt5-vs-pyqt6/Python books) on the subject. 
**PyQt5 vs PyQt6** was published in [faq](https://www.pythonguis.com/faq/) on February 03, 2022 (updated October 12, 2023) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [qt](https://www.pythonguis.com/topics/qt/) [upgrade](https://www.pythonguis.com/topics/upgrade/) [qt6](https://www.pythonguis.com/topics/qt6/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ licensing](https://www.pythonguis.com/topics/licensing/) [python](https://www.pythonguis.com/topics/python/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
