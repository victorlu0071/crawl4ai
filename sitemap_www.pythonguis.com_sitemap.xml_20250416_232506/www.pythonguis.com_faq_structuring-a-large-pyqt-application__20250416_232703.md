# Content from: https://www.pythonguis.com/faq/structuring-a-large-pyqt-application/

[](https://www.pythonguis.com/faq/structuring-a-large-pyqt-application/#menu)
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
# Structuring a Large PyQt Application
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
tcarson4344 | 2020-05-25 20:27:19 UTC | #1
I am an NVH Engineer and I am learning Python. Historically I have used Labview and other commercial software in my work life. I like that there is so much work that has been done developing code for NVH analysis in python.
I would like to make open-source GUI applications that can harness a lot of the work that has been done. The first thing I want to tackle is a Time Data Recorder application. functionally it would operate similarly to this [commercial product](https://www.youtube.com/watch?v=3hrG8IlioIM).
HDF5 - Data Storage pyacq - Possible acquisition framework GUI - Develop in PySide2
I was thinking about something like this for gui skeleton ![image|690x474, 50%](https://www.pythonguis.com/static/faq/forum/structuring-a-large-pyqt-application/9NXDM02bCS8ekjXAJpuu2aGdWp.png)
and this for the TDR App inside it ![image|690x472, 50%](https://www.pythonguis.com/static/faq/forum/structuring-a-large-pyqt-application/jrnQ2XRRkZ9FloCUxVqnt22qln9.png)
I am looking for some help with directory and software structure. I have the main layout working in code (buttons don't do anything yet). Any thought would be helpful 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Timm
Eolinwen | 2020-05-26 14:45:35 UTC | #2
Hi tcarson4344
Indeed, it is a large PyQt application that you plan to design. :wink:
Personally, I can give a part of answer because, even I have planned to make a big (for me) application in another domain than you, I have studied a bit the question.
On the left part, you'll need a QListWidget and on the right part a QStackedWidget and probably a QStackedLayout. This latter is not sure. A bit like this.
[url=http://pix.toile-libre.org/?img=1590507878.png]![](https://www.pythonguis.com/static/faq/forum/structuring-a-large-pyqt-application/yAJJVnHOsmNDtPd6OUQkwLP3MPT.png)[/url]
About the structure, usually I used this one: (after it is done for Linux only) I don't know for Macos and Windwos.
For the root package (i.e the folder of the application herself), I introduce a start_app file (which run the application) and share files in different folders according to their membership ui, translations, window etc ... 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
This thread on [Stackoverflow](https://stackoverflow.com/questions/53899209/load-whole-ui-file-in-an-frame-widget-of-another-ui-file) will be helpful for you. You have even a project structure proposed.
I hope that will help you.
tcarson4344 | 2020-05-26 22:42:46 UTC | #3
@Eolinwen,
Thank you this is helpful. Does something like this seem reasonable?
python ```
├── main.py
├── ui_main.py
├── Modules
│  ├── Time_Data_Recorder
│  │  ├── TDR.py
│  │  ├── ui_TDR.py
│  ├── Spectral_Testing
│  └── Other_Modules
└── Third_Party_libraries
  ├── HDF5
  ├── Pyacq
  ├── Plotting
  └── Other

```

Eolinwen | 2020-05-27 14:58:20 UTC | #4
Hum. Like it is a large App, and with the result that you want, I 'll create a sub-folder (like Modules folder) for ui files at least. You should cut your code if you don't want to be overflow. And if you add views.....
I suggest that you 'll take a look at the structure of [Openshot-qt](https://github.com/OpenShot/openshot-qt). Even it is not in the same domain, it is a large project (Video Editor) and with the Stackoverflow structure they will correspond more at that you want to get.
And use uic for loading ui files.........but be careful for memory foot.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Structuring a Large PyQt Application** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/structuring-a-large-pyqt-application/Python books) on the subject. 
**Structuring a Large PyQt Application** was published in [faq](https://www.pythonguis.com/faq/) on May 25, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyside](https://www.pythonguis.com/topics/pyside/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
