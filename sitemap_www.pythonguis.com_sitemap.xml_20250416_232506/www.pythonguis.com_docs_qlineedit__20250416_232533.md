# Content from: https://www.pythonguis.com/docs/qlineedit/

[](https://www.pythonguis.com/docs/qlineedit/#menu)
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
# QLineEdit
A Simple Text Input Widget
by [Leo Well](https://www.pythonguis.com/authors/leo-well/) Last updated Jan 12 [ Documentation ](https://www.pythonguis.com/docs/)
The `QLineEdit` class is a versatile tool for single-line text input. The widget facilitates text manipulation by supporting insertion, deletion, selection, and cut-copy-paste operations natively. You can use line edits when you need to accept text input from your users in a PyQt/PySide application.
The widget is highly customizable. You can set it up to include placeholder text, input masks, input validators, and more. It also supports many keyboard shortcuts out of the box and is able to process custom ones. This feature opens an opportunity to enhance user input speed and efficiency.
In this article, you will learn the basics of using `QLineEdit` by going through its most commonly used features and capabilities.
Table of Contents
  * [Creating Line Edit Widgets With QLineEdit](https://www.pythonguis.com/docs/qlineedit/#creating-line-edit-widgets-with-qlineedit)
    * [Creating Non-Editable Line Edits](https://www.pythonguis.com/docs/qlineedit/#creating-non-editable-line-edits)
    * [Creating Line Edits for Passwords](https://www.pythonguis.com/docs/qlineedit/#creating-line-edits-for-passwords)
  * [Manipulating the Input in a Line Edit](https://www.pythonguis.com/docs/qlineedit/#manipulating-the-input-in-a-line-edit)
  * [Aligning and Formatting the Text in a Line Edit](https://www.pythonguis.com/docs/qlineedit/#aligning-and-formatting-the-text-in-a-line-edit)
  * [Connecting Signals and Slots](https://www.pythonguis.com/docs/qlineedit/#connecting-signals-and-slots)
  * [Validating Input in Line Edits](https://www.pythonguis.com/docs/qlineedit/#validating-input-in-line-edits)
  * [Conclusion](https://www.pythonguis.com/docs/qlineedit/#conclusion)


## Creating Line Edit Widgets With `QLineEdit`
A line edit allows the user to enter and edit a single line of plain text with a useful collection of editing functionalities, such as insertion, deletion, selection, cut-copy-paste, and drag-and-drop operations.
If you've used [PyQt](https://www.pythonguis.com/pyqt6/) or [PySide](https://www.pythonguis.com/pyside6/) to create GUI applications in Python, then it'd be likely that you already know about the [`QLineEdit`](https://doc.qt.io/qt-6/qlineedit.html) class. This class allows you to create line edits in your graphical interfaces (GUI) quickly.
The `QLineEidt` class provides two different constructors that you can use to create line edits according to your needs:
Constructor | Description  
---|---  
[`QLineEdit(parent: QWidget = None)`](https://doc.qt.io/qt-6/qlineedit.html#QLineEdit) | Constructs a line edit with a parent widget but without text  
[`QLineEdit(text: str, parent: QWidget = None)`](https://doc.qt.io/qt-6/qlineedit.html#QLineEdit-1) | Constructs a line edit with default text and a parent widget  
The parent widget would be the window or dialog where you need to place the line edit. The text can be a default text that will appear in the line edit when you run the application. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
To illustrate how to use the above constructors, we can code a demo example:
python ```
from PyQt6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setWindowTitle("QLineEdit Constructors")
    self.resize(300, 100)
    # Line edit with a parent widget
    top_line_edit = QLineEdit(parent=self)
    # Line edit with a parent widget and a default text
    bottom_line_edit = QLineEdit(
      "Hello! This is a line edit.", parent=self
    )
    layout = QVBoxLayout()
    layout.addWidget(top_line_edit)
    layout.addWidget(bottom_line_edit)
    self.setLayout(layout)
app = QApplication([])
window = Window()
window.show()
app.exec()

```

In this example, we first do the required imports and then define the `Window` class inheriting from `QWidget`. Inside `Window`, we create two `QLineEdit` widgets.
To create the first line edit, we use the first constructor of `QLineEdit`, passing only a `parent` widget. For the second line editor, we use the second constructor, which requires the parent widget and a default text. Note that the text is a regular Python string.
Save the code to a file called `constructors.py` file and run it from your command line. You'll get a window that looks something like this:
![QLineEdit constructors example](https://www.pythonguis.com/static/docs/qlineedit/qlineedit-constructors.png) _Standard window showing our two line edits._
The first line edit has no text. In most cases, this is how you would create your line edits because they're designed for accepting input. If you'd like to just display some text, then you can use a `QLabel` widget instead. The second line edit displays the text that you passed to the constructor.
Both line edits are ready for accepting input text. Note that you can use all the following keyboard shortcuts to optimize your text input process:
Keys | Action  
---|---  
Left Arrow | Moves the cursor one character to the left  
Shift+Left Arrow | Moves and selects text one character to the left  
Right Arrow | Moves the cursor one character to the right  
Shift+Right Arrow | Moves and selects text one character to the right  
Home | Moves the cursor to the beginning of the line  
End | Moves the cursor to the end of the line  
Backspace | Deletes the character to the left of the cursor  
Ctrl+Backspace | Deletes the word to the left of the cursor  
Delete | Deletes the character to the right of the cursor  
Ctrl+Delete | Deletes the word to the right of the cursor  
Ctrl+A | Select all  
Ctrl+C | Copies the selected text to the clipboard  
Ctrl+Insert | Copies the selected text to the clipboard  
Ctrl+K | Deletes to the end of the line  
Ctrl+V | Pastes the clipboard text into the line edit  
Shift+Insert | Pastes the clipboard text into the line edit  
Ctrl+X | Deletes the selected text and copies it to the clipboard  
Shift+Delete | Deletes the selected text and copies it to the clipboard  
Ctrl+Z | Undoes the last operation  
Ctrl+Y | Redoes the last undone operation  
That's a lot of shortcuts! This table is just a sample of all the features that the `QLineEdit` class provides out of the box.
In addition to these keyboard shortcuts, the `QLineEdit` class provides a context menu that you can trigger by clicking on a line edit using the right button of your mouse:
![QLineEdit context menu](https://www.pythonguis.com/static/docs/qlineedit/qlineedit-context-menu.png) _QLineEdit with a context menu visible._
The built-in context menu provides basic edition options, such as cut, copy, paste, and delete. It also has options for undoing and redoing edits, and for selecting all the content of a given line edit.
### Creating Non-Editable Line Edits
Sometimes, we need to make a line edit non-editable. By default, all line edits are editable because their main use case is to provide text input for the user. However, in some situations, a non-editable line edit can be useful.
For example, say that you're creating a GUI application that generates some recovery keys for the users. The user must be able to copy the key to a safe place so that they can use it to recover access if they forget their password. In this situation, creating a non-editable line edit can provide a suitable solution.
To make a line edit read-only, we can use the [`readOnly`](https://doc.qt.io/qt-6/qlineedit.html#readOnly-prop) property and its setter method `setReadOnly()` as in the following example:
python ```
import secrets
from PyQt6.QtWidgets import (
  QApplication,
  QLabel,
  QLineEdit,
  QVBoxLayout,
  QWidget,
)
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setWindowTitle("Non-editable QLineEdit")
    self.resize(300, 100)
    non_editable_line_edit = QLineEdit(parent=self)
    non_editable_line_edit.setReadOnly(True)
    non_editable_line_edit.setText(secrets.token_hex(16))
    layout = QVBoxLayout()
    layout.addWidget(QLabel(parent=self, text="Your secret key:"))
    layout.addWidget(non_editable_line_edit)
    self.setLayout(layout)
app = QApplication([])
window = Window()
window.show()
app.exec()

```

In this example, we create a non-editable line edit by using the `setReadOnly()` method. When we set the `readOnly` property to `True`, our line edit won't accept editions. It'll only allow us to select and copy its content.
Go ahead and run the application from your command line to explore how this line edit works. You'll get a window like the following:
![Non-editable line edit](https://www.pythonguis.com/static/docs/qlineedit/non-editable-lineedit.png) _A read-only line edit with editing disabled._
If you play a bit with this line edit, you'll soon discover that you can't change its text. You'll also note that the options in the context menu are now limited to _Copy_ and _Select All_.
### Creating Line Edits for Passwords
Another cool feature of the `QLineEdit` class is that it allows you to create text input for passwords. This can be pretty convenient for those applications that manage several users, and each user needs to have access credentials.
You can create line edits for passwords by using the [`echoMode()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtwidgets/qlineedit.html#echoMode) method. This method takes one of the following constants as an argument:
Constant | Value | Description  
---|---|---  
`QLineEdit.EchoMode.Normal` | `0` | Display characters as you enter them.  
`QLineEdit.EchoMode.NoEcho` | `1` | Display no characters when you enter them.  
`QLineEdit.EchoMode.Password` | `2` | Display platform-dependent password mask characters instead of the characters you enter.  
`QLineEdit.EchoMode.PasswordEchoOnEdit` | `3` | Display characters as you enter them while editing. Display characters as the `Password` mode does when reading.  
The `Normal` mode is the default. The `NoEcho` mode may be appropriate for critical passwords where even the length of the password should be kept secret. The `Password` mode is appropriate for most password use cases, however `PasswordEchoOnEdit` can be used instead if you need to give users some confirmation of what they are typing.
Here's a sample app that shows a user and password form:
python ```
from PyQt6.QtWidgets import (
  QApplication,
  QFormLayout,
  QLineEdit,
  QWidget,
)
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setWindowTitle("Password QLineEdit")
    self.resize(300, 100)
    username_line_edit = QLineEdit(parent=self)
    password_line_edit = QLineEdit(parent=self)
    password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
    layout = QFormLayout()
    layout.addRow("Username:", username_line_edit)
    layout.addRow("Password:", password_line_edit)
    self.setLayout(layout)
app = QApplication([])
window = Window()
window.show()
app.exec()

```

In this example, you call `setEchoMode()` on the `password_line_edit` widget using the `Password` mode as an argument. When you run this code from your command line, you get the following window on your screen:
![Password line edit](https://www.pythonguis.com/static/docs/qlineedit/password-qlineedit.png) _Window with a username and password line edit._
The `username_line_edit` line edit is in `Normal` mode, so we can see the characters as we type them in. In contrast, the Password line edit is in `Password` mode. In this case, when we enter a character, the line edit shows the platform's character for passwords.
## Manipulating the Input in a Line Edit
You can change the text of a line edit using the [`setText()`](https://doc.qt.io/qt-6/qlineedit.html#text-prop) or [`insert()`](https://doc.qt.io/qt-6/qlineedit.html#insert) methods. You can retrieve the text with the [`text()`](https://doc.qt.io/qt-6/qlineedit.html#text-prop) method. However, these are not the only operations that you can perform with the text of a line edit.
The following table shows a summary of some of the most commonly used methods for text manipulation in line edits:
Method | Description  
---|---  
[`setText(text)`](https://doc.qt.io/qt-6/qlineedit.html#text-prop) | Sets the text of a line edit to `text`, clears the selection, clears the undo/redo history, moves the cursor to the end of the line, and resets the [modified](https://doc.qt.io/qt-6/qlineedit.html#modified-prop) property to false.  
[`insert(text)`](https://doc.qt.io/qt-6/qlineedit.html#insert) | Deletes any selected text, inserts `text`, and validates the result. If it is valid, it sets it as the new contents of the line edit.  
[`clear()`](https://doc.qt.io/qt-6/qlineedit.html#clear) | Clears the contents of the line edit.  
[`copy()`](https://doc.qt.io/qt-6/qlineedit.html#copy) | Copies the selected text to the clipboard.  
[`cut()`](https://doc.qt.io/qt-6/qlineedit.html#cut) | Copies the selected text to the clipboard and deletes it from the line edit.  
[`paste()`](https://doc.qt.io/qt-6/qlineedit.html#paste) | Inserts the clipboard's text at the cursor position, deleting any selected text.  
[`redo()`](https://doc.qt.io/qt-6/qlineedit.html#redo) | Redoes the last operation if redo is [available](https://doc.qt.io/qt-6/qlineedit.html#redoAvailable-prop). Redo becomes available once the user has performed one or more undo operations on text in the line edit.  
[`undo()`](https://doc.qt.io/qt-6/qlineedit.html#undo) | Undoes the last operation if undo is [available](https://doc.qt.io/qt-6/qlineedit.html#undoAvailable-prop). Undo becomes available once the user has modified the text in the line edit.  
[`selectAll()`](https://doc.qt.io/qt-6/qlineedit.html#selectAll) | Selects all the text and moves the cursor to the end.  
You can use any of these methods to manipulate the text of a line edit from your code. Consider the following example where you have two line edits and two buttons that take advantage of some of the above methods to copy some text from one line edit to the other:
python ```
from PyQt6.QtWidgets import (
  QApplication,
  QGridLayout,
  QLabel,
  QLineEdit,
  QPushButton,
  QWidget,
)
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setWindowTitle("Copy and Paste")
    self.resize(300, 100)
    self.source_line_edit = QLineEdit(parent=self)
    self.source_line_edit.setText("Hello, World!")
    self.dest_line_edit = QLineEdit(parent=self)
    copy_button = QPushButton(parent=self, text="Copy")
    paste_button = QPushButton(parent=self, text="Paste")
    copy_button.clicked.connect(self.copy)
    paste_button.clicked.connect(self.paste)
    layout = QGridLayout()
    layout.addWidget(self.source_line_edit, 0, 0)
    layout.addWidget(copy_button, 0, 1)
    layout.addWidget(self.dest_line_edit, 1, 0)
    layout.addWidget(paste_button, 1, 1)
    self.setLayout(layout)
  def copy(self):
    self.source_line_edit.selectAll()
    self.source_line_edit.copy()
  def paste(self):
    self.dest_line_edit.clear()
    self.dest_line_edit.paste()
app = QApplication([])
window = Window()
window.show()
app.exec()

```

In this example, we create two line edits. The first one will hold some sample text. The second line edit will receive the text. Then, we create two buttons and connect their `clicked` signals to the `copy()` and `paste()` slots.
Inside the `copy()` method we first select all the text from the source line edit. Then we use the `copy()` method to copy the selected text to the clipboard. In `paste()`, we call `clear()` on the destination line edit to remove any previous text. Then, we use the `paste()` method to copy the clipboard's content.
Go ahead and run the application. You'll get the following window on your screen: 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
![QLineEdit Copy and Paste](https://www.pythonguis.com/static/docs/qlineedit/qlineedit-text-manipulation.png) _QLineEdit with Copy & Paste buttons attached to handlers._
Once you've run the app, then you can click the _Copy_ button to copy the text in the first line edit. Next, you can click the _Paste_ button to paste the copied text to the second line edit. Go ahead and give it a try!
## Aligning and Formatting the Text in a Line Edit
You can also align and format the text in a line edit. For example, for text alignment, you can use the [`setAlignment()`](https://doc.qt.io/qt-6/qlineedit.html#alignment-prop) method with one or more alignment flags. Some of the most useful flags that you can find in the [`Qt.AlignmentFlag`](https://doc.qt.io/qt-6/qt.html#AlignmentFlag-enum) namespace includes the following:
Flag | Description  
---|---  
`AlignLeft` | Aligns with the left edge.  
`AlignRight` | Aligns with the right edge.  
`AlignHCenter` | Centers horizontally in the available space.  
`AlignJustify` | Justifies the text in the available space.  
`AlignTop` | Aligns with the top.  
`AlignBottom` | Aligns with the bottom.  
`AlignVCenter` | Centers vertically in the available space.  
`AlignCenter` | Centers in both dimensions.  
If you want to apply multiple alignment flags to a given line edit, you don't have to call `setAlignment()` multiple times. You can just use the bitwise OR operator (`|`) to combine them. Consider the following example:
python ```
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLineEdit
class Window(QLineEdit):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setWindowTitle("Aligning Text")
    self.resize(300, 100)
    self.setText("Hello, World!")
    self.setAlignment(Qt.AlignmentFlag.AlignCenter)
app = QApplication([])
window = Window()
window.show()
app.exec()

```

In this example, we use a `QLineEdit` as the only component of our app's GUI. Using the `setAlignment()` method, we center the `"Hello, World!"` message in both directions, horizontally and vertically. To do this, we use the `AlignCenter` flag. Here's what the app looks like:
![QLineEdit text alignment](https://www.pythonguis.com/static/docs/qlineedit/qlineedit-text-alignment.png) _QLineEdit with text alignment set._
Go ahead and play with other flags to see their effect on the text alignment. Use the `|` bitwise operator to combine several alignment flags.
Line edits also have a `textMargins` property that you can tweak to customize the text alignment using specific values. To set margin values for your text, you can use the `setTextMargins()` method, which has the following signatures:
Method | Description  
---|---  
[`setTextMargins(left, top, right, bottom)`](https://doc.qt.io/qt-6/qlineedit.html#setTextMargins) | Sets the margins around the text to have the sizes `left`, `top`, `right`, and `bottom`.  
[`setTextMargins(margins)`](https://doc.qt.io/qt-6/qlineedit.html#setTextMargins-1) | Sets the `margins` around the text using a [`QMargins`](https://doc.qt.io/qt-6/qmargins.html) object.  
The first signature allows you to provide four integer values as the left, top, right, and bottom margins for the text. The second signature accepts a `QMargins` object as an argument. To build this object, you can use four integer values with the same meaning as the `left`, `top`, `right`, and `bottom` arguments in the first signature.
Here's an example of how to set custom margins for the text in a line edit:
python ```
from PyQt6.QtWidgets import QApplication, QLineEdit
class Window(QLineEdit):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setWindowTitle("Aligning Text")
    self.resize(300, 100)
    self.setText("Hello, World!")
    self.setTextMargins(30, 30, 0, 0)
app = QApplication([])
window = Window()
window.show()
app.exec()

```

In this example, you set the left and top margins to custom values. Here's how this app looks when you run it:
![QLineEdit text margins](https://www.pythonguis.com/static/docs/qlineedit/qlineedit-text-margins.png) _QLineEdit with text margins added._
Using the `setTextMargins()` method, we can place the text in the desired place in a line edit, which may be a requirement in some situations.
## Connecting Signals and Slots
When you're creating a GUI application and you need to use line edits, you may need to perform actions when the user enters or modifies the content of the line edit. To do this, you need to connect some of the signals of the line edit to specific slots or functions.
Depending on specific user events, the `QLineEdit` class can emit several different signals. Here's is a summary of these signals and their corresponding meaning:
Signal | Emitted  
---|---  
[`textChanged(text)`](https://doc.qt.io/qt-6/qlineedit.html#textChanged) | Whenever the user changes the text either manually or programmatically. The `text` argument is the new text.  
[`textEdited(text)`](https://doc.qt.io/qt-6/qlineedit.html#textEdited) | Whenever the user edits the text manually. The `text` argument is the new text.  
[`editingFinished`](https://doc.qt.io/qt-6/qlineedit.html#editingFinished) | When the user presses the _Return_ or _Enter_ key, or when the line edit loses focus, and its contents have changed since the last time this signal was emitted.  
[`inputRejected`](https://doc.qt.io/qt-6/qlineedit.html#inputRejected) | When the user presses a key that is an unacceptable input.  
[`returnPressed`](https://doc.qt.io/qt-6/qlineedit.html#returnPressed) | When the user presses the _Return_ or _Enter_ key.  
[`selectionChanged`](https://doc.qt.io/qt-6/qlineedit.html#selectionChanged) | When the selection changes.  
We can connect either of these signals with any slot. A slot is a method or function that performs a concrete action in your application. We can connect a signal and a slot so that the slot gets called when the signal gets emitted. Here's the required syntax to do this:
python ```
line_edit.<signal>.connect(<method>)

```

In this construct, `line_edit` is the `QLineEdit` object that we need to connect with a given slot. The `<signal>` placeholder can be any of the abovementioned signals. Finally, `<method>` represents the target slot or method.
Let's write an example that puts this syntax into action. For this example, we'll connect the `textEdited` signal with a method that updates the text of a `QLabel` to match the text of our line edit:
python ```
from PyQt6.QtWidgets import (
  QApplication,
  QLabel,
  QLineEdit,
  QVBoxLayout,
  QWidget,
)
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setWindowTitle("Signal and Slot")
    self.resize(300, 100)
    self.line_edit = QLineEdit(parent=self)
    self.label = QLabel(parent=self)
    self.line_edit.textEdited.connect(self.update_label)
    layout = QVBoxLayout()
    layout.addWidget(self.line_edit)
    layout.addWidget(self.label)
    self.setLayout(layout)
  def update_label(self):
    self.label.setText(self.line_edit.text())
app = QApplication([])
window = Window()
window.show()
app.exec()

```

In this example, we connect the line edit's `textEdited` signal with the `update_label()` method, which sets the label's text to match the text we enter in our line edit. Go ahead and run the app. Then, enter some text in the line edit and see what happens with the label at the bottom of the app's window.
## Validating Input in Line Edits
We can provide input validators to our line edits using the [`setValidator()`](https://doc.qt.io/qt-6/qlineedit.html#setValidator) method. This method takes a `QValidator` object as an argument. PyQt has a few built-in validators that you can use directly on a line edit:
  * [QIntValidator](https://doc.qt.io/qt-6/qintvalidator.html) for integer validation
  * [QDoubleValidator](https://doc.qt.io/qt-6/qdoublevalidator.html) for floating-point validation
  * [QRegularExpressionValidator](https://doc.qt.io/qt-6/qregularexpressionvalidator.html) for validation based on regular expressions


Validator objects process the input to check whether it's valid. In general, validator object has three possible states:
Constant | Value | Description  
---|---|---  
`QValidator.State.Invalid` | `0` | The input is invalid.  
`QValidator.State.Intermediate` | `1` | The input is a valid intermediate value.  
`QValidator.State.Acceptable` | `2` | The input is acceptable as a final result.  
When you set a validator to a given line edit, the user may change the content to any [`Intermediate`](https://doc.qt.io/qt-6/qvalidator.html#State-enum) value during editing. However, they can't edit the text to a value that is [`Invalid`](https://doc.qt.io/qt-6/qvalidator.html#State-enum). The line edit will emit the `returnPressed` and `editingFinished` signals only when the validator validates input as [`Acceptable`](https://doc.qt.io/qt-6/qvalidator.html#State-enum).
Here's an example where we use a `QIntValidator` and a `QRegularExpressionValidator`
python ```
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QIntValidator, QRegularExpressionValidator
from PyQt6.QtWidgets import (
  QApplication,
  QFormLayout,
  QLabel,
  QLineEdit,
  QWidget,
)
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setWindowTitle("Input Validators")
    self.resize(300, 100)
    self.int_line_edit = QLineEdit(parent=self)
    self.int_line_edit.setValidator(QIntValidator())
    self.uppercase_line_edit = QLineEdit(parent=self)
    input_validator = QRegularExpressionValidator(
      QRegularExpression("[A-Z]+"), self.uppercase_line_edit
    )
    self.uppercase_line_edit.setValidator(input_validator)
    self.uppercase_line_edit.returnPressed.connect(self.update_label)
    self.signal_label = QLabel(parent=self)
    layout = QFormLayout()
    layout.addRow("Integers:", self.int_line_edit)
    layout.addRow("Uppercase letters:", self.uppercase_line_edit)
    layout.addRow("Signal:", self.signal_label)
    self.setLayout(layout)
  def update_label(self):
    self.signal_label.setText("Return pressed!")
if __name__ == "__main__":
  app = QApplication([])
  window = Window()
  window.show()
  app.exec()

```

In this example, we have two line edits. In the first line edit, we've used a `QIntValidator` object. This way, the line edit will only accept valid integer numbers. If you try to type in something different, then the line edit won't accept your input.
In the second line edit, we've used a `QRegularExpressionValidator`. In this specific case, the regular expression accepts one or more uppercase letters. Again if you try to enter something else, then the line edit won't accept the input.
The `QLabel` will show the text `Return pressed!` if the input in the second line edit is valid and you press the Enter key. Here's what the app looks like:
![QLineEdit with input validator](https://www.pythonguis.com/static/docs/qlineedit/qlineedit-input-validators.png) _QLineEdit with input validator._
Validators provide a quick way to restrict the user input and set our own validation rules. This way, we can ensure valid user input in our applications.
## Conclusion
Line edits are pretty useful widgets in any GUI application. They allow text input through a single-line editor that has many cool features.
In this tutorial, you've learned how to create, use, and customize your line edits while building a GUI application with PyQt/PySide.
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Leo Well](https://www.pythonguis.com/static/theme/images/authors/leo-well.jpg)](https://www.pythonguis.com/authors/leo-well/)
**QLineEdit** was written by [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
**QLineEdit** was published in [docs](https://www.pythonguis.com/docs/) on February 05, 2024 (updated January 12, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [widgets](https://www.pythonguis.com/topics/widgets/) [qlineedit](https://www.pythonguis.com/topics/qlineedit/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
