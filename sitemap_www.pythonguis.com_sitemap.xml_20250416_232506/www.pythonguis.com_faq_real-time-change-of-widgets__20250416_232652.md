# Content from: https://www.pythonguis.com/faq/real-time-change-of-widgets/

[](https://www.pythonguis.com/faq/real-time-change-of-widgets/#menu)
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
# Real Time Change of Widgets?
How to update the UI while in a loop
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 02 [ FAQ ](https://www.pythonguis.com/faq/)
_Bentraje wrote_
Hi,
I'm trying to create a simple class recitation app where it randomly picks from the list of students. It works, but I want it to change in real time, so there's a bit of suspense who is being picked.
You can see in the illustration video below that the console updates the names in real time but the QtWidget does not: https://www.dropbox.com/s/rwcbhhj58tevshl/py003_pyqt_real_time_update_widget.mp4?dl=0
Here is the working code so far:
python ```
import sys
import os
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QSpinBox, QWidget, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
from PySide2.QtGui import QPixmap

from time import sleep, perf_counter
import time
import random

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Class Recitation")
    # Widget
    root_img_path = 'img'
    self.image_list = []
    for root, dirs, files in os.walk(root_img_path):
      for f in files:
        img_path = os.path.join(root_img_path, f)
        first_name = f.split('_')[0]
        last_name = f.split('_')[1]
        self.image_list.append( (img_path, first_name + " " + last_name ) )
    # creating label
    self.label = QLabel(self)
    # loading image
    #self.pixmap = QPixmap('img/Eijirou_Kirishima_Portrait.png')
    self.pixmap = QPixmap(self.image_list[0][0])
    # adding image to label
    self.label.setPixmap(self.pixmap)
    self.name_label = QLabel()
    self.name_label.setText(self.image_list[0][1])
    self.pick_btn = QPushButton("Pick")
    self.pick_btn.setObjectName("Pick")
    self.pick_btn.clicked.connect(self.random_pick)

    # Layout Creations
    hbox = QHBoxLayout()
    # hbox.addWidget(self.search_button)
    # hbox.addWidget(self.search_bar)
    vbox = QVBoxLayout()
    vbox.addWidget(self.label)
    vbox.addWidget(self.name_label)
    vbox.addWidget(self.pick_btn)
    # vbox.addWidget(self.result_text_edit)
    layout = QVBoxLayout()
    layout.addLayout(hbox)
    layout.addLayout(vbox)
    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)
  def random_pick(self):
    choice_list = self.image_list
    time_started = time.perf_counter()
    counter = 0
    for x in range(0,10000):
      random_pick = random.choice(choice_list)
      self.name_label.setText(random_pick[1])
      self.label.setPixmap(random_pick[0])
      print (random_pick[1])
      sleep(counter)
      current_time = time.perf_counter()
      time_elapse = current_time - time_started
      counter += 0.0001 * (2**4)
      if time_elapse >= 5:
        break
    return random_pick

  def change_name(self):
    self.name_label.setText("Name Changed")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

Is there a way around this?
Thanks 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
_Martin Fitzpatrick_
Hi Bentraje welcome to the forum!
The problem is the `random_pick` method.
First some background -- In GUI applications the update of the UI is handled by an event loop, and a queue of _things to do_. The event loop takes items form the queue, does them, then takes the next, and so on. Things are done in order, and only one thing is done at a time.
When you update the text of a widget, with `self.name_label.setText(random_pick[1])` that update happens immediately (the value in the widget changes) but the widget is not redrawn. Instead a "redraw" request is put onto the event queue, and that will happen once the event loop gets to it.
Why doesn't the event loop get to it in your case? Because your method is blocking the loop. In your code you've linked pressing the button to this method as follows
python ```
self.pick_btn.clicked.connect(self.random_pick)

```

When the button is pressed it generates a signal, which you've correctly connected to your method. But when the event loop gets to that signal and calls your method, _it has to wait for the method to finish_ before doing anything else. And "anything else" in this case includes redrawing the widgets you've updated.
The end result is you update the widget multiple times, but it never redraws, so you can't see it being updated.
How to solve it?
There are a few ways. Firstly, you can call `QApplication.processEvents()` in your loop, to make Qt process the outstanding events (including the outstanding redraws). I wouldn't recommend this, as it's better to structure your application to use the event loop, rather than try and work around it -- but it's there as a quick and dirty solution.
Another option is to run this selection process in a thread. This would stop it blocking your main GUI thread, and allow you to keep the code more or less the same (aside from creating the workers). See a [tutorial on multithreading here](https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/). 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
A third option is to use a `QTimer` to trigger the random selection and another to stop it. Remove the loop code from `random_pick` and have it make just one choice. Then add a new method which starts the two timers. I think this is the approach I would prefer in this case.
Something like the following (untested)
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    # snip
    self.pick_btn = QPushButton("Pick")
    self.pick_btn.setObjectName("Pick")
    self.pick_btn.clicked.connect(self.start_selection)
  def start_selection(self):
    # Repeating timer, calls random_pick over and over.
    self.picktimer = QTimer()
    self.picktimer.setInterval(500)
    self.picktimer.timeout.connect(self.random_pick)
    self.picktimer.start()
    # Single oneshot which stops the selection after 5 seconds
    QTimer.singleShot(5000, self.stop_selection)
  def stop_selection(self):
    # Stop the random selection
    self.picktimer.stop()
    # The current pick is in self.current_selection
    print("Current selection is: ", self.current_selection)

  def random_pick(self):
    random_pick = random.choice(self.image_list)
    self.name_label.setText(random_pick[1])
    self.label.setPixmap(random_pick[0])
    print (random_pick[1])
    # Store the current selection, so we have it at the end in stop_selection.
    self.current_selection = random_pick

```

_Bentraje_
Thanks for the response. It works as expected. Just to confirm, if I have to loop (other than based on time) in Qt, I guess I'll have to use the threading/process feature right?
_Martin Fitzpatrick_
Great, glad it did the trick!
> Just to confirm, if I have to loop (other than based on time) in Qt, I guess I’ll have to use the threading/process feature right?
It depends on how long the loop lasts. The key thing to remember is that whenever your code is running the UI is blocked. But you can get away with doing a _lot_ before it becomes noticeable.
If you have any long-running tasks that can't be broken down into smaller units, then yes you would ideally put these in a thread. The timer approach works well for anything that _can_ be broken down into smaller steps -- like your random selection example, it's a series of very quick steps, that you want to happen regularly, but the subsequent steps don't rely on one another so can be easily split.
_Bentraje_
Ah gotcha. Thanks for the clarification!
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Real Time Change of Widgets?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/real-time-change-of-widgets/Python books) on the subject. 
**Real Time Change of Widgets?** was published in [faq](https://www.pythonguis.com/faq/) on November 19, 2020 (updated September 02, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
