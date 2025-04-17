# Content from: https://www.pythonguis.com/faq/avoid-gray-background-for-selected-icons/

[](https://www.pythonguis.com/faq/avoid-gray-background-for-selected-icons/#menu)
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
# Avoid gray background for selected icons
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
ERIC_HUYGEN | 2021-04-23 18:38:21 UTC | #1
Hi,
I have a question about a checkable QAction with two custom icons. In a toolbar, I have a number of actions/icon that are checkable. The actions have two states and the icons are different for each state. The code looks like this:
python ```
  switch_on_pix = QPixmap(str(get_resource(":/icons/switch-on.svg")))
  switch_off_pix = QPixmap(str(get_resource(":/icons/switch-off.svg")))
  switch_icon = QIcon()
  switch_icon.addPixmap(switch_on_pix, QIcon.Normal, QIcon.On)
  switch_icon.addPixmap(switch_off_pix, QIcon.Normal, QIcon.Off)
  self.control_action = QAction(switch_icon, "Control", self)
  self.control_action.setToolTip("Control ON/OFF")
  self.control_action.setCheckable(True)
  self.control_action.triggered.connect(partial(self.onClick, switch_icon))

```

![image|250x50](https://www.pythonguis.com/static/faq/forum/avoid-gray-background-for-selected-icons/qkZKwN2PTuTDENpSBcQjZ6oRbTR.png) ![image|250x50](https://www.pythonguis.com/static/faq/forum/avoid-gray-background-for-selected-icons/A5VVbruXD1hkW0j7ojlPO6CJ7IR.png)
The two screenshots above show the 'on' switch in the selected state and the 'off' switch not selected. The selected state has a gray background which is added by Qt. The question is if there is a way to get rid of the gray background because this doesn't bring any added value in this case.
Thanks, Rik
ERIC_HUYGEN | 2021-05-11 21:05:30 UTC | #2 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
I have solved this issue in the mean time. I created my own button, ToggleButton. This button inherits from QCheckBox and implements it's own paintEvent() method. The ToggleButton can take either two or three states and an additional 'disabled' state. For each of the states you will have to provide an icon, an SVG file. When you run the example code, it opens a small window as shown below. When you click the button, it toggles between the different states and changes the icon to the current state. When you press the 'disable' button, the icon corresponding to the disabled state will be painted and the icon will also be disabled. No disturbing background will be drawn.
Enjoy!
[details="Click here to see the code..."] 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
python ```
import sys
from pathlib import Path
from typing import Union
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QPushButton
BUTTON_DISABLED = 0
BUTTON_SELECTED = 1
BUTTON_NOT_SELECTED = 2
BUTTON_NO_CHANGE = 3
BUTTON_ACTIONED = 4

class ToggleButton(QCheckBox):
  def __init__(
      self,
      width: int = 32,
      height: int = 32,
      name: str = None,
      status_tip: str = None,
      selected: Union[str, Path] = None,
      not_selected: Union[str, Path] = None,
      no_change: Union[str, Path] = None,
      disabled: Union[str, Path] = None,
      tristate: bool = False
  ):
    super().__init__()
    self.setFixedSize(width, height)
    self.setCursor(Qt.PointingHandCursor)
    self.setTristate(tristate)
    self.setText(name)
    self.setStatusTip(status_tip)
    self.status_tip = status_tip
    self.max_states = 3 if tristate else 2
    self.button_selected = selected
    self.button_not_selected = not_selected
    self.no_change = no_change
    self.button_disabled = disabled
    self.resource = {
      BUTTON_DISABLED: self.button_disabled,
      BUTTON_SELECTED: self.button_selected,
      BUTTON_NOT_SELECTED: self.button_not_selected,
      BUTTON_NO_CHANGE: self.no_change,
    }
    self.state = BUTTON_SELECTED
    self.disabled = False
    self.clicked.connect(self.handle_clicked)
  def handle_clicked(self):
    self.state = 1 if self.state == self.max_states else self.state + 1
    self.repaint()
  def setDisabled(self, flag: bool = True):
    self.disabled = flag
    super().setDisabled(flag)
    self.setStatusTip(f"{self.status_tip or ''} {'[DISABLED]' if flag else ''}")
  def disable(self):
    self.setDisabled(True)
  def enable(self):
    self.setDisabled(False)
  def is_selected(self):
    return self.state == BUTTON_SELECTED
  def set_selected(self, on: bool = True):
    self.state = BUTTON_SELECTED if on else BUTTON_NOT_SELECTED
    self.repaint()
  def hitButton(self, pos: QPoint):
    return self.contentsRect().contains(pos)
  def paintEvent(self, *args, **kwargs):
    painter = QPainter(self)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setPen(Qt.NoPen)
    self.drawCustomWidget(painter)
    painter.end()
  def drawCustomWidget(self, painter):
    renderer = QSvgRenderer()
    resource = self.resource[self.state if not self.disabled else BUTTON_DISABLED]
    renderer.load(resource)
    renderer.render(painter)

if __name__ == "__main__":
  from PyQt5.QtWidgets import QMainWindow
  from PyQt5.QtWidgets import QFrame
  from PyQt5.QtWidgets import QVBoxLayout

  class MainWindow(QMainWindow):
    def __init__(self):
      super().__init__()
      self.resize(200, 200)
      self.container = QFrame()
      self.container.setObjectName("Container")
      self.layout = QVBoxLayout()
      button_selected = "cs-connected.svg"
      button_not_selected = "cs-not-connected.svg"
      button_no_change = "cs-connected-alert.svg"
      button_disabled = "cs-connected-disabled.svg"
      self.toggle = ToggleButton(
        name="CS-CONNECT",
        status_tip="connect-disconnect hexapod control server",
        selected=button_selected,
        not_selected=button_not_selected,
        no_change=button_no_change,
        disabled=button_disabled,
        tristate=True,
      )
      self.layout.addWidget(self.toggle, Qt.AlignCenter, Qt.AlignCenter)
      self.layout.addWidget(pb := QPushButton("disable"))
      self.container.setLayout(self.layout)
      self.setCentralWidget(self.container)
      self.pb = pb
      self.pb.setCheckable(True)
      self.pb.clicked.connect(self.toggle_disable)
      self.toggle.clicked.connect(self.toggle_clicked)
      self.statusBar()
    def toggle_disable(self, checked: bool):
      self.toggle.disable() if checked else self.toggle.enable()
      self.pb.setText("enable" if checked else "disable")
    def toggle_clicked(self, *args, **kwargs):
      sender = self.sender()
      print(f"clicked: {args=}, {kwargs=}")
      print(f"     {sender.state=}")
      print(f"     {sender.text()=}")

  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

```

[/details]
![image|312x340](https://www.pythonguis.com/static/faq/forum/avoid-gray-background-for-selected-icons/cl5CSFgRIO0XDvvotNqiAbQzeGA.png) ![image|312x340](https://www.pythonguis.com/static/faq/forum/avoid-gray-background-for-selected-icons/lvKcOxXQxw6v7vxrFH2reL5n3Bg.png) ![image|312x340](https://www.pythonguis.com/static/faq/forum/avoid-gray-background-for-selected-icons/iAjiaubuf9csMGHDnPz2wZyfQtW.png) ![image|312x340](https://www.pythonguis.com/static/faq/forum/avoid-gray-background-for-selected-icons/kypypUz1l4UPVHBq7c6dE9DFeH.png)
The code is based on this YouTube tutorial [https://www.youtube.com/watch?v=NnJFi285s3M].
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Avoid gray background for selected icons** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/avoid-gray-background-for-selected-icons/Python books) on the subject. 
**Avoid gray background for selected icons** was published in [faq](https://www.pythonguis.com/faq/) on April 23, 2021 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
