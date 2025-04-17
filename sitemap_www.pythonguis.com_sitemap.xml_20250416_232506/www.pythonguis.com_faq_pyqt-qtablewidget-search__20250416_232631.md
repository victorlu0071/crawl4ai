# Content from: https://www.pythonguis.com/faq/pyqt-qtablewidget-search/

[](https://www.pythonguis.com/faq/pyqt-qtablewidget-search/#menu)
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
# Search a QTablewidget and select matching items
Finding and selecting matching items in a QTableWidget
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Mar 03 [ FAQ ](https://www.pythonguis.com/faq/)
We've previously covered how to use search in a `QTableView`. However, if you're using `QTableWidget` instead of model views you may still want to be able to search through the items in the table and highlight or select them. In this quick tutorial we'll show how to do that.
Searching in a `QTableWidget` is handled with the `.findItems` method. The method definition from the documentation is shown below (converted to Python).
python ```
[QTableWidgetItem] = QTableWidget.findItems(str, Qt.MatchFlags)

```

This tells us that the method accepts a `str` "text" to search, and a `Qt.MatchFlags` "flags" object which is what determines _how_ we search. The `.findItems` method when called will return a `list` of `QTableWidgetItem` objects. These objects are the actual _data items_ in the table. Once you have them, you can select a given item by calling `.setCurrentItem` and passing in an individual item, or for multiple-selection calling `.setSelected(True)` on the item itself.
Below is a quick example showing a `QTableWidget` with a `QLineEdit` search box. As you type in the box matching items are highlighted in the table view.
  * PyQt5
  * PySide2
  * PyQt6
  * PySide6


python ```

from PyQt5.QtWidgets import QTableWidget, QLineEdit, QPushButton, QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import random, string, sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.query = QLineEdit()
    self.query.setPlaceholderText("Search...")
    self.query.textChanged.connect(self.search)
    n_rows = 50
    n_cols = 4
    self.table = QTableWidget()
    self.table.setRowCount(n_rows)
    self.table.setColumnCount(n_cols)
    for c in range(0, n_cols):
      for r in range(0, n_rows):
        s = ''.join(random.choice(string.ascii_lowercase) for n in range(10))
        i = QTableWidgetItem(s)
        self.table.setItem(c, r, i)
    layout = QVBoxLayout()
    layout.addWidget(self.query)
    layout.addWidget(self.table)
    w = QWidget()
    w.setLayout(layout)
    self.setCentralWidget(w)
  def search(self, s):
    # Clear current selection.
    self.table.setCurrentItem(None)
    if not s:
      # Empty string, don't search.
      return
    matching_items = self.table.findItems(s, Qt.MatchContains)
    if matching_items:
      # We have found something.
      item = matching_items[0] # Take the first.
      self.table.setCurrentItem(item)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

```

python ```

from PySide2.QtWidgets import QTableWidget, QLineEdit, QPushButton, QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidgetItem
from PySide2.QtCore import Qt
import random, string, sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.query = QLineEdit()
    self.query.setPlaceholderText("Search...")
    self.query.textChanged.connect(self.search)
    n_rows = 50
    n_cols = 4
    self.table = QTableWidget()
    self.table.setRowCount(n_rows)
    self.table.setColumnCount(n_cols)
    for c in range(0, n_cols):
      for r in range(0, n_rows):
        s = ''.join(random.choice(string.ascii_lowercase) for n in range(10))
        i = QTableWidgetItem(s)
        self.table.setItem(c, r, i)
    layout = QVBoxLayout()
    layout.addWidget(self.query)
    layout.addWidget(self.table)
    w = QWidget()
    w.setLayout(layout)
    self.setCentralWidget(w)
  def search(self, s):
    # clear current selection.
    self.table.setCurrentItem(None)
    if not s:
      # Empty string, don't search.
      return
    matching_items = self.table.findItems(s, Qt.MatchContains)
    if matching_items:
      # we have found something
      item = matching_items[0] # take the first
      self.table.setCurrentItem(item)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

```

python ```

from PyQt6.QtWidgets import QTableWidget, QLineEdit, QPushButton, QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidgetItem
from PyQt6.QtCore import Qt
import random, string, sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.query = QLineEdit()
    self.query.setPlaceholderText("Search...")
    self.query.textChanged.connect(self.search)
    n_rows = 50
    n_cols = 4
    self.table = QTableWidget()
    self.table.setRowCount(n_rows)
    self.table.setColumnCount(n_cols)
    for c in range(0, n_cols):
      for r in range(0, n_rows):
        s = ''.join(random.choice(string.ascii_lowercase) for n in range(10))
        i = QTableWidgetItem(s)
        self.table.setItem(c, r, i)
    layout = QVBoxLayout()
    layout.addWidget(self.query)
    layout.addWidget(self.table)
    w = QWidget()
    w.setLayout(layout)
    self.setCentralWidget(w)
  def search(self, s):
    # clear current selection.
    self.table.setCurrentItem(None)
    if not s:
      # Empty string, don't search.
      return
    matching_items = self.table.findItems(s, Qt.MatchFlag.MatchContains)
    if matching_items:
      # we have found something
      item = matching_items[0] # take the first
      self.table.setCurrentItem(item)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

```

python ```

from PySide6.QtWidgets import QTableWidget, QLineEdit, QPushButton, QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidgetItem
from PySide6.QtCore import Qt
import random, string, sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.query = QLineEdit()
    self.query.setPlaceholderText("Search...")
    self.query.textChanged.connect(self.search)
    n_rows = 50
    n_cols = 4
    self.table = QTableWidget()
    self.table.setRowCount(n_rows)
    self.table.setColumnCount(n_cols)
    for c in range(0, n_cols):
      for r in range(0, n_rows):
        s = ''.join(random.choice(string.ascii_lowercase) for n in range(10))
        i = QTableWidgetItem(s)
        self.table.setItem(c, r, i)
    layout = QVBoxLayout()
    layout.addWidget(self.query)
    layout.addWidget(self.table)
    w = QWidget()
    w.setLayout(layout)
    self.setCentralWidget(w)
  def search(self, s):
    # clear current selection.
    self.table.setCurrentItem(None)
    if not s:
      # Empty string, don't search.
      return
    matching_items = self.table.findItems(s, Qt.MatchContains)
    if matching_items:
      # we have found something
      item = matching_items[0] # take the first
      self.table.setCurrentItem(item)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

```

The `search` method receives the `textChanged` signal from the `QLineEdit` as `s`. We first clear the current selection to simplify the conditions below: we don't need to clear on empty string _and_ if there are no matches. Next we check if `s` is _empty_ (`not s` is `True` if the string is empty). If it is we return without searching, leaving the table with no selection.
This step is necessary because calling `.findItems` with an empty string will return a `list` containing all currently selected items and `None` for non-selected items. This isn't what we want!
Once we know we have a search string we call `.findItems` with a `Qt.MatchContains` search, which will return any items containing the search string. If there are items, we take the first via `matching_items[0]` and set it as the current item (the currently selected item). If not, we clear the selection.
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
If you type a search string in the line input, you'll see the first matching item in the table selected (and highlighted) like below.
![Search selecting a single item in the table](https://www.pythonguis.com/static/faq/qtablewidget-search/search-single-item.jpeg) _Search selecting a single item in the table_
If you would like to select _all_ matching items in the table, you can iterate the items and use `.setSelected(True)` instead. The modified `search` method is shown below.
python ```

class MainWindow(QMainWindow):
  # ... __init__ unchanged

  def search(self, s):
    # Clear current selection.
    self.table.setCurrentItem(None)
    if not s:
      # Empty string, don't search.
      return
    matching_items = self.table.findItems(s, Qt.MatchContains)
    if matching_items:
      # We have found something.
      for item in matching_items:
        item.setSelected(True)

```

This works similarly to the previous example. First we clear the active selection: here it is more important to do this, as we need to ensure selected items are unselected when the search string is extended. As before we then check if `s` is empty, then perform the search. However, instead of setting only a single item we call `setSelected` on each item to mark it as selected. You'll see any matching items in the table highlighted as you type.
![Search selecting a single item in the table](https://www.pythonguis.com/static/faq/qtablewidget-search/search-many-items.png) _Search selecting multiple items in the table_
Below is a a short demo video.
You can experiment with different matching types for your search. Below are the available options in [Qt.MatchFlags](https://doc.qt.io/qt-5/qt.html#MatchFlag-enum) -- for example _starts with_ , _contains_ , etc. and whether the search is _case sensitive_.
Flag | Value | Search type  
---|---|---  
`Qt.MatchContains` | 1 | The search term is contained in the item.  
`Qt.MatchStartsWith` | 2 | The search term matches the start of the item.  
`Qt.MatchEndsWith` | 3 | The search term matches the end of the item.  
`Qt.MatchWildcard` | 5 | Performs string-based matching using a string with wildcards as the search term.  
`Qt.MatchFixedString` | 8 | Performs string-based matching. String-based comparisons are case-insensitive unless the MatchCaseSensitive flag is also specified.  
`Qt.MatchRegularExpression` | 9 | Performs string-based matching using a regular expression as the search term. Uses QRegularExpression. When using this flag, a QRegularExpression object can be passed as parameter and will directly be used to perform the search. The case sensitivity flag will be ignored as the QRegularExpression object is expected to be fully configured. This enum value was added in Qt 5.15.  
`Qt.MatchCaseSensitive` | 16 | The search is case sensitive.  
You can combine `MatchCaseSensitive` with other searches to modify case matching behavior. For example `Qt.MatchContains | Qt.MatchCaseSensitive` would do a case-sensitive contains match.
For PyQt6 you must use the fully-qualified flag name, for example `Qt.MatchFlag.MatchFixedString`.
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Search a QTablewidget and select matching items** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyqt-qtablewidget-search/Python books) on the subject. 
**Search a QTablewidget and select matching items** was published in [faq](https://www.pythonguis.com/faq/) on September 03, 2021 (updated March 03, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qtablewidget](https://www.pythonguis.com/topics/qtablewidget/) [search](https://www.pythonguis.com/topics/search/) [filter](https://www.pythonguis.com/topics/filter/) [table](https://www.pythonguis.com/topics/table/) [tablewidget](https://www.pythonguis.com/topics/tablewidget/)
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
