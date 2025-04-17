# Content from: https://www.pythonguis.com/faq/what-replaces-pyqt5-qtmultimedia-pyside2-qtmultimedia-in-pyqt6-pyside6-if-anything/

[](https://www.pythonguis.com/faq/what-replaces-pyqt5-qtmultimedia-pyside2-qtmultimedia-in-pyqt6-pyside6-if-anything/#menu)
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
# What replaces PyQt5.QtMultimedia / PySide2.QtMultimedia in PyQt6 / PySide6, if anything?
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
PedanticHacker | 2021-03-15 11:40:35 UTC | #1
Hello there! :slight_smile:
I have successfully ported all of my codebase from PyQt5 to PyQt6, thanks to @martin and his [blog post](https://www.pythonguis.com/blog/pyqt6-vs-pyside6/). It helped a lot!
I have, however, one area of my codebase that can't be ported to PyQt6. Since Qt6 removed QtMultimedia, PyQt6 / PySide6 as a consequence don't have it anymore.
I was using QtMultimedia's QSound() class to play WAV sound files by using its play() method.
What do you guys propose I use now to play WAV sound files? Is there something similar to QtMultimedia.QSound() in PyQt6 / PySide6? If it is, I can't find it. If not, I need something that is cross-platform (Windows, Linux, Mac) and simple to implement.
Also, do you have any news on whether QtMultimedia is coming back anytime soon, if at all? 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Thanks in advance for your answer and stay safe!
PedanticHacker | 2021-03-16 09:02:32 UTC | #2
I forgot to add that I tried to use QtMultimedia from PyQt5 in the event loop of PyQt6, but that doesn't work.
PedanticHacker | 2021-04-07 14:22:13 UTC | #3
After browsing for an answer on the Interwebs, I found out that QtMultimedia is planned to be added back to Qt in version 6.2 (and then, of course, to new versions of PyQt6 / PySide6). So that's good news! Someone on some forum (forgot on which) said that Qt 6.2 is planned to be released around September 2021. We'll just have to wait, I guess.
Anyway, Qt 6.2 (and consequently new versions of PyQt6 / PySide6) is gonna give us these toys: _Qt Bluetooth_ Qt Data Visualization _Qt Lottie Animation_ **Qt Multimedia** _Qt NFC_ Qt Positioning _Qt Quick Dialogs: Folder, Message Box_ Qt Remote Objects _Qt Sensors_ Qt SerialBus _Qt SerialPort_ Qt WebChannel _Qt WebEngine_ Qt WebSockets * Qt WebView
However, prior to version 6.2, Qt 6.1 will not be so generous and will not be such toy heaven; we'll only get these toys: _Active Qt_ Qt Charts _Qt Quick Dialogs (File dialog)_ Qt ScXML _Qt Virtual Keyboard (_ Meh, okay.*)
PedanticHacker | 2021-03-16 22:57:05 UTC | #4
While we wait for those new toys coming in Qt 6.2 and consequently in new versions of PyQt6 / PySide6, the [playsound](https://pypi.org/project/playsound/) project found on PyPI is very good. I just tried it and it works as good as QSound() from QtMultimedia.
Install playsound with the `pip install playsound` command and then import its playsound function in your Python script with `from playsound import playsound`. It's important that you don't forget to pass the `block` argument to the playsound function and set it to `False`; that way the sound will play asynchronously.
python ```
from playsound import playsound
playsound("path/to/my/sound/file.wav", block=False)

```

:slight_smile:
martin | 2021-04-07 14:24:23 UTC | #5 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyside2-book/) _by Martin Fitzpatrick_ — (PySide2 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside2-book/) [Get the book](https://secure.pythonguis.com/01hf778jyaajk5vk1q6824sd44/)
Thanks for looking all this up, really appreciate it!
I hit this same snag when trying to migrate over the browser example from the book & had to remove it for the time being. It's a bit of a shame that didn't make it, but a good excuse to refresh the demos a bit.
PedanticHacker | 2021-04-08 10:39:06 UTC | #6
Yeah, too bad `QtMultimedia` didn't make it to `Qt 6.0`. But for the time being, I'm using the `playsound` function from the `playsound` package.
amohgyebigodwin10691 | 2021-04-09 08:08:26 UTC | #7
If ever playsound is not able to play an audio file, you can use soloman. It plays everything.
python ```
pip install soloman

```

and then
python ```
from soloman import Audio

aud = Audio()
aud.play('/path/to/music.mp3')

```

PedanticHacker | 2021-04-09 08:29:37 UTC | #8
Yeah, `soloman` is good, too. But for simple WAV files, `playsound` is okay. 😉
stelaldridge11281 | 2021-05-28 14:52:22 UTC | #9
I upvote for playsound too, it might be helpful there.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**What replaces PyQt5.QtMultimedia / PySide2.QtMultimedia in PyQt6 / PySide6, if anything?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/what-replaces-pyqt5-qtmultimedia-pyside2-qtmultimedia-in-pyqt6-pyside6-if-anything/Python books) on the subject. 
**What replaces PyQt5.QtMultimedia / PySide2.QtMultimedia in PyQt6 / PySide6, if anything?** was published in [faq](https://www.pythonguis.com/faq/) on March 15, 2021 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
