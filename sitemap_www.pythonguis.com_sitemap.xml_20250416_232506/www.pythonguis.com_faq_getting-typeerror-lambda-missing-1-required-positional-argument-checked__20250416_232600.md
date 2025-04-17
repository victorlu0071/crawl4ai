# Content from: https://www.pythonguis.com/faq/getting-typeerror-lambda-missing-1-required-positional-argument-checked/

[](https://www.pythonguis.com/faq/getting-typeerror-lambda-missing-1-required-positional-argument-checked/#menu)
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
# Getting TypeError: () missing 1 required positional argument: 'checked'
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
Gdaliy_Garmiza | 2020-11-16 12:18:04 UTC | #1
Hi, Martin!
I purchased your book a couple of months ago. It helps me a lot. I'm currently developing my own application, where I try to implement the 'Open recent files' functionality in the main menu. It's quite similar to your example here: https://www.pythonguis.com/tutorials/transmitting-extra-data-qt-signals/ with the difference that I connect the 'triggered' signals to the QActions (the list of files, generated in the loop). But neither my nor your code works for me.
Both
button.clicked.connect(lambda checked, a=a: self.button_clicked(a)) # [in your 'signals_extra_3.py' script]
and
new_act.triggered.connect(lambda checked, filename=file: self.OpenRecent(filename)) # [in my code] 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
give out the TypeError: () missing 1 required positional argument: 'checked'. I use PySide2 and Python 3.8
Thanks.
martin | 2020-11-16 14:51:04 UTC | #2
Hi @Gdaliy_Garmiza welcome to the forum! Glad you're finding the book useful.
Yep, this unfortunately due to differences in how the `.triggered()` and `.clicked()` signals work between version of PyQt5 (& PySide2). The "checked" parameter is (according to [the documentation](https://doc.qt.io/qt-5/qaction.html#triggered)) supposed to be sent with the `.triggered` signal, for example, but it isn't 
Can you check if this also happens when connecting to a real method (vs. a `lambda`)? I wonder if that has something to do with it.
If you don't need the `checked` parameter (i.e. the action or button is not toggleable) you can just remove that parameter from your receiver method/function.
Gdaliy_Garmiza | 2020-11-17 00:53:23 UTC | #3
Hi, @martin!
Thanks for your quick response. I seem to have tried almost all the combinations with no success.
E.g.:
python ```
# self.OpenRecentList — list of the full filenames/paths
for file in self.OpenRecentList:
  new_act = QAction(file, self)
  self.menuOpen_Recent.addAction(new_act)
  new_act.triggered.connect(lambda filename=file: self.OpenRecent(filename))
def OpenRecent(self, file):
# Code that opens a file

```

Result: When triggering the created actions(menu items) it tries to pass the boolean instead of the filename, because the error “File False not found” is raised within my app. It seems to be the boolean from the ‘checked’ parameter which is sent from the triggered signal, but omitted in my code.
—
python ```
for file in self.OpenRecentList:
  def open_recent_connector(filename=file):
    return self.OpenRecent(filename)
  new_act = QAction(file, self)
  self.menuOpen_Recent.addAction(new_act)
  new_act.triggered.connect(open_recent_connector)

```

Result: the same as above. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
python ```
for file in self.OpenRecentList:
  def open_recent_connector(checked, filename=file):
    return self.OpenRecent(filename)
  new_act = QAction(file, self)
  self.menuOpen_Recent.addAction(new_act)
  new_act.triggered.connect(open_recent_connector)

```

Result (on triggering the action): TypeError: open_recent_connector() missing 1 required positional argument: 'checked'.
python ```
for file in self.OpenRecentList:
  filename = file
  def open_recent_connector():
    return self.OpenRecent(filename)
  new_act = QAction(file, self)
  self.menuOpen_Recent.addAction(new_act)
  new_act.triggered.connect(open_recent_connector)

```

Result (on triggering the action): the OpenRecent function is called (it opens the file), but the ‘loop problem’, described in your book, occurs. It passes the value of the last iteration when any QAction is triggered, and my app always opens the last file in the list.
Trying to fix it using your 'naming method' I went even as far as that:
python ```
new_act = []
for ind, file in enumerate(self.OpenRecentList):
  def open_recent_connector():
    filename = self.OpenRecentList[ind]
    return self.OpenRecent(filename)
  new_act.append(QAction(file, self))
  self.menuOpen_Recent.addAction(new_act[ind])
  new_act[ind].triggered.connect(open_recent_connector)

```

Result (on triggering the action): the same as above (the loop problem).
Gdaliy_Garmiza | 2020-11-17 17:41:40 UTC | #4
Hey, @martin
I have found the correct solution how to do this without lambda here: https://stackoverflow.com/questions/52283469/using-qsignalmapper
Here is the code which worked for me:
`from functools import partial` ...
python ```
def open_recent_menu_builder(self):
   for file in self.OpenRecentList:
     new_act = QAction(file, self)
     self.menuOpen_Recent.addAction(new_act)
     new_act.triggered.connect(partial(self.OpenRecent, file))
def OpenRecent(self, file):
# Code that opens a file

```

Jesus_Gangoso_Burgos | 2021-01-07 16:06:36 UTC | #5
Hi,
in order the code in the signals_extra_3.py script work, change "checked" by "*args". That is,
button.clicked.connect(lambda *args, val=a: self.button_clicked(val)) # <1>
in line 25.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Getting TypeError:() missing 1 required positional argument: 'checked'** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/getting-typeerror-lambda-missing-1-required-positional-argument-checked/Python books) on the subject. 
**Getting TypeError:() missing 1 required positional argument: 'checked'** was published in [faq](https://www.pythonguis.com/faq/) on November 16, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyside](https://www.pythonguis.com/topics/pyside/) [python38](https://www.pythonguis.com/topics/python38/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
