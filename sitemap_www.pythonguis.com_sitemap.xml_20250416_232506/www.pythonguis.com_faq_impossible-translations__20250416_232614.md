# Content from: https://www.pythonguis.com/faq/impossible-translations/

[](https://www.pythonguis.com/faq/impossible-translations/#menu)
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
# Impossible Translations
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Eolinwen | 2020-06-27 16:48:38 UTC | #1
Hi,
Since 15 days, I have worked on Translations for one of my project. All was working nearly fine, I have just forgotten to translate in my pro file my ui files so I 've had a partial translation. Not a really big issue. After including my ui files in my pro file, I've been able to translate then and generate my qm files like usual. I've decided to move them in a translation folder for reaching my final structure. Ui and Python files are in separated folder at the same level and my start_app.py file run my app without any issue. See the screenshot for project structure. [url=http://pix.toile-libre.org/?img=1593279813.png]![](https://www.pythonguis.com/static/faq/forum/impossible-translations/nWc4jB1yysXQh57U0wYgO3ThtKR.png)[/url]
What is surrounded in red does not exist in my final structure. It was just for testing but even so it doesn't work.
I've tried several combination in my start_app file but nothing until now. Initially, I was thinking that just a path problem. But Even if I have qm files at the same level than start_app file it doesn't work.
I precise that I'm an on Linux Manjaro with Python 3.8.3, Qt 5.15.0, PyQt5 5.15.0
Now, I don't know what doing. I'm coming completely crazy with this issue. If somebody can help me, that will be great. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
PS it is a minimal example.
Here my code of my start_app.py. Like you can see,I've tried several things.
python ```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTranslator, QLocale, QLibraryInfo, QDir
from windows.minimal import MiniMal

if __name__ == "__main__":
application = QApplication(sys.argv)
# Translate application
# locale = QLocale.system().name()
# TranslationsPath = QDir('./translations').canonicalPath()
# translator = QTranslator()
# path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
# translator.load(locale, path)
# if len(sys.argv) == 1:
#   # locale = QLocale().system().name()
#   translator.load(locale, "minimal", ".")
#   # translator.load('qt_%s' % locale, path)
# else:
#   translator.load("minimal."+ sys.argv[1])
#   # translator.load(locale + sys.argv[1])
# application.installTranslator(translator)
enNativeLanguage = len(sys.argv) == 1
if enNativeLanguage:
  locale = QLocale().system().name()
else:
  languageCountry = sys.argv[1]
translators = []
for prefixQm in ("minimal.", "qt_", "qtbase_"):
  translator = QTranslator()
  translators.append(translator)
  if enNativeLanguage:
    translator.load(locale, prefixQm)
  else:
    translator.load(prefixQm+languageCountry)
  application.installTranslator(translator)
window = MiniMal()
window.show()
rc = application.exec_()
sys.exit(rc)

```

Here the code of the minimal.py (in the folder called windows)
python ```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui.exempleui import Ui_MainWindow

class MiniMal(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi()
    self.connectActions()
    format_capture = ['Dv Raw (.dv)', 'DV 2 (.avi)', 'Dv (.avi)', 'Hdv (.m2t)', 'Mpeg 2 (.mpg)', 'Mov (.mov)']
    for format in format_capture:
      self.ui.cmbformatacquisition.addItem(format)
      self.ui.cmbformatacquisition.setCurrentIndex(0)
  def setupUi(self):
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.lnetext.setText(self.tr("My Awesome Movie"))
    self.ui.btnsomething.setToolTip(self.tr("Choose the Dv Acquisition mode"))
    self.ui.lnetext.setToolTip(self.tr("Set the Film Name"))
    self.ui.cmbformatacquisition.setToolTip(self.tr("Choose a format"))
    self.ui.chksystray.setToolTip(self.tr("Application in the systray"))
    self.ui.lnetext.setStatusTip(self.tr('The Film name is '))
    self.ui.btnsomething.setStatusTip(self.tr('Dv Acquisition mode is used'))
    self.ui.cmbformatacquisition.setStatusTip(self.tr("Acquisition Mode Changed"))
    self.ui.chksystray.setStatusTip(self.tr('Show this window in the systray'))
  def connectActions(self):
    self.ui.cmbformatacquisition.currentIndexChanged.connect(self.callSomething)
    self.ui.lnetext.textChanged.connect(self.showName)
    self.ui.chksystray.toggled.connect(self.putSystray)
    self.ui.btnsomething.clicked.connect(self.callSomething)
  def changeChoice(self):
    pass
  def putSystray(self):
    pass
  def showName(self):
    pass
  def callSomething(self):
    pass

```

Here the code of the exempleui.py (in the folder called ui)
python ```
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'exemple.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(560, 339)
    MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.lnetext = QtWidgets.QLineEdit(self.centralwidget)
    self.lnetext.setGeometry(QtCore.QRect(210, 30, 251, 26))
    self.lnetext.setObjectName("lnetext")
    self.label = QtWidgets.QLabel(self.centralwidget)
    self.label.setGeometry(QtCore.QRect(36, 30, 101, 20))
    self.label.setObjectName("label")
    self.btnsomething = QtWidgets.QPushButton(self.centralwidget)
    self.btnsomething.setGeometry(QtCore.QRect(70, 90, 361, 71))
    self.btnsomething.setObjectName("btnsomething")
    self.cmbformatacquisition = QtWidgets.QComboBox(self.centralwidget)
    self.cmbformatacquisition.setGeometry(QtCore.QRect(80, 175, 351, 51))
    self.cmbformatacquisition.setObjectName("cmbformatacquisition")
    self.chksystray = QtWidgets.QCheckBox(self.centralwidget)
    self.chksystray.setGeometry(QtCore.QRect(60, 250, 371, 26))
    self.chksystray.setObjectName("chksystray")
    MainWindow.setCentralWidget(self.centralwidget)
    self.menubar = QtWidgets.QMenuBar(MainWindow)
    self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 28))
    self.menubar.setObjectName("menubar")
    self.menuFile = QtWidgets.QMenu(self.menubar)
    self.menuFile.setObjectName("menuFile")
    self.menuHelp = QtWidgets.QMenu(self.menubar)
    self.menuHelp.setObjectName("menuHelp")
    MainWindow.setMenuBar(self.menubar)
    self.statusbar = QtWidgets.QStatusBar(MainWindow)
    self.statusbar.setObjectName("statusbar")
    MainWindow.setStatusBar(self.statusbar)
    self.actionQuit = QtWidgets.QAction(MainWindow)
    self.actionQuit.setObjectName("actionQuit")
    self.actionAbout = QtWidgets.QAction(MainWindow)
    self.actionAbout.setObjectName("actionAbout")
    self.menuFile.addAction(self.actionQuit)
    self.menuHelp.addAction(self.actionAbout)
    self.menubar.addAction(self.menuFile.menuAction())
    self.menubar.addAction(self.menuHelp.menuAction())
    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
  def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.label.setText(_translate("MainWindow", "Name"))
    self.btnsomething.setText(_translate("MainWindow", "Click me"))
    self.chksystray.setText(_translate("MainWindow", "Put in this window in the systray"))
    self.menuFile.setTitle(_translate("MainWindow", "File"))
    self.menuHelp.setTitle(_translate("MainWindow", "Help"))
    self.actionQuit.setText(_translate("MainWindow", "Quit"))
    self.actionAbout.setText(_translate("MainWindow", "About"))

if __name__ == "__main__":
  import sys
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()
  ui = Ui_MainWindow()
  ui.setupUi(MainWindow)
  MainWindow.show()
  sys.exit(app.exec_())

```

@martin BTW Still an idea for the next version of the book.
martin | 2020-06-30 11:46:02 UTC | #2
Sorry for the delay in answering this, needed a couple of days to recover from the book ;) This _will_ be in the next update, because I know how horrible it can be. It's been a while since I did it, and had to go digging into an old projects, but I found this snippet that I know _was_ working.
This loads the base Qt translations, and then custom translations.
python ```
# Get the locale (language) name
locale = QLocale.system().name()
# Load base QT translations from the normal place
translator_qt = QTranslator()
if translator_qt.load("qt_%s" % locale, QLibraryInfo.location(QLibraryInfo.TranslationsPath)):
  app.installTranslator(translator_qt)
# Load custom translations
translator_custom = QTranslator()
if translator_custom .load("custom_%s" % locale, 'translations'):
    app.installTranslator(translator_custom )

```

In this setup I had a folder `translations` which contained all my custom translations. I used the current scripts folder to construct that path (for when it was packaged), perhaps you'll see something similar?
The following lines confuse me a bit
python ```
  if enNativeLanguage:
    translator.load(locale, prefixQm)

```

...as this means if you pass the language on the command line, it doesn't prefix the files, but looks in a _folder_ named with the prefix (right?) ...that doesn't seem right.
Eolinwen | 2020-07-01 16:00:51 UTC | #3
No worries. I understand and what great work. :heart_eyes: To answer your question about the file, that's correct. :wink:
For my part, I came to a fairly close conclusion in the following way. It is true that it is annoying when it does not work because we have no errors therefore no way to resolve this situation. We can only fumble. I am almost arrived at the same conclusion with the following code by taking all the code, unfortunately I haven't had time to test yet:
```translator = QTranslator() 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
locale_path = os.path.join(os.path.dirname(os.path.abspath(**file**)), "translations") locale = QLocale().system().name()
qt_locale_path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
locale = os.path.join (locale_path, locale)
python ```

To answer your question about the file, that's correct. It was badly formatted and Drop this part. It was an error.
I too have delved into a project on which I had introduced the translations
at least October but the situation is different because there is no ui file and no
translations folder. Everything is on the same level. And strangely, it doesn't work now, has
when I'm sure it worked in October. I even checked if it didn't
was not from my version of QT / PyQt but at first glance not.
I also even asked myself the question if there was not a problem with my pro file, my ts files and therefore qm.

```

SOURCES + = ../windows/minimal.py ../ui/exempleui.py TRANSLATIONS + = ../translations/minimal.fr_FR.ts ../translations/minimal.en_US.ts
python ```
Speaking of which, I would like you to give me your opinion on my .pro file.
I wonder if all would not come from him with an error on the roads.
Besides, should we do it as I did or should we specify the source for
each file and for each translation, in this style:

```

SOURCES + = SOURCES + = .... TRANSLATIONS + = TRANSLATIONS + = TRANSLATIONS + = ....
python ```

No in fact it was to have the qt_fr files, qt_base_fr if minimal.qm existed. The
2 first are necessary to translate the ui (buttons, menus, ...). It was very poorly formulated, I understand it well.
In the next few days I will test this code and I will give you news I think Thursday Evening.
-------------------------
Eolinwen | 2020-07-01 16:36:24 UTC | #4
@martin
I have tested the following code that you have given to me and it doesn't work. The Ui is not translated automatically and if I precise the locale by this one `python start_app.py fr_FR` nothing too.


```

import sys from PyQt5.QtWidgets import QApplication from PyQt5.QtCore import QTranslator, QLocale, QLibraryInfo
from windows.minimal import MiniMal
if **name** == "**main** ": application = QApplication(sys.argv)
python ```
# # Translate application
locale = QLocale().system().name()
# qt_path_locale = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
translator_qt = QTranslator()
# if translator_qt.load("qt_%s" % locale, qt_path_locale):
if translator_qt.load("qt_%s" % locale, QLibraryInfo.location(QLibraryInfo.TranslationsPath)):
  application.installTranslator(translator_qt)
translator_custom = QTranslator()
if translator_custom.load("minimal_%s" % locale, "translations"):
  application.installTranslator(translator_custom)
window = MiniMal()
window.show()
rc = application.exec_()
sys.exit(rc)

```

python ```

-------------------------
Eolinwen | 2020-07-03 13:25:13 UTC | #5
Hi Ah . :heart_eyes: :stuck_out_tongue_winking_eye: :hot_face: :smiling_imp:
I've found the solution. That's work at least on the minimal code above. In fact, there were actually 2 problems ; one with the path of folder translations and another with the end of my qm files.
I've just modified this line :

```

... translator_custom = QTranslator() if translator_custom.load("minimal.%s" % locale, "translations"): ....
python ```
Now I'm going to modified my real program and check if qt_** translations of Ui's works fines.
And i'll give you a feedback perhaps today but nothing is sure. :crazy_face:
-------------------------
Eolinwen | 2020-07-03 13:25:13 UTC | #6
As promised I give feedback.
My initial project works as well as my example.
Only downside: the translation of software other than that of the system does not work. We cannot perform this operation
by launching start_app.py specifying the target language. Example: Switch software from French to English: `python start_up.py en_US`
For now, it is not a priority, the main is done but I will come back to it.
Afterwards, there will only be dynamic translation of the software, by selecting the language in a QComboBox, for example.
Another idea for the next version. To put in your TODO list. :stuck_out_tongue_winking_eye:
I close this thread as it is resolved.
Thanks again. :wink:
-------------------------
martin | 2020-07-03 13:40:38 UTC | #7
Thanks for documenting what you did @Eolinwen it'll be a great help when I come to write this chapter ;)
-------------------------
Eolinwen | 2020-07-04 16:21:15 UTC | #8
I'll give you some feedback when I will do that but not for the moment. :+1:
-------------------------
probono | 2021-02-28 10:42:23 UTC | #9
I am still looking for the leanest way to translate PyQt5 applications, ideally without the need to compile anything. After all, I chose PyQt5 specifically because it doesn't need to be compiled...
This is what I have, notice the QUESTIONs:

```

# !/usr/bin/env python3
# -_- coding: UTF-8 -_ -
import os, sys import gettext
# QUESTION: This style of imports significantly simplifies the code.
# Does it lead to a noticeable memory/performance penalty though?
# Is it frowned upon?
from PyQt5.QtCore import _from PyQt5.QtGui import_ from PyQt5.QtWidgets import *
class Window(QMainWindow):
python ```
def __init__(self, parent=None):
  super().__init__(parent)
  self.setWindowTitle(_("Translate me"))
  self.resize(400, 200)
  self.centralWidget = QLabel(_("If this text is translated, then it is working"))
  self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
  self.setCentralWidget(self.centralWidget)

```

if **name** == "**main** ":
python ```
app = QApplication(sys.argv)
# Load the translations for Qt itself as seen in, e.g., the "About Qt" dialog
# On FreeBSD, this gets resolved to /usr/local/share/qt5/translations/ which contains qt_de.qm
# which references qtbase_de, qtscript_de, qtmultimedia_de, qtxmlpatterns_de
qt_translator = QTranslator()
qt_translator.load("qt_" + QLocale.system().name(),
          QLibraryInfo.location(QLibraryInfo.TranslationsPath))
app.installTranslator(qt_translator)
# Load the translations for this application.
# On FreeBSD, this gets resolved to
# access("Desktop/translated.py/translations/app_de_DE",R_OK) ERR#20 'Not a directory'
# access("Desktop/translated.py/translations/app_de.qm",R_OK) ERR#20 'Not a directory'
# access("Desktop/translated.py/translations/app_de",R_OK) ERR#20 'Not a directory'
# access("Desktop/translated.py/translations/app.qm",R_OK) ERR#20 'Not a directory'
# access("Desktop/translated.py/translations/app",R_OK) ERR#20 'Not a directory
# QUESTION: Can we use this to override some strings in Qt that we do not like? (Including English)
# QUESTION: Can we make it load non-binary .ts files rather than binary .qm files?
# This would make distributing and changing the strings locally much easier and remove
# the need for compilation, which is the point in using Python
app_translator = QTranslator()
app_translator.load("app_" + QLocale.system().name(),
          __file__ + "/translations")
app.installTranslator(app_translator)
# QUESTION: According to https://doc.bccnsoft.com/docs/PyQt5/i18n.html,
# PyQt5 has nasty quirks when it comes to using Qt translations which make this cumbersome.
# Would it be better to use the Python way using gettext
# for our own translatable strings?
# https://www.mattlayman.com/blog/2015/i18n/
# https://phrase.com/blog/posts/translate-python-gnu-gettext/
# On FreeBSD, this gets resolved to
# /usr/home/user/Desktop/locale/de_DE.UTF-8/LC_MESSAGES/app.mo
# /usr/home/user/Desktop/locale/de_DE/LC_MESSAGES/app.mo
# /usr/home/user/Desktop/locale/de.UTF-8/LC_MESSAGES/app.mo
# /usr/home/user/Desktop/locale/de/LC_MESSAGES/app.mo
# QUESTION: Can we make it load non-binary .po files rather than binary .mo files?
# This would make distributing and changing the strings locally much easier and remove
# the need for compilation, which is the point in using Python
localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locales')
translate = gettext.translation('messages', localedir, fallback=True)
_ = translate.gettext
win = Window()
win.show()
QMessageBox.aboutQt(None)
sys.exit(app.exec_())
# Step 0: The source Python file MUST have:
# # -*- coding: UTF-8 -*-
# Step 1: Extract gettext strings from source, by generating a .pot template file with
# mkdir -p locales/{en,de}/LC_MESSAGES/
# xgettext --language=Python *.py --output=locales/messages.pot
# sed -i -e 's|CHARSET|UTF-8|g' locales/messages.pot
# rm locales/messages.pot-e
# Step 2: Copy the .pot template file for each language (or let Weblate do it)
# cp locales/messages.pot locales/de/LC_MESSAGES/messages.po
# Step 3: Translate locales/de/LC_MESSAGES/messages.po (or let Weblate do it)
# Step 5: Compile .po into binary .mo (we would like to get rid of this)
# msgfmt locales/de/LC_MESSAGES/messages.po --output-file=locales/de/LC_MESSAGES/messages.mo
# This is super annoying because it means that we need to introduce a compilation step

```

```
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Impossible Translations** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/impossible-translations/Python books) on the subject. 
**Impossible Translations** was published in [faq](https://www.pythonguis.com/faq/) on June 27, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
