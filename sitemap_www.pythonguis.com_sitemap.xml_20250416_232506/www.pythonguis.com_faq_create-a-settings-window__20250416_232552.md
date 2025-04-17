# Content from: https://www.pythonguis.com/faq/create-a-settings-window/

[](https://www.pythonguis.com/faq/create-a-settings-window/#menu)
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
# Create a Settings window
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
PedanticHacker | 2021-03-19 07:02:21 UTC | #1
Me again. :slight_smile:
I was thinking of implementing a Settings window into my app. You know, a window with a bunch of those on/off switches.
How would **you** go about it? Would you subclass from QDialog() or from QWidget()? Also, are there any examples already for PyQt5/PyQt6 or PySide2/PySide6 to help me get started?
Can anyone explain QSettings() to me? 🤔
martin | 2021-03-19 07:59:34 UTC | #2
Yeah, I would probably go with `QDialog` for something like this. You can subclass from the base to add any custom layout to the dialog and you still get the standard buttons etc. e.g. the following example from the book
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
python ```
class CustomDialog(QDialog):
  def __init__(self, parent=None): # <1>
    super().__init__(parent)
    self.setWindowTitle("HELLO!")
    QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
    self.buttonBox = QDialogButtonBox(QBtn)
    self.buttonBox.accepted.connect(self.accept)
    self.buttonBox.rejected.connect(self.reject)
    self.layout = QVBoxLayout()
    message = QLabel("Something happened, is that OK?")
    self.layout.addWidget(message)
    self.layout.addWidget(self.buttonBox)
    self.setLayout(self.layout)

```

You can definitely use `QSettings` for this, but I always found it to be a bit of a faff. You need to read your widgets and then write them to a settings object (and the reverse when you load them to display).
A while back I wrote a Python library to help with this [pyqtconfig](https://github.com/learnpyqt/pyqtconfig), which stores your settings in a Python dictionary and allows you to hook specific keys to specific widgets -- the link is 2 way, as in if you change the dictionary the widget will update, and if you change the widget the dictionary will update. Signals are fired on changes.
If you need it, that makes it easy to show immediate updates when settings are changed, do the "Apply" logic and allow them to be rolled back on Cancel/etc.
I haven't updated it in a while, so it might be a bit rusty. But it's on my todo list (also for PyQt6).
PedanticHacker | 2021-03-19 10:07:36 UTC | #3
Thanks for your answer, @martin! That was very helpful. :+1:
Also, I need help on merging a QGroupBox() with QRadioButton() widgets. I am playing with those two things and can't seem to merge them together. There's no example in the book and I am asking whether that can be added in the book, not just for me, but for others as well. Maybe an example of a Settings window with group boxes and radio buttons and all other related widgets would be very instructional. Just a thought.
PedanticHacker | 2021-03-19 12:01:42 UTC | #4
[quote="martin, post:2, topic:806"] `QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel` [/quote]
While this is okay in PySide6, PyQt6 throws an error. It's better like this: _PySide6:`QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel`_ PyQt6: `QBtn = QDialogButtonBox.StandardButtons.Ok | QDialogButtonBox.StandardButtons.Cancel`
While PySide6 uses the singular form (`StandardButton`), PyQt6 uses the plural form (`StandardButtons`). That is also a distinction between PySide6 and PyQt6 to keep in mind. All enums are like this: singular in PySide6, plural in PyQt6.
martin | 2021-03-27 01:15:02 UTC | #5
Here's an example using the `QGroupBox` -- the key is that `QGroupBox` is a widget, so to add the widgets to it you need to add them to a layout & then apply that layout onto the group box. It works the rest out itself.
python ```
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QRadioButton, QApplication, QLabel, QGroupBox
class CustomDialog(QDialog):
  def __init__(self, parent=None): # <1>
    super().__init__(parent)
    self.setWindowTitle("HELLO!")
    QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
    group_box = QGroupBox("Some radio buttons")
    radio1 = QRadioButton("Radio 1")
    radio2 = QRadioButton("Radio 1")
    radio3 = QRadioButton("Radio 1")
    radio_layout = QVBoxLayout()
    radio_layout.addWidget(radio1)
    radio_layout.addWidget(radio2)
    radio_layout.addWidget(radio3)
    group_box.setLayout(radio_layout)
    buttonBox = QDialogButtonBox(QBtn)
    buttonBox.accepted.connect(self.accept)
    buttonBox.rejected.connect(self.reject)
    layout = QVBoxLayout()
    layout.addWidget(group_box)
    layout.addWidget(buttonBox)
    self.setLayout(layout)

app = QApplication([])
dlg = CustomDialog()
dlg.exec_()

```

That should give you a dialog window with three options in a group, with them being exclusive. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
![Screenshot 2021-03-19 130751|220x213](https://www.pythonguis.com/static/faq/forum/create-a-settings-window/fUstkv3UGivQ1CxKu6qppXzLxW7.png)
[quote="PedanticHacker, post:4, topic:806"] While this is okay in PySide6, PyQt6 throws an error. It’s better like this: [/quote]
Ah yeah, I'm still writing with PyQt5. Find that change quite frustrating to be honest, ah well! :)
PedanticHacker | 2021-03-27 01:14:13 UTC | #6
[quote="martin, post:5, topic:806"] Ah yeah, I’m still writing with PyQt5. Find that change quite frustrating to be honest, ah well! :slight_smile: [/quote]
That bugs me, too. We'll all get used to it, eventually. Minor hickup. :wink:
Say, how can I now use those radio buttons so that my app responds accordingly to a radio button being in a different state (i.e., checked)?
martin | 2021-04-26 16:11:47 UTC | #7
The tricky part here is to read those settings and make them available elsewhere -- since once you destroy the dialog you can no longer read the values. That was the original reason I wrote the pyqtconfig module, to sync the data from config dialogs into a dictionary which you can then return as the "result" of a dialog.
You have a couple of options:
  1. connect signals on these, sending additional data (the value name) and receive this somewhere, to store it in a data object. The problem is you still need some way to set the initial state, and you can't postpone the changes until the dialog is OK/Applied
  2. load/unload the data from somewhere when opening the dialog (this is what I'd recommend)


You can implement something similar to pyqtconfig by creating a map of name, getter, setter and then using this to set/reset the values, e.g.
python ```

data = {
  'checkbox1': Qt.Checked,
  'checkbox2': Qt.Unchecked,
  'somestring': "hello",
  'int': 23
}
options = {
  'checkbox1': (obj.checkbox1.checkState, obj.checkbox1.setCheckState)
  'checkbox2': (obj.checkbox2.checkState, obj.checkbox2.setCheckState)
  'somestring': (obj.strinput.text, obj.strinput.setText)
  'int': (obj.spinbox1.value, obj.spinbox1.setValue)
}
# Set values from dictionary
for k, (_, setter) in options.items():
  value = data[k]
  setter(v)
# Copy values into dictionary
for k, (getter, ) in options.items():
  data[k] = getter()

```

In pyqtconfig the mapper getter/setters are handled automatically based on the type of the widget. For this you just need a table of object types and getter setter names, e.g.
python ```

data = {
  'checkbox1': Qt.Checked,
  'checkbox2': Qt.Unchecked,
  'somestring': "hello",
  'int': 23
}
mappers = {
  'QCheckBox': ('checkState', 'setCheckState'),
  'QLineEdit': ('text', 'setText'),
  'QSpinBox': ('value', 'setValue'),
}

options = {
  'checkbox1': obj.checkbox1,
  'checkbox2': obj.checkbox2,
  'somestring': obj.strinput,
  'int': obj.spinbox
}
# Set values from dictionary
for k, widget in options.items():
  widget_cls = widget.__class__
  getter_name, setter_name = mappers[widget_cls]
  value = data[k]
  setter = getattr(widget, setter)
  setter(v)
# Copy values into dictionary
for k, widget in options.items():
  widget_cls = widget.__class__
  getter_name, setter_name = mappers[widget_cls]
  getter = getattr(widget, getter_name)
  data[k] = getter()

```

You can wrap this up into some kind of handler object -- I'd recommend a central "config" manager which you can pass a series of widgets and config names and it handles the rest.
fyi you could do the same thing using `QSettings` and `.setValue()` and `.value()` in place of the dictionary `data` gets/sets if you prefer. The types for all standard widgets should be handled automatically. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyside2-book/) _by Martin Fitzpatrick_ — (PySide2 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside2-book/) [Get the book](https://secure.pythonguis.com/01hf778jyaajk5vk1q6824sd44/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Create a Settings window** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/create-a-settings-window/Python books) on the subject. 
**Create a Settings window** was published in [faq](https://www.pythonguis.com/faq/) on March 18, 2021 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
