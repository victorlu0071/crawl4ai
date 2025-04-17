# Content from: https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/

[](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/#menu)
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
# Multithreading PySide6 applications with QThreadPool
Run background tasks concurrently without impacting your UI
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 08 PySide6 [ Threads & Processes in PyQt6 ](https://www.pythonguis.com/pyside6-tutorial/#pyside6-concurrent-execution)
#### [ PySide6 Tutorial ](https://www.pythonguis.com/pyside6-tutorial/) — [Threads & Processes in PyQt6](https://www.pythonguis.com/pyside6-tutorial/#pyside6-concurrent-execution)
  * [Multithreading PySide6 applications with QThreadPool](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/)
  * [Using QProcess to Run External Programs in PySide6](https://www.pythonguis.com/tutorials/pyside6-qprocess-external-programs/)


This tutorial is also available for [PyQt6](https://www.pythonguis.com/tutorials/multithreading-pyqt6-applications-qthreadpool/) , [PySide2](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/) and [PyQt5](https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/)
A common problem when building Python GUI applications is the interface "locking up" when attempting to perform long-running background tasks. In this tutorial, we'll cover quick ways to achieve concurrent execution in PySide6.
If you'd like to run external programs (such as command-line utilities) from your applications, check out the [Using `QProcess` to run external programs](https://www.pythonguis.com/tutorials/pyside6-qprocess-external-programs/) tutorial.
Table of Contents
  * [Background: The frozen GUI issue](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/#background-the-frozen-gui-issue)
  * [Preparation: A minimal stub app](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/#preparation-a-minimal-stub-app)
  * [The wrong approach](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/#the-wrong-approach)
  * [Use threads and processes](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/#use-threads-and-processes)
    * [QRunnable and the QThreadPool](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/#qrunnable-and-the-qthreadpool)
    * [Improved QRunnable](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/#improved-qrunnable)
  * [Thread Input/Output](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/#thread-inputoutput)
  * [The complete code](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/#the-complete-code)
  * [Caveats](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/#caveats)


## Background: The frozen GUI issue
Applications based on Qt (like most GUI applications) are based on _events_. This means that execution is driven in response to user interaction, signals, and timers. In an event-driven application, clicking a button creates an _event_ that your application subsequently _handles_ to produce some expected output. Events are pushed onto and taken off an event queue and processed sequentially.
In PySide6, we create an app with the following code:
python ```
app = QApplication([])
window = MainWindow()
app.exec()

```

The event loop starts when you call `.exec()` on the `QApplication` object and runs within the same thread as your Python code. The thread that runs this event loop — commonly referred to as the _GUI thread_ — also handles all window communication with the host operating system.
By default, any execution triggered by the event loop will also run synchronously within this thread. In practice, this means that the time your PySide6 application spends _doing something_ , the communication with the window and the interaction with the GUI are frozen.
If what you're doing is simple, and it returns control to the GUI loop quickly, the GUI freeze will be imperceptible to the user. However, if you need to perform _longer-running tasks_ , for example, opening and writing a large file, downloading some data, or rendering a high-resolution image, there are going to be problems.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
To your user, the application will appear to be unresponsive (because it is). Because your app is no longer communicating with the OS, on macOS, if you click on your app, you will see the spinning wheel of death. And, _nobody_ wants that.
The solution is to move your long-running tasks out of the GUI thread into another thread. PySide6 provides a straightforward interface for this.
## Preparation: A minimal stub app
To demonstrate multi-threaded execution, we need an application to work with. Below is a minimal stub application for PySide6 that will allow us to demonstrate multithreading and see the outcome in action. Simply copy and paste this into a new file and save it with an appropriate filename, like `multithread.py`. The remainder of the code will be added to this file. There is also a complete working example at the bottom if you're impatient:
python ```
import time
from PySide6.QtCore import (
  QTimer,
)
from PySide6.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QWidget,
)
class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.counter = 0
    layout = QVBoxLayout()
    self.label = QLabel("Start")
    button = QPushButton("DANGER!")
    button.pressed.connect(self.oh_no)
    layout.addWidget(self.label)
    layout.addWidget(button)
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
    self.counter += 1
    self.label.setText(f"Counter: {self.counter}")
app = QApplication([])
window = MainWindow()
app.exec()

```

Run the app as for any other Python application:
sh ```
$ python multithread.py

```

You will see a demonstration window with a number counting upwards. This count is generated by a simple recurring timer, firing once per second. Think of this as our _event loop indicator_ (or _GUI thread indicator_), a simple way to let us know that our application is ticking over normally. There is also a button with the word _"DANGER!_. Push it.
You'll notice that each time you push the button, the counter stops ticking, and your application freezes entirely. On Windows, you may see the window turn pale, indicating it is not responding, while on macOS, you'll get the spinning wheel of death.
## The _wrong_ approach
Avoid doing this in your code.
What appears as a _frozen_ interface is the main Qt event loop being blocked from processing (and responding to) window events. Your clicks on the window are still registered by the host OS and sent to your application, but because it's sat in your big ol' lump of code (calling `time.sleep()`), it can't accept or react to them. They have to wait until your code passes control back to Qt.
The quickest and perhaps most logical way to get around this issue is to accept events from within your code. This allows Qt to continue to respond to the host OS and your application will stay responsive. You can do this easily by using the static `processEvents()` method on the `QApplication` class.
For example, our _long-running_ code `time.sleep()` could be broken down into five 1-second sleeps and insert the `processEvents()` in between. The code for this would be:
python ```
def oh_no(self):
  for n in range(5):
    QApplication.processEvents()
    time.sleep(1)

```

Now, when you push the _DANGER!_ button, your app runs as before. However, now `QApplication.processEvents()` intermittently passes control back to Qt, and allows it to respond to events as normal. Qt will then accept events _and handle them_ before returning to run the remainder of your code.
This approach works, but it's horrible for a few reasons, including the following:
  1. When you pass control back to Qt, your code is no longer running. This means that whatever long-running task you're trying to do will take _longer_. That is definitely not what you want.
  2. When you have multiple long-running tasks within your application, with each calling `QApplication.processEvents()` to keep things ticking, your application's behavior can be unpredictable.
  3. Processing events outside the main event loop (`app.exec()`) causes your application to branch off into handling code (e.g. for triggered slots or events) while within your loop. If your code depends on or responds to an external state, then this can cause undefined behavior.


The code below demonstrates the last point in action:
python ```
import time
from PySide6.QtCore import (
  QTimer,
)
from PySide6.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QWidget,
)
class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.counter = 0
    layout = QVBoxLayout()
    self.label = QLabel("Start")
    button = QPushButton("DANGER!")
    button.pressed.connect(self.oh_no)
    c = QPushButton("?")
    c.pressed.connect(self.change_message)
    layout.addWidget(self.label)
    layout.addWidget(button)
    layout.addWidget(c)
    w = QWidget()
    w.setLayout(layout)
    self.setCentralWidget(w)
    self.show()
    self.timer = QTimer()
    self.timer.setInterval(1000)
    self.timer.timeout.connect(self.recurring_timer)
    self.timer.start()
  def change_message(self):
    self.message = "OH NO"
  def oh_no(self):
    self.message = "Pressed"
    for n in range(100):
      time.sleep(0.1)
      self.label.setText(self.message)
      QApplication.processEvents()
  def recurring_timer(self):
    self.counter += 1
    self.label.setText(f"Counter: {self.counter}")
app = QApplication([])
window = MainWindow()
app.exec()

```

If you run this code you'll see the counter as before. Pressing _DANGER!_ will change the displayed text to `"Pressed"`, as defined at the entry point to the `oh_no()` method. However, if you press the _"?"_ button while `oh_no()` is still running, you'll see that the message changes. The state is being changed from outside your event loop.
## Use threads and processes
If you take a step back and think about what you want to happen in your application, then you can probably sum it up with "stuff to happen at the same time as other stuff happens".
There are two main approaches to running independent tasks within a PySide6 application:
  1. Threads
  2. Processes


**Threads** share the same memory space, so they are quick to start up and consume minimal resources. The shared memory makes it trivial to pass data between threads. However, reading or writing memory from different threads can lead to race conditions or segfaults.
In Python, there is the added issue that multiple threads are bound by the Global Interpreter Lock (GIL) — meaning non-GIL-releasing Python code can only execute in one thread at a time. However, this is not a major issue with PySide6, where most of the time is spent outside of Python.
**Processes** use separate memory space and an entirely separate Python interpreter. They sidestep any potential problems with Python's GIL but at the cost of slower start-up times, larger memory overhead, and complexity in sending and receiving data.
Processes in Qt are well suited to running and communicating with external programs. However, for simplicity's sake, threads are usually the best choice unless you have a good reason to use processes (see [caveats](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/#caveats) later).
There is nothing stopping you from using pure Python threading or process-based approaches within your PySide6 application. In the following sections, though, you'll rely on Qt's threading classes.
### `QRunnable` and the `QThreadPool`
Favor this approach in your code.
Qt provides a straightforward interface for running jobs or tasks in other threads, which is nicely supported in PySide6. This interface is built around two classes: 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
  1. `QRunnable`: The container for the work you want to perform.
  2. `QThreadPool`: The method by which you pass that work to alternate threads.


The neat thing about using `QThreadPool` is that it handles queuing and executing workers for you. Other than queuing up jobs and retrieving the results, there is not much to do.
To define a custom `QRunnable`, you can subclass the base `QRunnable` class. Then, place the code you wish you execute within the `run()` method. The following is an implementation of our long-running `time.sleep()` job as a `QRunnable`.
Go ahead and add the following code to `multithread.py`, above the `MainWindow` class definition, and don't forget to import `QRunnable` and `Slot` from `PySide6.QtCore`:
python ```
class Worker(QRunnable):
  """Worker thread."""
  @Slot()
  def run(self):
    """Your long-running job goes in this method."""
    print("Thread start")
    time.sleep(5)
    print("Thread complete")

```

Executing our long-running job in another thread is simply a matter of creating an instance of the `Worker` and passing it to our `QThreadPool` instance. It will be executed automatically.
Next, import `QThreadPool` from `PySide6.QtCore` and add the following code to the `__init__()` method to set up our thread pool:
python ```
self.threadpool = QThreadPool()
thread_count = self.threadpool.maxThreadCount()
print(f"Multithreading with maximum {thread_count} threads")

```

Finally, update the `oh_no()` method as follows:
python ```
def oh_no(self):
  worker = Worker()
  self.threadpool.start(worker)

```

Now, clicking the _DANGER!_ button will create a worker to handle the (long-running) job and spin that off into another thread via thread pool. If there are not enough threads available to process incoming workers, they'll be queued and executed in order at a later time.
Try it out, and you'll see that your application now handles you bashing the button with no problems.
Check what happens if you hit the button multiple times. You should see your threads executed immediately _up to_ the number reported by `maxThreadCount()`. If you press the button again after there are already this number of active workers, then the subsequent workers will be queued until a thread becomes available.
### Improved `QRunnable`
If you want to pass custom data into the runner function, you can do so via `__init__()`, and then have access to the data via `self` from within the `run()` slot:
python ```
class Worker(QRunnable):
  """Worker thread.
  :param args: Arguments to make available to the run code
  :param kwargs: Keywords arguments to make available to the run code
  """
  def __init__(self, *args, **kwargs):
    super().__init__()
    self.args = args
    self.kwargs = kwargs
  @Slot()
  def run(self):
    """Initialise the runner function with passed self.args, self.kwargs."""
    print(self.args, self.kwargs)

```

We can take advantage of the fact that Python functions are objects and pass in the function to execute rather than subclassing `QRunnable` for each runner function. In the following construction, we only require a single `Worker` class to handle all of our jobs:
python ```
class Worker(QRunnable):
  """Worker thread.
  Inherits from QRunnable to handler worker thread setup, signals and wrap-up.
  :param callback: The function callback to run on this worker thread.
           Supplied args and kwargs will be passed through to the runner.
  :type callback: function
  :param args: Arguments to pass to the callback function
  :param kwargs: Keywords to pass to the callback function
  """
  def __init__(self, fn, *args, **kwargs):
    super().__init__()
    self.fn = fn
    self.args = args
    self.kwargs = kwargs
  @Slot()
  def run(self):
    """Initialise the runner function with passed args, kwargs."""
    self.fn(*self.args, **self.kwargs)

```

You can now pass in any Python function and have it executed in a separate thread. Go ahead and update `MainWindow` with the following code:
python ```
def execute_this_fn(self):
  print("Hello!")
def oh_no(self):
  # Pass the function to execute
  worker = Worker(
    self.execute_this_fn
  ) # Any other args, kwargs are passed to the run function
  # Execute
  self.threadpool.start(worker)

```

Now, when you click _DANGER!_ , the app will print `Hello!` to your terminal without affecting the counter.
## Thread Input/Output
Sometimes, it's helpful to be able to pass back _state_ and _data_ from running workers. This could include the outcome of calculations, raised exceptions, or ongoing progress (maybe for progress bars). Qt provides the _signals and slots_ framework to allow you to do just that. Qt's signals and slots are thread-safe, allowing safe communication directly from running threads to your GUI thread.
_Signals_ allow you to emit values, which are then picked up elsewhere in your code by _slot_ functions that have been linked with the `connect()` method.
Below is a custom `WorkerSignals` class defined to contain a number of example signals. Note that custom signals can only be defined on objects derived from `QObject`. Since `QRunnable` is not derived from `QObject` we can't define the signals there directly. A custom `QObject` to hold the signals is a quick solution:
python ```
class WorkerSignals(QObject):
  """Signals from a running worker thread.
  finished
    No data
  error
    tuple (exctype, value, traceback.format_exc())
  result
    object data returned from processing, anything
  """
  finished = Signal()
  error = Signal(tuple)
  result = Signal(object)

```

In this code, we've defined three custom signals:
  1. `finished`, which receives no data and is aimed to indicate when the task is complete.
  2. `error`, which receives a `tuple` of `Exception` type, `Exception` value, and formatted traceback.
  3. `result`, which receives any `object` type from the executed function.


You may not find a need for all of these signals, but they are included to give an indication of what is possible. In the following code, we're going to implement a long-running task that makes use of these signals to provide useful information to the user:
python ```
class Worker(QRunnable):
  """Worker thread.
  Inherits from QRunnable to handler worker thread setup, signals and wrap-up.
  :param callback: The function callback to run on this worker thread.
           Supplied args and
           kwargs will be passed through to the runner.
  :type callback: function
  :param args: Arguments to pass to the callback function
  :param kwargs: Keywords to pass to the callback function
  """
  def __init__(self, fn, *args, **kwargs):
    super().__init__()
    self.fn = fn
    self.args = args
    self.kwargs = kwargs
    self.signals = WorkerSignals()
  @Slot()
  def run(self):
    """Initialise the runner function with passed args, kwargs."""
    # Retrieve args/kwargs here; and fire processing using them
    try:
      result = self.fn(*self.args, **self.kwargs)
    except Exception:
      traceback.print_exc()
      exctype, value = sys.exc_info()[:2]
      self.signals.error.emit((exctype, value, traceback.format_exc()))
    else:
      self.signals.result.emit(result) # Return the result of the processing
    finally:
      self.signals.finished.emit() # Done

```

You can connect your own handler functions to the signals to receive notification of completion (or the result) of threads:
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
  worker = Worker(
    self.execute_this_fn
  ) # Any other args, kwargs are passed to the run function
  worker.signals.result.connect(self.print_output)
  worker.signals.finished.connect(self.thread_complete)
  # Execute
  self.threadpool.start(worker)

```

You also often want to receive status information from long-running threads. This can be done by passing in _callbacks_ to which your running code can send the information. You have two options here:
  1. Define new signals, allowing the handling to be performed using the event loop
  2. Use a regular Python function


In both cases, you'll need to pass these callbacks into your target function to be able to use them. The signal-based approach is used in the completed code below, where we pass a `float` back as an indicator of the thread's % progress.
## The complete code
A complete working example is given below, showcasing the custom `QRunnable` worker together with the worker and progress signals. You should be able to easily adapt this code to any multithreaded application you develop:
python ```
import sys
import time
import traceback
from PySide6.QtCore import (
  QObject,
  QRunnable,
  QThreadPool,
  QTimer,
  Signal,
  Slot,
)
from PySide6.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QWidget,
)
class WorkerSignals(QObject):
  """Signals from a running worker thread.
  finished
    No data
  error
    tuple (exctype, value, traceback.format_exc())
  result
    object data returned from processing, anything
  progress
    float indicating % progress
  """
  finished = Signal()
  error = Signal(tuple)
  result = Signal(object)
  progress = Signal(float)
class Worker(QRunnable):
  """Worker thread.
  Inherits from QRunnable to handler worker thread setup, signals and wrap-up.
  :param callback: The function callback to run on this worker thread.
           Supplied args and
           kwargs will be passed through to the runner.
  :type callback: function
  :param args: Arguments to pass to the callback function
  :param kwargs: Keywords to pass to the callback function
  """
  def __init__(self, fn, *args, **kwargs):
    super().__init__()
    self.fn = fn
    self.args = args
    self.kwargs = kwargs
    self.signals = WorkerSignals()
    # Add the callback to our kwargs
    self.kwargs["progress_callback"] = self.signals.progress
  @Slot()
  def run(self):
    try:
      result = self.fn(*self.args, **self.kwargs)
    except Exception:
      traceback.print_exc()
      exctype, value = sys.exc_info()[:2]
      self.signals.error.emit((exctype, value, traceback.format_exc()))
    else:
      self.signals.result.emit(result)
    finally:
      self.signals.finished.emit()
class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.counter = 0
    layout = QVBoxLayout()
    self.label = QLabel("Start")
    button = QPushButton("DANGER!")
    button.pressed.connect(self.oh_no)
    layout.addWidget(self.label)
    layout.addWidget(button)
    w = QWidget()
    w.setLayout(layout)
    self.setCentralWidget(w)
    self.show()
    self.threadpool = QThreadPool()
    thread_count = self.threadpool.maxThreadCount()
    print(f"Multithreading with maximum {thread_count} threads")
    self.timer = QTimer()
    self.timer.setInterval(1000)
    self.timer.timeout.connect(self.recurring_timer)
    self.timer.start()
  def progress_fn(self, n):
    print(f"{n:.1f}% done")
  def execute_this_fn(self, progress_callback):
    for n in range(0, 5):
      time.sleep(1)
      progress_callback.emit(n * 100 / 4)
    return "Done."
  def print_output(self, s):
    print(s)
  def thread_complete(self):
    print("THREAD COMPLETE!")
  def oh_no(self):
    # Pass the function to execute
    worker = Worker(
      self.execute_this_fn
    ) # Any other args, kwargs are passed to the run function
    worker.signals.result.connect(self.print_output)
    worker.signals.finished.connect(self.thread_complete)
    worker.signals.progress.connect(self.progress_fn)
    # Execute
    self.threadpool.start(worker)
  def recurring_timer(self):
    self.counter += 1
    self.label.setText(f"Counter: {self.counter}")
app = QApplication([])
window = MainWindow()
app.exec()

```

## Caveats
You may have spotted a slight flaw in this master plan—we are still using the event loop (and the GUI thread) to process our workers' output.
This isn't a problem when we're simply tracking progress, completion, or returning metadata. However, if you have workers that return large amounts of data — e.g. loading large files, performing complex analysis and needing (large) results, or querying databases — passing this data back through the GUI thread may cause performance problems and is best avoided.
Similarly, if your application uses a large number of threads and Python result handlers, you may come up against the limitations of the GIL. As mentioned previously, when using threads execution of Python code is limited to a single thread at a time. The Python code that handles signals from your threads can be blocked by your workers and the other way around. Since blocking your slot functions blocks the event loop, this can directly impact GUI responsiveness.
In these cases, it is often better to investigate using a pure Python thread pool (e.g. concurrent futures) to keep your processing and thread-event handling further isolated from your GUI. However, note that _any_ Python GUI code can block other Python code unless it's in a separate process.
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
Continue with [ PySide6 Tutorial ](https://www.pythonguis.com/tutorials/pyside6-qprocess-external-programs/ "Continue to next part")
Return to [Create Desktop GUI Applications with PySide6 ](https://www.pythonguis.com/pyside6-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Multithreading PySide6 applications with QThreadPool** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/Python books) on the subject. 
**Multithreading PySide6 applications with QThreadPool** was published in [tutorials](https://www.pythonguis.com/tutorials/) on March 26, 2025 (updated April 08, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[multithreading](https://www.pythonguis.com/topics/multithreading/) [responsive](https://www.pythonguis.com/topics/responsive/) [gui](https://www.pythonguis.com/topics/gui/) [threading](https://www.pythonguis.com/topics/threading/) [qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [concurrency](https://www.pythonguis.com/topics/concurrency/) [performance](https://www.pythonguis.com/topics/performance/) [ pyside6-concurrency](https://www.pythonguis.com/topics/pyside6-concurrency/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
