# Content from: https://www.pythonguis.com/docs/qcombobox/

[](https://www.pythonguis.com/docs/qcombobox/#menu)
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
# QComboBox
Drop-down selection widget
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Mar 15 [ Documentation ](https://www.pythonguis.com/docs/)
The `QComboBox` is a simple widget for presenting a list of options to your users in PyQt, taking up the minimum amount of screen space. The widget can have a single selected item, which is displayed in the widget area. When selected a `QComboBox` pops out a list of possible values from which you can select. A `QComboBox` can also - optionally - be made editable, so your users can enter their own values onto the list of possible values.
![QComboBox](https://www.pythonguis.com/static/docs/qcombobox/qcombobox.png) _QComboBox in its closed and open state_
Table of Contents
  * [Populating a QComboBox](https://www.pythonguis.com/docs/qcombobox/#populating-a-qcombobox)
  * [QComboBox signals](https://www.pythonguis.com/docs/qcombobox/#qcombobox-signals)
  * [Getting the current state](https://www.pythonguis.com/docs/qcombobox/#getting-the-current-state)
  * [Editable comboboxes](https://www.pythonguis.com/docs/qcombobox/#editable-comboboxes)


## Populating a QComboBox
Items can be added or inserted to a `QComboBox`, where _adding_ appends the item to the end of the current list, while _insert_ inserts them in a specific index in the existing list. There are convenience methods for adding multiple items to a combobox and also for adding icons to the list. The following example will demonstrate each of these using a series of comboboxes.
python ```
from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    combobox1 = QComboBox()
    combobox1.addItem('One')
    combobox1.addItem('Two')
    combobox1.addItem('Three')
    combobox1.addItem('Four')
    combobox2 = QComboBox()
    combobox2.addItems(['One', 'Two', 'Three', 'Four'])
    combobox3 = QComboBox()
    combobox3.addItems(['One', 'Two', 'Three', 'Four'])
    combobox3.insertItem(2, 'Hello!')
    combobox4 = QComboBox()
    combobox4.addItems(['One', 'Two', 'Three', 'Four'])
    combobox4.insertItems(2, ['Hello!', 'again'])
    combobox5 = QComboBox()
    icon_penguin = QIcon('animal-penguin.png')
    icon_monkey = QIcon('animal-monkey.png')
    icon_bauble = QIcon('bauble.png')
    combobox5.addItem(icon_penguin, 'Linux')
    combobox5.addItem(icon_monkey, 'Monkeyix')
    combobox5.insertItem(1, icon_bauble, 'Baublix')
    layout = QVBoxLayout()
    layout.addWidget(combobox1)
    layout.addWidget(combobox2)
    layout.addWidget(combobox3)
    layout.addWidget(combobox4)
    layout.addWidget(combobox5)
    container = QWidget()
    container.setLayout(layout)
    self.setCentralWidget(container)
  def current_text_changed(self, s):
    print("Current text: ", s)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

```

Run the example and compare the result with each series of _add_ and _insert_ steps.
![Adding items to a QComboBox](https://www.pythonguis.com/static/docs/qcombobox/qcombobox-add.png) _Adding items to a QComboBox_
You can replace the text at a specific index in the list by calling `.setItemText()` for example.
python ```
widget.setItemText(3, 'new text')

```

Finally, you can clear a `QComboBox` -- removing all items in it -- by calling `.clear()`. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
python ```
widget.clear()

```

## QComboBox signals
The `QComboBox` emits a number of signals on state changes. When the currently selected item changes, the widget emits `.currentIndexChanged()` and `.currentTextChanged()` signals. The first receives the _index_ of the selected entry while the second receives the text of that item. There is a further signal `.activated()` which is emitted for user-selections whether the index is changed or not: selecting the same entry again will still emit the signal. Highlighting an entry in the `QComboBox` popup list will emit the `.highlighted()` signal.
The following example demonstrates these signals in action.
python ```
from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    combobox = QComboBox()
    combobox.addItems(['One', 'Two', 'Three', 'Four'])
    # Connect signals to the methods.
    combobox.activated.connect(self.activated)
    combobox.currentTextChanged.connect(self.text_changed)
    combobox.currentIndexChanged.connect(self.index_changed)
    self.setCentralWidget(combobox)
  def activated(Self, index):
    print("Activated index:", index)
  def text_changed(self, s):
    print("Text changed:", s)
  def index_changed(self, index):
    print("Index changed", index)
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

```

If you run the example the signals emitted as you interact with the `QComboBox` will be shown in the console, giving output like that shown below. Note that when re-selecting the same entry, only the `.activated()` signal is emitted.
python ```
Index changed 1
Text changed: Two
Activated index: 1
Index changed 2
Text changed: Three
Activated index: 2
Index changed 3
Text changed: Four
Activated index: 3
Activated index: 3
Activated index: 3

```

## Getting the current state
In addition to the signals, `QComboBox` has a few methods for getting the current state at any time. For example, you can use `.currentIndex()` to get the _index_ of the currently selected item in the combobox, or use `.currentText()` to get the text. With the _index_ you can also look up the text of a specific item using `.itemText()`. Finally, you can use `.count()` to get the total number of items in the combobox list.
In the example below, we use the _activated signal_ we've already seen to hook up a number of methods which get information about the combobox and display this in the console. As you select any item in the combobox every method will run printing a message to the console.
python ```
from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    # Keep a reference to combobox on self, so we can access it in our methods.
    self.combobox = QComboBox()
    self.combobox.addItems(['One', 'Two', 'Three', 'Four'])
    # Connect signal to our methods.
    self.combobox.activated.connect(self.check_index)
    self.combobox.activated.connect(self.current_text)
    self.combobox.activated.connect(self.current_text_via_index)
    self.combobox.activated.connect(self.current_count)
    self.setCentralWidget(self.combobox)
  def check_index(self, index):
    cindex = self.combobox.currentIndex()
    print(f"Index signal: {index}, currentIndex {cindex}")
  def current_text(self, _): # We receive the index, but don't use it.
    ctext = self.combobox.currentText()
    print("Current text", ctext)
  def current_text_via_index(self, index):
    ctext = self.combobox.itemText(index) # Get the text at index.
    print("Current itemText", ctext)
  def current_count(self, index):
    count = self.combobox.count()
    print(f"Index {index+1}/{count}")

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

```

Running this and selecting different items in the combobox will show the outputs.
python ```
Current text Two
Current itemText Two
Index 1/4
Index signal: 2, currentIndex 2
Current text Three
Current itemText Three
Index 2/4
Index signal: 3, currentIndex 3
Current text Four
Current itemText Four
Index 3/4

```

## Editable comboboxes
You can set a `QComboBox` to be _editable_ allowing the user to type enter the values not currently in the list. Entered values can be added to the list, or just used as a value which is not inserted. To enable editing you can call `.setEditable(True)` on the widget, while control of how inserts operate is handled through the _insert policy_. This is set by calling `.setInsertPolicy()` passing one of the following flags:
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Flag | Value | Behavior  
---|---|---  
`QComboBox.NoInsert` | 0 | No insert  
`QComboBox.InsertAtTop` | 1 | Insert as first item  
`QComboBox.InsertAtCurrent` | 2 | Replace currently selected item  
`QComboBox.InsertAtBottom` | 3 | Insert after last item  
`QComboBox.InsertAfterCurrent` | 4 | Insert after current item  
`QComboBox.InsertBeforeCurrent` | 5 | Insert before current item  
`QComboBox.InsertAlphabetically` | 6 | Insert in alphabetical order  
For PyQt6 use the fully-qualified flag name, i.e. `QComboBox.InsertPolicy.NoInsert`
For example, to insert new values alphabetically, you would use.
python ```
widget.setInsertPolicy(QComboBox.InsertAlphabetically)

```

If the combobox is set to be editable, but `QComboBox.NoInsert` is set as the insert policy, users will be able to enter their own custom values, but they will not be added to the list. In the following example we have two `QComboBox` widgets: one which is our editable box and the second which controls the _insert policy_ of the first. Note that since the values of the flags (see above) are just numbers from 0 to 6, we can use the _index_ to determine the flag.
python ```
from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QVBoxLayout
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    # Keep a reference to combobox on self, so we can access it in our methods.
    self.combobox = QComboBox()
    self.combobox.addItems(['One', 'Two', 'Three', 'Four'])
    self.combobox.setEditable(True)
    self.combobox.currentTextChanged.connect(self.current_text_changed)
    # Insert policies
    self.insertpolicy = QComboBox()
    self.insertpolicy.addItems([
      'NoInsert',
      'InsertAtTop',
      'InsertAtCurrent',
      'InsertAtBottom',
      'InsertAfterCurrent',
      'InsertBeforeCUrrent',
      'InsertAlphabetically'
    ])
    # The index in the insertpolicy combobox (0-6) is the correct flag value to set
    # to enable that insert policy.
    self.insertpolicy.currentIndexChanged.connect(self.combobox.setInsertPolicy)
    layout = QVBoxLayout()
    layout.addWidget(self.combobox)
    layout.addWidget(self.insertpolicy)
    container = QWidget()
    container.setLayout(layout)
    self.setCentralWidget(container)
  def current_text_changed(self, s):
    print("Current text: ", s)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

```

If you run this example you'll notice you can now type into the (top) editable combobox and submit them by pressing Enter. The `.currentTextChanged()` signal will be emitted as you type into the field.
python ```
Current text: w
Current text: wq
Current text: wqe
Current text: wqew
Current text: wqeww
Current text: wqewwq
Current text: wqewwqe

```

By default the _insert policy_ is set to `QComboBox.NoInsert` so entered values will not be added, just set as the value of the combobox. By selecting the insert policy in the second combobox you can change this behavior, having new entries added to the list.
![Editing a QComboBox with insert policy](https://www.pythonguis.com/static/docs/qcombobox/qcombobox-insert.png) _Editing a QComboBox with insert policy_
When you allow users to add values to the list, you may wish to constrain the maximum number of entries. This can be done using `.setMaxCount`, e.g. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
python ```
widget.setMaxCount(10)

```

Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**QComboBox** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/docs/qcombobox/Python books) on the subject. 
**QComboBox** was published in [docs](https://www.pythonguis.com/docs/) on September 05, 2021 (updated March 15, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [widgets](https://www.pythonguis.com/topics/widgets/) [qcombobox](https://www.pythonguis.com/topics/qcombobox/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
