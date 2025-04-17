# Content from: https://www.pythonguis.com/examples/python-unzip-application/

[](https://www.pythonguis.com/examples/python-unzip-application/#menu)
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
# 7Pez, custom skinned Unzip
Skinning a PyQt5 decorationless window
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 04 PyQt5 [ Example applications ](https://www.pythonguis.com/examples/)
[ 7Pez Source Code ](https://www.pythonguis.com/d/unzip.zip)
This is a functionally terrible unzip application, saved only by the fact that you get to look at a cat while using it.
The original idea reflected in the name _7Pez_ was actually worse — to rig it up so you had to push on the head to unzip each file from the zipfile, so press 5 times to get 5 files. Opening a zipfile with 1000s of items in it soon put a stop to that idea.
It also fails on the Pez front, since you press the head instead of lifting it to release the file. I haven't seen a Pez in years, so I forgot how they work.
But look, cat.
Cat.
## Setting up
The UI of the app was built in Qt Designer, and consists entirely of `QLabel` objects. Two seperate `QLabel` objects with pixmaps were used for the head and body. The progress _Pez bar_ is made from a stack of `QLabel` objects inside a `QVBoxLayout`.
The widget for the progress bar is placed _behind_ the cat image, which is transparent with a central heart-shaped cutout. This means the progress bar shows through nicely.
1:1 Coaching & Tutoring for your Python GUIs project
[![Martin Fitzpatrick Python GUIs Coaching & Training](https://www.pythonguis.com/static/theme/images/products/coaching.jpg)](https://calendly.com/martinfitzpatrick/60min-python-guis-coaching)
[60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/) [Book Now](https://www.pythonguis.com/live/)
1:1 Python GUIs Coaching & Training
**Comprehensive code review** • **Bugfixes** & improvements • **Maintainability** advice and **architecture** improvements • **Design and usability** assessment • Suggestions and tips to **expand your knowledge** • **Packaging and distribution** help for Windows, Mac & Linux • [Find out more.](https://www.pythonguis.com/live)
The completed `.ui` file was built with `pyuic5` to produce an importable Python module. This, together with the standard PyQt5 modules are imported as usual. We also make use of some standard library modules, including the `zipfile` module to handle the loading and unpacking of `.zip` files.
python ```
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MainWindow import Ui_MainWindow
import os
import types
import random
import sys
import traceback
import zipfile

```

The state of the _Pez bar_ is controlled by switching CSS styles on `QLabel` elements between _on_ — pink background with dark pink writing and border — and _off_ — no background and transparent text.
The colour used for `OFF` is `rgba(0,0,0,0)`. In RGBA format the fourth value indicates _transparency_ , with 0 meaning fully transparent. So our OFF state is fully transparent and not at all black.
python ```
PROGRESS_ON = """
QLabel {
  background-color: rgb(233,30,99);
  border: 2px solid rgb(194,24,91);
  color: rgb(136,14,79);
}
"""
PROGRESS_OFF = """
QLabel {
  color: rgba(0,0,0,0);
}
"""

```

We also define a bunch of paths to exclude while unzipping. In this case we're just excluding the special `__MACOSX` folder which is added on macOS to extended attributes. We don't want to unpack this.
python ```
EXCLUDE_PATHS = [
  '__MACOSX/',
]

```

## Theming the QMainWindow
The app uses a few advanced features for Qt window appearance, including translucency, frameless/decoration-less windows and a custom window PNG overlay.
To enable transparent windows in Qt we need to set the `Qt.WA_TranslucentBackground` attribute on the window. Without this, the window manager will automatically draw a background window colour behind the window. To turn off the window decorations (open, restore, close buttons and the titlebar) we set the `Qt.FramelessWindowHint` flag.
We also enable our window to accept drag-drops, so we can drop zip files on it. The actual code to handle the dropping files is implemented later.
python ```
class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)
    self.setAttribute(Qt.WA_TranslucentBackground )
    self.setWindowFlags(Qt.FramelessWindowHint)
    self.setAcceptDrops(True)

```

We set the initial _unset_ state for previous drag position and active unzip workers.
python ```
    self.prev_pos = None
    self.worker = None
    # Reset progress bar to complete (empty)
    self.update_progress(1)

```

Unzipping is handled by a single `threadpool` which we create at startup.
python ```
    # Create a threadpool to run our unzip worker in.
    self.threadpool = QThreadPool()

```

To put the head on top of the body we must `.raise_` it.
python ```
    self.head.raise_()

```

## Animating the head
The head is disconnected and bobbles around when pressed. The progress bar fills up when a zip file is dropped onto the application and empties when the files are unzipped. Unzipping is a one-off operation, and a new zip file must be dropped to repeat the process.
To start the animation we need to be able to detect clicks on the head from our Python code. When subclassing a widget we can do this by implementing our own `mousePressEvent`.
In this case the UI has been implemented in Qt Designer, and we cannot subclass before adding to the layout. To override methods on the existing object, we need to _patch_ it.
The first patch is for the `mousePressEvent`. This captures clicks on the cat head and triggers the extraction process — if one isn't already underway — and the animation.
The head animation is implemented as a random rotation, between -15 and +15 degrees, and lifting the head to 30 pixels up. This is gradually returned back to 0 rotation and 0 offset by the animation timer interrupt.
python ```
:::python
    def patch_mousePressEvent(self_, e):
      if e.button() == Qt.LeftButton and self.worker is not None:
        # Start the head animation.
        self_.current_rotation = random.randint(-15, +15)
        self_.current_y = 30
        # Redraw the mainwindow
        self.update()
        # Start the extraction.
        self.threadpool.start(self.worker)
        self.worker = None # Remove the worker so it is not double-triggere.
      elif e.button() == Qt.RightButton:
        pass # Open a new zip?

```

You could add an x offset as well to make the head movement more erratic.
Notice our event patch also checks for a right button, here you could show a dialog to open a file directly rather than dropping.
The second patch covers the `paintEvent` where the widget is drawn.
python ```
:::python
    def patch_paintEvent(self, event):
      p = QPainter(self)
      rect = event.rect()
      # Translate
      transform = QTransform()
      transform.translate(rect.width()/2, rect.height()/2)
      transform.rotate(self.current_rotation)
      transform.translate(-rect.width()/2, -rect.height()/2)
      p.setTransform(transform)
      # Calculate rect to center the pixmap on the QLabel.
      prect = self.pixmap().rect()
      rect.adjust(
        (rect.width() - prect.width()) / 2,
        self.current_y + (rect.height() - prect.height()) / 2,
        -(rect.width() - prect.width()) / 2,
        self.current_y + -(rect.height() - prect.height()) / 2,
      )
      p.drawPixmap(rect, self.pixmap())

```

To patch an object method in Python we assign the function to an attribute on the object, wrapping it with `types.MethodType` and passing in the parent object (in this case `self.head`).
python ```
:::python
    self.head.mousePressEvent = types.MethodType(patch_mousePressEvent, self.head)
    self.head.paintEvent = types.MethodType(patch_paintEvent, self.head)

```

With the patches in place, we set up a timer — firing every 5 milliseconds (or thereabouts) — to handle the animation update. We also set the initial states for _rotation_ and _y_ position of the head.
python ```
:::python
    # Initialize
    self.head.current_rotation = 0
    self.head.current_y = 0
    self.head.locked = True
    self.timer = QTimer()
    self.timer.timeout.connect(self.timer_triggered)
    self.timer.start(5)

```

That is the end of the window `__init__` block. The handler for the timer is implemented as a window method, `timer_triggered`. This is called each time the timer times out.
The logic here is pretty self explanatory. If the head position is raised `>0` reduce it. If the rotation is clockwise `>0` rotate it back, if the rotation is anticlockwise `<0` rotate it forward. The result is to gradually bring the head back to it's default position.
The `.update()` is triggered to redraw the head. Finally, if after this update we are back at `0` rotation and `0` offset, we unlock the head, allowing it to be clicked again. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
python ```
:::python
  def timer_triggered(self):
    if self.head.current_y > 0:
      self.head.current_y -= 1
    if self.head.current_rotation > 0:
      self.head.current_rotation -= 1
    elif self.head.current_rotation < 0:
      self.head.current_rotation += 1
    self.head.update()
    if self.head.current_y == 0 and self.head.current_rotation == 0:
      self.head.locked = False

```

## Drag & drop
To accept zip files dropped onto our cat we need to define the standard Qt `dragEnterEvent` and `dropEvent` handlers.
The `dragEnterEvent` is triggered when an object (such as a file) is dragged over the window. It receives a `QDragEnterEvent` which contains information about the object being dragged. In our event handler we can either respond by _accepting_ or _rejecting_ the event (or ignoring it).
Depending on the _accept_ or _reject_ response the desktop will provide feedback to the user whether the drop can be performed. In our case we're checking that we're receiving _URLs_ — all files are URLs in Qt — and that the first of these has a `.zip` file extension.
python ```
:::python
  def dragEnterEvent(self, e):
    data = e.mimeData()
    if data.hasUrls():
      # We are passed urls as a list, but only accept one.
      url = data.urls()[0].toLocalFile()
      if os.path.splitext(url)[1].lower() == '.zip':
        e.accept()

```

We only check the first since we can only accept a single file. You could change this to iterate all the files added and find the *first* `.zip` instead.
The `dropEvent` is only triggered where the `dragEnterEvent` _accepted_ the drop, and the user dropped the object. In this case we receive a `QDropEvent` containing the same data as before.
Here we retrieve the zip file from the first URL in the list, as before, and then pass this into a new `UnzipWorker` which will handle the unzip process. This worker is not yet started, so will not unzip the file until we start it.
python ```
:::python
  def dropEvent(self, e):
    data = e.mimeData()
    path = data.urls()[0].toLocalFile()
    # Load the zipfile and pass to the worker which will extract.
    self.worker = UnzipWorker(path)
    self.worker.signals.progress.connect(self.update_progress)
    self.worker.signals.finished.connect(self.unzip_finished)
    self.worker.signals.error.connect(self.unzip_error)
    self.update_progress(0)

```

## Moving the Window
In a normal windowed application you're able to drag and drop it around your desktop using the window bar. For this app we've turned that off, and so we need to implement the logic for repositioning the window ourselves.
To do this we define two custom event handlers. The first `mousePressEvent` fires when the user clicks in the window (on the cat) and simply records the _global_ location of this click.
The second `mouseMoveEvent` is triggered any time the mouse moves over our window _while it is focused_. We check for `self.prev_pos` to be set since we require this for our calculation, however it should not be possible for the `mouseMoveEvent` event to occur without first registering a `mousePressEvent` to select the window.
This is why we don't need to check for the release event. Once the mouse is released `mouseMoveEvent` will stop firing.
The movement is calculated relative to the previous position, again using the _global_ position. We use the `delta` between these positions to update the window using `move()`.
python ```
:::python
  def mousePressEvent(self, e):
    self.prev_pos = e.globalPos()
  def mouseMoveEvent(self, e):
    if self.prev_pos:
      delta = e.globalPos() - self.prev_pos
      self.move(self.x() + delta.x(), self.y() + delta.y())
      self.prev_pos = e.globalPos()

```

## Unzip handlers
As we unzip a file we want to update our _Pez bar_ with the progress in realtime. The `update_progress` callback method is defined below. When called with a `float` in the range 0-1 — representing 0-100% —this will update the current state.
The update itself is handled by iterating over each progress bar indicator `QLabel`, numbered 1-10, and setting their style sheet to `PROGRESS_ON` or `PROGRESS_OFF`.
python ```
:::python
  def update_progress(self, pc):
    """
    Accepts progress as float in
    :param pc: float 0-1 of completion.
    :return:
    """
    current_n = int(pc * 10)
    for n in range(1, 11):
      getattr(self, 'progress_%d' % n).setStyleSheet(
        PROGRESS_ON if n > current_n else PROGRESS_OFF
      )

```

An `unzip_finished` callback is set, although it doesn't do anything. You coudl add some custom notifications here if you like.
python ```
:::python
  def unzip_finished(self):
    pass

```

We also define an error callback, which will receive any tracebacks from the unzip progress and display them as a _critical_ error message.
python ```
:::python
  def unzip_error(self, err):
    exctype, value, traceback = err
    self.update_progress(1) # Reset the Pez bar.
    dlg = QMessageBox(self)
    dlg.setText(traceback)
    dlg.setIcon(QMessageBox.Critical)
    dlg.show()

```

This isn't particularly user friendly, so you could extend it to display nicer customized messages for different exception types.
## Unzipping, in separate thread
The unzipping of files is handled in a separate thread, so it doesn't lock the application. We use the `QThreadPool` approach [described here](https://www.pythonguis.com/article/multithreading-pyqt-applications-with-qthreadpool/). Unzipping occurs in standalone `QRunnable` jobs, which communicate with the application using Qt signals.
We define 3 signals our unzipper can return —  _finished_ , _error_ and _progress_. These are emitted from the worker `run()` slot below, and connected up to the callback handlers we've just defined.
python ```
  class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.
    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    progress = pyqtSignal(float)

```

The worker itself accepts a path to the zip file which we intend to unzip. Creating the worker does not start the unzip process, just passes it to `zipfile.ZipFile` to create a new zip objects.
When the worker is started, the `run()` method is executed. Here we get a complete list of the files in the zipfile, and then proceed to unzip each file in turn. This is a little slower than doing them in one go but it allows us to update the _Pez bar_ with progress.
Progress is updated by dividing the current iteration number by the total number of items in the list. By `enumerate()` provides a 0-based index, which would mean our final state would be `(total_n-1)/total_n` — not quite 100%. By passing `1` as a second parameter we start the counting from 1, giving a final loop state of `total_n/total_n` which gives 1.
python ```
  class UnzipWorker(QRunnable):
    '''
    Worker thread for unzipping.
    '''
    signals = WorkerSignals()
    def __init__(self, path):
      super().__init__()
      os.chdir(os.path.dirname(path))
      self.zipfile = zipfile.ZipFile(path)
    @pyqtSlot()
    def run(self):
      try:
        items = self.zipfile.infolist()
        total_n = len(items)
        for n, item in enumerate(items, 1):
          if not any(item.filename.startswith(p) for p in EXCLUDE_PATHS):
            self.zipfile.extract(item)
          self.signals.progress.emit(n / total_n)
      except Exception as e:
        exctype, value = sys.exc_info()[:2]
        self.signals.error.emit((exctype, value, traceback.format_exc()))
        return
      self.signals.finished.emit()

```

The _finished_ signal is emitted if the unzip completes successfully or unsuccessfully, and is used to reset the application state. An _error_ is emitted on if unzipping fails, passing the exception and traceback as a tuple. Our `run()` slot emits _progress_ as a `float` 0..1.
## Challenges
You could make this even more awesome by — 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
  1. Animate the cat head some more, so it bobbles around more amusingly when pressed.
  2. Making the cat meow when you press the head. Take a look at the Qt Multimedia components, which make it simple to play audio cross-platform.
  3. Add support for unzipping multiple files simultaneously.


Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**7Pez, custom skinned Unzip** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/examples/python-unzip-application/Python books) on the subject. 
**7Pez, custom skinned Unzip** was published in [examples](https://www.pythonguis.com/examples/) on March 30, 2019 (updated April 04, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [unzip](https://www.pythonguis.com/topics/unzip/) [app](https://www.pythonguis.com/topics/app/) [qt5](https://www.pythonguis.com/topics/qt5/) [multithreaded](https://www.pythonguis.com/topics/multithreaded/) [threading](https://www.pythonguis.com/topics/threading/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/)
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
