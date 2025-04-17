# Content from: https://www.pythonguis.com/faq/custom-widgets-without-a-gap-between-each-widget/

[](https://www.pythonguis.com/faq/custom-widgets-without-a-gap-between-each-widget/#menu)
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
# Custom widgets without a gap between each widget
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Pier-Justin_Mora | 2021-04-16 14:49:24 UTC | #1
Hello guys I have created a custom button and a custom bar. Both are created in a separate class. Because I want to extend it and use it like a construction plan by putting all the parts together. There is only one problem. This is also represented in the following image. The custom widgets should be lined up without a gap. How can I make it so that there is no space between the widgets?
![customWidget|690x387](https://www.pythonguis.com/static/faq/forum/custom-widgets-without-a-gap-between-each-widget/vMqb9pdW4YoaYTolAouTuWupwtM.jpeg)
Here the code:
python ```
from PyQt5 import QtWidgets, QtCore, QtGui, Qt
def clear(layout):
    if layout is not None:
      while layout.count():
        child = layout.takeAt(0)
        print(child)
        if child.widget() is not None:
          child.widget().setParent(None)
          # child.widget().deleteLater() ##also deletes the content of the file
        if child.layout() is not None:
          # child.layout().setParent(None)
          clear(child.layout())
class TopBar(QtWidgets.QWidget):
  back = QtCore.pyqtSignal()
  new = QtCore.pyqtSignal()
  clicked = QtCore.pyqtSignal(str)
  def __init__(self, name, icon_path, width, height, parent=None, **kwargs):
    super().__init__(parent)
    self.__color = QtGui.QColor("#215dde")
    self.__name = name
    self.__icon_path = icon_path
    self.action_lst = []
    self.__sig_lst = []
    self.actual_action = None
    self.__min_size = False
    self.text_size = 30
    self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)
    # self.setSizePolicy(
    #   # policy
    #   QSizePolicy.Fixed,
    #   QSizePolicy.Fixed
    #   # QSizePolicy.Maximum
    # )
    self.width = width
    self.height = height
    self.resize(self.width, self.height)

  def __del__(self):
    print('Object deleted.')
  def paintEvent(self, event):
    self.width = event.rect().width()
    painter = QtGui.QPainter()
    painter.begin(self)
    painter.setRenderHint(QtGui.QPainter.Antialiasing)
    fontText = QtGui.QFont(painter.font())
    fontText.setFamily("Arial")
    fontText.setPixelSize(self.text_size)
    painter.setFont(fontText)
    actual_width = 0
    bar_rect = QtCore.QRect(0, 0, self.width, self.height)
    painter.fillRect(bar_rect, QtGui.QBrush(QtGui.QColor(160, 166, 167, 255)))

    image = QtGui.QPixmap(self.__icon_path)
    text_height = self.height
    icon_rect = QtCore.QRect(text_height*0.1, text_height*0.1, text_height*0.9, text_height*0.9)
    painter.drawPixmap(icon_rect,image)
    actual_width = text_height*0.9

    size_text_line = QtCore.QSize(painter.fontMetrics().size(QtCore.Qt.TextSingleLine, self.__name))
    text_rect = QtCore.QRect(QtCore.QPoint(actual_width + text_height*1 , text_height-size_text_line.height()), size_text_line)
    painter.drawText(text_rect, QtCore.Qt.AlignBottom, self.__name)
    painter.end()

class Custom_Button(QtWidgets.QWidget):
  clicked = QtCore.pyqtSignal(bool)
  def __init__(self, icon_path, parent=None, **kwargs):
    # super().__init__()
    super(Custom_Button, self).__init__(parent)
    self.__color = QtGui.QColor("#215dde")
    self.setMouseTracking(True)
    self.__mouse_checked = False
    self.__mouse_over = False
    self.actual_action = None
    self.__pixmap = QtGui.QPixmap(icon_path)
    self.number_lines = 3
    self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)
    self.setMouseTracking(True)
  def sizeHint(self):
    return QtCore.QSize(150,100)
  def setText(self, text):
    self.__text = text
  def __del__(self):
    print('Button deleted.')

  def paintEvent(self, event):
    painter = QtGui.QPainter(self)
    painter.begin(self)
    painter.setRenderHint(QtGui.QPainter.Antialiasing)
    self.button_width = 80
    self.button_height = 80
    self.resize(self.button_width, self.button_height)
    painter.setBrush(QtGui.QColor(160, 166, 167, 255))
    painter.setPen(QtCore.Qt.NoPen)
    rect = QtCore.QRect(0, 0, self.width(), self.height())
    painter.drawRect(rect)
    if(self.__mouse_checked):
      painter.setBrush(QtGui.QColor("#c00000"))
      painter.setPen(QtGui.QColor("#c00000"))
      painter.drawRect(QtCore.QRect(0,0,self.width(), self.height()))
    for i in range(self.number_lines):
      actual_height = (i+1) * self.height() / ((self.number_lines - 1)*2)
      line = QtCore.QRect(self.width() *0.1 , actual_height, self.width() *0.8, 5)##QRect(QPoint(self.painter.device().width()*0.3 , actual_height), size_text_line)###QRect because to color the whole line not only the text or the area of the text
      painter.setPen(QtGui.QColor(71, 77, 78))
      painter.setBrush(QtGui.QColor(71, 77, 78))
      painter.drawRect(line)##drawLine(line)
    painter.end()

  def mousePressEvent(self, event):
    self.__mouse_checked = True
    self.update()

  def mouseReleaseEvent(self, event):
    self.__mouse_checked = False
    self.clicked.emit(True)
    self.update()

  def mouseMoveEvent(self, event):
    self.__mouse_over = True

  def leaveEvent(self, event):
    self.__mouse_over = False

class MainWindow(QtWidgets.QWidget):
  def __init__(self, parent=None, **kwargs):
    super(MainWindow, self).__init__(parent)
  # def __init__(self):
    super().__init__()
    self.ui()

  def ui(self):
    self.widgets()
    self.actions()
    self.layout()

  def widgets(self):
    self.__top_bar = TopBar("Text", "Icons/dots.png", self.width(), 80, self)
    self.__menu_button = Custom_Button("Icons/menu.png", self)
    self.__actual_widget = QtWidgets.QFrame()
    self.__first_widget = QtWidgets.QFrame()
  def actions(self):
    self.__menu_button.clicked.connect(self.menu_Pressed)
  def menu_Pressed(self):
    print("Pressed!!!")

  def Back(self):
    if(self.__last == "Start" or self.__last == "Calibration"):
      self.new_Content(self.__first_widget)
      self.new_Menu(self.__first_menu)
    else:
      self.menu_Action(self.__last)

  def new_Content(self, widget):
    if(self.__actual_widget != None):
      del self.__actual_widget
    self.__actual_widget=widget
    clear(self.__content_layout)
    self.__content_layout.addWidget(self.__actual_widget)

  def layout(self):
    self.__main_layout = QtWidgets.QVBoxLayout(self)
    self.__main_layout.setSpacing(0)
    self.__main_layout.setContentsMargins(0,0,0,0)
    self.__top_layout = QtWidgets.QHBoxLayout(self)
    self.__top_layout.setSpacing(0)
    self.__top_layout.setContentsMargins(0,0,0,0)

    self.__content_layout = QtWidgets.QHBoxLayout()
    self.__content_layout.addWidget(QtWidgets.QLabel(""))
    self.__actual_widget.setLayout(self.__content_layout)
    self.__first_widget = self.__actual_widget
    self.__top_layout.addWidget(self.__menu_button, 0, QtCore.Qt.AlignTop)
    self.__top_layout.addWidget(self.__top_bar)#, 0, QtCore.Qt.AlignTop)#, alignment=QtCore.Qt.AlignLeft)
    self.__top_layout.setContentsMargins(0,0,0,0)
    self.__top_layout.setSpacing(0)
    # self.__top_layout.addStretch()
    # self.__top_layout.
    self.__main_layout.addLayout(self.__top_layout)
    self.__main_layout.addWidget(self.__actual_widget)
    self.setLayout(self.__main_layout)



def main():
  app = QtWidgets.QApplication([])
  volume = MainWindow()
  volume.show()
  app.exec_()
if __name__ == '__main__':
  main()

```

martin | 2021-04-23 17:27:40 UTC | #2
Hey @Pier-Justin_Mora welcome to the forum!
To change how the resizing of the widgets works you need to use _size policies_ -- they tell Qt how the widget should scale to fill space around it (it at all) in layouts. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
What you're asking for on the layout is for it to expand horizontally, while remaining the same height vertically. That can be achieved with.
python ```
    self.setSizePolicy(Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Fixed)

```

In contrast the button needs to retain a fixed position at all times. You can do this with
python ```
    self.setSizePolicy(Qt.QSizePolicy.Fixed, Qt.QSizePolicy.Fixed)

```

In both cases, you need to specify a base size for the widget for these instructions to make any sense. To do this you can implement a `sizeHint` method on your classes, which returns the base size for the widgets, e.g.
python ```
  def sizeHint(self):
    return QtCore.QSize(80,80)

```

If you set this size on the button, that will be the exact _fixed_ size of the button. If you set this size on the bar, the height will be the exact _fixed_ height of the bar, while the width will be the minimum width (from which the bar will expand upwards).
There are a few other errors in the code, for example you are assigning to `self.width` (& height) which overrides the Qt `self.width()` method present on all widgets. You're also calling `.resize()` in the paint method -- I don't know what the intent of that is, but it's a bad idea. If that call does resize the button, it will trigger a re-draw.
Making these changes, the code works (alignment needs some work) 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
![Screenshot 2021-04-16 170619|690x131](https://www.pythonguis.com/static/faq/forum/custom-widgets-without-a-gap-between-each-widget/d2kim6qdacrVeqwNpfITyk2ea45.png)
The modified code of the two classes is copied below.
python ```

class TopBar(QtWidgets.QWidget):
  back = QtCore.pyqtSignal()
  new = QtCore.pyqtSignal()
  clicked = QtCore.pyqtSignal(str)
  def __init__(self, name, icon_path, width, height, parent=None, **kwargs):
    # super().__init__()
    super(TopBar, self).__init__(parent)
    self.__color = QtGui.QColor("#215dde")
    self.__name = name
    self.__icon_path = icon_path
    self.action_lst = []
    self.__sig_lst = []
    self.actual_action = None
    self.__min_size = False
    self.text_size = 30
    self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)
    self.setSizePolicy(Qt.QSizePolicy.Expanding, Qt.QSizePolicy.Fixed)
  def sizeHint(self):
    return QtCore.QSize(80,80)
  def __del__(self):
    print('Object deleted.')
  def paintEvent(self, event):
    width = event.rect().width()
    painter = QtGui.QPainter(self)
    painter.begin(self)
    painter.setRenderHint(QtGui.QPainter.Antialiasing)
    fontText = QtGui.QFont(painter.font())
    fontText.setFamily("Arial")
    fontText.setPixelSize(self.text_size)
    painter.setFont(fontText)
    actual_width = 0
    bar_rect = QtCore.QRect(0, 0, width, self.height())
    painter.fillRect(bar_rect, QtGui.QBrush(QtGui.QColor(160, 166, 167, 255)))

    image = QtGui.QPixmap(self.__icon_path)
    text_height = self.height()
    icon_rect = QtCore.QRect(text_height*0.1, text_height*0.1, text_height*0.9, text_height*0.9)
    painter.drawPixmap(icon_rect,image)
    actual_width = text_height*0.9

    size_text_line = QtCore.QSize(painter.fontMetrics().size(QtCore.Qt.TextSingleLine, self.__name))
    text_rect = QtCore.QRect(QtCore.QPoint(actual_width + text_height*1 , text_height-size_text_line.height()), size_text_line)
    painter.drawText(text_rect, QtCore.Qt.AlignBottom, self.__name)
    painter.end()

class Custom_Button(QtWidgets.QWidget):
  clicked = QtCore.pyqtSignal(bool)
  def __init__(self, icon_path, parent=None, **kwargs):
    # super().__init__()
    super(Custom_Button, self).__init__(parent)
    self.__color = QtGui.QColor("#215dde")
    self.setMouseTracking(True)
    self.__mouse_checked = False
    self.__mouse_over = False
    self.actual_action = None
    self.__pixmap = QtGui.QPixmap(icon_path)
    self.number_lines = 3
    self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)
    self.setMouseTracking(True)
    self.setSizePolicy(Qt.QSizePolicy.Fixed, Qt.QSizePolicy.Fixed)
  def sizeHint(self):
    return QtCore.QSize(80,80)
  def setText(self, text):
    self.__text = text
  def __del__(self):
    print('Button deleted.')

  def paintEvent(self, event):
    painter = QtGui.QPainter(self)
    painter.begin(self)
    painter.setRenderHint(QtGui.QPainter.Antialiasing)
    painter.setBrush(QtGui.QColor(160, 166, 167, 255))
    painter.setPen(QtCore.Qt.NoPen)
    rect = QtCore.QRect(0, 0, self.width(), self.height())
    painter.drawRect(rect)
    if(self.__mouse_checked):
      painter.setBrush(QtGui.QColor("#c00000"))
      painter.setPen(QtGui.QColor("#c00000"))
      painter.drawRect(QtCore.QRect(0,0,self.width(), self.height()))
    for i in range(self.number_lines):
      actual_height = (i+1) * self.height() / ((self.number_lines - 1)*2)
      line = QtCore.QRect(self.width() *0.1 , actual_height, self.width() *0.8, 5)##QRect(QPoint(self.painter.device().width()*0.3 , actual_height), size_text_line)###QRect because to color the whole line not only the text or the area of the text
      painter.setPen(QtGui.QColor(71, 77, 78))
      painter.setBrush(QtGui.QColor(71, 77, 78))
      painter.drawRect(line)##drawLine(line)
    painter.end()

  def mousePressEvent(self, event):
    self.__mouse_checked = True
    self.update()

  def mouseReleaseEvent(self, event):
    self.__mouse_checked = False
    self.clicked.emit(True)
    self.update()

  def mouseMoveEvent(self, event):
    self.__mouse_over = True

  def leaveEvent(self, event):
    self.__mouse_over = False

```

Pier-Justin_Mora | 2021-04-23 17:28:40 UTC | #3
Hi @martin,
Thank you very much for your quick and detailed answer. You helped me a lot.
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Custom widgets without a gap between each widget** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/custom-widgets-without-a-gap-between-each-widget/Python books) on the subject. 
**Custom widgets without a gap between each widget** was published in [faq](https://www.pythonguis.com/faq/) on April 15, 2021 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
