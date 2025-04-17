# Content from: https://www.pythonguis.com/faq/pyqt-thread-execution-timeout-in-the-background/

[](https://www.pythonguis.com/faq/pyqt-thread-execution-timeout-in-the-background/#menu)
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
# PyQt thread execution timeout in the background
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Alex1 | 2021-05-07 07:28:49 UTC | #1
When I click the minimize button to perform this operation in the background，Threads often execute beyond the limited time， Waking up the program in the background is back to normal. Please be patient, it will appear in about a minute.
![83EABA78-8324-4105-9E6F-0ADD2998CBC5|652x238, 50%](https://www.pythonguis.com/static/faq/forum/pyqt-thread-execution-timeout-in-the-background/vTgTBn8faDFmgTZAonglvhiaRWb.jpeg)
![EFB3D59A-54C5-4D3E-8128-C303C2774578|406x424, 50%](https://www.pythonguis.com/static/faq/forum/pyqt-thread-execution-timeout-in-the-background/BAjygHFuRshIzNvO8sl6FO1Ob6.jpeg)
python ```
import sys, random, time, functools
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QHBoxLayout
from PyQt5.QtCore import QThread, QObject
def clock(func):
  @functools.wraps(func)
  def clocked(*args, **kwargs):
    t0 = time.time()
    result = func(*args, **kwargs)
    elapsed = time.time() - t0
    name = func.__name__
    l_arg = []
    if args:
      l_arg.append(', '.join(repr(arg) for arg in args))
    arg_str = ', '.join(l_arg)
    print('[%0.5fs] %s(%s)' % (elapsed, name, arg_str))
    return result
  return clocked
@clock
def go_sleep(sleep_time):
  time.sleep(sleep_time)
def go_run():
  for i in range(100):
    go_sleep(random.randint(1, 3))
class WorkThread(QObject):
  def __int__(self):
    super().__init__()
  def run(self):
    go_run()
class WinForm(QMainWindow):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.button1 = QPushButton('Run')
    self.button1.clicked.connect(self.onButtonClick)
    self._thread = QThread(self)
    self.wt = WorkThread()
    self.wt.moveToThread(self._thread)
    layout = QHBoxLayout()
    layout.addWidget(self.button1)
    main_frame = QWidget()
    main_frame.setLayout(layout)
    self.setCentralWidget(main_frame)
  def onButtonClick(self):
    self.button1.setText('Running')
    self._thread.started.connect(self.wt.run)
    self._thread.start()
if __name__ == "__main__":
  app = QApplication(sys.argv)
  form = WinForm()
  form.show()
  sys.exit(app.exec_())

```

martin | 2020-10-23 08:30:58 UTC | #2
Do you mean that the execution of those threads lasts _longer_ than the time given by the name? i.e. a `time.sleep(1)` lasts more than a single second?
That is actually expected! The `time.sleep()` method can sleep for longer than requested depending on system activity -- if the OS doesn't return control back to the thread, then the sleep won't finish. I guess that when you minimize the application the priority of the threads is being reduced. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
From the [Python documentation](https://docs.python.org/3/library/time.html#time.sleep)
> `time.sleep` ( _secs_ ) Suspend execution of the calling thread for the given number of seconds. The argument may be a floating point number to indicate a more precise sleep time. The actual suspension time may be less than that requested because any caught signal will terminate the [`sleep()`](https://docs.python.org/3/library/time.html#time.sleep) following execution of that signal’s catching routine. Also, the suspension time may be longer than requested by an arbitrary amount because of the scheduling of other activity in the system.
If you don't want this to happen, you can set the priority on your threads. For a single `QThread` you can use `.setPriority`. It looks like the equivalent for a `QRunnable` is passing priority when _starting_ it on your thread pool (although it says this determines _run order_ so it may be subtley different)
python ```
threadpool.start(runnable, priority = 0)

```

Something worth covering in the book I think!
Alex1 | 2020-10-25 12:58:16 UTC | #3
Hi, martin ,Thank you for answering my question. I want to simulate I/O operation by Sleep(). I tried many types of priorities but none of them achieved the expected.Which priority should I use?
python ```
HighestPriority = 5
HighPriority = 4
IdlePriority = 0
InheritPriority = 7
LowestPriority = 1
LowPriority = 2
NormalPriority = 3
TimeCriticalPriority = 6

```

self._thread.setPriority(QThread.HighPriority)
Alex1 | 2020-10-28 06:09:23 UTC | #4
I am using macOS, this is related to the operating system, it can work normally in Windows. [setPriority](https://doc.qt.io/Qt-5/qthread.html#setPriority) That doc included this line: "The effect of the priority parameter is dependent on the operating system's scheduling policy. In particular, the priority will be ignored on systems that do not support thread priorities." 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
martin | 2020-10-28 11:50:48 UTC | #5
> this is related to the operating system, it can work normally in Windows.
Ah, good to know. I'm wondering if you can use another approach to simulate the IO delay -- a sleep is very explicitly saying "do nothing for X", and perhaps the GIL is getting involved here. An actual IO call (even if slow) might wake up more reliably, since the end-time isn't known in advanced.
What kind of IO are wanting to test? For API calls there are things like [Slowwly](http://slowwly.robertomurray.co.uk/) for example.
Alex1 | 2020-10-28 16:55:40 UTC | #6
Network I/O with Socket communication， Can you give a small demonstration? thank you very much. :smiley:
Alex1 | 2020-11-17 05:54:52 UTC | #7
This is a promising solution:
python ```
 defaults write NSGlobalDomain NSAppSleepDisabled -bool YES

```

Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PyQt thread execution timeout in the background** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyqt-thread-execution-timeout-in-the-background/Python books) on the subject. 
**PyQt thread execution timeout in the background** was published in [faq](https://www.pythonguis.com/faq/) on October 23, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
