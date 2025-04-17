# Content from: https://www.pythonguis.com/faq/help-with-creating-your-first-app-tutorial/

[](https://www.pythonguis.com/faq/help-with-creating-your-first-app-tutorial/#menu)
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
# Help with Creating Your First App Tutorial
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ FAQ ](https://www.pythonguis.com/faq/)
bryon | 2020-10-24 20:46:54 UTC | #1
I'm struggling a bit with the very first lesson. I'm following along the video at the top of the page since the codeblocks on the page are different and don't seem to be working for me (missing imports as far as I can tell). I've gotten to the part where we use a class to create the window but when I attempt to change the title of the window it doesn't change. Code is below, I'm on Windows 10 with Python 3.7.4. and Python 3.9 (I just reinstalled it as a test)
python ```
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args,**kwargs)
    self.setWindowTitle('Awesome App')
app = QApplication(sys.argv)
window = QWidget()
window.show() # IMPORTANT! Windows are hidden by default.
app.exec_()

```

Setting the title with window.setWindowTitle('whatever') does work though.
bryon | 2020-10-25 00:56:29 UTC | #3
window = MainWindow() worked. I'm guessing this is an error in the lesson. Further down the variable is changed though to that. I didn't notice it changes
Mark_Salerno | 2020-11-29 14:04:31 UTC | #4
I an running the example compiled_example.py from the tutorial download in the designer examples: compiled_example.py
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
python ```
import random
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.show()
    # You can still override values from your UI file within your code,
    # but if possible, set them in Qt Creator. See the properties panel.
    f = self.label.font()
    f.setPointSize(25)
    self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    self.label.setFont(f)
    # Signals from UI widgets can be connected as normal.
    self.pushButton.pressed.connect(self.update_label)
  def update_label(self):
    #n = n + 1
    n = random.randint(1, 6)
    self.label.setText("%d" % n)

app = QApplication(sys.argv)
w = MainWindow()
app.exec_()

```

I wanted to show a number incrementing in the label and I commented out the random line an d added n=n+1 line. The program crashes when I push the button. If I leave the random line in and add the n=n+1 line it crashes when I push the button.
Can someone explain why this is happening
Mark
martin | 2020-11-30 17:48:35 UTC | #5
Hi Mark
The reason your `n = n + 1` line causes the program to crash is that `n` is not defined in `update_label` -- you can't add 1 to a variable that doesn't exist. There is a second issue in that within that method the `n` variable is local, which means that even if you do define it, on exiting that method `n` will be deleted.
The solution to this is to store your reference to `n` on the object, via `self`, e.g.
python ```
self.n = self.n + 1

```

But even then, you still need to define `self.n` first. To do this, in the `__init__` block of your class, you can write 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
python ```
self.n = 0

```

...to initialize it to zero. The full code would be
python ```
import random
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.show()
    self.n = 0
    # You can still override values from your UI file within your code,
    # but if possible, set them in Qt Creator. See the properties panel.
    f = self.label.font()
    f.setPointSize(25)
    self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    self.label.setFont(f)
    # Signals from UI widgets can be connected as normal.
    self.pushButton.pressed.connect(self.update_label)
  def update_label(self):
    self.n = self.n + 1
    self.label.setText("%d" % self.n)

app = QApplication(sys.argv)
w = MainWindow()
app.exec_()

```

martin | 2020-11-30 17:49:06 UTC | #6
Thanks for the feedback @bryon I'll take another look at that tutorial, I'm in the process of updating them all to contain the full code blocks, etc.
Mark_Salerno | 2020-11-30 18:49:27 UTC | #7
Thanks Martin for taking the time to so thoroughly answer my question and show me the solution.
I currently program small embedded systems in c and I am not used to the self. references.
Mark
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Help with Creating Your First App Tutorial** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/help-with-creating-your-first-app-tutorial/Python books) on the subject. 
**Help with Creating Your First App Tutorial** was published in [faq](https://www.pythonguis.com/faq/) on October 24, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
