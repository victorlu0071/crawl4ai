# Content from: https://www.pythonguis.com/examples/python-calculator-gui/

[](https://www.pythonguis.com/examples/python-calculator-gui/#menu)
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
# Calculon, a Desktop Calculator
Calculon
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 13 PyQt5 [ Example applications ](https://www.pythonguis.com/examples/)
[ Calculon Source Code ](https://www.pythonguis.com/d/calculator.zip)
Calculators are one of the simplest desktop applications, found by default on every window system. Over time these have been extended to support scientific and programmer modes, but fundamentally they all work the same.
In this project we implement a basic working desktop calculator using PyQt. This implementation uses a stack for holding inputs, operator and state. Basic memory operations are also implemented.
## The User Interface
The user interface for _Calculon_ was created in Qt Designer. The layout of the mainwindow uses a `QVBoxLayout` with the LCD display added to the top, and a `QGridLayout` to the bottom.
We use the grid layout is used to position all the buttons for the calculator. Each button takes a single space on the grid, except for the equals sign which is set to span two squares.
![Defining the layout for the calculator in Qt Designer.](https://www.pythonguis.com/static/examples/build-desktop-calculator/screenshot-calculator2.jpg) _Defining the layout for the calculator in Qt Designer._
Each button is defined with a keyboard shortcut which triggers a `.pressed` signal — e.g. `3` for the 3 key. The actions for each button are defined in code and connected to this signal. By making this small addition it's possible to use the calculator with a numeric pad.
If you want to edit the design in Qt Designer, remember to regenerate the `MainWindow.py` file using `pyuic5 mainwindow.ui -o MainWindow.py`.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
## Actions
To make the buttons do something we need to connect them up to specific handlers. The connections defined are shown first below, and then the handlers covered in detail.
First we connect all the numeric buttons to the same handler. In ***__Qt Designer** *__ we named all the buttons using a standard format, as `pushButton_nX` where `X` is the number. This makes it simple to iterate over each one and connect it up.
We use [a function wrapper on the signal](_/article/qt-transmit-extra-data-with-signals_) to send additional data with each trigger — in this case the number which was pressed.
python ```
for n in range(0, 10):
  getattr(self, 'pushButton_n%s' % n).pressed.connect(lambda v=n: self.input_number(v))

```

The next block of signals to connect are for standard calculator operations, including add, multiply, subtraction and divide. Again these are hooked up to the same slot, and consist of a wrapped signal to transmit the operation (a specific Python `operator` type).
python ```
self.pushButton_add.pressed.connect(lambda: self.operation(operator.add))
self.pushButton_sub.pressed.connect(lambda: self.operation(operator.sub))
self.pushButton_mul.pressed.connect(lambda: self.operation(operator.mul))
self.pushButton_div.pressed.connect(lambda: self.operation(operator.truediv)) # operator.div for Python2.7

```

In addition to the numbers and operators, we have a number of custom behaviours to wire up — percentage (to convert the previously typed number to a percentage amount), equals, reset and memory actions.
python ```
self.pushButton_pc.pressed.connect(self.operation_pc)
self.pushButton_eq.pressed.connect(self.equals)
self.pushButton_ac.pressed.connect(self.reset)
self.pushButton_m.pressed.connect(self.memory_store)
self.pushButton_mr.pressed.connect(self.memory_recall)

```

Now the buttons and actions are wired up, we can implement the logic in the slot methods for handling these events.
## Operations
Calculator operations are handled using three components — the _stack_ , the _state_ and the _current operation_.
### The `stack`
The `stack` is a short memory store of maximum 2 elements, which holds the numeric values with which we're currently calculating. When the user starts entering a new number it is added to the _end_ of the stack (which, if the stack is empty, is also the beginning). Each numeric press multiplies the current stack end value by 10, and adds the value pressed.
python ```
:::python
def input_number(self, v):
  if self.state == READY:
    self.state = INPUT
    self.stack[-1] = v
  else:
    self.stack[-1] = self.stack[-1] * 10 + v
  self.display()

```

This has the effect of numbers filling from the right as expected, e.g.
Value pressed | Calculation | Stack  
---|---|---  
0  
2 | 0 * 10 + 2 | 2  
3 | 2 * 10 + 3 | 23  
5 | 23 * 10 + 5 | 235  
### The `state`
A `state` flag, to toggle between _ready_ and _input_ states. This affects the behaviour while entering numbers. In _ready_ mode, the value entered is set direct onto the stack at the current position. In _input_ mode the above shift+add logic is used.
This is required so it is possible to _type over_ a result of a calculation, rather than have new numbers added to the result of the previous calculation.
python ```
:::python
def input_number(self, v):
  if self.state == READY:
    self.state = INPUT
    self.stack[-1] = v
  else:
    self.stack[-1] = self.stack[-1] * 10 + v
  self.display()

```

You'll see switches between `READY` and `INPUT` states elsewhere in the code. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
### The `current_op`
The `current_op` variable stores the currently active operation, which will be applied when the user presses _equals_. If an operation is already in progress, we first calculate the result of that operation, pushing the result onto the stack, and then apply the new one.
Starting a new operation also pushes `0` onto the stack, making it now length 2, and switches to `INPUT` mode. This ensures any subsequent number input will start from zero.
python ```
:::python
def operation(self, op):
  if self.current_op: # Complete the current operation
    self.equals()
  self.stack.append(0)
  self.state = INPUT
  self.current_op = op

```

The operation handler for percentage calculation works a little differently. This instead operates directly on the current contents of the stack. Triggering the `operation_pc` takes the last value in the stack and divides it by 100.
python ```
:::python
def operation_pc(self):
  self.state = INPUT
  self.stack[-1] *= 0.01
  self.display()

```

## Equals & Memory operations
The core of the calculator is the handler which actually does the maths. All operations (with the exception of percentage) are handled by the `equals` handler, which is triggered either by pressing the equals key, Enter or another operation key while an op is in progress.
## Equals
The equals handler takes the `current_op` and applies it to the values in the stack (2 values, unpacked using `*self.stack`) to get the result. The result is put back in the stack as a single value, and we return to a `READY` state. Errors (exceptions, e.g. for division by zero) are caught and an error message is displayed if necessary.
python ```
:::python
def equals(self):
  # Support to allow '=' to repeat previous operation
  # if no further input has been added.
  if self.state == READY and self.last_operation:
    s, self.current_op = self.last_operation
    self.stack.append(s)
  if self.current_op:
    self.last_operation = self.stack[-1], self.current_op
    try:
      self.stack = [self.current_op(*self.stack)]
    except Exception:
      self.lcdNumber.display('Err')
      self.stack = [0]
    else:
      self.current_op = None
      self.state = READY
      self.display()

```

Support has also been added for repeating previous operations by pressing the equals key again. This is done by storing the value and operator when equals is triggered, and re-using them if equals is pressed again without leaving `READY` mode (no user input).
## Memory
Finally, we can define the handlers for the memory actions. For _Calculon_ we've defined only two memory actions — _store_ and _recall_. Store takes the current value from the LCD display, and copies it to `self.memory`. Recall takes the value in `self.memory` and puts in the final place on our stack.
python ```
def memory_store(self):
  self.memory = self.lcdNumber.value()
def memory_recall(self):
  self.state = INPUT
  self.stack[-1] = self.memory
  self.display()

```

By setting the mode to INPUT and updating the display this behaves exactly the same as for entering a number by hand.
## Challenges
The current implementation of _Calculon_ only supports basic math operations. Most GUI desktop calculators also include support for scientific (and sometimes programmer) modes, which add a number or alternative functions.
In _Calculon_ you could define these additional operations as a set of `lambda`s, which each accept the two parameters to operate on.
Switching modes (e.g. between normal and scientific) on the calculator will be tricky with the current `QMainWindow`-based layout. You could rework the calculator layout in QtDesigner to use a `QWidget` base. Each view is just a widget, and switching modes can be performed by swapping out the central widget on your running main window.
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Calculon, a Desktop Calculator** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/examples/python-calculator-gui/Python books) on the subject. 
**Calculon, a Desktop Calculator** was published in [examples](https://www.pythonguis.com/examples/) on January 12, 2019 (updated September 13, 2023) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[pyqt](https://www.pythonguis.com/topics/pyqt/) [calculator](https://www.pythonguis.com/topics/calculator/) [qt5](https://www.pythonguis.com/topics/qt5/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/)
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
