# Content from: https://www.pythonguis.com/faq/progress-track-thread-pool-rather-than-each-process/

[](https://www.pythonguis.com/faq/progress-track-thread-pool-rather-than-each-process/#menu)
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
# Progress track thread pool rather than each process
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Thomas_Parker | 2020-08-03 06:21:33 UTC | #1
Hiya,
Amazing book and site. By the way just quickly before I ask this question you have mistakes on your 1 to 1 live tutoring page. The 30 min session says 2 hours and is 190 dollars and then you have 2 other sessions each 1 hour at 100 dollars. Doesn't seem right.
Anyway I am building an inference tester for a tensorflow model I have built and trained. I have written it using the skeleton of your "progress_many" example. However in that example you create a for loop within the thread to simulate progress and send it back to the progress bar.
Inference happens so fast there is no point in that for my use. But I do need to know how long the whole batch took. I have two types of workers. One performs predicitons on an image parsed to it, the other is then signalled to run a worker that copies that file into the appropiate folder.
EDIT: I have set it up so I only click the start button once and it does the whole lot. I don't click it to start each thread.
I need to know how long all of the inference threads took as well as the file copying.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
I'm not sure how to track the workers and do this. Do you have any quick examples please?
Thank You!
martin | 2020-09-07 12:25:59 UTC | #2
Hey @Thomas_Parker welcome to the forum
> By the way just quickly before I ask this question you have mistakes on your 1 to 1 live tutoring page. The 30 min session says 2 hours and is 190 dollars and then you have 2 other sessions each 1 hour at 100 dollars 
> [Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
> [More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
You're quite right -- thanks for spotting that! Fixed now.
> Inference happens so fast there is no point in that for my use. But I do need to know how long the whole batch took. I have two types of workers. One performs predicitons on an image parsed to it, the other is then signalled to run a worker that copies that file into the appropiate folder.
If you want to track the duration of time taken for each worker, I would make each worker calculate it's own time and emit the _duration_ at the end (when it is complete). You can collect these up together, and display. A simple way to do this would be to use Python `time()` to get the milliseconds before and after the run (from within the runner's `run` method) and emit this as a duration at the end.
python ```
import random
import sys
import time
import uuid
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, QTimer, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QProgressBar,
  QPushButton,
  QVBoxLayout,
  QWidget,
)

class WorkerSignals(QObject):
  """
  Defines the signals available from a running worker thread.
  progress
    int progress complete,from 0-100
  """
  duration = pyqtSignal(str, int)
  finished = pyqtSignal(str)

class Worker(QRunnable):
  """
  Worker thread
  Inherits from QRunnable to handle worker thread setup, signals
  and wrap-up.
  """
  def __init__(self):
    super().__init__()
    self.job_id = uuid.uuid4().hex # <1>
    self.signals = WorkerSignals()
  @pyqtSlot()
  def run(self):
    start_time = time.time()
    total_n = 1000
    delay = random.random() / 100 # Random delay value.
    for n in range(total_n):
      time.sleep(delay)
    end_time = time.time()
    self.signals.duration.emit(self.job_id, end_time-start_time)
    self.signals.finished.emit(self.job_id)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout()
    self.duration = QLabel()
    button = QPushButton("START IT UP")
    button.pressed.connect(self.execute)
    layout.addWidget(self.duration)
    layout.addWidget(button)
    w = QWidget()
    w.setLayout(layout)
    # Dictionary holds the duration of current workers.
    self.worker_duration = {}
    self.setCentralWidget(w)
    self.show()
    self.threadpool = QThreadPool()
    print(
      "Multithreading with maximum %d threads" % self.threadpool.maxThreadCount()
    )
    self.timer = QTimer()
    self.timer.setInterval(100)
    self.timer.timeout.connect(self.refresh_duration)
    self.timer.start()
  def execute(self):
    self.cleanup() # Clear existing durations.
    for n in range(0, 4): # 4 per batch
      worker = Worker()
      worker.signals.duration.connect(self.update_duration)
      # Execute
      self.threadpool.start(worker)
  def cleanup(self):
    # Remove all previous durations.
    self.worker_duration = {}
    self.refresh_duration()
  def update_duration(self, job_id, duration):
    self.worker_duration[job_id] = duration
  def calculate_duration(self):
    if not self.worker_duration:
      return 0
    return sum(ms for ms in self.worker_duration.values())
  def refresh_duration(self):
    # Calculate total duration.
    duration = self.calculate_duration()
    self.duration.setText("{} ms ({} complete)".format(duration, len(self.worker_duration)))
app = QApplication(sys.argv)
window = MainWindow()
app.exec_()

```

If you're only running one batch at a time this should be enough. If you're going to be doing multiple concurrent batches, you could also pass the "batch id" into the workers and have them emit it along with the duration so you can group the times for each batch separately.
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Progress track thread pool rather than each process** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/progress-track-thread-pool-rather-than-each-process/Python books) on the subject. 
**Progress track thread pool rather than each process** was published in [faq](https://www.pythonguis.com/faq/) on August 03, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
