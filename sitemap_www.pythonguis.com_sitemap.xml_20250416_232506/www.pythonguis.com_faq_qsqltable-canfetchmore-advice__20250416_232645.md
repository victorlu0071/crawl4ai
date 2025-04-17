# Content from: https://www.pythonguis.com/faq/qsqltable-canfetchmore-advice/

[](https://www.pythonguis.com/faq/qsqltable-canfetchmore-advice/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PyQt5 ](https://www.pythonguis.com/pyqt5/)
  * [PyQt5 Tutorial ](https://www.pythonguis.com/pyqt5-tutorial/)
  * Basics
  * [Create a PyQt5 app](https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/)
  * [PyQt5 Signals](https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/)
  * [PyQt5 Widgets](https://www.pythonguis.com/tutorials/pyqt-basic-widgets/)
  * [PyQt5 Layouts](https://www.pythonguis.com/tutorials/pyqt-layouts/)
  * [PyQt5 Menus](https://www.pythonguis.com/tutorials/pyqt-actions-toolbars-menus/)
  * [PyQt5 Dialogs](https://www.pythonguis.com/tutorials/pyqt-dialogs/)
  * [Multi-window PyQt5](https://www.pythonguis.com/tutorials/creating-multiple-windows/)
  * Qt Designer
  * [First Qt Designer app](https://www.pythonguis.com/tutorials/first-steps-qt-creator/)
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/creating-dialogs-qt-designer/)
  * [The QResource System in PyQt5](https://www.pythonguis.com/tutorials/qresource-system/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/)
  * Plotting
  * [Plotting With PyQtGraph and PyQt5](https://www.pythonguis.com/tutorials/plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PyQt5](https://www.pythonguis.com/tutorials/plotting-matplotlib/)
  * QGraphics
  * [Vector Graphics](https://www.pythonguis.com/tutorials/pyqt-qgraphics-vector-graphics/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/qpropertyanimation/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/system-tray-mac-menu-bar-applications-pyqt/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/)
  * [Packaging for Linux](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-linux-pyinstaller/)
  * [Packaging QResources](https://www.pythonguis.com/tutorials/packaging-data-files-pyqt5-with-qresource-system/)
  * [Packaging with fbs](https://www.pythonguis.com/tutorials/packaging-pyqt5-apps-fbs/)
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
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# QSqltable canFetchMore advice
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
mike2750 | 2020-07-23 03:53:32 UTC | #1
I noticed this odd issue a few weeks ago and only recently found out the why and wondering if anyone has any pyqt5 snippets for qsortfilter model with canfetchmore.
References i could find for regular QT https://stackoverflow.com/questions/27372078/qtableview-export-to-csv-number-of-rows-fetched-is-limited-to-only-256/27372480#27372480 https://stackoverflow.com/questions/50181951/qtableview-not-showing-all-of-the-data-from-an-sqlite-database
Basically unless i load a further section in the DB first and then try again my search which has stuff in it its missing results. Was super frustrating as it took awhile to find out how to trigger the whole DB but i'd like to properly implement it so it shows all the stuff.
Excerpt of my current bits for QSqltable and its using sqlite driver for the DB
In Main
python ```
    self.commandcategorydropdown.setCurrentText('All')
    db.open()
    self.model = QSqlTableModel()
    self.initializedModel()
    #
    # self.commands.tableView = QTableView()
    # self.commands.tableView.setModel(self.model)
    # self.tableView = QTableView(self.commandsbox)
    self.tableView.verticalHeader().setVisible(False)
    # self.tableView.resizeColumnsToContents()
    # self.tableView.resizeRowsToContents()
    # self.tableView.horizontalHeader().setVisible(False)
    # self.tableView.horizontalHeader().setDefaultAlignment(Qt.AlignLeft)
    self.tableView.horizontalHeader().setStretchLastSection(True)
    self.source_model = self.model
    # self.initializedModel()
    self.proxy_model = QSortFilterProxyModel(self.source_model)
    self.proxy_model.setSourceModel(self.source_model)
    self.tableView.setModel(self.proxy_model)
    self.tableView.hideColumn(0)
    self.tableView.hideColumn(1)
    self.tableView.hideColumn(3)
    self.tableView.hideColumn(4)
    self.tableView.hideColumn(5)
    self.tableView.hideColumn(6)
    self.tableView.hideColumn(7)
    # self.proxy_model.setFilterRegExp(QRegExp(self.searchcommands.text(), Qt.CaseInsensitive,
    #                     QRegExp.FixedString))
    # self.proxy_model.setFilterKeyColumn(-1)
    self.tableView.setSortingEnabled(True)
    self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
    # self.tableView.setWordWrap(True)
    # self.command_description = QLabel()
    # self.command_description.setWordWrap(True)
    # self.command_requires_label = QLabel('')
    # self.command_requires_label.setWordWrap(True)
    # self.verticalLayout_8.addWidget(self.commandsbox)
    # self.verticalLayout_8.addWidget(self.tableView)
    # self.verticalLayout_8.addWidget(self.searchcommands)
    # self.verticalLayout_8.addWidget(self.command_requires_label)
    # self.verticalLayout_8.addWidget(self.command_description)
    self.commandcategorydropdown.activated.connect(self.current_activated_category)
  def on_searchcommands_update(self):
    self.proxy_model.setFilterRegExp(QRegExp(self.searchcommands.text(), Qt.CaseInsensitive,
                         QRegExp.FixedString))
    self.proxy_model.setFilterKeyColumn(-1)

  def current_activated_category(self):
    global command_category
    command_category = str(self.commandcategorydropdown.currentText())
    print(str(self.commandcategorydropdown.currentText()))
    # db.open()
    # self.commandslist.projectModel.setQuery(
    #   QtSql.QSqlQuery("SELECT command_alias, command FROM commands WHERE category = '%s'" % command_category))
    # self.commandslist.projectView = QListView(self.commandslist)
    # self.commandslist.projectView.setModel(self.commandslist.projectModel)
    # db.close()
    self.command_description.setText('')
    self.command_requires_label.setText('')
    self.searchcommands.setText('')
    if command_category == 'All':
      self.proxy_model.setFilterRegExp(QRegExp(self.searchcommands.text(), Qt.CaseInsensitive,
                           QRegExp.FixedString))
      self.proxy_model.setFilterKeyColumn(-1)
    else:
      self.proxy_model.setFilterRegExp(QRegExp(self.commandcategorydropdown.currentText(), Qt.CaseSensitive,
                           QRegExp.FixedString))
      self.proxy_model.setFilterKeyColumn(1)
    # db.close()
  def on_searchcommands_update(self):
    self.proxy_model.setFilterRegExp(QRegExp(self.searchcommands.text(), Qt.CaseInsensitive,
                         QRegExp.FixedString))
    self.proxy_model.setFilterKeyColumn(-1)

  def initializedModel(self):
    self.model.setTable("commands")
    # self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
    self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    self.model.select()
    self.model.setHeaderData(0, Qt.Horizontal, "ID")
    self.model.setHeaderData(1, Qt.Horizontal, "Category")
    self.model.setHeaderData(2, Qt.Horizontal, "command_alias")
    self.model.setHeaderData(3, Qt.Horizontal, "command")
    self.model.setHeaderData(4, Qt.Horizontal, "requires")
    self.model.setHeaderData(5, Qt.Horizontal, "description")
    self.model.setHeaderData(6, Qt.Horizontal, "controlpanel")
    self.model.setHeaderData(7, Qt.Horizontal, "verification")
  def onAddRow(self):
    self.model.insertRows(self.model.rowCount(), 1)
    self.model.submit()
  def onDeleteRow(self):
    self.model.removeRow(self.tableView.currentIndex().row())
    self.model.submit()
    self.model.select()
  def closeEvent(self, event):
    db.close()

```

Any advice or guidance would be greatly appreciated. The 'current_activated_category' and 'on_searchcommands_update' function is what i use to filter results by qcombobox and lineedit so would need to ideally work when these are called. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
mike2750 | 2020-07-24 13:40:35 UTC | #2
Ended up getting this problem sorted by using the below snippet at the end of the "initializedModel" function. Now loads all into and works on start without having to trigger manual stuff in the UI 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
python ```
def initializedModel(self):

```

python ```
  while self.model.canFetchMore():
    self.model.fetchMore()
  self.model.rowCount()

```

leaving this here in case anyone else runs into the same issue.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**QSqltable canFetchMore advice** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/qsqltable-canfetchmore-advice/Python books) on the subject. 
**QSqltable canFetchMore advice** was published in [faq](https://www.pythonguis.com/faq/) on July 23, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
