# Content from: https://www.pythonguis.com/examples/python-tabbed-web-browser/

[](https://www.pythonguis.com/examples/python-tabbed-web-browser/#menu)
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
# Tabbed web browsing
Use signal redirection to add a multi-tab interface
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 04 PyQt5 [ Build a Web Browser with PyQt5 ](https://www.pythonguis.com/pyqt5-tutorial/#example-browser)
#### [ PyQt5 Tutorial ](https://www.pythonguis.com/pyqt5-tutorial/) — [Build a Web Browser with PyQt5](https://www.pythonguis.com/pyqt5-tutorial/#example-browser)
  * [Mozzerella Ashbadger](https://www.pythonguis.com/examples/python-web-browser/)
  * [Adding navigational controls to a PyQt5 Web Browser](https://www.pythonguis.com/examples/python-web-browser-navigation/)
  * [Open and save HTML in a PyQt5 browser](https://www.pythonguis.com/examples/python-web-browser-save-html/)
  * [Adding application Help and About dialogs](https://www.pythonguis.com/examples/python-web-browser-dialogs/)
  * [Tabbed web browsing](https://www.pythonguis.com/examples/python-tabbed-web-browser/)


In the previous parts of this tutorial we built our own custom web browser using PyQt5 widgets. Starting from a basic app skeleton we've extended it to add support a simple UI, help dialogs and file operations. However, one big feature is missing -- tabbed browsing.
Tabbed browsing was a revolution when it first arrived, but is now an expected feature of web browsers. Being able to keep multiple documents open in the same window makes it easier to keep track of things as you work. In this tutorial we'll take our existing browser application and implement tabbed browsing in it.
This is a little tricky, making use of [signal redirection](https://www.pythonguis.com/transmitting-extra-data-qt-signals/) to add additional data about the current tab to Qt's built-in signals. If you get confused, take a look back at that tutorial.
![Mozarella Ashbadger \(Tabbed\)](https://www.pythonguis.com/static/examples/pyqt-example-browser/browser-tabbed-home.png)
The full source code for _Mozzarella Ashbadger_ is available in the [15 minute apps](https://github.com/learnpyqt/15-minute-apps/tree/master/browser_tabbed) repository. You can download/clone to get a working copy, then install requirements using:
bash ```
pip3 install -r requirements.txt

```

You can then run _Mozzarella Ashbadger_ with:
bash ```
python3 browser_tabbed.py

```

Read on for a walkthrough of how to convert the existing browser code to support tabbed browsing. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
## Creating a `QTabWidget`
Adding a tabbed interface to our browser is simple using a `QTabWidget`. This provides a simple container for multiple widgets (in our case `QWebEngineView` widgets) with a built-in tabbed interface for switching between them.
Two customisations we use here are `.setDocumentMode(True)` which provides a Safari-like interface on Mac, and `.setTabsClosable(True)` which allows the user to close the tabs in the application.
We also connect `QTabWidget` signals `tabBarDoubleClicked`, `currentChanged` and `tabCloseRequested` to custom slot methods to handle these behaviours.
python ```
class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.tabs = QTabWidget()
    self.tabs.setDocumentMode(True)
    self.tabs.tabBarDoubleClicked.connect( self.tab_open_doubleclick )
    self.tabs.currentChanged.connect( self.current_tab_changed )
    self.tabs.setTabsClosable(True)
    self.tabs.tabCloseRequested.connect( self.close_current_tab )
    self.setCentralWidget(self.tabs)

```

The three slot methods accept an `i` (index) parameter which indicates which tab the signal resulted from (in order).
We use a double-click on an empty space in the tab bar (represented by an index of `-1` to trigger creation of a new tab. For removing a tab, we use the index directly to remove the widget (and so the tab), with a simple check to ensure there are at least 2 tabs — closing the last tab would leave you unable to open a new one.
The `current_tab_changed` handler uses a `self.tabs.currentWidget()` construct to access the widget (`QWebEngineView` browser) of the currently active tab, and then uses this to get the URL of the current page. This same construct is used throughout the source for the tabbed browser, as a simple way to interact with the current browser view.
python ```
  def tab_open_doubleclick(self, i):
    if i == -1: # No tab under the click
      self.add_new_tab()
  def current_tab_changed(self, i):
    qurl = self.tabs.currentWidget().url()
    self.update_urlbar( qurl, self.tabs.currentWidget() )
    self.update_title( self.tabs.currentWidget() )
  def close_current_tab(self, i):
    if self.tabs.count() < 2:
      return
    self.tabs.removeTab(i)

```

The code for adding a new tab is is follows:
python ```
  def add_new_tab(self, qurl=None, label="Blank"):
    if qurl is None:
      qurl = QUrl('')
    browser = QWebEngineView()
    browser.setUrl( qurl )
    i = self.tabs.addTab(browser, label)
    self.tabs.setCurrentIndex(i)

```

## Signal & Slot changes
While the setup of the `QTabWidget` and associated signals is simple, things get a little trickier in the browser slot methods. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Whereas before we had a single `QWebEngineView` now there are multiple views, all with their own signals. If signals for hidden tabs are handled things will get all mixed up. For example, the slot handling a `loadCompleted` signal must check that the source view is in a visible tab and only act if it is.
We can do this using [a little trick](https://www.pythonguis.com/tutorials/transmitting-extra-data-qt-signals/) for sending additional data with signals. Below is an example of doing this when creating a new `QWebEngineView` in the `add_new_tab` function.
python ```
  def add_new_tab(self, qurl=None, label="Blank"):
    if qurl is None:
      qurl = QUrl('')
    browser = QWebEngineView()
    browser.setUrl( qurl )
    i = self.tabs.addTab(browser, label)
    self.tabs.setCurrentIndex(i)
    # More difficult! We only want to update the url when it's from the
    # correct tab
    browser.urlChanged.connect( lambda qurl, browser=browser:
      self.update_urlbar(qurl, browser) )
    browser.loadFinished.connect( lambda _, i=i, browser=browser:
      self.tabs.setTabText(i, browser.page().title()) )

```

As you can see, we set a `lambda` as the slot for the `urlChanged` signal, accepting the `qurl` parameter that is sent by this signal. We add the recently created `browser` object to pass into the `update_urlbar` function.
Now, whenever the `urlChanged` signal fires `update_urlbar` will receive both the new URL and the browser it came from. In the slot method we can then check to ensure that the source of the signal matches the currently visible browser — if not, we simply discard the signal.
python ```
  def update_urlbar(self, q, browser=None):
    if browser != self.tabs.currentWidget():
      # If this signal is not from the current tab, ignore
      return
    if q.scheme() == 'https':
      # Secure padlock icon
      self.httpsicon.setPixmap( QPixmap( os.path.join('icons','lock-ssl.png') ) )
    else:
      # Insecure padlock icon
      self.httpsicon.setPixmap( QPixmap( os.path.join('icons','lock-nossl.png') ) )
    self.urlbar.setText( q.toString() )
    self.urlbar.setCursorPosition(0)

```

This same technique is used to handle all other signals which we can receive from web views, and which need to be redirected. This is a good pattern to learn and practice as it gives you a huge amount of flexibility when building PyQt5 applications.
## What's next?
Feel free to continue experimenting with the browser, adding features and tweaking things to your liking. Some ideas you might want to consider trying out --
  * Add support for Bookmarks/Favorites, either in the menus or as a "Bookmarks Bar"
  * Add a download manager using [threads](https://www.pythonguis.com/courses/concurrent-execution/) to download in the background and display progress
  * Customize how links are opened, see our [quick tip on opening links in new windows](https://www.pythonguis.com/qwebengineview-open-links-new-window/)
  * Implement real SSL verification (check the certificate)


Remember that the [full source code](https://github.com/learnpyqt/15-minute-apps/tree/master/browser_tabbed) for Mozzarella Ashbadger is available.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Tabbed web browsing** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/examples/python-tabbed-web-browser/Python books) on the subject. 
**Tabbed web browsing** was published in [examples](https://www.pythonguis.com/examples/) on April 08, 2018 (updated April 04, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[python](https://www.pythonguis.com/topics/python/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [qt](https://www.pythonguis.com/topics/qt/) [browser](https://www.pythonguis.com/topics/browser/) [apps](https://www.pythonguis.com/topics/apps/) [desktop](https://www.pythonguis.com/topics/desktop/) [gui](https://www.pythonguis.com/topics/gui/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
