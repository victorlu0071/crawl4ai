# Content from: https://www.pythonguis.com/faq/built-in-qicons-pyqt/

[](https://www.pythonguis.com/faq/built-in-qicons-pyqt/#menu)
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
# Q&A: Are there any built-in QIcons?
Using built-in icons for your apps.
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 14 [ FAQ ](https://www.pythonguis.com/faq/)
In the tutorials on this site and in [my books](https://www.pythonguis.com/books/) I recommend using the [fugue icons set](https://p.yusukekamiyamane.com/). This is a _free_ set of icons from Yusuke Kamiyamane, a freelance designer from Tokyo. The set contains 3,570 icons and is a great way to add some nice visual touches to your application without much hassle.
But this isn't the only icon set available, and there's another option you may not know about. Read on for details.
Veronica asked:
> Are there any built-in icons with PyQt5? I have searched the web and it seems like there are some but I can’t find any examples of them being used. Does it depend on the situation? If so, then in which cases can I use an icon without downloading it first?
First we need to clarify what is meant by _built in_ icons -- it can mean two different things depending on context -- either Qt built-in, or system built-in (Linux only). I'll start with the Qt built-ins as that's cross-platform (they're available on Windows, MacOS and Linux).
Table of Contents
  * [Qt Standard Icons](https://www.pythonguis.com/faq/built-in-qicons-pyqt/#qt-standard-icons)
  * [Free Desktop Icons](https://www.pythonguis.com/faq/built-in-qicons-pyqt/#free-desktop-icons)


### Qt Standard Icons
Qt ships with a small set of standard icons you can use in any of your applications for common actions. The icons are all accessible through the current active application style -- available as a series of flags, which can be passed to `.standardIcon` to get the icon.
The following script can be used to display all the built-in icons. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
  * PyQt5
  * PyQt6
  * PySide2
  * PySide6


python ```
import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QStyle, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    icons = sorted([attr for attr in dir(QStyle) if attr.startswith("SP_")])
    layout = QGridLayout()
    for n, name in enumerate(icons):
      btn = QPushButton(name)
      pixmapi = getattr(QStyle, name)
      icon = self.style().standardIcon(pixmapi)
      btn.setIcon(icon)
      layout.addWidget(btn, n // 4, n % 4)
    self.setLayout(layout)

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec_()


```

python ```
import sys
from PyQt6.QtWidgets import (QApplication, QGridLayout, QPushButton, QStyle,
               QWidget)

class Window(QWidget):
  def __init__(self):
    super().__init__()
    icons = sorted([attr for attr in dir(QStyle.StandardPixmap) if attr.startswith("SP_")])
    layout = QGridLayout()
    for n, name in enumerate(icons):
      btn = QPushButton(name)
      pixmapi = getattr(QStyle.StandardPixmap, name)
      icon = self.style().standardIcon(pixmapi)
      btn.setIcon(icon)
      layout.addWidget(btn, int(n/4), int(n%4))
    self.setLayout(layout)

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec()

```

python ```
import sys
from PySide2.QtWidgets import QApplication, QGridLayout, QPushButton, QStyle, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    icons = sorted([attr for attr in dir(QStyle) if attr.startswith("SP_")])
    layout = QGridLayout()
    for n, name in enumerate(icons):
      btn = QPushButton(name)
      pixmapi = getattr(QStyle, name)
      icon = self.style().standardIcon(pixmapi)
      btn.setIcon(icon)
      layout.addWidget(btn, n // 4, n % 4)
    self.setLayout(layout)

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec_()

```

python ```
import sys
from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QStyle, QWidget

class Window(QWidget):
  def __init__(self):
    super().__init__()
    icons = sorted(
      [attr for attr in dir(QStyle.StandardPixmap) if attr.startswith("SP_")]
    )
    layout = QGridLayout()
    for n, name in enumerate(icons):
      btn = QPushButton(name)
      pixmapi = getattr(QStyle, name)
      icon = self.style().standardIcon(pixmapi)
      btn.setIcon(icon)
      layout.addWidget(btn, n // 4, n % 4)
    self.setLayout(layout)

app = QApplication(sys.argv)
w = Window()
w.show()
app.exec()

```

If you run this script you'll see the following window, listing all the available icons.
![Qt's Built-in Icons](https://www.pythonguis.com/static/faq/built-in-qicons-pyqt/icons-builtin.png) _Qt's Built-in Icons_
The full table is below --
.. | .. | ..  
---|---|---  
SP_ArrowBack | SP_DirIcon | SP_MediaSkipBackward  
SP_ArrowDown | SP_DirLinkIcon | SP_MediaSkipForward  
SP_ArrowForward | SP_DirOpenIcon | SP_MediaStop  
SP_ArrowLeft | SP_DockWidgetCloseButton | SP_MediaVolume  
SP_ArrowRight | SP_DriveCDIcon | SP_MediaVolumeMuted  
SP_ArrowUp | SP_DriveDVDIcon | SP_MessageBoxCritical  
SP_BrowserReload | SP_DriveFDIcon | SP_MessageBoxInformation  
SP_BrowserStop | SP_DriveHDIcon | SP_MessageBoxQuestion  
SP_CommandLink | SP_DriveNetIcon | SP_MessageBoxWarning  
SP_ComputerIcon | SP_FileDialogBack | SP_TitleBarCloseButton  
SP_CustomBase | SP_FileDialogContentsView | SP_TitleBarContextHelpButton  
SP_DesktopIcon | SP_FileDialogDetailedView | SP_TitleBarMaxButton  
SP_DialogApplyButton | SP_FileDialogEnd | SP_TitleBarMenuButton  
SP_DialogCancelButton | SP_FileDialogInfoView | SP_TitleBarMinButton  
SP_DialogCloseButton | SP_FileDialogListView | SP_TitleBarNormalButton  
SP_DialogDiscardButton | SP_FileDialogNewFolder | SP_TitleBarShadeButton  
SP_DialogHelpButton | SP_FileDialogStart | SP_TitleBarUnshadeButton  
SP_DialogNoButton | SP_FileDialogToParent | SP_ToolBarHorizontalExtensionButton  
SP_DialogOkButton | SP_FileIcon | SP_ToolBarVerticalExtensionButton  
SP_DialogResetButton | SP_FileLinkIcon | SP_TrashIcon  
SP_DialogSaveButton | SP_MediaPause | SP_VistaShield  
SP_DialogYesButton | SP_MediaPlay  
SP_DirClosedIcon | SP_MediaSeekBackward  
SP_DirHomeIcon | SP_MediaSeekForward  
In our script above to get the icons we're looking them up by name on the `QStyle` object, using `getattr` -- but this is only necessary so we can iterate over the list of names and display the icon next to their name. If you want a specific icon you can access it like any other flag. For example --
  * Others
  * PyQt6


python ```
pixmapi = QStyle.SP_MessageBoxCritical
icon = self.style().standardIcon(pixmapi)

```

python ```
pixmapi = QStyle.StandardPixmap.SP_MessageBoxCritical
icon = self.style().standardIcon(pixmapi)

```

In PyQt6 the flags must be accessed via `QStyle.StandardPixmap`. In other versions, they are available on `QStyle` itself.
### Free Desktop Icons
On Linux desktops there is something called the _Free Desktop Specification_ which defines standard names for icons for specific actions.
If your application uses these specific icon names (and loads the icon from a "theme") then on Linux your application will use the current icon set which is enabled on the desktop. The idea is to make all application have the same look & feel while remaining user configurable.
To use these icons within Qt Designer you would select the drop-down and choose "Set Icon From Theme..." 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
![Icon theme in Qt Designer](https://www.pythonguis.com/static/faq/built-in-qicons-pyqt/icontheme1.png)
You then enter the _name_ of the icon you want to use, e.g. `document-new` (the [full list of valid names](https://specifications.freedesktop.org/icon-naming-spec/latest/ar01s04.html)).
![Icon theme in Qt Designer](https://www.pythonguis.com/static/faq/built-in-qicons-pyqt/icontheme2.png)
If you're not using designer, you can set icons from a theme in your code using the following.
python ```
    icon = QtGui.QIcon.fromTheme("document-new")
    self.pushButton_n6.setIcon(icon)

```

If you're developing a cross-platform application you'll still need your own icons for Windows & MacOS, but by using these theme names you can ensure that your app looks _native_ when run on Linux.
> Does the .fromTheme() option only work on Linux?
Qt themes work on all platforms, it's just that on Linux you get the theme for _free_. On non-Linux platforms you have to define your own icon theme from scratch. However, this is only really worth doing if you want to have a Linux-native look, for other use cases the `QResource` system is simpler.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Q &A: Are there any built-in QIcons?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/built-in-qicons-pyqt/Python books) on the subject. 
**Q &A: Are there any built-in QIcons?** was published in [faq](https://www.pythonguis.com/faq/) on May 11, 2020 (updated April 14, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [icons](https://www.pythonguis.com/topics/icons/) [theme](https://www.pythonguis.com/topics/theme/) [ qt-designer](https://www.pythonguis.com/topics/qt-designer/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/)
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
