# Content from: https://www.pythonguis.com/faq/pyside2-vs-pyside6/

[](https://www.pythonguis.com/faq/pyside2-vs-pyside6/#menu)
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
# PySide2 vs PySide6
What are the differences, and is it time to upgrade?
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Oct 12 [ FAQ ](https://www.pythonguis.com/faq/)
If you are already developing Python GUI apps with PySide2, you might be asking yourself whether it's time to upgrade to PySide6 and use the latest version of the Qt library. In this article we'll look at the main differences between PySide2 and PySide6, benefits of upgrading and problems you might encounter when doing so.
If you're starting out and having trouble deciding, don't worry! I have both a [PySide2 ebook](https://www.pythonguis.com/pyside2-book/) and [PySide6 ebook](https://www.pythonguis.com/pyside6-book/) available. If you get both, you get a heavy discount since they're fundamentally the same.
## Background
Qt is a GUI _framework_ written in the C++ programming language created by _Trolltech_ , now developed by The Qt Company. They also maintain the _Qt for Python_ project, which provides the official Python binding for Qt under the name _PySide_.
The name _PySide_ was chosen because the word _side_ means _binding_ in the Finnish language.
While the development of Qt started in 1992, it wasn't until 2009 that the Python binding _PySide_ became available. Development of _PySide_ lagged behind Qt for many years, and the _other_ Python binding _PyQt_ became more popular. However, in recent years _The Qt Company_ have been putting increased resources into development, and it now tracks Qt releases closely.
The first version of PySide6 was released on December 10, 2020, just two days after the release of Qt6 itself.
## Upgrading from PySide2 to PySide6
The upgrade path from _PySide2_ to _PySide6_ is very straightforward. For most applications, just renaming the imports from `PySide2` to `PySide6` will be enough to convert your application to work with the new library. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
If you are considering upgrading, I recommend you try this first and see if works -- if not, take a look at the differences below and see if they apply to your project.
## Where things might go wrong
Let’s get acquainted with a few differences between the two versions to know how to write code that works seamlessly with both. After reading this, you should be able to take any PySide2 example online and convert it to work with PySide6. These changes reflect underlying differences in Qt6 vs. Qt5 and aren't unique to PySide itself.
If you’re still using Python 2.x, note that PySide6 is available only for Python 3.x versions.
### `QAction` moved
In Qt6 the `QAction` class, which is used for creation toolbars and menus, has been moved from the _QtWidgets_ to the _QtGui_ module.
  * PySide2
  * PySide6


python ```
from PySide2.QtWidgets import QAction

```

python ```
from PySide6.QtGui import QAction

```

This may seem strange, but the move makes sense since _actions_ can also be used in QML (non-widgets) applications.
### High DPI Scaling
The high DPI (_dots per inch_) scaling attributes `Qt.AA_EnableHighDpiScaling`, `Qt.AA_DisableHighDpiScaling` and `Qt.AA_UseHighDpiPixmaps` have been deprecated because high DPI is enabled by default in PySide6 and can’t be disabled.
### QMouseEvent
`QMouseEvent.pos()` and `QMouseEvent.globalPos()` methods returning a `QPoint` object as well as `QMouseEvent.x()` and `QMouseEvent.y()` returning an `int` object have been deprecated – use `QMouseEvent.position()` and `QMouseEvent.globalPosition()` returning a `QPointF` object instead, so like `QMouseEvent.position().x()` and `QMouseEvent.position().y()`.
`Qt.MidButton` has been renamed to `Qt.MiddleButton`
### Platform specific
Finally, platform-specific methods in the `QtWin` and `QtMac` modules have been deprecated, in favor of using the native calls instead. In PySide applications the only likely consequence of this will be the `setCurrentProcessExplicitAppUserModelID` call to set an application ID, for taskbar icon grouping on Windows.
  * QtWin
  * Native


python ```
try:
  # Include in try/except block if you're also targeting Mac/Linux
  from PySide2.QtWinExtras import QtWin
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
  * All methods named `.exec_()` (in classes `QCoreApplication`, `QDialog`, and `QEventLoop`) have been deprecated, and should be replaced with `.exec()` which became possible since Python 3. However, they are still available under the underscored names for backwards compatibility.


## `snake_case` and the new `true_property`
PySide2 introduced the `snake_case` feature to write Qt method names – like `.addWidget()` – in a Python-friendly snake-case style like `.add_widget()`. This allows your PySide code to follow the Python standard PEP8 style.
Introduced in PySide6 is a new feature which allows direct access to Qt properties as Python object properties, eliminating the _setter_ and _getter_ methods. This can be enabled explicitly on a per-module basis by importing the `true_property` feature.
The example below demonstrates the effect on PySide6 code of applying both these features.
  * Standard API
  * Pythonic API


python ```
table = QTableWidget()
table.setColumnCount(2)
button = QPushButton("Add")
button.setEnabled(False)
layout = QVBoxLayout()
layout.addWidget(table)
layout.addWidget(button)

```

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

As you can see, the `true_property` feature allows you to assign a value to a Qt property directly – rather than using _setters_.
In the pre-PySide6 code, you could only do `.setEnabled(False)` to set the _enabled_ property of a widget to the value _False_ , hence disabling the widget. However, with `true_property` enabled, you can set a property directly with, for example, `button.enabled = False`. While this may seem like a cosmetic change, following _Pythonic_ style in this way makes code easier for Python developers to understand and maintain.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt5](https://www.pythonguis.com/static/theme/images/products/pyside2-book.png)](https://www.pythonguis.com/pyside2-book/)
[Take a look ](https://www.pythonguis.com/pyside2-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/create-gui-applications-pyside/) and [Amazon Paperback](https://www.amazon.com/dp/B08R92BW7R/)
### PySide6 demo
Let’s demonstrate how these two features could be valuable in your PySide6 code.
python ```
import sys
import random
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import (
  QLabel,
  QWidget,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QApplication,
)
# Import snake_case and true_property after PySide6 imports.
from __feature__ import snake_case, true_property

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    # Since QMainWindow does not have a fixedSize property,
    # we use the setFixedSize() method but call it in the
    # snake-case style.
    self.set_fixed_size(300, 100)
    # However, QMainWindow does have a windowTitle property
    # for which we assign a value directly but must write
    # the property's name in snake-case style.
    self.window_title = "PySide6 Translator"
    # And this is our non-Qt Python property to which
    # we must assign a value just like above anyway,
    # so assigning values to properties uniformly
    # throughout our code could be intriguing.
    self.multilingual_greetings = (
      "Привет мир!",  # Russian ("Privet mir!" in Cyrillic)
      "Hallo Welt!",  # German
      "¡Hola Mundo!",  # Spanish
      "Hei maailma!",  # Finnish
      "Helló Világ!",  # Hungarian
      "Hallo Wereld!", # Dutch
    )
    # We create a label with an English greeting by default.
    self.greeting = QLabel("Hello world!")
    # Instead of self.message.setAlignment(Qt.AlignCenter),
    # we set a value to the alignment property directly...
    self.greeting.alignment = Qt.AlignCenter
    # We now also create a button to translate our
    # English greeting and then connect it with
    # our translate_greeting() slot.
    self.translate_button = QPushButton("Translate")
    self.translate_button.clicked.connect(self.translate_greeting)
    self.vertical_layout = QVBoxLayout()
    self.vertical_layout.add_widget(self.greeting)
    self.vertical_layout.add_widget(self.translate_button)
    self.widget_container = QWidget()
    self.widget_container.set_layout(self.vertical_layout)
    # Instead of calling .setCentralWidget(),
    # we call it by its snake-case name...
    self.set_central_widget(self.widget_container)
  @Slot()
  def translate_greeting(self):
    # Here, instead of using the .setText() method,
    # we set a value to the text property directly...
    self.greeting.text = random.choice(self.multilingual_greetings)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  app.exec()

```

## `.exec()` or `.exec_()`?
The `.exec()` method in Qt starts the event loop of your `QApplication` or dialog boxes. In Python 2.7, `exec` was a keyword, meaning that it could not be used as a variable name, a function name, or a method name. The solution used in PySide was to name the method as `.exec_()` – adding a trailing underscore – to avoid a conflict.
Python 3.0 removed the `exec` keyword, freeing up the name to be used. And since PySide6 targets only Python 3.x versions, it currently deprecates the workaround name and will later remove it. The `.exec()` method is named just as in Qt itself. However, the `.exec_()` name only exists for short-term backward compatibility with old code.
If your code must target PySide2 and PySide6 libraries, you can use `.exec_()`, but beware that this method name will be removed.
## Missing modules
This isn’t a concern anymore, but when Qt6 was new, not _all_ of the Qt modules had been ported yet, and so were not available in PySide6. If you needed any of these modules, the upgrade to PySide6 was not desirable then. Fast forward to Qt 6.2 and PySide 6.2, the good news is that _all_ of those missing modules are now back. You can upgrade with no hesitation.
## Is it time to upgrade?
Whether or not it's time to upgrade depends on your project. If you're starting out learning PySide (or GUI programming in general), you may prefer to stick with PySide2 for the time being as there are more examples available for PySide2 online. While the differences are minor, anything not working is confusing when you learn. Anything you know using PySide2 will carry over when you choose to upgrade to PySide6.
However, if you're starting a new project and are reasonably familiar with PySide/Qt, I'd recommend jumping into PySide6 now.
If you want to get started with PySide6, the [PySide6 book](https://www.pythonguis.com/pyside6-book?aid=139759) is available with all code examples updated for this latest PySide edition.
## `PySide` Backwards compatibility
If you're developing software that's targeting both PySide2 and PySide6 you can use conditional imports to import the classes from whichever module is loaded.
python ```
try:
  from PySide6 import QtWidgets, QtGui, QtCore # ...
except ImportError:
  from PySide2 import QtWidgets, QtGui, QtCore # ...

```

If you add these imports to a file in the root of your project named `qt.py`. You can then, in your own code files import use `from qt import QtWidgets` and the available library will be imported automatically.
Note however, that importing in this way won't work around any of the other differences between PySide2 and PySide6 mentioned above. For that, we recommend using the _QtPy_ library.
## Universal compatibility
If you need to support _all_ Python Qt libraries (PySide2, PySide6, PyQt5, PyQt6) or are dependent on features which have changed between versions of Qt, then you should consider using [QtPy](https://github.com/spyder-ide/qtpy). This package is a small abstraction layer around all versions of the Qt libraries, which allows you to use them interchangeably (as far as possible) in your applications.
If you're developing Python libraries or applications that need to be portable across different versions it is definitely worth a look.
## Conclusion
As we've discovered, there are no major differences between PySide2 and PySide6. The changes that are there can be easily worked around. If you are new to Python GUI programming with Qt you may find it easier to start with PySide2 still, but for any new project I'd suggest [starting with PySide6](https://www.pythonguis.com/pyside6-tutorial/). It is an LTS (_Long Term Support_) version. If you’re not upgrading for the benefits, which are not significant, do it for the long-term bug fixes. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PySide2 vs PySide6** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) with contributions from [Boštjan Mejak](https://www.pythonguis.com/authors/bostjan-mejak/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyside2-vs-pyside6/Python books) on the subject. 
**PySide2 vs PySide6** was published in [faq](https://www.pythonguis.com/faq/) on January 31, 2022 (updated October 12, 2023) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyside2](https://www.pythonguis.com/topics/pyside2/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [qt](https://www.pythonguis.com/topics/qt/) [upgrade](https://www.pythonguis.com/topics/upgrade/) [qt6](https://www.pythonguis.com/topics/qt6/) [pyside](https://www.pythonguis.com/topics/pyside/) [ licensing](https://www.pythonguis.com/topics/licensing/) [python](https://www.pythonguis.com/topics/python/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
