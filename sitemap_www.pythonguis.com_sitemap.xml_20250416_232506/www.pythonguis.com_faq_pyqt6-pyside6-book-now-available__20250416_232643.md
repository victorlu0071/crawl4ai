# Content from: https://www.pythonguis.com/faq/pyqt6-pyside6-book-now-available/

[](https://www.pythonguis.com/faq/pyqt6-pyside6-book-now-available/#menu)
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
# PyQt6 & PySide6 Book now available!
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
martin | 2021-04-09 15:18:58 UTC | #1
The [**PyQt6 edition**](https://www.pythonguis.com/pyqt6-book) and [**PySide6 edition**](https://www.pythonguis.com/pyside6-book) of the _Create GUI Applications_ book has just been released! If you have bought the PyQt5 or PySide2 editions of the book **you have access to all versions** , including this update -- just go to your account at <https://account.learnpyqt.com>. Enjoy!
martin | 2021-03-15 08:31:42 UTC | #6
martin | 2021-03-15 08:35:40 UTC | #7
This is a straight conversion of the latest PyQt5 & PySide2 editions of the book, updating code examples and reworking some parts where necessary.
The PyQt6 edition will be following shortly -- there are more incompatibilities with earlier versions, so this needs some additional rewrites. Should be complete by next week.
If you're sticking with PyQt5/PySide2 then good news: there will be one further update of the Qt5 books to add a few additional chapters I've been working on. The PySide6/PyQt6 editions will get these updates too at the same time. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Let me know if you have any questions/feedback!
martin | 2021-03-15 08:35:45 UTC | #8
martin | 2021-03-15 08:35:48 UTC | #9
PedanticHacker | 2021-03-15 10:37:03 UTC | #10
Thanks for publishing the PySide6 edition of your book! I personally can't wait to check out the PyQt6 edition of it. :slight_smile:
Anyway, I have some feedback to give. It applies to the upcoming PyQt6 edition of your book as well.
Would it be possible to use f-strings in the example parts of the code? Like in the PySide6 edition of your book in the `Listing 132. bitmap/paint.py` (page 422) where the very last line of code is `self.setStyleSheet("background-color: %s;" % color)`. That would look much nicer if it were `self.setStyleSheet(f"background-color: {color};")`.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
I know that you're trying to be as much backwards compatible as possible, but this old syntax looks very ugly. I personally believe that f-strings should be used at all times; they make Python code look very beautiful. The f-strings format joined the party in Python 3.6 and I believe that the vast majority of people are already on the 3.6+ boat.
Just my 2 cents. I hope you find any value in this.
Side note: Thanks for all your wonderful work, you are simply amazing!
martin | 2021-03-15 10:57:02 UTC | #11
Hey thanks, really appreciate it! 
As for f-strings -- yes! I much prefer them too. This first release is still using the old style, since it shares the codebase with the final PySide2 editions (which supported 3.4). But they'll now start diverging and I'll be targeting 3.6 as a minimum -- that's the minimum version supported by PySide6/PyQt6 (+PyQt5) anyway, and like you say the majority of people are on it already.
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PyQt6 & PySide6 Book now available!** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyqt6-pyside6-book-now-available/Python books) on the subject. 
**PyQt6 & PySide6 Book now available!** was published in [faq](https://www.pythonguis.com/faq/) on March 15, 2021 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
