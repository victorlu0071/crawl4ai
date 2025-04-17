# Content from: https://www.pythonguis.com/faq/pyqt-pyside6-missing-modules/

[](https://www.pythonguis.com/faq/pyqt-pyside6-missing-modules/#menu)
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
# What modules are missing from PySide6 & PyQt6?
The Qt extension modules not yet available in Qt 6.1
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Dec 15 [ FAQ ](https://www.pythonguis.com/faq/)
With the release of Qt6 many people are itching to get started porting their existing applications over to PyQt6 and PySide6. However, as with any new releases there are some rough edges to be aware of.
Reader Boštjan asked:
> I have successfully ported all of my codebase from PyQt5 to PyQt6, thanks to Martin's [tutorial](https://www.pythonguis.com/blog/pyqt6-vs-pyside6/). It helped a lot! I have, however, one area of my codebase that can't be ported to PyQt6. Since Qt6 removed QtMultimedia, PyQt6 / PySide6 as a consequence don't have it anymore. Do you have any news on whether QtMultimedia is coming back anytime soon, if at all?
Qt6 is still new and as such not _all_ of the Qt modules have been ported yet, and so are not available in PyQt6 or PySide6. If you're using any of these modules you'll want to postpone upgrading to v6 until they are available -- once they're added to Qt6 they will be available in a subsequent release of PyQt6 & PySide6. The good news is the porting has already started, and as of Qt 6.1 the following modules are now available. If you're using an earlier version of PyQt6/PySide6, upgrade now!
  * Active Qt
  * Qt Charts
  * Qt Quick Dialogs (File dialog)
  * Qt ScXML
  * Qt Virtual Keyboard


For the following modules you'll need to wait for Qt 6.2.
  * Qt Bluetooth
  * Qt Data Visualization
  * Qt Lottie Animation
  * **Qt Multimedia**
  * Qt NFC
  * Qt Positioning
  * Qt Quick Dialogs: Folder, Message Box
  * Qt Remote Objects
  * Qt Sensors
  * Qt SerialBus
  * Qt SerialPort
  * Qt WebChannel
  * **Qt WebEngine**
  * Qt WebSockets
  * Qt WebView


Qt 6.2 is scheduled for release in September 2021.
For Python applications built with Qt the two in bold are likely to be the biggest issues. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
## What can I do instead?
> I was using QtMultimedia's QSound() class to play WAV sound files by using its play() method. What do you guys propose I use now to play WAV sound files? Is there something similar to QtMultimedia.QSound() in PyQt6 / PySide6? If it is, I can't find it. If not, I need something that is cross-platform (Windows, Linux, Mac) and simple to implement.
If you're using _Qt Multimedia_ to play sounds in your application you _could_ switch over to the Python library `playsound` instead. This is across-platform single-function library which will play sounds for you. But for anything else you're going to want to wait for the Qt 6.2 update: integrating anything more complicated with your Qt app is going to require much more work than it's really worth. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
## Is it time to upgrade?
Whether or not it's time to upgrade is entirely dependent on your project. If you're using modules that aren't available, you _can't_ upgrade yet. If you're just starting out learning Python GUI programming you may prefer to stick with PyQt5/PySide2 for the time being -- there are more examples available and while the differences are minor anything not working is confusing when learning. Anything you learn using PyQt5/PySide2 will carry over when you _do_ choose to upgrade to Qt6.
If you like to be on the bleeding edge and want to get started with Python & Qt6, the [PyQt6](https://www.pythonguis.com/pyqt6-book/) and [PySide6](https://www.pythonguis.com/pyside6-book/) editions of my books are available with all code examples updated for the new version.
1:1 Coaching & Tutoring for your Python GUIs project
[![Martin Fitzpatrick Python GUIs Coaching & Training](https://www.pythonguis.com/static/theme/images/products/coaching.jpg)](https://calendly.com/martinfitzpatrick/60min-python-guis-coaching)
[60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/) [Book Now](https://www.pythonguis.com/live/)
1:1 Python GUIs Coaching & Training
**Comprehensive code review** • **Bugfixes** & improvements • **Maintainability** advice and **architecture** improvements • **Design and usability** assessment • Suggestions and tips to **expand your knowledge** • **Packaging and distribution** help for Windows, Mac & Linux • [Find out more.](https://www.pythonguis.com/live)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**What modules are missing from PySide6 & PyQt6?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyqt-pyside6-missing-modules/Python books) on the subject. 
**What modules are missing from PySide6 & PyQt6?** was published in [faq](https://www.pythonguis.com/faq/) on March 15, 2021 (updated December 15, 2021) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [qt](https://www.pythonguis.com/topics/qt/) [qt6](https://www.pythonguis.com/topics/qt6/) [python](https://www.pythonguis.com/topics/python/)
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
