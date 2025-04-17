# Content from: https://www.pythonguis.com/examples/python-web-browser-save-html/

[](https://www.pythonguis.com/examples/python-web-browser-save-html/#menu)
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
# Open and save HTML in a PyQt5 browser
Adding file dialogs to load and save HTML
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Jul 15 [ Build a Web Browser with PyQt5 ](https://www.pythonguis.com/pyqt5-tutorial/#example-browser)
#### [ PyQt5 Tutorial ](https://www.pythonguis.com/pyqt5-tutorial/) — [Build a Web Browser with PyQt5](https://www.pythonguis.com/pyqt5-tutorial/#example-browser)
  * [Mozzerella Ashbadger](https://www.pythonguis.com/examples/python-web-browser/)
  * [Adding navigational controls to a PyQt5 Web Browser](https://www.pythonguis.com/examples/python-web-browser-navigation/)
  * [Open and save HTML in a PyQt5 browser](https://www.pythonguis.com/examples/python-web-browser-save-html/)
  * [Adding application Help and About dialogs](https://www.pythonguis.com/examples/python-web-browser-dialogs/)
  * [Tabbed web browsing](https://www.pythonguis.com/examples/python-tabbed-web-browser/)


A File menu was added with `self.menuBar().addMenu("&File")` assigning the `F` key as a Alt-shortcut. Once we have the menu object, we can can add `QAction` objects to it to create the entries. We create two basic entries here for opening and saving HTML files (from a local disk). These both require custom slot method.
python ```
file_menu = self.menuBar().addMenu("&File")
open_file_action = QAction( QIcon( os.path.join('icons','disk--arrow.png') ), "Open file...", self)
open_file_action.setStatusTip("Open from file")
open_file_action.triggered.connect( self.open_file )
file_menu.addAction(open_file_action)
save_file_action = QAction( QIcon( os.path.join('icons','disk--pencil.png') ), "Save Page As...", self)
save_file_action.setStatusTip("Save current page to file")
save_file_action.triggered.connect( self.save_file )
file_menu.addAction(save_file_action)

```

The slot method for opening a file uses the built-in `QFileDialog.getOpenFileName()` method to create a file-open dialog and get a name. We restrict the names by default to files matching `\*.htm` or `*.html`.
We read the file into a variable `html` using standard Python functions, then use `.setHtml()` to load the HTML into the browser.
python ```
def open_file(self):
  filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
          "Hypertext Markup Language (*.htm *.html);;"
          "All files (*.*)")
  if filename:
    with open(filename, 'r') as f:
      html = f.read()
    self.browser.setHtml( html )
    self.urlbar.setText( filename )

```

Similarly to save the HTML from the current page, we use the built-in `QFileDialog.getSaveFileName()` to get a filename. However, this time we get the HTML from `self.browser.page().toHtml()` and write it to the selected filename. Again we use standard Python functions for the file handler.
python ```
def save_file(self):
  filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
          "Hypertext Markup Language (*.htm *html);;"
          "All files (*.*)")
  if filename:
    html = self.browser.page().toHtml()
    with open(filename, 'w') as f:
      f.write(html)

```

Now we have the basic file operations in place. In the next part we'll next improve the interface further by adding a custom Help & About dialog to inform our users.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
Continue with [ PyQt5 Tutorial ](https://www.pythonguis.com/examples/python-web-browser-dialogs/ "Continue to next part")
Return to [Create Desktop GUI Applications with PyQt5 ](https://www.pythonguis.com/pyqt5-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Open and save HTML in a PyQt5 browser** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/examples/python-web-browser-save-html/Python books) on the subject. 
**Open and save HTML in a PyQt5 browser** was published in [examples](https://www.pythonguis.com/examples/) on March 20, 2018 (updated July 15, 2021) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
