# Content from: https://www.pythonguis.com/blog/macos-mojave-dark-mode-support-pyqt5122/

[](https://www.pythonguis.com/blog/macos-mojave-dark-mode-support-pyqt5122/#menu)
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
# MacOS Mojave Dark Mode Support in PyQt 5.12.2
Ensuring your apps follow the desktop style
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 13 [ blog ](https://www.pythonguis.com/blog/)
MacOS Mojave, released in September of last year, introduced a user-toggleable "Dark Mode". This enables a system-wide dark color scheme, intended to make things easier on your eyes at night, or less distracting when working with content. The mode was supported by all built-in Mac apps on release, but 3rd party applications (including those developed with PyQt) were left looking a bit out of place.
The support for Dark Mode in Qt [was targeted for 5.12](https://blog.qt.io/blog/2018/11/08/qt-macos-10-14-mojave/) which landed in December 2018, with the first Python support in [PyQt 5.12 released February 2019](https://pypi.org/project/PyQt5/5.12/).
Early implementations had a few issues (see below) but as of PyQt 5.12.2 it's looking great. The pictures below show the same example app (just a random assortment of widgets) under Dark Mode and (default) Light Mode on MacOS Mojave.
python ```
pip3 install pyqt5==5.12.2

```

If you're on PyQt 5.12.2 or over Dark Mode is **automatic**. If your computer is in Dark Mode, your Qt apps should appear in the appropriate color scheme.
![Example app on MacOS Mojave in Light Mode — PyQt 5.12.2](https://www.pythonguis.com/static/blog/macos-mojave-dark-mode-support-pyqt5122/Screenshot_2019-05-30_at_20.57.47.png) _Example app on MacOS Mojave in Light Mode — PyQt 5.12.2_
![Example app on MacOS Mojave in Dark Mode —&nbsp;PyQt 5.12.2](https://www.pythonguis.com/static/blog/macos-mojave-dark-mode-support-pyqt5122/Screenshot_2019-05-30_at_20.57.08.png) _Example app on MacOS Mojave in Dark Mode — PyQt 5.12.2_
## Issues on earlier versions
While PyQt 5.2.12 applications look great in Dark Mode, earlier versions have had a few issues. Below are a few screenshots of the same example app taken across earlier releases. If you're releasing your PyQt 5 apps to MacOS you might want to take a look at how it handles.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Downgrading to PyQt 5.12 produces the UI below — more or less fine, but with a missing color on the spin-wheel nubbin. It doesn't effect the functioning of the app, just looks a bit less nice.
python ```
pip3 install pyqt5==5.12

```

![Example App in Dark Mode —&nbsp;PyQt 5.12, showing tiny style error](https://www.pythonguis.com/static/blog/macos-mojave-dark-mode-support-pyqt5122/Screenshot_2019-05-30_at_21.23.18.png) _Example App in Dark Mode — PyQt 5.12, showing tiny style error_
Downgrading further to PyQt 5.10 produces this disaster. Strangely the wheel is now shaded properly, but the text is white-on-white.
python ```
  pip3 install pyqt5==5.10

```

![Example App in Dark Mode —&nbsp;PyQt 5.10, it ain't pretty.](https://www.pythonguis.com/static/blog/macos-mojave-dark-mode-support-pyqt5122/Screenshot_2019-05-30_at_21.27.36.png) _Example App in Dark Mode — PyQt 5.10, it ain't pretty._
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Weirdly, although PyQt 5.11 looks just as bad, 5.9 looks slightly better (as in potentially usable).
python ```
  pip3 install pyqt5==5.9

```

![Example App in Dark Mode —&nbsp;PyQt 5.9, at least you can see some of the text](https://www.pythonguis.com/static/blog/macos-mojave-dark-mode-support-pyqt5122/Screenshot_2019-05-30_at_21.33.19.png) _Example App in Dark Mode — PyQt 5.9, at least you can see some of the text_
The bottom line is: if you're targeting MacOS with your applications and using < PyQt5.12.2 then now would be a very good time to upgrade and ensure your app looks as great as it can under Mojave Dark Mode.
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**MacOS Mojave Dark Mode Support in PyQt 5.12.2** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/blog/macos-mojave-dark-mode-support-pyqt5122/Python books) on the subject. 
**MacOS Mojave Dark Mode Support in PyQt 5.12.2** was published in [blog](https://www.pythonguis.com/blog/) on May 30, 2019 (updated September 13, 2023) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qt](https://www.pythonguis.com/topics/qt/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [python](https://www.pythonguis.com/topics/python/)
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
