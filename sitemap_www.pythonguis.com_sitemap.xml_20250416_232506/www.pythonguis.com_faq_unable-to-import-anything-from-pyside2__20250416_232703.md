# Content from: https://www.pythonguis.com/faq/unable-to-import-anything-from-pyside2/

[](https://www.pythonguis.com/faq/unable-to-import-anything-from-pyside2/#menu)
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
# Unable to import anything from PySide2
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
Virginia | 2020-05-17 19:52:07 UTC | #1
After another website suggested using PySide2 to solve an issue I am having with system tray icons not responding, I installed PySide2. However, I am unable to import anything from it. If I try to import anything from PySide2 I get the following error: 
ImportError: DLL load failed: The specified procedure could not be found. 
I can see from searching the web that this error message sometimes has to do with combinations of packages or other software that needs to be installed, but haven't found a solution. How do I get PySide2 working on my computer? I'm using Windows 10 and have Spyder, PyCharm, and Jupyter Notebook IDE's available.
Thank you!
martin | 2020-05-17 20:06:22 UTC | #2
You can have PySide2 and PyQt5 installed at the same time, the only problem is if you try and import both at the same time. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Are you trying this in Spyder by any chance? Spyder is built with Python & Qt. It can use either PyQt or PySide, but [defaults to PyQt5 if it is installed](https://github.com/spyder-ide/qtpy/blob/master/qtpy/__init__.py). That might mean PySide2 won't work. You can override this by setting a `QT_API` environment variable to e.g. 'pyside2'. 
As before if you can try importing PySide2 in Python run from the command line (you can do it in a shell) you can exclude any problems with the IDEs.
Virginia | 2020-05-18 15:32:30 UTC | #3
Thank you for this information. Do you mean that I can't even have both installed at the same time? I did not try to import both at the same time, but the first time this happened I had just run the same program with importing PyQt5. The error message has now changed to one about needing only one instance of QApplication. From here https://stackoverflow.com/questions/50259785/unable-to-see-app-windows-created-by-pyside2-in-spyder it appears that this problem might apply to other IDE's that use ipykernel - certainly I get the same errors in Jupyter Notebook, which are "# You need one (and only one) QApplication instance per application." and "No module named 'PySide2.QtWidgets'; 'PySide2' is not a package." Thank you also for the link. I can see from that link and from the post on StackOverflow that they recommend using QtPy. I don't entirely understand from the link how I would use QtPy in my System Tray example. I tried to edit my code based on what was in the link, setting the environment variable, but got this error: 'No Qt bindings could be found.' Did I misunderstand what was written on that site? How would I edit the System Tray Icon example code to use PySide2 instead of PyQt5 in Spyder? Or is it not worth trying, since I can do it elsewhere? Thank you again for all your help!
martin | 2020-05-20 14:19:30 UTC | #4
[quote="Virginia, post:3, topic:202"] Do you mean that I can’t even have both installed at the same time? [/quote]
No, I mean the opposite -- it's perfectly fine to have both installed at the same time.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
The issue with Spyder is simply that it _itself_ is built using Qt and defaults to PyQt5. If you try and run PySide2 code inside Spyder, Spyder has already imported PyQt5 so PySide2 won't work.
I wouldn't recommend using the Jupyter notebook for doing GUI development, since it's based around a long-running kernel. Ideally you want to run PyQt apps as a separate process -- either from the command line, or running as a file in an IDE.
This might explain the other issues you had with Spyder actually -- how exactly are you running the code in Spyder? I see it has an internal console https://docs.spyder-ide.org/internalconsole.html but as it says there 
> all the commands entered in the Internal Console are executed in the same process as Spyder’s.
Since this process keeps running after you exit your app it would explain the icon sticking around.
Virginia | 2020-05-21 15:48:03 UTC | #5
I haven't been able to access the internal console. My version of Spyder does not have the same dropdown menu and when I opened Spyder using the --multithread command as instructed it looked exactly the same, and behaved exactly the same. I've also seen on Stack Overflow that Spyder had a console which was discontinued after version 3.1.4: https://stackoverflow.com/questions/45960590/how-to-add-python-console-in-spyder I'm not sure if I'm trying to open it wrong or if it is indeed wrong, since the link you sent me does seem to refer to Spyder 3. I will probably just need to use other IDE's for this kind of thing and use Jupyter or Spyder for other types of programs. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Unable to import anything from PySide2** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/unable-to-import-anything-from-pyside2/Python books) on the subject. 
**Unable to import anything from PySide2** was published in [faq](https://www.pythonguis.com/faq/) on May 17, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
