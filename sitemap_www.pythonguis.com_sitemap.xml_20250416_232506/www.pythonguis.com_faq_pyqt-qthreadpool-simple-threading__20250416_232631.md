# Content from: https://www.pythonguis.com/faq/pyqt-qthreadpool-simple-threading/

[](https://www.pythonguis.com/faq/pyqt-qthreadpool-simple-threading/#menu)
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
# Simple threading in PyQt/PySide apps with .start() of QThreadPool
How to move Python functions/methods & PyQt/PySide slots onto separate threads
by [Boštjan Mejak](https://www.pythonguis.com/authors/bostjan-mejak/) Last updated Nov 04 [ FAQ ](https://www.pythonguis.com/faq/)
In PyQt version 5.15.0 and PySide 6.2.0, the `.start()` method of `QThreadPool` was extended to take a Python _function_ , a Python _method_ , or a PyQt/PySide _slot_ , besides taking only a `QRunnable` object. This simplifies running Python code in the background, avoiding the hassle of creating a `QRunnable` object for each task.
For more information about creating a `QRunnable` object for multithreading, see the [multithreading tutorial](https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/).
The `.start()` method schedules the execution of a function/method/slot on a separate thread using `QThreadPool`, so it avoids blocking the main GUI thread of your app. Therefore, if you have one or more long-running tasks that need to be completed or be running in the background, pass them to `.start()` and be done.
We'll build a simple demo app that simulates a long-running task to show how `.start()` can move a user-defined Python function/method or a PyQt/PySide slot onto a separate thread.
But first, let’s begin with a flawed approach.
## Blocking the GUI
Our demo app is a _sheep counter_ that counts upwards from 1. While this is happening, you can press a button to pick a sheep. And since picking a sheep is hard, it takes some time to complete.
![Demo app screenshot](https://www.pythonguis.com/static/faq/pyqt-qthreadpool-simple-threading/demo-app.jpg) _This is how our demo app looks like._
1:1 Coaching & Tutoring for your Python GUIs project
[![Martin Fitzpatrick Python GUIs Coaching & Training](https://www.pythonguis.com/static/theme/images/products/coaching.jpg)](https://calendly.com/martinfitzpatrick/60min-python-guis-coaching)
[60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/) [Book Now](https://www.pythonguis.com/live/)
1:1 Python GUIs Coaching & Training
**Comprehensive code review** • **Bugfixes** & improvements • **Maintainability** advice and **architecture** improvements • **Design and usability** assessment • Suggestions and tips to **expand your knowledge** • **Packaging and distribution** help for Windows, Mac & Linux • [Find out more.](https://www.pythonguis.com/live)
Make sure you're using PyQt 5.15.0+ or PySide 6.2.0+; otherwise, the demo app won’t work for you.
  * PySide6
  * PyQt6
  * PyQt5


python ```
import time
from PySide6.QtCore import Slot, QTimer
from PySide6.QtWidgets import (
  QLabel,
  QWidget,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QApplication,
)

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setFixedSize(250, 100)
    self.setWindowTitle("Sheep Picker")
    self.sheep_number = 1
    self.timer = QTimer()
    self.picked_sheep_label = QLabel()
    self.counted_sheep_label = QLabel()
    self.layout = QVBoxLayout()
    self.main_widget = QWidget()
    self.pick_sheep_button = QPushButton("Pick a sheep!")
    self.layout.addWidget(self.counted_sheep_label)
    self.layout.addWidget(self.pick_sheep_button)
    self.layout.addWidget(self.picked_sheep_label)
    self.main_widget.setLayout(self.layout)
    self.setCentralWidget(self.main_widget)
    self.timer.timeout.connect(self.count_sheep)
    self.pick_sheep_button.pressed.connect(self.pick_sheep)
    self.timer.start()
  @Slot()
  def count_sheep(self):
    self.sheep_number += 1
    self.counted_sheep_label.setText(f"Counted {self.sheep_number} sheep.")
  @Slot()
  def pick_sheep(self):
    self.picked_sheep_label.setText(f"Sheep {self.sheep_number} picked!")
    time.sleep(5) # This function represents a long-running task!

if __name__ == "__main__":
  app = QApplication([])
  main_window = MainWindow()
  main_window.show()
  app.exec()

```

python ```
import time
from PyQt6.QtCore import pyqtSlot, QTimer
from PyQt6.QtWidgets import (
  QLabel,
  QWidget,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QApplication,
)

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setFixedSize(250, 100)
    self.setWindowTitle("Sheep Picker")
    self.sheep_number = 1
    self.timer = QTimer()
    self.picked_sheep_label = QLabel()
    self.counted_sheep_label = QLabel()
    self.layout = QVBoxLayout()
    self.main_widget = QWidget()
    self.pick_sheep_button = QPushButton("Pick a sheep!")
    self.layout.addWidget(self.counted_sheep_label)
    self.layout.addWidget(self.pick_sheep_button)
    self.layout.addWidget(self.picked_sheep_label)
    self.main_widget.setLayout(self.layout)
    self.setCentralWidget(self.main_widget)
    self.timer.timeout.connect(self.count_sheep)
    self.pick_sheep_button.pressed.connect(self.pick_sheep)
    self.timer.start()
  @pyqtSlot()
  def count_sheep(self):
    self.sheep_number += 1
    self.counted_sheep_label.setText(f"Counted {self.sheep_number} sheep.")
  @pyqtSlot()
  def pick_sheep(self):
    self.picked_sheep_label.setText(f"Sheep {self.sheep_number} picked!")
    time.sleep(5) # This function represents a long-running task!

if __name__ == "__main__":
  app = QApplication([])
  main_window = MainWindow()
  main_window.show()
  app.exec()

```

python ```
import time
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import (
  QLabel,
  QWidget,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QApplication,
)

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setFixedSize(250, 100)
    self.setWindowTitle("Sheep Picker")
    self.sheep_number = 1
    self.timer = QTimer()
    self.picked_sheep_label = QLabel()
    self.counted_sheep_label = QLabel()
    self.layout = QVBoxLayout()
    self.main_widget = QWidget()
    self.pick_sheep_button = QPushButton("Pick a sheep!")
    self.layout.addWidget(self.counted_sheep_label)
    self.layout.addWidget(self.pick_sheep_button)
    self.layout.addWidget(self.picked_sheep_label)
    self.main_widget.setLayout(self.layout)
    self.setCentralWidget(self.main_widget)
    self.timer.timeout.connect(self.count_sheep)
    self.pick_sheep_button.pressed.connect(self.pick_sheep)
    self.timer.start()
  @pyqtSlot()
  def count_sheep(self):
    self.sheep_number += 1
    self.counted_sheep_label.setText(f"Counted {self.sheep_number} sheep.")
  @pyqtSlot()
  def pick_sheep(self):
    self.picked_sheep_label.setText(f"Sheep {self.sheep_number} picked!")
    time.sleep(5) # This function represents a long-running task!

if __name__ == "__main__":
  app = QApplication([])
  main_window = MainWindow()
  main_window.show()
  app.exec()

```

When you run the demo app and press the **_Pick a sheep!_** button, you’ll notice that for 5 seconds, the GUI is completely unresponsive. That's not good.
The delay in GUI responsiveness comes from the line `time.sleep(5)` which pauses execution of Python code for 5 seconds. This was added to simulate a long-running task. We can, however, improve that by threading, as you’ll see later on.
Feel free to experiment by increasing the length of the delay – pass a number greater than 5 to `.sleep()` – and you may notice that your operating system starts complaining about the demo app not responding.
## Run a task on a separate thread
So, how can we improve the responsiveness of our demo app? This is where the extended `.start()` method of `QThreadPool` comes in!
First, we need to import `QThreadPool`, so let’s do that.
  * PySide6
  * PyQt6
  * PyQt5


python ```
from PySide6.QtCore import QThreadPool

```

python ```
from PyQt6.QtCore import QThreadPool

```

python ```
from PyQt5.QtCore import QThreadPool

```

Next, we need to create a `QThreadPool` instance. Let’s add 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
python ```
self.thread_manager = QThreadPool()

```

to the `__init__` block of the `MainWindow` class.
Now, let’s create a `pick_sheep_safely()` slot. It will use the `.start()` method to call the long-running `pick_sheep()` slot and move it from the main GUI thread onto a separate thread.
  * PySide
  * PyQt


python ```
@Slot()
def pick_sheep_safely(self):
  self.thread_manager.start(self.pick_sheep) # This is where the magic happens!

```

python ```
@pyqtSlot()
def pick_sheep_safely(self):
  self.thread_manager.start(self.pick_sheep) # This is where the magic happens!

```

Also, make sure that you connect the `pick_sheep_safely()` slot with the `pressed` signal of `self.pick_sheep_button`. So, in the `__init__` block of the `MainWindow` class, you should have
python ```
self.pick_sheep_button.pressed.connect(self.pick_sheep_safely)

```

And if you followed along, the code of our improved demo app should now be:
  * PySide6
  * PyQt6
  * PyQt5


python ```
import time
from PySide6.QtCore import Slot, QThreadPool, QTimer
from PySide6.QtWidgets import (
  QLabel,
  QWidget,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QApplication,
)

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setFixedSize(250, 100)
    self.setWindowTitle("Sheep Picker")
    self.sheep_number = 1
    self.timer = QTimer()
    self.picked_sheep_label = QLabel()
    self.counted_sheep_label = QLabel()
    self.layout = QVBoxLayout()
    self.main_widget = QWidget()
    self.thread_manager = QThreadPool()
    self.pick_sheep_button = QPushButton("Pick a sheep!")
    self.layout.addWidget(self.counted_sheep_label)
    self.layout.addWidget(self.pick_sheep_button)
    self.layout.addWidget(self.picked_sheep_label)
    self.main_widget.setLayout(self.layout)
    self.setCentralWidget(self.main_widget)
    self.timer.timeout.connect(self.count_sheep)
    self.pick_sheep_button.pressed.connect(self.pick_sheep_safely)
    self.timer.start()
  @Slot()
  def count_sheep(self):
    self.sheep_number += 1
    self.counted_sheep_label.setText(f"Counted {self.sheep_number} sheep.")
  @Slot()
  def pick_sheep(self):
    self.picked_sheep_label.setText(f"Sheep {self.sheep_number} picked!")
    time.sleep(5) # This function doesn't affect GUI responsiveness anymore...
  @Slot()
  def pick_sheep_safely(self):
    self.thread_manager.start(self.pick_sheep) # ...since .start() is used!

if __name__ == "__main__":
  app = QApplication([])
  main_window = MainWindow()
  main_window.show()
  app.exec()

```

python ```
import time
from PyQt6.QtCore import pyqtSlot, QThreadPool, QTimer
from PyQt6.QtWidgets import (
  QLabel,
  QWidget,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QApplication,
)

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setFixedSize(250, 100)
    self.setWindowTitle("Sheep Picker")
    self.sheep_number = 1
    self.timer = QTimer()
    self.picked_sheep_label = QLabel()
    self.counted_sheep_label = QLabel()
    self.layout = QVBoxLayout()
    self.main_widget = QWidget()
    self.thread_manager = QThreadPool()
    self.pick_sheep_button = QPushButton("Pick a sheep!")
    self.layout.addWidget(self.counted_sheep_label)
    self.layout.addWidget(self.pick_sheep_button)
    self.layout.addWidget(self.picked_sheep_label)
    self.main_widget.setLayout(self.layout)
    self.setCentralWidget(self.main_widget)
    self.timer.timeout.connect(self.count_sheep)
    self.pick_sheep_button.pressed.connect(self.pick_sheep_safely)
    self.timer.start()
  @pyqtSlot()
  def count_sheep(self):
    self.sheep_number += 1
    self.counted_sheep_label.setText(f"Counted {self.sheep_number} sheep.")
  @pyqtSlot()
  def pick_sheep(self):
    self.picked_sheep_label.setText(f"Sheep {self.sheep_number} picked!")
    time.sleep(5) # This function doesn't affect GUI responsiveness anymore...
  @pyqtSlot()
  def pick_sheep_safely(self):
    self.thread_manager.start(self.pick_sheep) # ...since .start() is used!

if __name__ == "__main__":
  app = QApplication([])
  main_window = MainWindow()
  main_window.show()
  app.exec()

```

python ```
import time
from PyQt5.QtCore import pyqtSlot, QThreadPool, QTimer
from PyQt5.QtWidgets import (
  QLabel,
  QWidget,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QApplication,
)

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setFixedSize(250, 100)
    self.setWindowTitle("Sheep Picker")
    self.sheep_number = 1
    self.timer = QTimer()
    self.picked_sheep_label = QLabel()
    self.counted_sheep_label = QLabel()
    self.layout = QVBoxLayout()
    self.main_widget = QWidget()
    self.thread_manager = QThreadPool()
    self.pick_sheep_button = QPushButton("Pick a sheep!")
    self.layout.addWidget(self.counted_sheep_label)
    self.layout.addWidget(self.pick_sheep_button)
    self.layout.addWidget(self.picked_sheep_label)
    self.main_widget.setLayout(self.layout)
    self.setCentralWidget(self.main_widget)
    self.timer.timeout.connect(self.count_sheep)
    self.pick_sheep_button.pressed.connect(self.pick_sheep_safely)
    self.timer.start()
  @pyqtSlot()
  def count_sheep(self):
    self.sheep_number += 1
    self.counted_sheep_label.setText(f"Counted {self.sheep_number} sheep.")
  @pyqtSlot()
  def pick_sheep(self):
    self.picked_sheep_label.setText(f"Sheep {self.sheep_number} picked!")
    time.sleep(5) # This function doesn't affect GUI responsiveness anymore...
  @pyqtSlot()
  def pick_sheep_safely(self):
    self.thread_manager.start(self.pick_sheep) # ...since .start() is used!

if __name__ == "__main__":
  app = QApplication([])
  main_window = MainWindow()
  main_window.show()
  app.exec()

```

When you press the **_Pick a sheep!_** button now, the `pick_sheep()` slot is executed on a separate thread and no longer blocks the main GUI thread. The sheep counting goes on, and the GUI remains responsive – even though our demo app still has to complete a long-running task in the background.
Try increasing the length of the delay now – for example, `time.sleep(10)` – and notice that it doesn’t affect the GUI anymore.
## Conclusion
And that’s it! I hope you’ll find the extended `.start()` method of `QThreadPool` helpful in any of your PyQt/PySide GUI apps that have long-running tasks to be executed in the background. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Boštjan Mejak](https://www.pythonguis.com/static/theme/images/authors/bostjan-mejak.jpg)](https://www.pythonguis.com/authors/bostjan-mejak/)
**Simple threading in PyQt/PySide apps with .start() of QThreadPool** was written by [Boštjan Mejak](https://www.pythonguis.com/authors/bostjan-mejak/) . 
Boštjan Mejak has been developing Python apps for about ten years. He started with Tkinter, then switched to wxPython, PyQt, and recently to PySide. 
**Simple threading in PyQt/PySide apps with .start() of QThreadPool** was published in [faq](https://www.pythonguis.com/faq/) on December 01, 2021 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[gui](https://www.pythonguis.com/topics/gui/) [multithreading](https://www.pythonguis.com/topics/multithreading/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [threading](https://www.pythonguis.com/topics/threading/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt6](https://www.pythonguis.com/topics/qt6/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
