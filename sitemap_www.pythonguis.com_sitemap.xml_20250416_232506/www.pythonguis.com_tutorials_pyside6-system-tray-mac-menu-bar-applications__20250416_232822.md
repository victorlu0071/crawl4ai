# Content from: https://www.pythonguis.com/tutorials/pyside6-system-tray-mac-menu-bar-applications/

[](https://www.pythonguis.com/tutorials/pyside6-system-tray-mac-menu-bar-applications/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PySide6 ](https://www.pythonguis.com/pyside6/)
  * [PySide6 Tutorial ](https://www.pythonguis.com/pyside6-tutorial/)
  * Basics
  * [Create a PySide6 app](https://www.pythonguis.com/tutorials/pyside6-creating-your-first-window/)
  * [PySide6 Signals](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/)
  * [PySide6 Widgets](https://www.pythonguis.com/tutorials/pyside6-widgets/)
  * [PySide6 Layouts](https://www.pythonguis.com/tutorials/pyside6-layouts/)
  * [PySide6 Menus](https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/)
  * [PySide6 Dialogs](https://www.pythonguis.com/tutorials/pyside6-dialogs/)
  * [Multi-window PySide6](https://www.pythonguis.com/tutorials/pyside6-creating-multiple-windows/)
  * Qt Designer
  * [First Qt Designer app](https://www.pythonguis.com/tutorials/pyside6-first-steps-qt-designer/)
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/pyside6-qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/pyside6-creating-dialogs-qt-designer/)
  * [The QResource System in PySide6](https://www.pythonguis.com/tutorials/pyside6-qresource-system/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/pyside6-qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/pyside6-modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/pyside6-qtableview-modelviews-numpy-pandas/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/pyside6-bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/pyside6-creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/pyside6-animated-widgets/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/pyside6-embed-pyqtgraph-custom-widgets/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/pyside6-transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/pyside6-system-tray-mac-menu-bar-applications/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyside6-applications-windows-pyinstaller-installforge/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyside6-applications-pyinstaller-macos-dmg/)
  * [Packaging QResources](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/)
  * Resources
  * [Books](https://www.pythonguis.com/books/)
  * Services
  * [Consulting](https://www.pythonguis.com/hire/)
  * [1:1 Coaching](https://www.pythonguis.com/live/)
  * [Contact](https://www.pythonguis.com/contact/)
  * [About](https://www.pythonguis.com/about/)
  * Libraries
  * [PyQt6](https://www.pythonguis.com/pyqt6/)
  * [PyQt5](https://www.pythonguis.com/pyqt5/)
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# System Tray & Mac Menu Bar Applications in PySide6
Add quick access functions to your apps
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Mar 15 PySide6 [ Extended UI features with PySide6 ](https://www.pythonguis.com/pyside6-tutorial/#pyside6-advanced-features)
#### [ PySide6 Tutorial ](https://www.pythonguis.com/pyside6-tutorial/) — [Extended UI features with PySide6](https://www.pythonguis.com/pyside6-tutorial/#pyside6-advanced-features)
  * [Transmitting Extra Data With Qt Signals in PySide6](https://www.pythonguis.com/tutorials/pyside6-transmitting-extra-data-qt-signals/)
  * [System Tray & Mac Menu Bar Applications in PySide6](https://www.pythonguis.com/tutorials/pyside6-system-tray-mac-menu-bar-applications/)


This tutorial is also available for [PyQt6](https://www.pythonguis.com/tutorials/pyqt6-system-tray-mac-menu-bar-applications/) , [PySide2](https://www.pythonguis.com/tutorials/pyside-system-tray-mac-menu-bar-applications/) and [PyQt5](https://www.pythonguis.com/tutorials/system-tray-mac-menu-bar-applications-pyqt/)
System tray applications (or menu bar applications) can be useful for making common functions or information available in a small number of clicks. For full desktop applications they're a useful shortcut to control apps without opening up the whole window.
Qt provides a simple interface for building cross-platform system tray (Windows) or menu bar (MacOS) apps.
## Minimal example
Below is a minimal working example for showing an icon in the toolbar/system tray with a menu. The action in the menu isn't connected and so doesn't do anything yet.
python ```
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
app = QApplication([])
app.setQuitOnLastWindowClosed(False)
# Create the icon
icon = QIcon("icon.png")
# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)
# Create the menu
menu = QMenu()
action = QAction("A menu item")
menu.addAction(action)
# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)
# Add the menu to the tray
tray.setContextMenu(menu)
app.exec()

```

You'll notice that there isn't a `QMainWindow`, simply because we don't actually have any window to show. You can create a window as normal without affecting the behaviour of the system tray icon.
You'll need an icon for this example — I recommend the [fugue icon set](http://p.yusukekamiyamane.com/).
The default behaviour in Qt is to close an application once all the active windows have closed. This won't affect this toy example, but will be an issue in application where you _do_ create windows and then close them. Setting `app.setQuitOnLastWindowClosed(False)` stops this and will ensure your application keeps running.
The provided icon shows up in the toolbar (you can see it on the left). 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
![The system tray icon shown on the menu bar \(as a poo emoticon\)](https://www.pythonguis.com/static/tutorials/qt/system-tray-mac-menu-bar/systemtray-1.jpg) _The system tray icon shown on the menu bar (as a poo emoticon)_
Clicking on the icon shows the added menu.
![System tray icon with menu expanded](https://www.pythonguis.com/static/tutorials/qt/system-tray-mac-menu-bar/systemtray-2.jpg) _System tray icon with menu expanded_
This application doesn't do anything yet, so in the next part we'll expand this example to create a mini color-picker.
## Color tray
Below is a more complete working example using the built in `QColorDialog` from Qt to give a toolbar accessible color picker. The menu lets you choose to get the picked color as HTML-format `#RRGGBB`, `rgb(R,G,B)` or `hsv(H,S,V)`.
python ```
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QColorDialog, QSystemTrayIcon, QMenu
app = QApplication([])
app.setQuitOnLastWindowClosed(False)
# Create the icon
icon = QIcon("color.png")
clipboard = QApplication.clipboard()
dialog = QColorDialog()
def copy_color_hex():
  if dialog.exec():
    color = dialog.currentColor()
    clipboard.setText(color.name())
def copy_color_rgb():
  if dialog.exec():
    color = dialog.currentColor()
    clipboard.setText("rgb(%d, %d, %d)" % (
      color.red(), color.green(), color.blue()
    ))
def copy_color_hsv():
  if dialog.exec():
    color = dialog.currentColor()
    clipboard.setText("hsv(%d, %d, %d)" % (
      color.hue(), color.saturation(), color.value()
    ))
# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)
# Create the menu
menu = QMenu()
action1 = QAction("Hex")
action1.triggered.connect(copy_color_hex)
menu.addAction(action1)
action2 = QAction("RGB")
action2.triggered.connect(copy_color_rgb)
menu.addAction(action2)
action3 = QAction("HSV")
action3.triggered.connect(copy_color_hsv)
menu.addAction(action3)
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)
# Add the menu to the tray
tray.setContextMenu(menu)
app.exec()

```

As in the previous example there is no `QMainWindow` for this example. The menu is created as before, but adding 3 actions for the different output formats. Each action is connected to a specific handler function for the format it represents. Each handler shows a dialog and, if a color is selected, copies that color to the clipboard in the given format.
As before, the icon appears in the toolbar.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
![Color-picker icon on the Mac menu bar \(left hand side\)](https://www.pythonguis.com/static/tutorials/qt/system-tray-mac-menu-bar/system-colorpicker-1.jpg) _Color-picker icon on the Mac menu bar (left hand side)_
Clicking the icon shows a menu, from which you can select the format of image you want to return.
![Options to return chosen color \(hex, RGB or HSV\)](https://www.pythonguis.com/static/tutorials/qt/system-tray-mac-menu-bar/system-colorpicker-2.jpg) _Options to return chosen color (hex, RGB or HSV)_
Once you've chosen the format, you'll see the standard Qt color picker window.
![PySide provides access to system dialogs, such as this Mac color picker](https://www.pythonguis.com/static/tutorials/qt/system-tray-mac-menu-bar/system-colorpicker-3.png) _PySide provides access to system dialogs, such as this Mac color picker_
Select the color you want and click OK. The chosen color will be copied to the clipboard in the requested format. The formats available will product the following output:
python ```
#a2b3cc       # range 00-FF
rgb(25, 28, 29)   # range 0-255
hsv(14, 93, 199)  # range 0-255

```

### Suggestions for improvements
One simple and nice improvement would be to make the previously-selected colours available to re-copy in other formats. You could do this by storing the color result value from the existing menu. Then add 3 more options, which show (on the menu) their return values — clicking these just copies that value to the clipboard. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**System Tray & Mac Menu Bar Applications in PySide6** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/pyside6-system-tray-mac-menu-bar-applications/Python books) on the subject. 
**System Tray & Mac Menu Bar Applications in PySide6** was published in [tutorials](https://www.pythonguis.com/tutorials/) on September 22, 2021 (updated March 15, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[windows](https://www.pythonguis.com/topics/windows/) [linux](https://www.pythonguis.com/topics/linux/) [mac](https://www.pythonguis.com/topics/mac/) [menu-bar](https://www.pythonguis.com/topics/menu-bar/) [system-tray](https://www.pythonguis.com/topics/system-tray/) [qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
