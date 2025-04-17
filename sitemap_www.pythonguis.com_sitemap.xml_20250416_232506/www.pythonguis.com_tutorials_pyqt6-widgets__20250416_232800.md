# Content from: https://www.pythonguis.com/tutorials/pyqt6-widgets/

[](https://www.pythonguis.com/tutorials/pyqt6-widgets/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PyQt6 ](https://www.pythonguis.com/pyqt6/)
  * [PyQt6 Tutorial ](https://www.pythonguis.com/pyqt6-tutorial/)
  * Basics
  * [Create a PyQt6 app](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/)
  * [PyQt6 Signals](https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/)
  * [PyQt6 Widgets](https://www.pythonguis.com/tutorials/pyqt6-widgets/)
  * [PyQt6 Layouts](https://www.pythonguis.com/tutorials/pyqt6-layouts/)
  * [PyQt6 Menus](https://www.pythonguis.com/tutorials/pyqt6-actions-toolbars-menus/)
  * [PyQt6 Dialogs](https://www.pythonguis.com/tutorials/pyqt6-dialogs/)
  * [Multi-window PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/)
  * Qt Designer
  * [First Qt Designer app](https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/)
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/pyqt6-qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/pyqt6-creating-dialogs-qt-designer/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyqt6-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/pyqt6-qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/pyqt6-qtableview-modelviews-numpy-pandas/)
  * Plotting
  * [Plotting With PyQtGraph and PyQt6](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PyQt6](https://www.pythonguis.com/tutorials/pyqt6-plotting-matplotlib/)
  * QGraphics
  * [Vector Graphics](https://www.pythonguis.com/tutorials/pyqt6-qgraphics-vector-graphics/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/pyqt6-bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/pyqt6-creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/pyqt6-embed-pyqtgraph-custom-widgets-qt-app/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/pyqt6-transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/pyqt6-system-tray-mac-menu-bar-applications/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyqt6-applications-windows-pyinstaller/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyqt6-applications-pyinstaller-macos-dmg/)
  * Resources
  * [Books](https://www.pythonguis.com/books/)
  * Services
  * [Consulting](https://www.pythonguis.com/hire/)
  * [1:1 Coaching](https://www.pythonguis.com/live/)
  * [Contact](https://www.pythonguis.com/contact/)
  * [About](https://www.pythonguis.com/about/)
  * Libraries
  * [PySide6](https://www.pythonguis.com/pyside6/)
  * [PyQt5](https://www.pythonguis.com/pyqt5/)
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# PyQt6 Widgets
Using QPushButton, QCheckBox, QComboBox, QLabel and QSlider widgets
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 This article has been updated for PyQt6. PyQt6 [ Getting started with PyQt6 ](https://www.pythonguis.com/pyqt6-tutorial/#pyqt6-start)
#### [ PyQt6 Tutorial ](https://www.pythonguis.com/pyqt6-tutorial/) — [Getting started with PyQt6](https://www.pythonguis.com/pyqt6-tutorial/#pyqt6-start)
  * [Creating your first app with PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/)
  * [PyQt6 Signals, Slots & Events](https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/)
  * [PyQt6 Widgets](https://www.pythonguis.com/tutorials/pyqt6-widgets/)
  * [PyQt6 Layouts](https://www.pythonguis.com/tutorials/pyqt6-layouts/)
  * [PyQt6 Toolbars & Menus — QAction](https://www.pythonguis.com/tutorials/pyqt6-actions-toolbars-menus/)
  * [PyQt6 Dialogs and Alerts](https://www.pythonguis.com/tutorials/pyqt6-dialogs/)
  * [Creating Additional Windows in PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/)


This tutorial is also available for [PySide6](https://www.pythonguis.com/tutorials/pyside6-widgets/) , [PySide2](https://www.pythonguis.com/tutorials/pyside-widgets/) and [PyQt5](https://www.pythonguis.com/tutorials/pyqt-basic-widgets/)
In Qt (and most User Interfaces), **widget** is the name given to a component of the UI that the user can interact with. User interfaces are made up of multiple widgets, arranged within the window.
Qt comes with a large selection of widgets and even allows you to create your own custom widgets or customize existing ones.
Table of Contents
  * [A Quick Demo](https://www.pythonguis.com/tutorials/pyqt6-widgets/#a-quick-demo)
  * [QLabel](https://www.pythonguis.com/tutorials/pyqt6-widgets/#qlabel)
  * [QCheckBox](https://www.pythonguis.com/tutorials/pyqt6-widgets/#qcheckbox)
  * [QComboBox](https://www.pythonguis.com/tutorials/pyqt6-widgets/#qcombobox)
  * [QListWidget](https://www.pythonguis.com/tutorials/pyqt6-widgets/#qlistwidget)
  * [QLineEdit](https://www.pythonguis.com/tutorials/pyqt6-widgets/#qlineedit)
  * [QSpinBox and QDoubleSpinBox](https://www.pythonguis.com/tutorials/pyqt6-widgets/#qspinbox-and-qdoublespinbox)
  * [QSlider](https://www.pythonguis.com/tutorials/pyqt6-widgets/#qslider)
  * [QDial](https://www.pythonguis.com/tutorials/pyqt6-widgets/#qdial)
  * [Conclusion](https://www.pythonguis.com/tutorials/pyqt6-widgets/#conclusion)


## A Quick Demo
First, let's have a look at some of the most common PyQt widgets. The following code creates a range of PyQt widgets and adds them to a window layout so you can see them together:
python ```
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
  QApplication,
  QCheckBox,
  QComboBox,
  QDateEdit,
  QDateTimeEdit,
  QDial,
  QDoubleSpinBox,
  QFontComboBox,
  QLabel,
  QLCDNumber,
  QLineEdit,
  QMainWindow,
  QProgressBar,
  QPushButton,
  QRadioButton,
  QSlider,
  QSpinBox,
  QTimeEdit,
  QVBoxLayout,
  QWidget,
)
# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Widgets App")
    layout = QVBoxLayout()
    widgets = [
      QCheckBox,
      QComboBox,
      QDateEdit,
      QDateTimeEdit,
      QDial,
      QDoubleSpinBox,
      QFontComboBox,
      QLCDNumber,
      QLabel,
      QLineEdit,
      QProgressBar,
      QPushButton,
      QRadioButton,
      QSlider,
      QSpinBox,
      QTimeEdit,
    ]
    for w in widgets:
      layout.addWidget(w())
    widget = QWidget()
    widget.setLayout(layout)
    # Set the central widget of the Window. Widget will expand
    # to take up all the space in the window by default.
    self.setCentralWidget(widget)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

**Run it!** You'll see a window appear containing all the widgets we've created.
![Big ol' list of widgets on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets-list.png) _Big ol' list of widgets on Windows, Mac & Ubuntu Linux._
You can learn how layouts work in Qt in our [PyQt6 Layouts](https://www.pythonguis.com/tutorials/pyqt6-layouts/) tutorial.
Let's have a look at all the example widgets, from top to bottom: 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Widget | What it does  
---|---  
`QCheckbox` | A checkbox  
`QComboBox` | A dropdown list box  
`QDateEdit` | For editing dates and datetimes  
`QDateTimeEdit` | For editing dates and datetimes  
`QDial` | Rotatable dial  
`QDoubleSpinBox` | A number spinner for floats  
`QFontComboBox` | A list of fonts  
`QLCDNumber` | A quite ugly LCD display  
`QLabel` | Just a label, not interactive  
`QLineEdit` | Enter a line of text  
`QProgressBar` | A progress bar  
`QPushButton` | A button  
`QRadioButton` | A toggle set, with only one active item  
`QSlider` | A slider  
`QSpinBox` | An integer spinner  
`QTimeEdit` | For editing times  
There are far more widgets than this, but they don’t fit so well! You can see them all by checking the Qt documentation.
Next, we'll step through some of the most commonly used widgets and look at them in more detail. To experiment with the widgets we'll need a simple application to put them in. Save the following code to a file named `app.py` and run it to make sure it's working:
python ```
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
  QApplication,
  QCheckBox,
  QComboBox,
  QDial,
  QDoubleSpinBox,
  QLabel,
  QLineEdit,
  QListWidget,
  QMainWindow,
  QSlider,
  QSpinBox,
)
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

```

In the code above we've imported a number of Qt widgets. Now we'll step through each of those widgets in turn, adding them to our application and seeing how they behave.
## QLabel
We'll start the tour with `QLabel`, arguably one of the simplest widgets available in the Qt toolbox. This is a simple one-line piece of text that you can position in your application. You can set the text by passing in a `str` as you create it:
python ```
widget = QLabel("Hello")

```

Or, by using the `.setText()` method:
python ```
widget = QLabel("1") # The label is created with the text 1.
widget.setText("2")  # The label now shows 2.

```

You can also adjust font parameters, such as the size of the font or the alignment of text in the widget:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    widget = QLabel("Hello")
    font = widget.font()
    font.setPointSize(30)
    widget.setFont(font)
    widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
    self.setCentralWidget(widget)

```

![QLabel on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets1.png) _QLabel on Windows, Mac & Ubuntu Linux._
**Font tip** Note that if you want to change the properties of a widget font it is usually better to get the _current_ font, update it and then apply it back. This ensures the font face remains in keeping with the desktop conventions.
The alignment is specified by using a flag from the `Qt.` namespace. The flags available for horizontal alignment are:
PyQt6 flag (long name) | Behavior  
---|---  
`Qt.AlignmentFlag.AlignLeft` | Aligns with the left edge.  
`Qt.AlignmentFlag.AlignRight` | Aligns with the right edge.  
`Qt.AlignmentFlag.AlignHCenter` | Centers horizontally in the available space.  
`Qt.AlignmentFlag.AlignJustify` | Justifies the text in the available space.  
The flags available for vertical alignment are:
PyQt6 flag (long name) | Behavior  
---|---  
`Qt.AlignmentFlag.AlignTop` | Aligns with the top.  
`Qt.AlignmentFlag.AlignBottom` | Aligns with the bottom.  
`Qt.AlignmentFlag.AlignVCenter` | Centers vertically in the available space.  
You can combine flags together using pipes (`|`), however note that you can only use vertical or horizontal alignment flag at a time:
python ```
align_top_left = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop

```

Note that you use an _OR_ pipe (`|`) to combine the two flags (not `A &amp; B`). This is because the flags are non-overlapping bitmasks. e.g. `Qt.AlignmentFlag.AlignLeft` has the hexadecimal value `0x0001`, while `Qt.AlignmentFlag.AlignBottom` is `0x0040`. By ORing together we get the value `0x0041` representing 'bottom left'. This principle applies to all other combinatorial Qt flags. If this is gibberish to you, feel free to ignore and move on. Just remember to use |
Finally, there is also a shorthand flag that centers in both directions simultaneously:
PyQt6 Flag | Behavior  
---|---  
`Qt.AlignmentFlag.AlignCenter` | Centers horizontally _and_ vertically  
Weirdly, you can also use `QLabel` to display an image using `.setPixmap()`. This method accepts a _pixmap_ , which you can create by passing an image filename to the `QPixmap` class from `PyQt6.QtGui`.
Below is an image which you can download for this example.
!["Otje" the cat.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/otje.jpg) _"Otje" the cat._
Place the file in the same folder as your code, and then display it in your window as follows:
python ```
widget.setPixmap(QPixmap('otje.jpg'))

```

!["Otje" the cat.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets2.png) _"Otje" the cat, displayed in a window._
What a lovely face. By default the image scales while maintaining its aspect ratio. If you want it to stretch and scale to fit the window completely you can set `.setScaledContents(True)` on the `QLabel`:
python ```
widget.setScaledContents(True)

```

## QCheckBox
The next widget to look at is `QCheckBox()` which, as the name suggests, presents a checkable box to the user. However, as with all Qt widgets there are number of configurable options to change the widget behaviors:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    widget = QCheckBox()
    widget.setCheckState(Qt.CheckState.Checked)
    # For tristate: widget.setCheckState(Qt.CheckState.PartiallyChecked)
    # Or: widget.setTristate(True)
    widget.stateChanged.connect(self.show_state)
    self.setCentralWidget(widget)
  def show_state(self, s):
    print(s == Qt.CheckState.Checked.value)
    print(s)

```

![QCheckBox on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets3.png) _QCheckBox on Windows, Mac & Ubuntu Linux._
You can set a checkbox state programmatically using `.setChecked` or `.setCheckState`. The former accepts either `True` or `False` representing checked or unchecked, respectively. However, with `.setCheckState` you also specify a particular checked state using a `Qt.CheckState` flag:
PyQt6 flag (long name) | Behavior  
---|---  
`Qt.CheckState.Unchecked` | Item is unchecked  
`Qt.CheckState.PartiallyChecked` | Item is partially checked  
`Qt.CheckState.Checked` | Item is checked  
A checkbox that supports a partially-checked (`Qt.CheckState.PartiallyChecked`) state is commonly referred to as 'tri-state', that is being neither on nor off. A checkbox in this state is commonly shown as a greyed-out checkbox, and is commonly used in hierarchical checkbox arrangements where sub-items are linked to parent checkboxes.
If you set the value to `Qt.CheckState.PartiallyChecked` the checkbox will become tristate. You can also set a checkbox to be tri-state without setting the current state to partially checked by using `.setTristate(True)`.
You may notice that when the script is running, the current state number is displayed as an `int` with checked = `2`, unchecked = `0`, and partially checked = `1`. You don't need to remember these values, the `Qt.CheckState.Checked` flag `== 2`, for example. This is the value of these state's respective flags. This means that you can test state using `state == Qt.CheckState.Checked`.
## QComboBox
The `QComboBox` is a drop down list, closed by default with an arrow to open it. You can select a single item from the list, with the currently selected item being shown as a label on the widget. The combo box is suited to selection of a choice from a long list of options.
You have probably seen the combo box used for selection of font faces, or size, in word processing applications. Although Qt actually provides a specific font-selection combo box as `QFontComboBox`.
You can add items to a `QComboBox` by passing a list of strings to `.addItems()`. Items will be added in the order they are provided:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    widget = QComboBox()
    widget.addItems(["One", "Two", "Three"])
    # Sends the current index (position) of the selected item.
    widget.currentIndexChanged.connect( self.index_changed )
    # There is an alternate signal to send the text.
    widget.currentTextChanged.connect( self.text_changed )
    self.setCentralWidget(widget)

  def index_changed(self, i): # i is an int
    print(i)
  def text_changed(self, s): # s is a str
    print(s)

```

![QComboBox on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets4.png) _QComboBox on Windows, Mac & Ubuntu Linux._
The `.currentIndexChanged` signal is triggered when the currently selected item is updated, by default passing the index of the selected item in the list. There is also a `.currentTextChanged` signal which instead provides the label of the currently selected item, which is often more useful.
`QComboBox` can also be editable, allowing users to enter values not currently in the list and either have them inserted, or simply used as a value. To make the box editable:
python ```
widget.setEditable(True)

```

You can also set a flag to determine how the insert is handled. These flags are stored on the `QComboBox` class itself and are listed below:
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
PyQt6 flag (long name) | Behavior  
---|---  
`QComboBox.InsertPolicy.NoInsert` | No insert  
`QComboBox.InsertPolicy.InsertAtTop` | Insert as first item  
`QComboBox.InsertPolicy.InsertAtCurrent` | Replace currently selected item  
`QComboBox.InsertPolicy.InsertAtBottom` | Insert after last item  
`QComboBox.InsertPolicy.InsertAfterCurrent` | Insert after current item  
`QComboBox.InsertPolicy.InsertBeforeCurrent` | Insert before current item  
`QComboBox.InsertPolicy.InsertAlphabetically` | Insert in alphabetical order  
To use these, apply the flag as follows:
python ```
widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

```

You can also limit the number of items allowed in the box by using `.setMaxCount`, e.g:
python ```
widget.setMaxCount(10)

```

For a more in-depth look at the `QComboBox` take a look at our [QComboBox documentation](https://www.pythonguis.com/docs/qcombobox/).
## QListWidget
This widget is similar to `QComboBox`, except options are presented as a scrollable list of items. It also supports selection of multiple items at once. A `QListWidget` offers an `currentItemChanged` signal which sends the `QListWidgetItem` (the element of the list widget), and a `currentTextChanged` signal which sends the text of the current item:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    widget = QListWidget()
    widget.addItems(["One", "Two", "Three"])
    widget.currentItemChanged.connect(self.index_changed)
    widget.currentTextChanged.connect(self.text_changed)
    self.setCentralWidget(widget)
  def index_changed(self, i): # Not an index, i is a QListWidgetItem
    print(i.text())
  def text_changed(self, s): # s is a str
    print(s)

```

![QListWidget on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets5.png) _QListWidget on Windows, Mac & Ubuntu Linux._
## QLineEdit
The `QLineEdit` widget is a simple single-line text editing box, into which users can type input. These are used for form fields, or settings where there is no restricted list of valid inputs. For example, when entering an email address, or computer name:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    widget = QLineEdit()
    widget.setMaxLength(10)
    widget.setPlaceholderText("Enter your text")
    #widget.setReadOnly(True) # uncomment this to make readonly
    widget.returnPressed.connect(self.return_pressed)
    widget.selectionChanged.connect(self.selection_changed)
    widget.textChanged.connect(self.text_changed)
    widget.textEdited.connect(self.text_edited)
    self.setCentralWidget(widget)

  def return_pressed(self):
    print("Return pressed!")
    self.centralWidget().setText("BOOM!")
  def selection_changed(self):
    print("Selection changed")
    print(self.centralWidget().selectedText())
  def text_changed(self, s):
    print("Text changed...")
    print(s)
  def text_edited(self, s):
    print("Text edited...")
    print(s)

```

![QLineEdit on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets6.png) _QLineEdit on Windows, Mac & Ubuntu Linux._
As demonstrated in the above code, you can set a maximum length for the text in a line edit.
The `QLineEdit` has a number of signals available for different editing events including when return is pressed (by the user), when the user selection is changed. There are also two edit signals, one for when the text in the box has been edited and one for when it has been changed. The distinction here is between user edits and programmatic changes. The `textEdited` signal is only sent when the user edits text.
Additionally, it is possible to perform input validation using an _input mask_ to define which characters are supported and where. This can be applied to the field as follows:
python ```
widget.setInputMask('000.000.000.000;_')

```

The above would allow a series of 3-digit numbers separated with periods, and could therefore be used to validate IPv4 addresses.
## QSpinBox and QDoubleSpinBox
`QSpinBox` provides a small numerical input box with arrows to increase and decrease the value. `QSpinBox` supports integers while the related widget `QDoubleSpinBox` supports floats:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    widget = QSpinBox()
    # Or: widget = QDoubleSpinBox()
    widget.setMinimum(-9)
    widget.setMaximum(3)
    # Or: widget.setRange(-9, 3)
    widget.setPrefix("$")
    widget.setSuffix("c")
    widget.setSingleStep(3) # Or e.g. 3.0 for QDoubleSpinBox
    widget.valueChanged.connect(self.value_changed)
    widget.textChanged.connect(self.value_changed_str)
    self.setCentralWidget(widget)
  def value_changed(self, i):
    print(i)
  def value_changed_str(self, s):
    print(s)

```

Run it and you'll see a numeric entry box. The value shows pre and post fix units, and is limited to the range `3` to `-9`.
It makes sense to set the step value to a multiple of the interval limits. Otherwise, you'll get weird behaviors. For example, if you change the lower limit from `-9` to `-10` and keep the step as `3`, then once you reach the `-10` limit, you won't be able to reach the `0` value again.
![QSpinBox on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets7.png) _QSpinBox on Windows, Mac & Ubuntu Linux._
The demonstration code above shows the various features that are available for the widget.
To set the range of acceptable values, you can use `setMinimum` and `setMaximum`, or alternatively, use `setRange` to set both simultaneously. Annotation of value types is supported with both prefixes and suffixes that can be added to the number, e.g. for currency markers or units using `.setPrefix` and `.setSuffix`, respectively.
Clicking on the up and down arrows on the widget will increase or decrease the value in the widget by an amount, which can be set using `.setSingleStep`. Note that this has no effect on the values that are acceptable to the widget.
Both `QSpinBox` and `QDoubleSpinBox` have a `.valueChanged` signal that fires whenever their value is altered. The raw `.valueChanged` signal sends the numeric value (either an `int` or a `float`), while `.textChanged` sends the value as a string, including both the prefix and suffix characters.
You can optionally disable text input on the spin box line edit, by setting it to read-only. With this set, the value can _only_ be changed using the controls. This also has the side effect of disabling the flashing cursor:
python ```
widget.lineEdit().setReadOnly(True)

```

## QSlider
`QSlider` provides a slide-bar widget, which functions internally much like a `QDoubleSpinBox`. Rather than display the current value numerically, it is represented by the position of the slider handle along the length of the widget. This is often useful when providing adjustment between two extremes, but where absolute accuracy is not required. The most common use of this type of widget is for volume controls.
There is an additional `.sliderMoved` signal that is triggered whenever the slider moves position and a `.sliderPressed` signal that emits whenever the slider is clicked:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    widget = QSlider()
    widget.setMinimum(-10)
    widget.setMaximum(3)
    # Or: widget.setRange(-10,3)
    widget.setSingleStep(3)
    widget.valueChanged.connect(self.value_changed)
    widget.sliderMoved.connect(self.slider_position)
    widget.sliderPressed.connect(self.slider_pressed)
    widget.sliderReleased.connect(self.slider_released)
    self.setCentralWidget(widget)
  def value_changed(self, i):
    print(i)
  def slider_position(self, p):
    print("Position", p)
  def slider_pressed(self):
    print("Pressed!")
  def slider_released(self):
    print("Released")

```

Run this and you'll see a slider widget. Drag the slider to change the value.
![QSlider on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets8.png) _QSlider on Windows, Mac & Ubuntu Linux._
You can also construct a slider with a vertical or horizontal orientation by passing the orientation in as you create it. The orientation flags are defined in the `Qt.` namespace. For example --
python ```
widget = QSlider(Qt.Orientation.Vertical)

```

Or --
python ```
widget = QSlider(Qt.Orientation.Horizontal)

```

## QDial
Finally, the `QDial` is a rotatable widget that functions just like the slider, but appears as an analogue dial. This looks nice, but from a UI perspective is not particularly user friendly. However, they are often used in audio applications as representation of real-world analogue dials:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    widget = QDial()
    widget.setRange(-10, 100)
    widget.setSingleStep(1)
    widget.valueChanged.connect(self.value_changed)
    widget.sliderMoved.connect(self.slider_position)
    widget.sliderPressed.connect(self.slider_pressed)
    widget.sliderReleased.connect(self.slider_released)
    self.setCentralWidget(widget)
  def value_changed(self, i):
    print(i)
  def slider_position(self, p):
    print("position", p)
  def slider_pressed(self):
    print("Pressed!")
  def slider_released(self):
    print("Released")

```

Run this and you'll see a circular dial, rotate it to select a number from the range.
![QDial on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets9.png) _QDial on Windows, Mac & Ubuntu Linux._
The signals are the same as for `QSlider` and retain the same names (e.g. `.sliderMoved`).
## Conclusion
This concludes our brief tour of the common widgets used in PyQt applications. To see the full list of available widgets, including all their signals and attributes, take a look at the [Qt documentation](http://doc.qt.io/qt-6/).
For a more in-depth look at some of the discussed widgets, see our documentation for the [`QComboBox`](https://www.pythonguis.com/docs/qcombobox/), [`QPushButton`](https://www.pythonguis.com/docs/qpushbutton/), [`QCheckBox`](https://www.pythonguis.com/docs/qcheckbox/), and [`QLineEdit`](https://www.pythonguis.com/docs/qlineedit/) widgets. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
Continue with [ PyQt6 Tutorial ](https://www.pythonguis.com/tutorials/pyqt6-layouts/ "Continue to next part")
Return to [Create Desktop GUI Applications with PyQt6 ](https://www.pythonguis.com/pyqt6-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PyQt6 Widgets** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/pyqt6-widgets/Python books) on the subject. 
**PyQt6 Widgets** was published in [tutorials](https://www.pythonguis.com/tutorials/) on September 08, 2021 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qt](https://www.pythonguis.com/topics/qt/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [widgets](https://www.pythonguis.com/topics/widgets/) [qlabel](https://www.pythonguis.com/topics/qlabel/) [qcheckbox](https://www.pythonguis.com/topics/qcheckbox/) [qcombobox](https://www.pythonguis.com/topics/qcombobox/) [qlistbox](https://www.pythonguis.com/topics/qlistbox/) [qlistwidget](https://www.pythonguis.com/topics/qlistwidget/) [qlineedit](https://www.pythonguis.com/topics/qlineedit/) [qspinbox](https://www.pythonguis.com/topics/qspinbox/) [qdoublespinbox](https://www.pythonguis.com/topics/qdoublespinbox/) [qslider](https://www.pythonguis.com/topics/qslider/) [qwidget](https://www.pythonguis.com/topics/qwidget/) [ foundation](https://www.pythonguis.com/topics/foundation/) [ pyqt6-foundation](https://www.pythonguis.com/topics/pyqt6-foundation/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
