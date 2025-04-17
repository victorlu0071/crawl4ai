# Content from: https://www.pythonguis.com/faq/setalignment-qtcore-qt-aligncenter-method-is-not-working-as-expected/

[](https://www.pythonguis.com/faq/setalignment-qtcore-qt-aligncenter-method-is-not-working-as-expected/#menu)
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
# setAlignment(QtCore.Qt.AlignCenter) method is not working as expected
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
bentraje6381 | 2020-11-29 05:33:05 UTC | #1
Hi,
I'm trying to center a log-in form relative to window space but the `setAlignment(QtCore.Qt.AlignCenter)` is not working as expected.
You can check the code below so far:
python ```
import sys
import os
import json
import PySide2
from PySide2 import QtCore
from PySide2.QtCore import Qt, QTimer
from PySide2.QtWidgets import QApplication, QMainWindow, QSpinBox, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QStackedLayout
from PySide2 import QtWidgets

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Quiz Application")
    self.setFixedWidth(500)
    self.setFixedHeight(500)
    # LOG IN LAYOUT
    self.login_layout = QVBoxLayout()
    login_form_layout = QtWidgets.QFormLayout()
    self.username_edit = QtWidgets.QLineEdit()
    self.password_edit = QtWidgets.QLineEdit()
    self.username_edit.setFixedWidth(120)
    self.password_edit.setFixedWidth(120)
    login_form_layout.addRow(QtWidgets.QLabel("Username"), self.username_edit)
    login_form_layout.addRow(QtWidgets.QLabel("Password"), self.password_edit)

    self.login_btn = QPushButton("Log In")
    self.login_btn.setFixedWidth(120)
    self.login_btn.pressed.connect(self.login_cmd)
    login_form_layout.addWidget(self.login_btn)
    self.login_layout.addLayout(login_form_layout)
    self.login_layout.addStretch()
    self.login_widget = QWidget()
    self.login_widget.setLayout(self.login_layout)

    # Main Menu Layout
    self.main_menu_layout = QVBoxLayout()
    self.logout_btn = QPushButton("Log Out")
    self.logout_btn.setFixedWidth(120)
    self.logout_btn.pressed.connect(self.logout_cmd)
    self.main_menu_layout.addWidget(self.logout_btn)
    self.main_menu_layout.addStretch()
    self.main_menu_widget = QWidget()
    self.main_menu_widget.setLayout(self.main_menu_layout )
    # Stack Layout
    self.stack_layout = QStackedLayout()
    self.stack_layout.addWidget(self.login_widget)
    self.stack_layout.addWidget(self.main_menu_widget)
    self.stack_layout.setCurrentIndex(0)
    self.stack_layout.setAlignment(QtCore.Qt.AlignCenter)

    widget = QWidget()
    widget.setLayout(self.stack_layout)
    self.setCentralWidget(widget)
  def login_cmd(self):
    self.stack_layout.setCurrentIndex(1)
  def logout_cmd(self):
    self.stack_layout.setCurrentIndex(0)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

![py005_pyqt_center_layout_in_the window|690x403](https://www.pythonguis.com/static/faq/forum/setalignment-qtcore-qt-aligncenter-method-is-not-working-as-expected/rMy8NKQORYSuZvzEwMXjiIl2rt8.jpeg)
Salem_Bream | 2020-12-01 14:14:54 UTC | #2
@bentraje6381 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
There are several issues we need to address.
  1. You are adding stretches! `.addStrech()`, stretches will try to eat most of the layout available space and forces the widgets inside the layout to be shrunk. Just delete the `.addStretch()` statements.
  2. you are setting the alignment of the `QStackedLayout` which shows only 1 widget at any given time!, so its alignment is meaningless. You need to set the alignment for the layouts of widgets themselves inside it.
  3. the `QFormLayout` is a special case, not as other layouts, it has special option to specify the layout, read the documentation to know more. Use `form_layout_xx.setFormAlignment()`.


Here is a working code...
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
python ```
import sys
import os
import json
import PySide2
from PySide2 import QtCore
from PySide2.QtCore import Qt, QTimer
from PySide2.QtWidgets import QApplication, QMainWindow, QSpinBox, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QStackedLayout
from PySide2 import QtWidgets

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Quiz Application")
    self.setFixedWidth(500)
    self.setFixedHeight(500)
    # LOG IN LAYOUT
    self.login_layout = QVBoxLayout()
    login_form_layout = QtWidgets.QFormLayout()
    self.username_edit = QtWidgets.QLineEdit()
    self.password_edit = QtWidgets.QLineEdit()
    self.username_edit.setFixedWidth(120)
    self.password_edit.setFixedWidth(120)
    login_form_layout.addRow(QtWidgets.QLabel(
      "Username"), self.username_edit)
    login_form_layout.addRow(QtWidgets.QLabel(
      "Password"), self.password_edit)
    self.login_btn = QPushButton("Log In")
    self.login_btn.setFixedWidth(120)
    self.login_btn.pressed.connect(self.login_cmd)
    login_form_layout.addWidget(self.login_btn)
    self.login_layout.addLayout(login_form_layout)
    login_form_layout.setFormAlignment(Qt.AlignCenter)
    self.login_widget = QWidget()
    self.login_widget.setLayout(self.login_layout)
    # Main Menu Layout
    self.main_menu_layout = QVBoxLayout()
    self.logout_btn = QPushButton("Log Out")
    self.logout_btn.setFixedWidth(120)
    self.logout_btn.pressed.connect(self.logout_cmd)
    self.main_menu_layout.addWidget(self.logout_btn)
    self.main_menu_layout.setAlignment(QtCore.Qt.AlignCenter)
    self.main_menu_widget = QWidget()
    self.main_menu_widget.setLayout(self.main_menu_layout)
    # Stack Layout
    self.stack_layout = QStackedLayout()
    self.stack_layout.addWidget(self.login_widget)
    self.stack_layout.addWidget(self.main_menu_widget)
    self.stack_layout.setCurrentIndex(0)
    widget = QWidget()
    widget.setLayout(self.stack_layout)
    self.setCentralWidget(widget)
  def login_cmd(self):
    self.stack_layout.setCurrentIndex(1)
  def logout_cmd(self):
    self.stack_layout.setCurrentIndex(0)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

bentraje6381 | 2020-12-01 14:16:25 UTC | #3
Thanks for the explaining what I did wrong. The code work as expected. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**setAlignment(QtCore.Qt.AlignCenter) method is not working as expected** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/setalignment-qtcore-qt-aligncenter-method-is-not-working-as-expected/Python books) on the subject. 
**setAlignment(QtCore.Qt.AlignCenter) method is not working as expected** was published in [faq](https://www.pythonguis.com/faq/) on November 29, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
