# Content from: https://www.pythonguis.com/faq/delay-in-signal-from-thread/

[](https://www.pythonguis.com/faq/delay-in-signal-from-thread/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
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
  * [PyQt5](https://www.pythonguis.com/pyqt5/)
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Delay in signal from thread
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ FAQ ](https://www.pythonguis.com/faq/)
Minsky | 2021-04-08 19:11:24 UTC | #1
I'm having trouble with sending a signal from a thread within an app that I'm writing.
To keep things simple, let's assume that the app consists of a main window which contains just a push button and a status bar, and has four classes - the MainWindow class, a Signals class, a Model class - which holds the logic functions, and a Worker class which is used to run separate threads.
When the push button is pressed, it connects to the 'call_do_this' function which starts a thread that calls the 'do_this' function in the separate Model class. The 'do_this function' emits a signal containing a message to be displayed in the main window status bar, and then continues with a long running process (around 14 seconds).
The simplistic code is displayed below:
[code] class Worker(QRunnable): def **init**(self, fn=None, _args,_ *kwargs): super().**init**()
python ```
      self.fn = fn
      self.args = args
      self.kwargs = kwargs
    def run(self):
      if self.fn is not None:
        self.fn(*self.args, **self.kwargs)

  class Signals(QObject):
    status = pyqtSignal(str)

  class MainWindow(QMainWindow):
    def __init__(self):
      super().__init__()
      self.threadpool = QThreadPool()
      self.model = Model()
      self.model.signals.status.connect(self.update_status_bar)
      self.button = QPushButton()
      self.button.pressed.connect(self.call_do_this)
    def call_do_this(self):
      self.worker = Worker(self.model.do_this)
      self.threadpool.start(self.worker)
    def update_status_bar(self, msg):
      self.statusBar().showMessage(msg)

  class Model(QObject):
    def __init__(self):
      super().__init__()
      self.signals = Signals()
    def do_this(self):
      self.signals.status.emit('This is a message')
      # continue with long running function

```

[/code] 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyside2-book/) _by Martin Fitzpatrick_ — (PySide2 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside2-book/) [Get the book](https://secure.pythonguis.com/01hf778jyaajk5vk1q6824sd44/)
The error that occurs, is that the status bar message should be displayed as soon as the 'do_this' function starts, but is displayed only after the function ends. What am I doing wrong?
PedanticHacker | 2021-04-08 23:55:19 UTC | #2
Hello, Minsky, welcome to the forum! :)
If you're using PyQt6 (or the latest version of PyQt5, at least version 5.15), the `QThreadPool` class has the method `start` that can also call any function, and `QThreadPool` reserves a thread and uses it to run the function that you pass to that `start` method. More about it [HERE](https://doc.qt.io/qt-5/qthreadpool.html#start-1).
You don't need to have a runnable at all, just pass your function to `start`, like in your case the `do_this` function of your `Model` class: `self.threadpool.start(self.model.do_this)`. Also, always instanciate a `QThreadPool` class **after** all the signals have been connected to slots.
So, in `__init__` of `MainWindow`:
python ```
self.model = Model()
self.model.signals.status.connect(self.update_status_bar)
self.button = QPushButton()
self.button.pressed.connect(self.call_do_this)
self.threadpool = QThreadPool()

```

The `QThreadPool.start` method of PySide doesn't provide calling a regular function, just of PyQt5 from version 5.15 onward and, of course, of PyQt6.
I hope this helps in any way.
Minsky | 2021-04-08 23:59:17 UTC | #3
Thanks PedanticHacker, that did the trick. However, if I change the code so that arguments are passed into the 'do_this' function, then this freezes the main event loop, making the GUI unresponsive until the function ends. I can't work out why this happens or how to solve it.
[code] class MainWindow(QMainWindow): def **init**(self): super().**init**()
python ```
    self.model = Model()
    self.model.signals.status.connect(self.update_status_bar)
    button = QPushButton()
    button.pressed.connect(self.call_do_this)
    self.threadpool = QThreadPool()
  def call_do_this(self):
    worker = Worker(self.model.do_this('This is a message'))
    self.threadpool.start(worker)
  def update_status_bar(self, msg):
    self.statusBar().showMessage(msg)

class Model(QObject):
  def __init__(self):
    super().__init__()
    self.signals = Signals()
  def do_this(self, msg):
    self.signals.status.emit(msg)
    # continue with long running function

```

[/code]
This has got me totally stumped. Any help would be very welcome. I'm using PyQt5 5.13.1, so unfortunately, I end up with a segmentation fault if I don't use a QRunnable.
PedanticHacker | 2021-04-09 07:46:04 UTC | #4
Can you try updating PyQt to version 5.15.3 and trying `self.threadpool.start(do_this)`?
passing a regular function to `start` (as opposed to passing a runnable) of `QThreadPool` class was introduced in PyQt in version 5.15. Your version of PyQt doesn't have that ability yet. That's why you get a SegmentationFault.
Minsky | 2021-04-09 11:27:15 UTC | #5
I've tried updating PyQt but I'm getting conflict messages regarding dependencies. I prefer to stick with the current version until I upgrade the OS in June. Can you think of a reason why passing the function with arguments locks the main event loop, while passing the same function without arguments works fine?
PedanticHacker | 2021-04-09 12:21:05 UTC | #6
python ```
class Worker(QRunnable):
  '''
  Worker thread
  Inherits from QRunnable to handler worker thread setup, signals and wrap-up.
  :param callback: The function callback to run on this worker thread. Supplied args and
           kwargs will be passed through to the runner.
  :type callback: function
  :param args: Arguments to pass to the callback function
  :param kwargs: Keywords to pass to the callback function
  '''
  def __init__(self, fn, *args, **kwargs):
    super().__init__()
    # Store constructor arguments (re-used for processing)
    self.fn = fn
    self.args = args
    self.kwargs = kwargs
  @pyqtSlot()
  def run(self):
    '''
    Initialise the runner function with passed args, kwargs.
    '''
    self.fn(*self.args, **self.kwargs)

```

The code above was taken from [THIS](https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/) article written by our fellow Martin Fitzpatrick (@martin).
A possible culprit in your code is that you don't decorate the `run` method of your `Worker` class with `@pyqtSlot()`. I think I read a post on some other forum that this is needed when subclassing QRunnable. Try it out and tell me if it works. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
python ```
class Worker(QRunnable):
  ...
  @pyqtSlot() # A cruical part!
  def run(self):
    ...

```

Minsky | 2021-04-09 14:34:36 UTC | #7
I've discovered the cause of the error, but not the reason for it. If the 'do_this' function is passed without arguments to the Worker, it is passed as a 'method'=""> and runs in a separate thread as expected. However, if it is passed with arguments, it for some reason, becomes a 'nonetype'=""> and somehow runs in the main thread instead, therefore locking the main event loop until it ends.
[code] @pyqtSlot() def run(self): print(type(self.fn)) if self.fn is not None: self.fn(_self.args,_ *self.kwargs) [/code]
I haven't a clue why this is happening. Any ideas?
PedanticHacker | 2021-04-09 16:25:56 UTC | #8
Try removing the default `None` value of the `fn` parameter in the `__init__` method signature in the `Worker` class.
So, instead of `def __init__(self, fn=None, *args, **kwargs):`, have that as `def __init__(self, fn, *args, **kwargs):`.
Then in the body of the `run` method in the `Worker` class, remove the `if` statement. So, let it be like this:
python ```
@pyqtSlot()
def run(self):
  self.fn(*self.args, **self.kwargs)

```

Maybe this helps?
PedanticHacker | 2021-04-09 16:45:34 UTC | #9
If you still don't succeed, study this code, provided by our good friend Martin Fitzpatrick (@martin):
python ```
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import traceback, sys

class WorkerSignals(QObject):
  '''
  Defines the signals available from a running worker thread.
  Supported signals are:
  finished
    No data
  error
    tuple (exctype, value, traceback.format_exc() )
  result
    object data returned from processing, anything
  progress
    int indicating % progress
  '''
  finished = pyqtSignal()
  error = pyqtSignal(tuple)
  result = pyqtSignal(object)
  progress = pyqtSignal(int)

class Worker(QRunnable):
  '''
  Worker thread
  Inherits from QRunnable to handler worker thread setup, signals and wrap-up.
  :param callback: The function callback to run on this worker thread. Supplied args and
           kwargs will be passed through to the runner.
  :type callback: function
  :param args: Arguments to pass to the callback function
  :param kwargs: Keywords to pass to the callback function
  '''
  def __init__(self, fn, *args, **kwargs):
    super().__init__()
    # Store constructor arguments (re-used for processing)
    self.fn = fn
    self.args = args
    self.kwargs = kwargs
    self.signals = WorkerSignals()
    # Add the callback to our kwargs
    self.kwargs['progress_callback'] = self.signals.progress
  @pyqtSlot()
  def run(self):
    '''
    Initialise the runner function with passed args, kwargs.
    '''
    # Retrieve args/kwargs here; and fire processing using them
    try:
      result = self.fn(*self.args, **self.kwargs)
    except:
      traceback.print_exc()
      exctype, value = sys.exc_info()[:2]
      self.signals.error.emit((exctype, value, traceback.format_exc()))
    else:
      self.signals.result.emit(result) # Return the result of the processing
    finally:
      self.signals.finished.emit() # Done

class MainWindow(QMainWindow):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.counter = 0
    layout = QVBoxLayout()
    self.l = QLabel("Start")
    b = QPushButton("DANGER!")
    b.pressed.connect(self.oh_no)
    layout.addWidget(self.l)
    layout.addWidget(b)
    w = QWidget()
    w.setLayout(layout)
    self.setCentralWidget(w)
    self.show()
    self.threadpool = QThreadPool()
    print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
    self.timer = QTimer()
    self.timer.setInterval(1000)
    self.timer.timeout.connect(self.recurring_timer)
    self.timer.start()
  def progress_fn(self, n):
    print("%d%% done" % n)
  def execute_this_fn(self, progress_callback):
    for n in range(0, 5):
      time.sleep(1)
      progress_callback.emit(n*100/4)
    return "Done."
  def print_output(self, s):
    print(s)
  def thread_complete(self):
    print("THREAD COMPLETE!")
  def oh_no(self):
    # Pass the function to execute
    worker = Worker(self.execute_this_fn) # Any other args, kwargs are passed to the run function
    worker.signals.result.connect(self.print_output)
    worker.signals.finished.connect(self.thread_complete)
    worker.signals.progress.connect(self.progress_fn)
    # Execute
    self.threadpool.start(worker)

  def recurring_timer(self):
    self.counter +=1
    self.l.setText("Counter: %d" % self.counter)

app = QApplication([])
window = MainWindow()
app.exec_()

```

Minsky | 2021-04-09 17:11:56 UTC | #10
Solved it! The Worker class '**init** ' function expects a **function name** with the arguments separated by commas, whereas I was passing a **function call** with arguments. The code below fixed the problem,
Instead of this:
[code] def call_do_this(self): worker = Worker(self.model.do_this('This is a message')) # Passing function call self.threadpool.start(worker) [/code]
Do this:
[code] def call_do_this(self): worker = Worker(self.model.do_this, 'This is a message') # Passing function name with self.threadpool.start(worker) # comma separated argument [/code]
@ PedanticHacker: Thank you for your help in getting this problem solved, it was greatly appreciated. Hopefully this thread :grinning: may help prevent others from making a similar mistake.
PedanticHacker | 2021-04-09 17:14:48 UTC | #11
Wow, congratz, the beast has been slayed! 👍 Good job! We all learn as we go, don't we? 😉
I'm proud of you, keep up the good work. 🙂
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Delay in signal from thread** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/delay-in-signal-from-thread/Python books) on the subject. 
**Delay in signal from thread** was published in [faq](https://www.pythonguis.com/faq/) on April 08, 2021 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [threads](https://www.pythonguis.com/topics/threads/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
