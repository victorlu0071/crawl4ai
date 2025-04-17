# Content from: https://www.pythonguis.com/faq/use-mouse-drag-to-change-the-width-of-a-rectangle/

[](https://www.pythonguis.com/faq/use-mouse-drag-to-change-the-width-of-a-rectangle/#menu)
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
# Use mouse drag to change the width of a rectangle?
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
esdairim | 2020-11-12 21:00:18 UTC | #1
Hello everyone, I got this code that helps me draw a rectangle, I'd like to be able to drag the left and right sides of the rectangle to adjust the width of the rectangle, make the rectangle behave in a way similar to how you crop an image on most photo editing software, where you draw the initial area but you have the possibility to adjust the width afterwards to get the crop you want. Thank you for your help. the code I have so far:
python ```
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyWidget(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(30,30,600,400)
    self.begin = QPoint()
    self.end = QPoint()
    self.show()
  def paintEvent(self, event):
    qp = QPainter(self)
    br = QBrush(QColor(100, 10, 10, 40))
    qp.setBrush(br)
    qp.drawRect(QRect(self.begin, self.end))
  def mousePressEvent(self, event):
    self.begin = event.pos()
    self.end = event.pos()
    # print(f"press begin {self.begin}")
    # print(f"press end  {self.end}")
    self.update()
  def mouseMoveEvent(self, event):
    self.end = event.pos()
    self.update()
  def mouseReleaseEvent(self, event):
    #self.begin = event.pos()
    self.end = event.pos()
    #self.update()
    print(f"begin {self.begin}")
    print(f"end  {self.end}")

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MyWidget()
  window.show()
  app.aboutToQuit.connect(app.deleteLater)
  sys.exit(app.exec_())

```

Salem_Bream | 2020-12-04 19:08:15 UTC | #2
Hi, maybe it's a late response, but hopefully it will benefit someone.
I will build on your code, will try to make my code very explicit, to be easy to understand.
Next, you will find 2 code blocks:
  1. the code with resize working as intended.
  2. same as the first one, but added the visual feed back part, to make it feel professional :D .


# Final Result:
![image|545x379, 75%](https://www.pythonguis.com/static/faq/forum/use-mouse-drag-to-change-the-width-of-a-rectangle/2KOLZr7y72dvpDrcUpiZvqew9FK.png)
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
## -----
# First Block
python ```
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

FREE_STATE = 1
BUILDING_SQUARE = 2
BEGIN_SIDE_EDIT = 3
END_SIDE_EDIT = 4

class MyWidget(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(30, 30, 600, 400)
    self.begin = QPoint()
    self.end = QPoint()
    self.state = FREE_STATE
  def paintEvent(self, event):
    qp = QPainter(self)
    br = QBrush(QColor(100, 10, 10, 40))
    qp.setBrush(br)
    qp.drawRect(QRect(self.begin, self.end))
  def mousePressEvent(self, event):
    if not self.begin.isNull() and not self.end.isNull():
      p = event.pos()
      y1, y2 = sorted([self.begin.y(), self.end.y()])
      if y1 <= p.y() <= y2:
        # 3 resolution, more easy to pick than 1px
        if abs(self.begin.x() - p.x()) <= 3:
          self.state = BEGIN_SIDE_EDIT
          return
        elif abs(self.end.x() - p.x()) <= 3:
          self.state = END_SIDE_EDIT
          return
    self.state = BUILDING_SQUARE
    self.begin = event.pos()
    self.end = event.pos()
    self.update()
  def applye_event(self, event):
    if self.state == BUILDING_SQUARE:
      self.end = event.pos()
    elif self.state == BEGIN_SIDE_EDIT:
      self.begin.setX(event.x())
    elif self.state == END_SIDE_EDIT:
      self.end.setX(event.x())
  def mouseMoveEvent(self, event):
    self.applye_event(event)
    self.update()
  def mouseReleaseEvent(self, event):
    self.applye_event(event)
    self.state = FREE_STATE

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MyWidget()
  window.show()
  app.aboutToQuit.connect(app.deleteLater)
  sys.exit(app.exec_())

```

## -----
# Second Block
python ```
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

FREE_STATE = 1
BUILDING_SQUARE = 2
BEGIN_SIDE_EDIT = 3
END_SIDE_EDIT = 4

CURSOR_ON_BEGIN_SIDE = 1
CURSOR_ON_END_SIDE = 2

class MyWidget(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(30, 30, 600, 400)
    self.begin = QPoint()
    self.end = QPoint()
    self.state = FREE_STATE
    self.setMouseTracking(True)
    self.free_cursor_on_side = 0
  def paintEvent(self, event):
    qp = QPainter(self)
    br = QBrush(QColor(100, 10, 10, 40))
    qp.setBrush(br)
    qp.drawRect(QRect(self.begin, self.end))
    if not self.free_cursor_on_side:
      return
    qp.setPen(QPen(Qt.black, 5, Qt.DashLine))
    if self.free_cursor_on_side == CURSOR_ON_BEGIN_SIDE:
      end = QPoint(self.end)
      end.setX(self.begin.x())
      qp.drawLine(self.begin, end)
    elif self.free_cursor_on_side == CURSOR_ON_END_SIDE:
      begin = QPoint(self.begin)
      begin.setX(self.end.x())
      qp.drawLine(self.end, begin)
  def cursor_on_side(self, e_pos) -> int:
    if not self.begin.isNull() and not self.end.isNull():
      y1, y2 = sorted([self.begin.y(), self.end.y()])
      if y1 <= e_pos.y() <= y2:
        # 5 resolution, more easy to pick than 1px
        if abs(self.begin.x() - e_pos.x()) <= 5:
          return CURSOR_ON_BEGIN_SIDE
        elif abs(self.end.x() - e_pos.x()) <= 5:
          return CURSOR_ON_END_SIDE
    return 0
  def mousePressEvent(self, event):
    side = self.cursor_on_side(event.pos())
    if side == CURSOR_ON_BEGIN_SIDE:
      self.state = BEGIN_SIDE_EDIT
    elif side == CURSOR_ON_END_SIDE:
      self.state = END_SIDE_EDIT
    else:
      self.state = BUILDING_SQUARE
      self.begin = event.pos()
      self.end = event.pos()
      self.update()
  def applye_event(self, event):
    if self.state == BUILDING_SQUARE:
      self.end = event.pos()
    elif self.state == BEGIN_SIDE_EDIT:
      self.begin.setX(event.x())
    elif self.state == END_SIDE_EDIT:
      self.end.setX(event.x())
  def mouseMoveEvent(self, event):
    if self.state == FREE_STATE:
      self.free_cursor_on_side = self.cursor_on_side(event.pos())
      if self.free_cursor_on_side:
        self.setCursor(Qt.SizeHorCursor)
      else:
        self.unsetCursor()
      self.update()
    else:
      self.applye_event(event)
      self.update()
  def mouseReleaseEvent(self, event):
    self.applye_event(event)
    self.state = FREE_STATE

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MyWidget()
  window.show()
  app.aboutToQuit.connect(app.deleteLater)
  sys.exit(app.exec_())

```

regards.
esdairim | 2020-12-04 19:08:09 UTC | #3 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
thank you very much for this man
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Use mouse drag to change the width of a rectangle?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/use-mouse-drag-to-change-the-width-of-a-rectangle/Python books) on the subject. 
**Use mouse drag to change the width of a rectangle?** was published in [faq](https://www.pythonguis.com/faq/) on November 12, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
