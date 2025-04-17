# Content from: https://www.pythonguis.com/faq/ui-files-with-fbs/

[](https://www.pythonguis.com/faq/ui-files-with-fbs/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PyQt5 ](https://www.pythonguis.com/pyqt5/)
  * [PyQt5 Tutorial ](https://www.pythonguis.com/pyqt5-tutorial/)
  * Basics
  * [Create a PyQt5 app](https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/)
  * [PyQt5 Signals](https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/)
  * [PyQt5 Widgets](https://www.pythonguis.com/tutorials/pyqt-basic-widgets/)
  * [PyQt5 Layouts](https://www.pythonguis.com/tutorials/pyqt-layouts/)
  * [PyQt5 Menus](https://www.pythonguis.com/tutorials/pyqt-actions-toolbars-menus/)
  * [PyQt5 Dialogs](https://www.pythonguis.com/tutorials/pyqt-dialogs/)
  * [Multi-window PyQt5](https://www.pythonguis.com/tutorials/creating-multiple-windows/)
  * Qt Designer
  * [First Qt Designer app](https://www.pythonguis.com/tutorials/first-steps-qt-creator/)
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/creating-dialogs-qt-designer/)
  * [The QResource System in PyQt5](https://www.pythonguis.com/tutorials/qresource-system/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/)
  * Plotting
  * [Plotting With PyQtGraph and PyQt5](https://www.pythonguis.com/tutorials/plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PyQt5](https://www.pythonguis.com/tutorials/plotting-matplotlib/)
  * QGraphics
  * [Vector Graphics](https://www.pythonguis.com/tutorials/pyqt-qgraphics-vector-graphics/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/qpropertyanimation/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/system-tray-mac-menu-bar-applications-pyqt/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/)
  * [Packaging for Linux](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-linux-pyinstaller/)
  * [Packaging QResources](https://www.pythonguis.com/tutorials/packaging-data-files-pyqt5-with-qresource-system/)
  * [Packaging with fbs](https://www.pythonguis.com/tutorials/packaging-pyqt5-apps-fbs/)
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
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# .ui files with fbs
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
MJ_McLaren | 2020-05-07 16:49:19 UTC | #1
https://www.pythonguis.com/courses/qt-creator/embed-pyqtgraph-custom-widgets-qt-app/
I'm trying to integrate this technique with fbs but can't seem to make it work. It doesn't see my .ui file. Can you please explain how to set this up in fbs?
mike2750 | 2020-07-23 13:47:22 UTC | #2
@MJ_McLaren Its probably due to the way the file is being called i learned the below techniques from trial and error and loading it this way loads it from a relative path which works in fbs when run from source in pycharm and fbs and when frozen
This would be the fbs way to do that tutorial with fbs in mind and if the mainwindow.ui file is in same path as main.py and also in "src/main/resources/base/mainwindow.ui"
python ```
# from fbs_runtime.application_context import is_frozen
# from fbs_runtime.excepthook.sentry import SentryExceptionHandler
import os
import sys
import requests
from PyQt5 import uic, QtWidgets
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from fbs_runtime.application_context.PyQt5 import ApplicationContext, \
  cached_property

class AppContext(ApplicationContext):
  def run(self):
    version = self.build_settings['version']
    QApplication.setApplicationName("App Name")
    QApplication.setOrganizationName("Some Corp")
    QApplication.setOrganizationDomain("example.com")
    current_version = version
    self.main_window.setWindowTitle("App Name v" + version)
    self.main_window.show()
    return self.app.exec_()
  @cached_property
  def main_window(self):
    return MainWindow(self)

qtCreatorFile = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "mainwindow.ui") # Type your file path
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self, ctx):
    super().__init__()
    self.ctx = ctx
    self.setupUi(self)

    #Put all your custom signals slots and other code here.

import sys
if __name__ == '__main__':
  appctxt = AppContext()
  exit_code = appctxt.run()
  sys.exit(exit_code)

```

I use this same approach in my fbs app with lots of UI files.
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Setting up Application context with fbs and UI was a royal pita to learn but once you have a nice skeleton def save a copy somewhere cause it comes in handy. You will want to then define as much as possible in the UI file vs the python main so its cleaner and just have the logic in the python.
For reference of my setup
Main root is `src/main/python`
Ui files `src/main/python/ui`
For FBS stuff i also copy same files into this path so bundled properly when compiled `src/main/resources/base/ui`
To load say the about.ui file from "src/main/resources/base/ui/about.ui" via relative path "ui/about.ui" with FBS even when frozen
python ```
about_ui = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), 'ui', "about.ui")
uic.loadUi(about_ui, self)

```

This handy trick also works for images too :slightly_smiling_face:
loads my app logo in about dialog from relative 'images/chevron_logo.png'
python ```
self.about_app_logo.setPixmap(
      QPixmap(os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), 'images', 'chevron_logo.png')))

```

==================================================== 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
The best part of joining paths and that code is always works from where code is executed even when frozen and its OS agnostic so works for joining same path on Windows with path separators \ like it does with / on linux and Mac. One of the things i wish i had learned at beginning of my python adventures.
this equals path of current running script
python ```
os.path.abspath(os.path.dirname(sys.argv[0]))

```

This is joining current path + 'ui' folder + 'about.ui' filename `os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), 'ui', "about.ui")`
To experiment can use the below snippet and adjust
python ```
import os
import sys
print(os.path.abspath(os.path.dirname(sys.argv[0])))
print(os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), 'ui'))
print(os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), 'ui', "about.ui"))

```

Output
python ```
/home/username/.config/JetBrains/PyCharm2020.1/scratches
/home/username/.config/JetBrains/PyCharm2020.1/scratches/ui
/home/username/.config/JetBrains/PyCharm2020.1/scratches/ui/about.ui

```

====================================================
To understand the resource files and structure for when its frozen also see. https://build-system.fman.io/manual/#resource-files
Hopefully that helps some and provides some context.
Screenshots for visualization. ![Selection_999\(1301\)|690x292](https://www.pythonguis.com/static/faq/forum/ui-files-with-fbs/rng9wwt4Hu1NeGFiXXCVICPlhlj.png) ![Selection_999\(1302\)|358x348](https://www.pythonguis.com/static/faq/forum/ui-files-with-fbs/vcQBMqie5mXBDpfirCSOyihgHyt.png)
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**.ui files with fbs** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/ui-files-with-fbs/Python books) on the subject. 
**.ui files with fbs** was published in [faq](https://www.pythonguis.com/faq/) on May 07, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyqtgraph](https://www.pythonguis.com/topics/pyqtgraph/) [qtdesigner](https://www.pythonguis.com/topics/qtdesigner/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [ data-science](https://www.pythonguis.com/topics/data-science/)
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
