# Content from: https://www.pythonguis.com/faq/unable-to-implement-gui-interface-to-face-recognition-script-in-pyqt5/

[](https://www.pythonguis.com/faq/unable-to-implement-gui-interface-to-face-recognition-script-in-pyqt5/#menu)
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
# Unable to implement GUI interface to Face Recognition script in PyQt5
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
tharabhuddha11695 | 2022-08-09 11:18:47 UTC | #1
Hello, I am trying to make a face recognition app with pyqt5, I have also tried tkinter but I felt pyqt5 has good looking GUI, I am able to make the basic looking interface using the QtDesigner app you can see here. What I want to do is in these steps.
![Face-App-GUI|510x500](https://www.pythonguis.com/static/faq/forum/unable-to-implement-gui-interface-to-face-recognition-script-in-pyqt5/c7l3vFFsxiuYBhFAZ2lK2DO2S5L.png)
python ```
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap,QIcon
from face import compare_images

class Ui_Main(object):
  def setupUi(self, Main):
      Main.setObjectName("MainWindow")
      Main.resize(663, 614)
      sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
      sizePolicy.setHorizontalStretch(0)
      sizePolicy.setVerticalStretch(0)
      sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
      Main.setSizePolicy(sizePolicy)
      Main.setMaximumSize(QtCore.QSize(8000, 4200))
      icon = QtGui.QIcon()
      icon.addPixmap(QtGui.QPixmap("../.designer/backup/img.png"), QtGui.QIcon.Normal)
      Main.setWindowIcon(icon)
      Main.setStyleSheet("")
      self.label = QtWidgets.QLabel(Main)
      self.label.setGeometry(QtCore.QRect(240, 10, 231, 21))
      font = QtGui.QFont()
      font.setPointSize(15)
      font.setBold(True)
      font.setWeight(75)
      self.label.setFont(font)
      self.label.setObjectName("label")
      self.Compare_button = QtWidgets.QPushButton(Main)
      self.Compare_button.setGeometry(QtCore.QRect(290, 390, 89, 25))
      self.Compare_button.setObjectName("Compare_button")
      self.Compare_button.clicked.connect(self.compare_data)
      self.label_3 = QtWidgets.QLabel(Main)
      self.label_3.setGeometry(QtCore.QRect(100, 490, 71, 21))
      font = QtGui.QFont()
      font.setBold(True)
      font.setWeight(75)
      self.label_3.setFont(font)
      self.label_3.setObjectName("label_3")
      self.Uploaded_Image_1 = QtWidgets.QFrame(Main)
      self.Uploaded_Image_1.setGeometry(QtCore.QRect(90, 60, 171, 241))
      self.Uploaded_Image_1.setStyleSheet("border: 3px solid black")
      self.Uploaded_Image_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
      self.Uploaded_Image_1.setFrameShadow(QtWidgets.QFrame.Raised)
      self.Uploaded_Image_1.setObjectName("Uploaded_Image_1")
      self.Uploaded_Image_2 = QtWidgets.QFrame(Main)
      self.Uploaded_Image_2.setGeometry(QtCore.QRect(410, 60, 171, 241))
      self.Uploaded_Image_2.setStyleSheet("border: 3px solid black;")
      self.Uploaded_Image_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
      self.Uploaded_Image_2.setFrameShadow(QtWidgets.QFrame.Raised)
      self.Uploaded_Image_2.setObjectName("Uploaded_Image_2")
      self.lineEdit = QtWidgets.QLineEdit(Main)
      self.lineEdit.setGeometry(QtCore.QRect(180, 490, 301, 25))
      self.lineEdit.setObjectName("lineEdit")
      self.Image_1_button = QtWidgets.QPushButton(Main)
      self.Image_1_button.setGeometry(QtCore.QRect(110, 330, 121, 31))
      self.Image_1_button.setStyleSheet("")
      self.Image_1_button.setObjectName("Image_1")
      self.Image_1_button.clicked.connect(self.upload_image_1)
      self.Image_2_button = QtWidgets.QPushButton(Main)
      self.Image_2_button.setGeometry(QtCore.QRect(440, 330, 121, 31))
      self.Image_2_button.setObjectName("Image_2")
      self.Image_1_button.clicked.connect(self.upload_image_2)
      self.retranslateUi(Main)
      QtCore.QMetaObject.connectSlotsByName(Main)
  def upload_image_1(self,Main):
    imagePath1, _ = QFileDialog.getOpenFileName()
    pixmap1 = QPixmap(imagePath1)
    self.Uploaded_Image_1.resize(self, 300, 200)
    self.Uploaded_Image_1.setFrameShape(pixmap1)

  def upload_image_2(self,Main):
    imagePath2, _ = QFileDialog.getOpenFileName()
    pixmap2 = QPixmap(imagePath2)
    self.Uploaded_Image_1.resize(self, 300, 200)
    self.Uploaded_Image_1.setFrameShape(pixmap2)
  def compare_data(self,Main):
    result = compare_images()
    if result == 'Match found':
      self.lineEdit.setText('Match Found')
    elif result == 'No Match found':
      self.lineEdit.setText('No Match Found')
    else:
      self.lineEdit.setText('Error Fetching Data')
  def retranslateUi(self, Main):
    _translate = QtCore.QCoreApplication.translate
    Main.setWindowTitle(_translate("MainWindow", "face app"))
    self.label.setText(_translate("MainWindow", "Face Recognition"))
    self.Compare_button.setText(_translate("MainWindow", "Compare"))
    self.label_3.setText(_translate("MainWindow", "Result -"))
    self.Image_1_button.setText(_translate("MainWindow", "Upload Image 1"))
    self.Image_2_button.setText(_translate("MainWindow", "Upload Image 2"))
if __name__ == '__main__':
   import sys
  app = QtWidgets.QApplication(sys.argv)
  Main = QtWidgets.QMainWindow()
  ui = Ui_Main()
  ui.setupUi(Main)
  Main.show()
  app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
  sys.exit(app.exec())

```

[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Unable to implement GUI interface to Face Recognition script in PyQt5** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/unable-to-implement-gui-interface-to-face-recognition-script-in-pyqt5/Python books) on the subject. 
**Unable to implement GUI interface to Face Recognition script in PyQt5** was published in [faq](https://www.pythonguis.com/faq/) on July 09, 2021 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [qtdesigner](https://www.pythonguis.com/topics/qtdesigner/) [ packaging](https://www.pythonguis.com/topics/packaging/) [python38](https://www.pythonguis.com/topics/python38/) [ pyqt5-packaging](https://www.pythonguis.com/topics/pyqt5-packaging/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
