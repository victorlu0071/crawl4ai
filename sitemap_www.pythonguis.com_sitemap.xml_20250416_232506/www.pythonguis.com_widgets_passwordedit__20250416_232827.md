# Content from: https://www.pythonguis.com/widgets/passwordedit/

[](https://www.pythonguis.com/widgets/passwordedit/#menu)
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
# PasswordEdit
Password editing field, with Show/Hide toggle
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 13 [ Python GUI Widget Library ](https://www.pythonguis.com/widgets/)
When building applications which require a password (or some other secret) from a user you should use fields that hide the input. This prevents _shoulder surfing_ passers by from being able to read off the user's secret and gain access to accounts.
Qt `QLinEdit` fields can be toggled to hide input using the `.setEchoMode` method, passing in the constant `QtWidgets.QLineEdit.Password` to hide all input or `QtWidgets.QLineEdit.Normal` to reverse the display back to normal.
python ```
le = QtWidgets.QLineEdit()
le.setEchoMode(QtWidgets.QLineEdit.Password)

```

Sometimes however you may want to allow the user themselves to toggle the state of the display. This is commonly used for _not so secret_ fields, such as WiFi passwords, or for situations where user-input is prone to error, for example on mobile or when passphrases are particularly long. Doing this gives the user the option to weigh up risk vs. usability themselves.
While you can achieve this with an additional button, it's become a convention from the web to add the show/hide toggle as an "eye" icon in the field itself. In this custom widget we've implemented this same behaviour by making use of Qt `QLineEdit` support for embedded actions with custom icons.
To use the widget install the `qtwidgets` Python library.
shell ```
pip3 install qtwidgets

```

You can then import the widget into your application using
python ```
from qtwidgets import PasswordEdit

```

There are [other widgets available](https://github.com/learnpyqt/python-qtwidgets) in the library too. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
You can use the `PasswordEdit` widget as any other `QLineEdit` as it subclasses from the standard widget. This gives you access to all standard signals/methods.
You can test the widget out using the following demo code.
  * PyQt5
  * PySide2


python ```
from PyQt5 import QtCore, QtGui, QtWidgets
from qtwidgets import PasswordEdit
class Window(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    password = PasswordEdit()
    self.setCentralWidget(password)

app = QtWidgets.QApplication([])
w = Window()
w.show()
app.exec_()

```

python ```
from PySide2 import QtCore, QtGui, QtWidgets
from qtwidgets import PasswordEdit

class Window(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    password = PasswordEdit()
    self.setCentralWidget(password)

app = QtWidgets.QApplication([])
w = Window()
w.show()
app.exec_()

```

Running the code you'll see a window appear containing a single line edit box, with an embedded eye icon. Try typing something in the box and then using the eye to toggle hide/show the content
![Empty PasswordEdit field](https://www.pythonguis.com/static/widgets/passwordedit/window_NGEQtFa.png) _Empty PasswordEdit field_
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
![Hidden PasswordEdit field](https://www.pythonguis.com/static/widgets/passwordedit/hidden_rJnxp35.png) _Hidden PasswordEdit field_
![Visible PasswordEdit field](https://www.pythonguis.com/static/widgets/passwordedit/visible.png) _Visible PasswordEdit field_
You can opt to hide the visibility toggle if you wish, by passing `show_visibility=False` when creating the widget. In this case the widget behaves just like a `QLineEdit` except defaulting to hidden input.
python ```
pe = PasswordEdit(show_visibility=False)

```

The `PasswordEdit` widget is based on this [original example by Kushal Das](https://kushaldas.in/posts/creating-password-input-widget-in-pyqt.html).
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PasswordEdit** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/widgets/passwordedit/Python books) on the subject. 
**PasswordEdit** was published in [widgets](https://www.pythonguis.com/widgets/) on April 16, 2020 (updated September 13, 2023) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[widget](https://www.pythonguis.com/topics/widget/) [toggle](https://www.pythonguis.com/topics/toggle/) [hidden](https://www.pythonguis.com/topics/hidden/) [password](https://www.pythonguis.com/topics/password/) [private](https://www.pythonguis.com/topics/private/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [python](https://www.pythonguis.com/topics/python/)
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
