# Content from: https://www.pythonguis.com/faq/drawing-dots-on-top-of-image-upon-mouse-clicks/

[](https://www.pythonguis.com/faq/drawing-dots-on-top-of-image-upon-mouse-clicks/#menu)
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
# Drawing dots on top of image upon mouse clicks
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
guidoasc4064 | 2020-05-16 12:43:57 UTC | #1
Hi all! I'm very new to PyQt5, so bare with me if the question has an obvious answer. Some context: I'm trying to develop a GUI that will let users open an image (using opencv; the image then goes onto a QLabel) that features a person. The GUI then allows the user to digitize (and save) the positions of the person's joints (ankles, knees, elbows, etc). Ideally, the GUI would function like this. First, the user opens an image by pressing CTRL+o. Then, the image gets displayed, and the user has to select one of the pushButtons with the joint names (these appear below the QLabel with the image), each corresponding to a different joint. When a joint button is selected, if the user clicks on a point on the image the coordinates of that point are saved in a dictionary under the name of the joint that was selected, and a dot should appear on that pixel, to indicate that that's the pixel where the joint was digitised (so the user can quickly see if he/she made a mistake). The part I got stuck on is this: when the user clicks on a joint, I want a green (if it was a left mouse click, representing a joint that is visible) or yellow (if it was a right mouse click, representing a joint that was occluded) dot to appear where the user clicked. I followed the code given in the brilliantly explained tutorial at <https://www.pythonguis.com/courses/custom-widgets/bitmap-graphics/>, but it did not work for me: it doesn't give any errors, and the draw_something method does get called whenever the user clicks (I checked this using print statements), but no dots appear. My hunch is that the dots are indeed being drawn, only they are being drawn UNDER the image. Any thoughts? Below is my code: I apologise if it's a bit long and articulated, I hope you can follow my line of thought. Thanks!
python ```
import cv2
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QFont, QColor
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow
from PyQt5.uic import loadUi
import json as serializer
import csv
# track movements of the mouse to display a (x,y) label next to it
class MouseTracker(QtCore.QObject):
  positionChanged = QtCore.pyqtSignal(QtCore.QPoint)
  def __init__(self, widget):
    super().__init__(widget)
    self._widget = widget
    self.widget.setMouseTracking(True)
    self.widget.installEventFilter(self)
  @property
  def widget(self):
    return self._widget
  def eventFilter(self, o, e):
    if o is self.widget and e.type() == QtCore.QEvent.MouseMove:
      self.positionChanged.emit(e.pos())
    return super().eventFilter(o, e)
# main window
class MyMainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    loadUi('load_and_save2.ui',self)
    self.image=None
    self.actionOpen.triggered.connect(self.loadTriggered)
    self.actionExit.triggered.connect(self.close)
    self.imgLabel.resize(1920, 844) # specific resolution (DO NOT CHANGE)
    self.joint_selected = None
    self.buttonLeft_ankle.clicked.connect(lambda: self.jointSelected('Left_ankle'))
    self.buttonRight_ankle.clicked.connect(lambda: self.jointSelected('Right_ankle'))
    self.buttonLeft_knee.clicked.connect(lambda: self.jointSelected('Left_knee'))
    self.buttonRight_knee.clicked.connect(lambda: self.jointSelected('Right_knee'))
    self.buttonLeft_hip.clicked.connect(lambda: self.jointSelected('Left_hip'))
    self.buttonRight_hip.clicked.connect(lambda: self.jointSelected('Right_hip'))
    self.buttonLeft_shoulder.clicked.connect(lambda: self.jointSelected('Left_shoulder'))
    self.buttonRight_shoulder.clicked.connect(lambda: self.jointSelected('Right_shoulder'))
    self.buttonLeft_elbow.clicked.connect(lambda: self.jointSelected('Left_elbow'))
    self.buttonRight_elbow.clicked.connect(lambda: self.jointSelected('Right_elbow'))
    self.buttonLeft_wrist.clicked.connect(lambda: self.jointSelected('Left_wrist'))
    self.buttonRight_wrist.clicked.connect(lambda: self.jointSelected('Right_wrist'))
    self.joints = {}
    tracker = MouseTracker(self.imgLabel)
    tracker.positionChanged.connect(self.on_positionChanged)
    self.label_position = QtWidgets.QLabel(
      self.imgLabel, alignment=QtCore.Qt.AlignCenter
    )
  def jointSelected(self, joint):
    self.joint_selected = joint
  # detects if left or right mouse was clicked
  def mousePressEvent(self, event):
    # on left mouse click, it prints to screen the coordinates and 0
    if event.button() == QtCore.Qt.LeftButton:
      self.lastLeftPoint = self.imgLabel.mapFromParent(event.pos())
      if self.joint_selected is not None:
        self.joints[self.joint_selected] = [self.lastLeftPoint.x(), self.lastLeftPoint.y(), 1]
        # turn green the background of corresponding joint button
        self.changeButtonBackground(joint_selected=self.joint_selected,
                      visible=1)
        self.draw_something(self.lastLeftPoint.x(),
                  self.lastLeftPoint.y(),
                  visible=1)
    # on right mouse click, it prints to screen the coordinates and 1
    elif event.button() == QtCore.Qt.RightButton:
      self.lastRightPoint = self.imgLabel.mapFromParent(event.pos())
      if self.joint_selected is not None:
        self.joints[self.joint_selected] = [self.lastLeftPoint.x(), self.lastLeftPoint.y(), 0]
        # turn yellow the background of corresponding joint button
        self.changeButtonBackground(joint_selected=self.joint_selected,
                      visible=0)
        self.draw_something(self.lastLeftPoint.x(),
                  self.lastLeftPoint.y(),
                  visible=0)
  def changeButtonBackground(self, joint_selected, visible):
    button_name = 'button' + joint_selected
    if visible:
      getattr(self, button_name).setStyleSheet("background-color:green")
    elif not visible:
      getattr(self, button_name).setStyleSheet("background-color:yellow")
  def draw_something(self, x, y, visible):
    print(f'About to draw a dot (visible={visible})')
    painter = QtGui.QPainter(self.imgLabel.pixmap())
    pen = QtGui.QPen()
    pen.setWidth(40)
    if visible:
      pen.setColor(QtGui.QColor('green'))
    else:
      pen.setColor(QtGui.QColor('yellow'))
    painter.setPen(pen)
    painter.drawPoint(x, y)
    painter.end()
    print('Dot drawn')
  # reposition the (x,y) label as the mouse moves
  # make the font of the label bold and green
  @QtCore.pyqtSlot(QtCore.QPoint)
  def on_positionChanged(self, pos):
    delta = QtCore.QPoint(30, -15)
    self.label_position.show()
    self.label_position.move(pos + delta)
    self.label_position.setText(f'{self.joint_selected}')
    myFont=QtGui.QFont('Arial', 12)
    myFont.setBold(True)
    self.label_position.setFont(myFont)
    self.label_position.adjustSize()
    color = QtGui.QColor(0,128,0)
    values = "{r}, {g}, {b}".format(r = color.red(),
                    g = color.green(),
                    b = color.blue()
                    )
    self.label_position.setStyleSheet("QLabel {color:rgb("+values+")}")
    #self.label_position.setBackground(QtGui.QColor('sea green'))
  # user wants to open an image -> open it from a user-selected folder
  def loadTriggered(self):
    fname,filter = QFileDialog.getOpenFileName(self, 'Open File','C:\\',"Image Files (*.jpg)")
    if fname:
      self.loadImage(fname)
    else:
      print('Invalid Image')
  # load the selected image, using opencv
  def loadImage(self,fname):
    self.image=cv2.imread(fname,cv2.IMREAD_COLOR)
    self.displayImage()
  # display loaded image on main window
  def displayImage(self):
    qformat=QImage.Format_Indexed8
    if len(self.image.shape)==3: # rows[0],cols[1],channels[2]
      if(self.image.shape[2])==4:
        qformat=QImage.Format_RGBA8888
      else:
        qformat=QImage.Format_RGB888
    img=QImage(self.image,self.image.shape[1],self.image.shape[0],self.image.strides[0],qformat)
    # BGR > RGB
    img= img.rgbSwapped()
    self.imgLabel.setPixmap(QPixmap.fromImage(img))
    self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
if __name__=='__main__':
  import sys
  app=QApplication(sys.argv)
  window=MyMainWindow()
  window.setWindowTitle('Load and Save Images')
  window.showMaximized()
  sys.exit(app.exec_())

```

martin | 2020-05-17 09:01:12 UTC | #2
Hey @guidoasc4064 welcome to the forum :slight_smile:
I can't be 100% sure without testing it (can you also attach your ui file?) but looking at the code I think the issue is that you're drawing to the wrong pixmap. In `draw_something` you have e.g.
python ```
    painter = QtGui.QPainter(self.imgLabel.pixmap())

```

But if I understand you right you want to draw to the actual image, which is in `self.image` ? If that's right the line should be --
python ```
    painter = QtGui.QPainter(self.image.pixmap())

```

Hope that helps!
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Drawing dots on top of image upon mouse clicks** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/drawing-dots-on-top-of-image-upon-mouse-clicks/Python books) on the subject. 
**Drawing dots on top of image upon mouse clicks** was published in [faq](https://www.pythonguis.com/faq/) on May 16, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
