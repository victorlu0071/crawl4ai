# Content from: https://www.pythonguis.com/widgets/qcolorbutton-a-color-selector-tool-for-pyqt/

[](https://www.pythonguis.com/widgets/qcolorbutton-a-color-selector-tool-for-pyqt/#menu)
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
# ColorButton
A color-selector tool for PyQt
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ Python GUI Widget Library ](https://www.pythonguis.com/widgets/)
Below is a short snippet to implement a color-picker attached to a button in Qt. Clicking on the button pops up a dialog (native) to select a color. The color is shown by the color of the button face. You can provide a _default_ color which will be the initial state of the button when it is created -- right-clicking on the button will reset the color to this default value (or `None` if no default is set)
To get the currently set color, use `button.color()`.
  * PyQt5
  * PySide


python ```
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
class ColorButton(QtWidgets.QPushButton):
  '''
  Custom Qt Widget to show a chosen color.
  Left-clicking the button shows the color-chooser, while
  right-clicking resets the color to None (no-color).
  '''
  colorChanged = pyqtSignal(object)
  def __init__(self, *args, color=None, **kwargs):
    super().__init__(*args, **kwargs)
    self._color = None
    self._default = color
    self.pressed.connect(self.onColorPicker)
    # Set the initial/default state.
    self.setColor(self._default)
  def setColor(self, color):
    if color != self._color:
      self._color = color
      self.colorChanged.emit(color)
    if self._color:
      self.setStyleSheet("background-color: %s;" % self._color)
    else:
      self.setStyleSheet("")
  def color(self):
    return self._color
  def onColorPicker(self):
    '''
    Show color-picker dialog to select color.
    Qt will use the native dialog by default.
    '''
    dlg = QtWidgets.QColorDialog(self)
    if self._color:
      dlg.setCurrentColor(QtGui.QColor(self._color))
    if dlg.exec_():
      self.setColor(dlg.currentColor().name())
  def mousePressEvent(self, e):
    if e.button() == Qt.RightButton:
      self.setColor(self._default)
    return super().mousePressEvent(e)

```

python ```
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, Signal

class ColorButton(QtWidgets.QPushButton):
  '''
  Custom Qt Widget to show a chosen color.
  Left-clicking the button shows the color-chooser, while
  right-clicking resets the color to None (no-color).
  '''
  colorChanged = Signal(object)
  def __init__(self, *args, color=None, **kwargs):
    super().__init__(*args, **kwargs)
    self._color = None
    self._default = color
    self.pressed.connect(self.onColorPicker)
    # Set the initial/default state.
    self.setColor(self._default)
  def setColor(self, color):
    if color != self._color:
      self._color = color
      self.colorChanged.emit(color)
    if self._color:
      self.setStyleSheet("background-color: %s;" % self._color)
    else:
      self.setStyleSheet("")
  def color(self):
    return self._color
  def onColorPicker(self):
    '''
    Show color-picker dialog to select color.
    Qt will use the native dialog by default.
    '''
    dlg = QtWidgets.QColorDialog(self)
    if self._color:
      dlg.setCurrentColor(QtGui.QColor(self._color))
    if dlg.exec_():
      self.setColor(dlg.currentColor().name())
  def mousePressEvent(self, e):
    if e.button() == Qt.RightButton:
      self.setColor(self._default)
    return super().mousePressEvent(e)

```

This custom widget is also available in the [LearnPyQt `qtwidgets` library](https://github.com/learnpyqt/python-qtwidgets).
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**ColorButton** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/widgets/qcolorbutton-a-color-selector-tool-for-pyqt/Python books) on the subject. 
**ColorButton** was published in [widgets](https://www.pythonguis.com/widgets/) on April 25, 2014 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[gui](https://www.pythonguis.com/topics/gui/) [qt](https://www.pythonguis.com/topics/qt/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [qcolorbutton](https://www.pythonguis.com/topics/qcolorbutton/) [custom widgets](https://www.pythonguis.com/topics/custom-widgets/) [ intermediate](https://www.pythonguis.com/topics/intermediate/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [qt5](https://www.pythonguis.com/topics/qt5/) [python](https://www.pythonguis.com/topics/python/)
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
