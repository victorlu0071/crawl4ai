# Content from: https://www.pythonguis.com/faq/how-to-make-qsplitter-responds-to-double-clicking/

[](https://www.pythonguis.com/faq/how-to-make-qsplitter-responds-to-double-clicking/#menu)
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
# How to make QSplitter responds to double clicking?
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
Scoodood | 2020-09-25 05:16:36 UTC | #1
The default [QSplitter Widget](https://doc.qt.io/qtforpython/PySide2/QtWidgets/QSplitter.html) only has `splitterMoved` signal. I would like to add a `doubleClicked` signal so that I can make the QSplitter widget can move all the way to the left on a double clicking event, and then double clicking it again will restore to its previous position. Below are my starter code. Any idea how to go from here?
python ```
from PySide2 import QtWidgets, QtCore
class Example(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()   
    splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
    textedit1 = QtWidgets.QTextEdit()
    textedit2 = QtWidgets.QTextEdit()
    splitter.addWidget(textedit1)
    splitter.addWidget(textedit2)
    splitter.setSizes([200,200])
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(splitter)
    self.setLayout(layout)    
    splitter.splitterMoved.connect(self.handler)
    # trying to do something like this...
    #splitter.doubleClicked.connect(self.handler)
  def handler(self, pos):
    print('pos', pos)
if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  w = Example()
  w.show()
  app.exec_()

```

martin | 2020-09-30 20:45:37 UTC | #2
Hey @Scoodood I knocked together a simple custom widget for this -- it implements a double click event handler which stores and restores a slide position. 
python ```

class ToggleSplitter(QtWidgets.QSplitter):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # Store the previos size of the left hand panel.
    self._previous_state = None
  def mouseDoubleClickEvent(self, e):
    sizes = self.sizes()
    if sizes[0] == 0 and self._previous_state:
      sizes = self._previous_state
    else:
      # Store the size so we can return to it.
      self._previous_state = sizes[:] # store copy so change below doesn't affect stored.
      sizes[0] = 0
    self.setSizes(sizes)

```

If you run it you'll notice the slight problem -- you can't actually double click on the splitter itself, just on the (tiny space) in the frame next to it. Move your mouse around the edge of the splitter until it turns into an arrow, then double click.
The problem is that `QSplitter` is a compound widget with the handles themselves [QSplitterHandle](https://doc.qt.io/qt-5/qsplitterhandle.html) objects. However, `QSplitter` has a `createHandle` method we can override allowing us to return our own custom handles -- and we can put our double-click handler on there instead.
Full working example ...
1:1 Coaching & Tutoring for your Python GUIs project
[![Martin Fitzpatrick Python GUIs Coaching & Training](https://www.pythonguis.com/static/theme/images/products/coaching.jpg)](https://calendly.com/martinfitzpatrick/60min-python-guis-coaching)
[60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/) [Book Now](https://www.pythonguis.com/live/)
1:1 Python GUIs Coaching & Training
**Comprehensive code review** • **Bugfixes** & improvements • **Maintainability** advice and **architecture** improvements • **Design and usability** assessment • Suggestions and tips to **expand your knowledge** • **Packaging and distribution** help for Windows, Mac & Linux • [Find out more.](https://www.pythonguis.com/live)
python ```
from PySide2 import QtWidgets, QtCore

class ToggleSplitterHandle(QtWidgets.QSplitterHandle):
  def mouseDoubleClickEvent(self, e):
    self.parent().toggle_collapse()

class ToggleSplitter(QtWidgets.QSplitter):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # Store the previos size of the left hand panel.
    self._previous_state = None
  def createHandle(self):
    return ToggleSplitterHandle(self.orientation(), self)
  def toggle_collapse(self):
    sizes = self.sizes()
    if sizes[0] == 0 and self._previous_state:
      sizes = self._previous_state
    else:
      # Store the size so we can return to it.
      self._previous_state = sizes[:] # store copy so change below doesn't affect stored.
      sizes[0] = 0
    self.setSizes(sizes)

class Example(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()   
    splitter = ToggleSplitter(QtCore.Qt.Horizontal)
    textedit1 = QtWidgets.QTextEdit()
    textedit2 = QtWidgets.QTextEdit()
    splitter.addWidget(textedit1)
    splitter.addWidget(textedit2)
    splitter.setSizes([200,200])
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(splitter)
    self.setLayout(layout)    
    splitter.splitterMoved.connect(self.handler)
  def handler(self, pos):
    print('pos', pos)
if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  w = Example()
  w.show()
  app.exec_()

```

Scoodood | 2020-09-30 20:59:09 UTC | #3 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Thanks @martin. This is awesome!! 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**How to make QSplitter responds to double clicking?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/how-to-make-qsplitter-responds-to-double-clicking/Python books) on the subject. 
**How to make QSplitter responds to double clicking?** was published in [faq](https://www.pythonguis.com/faq/) on September 25, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyside](https://www.pythonguis.com/topics/pyside/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
