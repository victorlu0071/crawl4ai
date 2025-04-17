# Content from: https://www.pythonguis.com/examples/python-web-browser-navigation/

[](https://www.pythonguis.com/examples/python-web-browser-navigation/#menu)
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
# Adding navigational controls to a PyQt5 Web Browser
Hook up QAction signals to web browser slots
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Jul 15 [ Build a Web Browser with PyQt5 ](https://www.pythonguis.com/pyqt5-tutorial/#example-browser)
#### [ PyQt5 Tutorial ](https://www.pythonguis.com/pyqt5-tutorial/) — [Build a Web Browser with PyQt5](https://www.pythonguis.com/pyqt5-tutorial/#example-browser)
  * [Mozzerella Ashbadger](https://www.pythonguis.com/examples/python-web-browser/)
  * [Adding navigational controls to a PyQt5 Web Browser](https://www.pythonguis.com/examples/python-web-browser-navigation/)
  * [Open and save HTML in a PyQt5 browser](https://www.pythonguis.com/examples/python-web-browser-save-html/)
  * [Adding application Help and About dialogs](https://www.pythonguis.com/examples/python-web-browser-dialogs/)
  * [Tabbed web browsing](https://www.pythonguis.com/examples/python-tabbed-web-browser/)


In the first part of this tutorial we put together a simple skeleton of a browser using Qt's built-in browser widget. This allows you to open a webpage, view it and click around -- all that is handled automatically for you. But the interface is entirely up to you.
To convert this bare-bones application into something more resembling an actual browser, in this part we'll set about adding UI controls. These are added as a series of `QActions` on a `QToolbar`. We add these definitions to the `__init__` block of the `QMainWindow`.
python ```
navtb = QToolBar("Navigation")
navtb.setIconSize( QSize(16,16) )
self.addToolBar(navtb)
back_btn = QAction( QIcon(os.path.join('icons','arrow-180.png')), "Back", self)
back_btn.setStatusTip("Back to previous page")
back_btn.triggered.connect( self.browser.back )
navtb.addAction(back_btn)

```

The `QWebEngineView` includes slots for forward, back and reload navigation, which we can connect to directly to our action's `.triggered` signals.
python ```
next_btn = QAction( QIcon(os.path.join('icons','arrow-000.png')), "Forward", self)
next_btn.setStatusTip("Forward to next page")
next_btn.triggered.connect( self.browser.forward )
navtb.addAction(next_btn)
reload_btn = QAction( QIcon(os.path.join('icons','arrow-circle-315.png')), "Reload", self)
reload_btn.setStatusTip("Reload page")
reload_btn.triggered.connect( self.browser.reload )
navtb.addAction(reload_btn)
home_btn = QAction( QIcon(os.path.join('icons','home.png')), "Home", self)
home_btn.setStatusTip("Go home")
home_btn.triggered.connect( self.navigate_home )
navtb.addAction(home_btn)

```

While forward, back and reload can use built-in slots to perform their actions, the navigate home button requires a custom slot function. The slot function is defined on our `QMainWindow` class, and simply sets the URL of the browser to the Google homepage. Note that the URL must be passed as a `QUrl` object.
python ```
def navigate_home(self):
  self.browser.setUrl( QUrl("http://www.google.com") )

```

Any decent web browser also needs an URL bar, and some way to stop the navigation.
python ```
self.httpsicon = QLabel() # Yes, really!
self.httpsicon.setPixmap( QPixmap( os.path.join('icons','lock-nossl.png') ) )
navtb.addWidget(self.httpsicon)
self.urlbar = QLineEdit()
self.urlbar.returnPressed.connect( self.navigate_to_url )
navtb.addWidget(self.urlbar)
stop_btn = QAction( QIcon(os.path.join('icons','cross-circle.png')), "Stop", self)
stop_btn.setStatusTip("Stop loading current page")
stop_btn.triggered.connect( self.browser.stop )
navtb.addAction(stop_btn)

```

As before the 'stop' functionality is available as a slot on the `QWebEngineView` itself, and we can simply connect the `.triggered` signal from the stop button to the existing slot. However, other features of the URL bar we must handle independently.
First we add a `QLabel` to hold our SSL or non-SSL icon to indicate whether the page is secure. Next, we add the URL bar which is simply a `QLineEdit`. To trigger the loading of the URL in the bar when entered (return key pressed) we connect to the `.returnPressed` signal on the widget to drive a custom slot function to trigger navigation to the specified URL. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
python ```
def navigate_to_url(self): # Does not receive the Url
  q = QUrl( self.urlbar.text() )
  if q.scheme() == "":
    q.setScheme("http")
  self.browser.setUrl(q)

```

We also want the URL bar to update in response to page changes. To do this we can use the `.urlChanged` and `.loadFinished` signals from the `QWebEngineView`. We set up the connections from the signals in the `__init__` block as follows:
python ```
self.browser.urlChanged.connect(self.update_urlbar)
self.browser.loadFinished.connect(self.update_title)

```

Then we define the target slot functions which for these signals. The first, to update the URL bar accepts a `QUrl` object and determines whether this is a `http` or `https` URL, using this to set the SSL icon.
This is a **terrible** way to test if a connection is 'secure'. To be correct we should perform a certificate validation. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
The `QUrl` is converted to a string and the URL bar is updated with the value. Note that we also set the cursor position back to the beginning of the line to prevent the `QLineEdit` widget scrolling to the end.
python ```
def update_urlbar(self, q):
  if q.scheme() == 'https':
    # Secure padlock icon
    self.httpsicon.setPixmap( QPixmap( os.path.join('icons','lock-ssl.png') ) )
  else:
    # Insecure padlock icon
    self.httpsicon.setPixmap( QPixmap( os.path.join('icons','lock-nossl.png') ) )
  self.urlbar.setText( q.toString() )
  self.urlbar.setCursorPosition(0)

```

It's also a nice touch to update the title of the application window with the title of the current page. We can get this via `browser.page().title()` which returns the contents of the `<title></title>` tag in the currently loaded web page.
python ```
def update_title(self):
  title = self.browser.page().title()
  self.setWindowTitle("%s - Mozarella Ashbadger" % title)

```

That's the basic interface implemented. In the next part we'll look at adding the standard Load & Save operations, to allow us to open local HTML files and save web pages to disk.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt5](https://www.pythonguis.com/static/theme/images/products/pyqt5-book.png)](https://www.pythonguis.com/pyqt5-book/)
[Take a look ](https://www.pythonguis.com/pyqt5-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/create-simple-gui-applications/) and [Amazon Paperback](https://www.amazon.com/dp/B08RB2HRS1/)
Mark As Complete 
Continue with [ PyQt5 Tutorial ](https://www.pythonguis.com/examples/python-web-browser-save-html/ "Continue to next part")
Return to [Create Desktop GUI Applications with PyQt5 ](https://www.pythonguis.com/pyqt5-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Adding navigational controls to a PyQt5 Web Browser** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/examples/python-web-browser-navigation/Python books) on the subject. 
**Adding navigational controls to a PyQt5 Web Browser** was published in [examples](https://www.pythonguis.com/examples/) on March 20, 2018 (updated July 15, 2021) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[web browser](https://www.pythonguis.com/topics/web-browser/) [browser](https://www.pythonguis.com/topics/browser/) [navigation](https://www.pythonguis.com/topics/navigation/) [qwebenginewidgets](https://www.pythonguis.com/topics/qwebenginewidgets/) [qt5](https://www.pythonguis.com/topics/qt5/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/)
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
