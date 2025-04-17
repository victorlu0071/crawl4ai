# Content from: https://www.pythonguis.com/faq/get-pyqt-version-number/

[](https://www.pythonguis.com/faq/get-pyqt-version-number/#menu)
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
# How to get the PyQt version number?
Find out which version of PyQt or PySide you're running
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Jun 29 [ FAQ ](https://www.pythonguis.com/faq/)
Sometimes you need to know which version of PyQt or PySide you have installed. Below are two methods of getting this information from your system -- first using `pip` and second from PyQt/PySide itself.
## Finding the version from the command prompt
If you just want to know which version is installed for yourself, and you installed the package using `pip`, you can use the following command to return the current version.
  * PyQt5
  * PyQt6
  * PySide2
  * PySide6


bash ```
pip show pyqt5

```

bash ```
pip show pyqt6

```

bash ```
pip show pyside2

```

bash ```
pip show pyside6

```

This outputs the metadata from the `pip` database, including the version number, e.g.
python ```
Name: PyQt5
Version: 5.15.1
Summary: Python bindings for the Qt cross platform application toolkit
Home-page: https://www.riverbankcomputing.com/software/pyqt/
Author: Riverbank Computing Limited
Author-email: info@riverbankcomputing.com
License: GPL v3
Location: /home/martin/.local/lib/python3.7/site-packages
Requires: PyQt5-sip
Required-by:

```

## Finding the version within your code
Sometimes you need to know the version within your code -- perhaps you're a library developer and your code uses certain features of PyQt which are only available in specific versions and you want to disable this in earlier versions.
In that case you can use the following code to get the version number. This _also_ gives you the version of Qt.
  * PyQt5
  * PyQt6
  * PySide2
  * PySide6


python ```
from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
print("Qt: v", QT_VERSION_STR, "\tPyQt: v", PYQT_VERSION_STR)

```

python ```
from PyQt6.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
print("Qt: v", QT_VERSION_STR, "\tPyQt: v", PYQT_VERSION_STR)

```

python ```
import PySide2
import PySide2.QtCore
print("Qt: v", PySide2.QtCore.__version__, "\tPyQt: v", PySide2.__version__)

```

python ```
import PySide6
import PySide6.QtCore
print("Qt: v", PySide6.QtCore.__version__, "\tPyQt: v", PySide6.__version__)

```

You can run this by opening up a Python shell and copy-pasting in the above code. On my machine it produces the following output.
  * PyQt5
  * PyQt5
  * PySide2
  * PySide6


python ```
>>> from PyQt5.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
>>> print("Qt: v", QT_VERSION_STR, "\tPyQt: v", PYQT_VERSION_STR)
Qt: v 5.15.2  PyQt: v 5.15.6

```

python ```
>> from PyQt6.QtCore import QT_VERSION_STR, PYQT_VERSION_STR
>>> print("Qt: v", QT_VERSION_STR, "\tPyQt: v", PYQT_VERSION_STR)
Qt: v 6.2.0   PyQt: v 6.2.0

```

python ```
>>> import PySide2
>>> import PySide2.QtCore
>>> print("Qt: v", PySide2.QtCore.__version__, "\tPyQt: v", PySide2.__version__)
Qt: v 5.15.2  PyQt: v 5.15.2

```

python ```
>>> import PySide6
>>> import PySide6.QtCore
>>> print("Qt: v", PySide6.QtCore.__version__, "\tPyQt: v", PySide6.__version__)
Qt: v 6.2.0   PyQt: v 6.2.0

```

[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**How to get the PyQt version number?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/get-pyqt-version-number/Python books) on the subject. 
**How to get the PyQt version number?** was published in [faq](https://www.pythonguis.com/faq/) on March 15, 2021 (updated June 29, 2022) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [qt](https://www.pythonguis.com/topics/qt/) [qt6](https://www.pythonguis.com/topics/qt6/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [python](https://www.pythonguis.com/topics/python/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
