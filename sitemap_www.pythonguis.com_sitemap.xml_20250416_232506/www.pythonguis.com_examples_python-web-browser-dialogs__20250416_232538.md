# Content from: https://www.pythonguis.com/examples/python-web-browser-dialogs/

[](https://www.pythonguis.com/examples/python-web-browser-dialogs/#menu)
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
# Adding application Help and About dialogs
Put some finishing touches to your application
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ Build a Web Browser with PyQt5 ](https://www.pythonguis.com/pyqt5-tutorial/#example-browser)
#### [ PyQt5 Tutorial ](https://www.pythonguis.com/pyqt5-tutorial/) — [Build a Web Browser with PyQt5](https://www.pythonguis.com/pyqt5-tutorial/#example-browser)
  * [Mozzerella Ashbadger](https://www.pythonguis.com/examples/python-web-browser/)
  * [Adding navigational controls to a PyQt5 Web Browser](https://www.pythonguis.com/examples/python-web-browser-navigation/)
  * [Open and save HTML in a PyQt5 browser](https://www.pythonguis.com/examples/python-web-browser-save-html/)
  * [Adding application Help and About dialogs](https://www.pythonguis.com/examples/python-web-browser-dialogs/)
  * [Tabbed web browsing](https://www.pythonguis.com/examples/python-tabbed-web-browser/)


In the previous parts we've added some basic UI elements, including menus and toolbars, and implemented basic loading & saving of HTML files to the browser view. Now, to complete the standard interface, we will add a Help menu.
Since our application is a web browser, it makes sense to show the help in the browser view. We have two options here: either include the help HTML with the application, and use our _load HTML_ code from the previous tutorial. Or, load up a web page in the browser view.
Here we're doing the latter, redirecting the user to a web page (this tutorial!) but have a go at implementing loading a HTML file for custom offline help.
python ```
help_menu = self.menuBar().addMenu("&Help")
about_action = QAction( QIcon( os.path.join('icons','question.png') ), "About Mozarella Ashbadger", self)
about_action.setStatusTip("Find out more about Mozarella Ashbadger") # Hungry!
about_action.triggered.connect( self.about )
help_menu.addAction(about_action)
navigate_mozarella_action = QAction( QIcon( os.path.join('icons','lifebuoy.png') ), "Mozarella Ashbadger Homepage", self)
navigate_mozarella_action.setStatusTip("Go to Mozarella Ashbadger Homepage")
navigate_mozarella_action.triggered.connect( self.navigate_mozarella )
help_menu.addAction(navigate_mozarella_action)

```

Next we add two custom slot methods to handle the display of the dialog, and to load the 'browser page' with more information.
The first method `navigate_mozzarella` opens up a page with more information on the browser, the second creates and executes a custom `QDialog` class `AboutDialog`.
python ```
def navigate_mozarella(self):
  self.browser.setUrl( QUrl("https://www.pythonguis.com/courses/example-browser/") )
def about(self):
  dlg = AboutDialog()
  dlg.exec_()

```

The definition for the about dialog is given below. The structure follows that seen earlier, with a `QDialogButtonBox` and associated signals to handle user input, and a series of `QLabels` to display the application information and a logo.
The only trick here is adding all the elements to the layout, then iterate over them to set the alignment to the center in a single loop. This saves duplication for the individual sections. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
python ```
class AboutDialog(QDialog):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    QBtn = QDialogButtonBox.Ok # No cancel
    self.buttonBox = QDialogButtonBox(QBtn)
    self.buttonBox.accepted.connect(self.accept)
    self.buttonBox.rejected.connect(self.reject)
    layout = QVBoxLayout()
    title = QLabel("Mozarella Ashbadger")
    font = title.font()
    font.setPointSize(20)
    title.setFont(font)
    layout.addWidget(title)
    logo = QLabel()
    logo.setPixmap( QPixmap( os.path.join('icons','ma-icon-128.png') ) )
    layout.addWidget(logo)
    layout.addWidget( QLabel("Version 23.35.211.233232") )
    layout.addWidget( QLabel("Copyright 2015 Mozarella Inc.") )
    for i in range(0, layout.count() ):
      layout.itemAt(i).setAlignment( Qt.AlignHCenter )
    layout.addWidget(self.buttonBox)
    self.setLayout(layout)

```

The completes the basic user interface for our web browser. In the next part we're going to take this functional web browser and extend it to implemented tabbed web browsing -- allowing you to keep multiple documents open at the same time. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Have other improvements you'd like to make? Then do! It's the best way to learn.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt5](https://www.pythonguis.com/static/theme/images/products/pyside2-book.png)](https://www.pythonguis.com/pyside2-book/)
[Take a look ](https://www.pythonguis.com/pyside2-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/create-gui-applications-pyside/) and [Amazon Paperback](https://www.amazon.com/dp/B08R92BW7R/)
Mark As Complete 
Continue with [ PyQt5 Tutorial ](https://www.pythonguis.com/examples/python-tabbed-web-browser/ "Continue to next part")
Return to [Create Desktop GUI Applications with PyQt5 ](https://www.pythonguis.com/pyqt5-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Adding application Help and About dialogs** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/examples/python-web-browser-dialogs/Python books) on the subject. 
**Adding application Help and About dialogs** was published in [examples](https://www.pythonguis.com/examples/) on March 20, 2018 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[web browser](https://www.pythonguis.com/topics/web-browser/) [browser](https://www.pythonguis.com/topics/browser/) [qt5](https://www.pythonguis.com/topics/qt5/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/)
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
