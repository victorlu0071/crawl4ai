# Content from: https://www.pythonguis.com/faq/navigating-qsqltablemodel-and-qtableview-in-very-large-databases/

[](https://www.pythonguis.com/faq/navigating-qsqltablemodel-and-qtableview-in-very-large-databases/#menu)
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
# Navigating QSqlTableModel and QTableView in very large databases
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
Max_Fritzler | 2021-05-04 15:16:40 UTC | #1
After reading Martin's excellent book, looking through tutorials, building some UI's, I must confess I'm missing something fundamental about navigating through the TableViews when they are showing large databases. I'm building an app for my son, a sociolinguist. These folks search through enormous amounts of data from social media looking for word patterns of interest. Currently we have a database of 668,000 rows, each containing a transcipt of up to 30 seconds of conversation, maximum 2K characters, average length of 80 characters.
The use case is to filter on phrases of interest, then when found, unfilter, and jump to the same record of interest so as to see the rest of the conversation around that phrase. Finally, click a button that launches the youtube video and start it at that phrase. I have all that working, EXCEPT the jump to the same record upon filter change. Also, we need to save the user's place and restore it when restarting the app. The user can spend days searching. 
Qt automatically pages this large dataset beautifully, in 256 record chunks.
So I thought, ok, use model.match to find, say, the record where the UID = 1000. But match only searches through the 256 records currently being displayed. There are several use cases where I know the record key from the database (UID), and I need to find and display that record and surrounding records in the tableview.
If I had the index of the record, I could do table.setCurrentIndex(index). Ah, but how do I get the index? If I knew the row, I could do table.selectRow(), except that it, too, is limited to the 256 records in the current page. table.selectRow(1000) throws no error, but does nothing.
This is starting to sound like a job for a proxy model. Filter for the UID so there is only one row that matches, then get the matching index in the source model and do sourcetable.setCurrentIndex(the found index). 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Surely it's not that hard, and I'm missing something fundamental. Please advise. thanks in advance.
Max_Fritzler | 2021-05-06 12:54:15 UTC | #2
The 256 row limit applies to filtering with a proxy model. UID is the integer key for the table. I got a TableView with a proxy model going, and can filter for e.g., UID 255 just fine. But not for UID 256. As expected, once I filter for and display UID 255 I can filter for the next 255 UIDs, as they are evidently loaded into the QTableView. But nothing past that.
This seems to leave me with three options that I can think of. First, do some kind of "loop till end of database" and do Match, or SelectRow, or a proxyfilter inside the loop. I'll bet that is prohibitively slow on a db of 600,000 records.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Second, create a second model and second tableview, filter the second model with self.model2.setFilter("UID >= 1000) (for example) If the user then does PgUp, I'll have to reset model2 with a new WHERE clause. Ick
Third, abandon the desired UI consisting of a single TableView that toggles between filtered and unfiltered states, while keeping the same row selected. Replace it with a two TableView window (kind of like the two TreeView window in basicsortfiltermodel.py in the examples). Then for each selectionChanged event in the TableView, do some sort of selectRow in the unfiltered Table view, so the same record appears in both. The unfiltrered TableView then shows the context of the conversation, not just the rows with the phrase of interest to the user. That still leaves me without a way to just GoTO UID 43,000 without filtering the model via a WHERE clause, and so complicating things when the user decides to scroll or page toward the front of the record set. In protyping sessions I have seen this happen a lot as the user compares two different conversations, separated by thousands of rows, to see which best suits the research project he has in mind.
Max_Fritzler | 2021-05-17 19:09:27 UTC | #3
I implemented option 3 above, writing my own crude paging logic. I use two separate sqltablemodels, each with a separate tableview, and using keyPressed, the selectionChanged signal, and the valueChanged.minimum signal for scrollbars. For those signals I reapply tablemodel.setFilter to the appropriate tablemodel, and scrollTo and selectRow for the Tableviews. The app is out to the user and so we'll see how well this scheme works. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Navigating QSqlTableModel and QTableView in very large databases** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/navigating-qsqltablemodel-and-qtableview-in-very-large-databases/Python books) on the subject. 
**Navigating QSqlTableModel and QTableView in very large databases** was published in [faq](https://www.pythonguis.com/faq/) on May 03, 2021 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyside](https://www.pythonguis.com/topics/pyside/) [qtableview](https://www.pythonguis.com/topics/qtableview/) [python38](https://www.pythonguis.com/topics/python38/) [qsqlquerymodel](https://www.pythonguis.com/topics/qsqlquerymodel/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
