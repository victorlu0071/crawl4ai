# Content from: https://www.pythonguis.com/tutorials/pyside6-widgets/

[](https://www.pythonguis.com/tutorials/pyside6-widgets/#menu)
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
# PySide6 Widgets
Using QPushButton, QCheckBox, QComboBox, QLabel, and QSlider widgets
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Oct 24 This article has been updated for PySide6. PySide6 [ Getting started with PySide6 ](https://www.pythonguis.com/pyside6-tutorial/#pyside6-getting-started)
#### [ PySide6 Tutorial ](https://www.pythonguis.com/pyside6-tutorial/) — [Getting started with PySide6](https://www.pythonguis.com/pyside6-tutorial/#pyside6-getting-started)
  * [Creating your first app with PySide6](https://www.pythonguis.com/tutorials/pyside6-creating-your-first-window/)
  * [PySide6 Signals, Slots & Events](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/)
  * [PySide6 Widgets](https://www.pythonguis.com/tutorials/pyside6-widgets/)
  * [PySide6 Layouts](https://www.pythonguis.com/tutorials/pyside6-layouts/)
  * [PySide6 Toolbars & Menus — QAction](https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/)
  * [PySide6 Dialogs and Alerts](https://www.pythonguis.com/tutorials/pyside6-dialogs/)
  * [Creating Additional Windows in PySide6](https://www.pythonguis.com/tutorials/pyside6-creating-multiple-windows/)


This tutorial is also available for [PyQt6](https://www.pythonguis.com/tutorials/pyqt6-widgets/) , [PySide2](https://www.pythonguis.com/tutorials/pyside-widgets/) and [PyQt5](https://www.pythonguis.com/tutorials/pyqt-basic-widgets/)
In Qt (and most User Interfaces), **widget** is the name given to a component of the UI that the user can interact with. User interfaces are made up of multiple widgets, arranged within the window.
Qt comes with a large selection of widgets available and even allows you to create your own custom and customized widgets.
Table of Contents
  * [A Quick Demo: PySide6 Widgets](https://www.pythonguis.com/tutorials/pyside6-widgets/#a-quick-demo-pyside6-widgets)
  * [QLabel](https://www.pythonguis.com/tutorials/pyside6-widgets/#qlabel)
  * [QCheckBox](https://www.pythonguis.com/tutorials/pyside6-widgets/#qcheckbox)
  * [QComboBox](https://www.pythonguis.com/tutorials/pyside6-widgets/#qcombobox)
  * [QListWidget](https://www.pythonguis.com/tutorials/pyside6-widgets/#qlistwidget)
  * [QLineEdit](https://www.pythonguis.com/tutorials/pyside6-widgets/#qlineedit)
  * [QSpinBox and QDoubleSpinBox](https://www.pythonguis.com/tutorials/pyside6-widgets/#qspinbox-and-qdoublespinbox)
  * [QSlider](https://www.pythonguis.com/tutorials/pyside6-widgets/#qslider)
  * [QDial](https://www.pythonguis.com/tutorials/pyside6-widgets/#qdial)
  * [Conclusion](https://www.pythonguis.com/tutorials/pyside6-widgets/#conclusion)


## A Quick Demo: PySide6 Widgets
First, let's have a look at some of the most common PySide widgets. The following code creates a range of PySide widgets and adds them to a window layout so that you can see them together:
python ```
import sys
from PySide6.QtWidgets import (
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
    for widget in widgets:
      layout.addWidget(widget())
    central_widget = QWidget()
    central_widget.setLayout(layout)
    self.setCentralWidget(central_widget)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

**Run it!** You'll see a window appear containing all the widgets we've created.
![Big ol' list of widgets on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets-list.png) _Big ol' list of widgets on Windows, Mac & Ubuntu Linux._
Let's have a look at all the example widgets, from top to bottom:
Widget | What it does  
---|---  
`QCheckbox` | A checkbox  
`QComboBox` | A dropdown list box  
`QDateEdit` | For editing dates and datetimes  
`QDateTimeEdit` | For editing dates and datetimes  
`QDial` | Rotateable dial  
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
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Next, we'll step through some of the most commonly used widgets and look at them in more detail. To experiment with the widgets we'll need a simple application to put them in. Save the following code to a file named `app.py` and run it to make sure it's working:
python ```
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
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
window = MainWindow()
window.show()
app.exec()

```

In the code above, we've imported a number of Qt widgets. Now we'll step through each of those widgets in turn, adding them to our application and seeing how they behave.
## `QLabel`
We'll start the tour with `QLabel`, arguably one of the simplest widgets available in the Qt toolbox. This is a simple one-line piece of text that you can position in your application. You can set the text by passing in a `str` as you create it:
python ```
label = QLabel("Hello")

```

Or, by using the `.setText()` method:
python ```
label_1 = QLabel("1") # The label is created with the text 1.
label_2.setText("2")  # The label now shows 2.

```

You can also adjust font parameters, such as the size of the font or the alignment of text in the widget:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    label = QLabel("Hello")
    font = label.font()
    font.setPointSize(30)
    label.setFont(font)
    label.setAlignment(
      Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
    )
    self.setCentralWidget(label)

```

![QLabel on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets1.png) _QLabel on Windows, Mac & Ubuntu Linux._
**Font tip** Note that if you want to change the properties of a widget font it is usually better to get the _current_ font, update it and then apply it back. This ensures the font face remains in keeping with the desktop conventions.
The alignment is specified by using a flag from the `Qt.AlignmentFlag` namespace. The flags available for horizontal alignment are:
Flag | Behavior  
---|---  
`Qt.AlignmentFlag.AlignLeft` | Aligns with the left edge.  
`Qt.AlignmentFlag.AlignRight` | Aligns with the right edge.  
`Qt.AlignmentFlag.AlignHCenter` | Centers horizontally in the available space.  
`Qt.AlignmentFlag.AlignJustify` | Justifies the text in the available space.  
The flags available for vertical alignment are:
Flag | Behavior  
---|---  
`Qt.AlignmentFlag.AlignTop` | Aligns with the top.  
`Qt.AlignmentFlag.AlignBottom` | Aligns with the bottom.  
`Qt.AlignmentFlag.AlignVCenter` | Centers vertically in the available space.  
You can combine flags together using pipes (`|`), however, note that you can only use the vertical or horizontal alignment flag at a time:
python ```
align_top_left = Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop

```

Note that you use an _OR_ pipe (`|`) to combine the two flags (not `A &amp; B`). This is because the flags are non-overlapping bitmasks. e.g. `Qt.AlignmentFlag.AlignLeft` has the hexadecimal value `0x0001`, while `Qt.AlignmentFlag.AlignBottom` is `0x0040`. By ORing flags together, we get the value `0x0041` representing 'bottom left'. This principle applies to all other combinatorial Qt flags. If this is gibberish to you, feel free to ignore it and move on. Just remember to use the pipe operator (`|`).
Finally, there is also a shorthand flag that centers in both directions simultaneously:
Flag | Behavior  
---|---  
`Qt.AlignmentFlag.AlignCenter` | Centers horizontally _and_ vertically  
Weirdly, you can also use `QLabel` to display an image using `.setPixmap()`. This accepts a pixmap object, which you can create by passing an image filename to the `QPixmap` class.
Below is an image which you can download for this example.
!["Otje" the cat.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/otje.jpg) _"Otje" the cat._
Place the file in the same folder as your code, and then display it in your window as follows:
python ```
widget.setPixmap(QPixmap('otje.jpg'))

```

!["Otje" the cat.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets2.png) _"Otje" the cat, displayed in a window._
What a lovely face. By default, the image scales while maintaining its aspect ratio. If you want it to stretch and scale to fit the window completely, you can set `.setScaledContents(True)` on the `QLabel`:
python ```
label.setScaledContents(True)

```

## `QCheckBox`
The next widget to look at is `QCheckBox()`, which presents a checkable box to the user, as the name suggests. However, as with all Qt widgets, there are a number of configurable options to change the widget behaviors:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    checkbox = QCheckBox()
    checkbox.setCheckState(Qt.CheckState.Checked)
    # For tristate: widget.setCheckState(Qt.PartiallyChecked)
    # Or: widget.setTriState(True)
    checkbox.stateChanged.connect(self.show_state)
    self.setCentralWidget(checkbox)
  def show_state(self, state):
    print(state == Qt.CheckState.Checked.value)
    print(state)

```

![QCheckBox on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets3.png) _QCheckBox on Windows, Mac & Ubuntu Linux._
You can set a checkbox state programmatically using `.setChecked()` or `.setCheckState()`. The former accepts either `True` or `False,` representing checked or unchecked, respectively. With `.setCheckState()`, you also specify a particular checked state using a `Qt.CheckState` namespace:
Flag | Behavior  
---|---  
`Qt.CheckState.Unchecked` | Item is unchecked  
`Qt.CheckState.PartiallyChecked` | Item is partially checked  
`Qt.CheckState.Checked` | Item is checked  
A checkbox that supports a partially-checked (`Qt.CheckState.PartiallyChecked`) state is commonly referred to as **tri-state** , which means the widget is neither on nor off. A checkbox in this state is commonly shown as a greyed-out checkbox and is commonly used in hierarchical checkbox arrangements where sub-items are linked to parent checkboxes.
If you set the value to `Qt.CheckState.PartiallyChecked` the checkbox will become tristate. You can also set a checkbox to be tri-state without setting the current state to partially checked by using `.setTriState(True)`
You may notice that when the script is running, the current state number is displayed as an `int` with checked = `2`, unchecked = `0`, and partially checked = `1`. You don’t need to remember these values, the `Qt.CheckState.Checked` namespace variable = `2,` for example. This is the value of these states' respective flags. This means you can test state using `state == Qt.CheckState.Checked`.
## `QComboBox`
The `QComboBox` widget is a drop-down list, closed by default with an arrow to open it. You can select a single item from the list, with the currently selected item being shown as a label on the widget. The combo box is suited to selecting choices from a list of options.
You have probably seen the combo box used for the selection of font faces, or sizes, in word-processing applications. Although Qt actually provides a specific font-selection combo box as `QFontComboBox`.
You can add items to a `QComboBox` by passing a list of strings to `.addItems()`. Items will be added in the order they are provided:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    combobox = QComboBox()
    combobox.addItems(["One", "Two", "Three"])
    # The default signal from currentIndexChanged sends the index
    combobox.currentIndexChanged.connect(self.index_changed)
    # The same signal can send a text string
    combobox.currentTextChanged.connect(self.text_changed)
    self.setCentralWidget(combobox)
  def index_changed(self, index): # index is an int starting from 0
    print(index)
  def text_changed(self, text): # text is a str
    print(text)

```

![QComboBox on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets4.png) _QComboBox on Windows, Mac & Ubuntu Linux._
The `.currentIndexChanged` signal is triggered when the currently selected item is updated, by default passing the index of the selected item in the list. There is also a `.currentTextChanged` signal, which instead provides the label of the currently selected item. This signal is often more useful.
`QComboBox` can also be editable, allowing users to enter values not currently in the list and either have them inserted, or simply used as a value. To make the box editable:
python ```
combobox.setEditable(True)

```

You can also set a flag to determine how the insert is handled. These flags are stored on the `QComboBox` class itself and are listed below:
Flag | Behavior  
---|---  
`QComboBox.InsertPolicy.NoInsert` | No insert  
`QComboBox.InsertPolicy.InsertAtTop` | Insert as first item  
`QComboBox.InsertPolicy.InsertAtCurrent` | Replace currently selected item  
`QComboBox.InsertPolicy.InsertAtBottom` | Insert after last item  
`QComboBox.InsertPolicy.InsertAfterCurrent` | Insert after current item  
`QComboBox.InsertPolicy.InsertBeforeCurrent` | Insert before current item  
`QComboBox.InsertPolicy.InsertAlphabetically` | Insert in alphabetical order  
To use these, apply the flag as follows: 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
python ```
combobox.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

```

You can also limit the number of items allowed in the box by using the `.setMaxCount()` method:
python ```
combobox.setMaxCount(10)

```

For a more in-depth look at the `QComboBox` take a look at my [QComboBox documentation](https://www.pythonguis.com/docs/qcombobox/).
## `QListWidget`
Next `QListWidget`. It's very similar to `QComboBox`, differing mainly in the signals available and in its on-screen appearance. This one is a box with a list of options rather than a drop-down list:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    listwidget = QListWidget()
    listwidget.addItems(["One", "Two", "Three"])
    # In QListWidget there are two separate signals for the item, and the str
    listwidget.currentItemChanged.connect(self.index_changed)
    listwidget.currentTextChanged.connect(self.text_changed)
    self.setCentralWidget(listwidget)
  def index_changed(self, index): # Not an index, index is a QListWidgetItem
    print(index.text())
  def text_changed(self, text): # text is a str
    print(text)

```

![QListWidget on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets5.png) _QListWidget on Windows, Mac & Ubuntu Linux._
`QListWidget` offers a `currentItemChanged` signal that sends the `QListWidgetItem` (the element of the list box), and a `currentTextChanged` signal that sends the text of the item.
## `QLineEdit`
The `QLineEdit` widget is a simple single-line text editing box, into which users can type input. These are used for form fields, or settings where there is no restricted list of valid inputs. For example, when entering an email address or computer name:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    self.lineedit = QLineEdit()
    self.lineedit.setMaxLength(10)
    self.lineedit.setPlaceholderText("Enter your text")
    # widget.setReadOnly(True) # uncomment this to make readonly
    self.lineedit.returnPressed.connect(self.return_pressed)
    self.lineedit.selectionChanged.connect(self.selection_changed)
    self.lineedit.textChanged.connect(self.text_changed)
    self.lineedit.textEdited.connect(self.text_edited)
    self.setCentralWidget(self.lineedit)
  def return_pressed(self):
    print("Return pressed!")
    self.lineedit.setText("BOOM!")
  def selection_changed(self):
    print("Selection changed")
    print(self.lineedit.selectedText())
  def text_changed(self, text):
    print("Text changed...")
    print(text)
  def text_edited(self, text):
    print("Text edited...")
    print(text)

```

![QLineEdit on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets6.png) _QLineEdit on Windows, Mac & Ubuntu Linux._
As demonstrated in the above code, you can set a maximum length for the text in a line edit.
The `QLineEdit` has a number of signals available for different editing events, including when the _Enter_ key is pressed (by the user), and when the user selection is changed. There are also two edit signals, one for when the text in the box has been edited and one for when it has been changed. The distinction here is between user edits and programmatic changes. The `textEdited` signal is only sent when the user edits text.
Additionally, it is possible to perform input validation using an _input mask_ to define which characters are supported and where. This can be applied to the field as follows:
python ```
lineedit.setInputMask('000.000.000.000;_')

```

The above would allow a series of 3-digit numbers separated with periods, and could therefore be used to validate IPv4 addresses.
## `QSpinBox` and `QDoubleSpinBox`
`QSpinBox` provides a small numerical input box with arrows to increase and decrease the value. `QSpinBox` supports integers, while the related widget, `QDoubleSpinBox`, supports floats:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    spinbox = QSpinBox()
    # Or: doublespinbox = QDoubleSpinBox()
    spinbox.setMinimum(-10)
    spinbox.setMaximum(3)
    # Or: doublespinbox.setRange(-10, 3)
    spinbox.setPrefix("$")
    spinbox.setSuffix("c")
    spinbox.setSingleStep(3) # Or e.g. 0.5 for QDoubleSpinBox
    spinbox.valueChanged.connect(self.value_changed)
    spinbox.textChanged.connect(self.value_changed_str)
    self.setCentralWidget(spinbox)
  def value_changed(self, value):
    print(value)
  def value_changed_str(self, str_value):
    print(str_value)

```

Run it, and you'll see a numeric entry box. The value shows pre and post fix units, and is limited to the range +3 to -10.
![QSpinBox on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets7.png) _QSpinBox on Windows, Mac & Ubuntu Linux._
The demonstration code above shows the various features that are available for the widget.
To set the range of acceptable values, you can use `.setMinimum()` and `.setMaximum()`. You can alternatively use `.setRange()` to set both simultaneously. Annotation of value types is supported with both prefixes and suffixes that can be added to the number, e.g. for currency markers or units using `.setPrefix()` and `.setSuffix()`, respectively.
Clicking on the up and down arrows on the widget will increase or decrease the value in the widget by an amount, which can be set using `.setSingleStep()`. Note that this has no effect on the values that are acceptable to the widget.
Both `QSpinBox` and `QDoubleSpinBox` have a `.valueChanged` signal which fires whenever their value is altered. The raw `.valueChanged` signal sends the numeric value (either an `int` or a `float`) while `.textChanged` sends the value as a string, including both the prefix and suffix characters.
You can optionally disable text input on the spin box line edit, by setting it to read-only. With this set, the value can _only_ be changed using the controls. This also has the side effect of disabling the flashing cursor:
python ```
spinbox.lineEdit().setReadOnly(True)

```

## `QSlider`
`QSlider` provides a slide-bar widget, which internally works much like a `QDoubleSpinBox`. Rather than displaying the current value numerically, the slider defines its value by its handle position along the length of the widget. This is often useful when providing adjustment between two extremes, but where absolute accuracy is not required. The most common use of this type of widget is for volume controls.
There is an additional `.sliderMoved` signal that is triggered whenever the slider moves position and a `.sliderPressed` signal that emits whenever the slider is clicked:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    slider = QSlider()
    slider.setMinimum(-10)
    slider.setMaximum(3)
    # Or: widget.setRange(-10,3)
    slider.setSingleStep(3)
    slider.valueChanged.connect(self.value_changed)
    slider.sliderMoved.connect(self.slider_position)
    slider.sliderPressed.connect(self.slider_pressed)
    slider.sliderReleased.connect(self.slider_released)
    self.setCentralWidget(slider)
  def value_changed(self, value):
    print(value)
  def slider_position(self, position):
    print("position", position)
  def slider_pressed(self):
    print("Pressed!")
  def slider_released(self):
    print("Released")

```

Run this, and you'll see a slider widget on your screen. Drag the slider to change its value.
![QSlider on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets8.png) _QSlider on Windows, Mac & Ubuntu Linux._
You can also construct a slider with a vertical or horizontal orientation by passing the orientation in as you create it. The orientation flags are defined in the `Qt.Orientation` namespace. For example:
python ```
slider = QSlider(Qt.Orientation.Vertical)

```

Or:
python ```
slider = QSlider(Qt.Orientation.Horizontal)

```

## `QDial`
Finally, the `QDial` is a rotatable widget that works just like the slider but appears as an analog dial. This looks nice, but from a UI perspective is not particularly user-friendly. However, they are often used in audio applications as a simulation of real-world analog dials:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    dial = QDial()
    dial.setRange(-10, 100)
    dial.setSingleStep(1)
    dial.valueChanged.connect(self.value_changed)
    dial.sliderMoved.connect(self.dial_position)
    dial.sliderPressed.connect(self.dial_pressed)
    dial.sliderReleased.connect(self.dial_released)
    self.setCentralWidget(dial)
  def value_changed(self, value):
    print(value)
  def dial_position(self, position):
    print("position", position)
  def dial_pressed(self):
    print("Pressed!")
  def dial_released(self):
    print("Released")

```

Run this, and you'll see a circular dial, rotate it to select a number from the range.
![QDial on Windows, Mac & Ubuntu Linux.](https://www.pythonguis.com/static/tutorials/qt/basic-widgets/widgets9.png) _QDial on Windows, Mac & Ubuntu Linux._
The signals are the same as for `QSlider` and retain the same names (e.g. `.sliderMoved`).
## Conclusion
This concludes our brief tour of the common widgets used in PySide6 applications. To check the full list of available widgets, including all their signals and attributes, take a look at the [Qt documentation](http://doc.qt.io/qt-5/).
For a more in-depth look at widgets, check out our [QComboBox](https://www.pythonguis.com/docs/qcombobox/) and [QPushButton](https://www.pythonguis.com/docs/qpushbutton/) documentation.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
Continue with [ PySide6 Tutorial ](https://www.pythonguis.com/tutorials/pyside6-layouts/ "Continue to next part")
Return to [Create Desktop GUI Applications with PySide6 ](https://www.pythonguis.com/pyside6-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PySide6 Widgets** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/pyside6-widgets/Python books) on the subject. 
**PySide6 Widgets** was published in [tutorials](https://www.pythonguis.com/tutorials/) on October 03, 2021 (updated October 24, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [widgets](https://www.pythonguis.com/topics/widgets/) [qlabel](https://www.pythonguis.com/topics/qlabel/) [qcheckbox](https://www.pythonguis.com/topics/qcheckbox/) [qcombobox](https://www.pythonguis.com/topics/qcombobox/) [qlistbox](https://www.pythonguis.com/topics/qlistbox/) [qlistwidget](https://www.pythonguis.com/topics/qlistwidget/) [qlineedit](https://www.pythonguis.com/topics/qlineedit/) [qspinbox](https://www.pythonguis.com/topics/qspinbox/) [qdoublespinbox](https://www.pythonguis.com/topics/qdoublespinbox/) [qslider](https://www.pythonguis.com/topics/qslider/) [qwidget](https://www.pythonguis.com/topics/qwidget/) [ foundation](https://www.pythonguis.com/topics/foundation/) [ pyside6-foundation](https://www.pythonguis.com/topics/pyside6-foundation/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
