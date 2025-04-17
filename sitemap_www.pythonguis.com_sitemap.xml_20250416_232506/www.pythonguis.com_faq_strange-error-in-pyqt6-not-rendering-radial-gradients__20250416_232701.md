# Content from: https://www.pythonguis.com/faq/strange-error-in-pyqt6-not-rendering-radial-gradients/

[](https://www.pythonguis.com/faq/strange-error-in-pyqt6-not-rendering-radial-gradients/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PyQt6 ](https://www.pythonguis.com/pyqt6/)
  * [PyQt6 Tutorial ](https://www.pythonguis.com/pyqt6-tutorial/)
  * Basics
  * [Create a PyQt6 app](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/)
  * [PyQt6 Signals](https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/)
  * [PyQt6 Widgets](https://www.pythonguis.com/tutorials/pyqt6-widgets/)
  * [PyQt6 Layouts](https://www.pythonguis.com/tutorials/pyqt6-layouts/)
  * [PyQt6 Menus](https://www.pythonguis.com/tutorials/pyqt6-actions-toolbars-menus/)
  * [PyQt6 Dialogs](https://www.pythonguis.com/tutorials/pyqt6-dialogs/)
  * [Multi-window PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/)
  * Qt Designer
  * [First Qt Designer app](https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/)
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/pyqt6-qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/pyqt6-creating-dialogs-qt-designer/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyqt6-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/pyqt6-qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/pyqt6-qtableview-modelviews-numpy-pandas/)
  * Plotting
  * [Plotting With PyQtGraph and PyQt6](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PyQt6](https://www.pythonguis.com/tutorials/pyqt6-plotting-matplotlib/)
  * QGraphics
  * [Vector Graphics](https://www.pythonguis.com/tutorials/pyqt6-qgraphics-vector-graphics/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/pyqt6-bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/pyqt6-creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/pyqt6-embed-pyqtgraph-custom-widgets-qt-app/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/pyqt6-transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/pyqt6-system-tray-mac-menu-bar-applications/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyqt6-applications-windows-pyinstaller/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyqt6-applications-pyinstaller-macos-dmg/)
  * Resources
  * [Books](https://www.pythonguis.com/books/)
  * Services
  * [Consulting](https://www.pythonguis.com/hire/)
  * [1:1 Coaching](https://www.pythonguis.com/live/)
  * [Contact](https://www.pythonguis.com/contact/)
  * [About](https://www.pythonguis.com/about/)
  * Libraries
  * [PySide6](https://www.pythonguis.com/pyside6/)
  * [PyQt5](https://www.pythonguis.com/pyqt5/)
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Strange error in PyQt6 (not rendering radial gradients)
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 02 PyQt6 [ FAQ ](https://www.pythonguis.com/faq/)
_PedanticHacker asked_
> Since using `PyQt6`, I am getting this strange error: `qt.svg: <input>:1:8277: Could not parse node: radialGradient`
> The `QSvgRenderer` (used by the `QSvgWidget`) can't display radial gradients in `PyQt6`. This same code, that I have, worked perfectly fine in `PyQt5`, but now on `PyQt6`, it does not render radial gradients in SVGs anymore. Is there a workaround or something?
_Martin Fitzpatrick_
I wonder if there are just some bugs in Qt6 at the moment. Remember the weird glitching effects I saw on the `QGraphicsScene` while using SVG in Qt6? Though losing radial gradient support is a bit weird.
Can you share the SVG? Might be worth validating it.
_PedanticHacker_
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
Well, the code for generating the SVG chessboard is on the python-chess' GitHub site [HERE](https://github.com/niklasf/python-chess/blob/master/chess/svg.py#L71).
The rendering part of the code for the generated python-chess SVG is [HERE](https://github.com/niklasf/python-chess/blob/master/chess/svg.py#L350).
The `board()` method of the `chess.svg` module is the one that generates the SVG chessboard, based upon the arguments given to that method. For the check mark that is the `check` argument. The code given to the `check` argument of `chess.svg.board()` method is:
python ```
if self.board.is_check():
  return self.board.king(self.board.turn)

```

where `self.board` is `chess.Board()` instance.
The error, when there is check in a chessboard position, is this:
python ```
qt.svg: <input>:1:7114: Could not parse node: radialGradient
qt.svg: <input>:1:31331: Could not resolve property: #check_gradient

```

_Martin Fitzpatrick_
Below is a small test case example which works in PyQt5 (read on for the solution in PyQt6). Here's the radial gradient (saved to a file named "gradient.svg") and the test program.
![image|404x192](https://www.pythonguis.com/static/faq/todo/strange-error-in-pyqt6-not-rendering-radial-gradients/ttKRstaEojmFEVMD1rKisbEcju2.png)
The svg
svg ```
<svg width="400" height="150">
 <defs>
  <radialGradient id="grad1"><stop offset="0%" stop-color="#ff0000" stop-opacity="1.0" /><stop offset="50%" stop-color="#e70000" stop-opacity="1.0" /><stop offset="100%" stop-color="#9e0000" stop-opacity="0.0" /></radialGradient>
 </defs>
 <ellipse fill="url(#grad1)" cx="200" cy="70" rx="85" ry="55"/>
 <text x="150" y="86" fill="green" font-family="Verdana" font-size="45">SVG</text>
</svg>

```

The test program
python ```
import math
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5.QtSvg import QGraphicsSvgItem
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.scene = QGraphicsScene()
    self.viewer = QGraphicsView()
    self.setCentralWidget(self.viewer)
    svg = QGraphicsSvgItem('gradient.svg')
    self.scene.addItem(svg)
    self.viewer.setScene(self.scene)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

```

The same code in PyQt6, which just needs to change the import for `from PyQt6.QtSvgWidgets import QGraphicsSvgItem`
python ```
import math
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
from PyQt6.QtSvgWidgets import QGraphicsSvgItem
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.scene = QGraphicsScene()
    self.viewer = QGraphicsView()
    self.setCentralWidget(self.viewer)
    svg = QGraphicsSvgItem('gradient.svg')
    self.scene.addItem(svg)
    self.viewer.setScene(self.scene)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

```

Switching out the radial gradient for a linear one, it works, e.g.
svg ```
<svg width="400" height="150">
 <defs>
 <linearGradient id="grad1" y1="0%" x1="0%" y2="0%" x2="100%">
  <stop offset="0%" style="stop-color:rgb(255,255,0);stop-opacity:1"/>
  <stop offset="100%" style="stop-color:rgb(255,0,0);stop-opacity:1"/>
 </linearGradient>
 </defs>
 <ellipse fill="url(#grad1)" cx="200" cy="70" rx="85" ry="55"/>
 <text x="150" y="86" fill="green" font-family="Verdana" font-size="45">SVG</text>
</svg>

```

Looks like the following (in PyQt6)
![image|505x229](https://www.pythonguis.com/static/faq/todo/strange-error-in-pyqt6-not-rendering-radial-gradients/5BrBvbmvdhbtwXEeVuS3L0fZHrs.png)
I looked up some other radial gradients online, and some don't throw the error. Porting back the attributes of the elements that work I found that adding an r (radius) attribute to the radialGradient will mean it doesn't throw the error. The value necessary to give the expected gradient is 0.5
svg ```
 <radialGradient id="grad1" r="0.5">
  <stop offset="0%" stop-color="#ff0000" stop-opacity="1.0"/>
  <stop offset="50%" stop-color="#e70000" stop-opacity="1.0"/>
  <stop offset="100%" stop-color="#9e0000" stop-opacity="0.0"/>
  </radialGradient>

```

It makes some sense, in that a radial gradient doesn't really make sense without a radius.
The result with the above
![image|505x229](https://www.pythonguis.com/static/faq/todo/strange-error-in-pyqt6-not-rendering-radial-gradients/6BfYOCxex4A7KS5INvpLUjhioIY.png)
Final SVG code
svg ```
<svg width="400" height="150">
 <defs>
 <radialGradient id="grad1" r="0.5">
  <stop offset="0%" stop-color="#ff0000" stop-opacity="1.0"/>
  <stop offset="50%" stop-color="#e70000" stop-opacity="1.0"/>
  <stop offset="100%" stop-color="#9e0000" stop-opacity="0.0"/>
  </radialGradient>
 </defs>
 <ellipse fill="url(#grad1)" cx="200" cy="70" rx="85" ry="55"/>
 <text x="150" y="86" fill="green" font-family="Verdana" font-size="45">SVG</text>
</svg>

```

_PedanticHacker_
Wow, Martin, you nailed it! I just needed to pass the `r` attribute with the value of `0.5` and now it works perfectly in `PyQt6`. Thank you, thank you, thank you, you are truly a master hacker! :+1:
I have reported this "missing `r` attribute" bug in python-chess and the issue has already been fixed. However, the python-chess author (Niklas Fiekas) told me that if the `r` attribute is missing, it should default to `50%`, as specified [HERE](https://www.w3.org/TR/SVG11/pservers.html#RadialGradientElementRAttribute), saying `If the attribute is not specified, the effect is as if a value of '50%' were specified.`. I don't know what guys at Riverbank changed in PyQt6 to break this. :thinking:
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Strange error in PyQt6 (not rendering radial gradients)** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/strange-error-in-pyqt6-not-rendering-radial-gradients/Python books) on the subject. 
**Strange error in PyQt6 (not rendering radial gradients)** was published in [faq](https://www.pythonguis.com/faq/) on June 09, 2021 (updated September 02, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
