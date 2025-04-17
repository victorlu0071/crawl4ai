# Content from: https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/

[](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PySide2 ](https://www.pythonguis.com/pyside2/)
  * [PySide2 Tutorial ](https://www.pythonguis.com/pyside2-tutorial/)
  * Basics
  * [Create a PySide2 app](https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/)
  * [PySide2 Signals](https://www.pythonguis.com/tutorials/pyside-signals-slots-events/)
  * [PySide2 Widgets](https://www.pythonguis.com/tutorials/pyside-widgets/)
  * [PySide2 Layouts](https://www.pythonguis.com/tutorials/pyside-layouts/)
  * [PySide2 Menus](https://www.pythonguis.com/tutorials/pyside-actions-toolbars-menus/)
  * [PySide2 Dialogs](https://www.pythonguis.com/tutorials/pyside-dialogs/)
  * [Multi-window PySide2](https://www.pythonguis.com/tutorials/pyside-creating-multiple-windows/)
  * Qt Designer
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/)
  * [The QResource System in PySide2](https://www.pythonguis.com/tutorials/pyside-qresource-system/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/pyside-qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/pyside-modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/pyside-qtableview-modelviews-numpy-pandas/)
  * Plotting
  * [Plotting With PyQtGraph and PySide2](https://www.pythonguis.com/tutorials/pyside-plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PySide2](https://www.pythonguis.com/tutorials/pyside-plotting-matplotlib/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/pyside-bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/pyside-creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/pyside-animated-widgets/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/pyside-embed-pyqtgraph-custom-widgets/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/pyside-transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/pyside-system-tray-mac-menu-bar-applications/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyside2-applications-windows-pyinstaller/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyside2-applications-pyinstaller-macos-dmg/)
  * [Packaging QResources](https://www.pythonguis.com/tutorials/packaging-data-files-pyside2-with-qresource-system/)
  * [Packaging with fbs](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/)
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


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Multithreading PySide2 applications with QThreadPool
Run background tasks concurrently without impacting your UI
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 04 PySide2 [ Threads & Processes ](https://www.pythonguis.com/pyside2-tutorial/#pyside-concurrent-execution)
#### [ PySide2 Tutorial ](https://www.pythonguis.com/pyside2-tutorial/) — [Threads & Processes](https://www.pythonguis.com/pyside2-tutorial/#pyside-concurrent-execution)
  * [Multithreading PySide2 applications with QThreadPool](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/)
  * [Using QProcess to Run External Programs in PySide2](https://www.pythonguis.com/tutorials/pyside-qprocess-external-programs/)


This tutorial is also available for [PySide6](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/) , [PyQt6](https://www.pythonguis.com/tutorials/multithreading-pyqt6-applications-qthreadpool/) and [PyQt5](https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/)
A common problem when building Python GUI applications is "locking up" of the interface when attempting to perform long-running background tasks. In this tutorial I'll cover one of the simplest ways to achieve concurrent execution in PySide2.
If you're looking to run external _programs_ (such as command line utilities) from your applications, check out the [Using `QProcess` to run external programs](https://www.pythonguis.com/tutorials/pyside-qprocess-external-programs/) tutorial.
Table of Contents
  * [Background](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/#background)
  * [Preparation](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/#preparation)
  * [The dumb approach](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/#the-dumb-approach)
  * [Threads and Processes](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/#threads-and-processes)
  * [QRunnable and the QThreadPool](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/#qrunnable-and-the-qthreadpool)
  * [Improved QRunnables](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/#improved-qrunnables)
  * [Thread IO](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/#thread-io)
  * [The complete code](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/#the-complete-code)
  * [Caveats](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/#caveats)


## Background
Applications based on Qt (like most GUI applications) are _event based_. This means that execution is driven in response to user interaction, signals and timers. In an event-driven application, clicking on a button creates an _event_ which your application subsequently _handles_ to produce some expected output. Events are pushed onto and taken off an event queue and processed sequentially.
python ```
app = QApplication([])
window = MainWindow()
app.exec_()

```

The event loop is started by calling `.exec_()` on your `QApplication` object and runs within the same thread as your Python code. The thread which runs this event loop — commonly referred to as the _GUI thread_ — also handles all window communication with the host operating system.
By default, any execution triggered by the event loop will also run synchronously within this thread. In practise this means that any time your PySide application spends _doing something_ in your code, window communication and GUI interaction are frozen.
If what you're doing is simple, and returns control to the GUI loop quickly, this freeze will be imperceptible to the user. However, if you need to perform longer-running tasks, for example opening/writing a large file, downloading some data, or rendering some complex image, there are going to be problems. To your user the application will appear to be unresponsive (because it is). Because your app is no longer communicating with the OS, on MacOS X if you click on your app you will see the spinning wheel of death. And, _nobody_ wants that.
The solution is simple: get your work out of the _GUI thread_ (and into another thread). PySide (via Qt) provides an straightforward interface to do exactly that. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
## Preparation
The following code will work with both Python 2.7 and Python 3.
To demonstrate multi-threaded execution we need an application to work with. Below is a minimal stub application for PySide which will allow us to demonstrate multithreading, and see the outcome in action. Simply copy and paste this into a new file, and save it with an appropriate filename like `multithread.py`. The remainder of the code will be added to this file (there is also a complete working example at the bottom if you're impatient).
python ```
from PySide2.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide2.QtCore import QTimer
import sys
import time
class MainWindow(QMainWindow):

  def __init__(self):
    super().__init__()
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
    self.timer = QTimer()
    self.timer.setInterval(1000)
    self.timer.timeout.connect(self.recurring_timer)
    self.timer.start()
  def oh_no(self):
    time.sleep(5)
  def recurring_timer(self):
    self.counter +=1
    self.l.setText("Counter: %d" % self.counter)

app = QApplication(sys.argv)
window = MainWindow()
app.exec_()

```

Run the file as for any other Python/PySide application:
bash ```
python3 multithread.py

```

You should see a demonstration window with a number counting upwards. This a generated by a simple recurring time, firing once per second. Think of this as our _event loop indicator_ , a simple way to let us known that out application is ticking over normally. There is also a button with the word **"DANGER!"**. Push it.
You'll notice that each time you push the button the counter stops ticking and your application freezes entirely. On Windows you may see the window turn pale, indicating it is not responding, while on a Mac you'll get the spinning wheel of death.
## The dumb approach
Don't do this. Ever.
What appears as a _frozen_ interface is the main Qt event loop being blocked from processing (and responding to) window events. Your clicks on the window as still registered by the host OS and sent to your application, but because it's sat in your big ol' lump of code (`time.sleep`), it can't accept or react to them. They have to wait until your code passes control back to Qt.
The simplest, and perhaps most logical, way to get around this is to accept events from within your code. This allows Qt to continue to respond to the host OS and your application will stay responsive. You can do this easily by using the static `.processEvents()` function on the `QApplication` class. Simply add a line like the following, somewhere in your long-running code block:
python ```
QApplication.processEvents()

```

For example _long running_ code `time.sleep` we could break that down into 5x 1-second sleeps and insert the `.processEvents` in between. The code for this would be:
python ```
def oh_no(self):
  for n in range(5):
    QApplication.processEvents()
    time.sleep(1)

```

Now when you push the button your code is entered as before. However, now `QApplication.processEvents()` intermittently passes control back to Qt, and allows it to respond to events as normal. Qt will then accept events _and handle them_ before returning to run the remainder of your code.
This works, but it's horrible for a couple of reasons.
Firstly, when you pass control back to Qt, your code is no longer running. This means that whatever long-running thing you're trying to do will take _longer_. That is definitely not what you want.
Secondly, processing events outside the main event loop (`app.exec_()`) causes your application to branch off into handling code (e.g. for triggered slots, or events) while within your loop. If your code depends on/responds to external state this can cause undefined behavior. The code below demonstrates this in action:
python ```
from PySide2.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
import sys
import time
class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.counter = 0
    layout = QVBoxLayout()
    self.l = QLabel("Start")
    b = QPushButton("DANGER!")
    b.pressed.connect(self.oh_no)
    c = QPushButton("?")
    c.pressed.connect(self.change_message)
    layout.addWidget(self.l)
    layout.addWidget(b)
    layout.addWidget(c)
    w = QWidget()
    w.setLayout(layout)
    self.setCentralWidget(w)
    self.show()
  def change_message(self):
    self.message = "OH NO"
  def oh_no(self):
    self.message = "Pressed"
    for n in range(100):
      time.sleep(0.1)
      self.l.setText(self.message)
      QApplication.processEvents()

app = QApplication(sys.argv)
window = MainWindow()
app.exec_()

```

If you run this code you'll see the counter as before. Pressing "DANGER!" will change the displayed text to "Pressed", as defined at the entry point to the `oh_no` function. However, if you press the "?" button while `oh_no` is still running you'll see that the message changes. State is being changed from outside your loop.
This is a toy example. However, if you have multiple long-running processes within your application, with each calling `QApplication.processEvents()` to keep things ticking, your application behaviour can be unpredictable.
## Threads and Processes
If you take a step back and think about what you want to happen in your application, it can probably be summed up with "stuff to happen at the same time as other stuff happens".
There are two main approaches to running independent tasks within a PySide application: _threads_ and _processes_.
_Threads_ share the same memory space, so are quick to start up and consume minimal resources. The shared memory makes it trivial to pass data between threads, however reading/writing memory from different threads can lead to race conditions or segfaults. In a Python GUI there is the added issue that multiple threads are bound by the same Global Interpreter Lock (GIL) — meaning non-GIL-releasing Python code can only execute in one thread at a time. However, this is not a major issue with PySide where most of the time is spent outside of Python.
_Processes_ use separate memory space (and an entirely separate Python interpreter). This side-steps any potential problems with the GIL, but at the cost of slower start-up times, larger memory overhead and complexity in sending/receiving data.
For simplicity's sake it usually makes sense to use threads, unless you have a good reason to use processes (see [caveats](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/#caveats) later). Subprocesses in Qt are better suited to running and communicating with external programs.
There is nothing stopping you using pure-Python threading or process-based approaches within your PySide application.
## QRunnable and the QThreadPool
Do this.
Qt provides a very simple interface for running jobs in other threads, which is exposed nicely in PySide. This is built around two classes: `QRunnable` and `QThreadPool`. The former is the container for the work you want to perform, while the latter is the method by which you pass that work to alternate threads.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
The neat thing about using `QThreadPool` is that it handles queuing and execution of workers for you. Other than queuing up jobs and retreiving the results there is not very much to do at all.
To define a custom `QRunnable` you can subclass the base `QRunnable` class, then place the code you wish you execute within the `run()` method. The following is an implementation of our long running `time.sleep` job as a `QRunnable`. Add the following code to `multithread.py`, above the `MainWindow` class definition.
python ```
from PySide2.QtCore import QRunnable, Slot, QThreadPool
class Worker(QRunnable):
  '''
  Worker thread
  '''
  @Slot() # QtCore.Slot
  def run(self):
    '''
    Your code goes in this function
    '''
    print("Thread start")
    time.sleep(5)
    print("Thread complete")

```

Executing our function in another thread is simply a matter of creating an instance of the `Worker` and then pass it to our `QThreadPool` instance and it will be executed automatically.
Next add the following within the `__init__` block, to set up our thread pool.
python ```
self.threadpool = QThreadPool()
print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

```

Finally, add the following lines to our `oh_no` function.
python ```
def oh_no(self):
  worker = Worker()
  self.threadpool.start(worker)

```

Now, clicking on the button will create a worker to handle the (long-running) process and spin that off into another thread via thread pool. If there are not enough threads available to process incoming workers, they'll be queued and executed in order at a later time.
Try it out and you'll see that your application now handles you bashing the button with no problems.
Check what happens if you hit the button multiple times. You should see your threads executed immediately _up to_ the number reported by `.maxThreadCount`. If you hit the button again after there are already this number of active workers, the subsequent workers will be queued until a thread becomes available.
## Improved QRunnables
If you want to pass custom data into the execution function you can do so via the init, and then have access to the data via `self.` from within the `run` slot.
python ```
class Worker(QRunnable):
  '''
  Worker thread
  :param args: Arguments to make available to the run code
  :param kwargs: Keywords arguments to make available to the run code
  '''
  def __init__(self, *args, **kwargs):
    super().__init__()
    self.args = args
    self.kwargs = kwargs
  @Slot() # QtCore.Slot
  def run(self):
    '''
    Initialise the runner function with passed self.args, self.kwargs.
    '''
    print(args, kwargs)

```

In fact, we can take avantage of the fact that in Python functions are objects and pass in the function to execute rather than subclassing each time. In the following construction we only require a single `Worker` class to handle all of our execution jobs.
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
  @Slot() # QtCore.Slot
  def run(self):
    '''
    Initialise the runner function with passed args, kwargs.
    '''
    self.fn(*self.args, **self.kwargs)

```

You can now pass in any Python function and have it executed in a separate thread.
python ```
def execute_this_fn(self):
  print("Hello!")
def oh_no(self):
  # Pass the function to execute
  worker = Worker(self.execute_this_fn) # Any other args, kwargs are passed to the run function
  # Execute
  self.threadpool.start(worker)

```

## Thread IO
Sometimes it's helpful to be able to pass back _state_ and _data_ from running workers. This could include the outcome of calculations, raised exceptions or ongoing progress (think progress bars). Qt provides the _signals and slots_ framework which allows you to do just that and is thread-safe, allowing safe communication directly from running threads to your GUI frontend. _Signals_ allow you to `.emit` values, which are then picked up elsewhere in your code by _slot_ functions which have been linked with `.connect`.
Below is a simple `WorkerSignals` class defined to contain a number of example signals.
Custom signals can only be defined on objects derived from `QObject`. Since `QRunnable` is not derived from `QObject` we can't define the signals there directly. A custom QObject to hold the signals is the simplest solution.
python ```
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
  '''
  finished = Signal() # QtCore.Signal
  error = Signal(tuple)
  result = Signal(object)

```

In this example we've defined 3 custom signals:
  1. _finished_ signal, with no data to indicate when the task is complete.
  2. _error_ signal which receives a `tuple` of `Exception` type, `Exception` value and formatted traceback.
  3. _result_ signal receiving any `object` type from the executed function.


You may not find a need for all of these signals, but they are included to give an indication of what is possible. In the following code we're going to implement a long-running task that makes use of these signals to provide useful information to the user.
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
    self.signals = WorkerSignals()
  @Slot() # QtCore.Slot
  def run(self):
    '''
    Initialise the runner function with passed args, kwargs.
    '''
    # Retrieve args/kwargs here; and fire processing using them
    try:
      result = self.fn(
        *self.args, **self.kwargs
        status=self.signals.status
        progress=self.signals.progress
      )
    except:
      traceback.print_exc()
      exctype, value = sys.exc_info()[:2]
      self.signals.error.emit((exctype, value, traceback.format_exc()))
    else:
      self.signals.result.emit(result) # Return the result of the processing
    finally:
      self.signals.finished.emit() # Done

```

You can connect your own handler functions to these signals to receive notification of completion (or the result) of threads.
python ```
def execute_this_fn(self):
  for n in range(0, 5):
    time.sleep(1)
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
  # Execute
  self.threadpool.start(worker)

```

You also often want to receive status information from long-running threads. This can be done by passing in _callbacks_ to which your running code can send the information. You have two options here: either define new signals (allowing the handling to be performed using the event loop) or use a standard Python function.
In both cases you'll need to pass these callbacks into your target function to be able to use them. The signal-based approach is used in the completed code below, where we pass an `int` back as an indicator of the thread's % progress.
## The complete code
A complete working example is given below, showcasing the custom `QRunnable` worker together with the worker & progress signals. You should be able to easily adapt this code to any multithreaded application you develop.
python ```
from PySide2.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide2.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThreadPool
import sys
import time
import traceback

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
  finished = Signal()
  error = Signal(tuple)
  result = Signal(object)
  progress = Signal(int)


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
  @Slot()
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

app = QApplication(sys.argv)
window = MainWindow()
app.exec_()

```

## Caveats
You may have spotted the slight flaw in this master plan — we are still making use of the event loop (and the _GUI thread_) to process the output of our workers.
This isn't a problem when we're simply tracking progress, completion or returning metadata. However, if you have workers which return large amounts of data — e.g. loading large files, performing complex analysis and need (large) results, or querying databases — passing this data back through the GUI thread may cause performance problems and is best avoided.
Similarly, if your application makes use of a large number of threads and Python result handlers, you may come up against the limitations of the GIL. As mentioned previously, when using threads execution of Python is limited to a single thread at one time. The Python code that handles signals from your threads can be blocked by your workers and _vice versa_. Since blocking your slot functions blocks the event loop, this can directly impact GUI responsiveness.
In these cases it is often better to investigate using a pure-Python thread pool (e.g. concurrent futures) to keep your processing and thread-event handling further isolated from your GUI. However, note that _any_ Python GUI code can block other Python code unless it's in a separate process. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
Continue with [ PySide2 Tutorial ](https://www.pythonguis.com/tutorials/pyside-qprocess-external-programs/ "Continue to next part")
Return to [Create Desktop GUI Applications with PySide2 ](https://www.pythonguis.com/pyside2-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Multithreading PySide2 applications with QThreadPool** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/Python books) on the subject. 
**Multithreading PySide2 applications with QThreadPool** was published in [tutorials](https://www.pythonguis.com/tutorials/) on August 15, 2019 (updated April 04, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[multithreading](https://www.pythonguis.com/topics/multithreading/) [responsive](https://www.pythonguis.com/topics/responsive/) [gui](https://www.pythonguis.com/topics/gui/) [threading](https://www.pythonguis.com/topics/threading/) [qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [concurrency](https://www.pythonguis.com/topics/concurrency/) [performance](https://www.pythonguis.com/topics/performance/) [python](https://www.pythonguis.com/topics/python/)
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
