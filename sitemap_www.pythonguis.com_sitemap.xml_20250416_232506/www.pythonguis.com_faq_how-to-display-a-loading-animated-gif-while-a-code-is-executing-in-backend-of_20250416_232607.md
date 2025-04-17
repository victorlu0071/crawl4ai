# Content from: https://www.pythonguis.com/faq/how-to-display-a-loading-animated-gif-while-a-code-is-executing-in-backend-of-my-python-qt5-ui/

[](https://www.pythonguis.com/faq/how-to-display-a-loading-animated-gif-while-a-code-is-executing-in-backend-of-my-python-qt5-ui/#menu)
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
# How to display a loading animated gif while a code is executing in backend of my Python Qt5 UI?
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
admin5940 | 2020-08-13 20:34:18 UTC | #1
**Environment:**
Python 3.7
Qt5
Windows 10
**Problem:**
When I execute my code, it shows immediately the UI, then it supposes to make some other preparing stuff and display a loading gif while these initialization tasks are running. But it does work. Instead of showing the gif, the UI is blocked(froze) waiting for my preparing script to finish its job. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
My script has a button to Run my main script "StartMyApp" and show an animated gif while MyApp is running without freezing my UI. I use multithread for this purpose. It works perfectly. I used this tutorial : <https://www.pythonguis.com/courses/concurrent-execution/multithreading-pyqt-applications-qthreadpool/>
So I thought by cloning the same logic, I could display another loading gif at the **init** of my UI but it didn't work. I missed something. I don't understand because the "Run" button works perfectly by showing the gif and running the main code without freezing the UI whereas my "preparing" code is not showing the gif and freezing my UI until it finishes.
Does anyone understand the source of this issue?
python ```
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
import traceback, sys
class WorkerSignals(QObject):
  '''
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
  '''
  finished = pyqtSignal ()
  error = pyqtSignal (tuple)
  result = pyqtSignal (object)
  progress = pyqtSignal (int)

class Worker (QRunnable):
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
    super (Worker, self).__init__ ()
    # Store constructor arguments (re-used for processing)
    self.fn = fn
    self.args = args
    self.kwargs = kwargs
    self.signals = WorkerSignals ()
    # Add the callback to our kwargs
    self.kwargs['progress_callback'] = self.signals.progress
  @pyqtSlot ()
  def run(self):
    '''
    Initialise the runner function with passed args, kwargs.
    '''
    # Retrieve args/kwargs here; and fire processing using them
    try:
      result = self.fn (*self.args, **self.kwargs)
    except:
      traceback.print_exc ()
      exctype, value = sys.exc_info ()[:2]
      self.signals.error.emit((exctype, value, traceback.format_exc ()))
    else:
      self.signals.result.emit (result) # Return the result of the processing
    finally:
      self.signals.finished.emit () # Done

class Ui(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    uic.loadUi('Ui/MyAppUI.Ui', self)
    # === We display the UI ==========
    self.show()
    # === THis will handle the MULTITHREAD PART ===================
    self.threadpool = QThreadPool()
    print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
    self.StartPreparingMyApp() #<======== This method doesn't work!!!!
    # === Associate methods to the buttons of the UI ==============
    self.button_Report.clicked.connect (self.ButtonStartMyAppReport)
    self.button_Run.clicked.connect (self.ButtonStartMyApp)
  def StartMyAppReport(self, progress_callback):
    #do some stuff
  def StartMyApp(self, progress_callback):
    # do some stuff
  def ButtonStartMyApp(self): #<=== This method works perfectly by showing the loading gif.
    # Pass the function to execute
    # === We need to block the Button Run and change its color
    self.button_Run.setEnabled (False)
    self.button_Run.setText ('Running...')
    self.button_Run.setStyleSheet ("background-color: #ffcc00;")
    self.label_logo.setHidden (True)
    self.label_running.setHidden (False)
    # === Play animated gif ================
    self.gif = QMovie ('ui/animated_gif_logo_UI_.gif')
    self.label_running.setMovie (self.gif)
    self.gif.start ()
    self.EditTextFieldUi (self.label_HeaderMsg1, '#ff8a00',
               "MyApp is running the tasks... You can press the button 'Report' to see what MyApp has done.")
    self.EditTextFieldUi (self.label_HeaderMsg2, '#ff8a00',
               "Press 'button 'Quit' to stop and turn off MyApp.")
    worker = Worker (self.StartMyApp) # Any other args, kwargs are passed to the run function
    worker.signals.result.connect (self.print_output)
    worker.signals.finished.connect (self.thread_complete)
    worker.signals.progress.connect (self.progress_fn)
    # Execute
    self.threadpool.start (worker)
  def PreparingMyApp(self, progress_callback):
    #do some stuff
    return "Done"
  def ButtonStartMyAppReport(self):
    # Pass the function to execute
    worker = Worker (self.StartMyAppReport) # Any other args, kwargs are passed to the run function
    worker.signals.result.connect (self.print_output)
    worker.signals.finished.connect (self.thread_complete)
    worker.signals.progress.connect (self.progress_fn)
    # Execute
    self.threadpool.start(worker)

  def StartPreparingMyApp(self): #<=== This method doesn't work !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # === Play animated gif ================
    self.label_loading.setHidden (False)
    self.gif_loading = QMovie ('ui/loading.gif')
    self.label_loading.setMovie (self.gif_loading)
    self.gif_loading.start ()
    # Pass the function to execute
    worker = Worker (self.PreparingMyApp) # Any other args, kwargs are passed to the run function
    worker.signals.result.connect (self.print_output)
    worker.signals.finished.connect (self.thread_complete)
    worker.signals.progress.connect (self.progress_fn)
    # Execute
    self.threadpool.start (worker)
    self.gif_loading.stop ()
    self.label_loading.setHidden (True)

if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  window = Ui()
  app.exec_()

```

**Edit:**
I added the xml source of MyAppUI.ui made with Qt Designer in order to reproduce my example:
<https://drive.google.com/file/d/1U9x0NmZ7GP6plzvRb6YgwIqaFHCz1PMc/view?usp=sharing>
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Eolinwen | 2020-08-20 16:52:25 UTC | #2
Hi,
I have not tested your application but just looking your code, I note something who seems to be wrong (perhaps an typo error ?) for me.
python ```
class Ui(QtWidgets.QMainWindow):
def __init__(self):
  super(Ui, self).__init__()
  uic.loadUi('Ui/MyAppUI.Ui', self)
  # === We display the UI ==========
  self.show()

```

it would not be ('Ui/MyAppUI.ui', self) by chance ?
Eolinwen | 2020-08-20 17:02:13 UTC | #3
You should take a look at this tutorial (in French) about throbbers. <http://python.jpvweb.com/python/mesrecettespython/doku.php?id=pyqt5_throbber>
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**How to display a loading animated gif while a code is executing in backend of my Python Qt5 UI?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/how-to-display-a-loading-animated-gif-while-a-code-is-executing-in-backend-of-my-python-qt5-ui/Python books) on the subject. 
**How to display a loading animated gif while a code is executing in backend of my Python Qt5 UI?** was published in [faq](https://www.pythonguis.com/faq/) on August 13, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
