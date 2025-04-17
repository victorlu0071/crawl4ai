# Content from: https://www.pythonguis.com/faq/pass-multiple-models-to-qlistview/

[](https://www.pythonguis.com/faq/pass-multiple-models-to-qlistview/#menu)
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
# Pass multiple models to QListView
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Thomas_Parker | 2020-10-01 12:27:43 UTC | #1
I have 3 worker manager classes each containing their own threadpools and worker queues.
I am using the worker manager 6 example. However when setting progress.setModel I can only pass one worker manager.
How do I get both worker managers to be in one QListView?
Thank You
martin | 2020-10-02 19:19:53 UTC | #2
Hi @Thomas_Parker welcome to the forum. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
You can't actually set more than one model on a view, as a view can only pull data from one source at a time. However, you can already achieve what you want with the current manager implementation.
If you look at the definition of the `WorkerManager` you'll see it has two variables `_workers` and `_state`. These are defined as _class variables_ (defined on the class definition rather than in the `__init__` -- which means they are shared among all instances of the class.
python ```
class WorkerManager(QAbstractListModel):
  """
  Manager to handle our worker queues and state.
  Also functions as a Qt data model for a view
  displaying progress for each worker.
  """
  _workers = {}
  _state = {}

```

That's a bit weird to be honest, and I should probably change it. But it does mean that you can get what you want simply by defining two `WorkerManager` instances and passing _one_ of them as the model.
Since they share their internal state, either will report the full state for both.
Here's the `MainWindow` definition to achieve this --
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.workers1 = WorkerManager()
    self.workers2 = WorkerManager()
    self.workers1.status.connect(self.statusBar().showMessage)
    self.workers2.status.connect(self.statusBar().showMessage)
    layout = QVBoxLayout()
    self.progress = QListView()
    self.progress.setModel(self.workers1)
    delegate = ProgressBarDelegate()
    self.progress.setItemDelegate(delegate)
    layout.addWidget(self.progress)
    self.text = QPlainTextEdit()
    self.text.setReadOnly(True)
    start1 = QPushButton("Start a worker 1")
    start1.pressed.connect(self.start_worker1)
    start2 = QPushButton("Start a worker 2")
    start2.pressed.connect(self.start_worker2)
    clear = QPushButton("Clear")
    clear.pressed.connect(self.workers1.cleanup)
    clear.pressed.connect(self.workers2.cleanup)
    layout.addWidget(self.text)
    layout.addWidget(start1)
    layout.addWidget(start2)
    layout.addWidget(clear)
    w = QWidget()
    w.setLayout(layout)
    self.setCentralWidget(w)
    self.show()
  # tag::startWorker[]
  def start_worker1(self):
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    w = Worker(x, y)
    w.signals.result.connect(self.display_result)
    w.signals.error.connect(self.display_result)
    self.workers1.enqueue(w)
  def start_worker2(self):
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    w = Worker(x, y)
    w.signals.result.connect(self.display_result)
    w.signals.error.connect(self.display_result)
    self.workers2.enqueue(w)
  # end::startWorker[]
  def display_result(self, job_id, data):
    self.text.appendPlainText("WORKER %s: %s" % (job_id, data))

```

If you click either the start1/start2 buttons you'll see the workers appear in the list. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
But yeah, as I say, that's a bit _weird_. So what we should do instead is separate the model from the manager, and share this separate model explicitly with both managers. Below is a full working example to do that.
The key changes are in the definition of the `WorkerModel` which holes everything relating to `_state`. The signals/etc. are modified to connect to the model directly. On the `MainWindow` we create a model instance, and then pass it into each `WorkerManager` so the _state_ is shared between them -- jobs for both are shown in the progress list.
python ```
import random
import subprocess
import sys
import time
import traceback
import uuid
from PyQt5.QtCore import (
  QAbstractListModel, QObject, QRect, QRunnable, Qt, QThreadPool, QTimer,
  pyqtSignal, pyqtSlot,
)
from PyQt5.QtGui import QBrush, QColor, QPen
from PyQt5.QtWidgets import (
  QApplication, QListView, QMainWindow, QPlainTextEdit, QProgressBar, 
  QPushButton, QStyledItemDelegate, QVBoxLayout, QWidget,
)

STATUS_WAITING = "waiting"
STATUS_RUNNING = "running"
STATUS_ERROR = "error"
STATUS_COMPLETE = "complete"
STATUS_COLORS = {
  STATUS_RUNNING: "#33a02c",
  STATUS_ERROR: "#e31a1c",
  STATUS_COMPLETE: "#b2df8a",
}
DEFAULT_STATE = {"progress": 0, "status": STATUS_WAITING}

class WorkerSignals(QObject):
  """
  Defines the signals available from a running worker thread.
  Supported signals are:
  finished
    No data
  error
    `tuple` (exctype, value, traceback.format_exc() )
  result
    `object` data returned from processing, anything
  progress
    `int` indicating % progress 
  """
  error = pyqtSignal(str, str)
  result = pyqtSignal(str, object) # We can send anything back.
  finished = pyqtSignal(str)
  progress = pyqtSignal(str, int)
  status = pyqtSignal(str, str)

class Worker(QRunnable):
  """
  Worker thread
  Inherits from QRunnable to handle worker thread setup, signals and wrap-up.
  :param args: Arguments to pass for the worker
  :param kwargs: Keywords to pass for the worker
  """
  def __init__(self, *args, **kwargs):
    super().__init__()
    # Store constructor arguments (re-used for processing).
    self.signals = WorkerSignals()
    # Give this job a unique ID.
    self.job_id = str(uuid.uuid4())
    # The arguments for the worker
    self.args = args
    self.kwargs = kwargs
    self.signals.status.emit(self.job_id, STATUS_WAITING)
  @pyqtSlot()
  def run(self):
    """
    Initialize the runner function with passed args, kwargs.
    """
    self.signals.status.emit(self.job_id, STATUS_RUNNING)
    x, y = self.args
    try:
      value = random.randint(0, 100) * x
      delay = random.random() / 10
      result = []
      for n in range(100):
        # Generate some numbers.
        value = value / y
        y -= 1
        # The following will sometimes throw a division by zero error.
        result.append(value)
        # Pass out the current progress.
        self.signals.progress.emit(self.job_id, n + 1)
        time.sleep(delay)
    except Exception as e:
      print(e)
      # We swallow the error and continue.
      self.signals.error.emit(self.job_id, str(e))
      self.signals.status.emit(self.job_id, STATUS_ERROR)
    else:
      self.signals.result.emit(self.job_id, result)
      self.signals.status.emit(self.job_id, STATUS_COMPLETE)
    self.signals.finished.emit(self.job_id)

class WorkerModel(QAbstractListModel):
  """
  Model holding the worker states (used by the managers)
  to track progress.
  """
  _state = {}
  def add(self, identifier, data):
    self._state[identifier] = data
    self.layoutChanged.emit()
  # Model interface
  def data(self, index, role):
    if role == Qt.DisplayRole:
      # See below for the data structure.
      job_ids = list(self._state.keys())
      job_id = job_ids[index.row()]
      return job_id, self._state[job_id]
  def rowCount(self, index):
    return len(self._state)
  def receive_status(self, job_id, status):
    self._state[job_id]["status"] = status
    self.layoutChanged.emit()
  def receive_progress(self, job_id, progress):
    self._state[job_id]["progress"] = progress
    self.layoutChanged.emit()

  def cleanup(self):
    """
    Remove any complete/failed workers from worker_state.
    """
    for job_id, s in list(self._state.items()):
      if s["status"] in (STATUS_COMPLETE, STATUS_ERROR):
        del self._state[job_id]
    self.layoutChanged.emit()    

class WorkerManager(QObject):
  """
  Manager to handle our worker queues and state.

  """
  _workers = {}
  status = pyqtSignal(str)
  def __init__(self, model):
    super().__init__()
    # Store the model we'll use for tracking state.
    self.model = model
    # Create a threadpool for our workers.
    self.threadpool = QThreadPool()
    # self.threadpool.setMaxThreadCount(1)
    self.max_threads = self.threadpool.maxThreadCount()
    print("Multithreading with maximum %d threads" % self.max_threads)
    self.status_timer = QTimer()
    self.status_timer.setInterval(100)
    self.status_timer.timeout.connect(self.notify_status)
    self.status_timer.start()
  def notify_status(self):
    n_workers = len(self._workers)
    running = min(n_workers, self.max_threads)
    waiting = max(0, n_workers - self.max_threads)
    self.status.emit(
      "{} running, {} waiting, {} threads".format(
        running, waiting, self.max_threads
      )
    )
  def enqueue(self, worker):
    """
    Enqueue a worker to run (at some point) by passing it to the QThreadPool.
    """
    worker.signals.error.connect(self.receive_error)
    worker.signals.status.connect(self.model.receive_status)
    worker.signals.progress.connect(self.model.receive_progress)
    worker.signals.finished.connect(self.done)
    self.threadpool.start(worker)
    self._workers[worker.job_id] = worker
    # Set default status to waiting, 0 progress.
    self.model.add(worker.job_id, DEFAULT_STATE.copy())

  def receive_error(self, job_id, message):
    print(job_id, message)
  def done(self, job_id):
    """
    Task/worker complete. Remove it from the active workers
    dictionary. We leave it in worker_state, as this is used to
    to display past/complete workers too.
    """
    del self._workers[job_id]

class ProgressBarDelegate(QStyledItemDelegate):
  def paint(self, painter, option, index):
    # data is our status dict, containing progress, id, status
    job_id, data = index.model().data(index, Qt.DisplayRole)
    if data["progress"] > 0:
      color = QColor(STATUS_COLORS[data["status"]])
      brush = QBrush()
      brush.setColor(color)
      brush.setStyle(Qt.SolidPattern)
      width = option.rect.width() * data["progress"] / 100
      rect = QRect(option.rect) # Copy of the rect, so we can modify.
      rect.setWidth(width)
      painter.fillRect(rect, brush)
    pen = QPen()
    pen.setColor(Qt.black)
    painter.drawText(option.rect, Qt.AlignLeft, job_id)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.model = WorkerModel()
    self.workers1 = WorkerManager(self.model)
    self.workers2 = WorkerManager(self.model)
    self.workers1.status.connect(self.statusBar().showMessage)
    self.workers2.status.connect(self.statusBar().showMessage)
    layout = QVBoxLayout()
    self.progress = QListView()
    self.progress.setModel(self.model)
    delegate = ProgressBarDelegate()
    self.progress.setItemDelegate(delegate)
    layout.addWidget(self.progress)
    self.text = QPlainTextEdit()
    self.text.setReadOnly(True)
    start1 = QPushButton("Start a worker 1")
    start1.pressed.connect(self.start_worker1)
    start2 = QPushButton("Start a worker 2")
    start2.pressed.connect(self.start_worker2)
    clear = QPushButton("Clear")
    # We clear the model.
    clear.pressed.connect(self.model.cleanup)
    layout.addWidget(self.text)
    layout.addWidget(start1)
    layout.addWidget(start2)
    layout.addWidget(clear)
    w = QWidget()
    w.setLayout(layout)
    self.setCentralWidget(w)
    self.show()
  def start_worker1(self):
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    w = Worker(x, y)
    w.signals.result.connect(self.display_result)
    w.signals.error.connect(self.display_result)
    self.workers1.enqueue(w)
  def start_worker2(self):
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    w = Worker(x, y)
    w.signals.result.connect(self.display_result)
    w.signals.error.connect(self.display_result)
    self.workers2.enqueue(w)
  def display_result(self, job_id, data):
    self.text.appendPlainText("WORKER %s: %s" % (job_id, data))

app = QApplication(sys.argv)
window = MainWindow()
app.exec_()

```

Hope that makes sense? Let me know if anything needs clarifying.
Thomas_Parker | 2020-10-05 08:39:07 UTC | #3
Awesome, can't thank you enough for taking the time to answer my questions complete with example code. thank you very much! :smiley:
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Pass multiple models to QListView** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pass-multiple-models-to-qlistview/Python books) on the subject. 
**Pass multiple models to QListView** was published in [faq](https://www.pythonguis.com/faq/) on October 01, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
