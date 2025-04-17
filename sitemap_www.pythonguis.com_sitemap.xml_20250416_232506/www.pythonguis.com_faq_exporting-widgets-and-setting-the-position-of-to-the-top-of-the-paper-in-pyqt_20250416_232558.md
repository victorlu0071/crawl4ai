# Content from: https://www.pythonguis.com/faq/exporting-widgets-and-setting-the-position-of-to-the-top-of-the-paper-in-pyqt5/

[](https://www.pythonguis.com/faq/exporting-widgets-and-setting-the-position-of-to-the-top-of-the-paper-in-pyqt5/#menu)
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
# Exporting widgets and setting the position of to the top of the paper in pyqt5
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
meshelleva4815 | 2020-07-05 14:19:36 UTC | #1
I have a set of student information which I kept inside a QWidget. I created the following method to render() the QWidget and convert the QWidget content to pdf. Include is the output, positioned at the center ![15939585535225667475434502721475|375x500](https://www.pythonguis.com/static/faq/forum/exporting-widgets-and-setting-the-position-of-to-the-top-of-the-paper-in-pyqt5/hwIBKdtF2UPyDzuBJueIwYGWSfz.jpeg)
python ```
def print_widget(self, widget, filename):
  printer = QPrinter(QPrinter.HighResolution)
  printer.setOutputFormat(QPrinter.PdfFormat)
  printer.setOutputFileName(filename)
  painter = QPrinter(printer)
  xscale = printer.pageRect().width() * 1.0 / widget.width()
   yscale = printer.pageRect().height * 1.0 / widget.height()
  scale = min(xscale, yscale)
  painter.translate(printer.paperRect().center())#set as center here
  painter.scale(scale, scale)
  painter.translate(-widget.width()/2, -widget.height()/2)
  widget.render(painter)
  painter.end()
def pdfexport(self):
  fn, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf);;All Files()")
  if fn:
    if QFileInfo(fn).suffix() == "":
      fn += ".pdf"
    self.print_widget(self.student_profiler, fn)

```

It worked well but I want it to position the widget at the top of the paper not at the centre. Thanks in anticipations
meshelleva4815 | 2020-07-07 19:28:32 UTC | #2
Hello hey, please someone should bail me out on this question, really need your help
martin | 2020-07-07 21:15:39 UTC | #3
Hey @meshelleva4815, sorry I missed this before. The centering is happening here, we can step through what you're currently doing and see how to modify it.
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
python ```
painter.translate(printer.paperRect().center())  #1
painter.scale(scale, scale) # 2
painter.translate(-widget.width()/2, -widget.height()/2) # 3

```

  1. Translate coordinates to the center of the page, in both x & y
  2. Scale to fit to the page
  3. Translate _back_ by half the width & height.


The first step would put the _top left_ of the widget in the middle of the paper. So, then shifting back by half height, half width, puts the middle of the widget, in the middle of the paper.
To translate just the X position we can _not_ translate the y to the middle of the page. We'll end up with the top left of the widget being at the top of the page, in the middle (horizontally). The next translate can then just move the widget back horizontally to align on the middle.
I think the following should do it ...
python ```
xshift = printer.paperRect().width() / 2
painter.translate(xshift, 0)  #1
painter.scale(scale, scale) # 2
painter.translate(-widget.width()/2, 0) # 3

```

  1. Translate to width/2 (the horizontal center), no change on vertical.
  2. Scale
  3. Translate back the width of the widget / 2, nothing on y.


Let me know if that works, can't test just now but will have a look again tomorrow if not.
meshelleva4815 | 2020-07-08 23:08:18 UTC | #4
That's a relief, it worked just exactly as I wanted it. You doing a great with this time help you give boss. I hope to be like you some days boss. :hugs:
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Exporting widgets and setting the position of to the top of the paper in pyqt5** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/exporting-widgets-and-setting-the-position-of-to-the-top-of-the-paper-in-pyqt5/Python books) on the subject. 
**Exporting widgets and setting the position of to the top of the paper in pyqt5** was published in [faq](https://www.pythonguis.com/faq/) on July 05, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
