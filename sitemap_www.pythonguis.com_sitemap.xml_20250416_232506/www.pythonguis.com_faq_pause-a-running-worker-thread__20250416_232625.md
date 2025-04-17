# Content from: https://www.pythonguis.com/faq/pause-a-running-worker-thread/

[](https://www.pythonguis.com/faq/pause-a-running-worker-thread/#menu)
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
# Pause a running worker thread
Put a running task on hold, waiting for the UI
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 02 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
_Mew Forest_
> I'm stuck on working [with your last example](https://www.pythonguis.com/courses/concurrent-execution/multithreading-pyqt-applications-qthreadpool/). What should I change to pause my worker until user type something in my gui?
_Martin Fitzpatrick_
Normally if your worker will be waiting a long time you should just stop and start a new worker later. But if you _do_ want it to wait, you can put it in a wait loop (while`self.waiting==True: time.sleep(0.1)`) and update the value of self.waiting with a signal from outside.
_Hampus Nasstrom_
I've been trying to implement this but I really don't understand how to "update the value of self.waiting with a signal from outside". Tried defining the signal in the main window by adding a class:
python ```
class MainSignals(QObject):
  wait_signal = pyqtSignal(bool)

```

and then add `self.signals = MainSignals()` in the init of the main window. I then send the parent (the main window) to the worker but when I connect to the signal with `self.parent.signals.wait_signal.connect(self.set_wait)` I get the error: `TypeError: connect() failed between MainSignals.wait_signal[bool] and set_wait()`
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
_Martin Fitzpatrick_
Have a look at this example. It uses methods on the worker to update the values, which are then connected to the signals from the buttons.
python ```
from PyQt5.QtWidgets import (
  QWidget, QApplication, QProgressBar, QMainWindow,
  QHBoxLayout, QPushButton
)
from PyQt5.QtCore import (
  Qt, QObject, pyqtSignal, pyqtSlot, QRunnable, QThreadPool
)
import time

class WorkerSignals(QObject):
  progress = pyqtSignal(int)

class JobRunner(QRunnable):
  signals = WorkerSignals()
  def __init__(self):
    super().__init__()
    self.is_paused = False
    self.is_killed = False
  @pyqtSlot()
  def run(self):
    for n in range(100):
      self.signals.progress.emit(n + 1)
      time.sleep(0.1)
      while self.is_paused:
        time.sleep(0)
      if self.is_killed:
        break
  def pause(self):
    self.is_paused = True
  def resume(self):
    self.is_paused = False
  def kill(self):
    self.is_killed = True

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    # Some buttons
    w = QWidget()
    l = QHBoxLayout()
    w.setLayout(l)
    btn_stop = QPushButton("Stop")
    btn_pause = QPushButton("Pause")
    btn_resume = QPushButton("Resume")
    l.addWidget(btn_stop)
    l.addWidget(btn_pause)
    l.addWidget(btn_resume)
    self.setCentralWidget(w)
    # Create a statusbar.
    self.status = self.statusBar()
    self.progress = QProgressBar()
    self.status.addPermanentWidget(self.progress)
    # Thread runner
    self.threadpool = QThreadPool()
    # Create a runner
    self.runner = JobRunner()
    self.runner.signals.progress.connect(self.update_progress)
    self.threadpool.start(self.runner)
    btn_stop.pressed.connect(self.runner.kill)
    btn_pause.pressed.connect(self.runner.pause)
    btn_resume.pressed.connect(self.runner.resume)
    self.show()
  def update_progress(self, n):
    self.progress.setValue(n)
app = QApplication([])
w = MainWindow()
app.exec_()

```

When you run this you'll see a progress bar moving left to right. If you hit pause it will pause, and resume it will restart. If you press stop it will kill the runner (by exiting the loop).
![progress-pause|317x139](https://www.pythonguis.com/static/faq/todo/pause-a-running-worker-thread/pM4msYDa7tkLgCj7xNW3dFGUBmV.png)
_Albert Ang_
Thank you for your wonderful example. I have a slight problem in using your example. When user closes the GUI without clicking on the Stop button, the thread seems to continue to run. Can advise on the detection of user's close GUI event and stop all the threads gracefully?
_Martin Fitzpatrick_
To detect when the app is shutting down you can use the `.aboutToQuit` signal on `QApplication`. You can connect this up to your workers stop/kill slot to trigger it on shutdown, e.g.
python ```
app = QApplication(sys.argv)

```

Then to connect the worker
python ```
app.aboutToQuit.connect(worker.stop)

```

If you have many workers, you might prefer to connect this to a handler that will clean up all the workers in one go.
If you have per-window workers, you could also catch the window `closeEvent` and stop the workers there.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
_Albert Ang_
[quote="martin, post:6, topic:147"] `app = QApplication(sys.argv)` [/quote]
Thank you for your prompt reply! I followed your code with app = QApplication(sys.argv) and app.aboutToQuit.connect(worker.stop) but I got the worker not defined error. As I used your example above which is # Create a runner self.runner = JobRunner() self.runner.signals.progress.connect(self.update_progress) self.threadpool.start(self.runner)
so I tried app.aboutToQuit.connect(runner.stop) but my program gave runner is not defined error. When I run my Python program eg. test.py, do I need to run it with an argument? eg. test.py runner?
_Martin Fitzpatrick_
The "not defined" error means that there isn't a variable with the name you're using -- that either means you're using the name before it's been defined, or you're using the wrong name.
In this case, when you define the window the runner object hasn't been created yet, so it can't be connected to. The simplest thing to do is to add an extra method on your window to handle this sort of "shutdown" cleanup, e.g.
python ```
def shutdown(self):
  if self.runner:  # set self.runner=None in your __init__ so it's always defined.
    self.runner.stop()

```

...and then you can connect to _that_ method, since it's available as soon as the window is created.
python ```
app.aboutToQuit.connect(w.shutdown) # connect to the shutdown method on the window.

```

_Hampus Nasstrom_
Hi Martin, I'm sorry I missed you reply after the update to a forum. Thank you so much for the reply! I had implemented something similar where the worker checked by calling a function of the parent but this is more elegant. Really appreciate your website, it really helps me as a PhD student in physics having to implement a bunch of GUIs. Many thanks!
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Pause a running worker thread** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pause-a-running-worker-thread/Python books) on the subject. 
**Pause a running worker thread** was published in [faq](https://www.pythonguis.com/faq/) on May 10, 2020 (updated September 02, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
