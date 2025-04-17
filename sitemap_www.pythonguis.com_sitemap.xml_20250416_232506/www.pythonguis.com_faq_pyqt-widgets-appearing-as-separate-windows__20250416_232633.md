# Content from: https://www.pythonguis.com/faq/pyqt-widgets-appearing-as-separate-windows/

[](https://www.pythonguis.com/faq/pyqt-widgets-appearing-as-separate-windows/#menu)
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
# Q&A: How to fix widgets appearing as separate windows?
Understanding Qt parents and layouts and the effect on widget position
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 13 [ FAQ ](https://www.pythonguis.com/faq/)
One very common issue when you start creating GUI applications with Python & Qt is having your widgets either disappear or start popping out of your interface as independent windows. This is pretty confusing if you don't understand _why_ it happens, but once you do it's usually very easy to fix.
The key points --
  1. Any widget without a parent is a window. If you create a widget but don't set a parent it will become a separate window.
  2. Widgets without parents (i.e. any windows) are hidden by default and remain hidden until they are _shown_ either by you, or automatically by Qt (for example when selecting tabs in a `QTabWidget`).
  3. Adding widgets to layouts sets their parent. Widgets not in layouts must have parents set explicitly.
  4. Removing a widget from a layout **doesn't** remove its parent.
  5. You can remove the parent from a widget by setting the parent to `None`. This will turn it into a window!


Below is a small example to demonstrate these effects. We create a window, add a layout and a widget.
  * PyQt5
  * PyQt6
  * PySide2
  * PySide6


python ```
import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QApplication
class Window(QWidget):
  def __init__(self):
    super().__init__()
    # This is the widget that we will experiment with: note that we don't
    # set a parenet, and don't add it to the layout.
    self.mywidget = QLabel("Hello")
    self.mywidget.show() # We need to show it (or focus it) to make it visible.
    add_parent = QPushButton("Add parent")
    add_parent.clicked.connect(self.add_parent)
    remove_parent = QPushButton("Remove parent")
    remove_parent.clicked.connect(self.remove_parent)
    add_layout = QPushButton("Add layout")
    add_layout.clicked.connect(self.add_layout)
    remove_layout = QPushButton("Remove layout")
    remove_layout.clicked.connect(self.remove_layout)
    self.vlayout = QVBoxLayout()
    self.vlayout.addWidget(add_parent)
    self.vlayout.addWidget(remove_parent)
    self.vlayout.addWidget(add_layout)
    self.vlayout.addWidget(remove_layout)
    self.setLayout(self.vlayout)
  def add_parent(self):
    self.mywidget.setParent(self)
    self.mywidget.move(0,0)
    self.mywidget.show()
    print("Added parent, parent is:", self.mywidget.parent())
  def remove_parent(self):
    self.mywidget.setParent(None)
    self.mywidget.show()
    print("Removed parent, parent is:", self.mywidget.parent())
  def add_layout(self):
    self.vlayout.addWidget(self.mywidget)
    print("Added layout, parent is:", self.mywidget.parent())
  def remove_layout(self):
    self.vlayout.removeWidget(self.mywidget)
    print("Removed layout, parent is:", self.mywidget.parent())
app = QApplication(sys.argv)
w = Window()
w.show()
app.exec()

```

python ```
import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QApplication

class Window(QWidget):
  def __init__(self):
    super().__init__()
    # This is the widget that we will experiment with: note that we don't
    # set a parenet, and don't add it to the layout.
    self.mywidget = QLabel("Hello")
    self.mywidget.show() # We need to show it (or focus it) to make it visible.
    add_parent = QPushButton("Add parent")
    add_parent.clicked.connect(self.add_parent)
    remove_parent = QPushButton("Remove parent")
    remove_parent.clicked.connect(self.remove_parent)
    add_layout = QPushButton("Add layout")
    add_layout.clicked.connect(self.add_layout)
    remove_layout = QPushButton("Remove layout")
    remove_layout.clicked.connect(self.remove_layout)
    self.vlayout = QVBoxLayout()
    self.vlayout.addWidget(add_parent)
    self.vlayout.addWidget(remove_parent)
    self.vlayout.addWidget(add_layout)
    self.vlayout.addWidget(remove_layout)
    self.setLayout(self.vlayout)
  def add_parent(self):
    self.mywidget.setParent(self)
    self.mywidget.move(0,0)
    self.mywidget.show()
    print("Added parent, parent is:", self.mywidget.parent())
  def remove_parent(self):
    self.mywidget.setParent(None)
    self.mywidget.show()
    print("Removed parent, parent is:", self.mywidget.parent())
  def add_layout(self):
    self.vlayout.addWidget(self.mywidget)
    print("Added layout, parent is:", self.mywidget.parent())
  def remove_layout(self):
    self.vlayout.removeWidget(self.mywidget)
    print("Removed layout, parent is:", self.mywidget.parent())

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec()

```

python ```
import sys
from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QApplication

class Window(QWidget):
  def __init__(self):
    super().__init__()
    # This is the widget that we will experiment with: note that we don't
    # set a parenet, and don't add it to the layout.
    self.mywidget = QLabel("Hello")
    self.mywidget.show() # We need to show it (or focus it) to make it visible.
    add_parent = QPushButton("Add parent")
    add_parent.clicked.connect(self.add_parent)
    remove_parent = QPushButton("Remove parent")
    remove_parent.clicked.connect(self.remove_parent)
    add_layout = QPushButton("Add layout")
    add_layout.clicked.connect(self.add_layout)
    remove_layout = QPushButton("Remove layout")
    remove_layout.clicked.connect(self.remove_layout)
    self.vlayout = QVBoxLayout()
    self.vlayout.addWidget(add_parent)
    self.vlayout.addWidget(remove_parent)
    self.vlayout.addWidget(add_layout)
    self.vlayout.addWidget(remove_layout)
    self.setLayout(self.vlayout)
  def add_parent(self):
    self.mywidget.setParent(self)
    self.mywidget.move(0,0)
    self.mywidget.show()
    print("Added parent, parent is:", self.mywidget.parent())
  def remove_parent(self):
    self.mywidget.setParent(None)
    self.mywidget.show()
    print("Removed parent, parent is:", self.mywidget.parent())
  def add_layout(self):
    self.vlayout.addWidget(self.mywidget)
    print("Added layout, parent is:", self.mywidget.parent())
  def remove_layout(self):
    self.vlayout.removeWidget(self.mywidget)
    print("Removed layout, parent is:", self.mywidget.parent())
app = QApplication(sys.argv)
w = Window()
w.show()
app.exec_()

```

python ```
import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QApplication

class Window(QWidget):
  def __init__(self):
    super().__init__()
    # This is the widget that we will experiment with: note that we don't
    # set a parenet, and don't add it to the layout.
    self.mywidget = QLabel("Hello")
    self.mywidget.show() # We need to show it (or focus it) to make it visible.
    add_parent = QPushButton("Add parent")
    add_parent.clicked.connect(self.add_parent)
    remove_parent = QPushButton("Remove parent")
    remove_parent.clicked.connect(self.remove_parent)
    add_layout = QPushButton("Add layout")
    add_layout.clicked.connect(self.add_layout)
    remove_layout = QPushButton("Remove layout")
    remove_layout.clicked.connect(self.remove_layout)
    self.vlayout = QVBoxLayout()
    self.vlayout.addWidget(add_parent)
    self.vlayout.addWidget(remove_parent)
    self.vlayout.addWidget(add_layout)
    self.vlayout.addWidget(remove_layout)
    self.setLayout(self.vlayout)
  def add_parent(self):
    self.mywidget.setParent(self)
    self.mywidget.move(0,0)
    self.mywidget.show()
    print("Added parent, parent is:", self.mywidget.parent())
  def remove_parent(self):
    self.mywidget.setParent(None)
    self.mywidget.show()
    print("Removed parent, parent is:", self.mywidget.parent())
  def add_layout(self):
    self.vlayout.addWidget(self.mywidget)
    print("Added layout, parent is:", self.mywidget.parent())
  def remove_layout(self):
    self.vlayout.removeWidget(self.mywidget)
    print("Removed layout, parent is:", self.mywidget.parent())
app = QApplication(sys.argv)
w = Window()
w.show()
app.exec_()

```

In the initial state the widget isn't added to any layout and has no parent, so when the application is run you'll actually see _two_ floating windows. Push the control buttons to experiment with adding the widget to the layout, setting a parent, clearing the parent and removing it from the layout.
![The starting view](https://www.pythonguis.com/static/faq/pyqt-widgets-appearing-as-separate-windows/demo.png)
Each time the state changes the current parent will be printed to the console. Notice that when you add the widget to the layout, the widget receives the `Window` as it's parent. This is the normal behavior in Qt: adding a widget to a layout will set it's parent to the widget on which the layout is applied (the container widget). In this case this is the `Window` itself.
python ```
Added layout, parent is: <__main__.Window(0x15413656090) at 0x000001542CB98688>

```

If you remove the widget from the layout, it's parent is _not_ automatically cleared. The widget will remain inside the window, near it's original position. But the layout will re-lay the other items over it. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
![The widget is removed from the layout, but remains in place](https://www.pythonguis.com/static/faq/pyqt-widgets-appearing-as-separate-windows/demo-borked.png)
If you remove the parent the widget will return to it's floating state.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Note that when setting the parent on the window we also call `.move(0, 0)` to move it to a specific point relative to the parent window. This is necessary to ensure we can see the widget: if you remove this, setting the parent will just make the widget disappear. If you have widgets disappearing in your apps, this is a good that they have a parent set but are not properly positioned or added to a layout. As a general rule, use layouts to avoid hitting these kinds of issues!
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Q &A: How to fix widgets appearing as separate windows?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyqt-widgets-appearing-as-separate-windows/Python books) on the subject. 
**Q &A: How to fix widgets appearing as separate windows?** was published in [faq](https://www.pythonguis.com/faq/) on August 30, 2021 (updated September 13, 2023) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[windows](https://www.pythonguis.com/topics/windows/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/)
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
