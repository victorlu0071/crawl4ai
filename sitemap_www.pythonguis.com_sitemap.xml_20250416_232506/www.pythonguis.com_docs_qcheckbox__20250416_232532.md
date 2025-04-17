# Content from: https://www.pythonguis.com/docs/qcheckbox/

[](https://www.pythonguis.com/docs/qcheckbox/#menu)
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
# QCheckBox
Toggleable checkable widget
by [Leo Well](https://www.pythonguis.com/authors/leo-well/) Last updated Feb 05 [ Documentation ](https://www.pythonguis.com/docs/)
A checkbox is a square-shaped widget used in graphical user interfaces (GUI) to provide users with a way to enable or disable options, or to allow users to enable or disable certain features of the app. Checkboxes usually have an adjacent label, indicating what the checkbox represents.
Checkboxes are usually used to represent _boolean_ state, being either _checked_ (on) or _unchecked_ (off). However, you can also have tri-state checkboxes with a third indeterminate state. In this tutorial, you'll learn how to create and customize checkboxes in your own applications, using the `QCheckBox` class.
## Creating Checkbox Widgets With `QCheckBox`
The [`QCheckBox`](https://doc.qt.io/qt-6/qcheckbox.html) class represents a **checkbox widget**. A checkbox is an option widget that can be switched on (checked) or off (unchecked) by the user. This widget is common in _settings_ or _preferences_ [dialogs](https://www.pythonguis.com/tutorials/pyqt6-dialogs/) where the user fine-tunes an application's configuration.
Checkboxes typically have a square shape looking like a checkbox on a paper form. We can click the box to switch it on and click it again to switch it off. When checked a cross or checkmark symbol will appear in the box. When a checkbox is unchecked, it will appear as an empty square.
If you're using [PyQt](https://www.pythonguis.com/pyqt6/) or [PySide](https://www.pythonguis.com/pyside6/) to create GUI applications in Python, then you can add checkboxes to your application with the `QCheckBox` class. This class provides two different constructors that we can use to create checkboxes:
Constructor | Description  
---|---  
[`QCheckBox(parent: QWidget = None)`](https://doc.qt.io/qt-6/qcheckbox.html#QCheckBox) | Constructs a checkbox with an optional parent widget but without an associated text  
[`QCheckBox(text: str, parent: QWidget = None)`](https://doc.qt.io/qt-6/qcheckbox.html#QCheckBox-1) | Constructs a checkbox with an associated description text and an optional parent widget  
To illustrate how to use the above constructors, let's get into our first example:
  * PyQt6
  * PySide6


python ```
import sys
from PyQt6.QtWidgets import (
  QApplication,
  QCheckBox,
  QVBoxLayout,
  QWidget,
)
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    # Checkbox with no label
    noTextCkBox = QCheckBox()
    # Checkbox with a text label
    textCkBox = QCheckBox(text="Option")
    layout = QVBoxLayout()
    layout.addWidget(noTextCkBox)
    layout.addWidget(textCkBox)
    self.setLayout(layout)
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

python ```
import sys
from PySide6.QtWidgets import (
  QApplication,
  QCheckBox,
  QVBoxLayout,
  QWidget,
)
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    # Checkbox with no label
    noTextCkBox = QCheckBox()
    # Checkbox with a text label
    textCkBox = QCheckBox(text="Option")
    layout = QVBoxLayout()
    layout.addWidget(noTextCkBox)
    layout.addWidget(textCkBox)
    self.setLayout(layout)
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

In this example, we import `QCheckBox` from the `QtWidgets` module. We create two `QCheckBox` instances in the `__init__` method of the `Window` class. The first is created using the constructor that does not require a text label.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Both constructors take an optional `parent` widget, but since we are adding the checkbox widgets to a layout, we don't need to pass a parent when contructing them.
Next up, we use the second constructor of `QCheckBox` to create another checkbox, this time with descriptive label. The text will display on the right of the checkbox. The text is a regular Python string. This label would typically be used to describe the option to be enabled or disabled, but here is just "Option".
Save this code to a `.py` file and run it. You'll get a window that looks something like this:
![QCheckBox constructors](https://www.pythonguis.com/static/docs/qcheckbox/qcheckbox-constructors.png)
As expected, the first checkbox has no associated text. It's just a square box on the window. This isn't too helpful, because it doesn't provide any information to your users. However, it can be useful when creating an array of checkboxes laid out to present some data in a table or a list.
The second checkbox on the window looks more familiar -- it has an associated text.
Both checkboxes are fully functional. We can _check_ and _uncheck_ them by clicking on them or -- in the case of the second example -- on the label. However, the checkboxes don't do any action yet, they just change their internal state from checked to unchecked and the other way around. To give a checkbox purpose we need to check the state and take action accordingly ourselves.
In most UIs checkboxes typically don't trigger external actions when toggled. [Use buttons](https://www.pythonguis.com/docs/qpushbutton/) to launch or trigger things.
Normal checkboxes have two internal states `Checked` and `Unchecked`, while tri-state checkboxes add a third `PartiallyChecked` state. Next we'll look at how to check and set these states on both two-state and tri-state checkboxes.
## Getting and Setting Checkbox state
The most important property of a checkbox is its internal _state_. This holds whether the checkbox is checked or not. By checking this property, you can take appropriate action in your application.
There are two main methods for checking the checkbox internal state -- `isChecked()` and `checkState()`. The possible values returned for a two-state checkbox are shown below:
Methods | Behavior  
---|---  
[`isChecked()`](https://doc.qt.io/qt-6/qabstractbutton.html#checked-prop) | Will return `True` if checkbox is checked, `False` if it is unchecked.  
[`checkState()`](https://doc.qt.io/qt-6/qcheckbox.html#checkState) | In two-state checkboxes this will return either `Checked` and `Unchecked`.  
Consider the following example:
  * PyQt6
  * PySide6


python ```
import sys
from PyQt6.QtWidgets import (
  QApplication,
  QCheckBox,
  QVBoxLayout,
  QWidget,
)
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.checkBox = QCheckBox(text="Unchecked")
    layout = QVBoxLayout()
    layout.addWidget(self.checkBox)
    self.setLayout(layout)
    self.checkBox.stateChanged.connect(self.onStateChanged)
  def onStateChanged(self):
    if self.checkBox.isChecked():
      self.checkBox.setText("Checked")
    else:
      self.checkBox.setText("Unchecked")
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

python ```
import sys
from PySide6.QtWidgets import (
  QApplication,
  QCheckBox,
  QVBoxLayout,
  QWidget,
)
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.checkBox = QCheckBox(text="Unchecked")
    layout = QVBoxLayout()
    layout.addWidget(self.checkBox)
    self.setLayout(layout)
    self.checkBox.stateChanged.connect(self.onStateChanged)
  def onStateChanged(self):
    if self.checkBox.isChecked():
      self.checkBox.setText("Checked")
    else:
      self.checkBox.setText("Unchecked")
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

In this example, we first create a `QCheckBox` instance with the text `"Click me!"` on it. In this case, we're defining a two-state checkbox, which represents the default behavior of this widget.
Then we create the app's layout and add the checkbox. Finally, we connect the `stateChanged()` signal with the `onStateChanged()` slot or method. This signal is emitted whenever we click the checkbox, and the `onStateChanged()` method is automatically called.
You can use the `stateChanged()` signal to trigger something to happen each time the checkbox changes its state. To connect the `stateChanged()` signal to a slot, you use the standard syntax:
python ```
checkbox.<signal>.connect(<method>)

```

In this construct, `checkbox` is the `QCheckBox` object we need to connect to a given slot. The `<signal>` name is `stateChanged`. Finally, `<method>` represents the target slot or method we want to connect the signal.
The `onStateChanged()` method uses `isChecked()` to determine the current state of our checkbox. This method returns `True` if the checkbox is checked and `False` if it's unchecked. The checkbox text changes alternatively from _Checked_ to _Unchecked_ depending on the result of this condition:
![Two-state checkbox](https://www.pythonguis.com/static/docs/qcheckbox/two-state-checkbox.gif)
Whenever you click the checkbox on this window, the text changes from _Checked_ to _Unchecked_ alternatively.
It's usually not a good idea to change a checkbox label with the state as it's confusing. Does the "Unchecked" label next to a unchecked checkbox mean checked or unchecked?
We could have used `checkState()` to determine the current state of our checkbox in the above example. However, using `isChecked()` feels more natural when working with two-state checkboxes.
When we are working with tri-state checkboxes, `checkState()` is our only option. We'll see how to work with `checkState()` in the next section.
## Building and Working With Tri-State Checkboxes
In addition to regular two-state checkboxes, you can optionally create tri-state checkboxes. This type of checkbox comes in handy when we want to give our user the option to set the checkbox in an intermediate state known as a **partially checked** state. This state means that the checkbox is neither checked nor unchecked.
Tri-state checkboxes are typically used to represent groups of other checkboxes, allowing them to all be turned on or off in one go. The _partially_ checked state then indicates that some of the children are on and some are off.
When using tri-state checkboxes, the `isChecked()` and `checkState()` methods return the following values --
Methods | Behavior  
---|---  
[`isChecked()`](https://doc.qt.io/qt-6/qabstractbutton.html#checked-prop) | Will return `True` if checkbox is checked or partially checked, `False` if it is unchecked.  
[`checkState()`](https://doc.qt.io/qt-6/qcheckbox.html#checkState) | In three-state checkboxes this will return either `Checked`, `Unchecked` or `PartiallyChecked` .  
The `QCheckBox` class has a Boolean [`tristate`](https://doc.qt.io/qt-6/qcheckbox.html#tristate-prop) property that indicates whether the checkbox is tri-state. This property defaults to `False`. If we set it to `True`, we turn our checkbox into a tri-state checkbox. To change the value of `tristate`, you need to use the `setTristate()` with a boolean value as an argument.
You can also turn a checkbox tri-state by setting a _partially checked_ state on it, using `.setState(Qt.CheckState.PartiallyChecked)`.
Consider the following example: 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
  * PyQt6
  * PySide6


python ```
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
  QApplication,
  QCheckBox,
  QVBoxLayout,
  QWidget,
)
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.triStateCheckBox = QCheckBox(text="Unchecked")
    self.triStateCheckBox.setTristate(True)
    layout = QVBoxLayout()
    layout.addWidget(self.triStateCheckBox)
    self.setLayout(layout)
    self.triStateCheckBox.stateChanged.connect(self.onStateChanged)
  def onStateChanged(self):
    state = self.triStateCheckBox.checkState()
    if state == Qt.CheckState.Checked:
      self.triStateCheckBox.setText("Checked")
    elif state == Qt.CheckState.PartiallyChecked:
      self.triStateCheckBox.setText("Partially checked")
    else:
      self.triStateCheckBox.setText("Unchecked")
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

python ```
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
  QApplication,
  QCheckBox,
  QVBoxLayout,
  QWidget,
)
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.triStateCheckBox = QCheckBox(text="Unchecked")
    self.triStateCheckBox.setTristate(True)
    layout = QVBoxLayout()
    layout.addWidget(self.triStateCheckBox)
    self.setLayout(layout)
    self.triStateCheckBox.stateChanged.connect(self.onStateChanged)
  def onStateChanged(self):
    state = self.triStateCheckBox.checkState()
    if state == Qt.CheckState.Checked:
      self.triStateCheckBox.setText("Checked")
    elif state == Qt.CheckState.PartiallyChecked:
      self.triStateCheckBox.setText("Partially checked")
    else:
      self.triStateCheckBox.setText("Unchecked")
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

In this example, we create a regular checkbox using the `QCheckBox()` constructor. To set this checkbox as tri-state, you call `.setTristate()` with `True` as an argument. From now on, our checkbox will have three states represented by the following [values](https://doc.qt.io/qt-6/qt.html#CheckState-enum):
Constant | Value | Description  
---|---|---  
`Qt.CheckState.Unchecked` | `0` | The checkbox is unchecked.  
`Qt.CheckState.PartiallyChecked` | `1` | The checkbox is partially checked.  
`Qt.CheckState.Checked` | `2` | The checkbox is checked.  
In tri-state checkboxes, the `isChecked()` method will return `True` whether the checkbox is checked or partially checked, and `False` if it is unchecked.
If you want to distinguish between _checked_ and _partially checked_ states, you need to use `checkState()` directly. Calling `checkState()` returns one of the constants in the above table, representing the current state of the checkbox.
Our `onStateChanged()` method is connected to the `stateChanged` signal of the checkbox. In this method, we get the current state by calling `checkState()` on the checkbox and storing the result in the variable `state`. We then check the value of this variable against the different states and take action accordingly. In this example, we alternatively change the checkbox text to reflect its state.
Here's how this example works in practice:
![Tri-state checkbox](https://www.pythonguis.com/static/docs/qcheckbox/tri-state-checkbox.gif)
When you click the checkbox, its text changes from _Unchecked_ to _Partially checked_ and finally to _Checked_. These are the three possible states of this kind of checkbox.
While we used the `checkState()` method above, the `stateChanged` signal actually sends the current state, as an integer value, to the slot. We can map that into the correct state in the method directly by passing it to `Qt.CheckState`. For example.
python ```
  def onStateChanged(self, state):
    state = Qt.CheckState(state)
    if state == Qt.CheckState.Checked:
      self.triStateCheckBox.setText("Checked")
    elif state == Qt.CheckState.PartiallyChecked:
      self.triStateCheckBox.setText("Partially checked")
    else:
      self.triStateCheckBox.setText("Unchecked")

```

In this alternative implementation of `onStateChanged()`, we receive a `state` argument that we map to a `Qt.CheckState` object. The rest of the code remains the same.
The mapping step is only required in PyQt6. In both PyQt5, PySide2, and PySide6 this is done automatically.
It's up to you which implementation to use in your code.
## Using Checkboxes in Practice
We can use checkbox widgets to provide a clean and user-friendly way to enable or disable options in a GUI app. Checkboxes are useful when building _preferences_ or _setting_ dialogs where the users can customize our applications. For example, say that you're making a text editor and you want to allow the user to customize a few features like:
  * Show word count
  * Auto pair brackets
  * Show minimap


Checkbox options shouldn't usually be mutually exclusive. If you have mutually exclusive options, consider using the [`QRadioButton`](https://doc.qt.io/qt-6/qradiobutton.html) class instead.
In this case, you can use a checkbox for each of these options like in the following code:
  * PyQt6
  * PySide6


python ```
import sys
from PyQt6.QtWidgets import (
  QApplication,
  QCheckBox,
  QLabel,
  QVBoxLayout,
  QWidget,
)
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.wordCountCkBox = QCheckBox(text="Show word count", parent=self)
    self.bracketsCkBox = QCheckBox(text="Auto pair brackets", parent=self)
    self.minimapCkBox = QCheckBox(text="Show minimap", parent=self)
    self.selectionLabel = QLabel(text="No selection yet", parent=self)
    layout = QVBoxLayout()
    layout.addWidget(self.wordCountCkBox)
    layout.addWidget(self.bracketsCkBox)
    layout.addWidget(self.minimapCkBox)
    layout.addWidget(self.selectionLabel)
    self.setLayout(layout)
    self.wordCountCkBox.stateChanged.connect(self.onStateChanged)
    self.bracketsCkBox.stateChanged.connect(self.onStateChanged)
    self.minimapCkBox.stateChanged.connect(self.onStateChanged)
  def onStateChanged(self):
    selection = "You've selected:\n"
    if self.wordCountCkBox.isChecked():
      selection += "- Word count\n"
    if self.bracketsCkBox.isChecked():
      selection += "- Auto pair brackets\n"
    if self.minimapCkBox.isChecked():
      selection += "- Show minimap\n"
    self.selectionLabel.setText(selection)
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

python ```
import sys
from PySide6.QtWidgets import (
  QApplication,
  QCheckBox,
  QLabel,
  QVBoxLayout,
  QWidget,
)
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.wordCountCkBox = QCheckBox(text="Show word count", parent=self)
    self.bracketsCkBox = QCheckBox(text="Auto pair brackets", parent=self)
    self.minimapCkBox = QCheckBox(text="Show minimap", parent=self)
    self.selectionLabel = QLabel(text="No selection yet", parent=self)
    layout = QVBoxLayout()
    layout.addWidget(self.wordCountCkBox)
    layout.addWidget(self.bracketsCkBox)
    layout.addWidget(self.minimapCkBox)
    layout.addWidget(self.selectionLabel)
    self.setLayout(layout)
    self.wordCountCkBox.stateChanged.connect(self.onStateChanged)
    self.bracketsCkBox.stateChanged.connect(self.onStateChanged)
    self.minimapCkBox.stateChanged.connect(self.onStateChanged)
  def onStateChanged(self):
    selection = "You've selected:\n"
    if self.wordCountCkBox.isChecked():
      selection += "- Word count\n"
    if self.bracketsCkBox.isChecked():
      selection += "- Auto pair brackets\n"
    if self.minimapCkBox.isChecked():
      selection += "- Show minimap\n"
    self.selectionLabel.setText(selection)
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

In this example, we create three checkboxes, one per option. We also create a label object to show the user's selections. If you run this application, then you'll get the following behavior:
![Checkboxes for text editor settings](https://www.pythonguis.com/static/docs/qcheckbox/text-editor-settings.gif)
This dialog shows the three required options for your text editor. Of course, this dialog doesn't look like a fully functional _setting_ or _preferences_ dialog. It intends to show how you can use checkboxes to provide non-exclusive options to your users. Note that you can select any combination of options.
## Setting Other Properties of `QCheckBox`
Up to this point, we've learned how to create two-state and tri-state checkboxes in your GUI applications. We've also learned how to make our checkboxes perform actions in response to state changes by connecting the `stateChanged` signals with concrete methods known as slots.
In this section, we'll learn about other useful features of `QCheckBox`, including the `text` and `icon` properties shown below:
Property | Description | Getter Method | Setter Method  
---|---|---|---  
[`text`](https://doc.qt.io/qt-6/qabstractbutton.html#text-prop) | Holds the text shown on the button | `text()` | `setText()`  
[`icon`](https://doc.qt.io/qt-6/qabstractbutton.html#icon-prop) | Holds the icon shown on the button | `icon()` | `setIcon()`  
As its name suggests, the `text` property controls the current text associated with a checkbox. You can use the `setText()` method to change this property and `text()` to retrieve its current value if needed. In previous sections, you used `setText()` to change the text of a checkbox. So, let's focus on how to work with icons.
Here's an example of a checkbox representing a traffic light in which each state will have its own associated icon:
  * PyQt6
  * PySide6


python ```
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QCheckBox, QVBoxLayout, QWidget
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.lightCkBox = QCheckBox(parent=self)
    self.lightCkBox.setTristate(True)
    self.lightCkBox.setIcon(QIcon("icons/red.png"))
    layout = QVBoxLayout()
    layout.addWidget(self.lightCkBox)
    self.setLayout(layout)
    self.lightCkBox.stateChanged.connect(self.onStateChanged)
  def onStateChanged(self, state):
    state = Qt.CheckState(state)
    if state == Qt.CheckState.Checked:
      self.lightCkBox.setIcon(QIcon("icons/green.png"))
    elif state == Qt.CheckState.PartiallyChecked:
      self.lightCkBox.setIcon(QIcon("icons/yellow.png"))
    else:
      self.lightCkBox.setIcon(QIcon("icons/red.png"))
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

python ```
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QCheckBox, QVBoxLayout, QWidget
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.lightCkBox = QCheckBox(parent=self)
    self.lightCkBox.setTristate(True)
    self.lightCkBox.setIcon(QIcon("icons/red.png"))
    layout = QVBoxLayout()
    layout.addWidget(self.lightCkBox)
    self.setLayout(layout)
    self.lightCkBox.stateChanged.connect(self.onStateChanged)
  def onStateChanged(self, state):
    state = Qt.CheckState(state)
    if state == Qt.CheckState.Checked:
      self.lightCkBox.setIcon(QIcon("icons/green.png"))
    elif state == Qt.CheckState.PartiallyChecked:
      self.lightCkBox.setIcon(QIcon("icons/yellow.png"))
    else:
      self.lightCkBox.setIcon(QIcon("icons/red.png"))
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

In this example, we use the `setIcon()` method to change the icon associated with the checkbox according to its current state. Go ahead and run the app! You'll get a window like the following:
![Checkbox with icons](https://www.pythonguis.com/static/docs/qcheckbox/checkbox-icons.gif)
In this example, the red light is associated with the unchecked state, the yellow light is linked to the partially checked state, and the green light is associated with the checked state.
Using icons like in this example is something rare with checkbox widgets. You'll typically use descriptive text. But it's good to know the capability is there for when you need it.
## Conclusion
Checkboxes are useful widgets in any GUI application. They allow us to give our users a clean way to enable or disable options in our applications. They are commonly used in dialogs and preferences windows to allow enabling and disabling of application features or configuring behavior.
In this tutorial, you've learned how to create, use, and customize checkboxes while building a GUI application with PyQt.
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Leo Well](https://www.pythonguis.com/static/theme/images/authors/leo-well.jpg)](https://www.pythonguis.com/authors/leo-well/)
**QCheckBox** was written by [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
**QCheckBox** was published in [docs](https://www.pythonguis.com/docs/) on January 20, 2023 (updated February 05, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [widgets](https://www.pythonguis.com/topics/widgets/) [qcombobox](https://www.pythonguis.com/topics/qcombobox/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
