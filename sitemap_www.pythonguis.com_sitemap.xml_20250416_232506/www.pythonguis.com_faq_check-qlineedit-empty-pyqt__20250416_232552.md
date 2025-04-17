# Content from: https://www.pythonguis.com/faq/check-qlineedit-empty-pyqt/

[](https://www.pythonguis.com/faq/check-qlineedit-empty-pyqt/#menu)
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
# Q&A: How to check if a QLineEdit is empty?
Empty strings are falsey in Python
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 13 [ FAQ ](https://www.pythonguis.com/faq/)
A reader asked:
> I just want to know, how do I check whether a QLineEdit is empty or not?
The `QLineEdit` class doesn't have an `isEmpty()` method which you can call to find out if the line edit is empty, but we don't need one! Instead we can get the current text using `.text())` and then check if that value is empty. In the code below `lineedit` is our already created `QLineEdit` widget.
python ```
text = lineedit.text()
if text == '': # if the line edit is empty, .text() will return an empty string.
   # do something

```

We can simplify this further. In Python empty strings are _falsey_ -- they are considered `False` values in conditional expressions. So instead of checking the string is empty, we can check if it is _true_ (non-empty) or _false_ (empty).
python ```
if lineedit.text():
   # do something if there is content in the line edit.

```

Or, to check if it is empty:
python ```
if not lineedit.text():
   # do something if the line edit is empty.

```

Below is a small demo application which updates a label to indicate if the line edit has text in it or not. In this we use Qt signals to send the current text to a slot method every time it is updated.
  * PyQt5
  * PyQt6
  * PySide2
  * PySide6


python ```
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.lineedit = QLineEdit()
    self.lineedit.textChanged.connect(self.text_changed)
    self.label = QLabel()
    vlayout = QVBoxLayout()
    vlayout.addWidget(self.lineedit)
    vlayout.addWidget(self.label)
    self.setLayout(vlayout)
  def text_changed(self, s):
    # s contains the text of the line edit, we could also test self.lineedit.text()
    if s:
      self.label.setText("Not empty")
    else:
      self.label.setText("Empty")

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec_()

```

python ```
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.lineedit = QLineEdit()
    self.lineedit.textChanged.connect(self.text_changed)
    self.label = QLabel()
    vlayout = QVBoxLayout()
    vlayout.addWidget(self.lineedit)
    vlayout.addWidget(self.label)
    self.setLayout(vlayout)
  def text_changed(self, s):
    # s contains the text of the line edit
    if s:
      self.label.setText("Not empty")
    else:
      self.label.setText("Empty")

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec()

```

python ```
import sys
from PySide2.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.lineedit = QLineEdit()
    self.lineedit.textChanged.connect(self.text_changed)
    self.label = QLabel()
    vlayout = QVBoxLayout()
    vlayout.addWidget(self.lineedit)
    vlayout.addWidget(self.label)
    self.setLayout(vlayout)
  def text_changed(self, s):
    # s contains the text of the line edit
    if s:
      self.label.setText("Not empty")
    else:
      self.label.setText("Empty")

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec_()


```

python ```
import sys
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.lineedit = QLineEdit()
    self.lineedit.textChanged.connect(self.text_changed)
    self.label = QLabel()
    vlayout = QVBoxLayout()
    vlayout.addWidget(self.lineedit)
    vlayout.addWidget(self.label)
    self.setLayout(vlayout)
  def text_changed(self, s):
    # s contains the text of the line edit
    if s:
      self.label.setText("Not empty")
    else:
      self.label.setText("Empty")

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec_()


```

Run the above and you'll see the label update as you add and remove text in the `QLineEdit`. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
![Empty lineedit](https://www.pythonguis.com/static/faq/check-qlinedit-is-empty/lineedit-empty.png)
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
![Lineedit with content](https://www.pythonguis.com/static/faq/check-qlinedit-is-empty/lineedit-notempty.png)
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Q &A: How to check if a QLineEdit is empty?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/check-qlineedit-empty-pyqt/Python books) on the subject. 
**Q &A: How to check if a QLineEdit is empty?** was published in [faq](https://www.pythonguis.com/faq/) on May 07, 2020 (updated September 13, 2023) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qlineedit](https://www.pythonguis.com/topics/qlineedit/) [widgets](https://www.pythonguis.com/topics/widgets/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/)
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
