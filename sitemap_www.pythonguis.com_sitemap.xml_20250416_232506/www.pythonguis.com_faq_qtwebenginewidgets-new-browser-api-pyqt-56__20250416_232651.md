# Content from: https://www.pythonguis.com/faq/qtwebenginewidgets-new-browser-api-pyqt-56/

[](https://www.pythonguis.com/faq/qtwebenginewidgets-new-browser-api-pyqt-56/#menu)
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
# QtWebEngineWidgets, the new browser API in PyQt 5.6
Simplified page model and asynchronous methods
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Jul 14 [ FAQ ](https://www.pythonguis.com/faq/)
With the release of Qt 5.5 the Qt WebKit API was deprecated and replaced with the new `QtWebEngine` API, based on Chromium. The WebKit API was subsequently removed from Qt entirely with the [release of Qt 5.6](https://wiki.qt.io/New_Features_in_Qt_5.6) in mid-2016.
The change to use Chromium for web widgets within Qt [was motivated by](http://blog.qt.io/blog/2013/09/12/introducing-the-qt-webengine/) improved cross-platform support, multimedia and HTML5 features, together with a rapid development pace offering better future proofing. The benefits were considered enough to warrant breaking API changes in a non-major release, rather than waiting for Qt 6.
The API for `QtWebEngineWidgets` was designed to make it — more or less — a drop-in replacement for it's predecessor, and this is also the case when using the API from PyQt5. However, the opportunity was taken to make a number of improvements to the API, which require changes to existing code. These changes include simplification of the page model and the conversion of HTML export and printing methods to be asynchronous. This is _good news_ since it prevents either of these operations from blocking your application execution.
This course gives a quick walkthrough of the changes, including working examples with the new API.
## Goodbye .mainFrame()
In the WebKit based API, each page was represented by a `QWebPage` object, which in turn contained _frames_ of content. This reflects the origin of this API during a time when HTML _frames_ were thing, used to break a document down into grid of constituent parts, each loaded as a separate source. The `.mainFrame()` of the page refers to the browser window, as a `QWebFrame` object which can itself contain multiple child frames, or HTML content.
To get the HTML content of the page we would previously have to access it via —
python ```
browser.page().mainFrame().toHtml()

```

With the use of frames in web pages falling out favour, and being deprecated in HTML5, this API becomes an unnecessary complication. Now the call to `.page()` returns a `QWebEnginePage` object, which directly contains the HTML itself.
1:1 Coaching & Tutoring for your Python GUIs project
[![Martin Fitzpatrick Python GUIs Coaching & Training](https://www.pythonguis.com/static/theme/images/products/coaching.jpg)](https://calendly.com/martinfitzpatrick/60min-python-guis-coaching)
[60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/) [Book Now](https://www.pythonguis.com/live/)
1:1 Python GUIs Coaching & Training
**Comprehensive code review** • **Bugfixes** & improvements • **Maintainability** advice and **architecture** improvements • **Design and usability** assessment • Suggestions and tips to **expand your knowledge** • **Packaging and distribution** help for Windows, Mac & Linux • [Find out more.](https://www.pythonguis.com/live)
python ```
browser.page().toHtml()

```

If you try to use the above to actually get the HTML content of a page, it won't work. That's because this method has been changed to use an asynchronous callback. See the next section.
## Asynchronous toHtml
Generating the HTML for a page can take some time, particularly on large pages. Not a _really_ long time, but enough to make your application stutter. To avoid this, the `.toHtml()` method on `QWebEnginePage` has been converted to be _asynchronous_. To receive a copy of the HTML content you call `.toHtml()` as before, but now pass in a callback function to receive the HTML once the generation has completed. The initial completes immediately and so does not block your application execution.
The following example shows a save method using a small callback function `write_html_to_file` to complete the process of writing the page HTML to the selected file location.
python ```
def save_file(self):
  filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                       "Hypertext Markup Language (*.htm *html);;"
                       "All files (*.*)")
  if filename:
    def write_html_to_file(html):
      with open(filename, 'w') as f:
        f.write(html)
    self.browser.page().toHtml(write_html_to_file)

```

The `write_html_to_file` method will be called whenever the generation of the HTML has completed, assuming there are no errors in doing so. You can pass any Python function/method in as a callback.
## Asynchronous Printing & Print to PDF
In the previous API printing was also handled from the `QWebFrame` object, via the print slot (`print_` in PyQt due to print being a keyword in Python 2.7). This too has been moved to the `QWebEnginePage` object, now as a normal method rather than a slot.
Because PyQt5 is Python 3 only, the method is now named `print()`, without a trailing underscore.
To print a page we can call `.print()` on any `QWebEnginePage` object, passing in an instance of `QPrinter` to print to, and a callback function to call once complete.
The `QPrinter` instance can be configured using a `QPrintDialog` as normal, however you must ensure the printer object is not cleaned up/removed before the end of the printing process. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
While you can generate a new `QPrinter` object from a call to `QPrintDialog`, this will be cleared up by Qt even if you hold onto a Python reference, leading to a segmentation fault. The simplest solution is just to create a `QPrinter` object at the start of your application and re-use it.
First create an instance of QPrinter on your main window during initialization, e.g.
python ```
self.printer = QPrinter()

```

Then you can use the following to show a print dialog and (optionally) print a page:
python ```
def print_page(self):
  dlg = QPrintDialog(self.printer)
  if dlg.exec_():
    self.browser.page().print(self.printer, self.print_completed)
def print_completed(self, success):
  pass  # Do something in here, maybe update the status bar?

```

The callback is required, but your not required to do anything in it. It receives a `bool` value indicating the success/failure of the printing process.
## Print to PDF
The new `QWebEnginePage` API also provides a little bonus in the form of PDF printing from HTML pages via `printToPdf`. This method accepts either a `str` filename to write the resulting PDF to, or a callback function to receive the rendered PDF as a `QByteArray`.
python ```
browser.page().printToPdf(path) # render to PDF and save to path

```

Existing files will be overwritten when writing to file. While this operation is is asynchronous there is no callback. Instead the notification of success/failure comes via a signal on the page object `pdfPrintingFinished`, which receives the file path string and a success `bool`. This signal is not triggered when using a callback:
python ```
def rendered_pdf_callback(b):
  print(b)
browser.page().printToPdf(rendered_pdf_callback) # render to PDF and send as `QByteArray` to `rendered_pdf_callback`

```

Paper formats and margins can all be configured by passing additional parameters.
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**QtWebEngineWidgets, the new browser API in PyQt 5.6** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/qtwebenginewidgets-new-browser-api-pyqt-56/Python books) on the subject. 
**QtWebEngineWidgets, the new browser API in PyQt 5.6** was published in [faq](https://www.pythonguis.com/faq/) on May 27, 2018 (updated July 14, 2021) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[web](https://www.pythonguis.com/topics/web/) [chromium](https://www.pythonguis.com/topics/chromium/) [upgrade](https://www.pythonguis.com/topics/upgrade/) [browser](https://www.pythonguis.com/topics/browser/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [python](https://www.pythonguis.com/topics/python/)
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
