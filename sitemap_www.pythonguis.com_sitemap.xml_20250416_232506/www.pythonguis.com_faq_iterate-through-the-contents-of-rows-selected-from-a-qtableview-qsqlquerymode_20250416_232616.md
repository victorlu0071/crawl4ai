# Content from: https://www.pythonguis.com/faq/iterate-through-the-contents-of-rows-selected-from-a-qtableview-qsqlquerymodel/

[](https://www.pythonguis.com/faq/iterate-through-the-contents-of-rows-selected-from-a-qtableview-qsqlquerymodel/#menu)
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
# Iterate through the contents of rows selected from a QTableView QSqlQueryModel?
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
luis | 2020-10-02 21:46:29 UTC | #1
I'm going through the "Querying SQL databases with Qt models" chapter of the PySide2 edition of the book. I need something like the "databases\tableview_querymodel.py" sample. And then a button, that should perform something based on the contents of the rows selected by the user from that tableview.
So, how can I get the rows that were selected by the user from that tableview and then iterate through the contents of those selected rows?
Thanks in advance!
luis | 2020-10-01 22:22:36 UTC | #2
I found the answer. On my self.table = QTableView() I need to do this the retrieve the rows selected by the user:
`indexes = self.table.selectionModel().selectedRows()`
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
and then for example to print the contents of the 2nd column of the selected rows:
python ```
for index in indexes:
      print(self.table.model().data(self.table.model().index(index.row(), 1)))

```

martin | 2020-10-03 12:03:28 UTC | #3
Hey @luis yep that will do it. I'd take a reference to the `model` object first just to simplify the code a bit
python ```
model = self.table.model()
for index in indexes:
      print(model.data(model.index(index.row(), 1)))

```

~~Note, that in your `.data` method the second param `1` is `Qt.DecorationRole` -- not sure if this is what you intended? If you want to get the content you would use `Qt.DisplayRole` (which == 0) (see [roles](https://doc.qt.io/qt-5/qt.html#ItemDataRole-enum) enum in the documentation).~~ Ignore this my eyes were wonky with the brackets.
Also .... I was looking at the [selectedRows](https://doc.qt.io/qt-5/qitemselectionmodel.html#selectedRows) method though and noticed that it actually accepts a parameter _column_ which (slightly confusingly) is the value it uses for the column in the returned indexes.
Since you want the values in column 2, you can simplify a bit by passing that column number to `selectedRows` directly... it then returns the exact indexes you want.
python ```
indexes = self.table.selectionModel().selectedRows(column=2)
model = self.table.model()
role = Qt.DisplayRole # or Qt.DecorationRole
for index in indexes:
  print(model.data(index, role))

```

luis | 2020-10-02 14:03:16 UTC | #4
Much cleaner! Thanks for the hints.
edit: and in my code, the 1 in index.row(), 1 is needed to access the data of the second column. 0 gives me the 1st column, 2 would be the 3rd and so on.
martin | 2020-10-02 21:45:49 UTC | #5
Great, glad it helped! I think this is a good candidate to add tutorial about, common to want to find what is selected in a table.
[quote="luis, post:4, topic:495"] edit: and in my code, the 1 in index.row(), 1 is needed to access the data of the second column. 0 gives me the 1st column, 2 would be the 3rd and so on. [/quote]
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt5](https://www.pythonguis.com/static/theme/images/products/pyqt5-book.png)](https://www.pythonguis.com/pyqt5-book/)
[Take a look ](https://www.pythonguis.com/pyqt5-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/create-simple-gui-applications/) and [Amazon Paperback](https://www.amazon.com/dp/B08RB2HRS1/)
Ha, quite right -- got confused among all the brackets :D
Max_Fritzler | 2021-05-01 21:15:17 UTC | #7
I would really appreciate a tutorial on this. 
Also, you can apparently do something like: "self.myQSQLTableModel.record(integer).value("myFieldName")
I'm trying to use this because it allows reference by name. I hate using positional reference to a sql record, because it breaks if I find myself having to add or delete fields. This apparently acts through the model, whereas your solution Martin acts through the TableView. Since I'm a newbie with QT, I have not yet figured out when I should be using the model, and when the view.
thanks
Max_Fritzler | 2021-05-02 10:45:15 UTC | #8
and of course, Martin, in your example I can use fieldIndex to get the value by name, like this: indexes = self.utterancesTable.selectionModel().selectedRows(column=self.model.fieldIndex("UID"))
Maxim_Doucet | 2021-07-16 12:59:35 UTC | #9
You can also get the same result with:
python ```
indexes = self.table.selectionModel().selectedRows()
for index in indexes:
  print(index.child(index.row(), 1).data())

```

(no need to retrieve the model, the index is enough)
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Iterate through the contents of rows selected from a QTableView QSqlQueryModel?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/iterate-through-the-contents-of-rows-selected-from-a-qtableview-qsqlquerymodel/Python books) on the subject. 
**Iterate through the contents of rows selected from a QTableView QSqlQueryModel?** was published in [faq](https://www.pythonguis.com/faq/) on October 01, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyside](https://www.pythonguis.com/topics/pyside/) [qtableview](https://www.pythonguis.com/topics/qtableview/) [qsqlquerymodel](https://www.pythonguis.com/topics/qsqlquerymodel/) [sql](https://www.pythonguis.com/topics/sql/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [ databases](https://www.pythonguis.com/topics/databases/)
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
