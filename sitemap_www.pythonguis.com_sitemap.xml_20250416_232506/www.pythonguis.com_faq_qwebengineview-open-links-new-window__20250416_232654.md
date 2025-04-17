# Content from: https://www.pythonguis.com/faq/qwebengineview-open-links-new-window/

[](https://www.pythonguis.com/faq/qwebengineview-open-links-new-window/#menu)
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
# Opening links in a new window with QWebEngineView
Redirect links to a separate floating browser window
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ FAQ ](https://www.pythonguis.com/faq/)
It's quite a common practice to use `QWebEngineView` as a documentation (or document) browser in PyQt5 applications as it allows the documentation to be created using familiar tools. You can build HTML documentation and bundle it with your application (or host them remotely) then allow your users to browse them within the app.
However, this raises an issue when the document contains links to external resources -- how should these links be handled? It's a weird user experience if your users, through clicking a series of links, can end up on Google or Facebook _inside_ your application. One way to avoid this is to enforce opening of certain links in external windows or browsers, ensuring your documentation browser remains just that.
In this quick tutorial we'll look at how to implement custom link handling in your Qt browser and use this to redirect clicked links to different windows or the user's desktop browser.
The skeleton web browser code is shown below. We'll modify this to add the _open in new window_ behavior.
  * PyQt5
  * PySide2


python ```
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os
import sys

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.browser = QWebEngineView()
    self.browser.setUrl(QUrl("https://www.mfitzp.com"))
    self.setCentralWidget(self.browser)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

python ```
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView
import os
import sys

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.browser = QWebEngineView()
    self.browser.setUrl(QUrl("https://www.mfitzp.com"))
    self.setCentralWidget(self.browser)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

This creates our basic browser window and navigates to the LearnPyQt homepage. All links will open within the same browser window (normal browser behavior).
![The basic browser](https://www.pythonguis.com/static/faq/qwebengineview-open-links-new-window/browser.png) _The basic browser window._
## Popping up a new window for each link
To override the default navigation behavior we need to create a customized `QWebEnginePage` class. This is the Qt class which handles viewing (and editing) of web documents, such as web pages within the `QWebEngineView`.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
By creating a custom `QWebEnginePage` class we are able to intercept the `.acceptNavigationRequest` signal and implement custom behavior. For example, we can decline links to block navigation, alter the links to navigate somewhere else, or (as we're doing here) open up custom viewers. In our specific case we will both _decline_ the default behavior, by returning `False`and implement our own, by opening a new window.
For our new windows, we create a custom web engine view (the same type we have in the main window), set the URL and then display the window. Note that we need to keep a reference to the created window (in the `external_windows` list) so it isn’t destroyed on exiting this method.
For everything else, we pass through to the handler on the parent class with `super().acceptNavigationRequest()`.
python ```
from PyQt5.QtWebEngineWidgets import QWebEnginePage
class CustomWebEnginePage(QWebEnginePage):
  """ Custom WebEnginePage to customize how we handle link navigation """
  # Store external windows.
  external_windows = []
  def acceptNavigationRequest(self, url, _type, isMainFrame):
    if _type == QWebEnginePage.NavigationTypeLinkClicked:
      w = QWebEngineView()
      w.setUrl(url)
      w.show()
      # Keep reference to external window, so it isn't cleared up.
      self.external_windows.append(w)
      return False
    return super().acceptNavigationRequest(url, _type, isMainFrame)

```

To use our custom page class we need to set it on the browser with `.setPage()`. After this, any navigation is sent through the custom page instance and our `acceptNavigationRequest` handler.
python ```
    self.browser = QWebEngineView()
    self.browser.setPage(CustomWebEnginePage(self))
    self.browser.setUrl(QUrl("http://google.com"))

```

The full working example is shown below.
  * PyQt5
  * PySide2


python ```
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
import os
import sys

class CustomWebEnginePage(QWebEnginePage):
  """ Custom WebEnginePage to customize how we handle link navigation """
  # Store external windows.
  external_windows = []
  def acceptNavigationRequest(self, url, _type, isMainFrame):
    if _type == QWebEnginePage.NavigationTypeLinkClicked:
      w = QWebEngineView()
      w.setUrl(url)
      w.show()
      # Keep reference to external window, so it isn't cleared up.
      self.external_windows.append(w)
      return False
    return super().acceptNavigationRequest(url, _type, isMainFrame)

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.browser = QWebEngineView()
    self.browser.setPage(CustomWebEnginePage(self))
    self.browser.setUrl(QUrl("https://www.mfitzp.com"))
    self.setCentralWidget(self.browser)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

python ```
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
import os
import sys

class CustomWebEnginePage(QWebEnginePage):
  """ Custom WebEnginePage to customize how we handle link navigation """
  # Store external windows.
  external_windows = []
  def acceptNavigationRequest(self, url, _type, isMainFrame):
    if _type == QWebEnginePage.NavigationTypeLinkClicked:
      w = QWebEngineView()
      w.setUrl(url)
      w.show()
      # Keep reference to external window, so it isn't cleared up.
      self.external_windows.append(w)
      return False
    return super().acceptNavigationRequest(url, _type, isMainFrame)

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.browser = QWebEngineView()
    self.browser.setPage(CustomWebEnginePage(self))
    self.browser.setUrl(QUrl("https://www.mfitzp.com"))
    self.setCentralWidget(self.browser)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

If you run this example and click on a link in the page, a new window will be opened for every link you click. You can continue to navigate within those external windows as normal -- they use the standard `QWebEnginePage` class, so don't have our _open in new window_ behavior.
![Links are opened in a separate window](https://www.pythonguis.com/static/faq/qwebengineview-open-links-new-window/browser-new-window.png) _Links are opened in a new window._
## Conditionally popping up a new window
Sometimes you only want "external" links to be popped up into a separate window -- navigation within your documentation should stay within the documentation browser window, and only external links (not from your documentation) popped up into a separate window.
Since we have access to the URL being navigated this is pretty straightforward. We can just compare that URL to some pattern (here we're using the hostname via `url.host()`), and choose to either pop a new window, or pass it to the default handler. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
python ```
class CustomWebEnginePage(QWebEnginePage):
  """ Custom WebEnginePage to customize how we handle link navigation """
  # Store external windows.
  external_windows = []
  def acceptNavigationRequest(self, url, _type, isMainFrame):
    if (_type == QWebEnginePage.NavigationTypeLinkClicked and
      url.host() != 'www.mfitzp.com'):
      # Pop up external links into a new window.
      w = QWebEngineView()
      w.setUrl(url)
      w.show()
      # Keep reference to external window, so it isn't cleared up.
      self.external_windows.append(w)
      return False
    return super().acceptNavigationRequest(url, _type, isMainFrame)

```

Navigating around the LearnPyQt site now stays within the main browser, but external links (such as to the forum) are popped out into a separate window.
![External window popped up for external links](https://www.pythonguis.com/static/faq/qwebengineview-open-links-new-window/browser-conditional-new-window.png) _The external window is popped up for external links only._
## Reusing an external window
In this first example we're creating a new window _for every link_ , rather than creating a new window if none exists and then sending all subsequent link clicks to that same window. To get this second behavior we just need to hold a single reference to the external window and check if it exists before creating a new one.
python ```
class WebEnginePage(QWebEnginePage):
  # Store second window.
  external_window = None
  def acceptNavigationRequest(self, url, _type, isMainFrame):
    print(url, _type, isMainFrame)
    if _type == QWebEnginePage.NavigationTypeLinkClicked:
      if not self.external_window:
        self.external_window = QWebEngineView()
      self.external_window.setUrl(url)
      self.external_window.show()
      return False
    return super().acceptNavigationRequest(url, _type, isMainFrame)

```

Putting this into our example gives us the following complete example.
  * PyQt5
  * PySide2


python ```
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
import sys

class CustomWebEnginePage(QWebEnginePage):
  # Store second window.
  external_window = None
  def acceptNavigationRequest(self, url, _type, isMainFrame):
    print(url, _type, isMainFrame)
    if _type == QWebEnginePage.NavigationTypeLinkClicked:
      if not self.external_window:
        self.external_window = QWebEngineView()
      self.external_window.setUrl(url)
      self.external_window.show()
      return False
    return super().acceptNavigationRequest(url, _type, isMainFrame)

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.browser = QWebEngineView()
    self.browser.setPage(CustomWebEnginePage(self))
    self.browser.setUrl(QUrl("https://www.mfitzp.com"))
    self.setCentralWidget(self.browser)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

python ```
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
import sys

class CustomWebEnginePage(QWebEnginePage):
  # Store second window.
  external_window = None
  def acceptNavigationRequest(self, url, _type, isMainFrame):
    print(url, _type, isMainFrame)
    if _type == QWebEnginePage.NavigationTypeLinkClicked:
      if not self.external_window:
        self.external_window = QWebEngineView()
      self.external_window.setUrl(url)
      self.external_window.show()
      return False
    return super().acceptNavigationRequest(url, _type, isMainFrame)

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.browser = QWebEngineView()
    self.browser.setPage(CustomWebEnginePage(self))
    self.browser.setUrl(QUrl("https://www.mfitzp.com"))
    self.setCentralWidget(self.browser)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

When clicking on a link in the browser window a new window is created. You can browse in that window as normal, but if you click a new link in the parent window, the current page will be replaced with that link.
## Opening links in the user's default browser
You might also want to consider popping up external links in the users default browser. This allows them to bookmark the links, or browse as normally, rather than in the restricted browser view your app provides.
For this we don't need to create a window, we can just send the url to the system default handler. This is accomplished by passing the url to the `QDesktopServices.openUrl()` method. The full working example is shown below.
  * PyQt5
  * PySide2


python ```
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtGui import QDesktopServices
import os
import sys

class CustomWebEnginePage(QWebEnginePage):
  """ Custom WebEnginePage to customize how we handle link navigation """
  # Store external windows.
  external_windows = []
  def acceptNavigationRequest(self, url, _type, isMainFrame):
    if (_type == QWebEnginePage.NavigationTypeLinkClicked and
      url.host() != 'www.mfitzp.com'):
      # Send the URL to the system default URL handler.
      QDesktopServices.openUrl(url)
      return False
    return super().acceptNavigationRequest(url, _type, isMainFrame)

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.browser = QWebEngineView()
    self.browser.setPage(CustomWebEnginePage(self))
    self.browser.setUrl(QUrl("https://www.mfitzp.com"))
    self.setCentralWidget(self.browser)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

python ```
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PySide2.QtGui import QDesktopServices
import os
import sys

class CustomWebEnginePage(QWebEnginePage):
  """ Custom WebEnginePage to customize how we handle link navigation """
  # Store external windows.
  external_windows = []
  def acceptNavigationRequest(self, url, _type, isMainFrame):
    if (_type == QWebEnginePage.NavigationTypeLinkClicked and
      url.host() != 'www.mfitzp.com'):
      # Send the URL to the system default URL handler.
      QDesktopServices.openUrl(url)
      return False
    return super().acceptNavigationRequest(url, _type, isMainFrame)

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.browser = QWebEngineView()
    self.browser.setPage(CustomWebEnginePage(self))
    self.browser.setUrl(QUrl("https://www.mfitzp.com"))
    self.setCentralWidget(self.browser)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

If you run this and click on any external links, you'll see them open in your system's default browser window (here showing Chrome).
![Link opened in default browser window](https://www.pythonguis.com/static/faq/qwebengineview-open-links-new-window/browser-conditional-desktop.png)
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Opening links in a new window with QWebEngineView** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/qwebengineview-open-links-new-window/Python books) on the subject. 
**Opening links in a new window with QWebEngineView** was published in [faq](https://www.pythonguis.com/faq/) on November 19, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qwebengineview](https://www.pythonguis.com/topics/qwebengineview/) [window](https://www.pythonguis.com/topics/window/) [web-browser](https://www.pythonguis.com/topics/web-browser/) [qt](https://www.pythonguis.com/topics/qt/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [python](https://www.pythonguis.com/topics/python/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
