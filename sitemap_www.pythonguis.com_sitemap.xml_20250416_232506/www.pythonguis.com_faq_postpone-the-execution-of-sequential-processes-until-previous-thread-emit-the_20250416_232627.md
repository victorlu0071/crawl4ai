# Content from: https://www.pythonguis.com/faq/postpone-the-execution-of-sequential-processes-until-previous-thread-emit-the-result/

[](https://www.pythonguis.com/faq/postpone-the-execution-of-sequential-processes-until-previous-thread-emit-the-result/#menu)
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
# Postpone the execution of sequential processes until previous thread emit the result
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ FAQ ](https://www.pythonguis.com/faq/)
JohnThePips | 2021-04-26 20:38:39 UTC | #1
I start with thanks to Martin Fitzpatrick for excellent explanation and code for running QRunnable objects within QThreadPool. My problem is that I have three separate processes where one of those is taking the results of the two as arguments. Of course I could combine them into on big function but as the result are stored in variable accessible for all the processes it is not necessary to run all of three processes every time.
So I start with Martin code that is used as class definition for QRunnable object and signals
python ```
class Worker(QtCore.QRunnable):
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
  self.running = None
  self.fn = fn
  self.args = args
  self.kwargs = kwargs
  self.signals = WorkerSignals()
  # Add the callback to our kwargs
  self.kwargs['callback_progress'] = self.signals.progress
  self.kwargs['callback_data'] = self.signals.data
  # @Slot()
def run(self):
  '''
  Initialise the runner function with passed args, kwargs.
  '''
  # Retrieve args/kwargs here; and fire processing using them
  try:
    self.signals.started.emit()
    self.result = self.fn(
      *self.args,
      **self.kwargs
    )
  except:
    traceback.print_exc()
    exctype, value = sys.exc_info()[:2]
    self.signals.error.emit((exctype, value, traceback.format_exc()))
  else:
    self.signals.result.emit(self.result) # Return the result of the processing
  finally:
    self.signals.finished.emit() # Done

```

Then I am using a function which executes functions passed to that as arguments
python ```
  def exe_worker_run(self, WorkerPool, function, arguments):
    Worker = thread.Worker(function, arguments)
    Worker.signal.started.connect(self.sig_thread_start)
    Worker.signal.error.connect(self.sig_thread_error)
    Worker.signal.result.connect(self.sig_thread_result)
    Worker.signal.finished.connect(self.sig_thread_finish)
    WorkerPool.start(Worker)

```

The results are intercepted by the following function (of course it is simplified)
python ```
  def sig_thread_result(self, result):
    self.dataframe = result

```

Then the "function" argument in the exe_worker_run is the name of the function that performs the real job. Again the simplified version of that function will look like
python ```
  def exe_languages_load(self, arguments, callback_progress, callback_data):
    try:
      result = (sql query to database)
    except Exception as ex:
      session.rollback()
      print(ex)
    finally:
      session.close()
      return result

```

The problem is that the results of two functions which are then arguments for third are not emitted before the execution of third function is started. What should I do to allow sequential execution of all three functions in a way which will postpone the execution of third until the results of first and second are emitted and assigned to respective dataframes?
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
martin | 2021-04-30 15:43:38 UTC | #2
Hi @JohnThePips welcome to the forum & glad you've found the code examples helpful.
What you're asking is actually quite tricky to accomplish. The trick is to use a _finished_ signal to trigger the execution of the next workers but add some kind of check to that method to make sure that both the prior workers have completed. A good way to do this is to give your workers IDs and emit those, storing the result in a list or dictionary. Checking this dictionary will let you know the current state & whether you can proceed.
python ```
from PySide2.QtCore import QObject, Slot, Signal, QRunnable, QThreadPool
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
import time
class Signals(QObject):
  finished = Signal(str, str) # worker_id and our data is a string
class BaseRunner(QRunnable):
  def __init__(self, data):
    super().__init__()
    self.data = data
  @Slot()
  def run(self):
    print("Running.. ", self.data)
    time.sleep(self.delay)
    print(".done")
    # do something
    self.data = self.data + '[more data]'
    self.signals.finished.emit(self.worker_id, self.data) # emit the worker ID too
class RunnerA(BaseRunner):
  worker_id = 'A'
  delay = 5
  signals = Signals()
class RunnerB(BaseRunner):
  worker_id = 'B'
  delay = 10
  signals = Signals()
class RunnerC(BaseRunner):
  worker_id = 'C'
  delay = 3
  signals = Signals()

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    button = QPushButton("Start")
    button.pressed.connect(self.start_initial_runners)
    self.setCentralWidget(button)
    self.data = {}
    self.threadpool = QThreadPool()
  def start_initial_runners(self, data=None):
    self.data = {} # reset
    runnerA = RunnerA('first')
    runnerB = RunnerB('second')
    # When either finishes, they will check to see if the 3rd can start.
    runnerA.signals.finished.connect(self.start_third_runner)
    runnerB.signals.finished.connect(self.start_third_runner)
    self.threadpool.start(runnerA)
    self.threadpool.start(runnerB)
  def start_third_runner(self, worker_id, data):
    print("Finished", worker_id)
    self.data[worker_id] = data # store data
    if 'A' in self.data and 'B' in self.data: # we have both results:
      runnerC = RunnerC('third')
      self.threadpool.start(runnerC)
    else:
      print("Not ready yet. Waiting.")


app = QApplication([])
w = MainWindow()
w.show()
app.exec_()

```

In the example above the completion of the runners will call `start_third_runner`. This will happen twice, once for each of the prior runners, but only when both are complete will it proceed. If you run it you should see the following output.
python ```
Running.. first
Running.. second
.done
Finished A
Not ready yet. Waiting.
.done
Finished B
Running.. third
.done

```

The "Not ready yet. Waiting." message is shown when either A or B is complete (we have receved `start_third_runner` method via a _finished_ signal) but not both.
JohnThePips | 2021-04-30 16:21:35 UTC | #3
Dear Martin, Thanks for the tip. I thought the solution would be much simpler but as there is no other way I would have to pursue that idea. I am however quite surprised that there is no built-in mechanism that allow to control the start of thread when a certain trigger is fired. However as I am not super advanced programmer it might be that there are some other circumstances that prevent such built-in mechanism to be implemented. Anyway once again thank you for the tip. I will certainly test the solution.
martin | 2021-04-30 17:58:39 UTC | #4
You _can_ start a `QThread` directly using a signal (by calling `.start()`) but I don't think that will help in your case -- because C depends on A & B being complete, and they (being threads) can complete in any order -- a single trigger from either isn't actually sufficient to start C.
As I understand it, what you're asking for isn't a "built-in mechanism that allow to control the start of thread when a certain trigger is fired" but a "built-in mechanism that allow to control the start of thread when **two** triggers have been fired".
Waiting for two signals inevitably makes things more complicated as you now need to maintain _state_ to know what you've received. There is also the complication that you need to pass data from A & B to C -- C must wait until it has the output from both A & B. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
This all adds up to making it a bit too use-case specific for a built in. If you can remove some of these constraints there might be a way to simplify things, e.g. it's simpler if you just have a A -> B -> C setup. Then you can limit a `QThreadPool` to 1 max threads (you can have many pools).
PedanticHacker | 2021-05-01 01:46:34 UTC | #5
@martin, would it be possible to define custom signals in a `QRunnable` subclass like in the example below?
python ```
class BaseRunner(QRunnable, QObject):
  finished = Signal(str, str)
  def __init__(self):
    super().__init__()
    # And so on...

```

Multiple inheritance to the rescue? 🤔
PedanticHacker | 2021-05-03 22:29:04 UTC | #6
I tried to define custom signals in a `QRunnable` subclass by also inheriting from `QObject` in the same object (multiple inheritance), but my application crashed. I guess you can't do that. It would be interesting to know why this can't work. Seemed like a good idea at first.
martin | 2021-05-05 07:58:43 UTC | #7
I wasn't sure if it would work, so glad you tried it out ;) ...I think the issue is that `QRunnable` and `QObject` have different C++ base classes. While it might be valid to implement your custom class using these two classes in C++, PyQt can only hook to existing C++ classes -- for this to work it would need to have a (compiled) implementation of a class using these two bases to hook to.
martin | 2021-05-05 08:00:12 UTC | #8
When I first read this I thought you were using the `Signals` wrapper class and putting that on the base -- fwiw that _also_ won't work as written, because then each worker will share the same signals object. When you get to running the 3rd runner it will now have 3 signals attached to itself.
Of course, you _could_ exploit that to avoid hooking them up on each run. But in that case I'd move the signals object off the runner class to avoid the confusion. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Postpone the execution of sequential processes until previous thread emit the result** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/postpone-the-execution-of-sequential-processes-until-previous-thread-emit-the-result/Python books) on the subject. 
**Postpone the execution of sequential processes until previous thread emit the result** was published in [faq](https://www.pythonguis.com/faq/) on April 26, 2021 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyside](https://www.pythonguis.com/topics/pyside/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
