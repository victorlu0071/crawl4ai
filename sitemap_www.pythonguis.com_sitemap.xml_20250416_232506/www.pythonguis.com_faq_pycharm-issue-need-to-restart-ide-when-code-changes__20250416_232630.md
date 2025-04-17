# Content from: https://www.pythonguis.com/faq/pycharm-issue-need-to-restart-ide-when-code-changes/

[](https://www.pythonguis.com/faq/pycharm-issue-need-to-restart-ide-when-code-changes/#menu)
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
# PyCharm issue, need to restart IDE when code changes
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ FAQ ](https://www.pythonguis.com/faq/)
DosSantos | 2021-04-07 13:08:58 UTC | #1
@martin I take this opportunity to thank you for your tutorials, very good. One more time i take your code and modified it :blush:. For testing news scripts that is good, but i only have one problem. When I assign the code to a new button I need to restart my IDE. I use pycharm. Is it possible to solve this without other ways ? Thanks
python ```
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from PyQt5.QtCore import Qt, QThread, QCoreApplication
from PyQt5 import uic
""" *** WARNING """
""" First need create dialog with tree buttons (bt_one, bt_two, bt_tree) with designer and save file window.ui """
import os # Used in Testing Script
os.system("pyuic5.exe resources\\window.ui -o resources\\window.py") # Used in Testing Script
from resources.window import Ui_MainWindow
import sys
qtCreatorFile = "resources\\window.ui" # Type your file path
""" This block used for testing script """
class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self):
      super().__init__()
      self.reload = None
      self.setupUi(self)
      self.mainbase = self
      self.load_ui()
  def load_ui(self):
    print("loading ui")
    cls, baseclass = uic.loadUiType(qtCreatorFile)
    self.ui = Window()
    self.ui.setupUi(self.ui)
    """ Move the central widget from the loaded UI main window our visible one."""
    self.setCentralWidget(self.ui.centralWidget())
    if not self.reload:
      menu = self.menuBar()
      ui = menu.addMenu("UI")
      self.reload = QAction("Reload UI")
      self.reloadexe = QAction("Reload App")
      self.quit = QAction("Quit")
      self.reload.triggered.connect(self.load_ui)
      self.reloadexe.triggered.connect(self.load_app)
      self.quit.triggered.connect(self.close)
      self.reload.setShortcut(Qt.CTRL | Qt.Key_A) # You can reload with >Ctrl-A
      self.reloadexe.setShortcut(Qt.CTRL | Qt.Key_Q) # You can run test >app >with Ctrl-Q
      self.quit.setShortcut(Qt.Key_Escape) # You can terminate with Ctrl-R
      ui.addActions([self.reload, self.reloadexe, self.quit])
  @staticmethod
  def load_app():
    import os, time
    os.system("pyuic5.exe resources\\window.ui -o resources\\window.py")
    runner()
""" End block used for testing script """

class MainBase(QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    cls, baseclass = uic.loadUiType("resources\\window.ui")
    class Window(cls, baseclass):
        pass
    self.ui = Window()
    self.ui.setupUi(self.ui)
    self.ui.show()
    """ First need create tree buttons (bt_one, bt_two, bt_tree) with designer >and save file window.ui """
    self.ui.bt_one.clicked.connect(lambda: self.ui.lineedit.setText("button >one"))
    self.ui.bt_two.clicked.connect(lambda: self.displaytxt("button two"))
    self.ui.bt_tree.clicked.connect(lambda: self.displaytxt("button tree"))
    """ first write "self." and connection, after this rename to self.ui. ... """
    """ second for test your new button need restart your IDE """
    """ put more connections and all other code bellow """
  def displaytxt(self, x):
    self.ui.lineedit.setText(x)

""" Used in Testing Script """
def runner():
  from resources.window import Ui_MainWindow
  apptest = QCoreApplication
  MainBase()
  apptest.exec_()

app = QApplication([])
w = MainWindow()
w.show()
app.exec_()

```

martin | 2021-04-07 13:12:26 UTC | #2
Hi @DosSantos I missed this when you originally posted it -- I've fixed up the code now so it's clearer. Do you still have this problem/have you found a solution?
You're not the only person who has reported it, but I've not been able to reproduce it myself. That said, normally what I do when developing with Qt is to open a separate terminal (command prompt) and run the code from there. I started doing that when I was using an IDE which would die if the Qt app hung -- it's now just a habit!
Since you're usually just running the same command over and over, it's just a case of hitting the ^ arrow on the keyboard (recall last command) and pressing Enter to repeat.
Would be great to hear of other solutions though.
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PyCharm issue, need to restart IDE when code changes** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pycharm-issue-need-to-restart-ide-when-code-changes/Python books) on the subject. 
**PyCharm issue, need to restart IDE when code changes** was published in [faq](https://www.pythonguis.com/faq/) on October 10, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
