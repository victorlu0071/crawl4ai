# Content from: https://www.pythonguis.com/faq/use-a-qrunnable-to-handle-the-execution-of-other-qrunnables/

[](https://www.pythonguis.com/faq/use-a-qrunnable-to-handle-the-execution-of-other-qrunnables/#menu)
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
# Use a Qrunnable to handle the execution of other QRunnables
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ FAQ ](https://www.pythonguis.com/faq/)
cesant210858 | 2021-04-19 09:09:18 UTC | #1
I am struggling (a lot) with a problem: I am launching a process that requires some computational resources and sometimes takes a lot of time. Since I cannot kill a running QRunnable with a button, I would like to use a QRunnable that launches no more than 6 other processes in parallel. Here is an example of what I thought:
python ```
from PyQt5 import QtWidgets, QtCore
from time  import sleep
from sys  import argv, exc_info, exit
import traceback
threadpool            = QtCore.QThreadPool()
max_paralell_processes = 6
class MainWindow(QtWidgets.QMainWindow):
  stopsignal = QtCore.pyqtSignal()
  def __init__(self):
    super().__init__()
    self.trainers = {}
    self.ntrainers = 10
    self.startButton = QtWidgets .QPushButton('Start', self)
    self.startButton.resize(self.startButton.sizeHint())
    self.startButton.move(50, 50)
    self.stopButton = QtWidgets.QPushButton('Stop', self)
    self.stopButton.resize(self.stopButton.sizeHint())
    self.stopButton.move(150, 50)
    self.setGeometry(300, 300, 300, 200)
    self.startButton.clicked.connect(self.create_trainers)
    self.stopButton.clicked.connect(self.stop)
    self.progressBar = QtWidgets.QProgressBar(self)
    self.progressBar.setGeometry(50, 20, 250, 20)
    self.count    = 0
    self.progressBar.setValue(self.count)

  def create_trainers(self):
    global threadpool
    for m in range(self.ntrainers):
      trainer = Trainer(self.the_long_process, m)
      trainer.progress.connect( self.progress_bar)
      trainer.finished.connect( self.finished_process)
      self.trainers[m] = trainer
    launcher   = LaunchWorkers(self.trainers, range(self.ntrainers))
    launcher.finished.connect(self.__all_processes_finished)
    self.stopsignal.connect(launcher.stop)
    threadpool.start(launcher)
  def the_long_process(self, m):
    print("In process {}".format(m))
    sleep(2)
  def progess_bar(self):
    self.count += 1
    self.progressBar.setValue(self.count/len(self.trainers)*100)
  def finished_process(self):
    pass
  def stop(self):
    self.stopsignal.emit()
class Trainer(QtCore.QRunnable):
  finished   = QtCore.pyqtSignal(str)
  error    = QtCore.pyqtSignal(tuple)
  progress   = QtCore.pyqtSignal()
  def __init__(self, the_fn, m):
    super(Trainer, self).__init__()
    self.the_fn = the_fn
    self.m   = m
    self.terminated = False
  @QtCore.pyqtSlot()
  def run(self):
    try:
      self.the_fn ( self.m )
    except:
      traceback.print_exc()
      exctype, value = exc_info()[:2]
      self.error.emit((exctype, value, traceback.format_exc()))
      self.terminated = True
    else:
      self.progress.emit()
    finally:
      self.terminated = True
      self.finished.emit( self.m)

class LaunchWorkers(QtCore.QRunnable):
  finished   = QtCore.pyqtSignal()
  error    = QtCore.pyqtSignal(tuple)
  def __init__(self, trainers, some_list ):
    super().__init__()
    self.trainers = trainers
    self.some_list = some_list
    self.stop   = False
  def stop(self):
    self.stop = True
  @QtCore.pyqtSlot()
  def run(self):
    global threadpool
    finished_threads = 0
    try:
      for m in self.some_list :
        if self.stop:
          break
        while finished_threads <= max_paralell_processes :
          sleep(10)
          finished_threads = 0
          for t in self.trainers:
            if self.trainers[t].terminated:
              finished_threads += 1
        threadpool.start( self.trainers[m] )
    except:
      traceback.print_exc()
      exctype, value = exc_info()[:2]
      self.error.emit((exctype, value, traceback.format_exc()))
    finally:
      self.finished.emit( )
def main():
  app = QtWidgets.QApplication(argv)
  ex = MainWindow()
  ex.show()
  exit(app.exec_())

if __name__ == '__main__':
  main()

```

Doing so, I get a **TypeError** _ModelTrainer cannot be converted to PyQt5.QtCore.QObject in this context_.
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Use a Qrunnable to handle the execution of other QRunnables** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/use-a-qrunnable-to-handle-the-execution-of-other-qrunnables/Python books) on the subject. 
**Use a Qrunnable to handle the execution of other QRunnables** was published in [faq](https://www.pythonguis.com/faq/) on April 19, 2021 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[multithreading](https://www.pythonguis.com/topics/multithreading/) [qrunnable](https://www.pythonguis.com/topics/qrunnable/)
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
