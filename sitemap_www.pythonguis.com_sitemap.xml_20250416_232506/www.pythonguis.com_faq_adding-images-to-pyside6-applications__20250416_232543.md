# Content from: https://www.pythonguis.com/faq/adding-images-to-pyside6-applications/

[](https://www.pythonguis.com/faq/adding-images-to-pyside6-applications/#menu)
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
# Q&A: How Do I Display Images in PySide6?
Using QLabel to easily add images to your applications
by [John Lim](https://www.pythonguis.com/authors/john-lim/) Last updated Mar 03 PySide6 [ FAQ ](https://www.pythonguis.com/faq/)
This tutorial is also available for [PyQt6](https://www.pythonguis.com/faq/adding-images-to-pyqt6-applications/) , [PySide2](https://www.pythonguis.com/faq/adding-images-to-pyside2-applications/) and [PyQt5](https://www.pythonguis.com/faq/adding-images-to-pyqt5-applications/)
Adding images to your application is a common requirement, whether you're building an image/photo viewer, or just want to add some decoration to your GUI. Unfortunately, because of how this is done in Qt, it can be a little bit tricky to work out at first.
In this short tutorial, we will look at how you can insert an external image into your PySide6 application layout, using both code and Qt Designer.
Table of Contents
  * [Which widget to use?](https://www.pythonguis.com/faq/adding-images-to-pyside6-applications/#which-widget-to-use)
  * [Using Qt Designer](https://www.pythonguis.com/faq/adding-images-to-pyside6-applications/#using-qt-designer)
  * [Using Code](https://www.pythonguis.com/faq/adding-images-to-pyside6-applications/#using-code)
  * [Conclusion](https://www.pythonguis.com/faq/adding-images-to-pyside6-applications/#conclusion)


### Which widget to use?
Since you're wanting to insert an image you might be expecting to use a widget named `QImage` or similar, but that would make a bit too much sense! `QImage` is actually Qt's image _object_ type, which is used to store the actual image data for use within your application. The _widget_ you use to display an image is `QLabel`.
The primary use of `QLabel` is of course to add labels to a UI, but it also has the ability to display an image — or _pixmap_ — instead, covering the entire area of the widget. Below we'll look at how to use `QLabel` to display a widget in your applications.
### Using Qt Designer
First, create a _MainWindow_ object in Qt Designer and add a "Label" to it. You can find Label at in _Display Widgets_ in the bottom of the left hand panel. Drag this onto the `QMainWindow` to add it.
![MainWindow with a single QLabel added](https://www.pythonguis.com/static/faq/adding-images-to-applications/1.png) _MainWindow with a single QLabel added_
Next, with the Label selected, look in the right hand `QLabel` properties panel for the `pixmap` property (scroll down to the blue region). From the property editor dropdown select "Choose File…" and select an image file to insert.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
As you can see, the image is inserted, but the image is kept at its original size, cropped to the boundaries of the`QLabel` box. You need to resize the `QLabel` to be able to see the entire image.
In the same controls panel, click to enable `scaledContents`.
When `scaledContents` is enabled the image is resized to the fit the bounding box of the `QLabel` widget. This shows the entire image at all times, although it does not respect the aspect ratio of the image if you resize the widget.
You can now save your UI to file (e.g. as `mainwindow.ui`).
To view the resulting UI, we can use the standard application template below. This loads the `.ui` file we've created (`mainwindow.ui`) creates the window and starts up the application.
PySide6 ```
import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
window = loader.load("mainwindow.ui", None)
window.show()
app.exec()

```

Running the above code will create a window, with the image displayed in the middle. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
![QtDesigner application showing a Cat](https://www.pythonguis.com/static/faq/adding-images-to-applications/5.png) _QtDesigner application showing a Cat_
### Using Code
Instead of using Qt Designer, you might also want to show an image in your application through code. As before we use a `QLabel` widget and add a _pixmap_ image to it. This is done using the `QLabel` method `.setPixmap()`. The full code is shown below.
PySide6 ```
import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.title = "Image Viewer"
    self.setWindowTitle(self.title)
    label = QLabel(self)
    pixmap = QPixmap('cat.jpg')
    label.setPixmap(pixmap)
    self.setCentralWidget(label)
    self.resize(pixmap.width(), pixmap.height())

app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())

```

The block of code below shows the process of creating the `QLabel`, creating a `QPixmap` object from our file `cat.jpg` (passed as a file path), setting this `QPixmap` onto the `QLabel` with `.setPixmap()` and then finally resizing the window to fit the image.
python ```
label = QLabel(self)
pixmap = QPixmap('cat.jpg')
label.setPixmap(pixmap)
self.setCentralWidget(label)
self.resize(pixmap.width(), pixmap.height())

```

Launching this code will show a window with the cat photo displayed and the window sized to the size of the image.
![QMainWindow with Cat image displayed](https://www.pythonguis.com/static/faq/adding-images-to-applications/4.png) _QMainWindow with Cat image displayed_
Just as in Qt designer, you can call `.setScaledContents(True)` on your `QLabel` image to enable scaled mode, which resizes the image to fit the available space.
python ```
label = QLabel(self)
pixmap = QPixmap('cat.jpg')
label.setPixmap(pixmap)
label.setScaledContents(True)
self.setCentralWidget(label)
self.resize(pixmap.width(), pixmap.height())

```

Notice that you set the scaled state on the `QLabel` widget and not the image pixmap itself.
### Conclusion
In this quick tutorial we've covered how to insert images into your Qt UIs using `QLabel` both from Qt Designer and directly from PySide6 code. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
[![John Lim Ji Xiong](https://www.pythonguis.com/static/theme/images/authors/john-lim.jpg)](https://www.pythonguis.com/authors/john-lim/)
**Q &A: How Do I Display Images in PySide6?** was written by [John Lim](https://www.pythonguis.com/authors/john-lim/) . 
John is a developer from Kuala Lumpur, Malaysia who works as a Senior R&D Engineer. 
**Q &A: How Do I Display Images in PySide6?** was published in [faq](https://www.pythonguis.com/faq/) on March 27, 2024 (updated March 03, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [images](https://www.pythonguis.com/topics/images/) [qlabel](https://www.pythonguis.com/topics/qlabel/) [widgets](https://www.pythonguis.com/topics/widgets/) [graphics](https://www.pythonguis.com/topics/graphics/) [qpixmap](https://www.pythonguis.com/topics/qpixmap/) [pixmap](https://www.pythonguis.com/topics/pixmap/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
