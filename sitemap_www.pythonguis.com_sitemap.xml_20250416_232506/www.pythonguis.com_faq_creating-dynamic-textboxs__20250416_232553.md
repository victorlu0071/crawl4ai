# Content from: https://www.pythonguis.com/faq/creating-dynamic-textboxs/

[](https://www.pythonguis.com/faq/creating-dynamic-textboxs/#menu)
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
# Creating dynamic TextBox's
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Hamid_Rezaie | 2020-06-17 13:47:19 UTC | #1
Hey guys, I have the following MUC, which produces the following GUI (see Fig: left GUI).
Depending on how many images are selected, TextBoxes appear dynamically. The name of the image appears in these text boxes (see Fig: middle GUI).
Now everything is finde but i want to extend the GUI so that it extracts important parameters from the imagename and prints them right next to the TextBox containing the name in two more TextBoxes (because there are two parameters (height and width)). I know how to extract the parameters, it works. But I do not know how to dynamically add two more TextBoxes horizontally. Then i use the Parameter to calculate the area. But I can't change the MUC so that it dynamically adds the desired TextBox's. It should look like the next image. At first three TextBox's in horizontal position. And if i select for example 3 Images, then in the next two rows should appear the same three TextBox's with particular imagename and parameters (see Fig 3: right GUI).
![3|690x175](https://www.pythonguis.com/static/faq/forum/creating-dynamic-textboxs/sMik23HEDTpcrXjbHVFbUPoX9qv.png)
Here you can see the MUC:
python ```
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QStyleFactory, QMainWindow, QWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtWidgets import QFileDialog, QLineEdit, QTextEdit
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QListView
from os import path as osPath
# Note this would most likely need a means to either re-size
# the window or better yet have a Scroll Area added to it
class OutWithLineEdits(QWidget):
  def __init__(self, parent):
    QWidget.__init__(self)
    self.Parent = parent
    self.LneEdts = {}
    self.LneEdts[0] = QLineEdit()
    self.PrimrSet = False
    self.LstIndx = 0
    self.EditBox = QVBoxLayout()
    self.EditBox.addWidget(self.LneEdts[0])
    self.setLayout(self.EditBox)

  def SetImage(self, Text, Indx):
    print('Setting Image ', Indx, ')', Text)
    if Indx not in self.LneEdts.keys():
      self.LneEdts[Indx] = QLineEdit()
      self.EditBox.addWidget(self.LneEdts[Indx])
    self.LneEdts[Indx].setText(Text)

# So here is how to make that (or any) GUI using straight Python-Qt
class LoadUI(QWidget):
  def __init__(self, parent):
    QWidget.__init__(self)
    self.Parent = parent
    self.FileNameLst = []
    self.btnOpnImg = QPushButton('Open Image')
    self.btnOpnImg.clicked.connect(self.LoadImage)
    HBox1 = QHBoxLayout()
    HBox1.addWidget(self.btnOpnImg)
    HBox1.addStretch(1)
    Font = QFont()
    Font.setPointSize(16)
    Font.setBold(True)
    lblSelectd = QLabel('Your Selected Images:')
    lblSelectd.setFont(Font)
    HBox2 = QHBoxLayout()
    HBox2.addWidget(lblSelectd)
    HBox2.addStretch(1)
    # Comment-Out what you do not want to use and Uncomment-Out what you do
    # they have been made to be interchangable so you can see what each one
    # would look like
    # Now displaying the list of selected images could actually be done
    # several ways
    # 1) Your method of using QLineEdits
    self.OutPut = OutWithLineEdits(self)

    # 2) Using QLabels instead
    #self.OutPut = OutWithLabels(self)
    # 3) Using a QTextEdit instead
    #self.OutPut = OutWithTextEdit(self)
    # 4) Using a QListView instead
    #self.OutPut = OutWithListView(self)
    VBox = QVBoxLayout()
    VBox.addLayout(HBox1)
    VBox.addLayout(HBox2)
    VBox.addWidget(self.OutPut)
    VBox.addStretch(1)
    self.setLayout(VBox)
  # This is just a simple redirect or pass through method used for
  # ease of reading as well as implementation as modifying is very
  # easy later on
  @pyqtSlot()
  def LoadImage(self):
    FileData, NotUsed = QFileDialog.getOpenFileNames(self, 'Select Multi File', 'default', 'All Files (*)')
    if len(FileData) > 0:
      # Enumeration was unnecessary, especially since it was not used
      for FileItem in FileData:
        # Extract the File Name
        BaseName = osPath.basename(FileItem)
        self.FileNameLst.append(BaseName)
        if not self.OutPut.PrimrSet:
          self.OutPut.PrimrSet = True
          Indx = 0
        else:
          self.OutPut.LstIndx += 1
          Indx = self.OutPut.LstIndx
        self.OutPut.SetImage(BaseName, Indx)

# Keep your Main Window simple let it handle those things that are outside your
# actual Graphic User Interface such MenuToolBar, StatusBar, and Dockable Windows
# if you use any of these
class Fenster(QMainWindow):
  def __init__(self):
    QMainWindow.__init__(self)
    self.setWindowTitle('Image Selector')
    WinLeft = 550;
    WinTop = 150;
    WinWidth = 350;
    WinHigh = 300
    self.setGeometry(WinLeft, WinTop, WinWidth, WinHigh)
    # The Center Pane is your actual Main Graphic User Interface
    self.CenterPane = LoadUI(self)
    self.setCentralWidget(self.CenterPane)
    self.StatBar = self.statusBar()
  def DsplyStatMsg(self, MsgTxt):
    self.StatBar.showMessage(MsgTxt)

######MAIN####################
if __name__ == "__main__":
  # Unless you plan to do something with Command Line arguments no need
  # to include this and if you are you are better off using argparse
  # library as it handles Command Line arguments much more cleanly
  # app = QApplication(sys.argv)
  MainEventThred = QApplication([])
  MainApplication = Fenster()
  MainApplication.show()
  # This is the Qt4 method of doing this
  # sys.exit(app.exec_())
  # While this is the Qt5 method for doing this
  MainEventThred.exec() ```

```

Luca | 2020-06-17 15:36:16 UTC | #2 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
I wrote an example using a QGridLayout:
python ```
from PyQt5.QtWidgets import *
import sys
import os
class ImageInfo():
  def __init__(self, index, filename, width, height, parent):
    self.parent = parent
    self.lineEditName = self.addLineEdit(filename, index, 0)
    self.lineEditWidth = self.addLineEdit(0, index, 1)
    self.lineEditHeight = self.addLineEdit(0, index, 2)
  def addLineEdit(self, text, row, col):
    lineEdit = QLineEdit(parent=self.parent)
    lineEdit.setText(str(text))
    self.parent.layout().addWidget(lineEdit, row, col)
    return lineEdit
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.widget = QWidget()
    self.setCentralWidget(self.widget)
    self.layout = QGridLayout()
    self.widget.setLayout(self.layout)
    self.imagesInfo = []
    paths, _ = QFileDialog.getOpenFileNames(self, 'Select Multi File', 'default', 'All Files (*)')
    for index, path in enumerate(paths):
      filename, width, height = self.getImageInfo(path)
      self.imagesInfo = ImageInfo(index, filename, width, height, parent=self.widget)
  def getImageInfo(self, path):
    filename = os.path.basename(path)
    width, height = self.getImageSize(path)
    return filename, width, height
  def getImageSize(self, path):
    width, height = (0, 0) # Add your function
    return width, height
if __name__ == "__main__":
  app = QApplication([])
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

```

An alternative could be: _Change the layout into a QVBoxLayout_ Set ImageInfo class as a subclass of QWidget * Add the QLineEdits to a QHBoxLayout inside the ImageInfo class
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Or another one using a QViewTable where each row is an image.
There are multiple solutions, that could be better, this was just a simple example to show you the concept. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Creating dynamic TextBox's** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/creating-dynamic-textboxs/Python books) on the subject. 
**Creating dynamic TextBox's** was published in [faq](https://www.pythonguis.com/faq/) on June 17, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
