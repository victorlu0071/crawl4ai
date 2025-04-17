# Content from: https://www.pythonguis.com/faq/about-pyqt6-and-pyside6/

[](https://www.pythonguis.com/faq/about-pyqt6-and-pyside6/#menu)
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
# When will there be a new version of Creating GUI Applications for PyQt6 and PySide6?
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 02 [ FAQ ](https://www.pythonguis.com/faq/)
It's out now! Get the [PyQt6 Edition](https://www.pythonguis.com/pyqt6-book) or [PySide6 Edition](https://www.pythonguis.com/pyside6-book)
I'm currently in the process of updating my book _Creating GUI Applications with Python and QT_ for the Qt6 releases of Qt. While these new versions are largely backwards compatible with Qt5 there are a number of signficant differences which will cause issues when migrating.
We now also have migration guides for moving from [PyQt5 to PyQt6](https://www.pythonguis.com/faq/pyqt5-vs-pyqt6/) or [PySide2 to PySide6](https://www.pythonguis.com/faq/pyside2-vs-pyside6/).
One major difference only applies to PyQt6: Riverbank Software have removed `QResource` support from PyQt6. If you have no idea what that is, don't worry, you're not alone. The _QResource System_ is used to manage application resources -- think images, icons, stylesheets -- from within Qt Designer. By _compiling_ these resources into Python code they could be used directly from within the application without needing to worry about paths.
If this sounds pretty useful _it is_ , but it's not commonly used: probably because managing the assets in Qt Designer isn't particularly friendly.
Some other thoughts from the migration --
  * PyQt6 is less directly source-compatible with PyQt6 than PySide6. In PyQt6 the namespaces have been moved under Python Enums so e.g. `Qt.DisplayRole` is now under `Qt.ItemDataRole.DisplayRole`. The same structure exists now in PySide6, but the old locations are retained, so it's backwards compatible `Qt.ItemDataRole.BackgroundRole == Qt.BackgroundRole`. **I'm 50/50 on whether to use the _new_ style in the PySide6 book -- thoughts?**
  * (PyQt6 & PySIde6) `QAction` is now in `QtGui` not `QtWidgets`. This always caught me out (since it's not a widget) so I think it's a good change. But it's hard to auto-migrate.
  * (PyQt6 & PySIde6) Retrieving a pixmap now seems to return a copy: if you get a labels pixmap and draw on it, it doesn't affect the widget. Required a rewrite of the custom widget code. May be missing something here, early days.
  * (PyQt6) `QMouseEvent` now doesn't have `.x()` or `.y()` which is odd. You need to get a position via `QMouseEvent.position()` instead.


In addition in PySide6.1, the following functions are all deprecated: 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
python ```
QEnterEvent.globalPos()
QEnterEvent.globalX()
QEnterEvent.globalY()
QEnterEvent.localPos()
QEnterEvent.pos()
QEnterEvent.QEnterEvent.screenPos()
QEnterEvent.QEnterEvent.windowPos()
QEnterEvent.QEnterEvent.x()
QEnterEvent.QEnterEvent.y()

```

It is still early days, and it's quite possible I'll find more incompatibilities as I dig further. The next version of the book should be out, at least in an "early access" form, by next week. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
For an up to date migration guide see [PyQt5 to PyQt6](https://www.pythonguis.com/faq/pyqt5-vs-pyqt6/) or [PySide2 to PySide6](https://www.pythonguis.com/faq/pyside2-vs-pyside6/).
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**When will there be a new version of Creating GUI Applications for PyQt6 and PySide6?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/about-pyqt6-and-pyside6/Python books) on the subject. 
**When will there be a new version of Creating GUI Applications for PyQt6 and PySide6?** was published in [faq](https://www.pythonguis.com/faq/) on February 12, 2021 (updated September 02, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
