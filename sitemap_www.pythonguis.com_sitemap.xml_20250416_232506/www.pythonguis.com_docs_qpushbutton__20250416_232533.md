# Content from: https://www.pythonguis.com/docs/qpushbutton/

[](https://www.pythonguis.com/docs/qpushbutton/#menu)
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
# QPushButton
Add clickable buttons to your Python UI
by [Leo Well](https://www.pythonguis.com/authors/leo-well/) Last updated Oct 22 [ Documentation ](https://www.pythonguis.com/docs/)
The push button, or command button, is perhaps the most commonly used widget in any graphical user interface (GUI). A button is a rectangular widget that typically displays a text describing its aim.
When we click a button, we command the computer to perform actions or to answer a question. Typical buttons include _Ok_ , _Apply_ , _Cancel_ , _Close_ , _Yes_ , _No_ and _Help_. However, they're not restricted to this list.
In this tutorial, you'll learn how to create and customize button widgets in your GUI applications.
## Creating Buttons Widgets With `QPushButton`
Buttons are probably the most common widgets in GUI applications. They come in handy when you need to create [dialogs](https://www.pythonguis.com/tutorials/pyqt6-dialogs/) for communicating with your users. You'll probably be familiar with _Accept_ , _Ok_ , _Canel_ , _Yes_ , _No_ , and _Apply_ buttons, which are commonplace in modern graphical user interfaces.
In general, buttons allow you to trigger actions in response to the user's clicks on the button's area. Buttons often have a rectangular shape and include a text label that describes their intended action or command.
If you've used [PyQt](https://www.pythonguis.com/pyqt6/) or [PySide](https://www.pythonguis.com/pyside6/) to create GUI applications in Python, then it'd be pretty likely that you already know about the [`QPushButton`](https://doc.qt.io/qt-6/qpushbutton.html) class. This class allows you to create buttons in your graphical interfaces quickly.
The `QPushButton` class provides three different constructors that you can use to create buttons according to your needs: 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Constructor | Description  
---|---  
[`QPushButton(parent: QWidget = None)`](https://doc.qt.io/qt-6/qpushbutton.html#QPushButton) | Constructs a button with a parent widget but without text or icon  
[`QPushButton(text: str, parent: QWidget = None)`](https://doc.qt.io/qt-6/qpushbutton.html#QPushButton-1) | Constructs a button with a parent widget and the description text but without an icon  
[`QPushButton(icon: QIcon, text: str, parent: QWidget = None)`](https://doc.qt.io/qt-6/qpushbutton.html#QPushButton-2) | Constructs a button with an icon, text, and parent widget  
To illustrate how to use the above constructors, you can code the following example:
  * PyQt6
  * PySide6


python ```
import sys
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    # Button with a parent widget
    topBtn = QPushButton(parent=self)
    topBtn.setFixedSize(100, 60)
    # Button with a text and parent widget
    centerBtn = QPushButton(text="Center", parent=self)
    centerBtn.setFixedSize(100, 60)
    # Button with an icon, a text, and a parent widget
    bottomBtn = QPushButton(
      icon=QIcon("./icons/logo.svg"),
      text="Bottom",
      parent=self
    )
    bottomBtn.setFixedSize(100, 60)
    bottomBtn.setIconSize(QSize(40, 40))
    layout = QVBoxLayout()
    layout.addWidget(topBtn)
    layout.addWidget(centerBtn)
    layout.addWidget(bottomBtn)
    self.setLayout(layout)
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

python ```
import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    # Button with a parent widget
    topBtn = QPushButton(parent=self)
    topBtn.setFixedSize(100, 60)
    # Button with a text and parent widget
    centerBtn = QPushButton(text="Center", parent=self)
    centerBtn.setFixedSize(100, 60)
    # Button with an icon, a text, and a parent widget
    bottomBtn = QPushButton(
      icon=QIcon("./icons/logo.svg"),
      text="Bottom",
      parent=self
    )
    bottomBtn.setFixedSize(100, 60)
    bottomBtn.setIconSize(QSize(40, 40))
    layout = QVBoxLayout()
    layout.addWidget(topBtn)
    layout.addWidget(centerBtn)
    layout.addWidget(bottomBtn)
    self.setLayout(layout)
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

You can [download the logo here](https://www.pythonguis.com/static/theme/images/logo.svg) or use your own image file. You can also use PNG format images if you prefer.
This code does a lot! First, we do the required imports. Inside our `Window` class, we create three `QPushButton` instances. To create the first button, we use the first constructor of `QPushButton`. That's why we only pass a `parent` widget.
For the second button, we use the second constructor of `QPushButton`. This time, we provide the button's text and parent. Note that the text is a regular Python string.
Our last button uses the third constructor. In this case, we need to provide the button's icon, text, and parent. We use the [`QIcon`](https://doc.qt.io/qt-6/qicon.html) class with an SVG image as an argument to provide the icon. Note that we can also use a `QPixmap` object as the button's icon.
Save this code to a `.py` file and run it. You'll get a window that looks something like this:
![QPushButton constructors example, showing three buttons with labels & icon](https://www.pythonguis.com/static/docs/qpushbutton/S1fDPLeXi.png) _QPushButton constructors example, showing three buttons with labels & icon_
The first button has no text. It's just a rectangular shape on the app's windows. The second button in the center has text only, while the third button at the bottom of the window has an icon and text. That looks great!
These buttons don't do any action jet. If you click them, then you'll realize that nothing happens. To make your buttons perform concrete actions, you need to connect their signals to some useful slots. You'll learn how to do this in the next section.
## Connecting Signals and Slots
Depending on specific user events, the `QPushButton` class can emit four different signals. Here's is a summary of these signals and their corresponding meaning:
Signal | Emitted  
---|---  
[`clicked(checked=false)`](https://doc.qt.io/qt-6/qabstractbutton.html#clicked) | When the user clicks the button and activates it.  
[`pressed()`](https://doc.qt.io/qt-6/qabstractbutton.html#pressed) | When the user presses the button down.  
[`released()`](https://doc.qt.io/qt-6/qabstractbutton.html#released) | When the user releases the button.  
[`toggled(checked=false)`](https://doc.qt.io/qt-6/qabstractbutton.html#toggled) | Whenever a checkable button changes its state from checked to unchecked and vice versa.  
When you're creating a GUI application, and you need to use buttons, then you need to think of the appropriate signal to use. Most of the time, you'll use the button's `clicked()` signal since clicking a button is the most common user event you'll ever need to process.
The other part of the signal and slot equation is the slot itself. A slot is a method or function that performs a concrete action in your application. Now, how can you connect a signal to a slot so that the slot gets called when the signal gets emitted? Here's the required syntax to do this:
python ```
button.<signal>.connect(<method>)

```

In this construct, `button` is the `QPushButton` object we need to connect with a given slot. The `<signal>` placeholder can be any of the four abovementioned signals. Finally, `<method>` represents the target slot or method.
Let's write an example that puts this syntax into action. For this example, we'll connect the `clicked` signal with a method that counts the clicks on a button:
  * PyQt6
  * PySide6


python ```
import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.count = 0
    self.button = QPushButton(f"Click Count: {self.count}", self)
    self.button.setFixedSize(120, 60)
    self.button.clicked.connect(self.count_clicks)
    layout = QVBoxLayout()
    layout.addWidget(self.button)
    self.setLayout(layout)
  def count_clicks(self):
    self.count += 1
    self.button.setText(f"Click Count: {self.count}")
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

python ```
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.count = 0
    self.button = QPushButton(f"Click Count: {self.count}", self)
    self.button.setFixedSize(120, 60)
    self.button.clicked.connect(self.count_clicks)
    layout = QVBoxLayout()
    layout.addWidget(self.button)
    self.setLayout(layout)
  def count_clicks(self):
    self.count += 1
    self.button.setText(f"Click Count: {self.count}")
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

The `button` variable holds an instance of `QPushButton`. To create this button, we use a text and parent widget. This parent widget works as our current window. Then we connect the button's `clicked` signal with the `count_clicks()` method.
The `count_clicks()` method counts the number of clicks on the button and updates the button's text accordingly. Go ahead and run the app!
## Exploring the Public API of `QPushButton`
Up to this point, you've learned about the different ways to create buttons in your GUI applications. You've also learned how to make your buttons perform actions in response to the user's actions by connecting the buttons' signals with concrete methods known as slots.
In the following sections, you'll learn about the `QPushButton` class's public API and its most useful properties, including the following:
Property | Description | Getter Method | Setter Method  
---|---|---|---  
[`text`](https://doc.qt.io/qt-6/qabstractbutton.html#text-prop) | Holds the text shown on the button | `text()` | `setText()`  
[`icon`](https://doc.qt.io/qt-6/qabstractbutton.html#icon-prop) | Holds the icon shown on the button | `icon()` | `setIcon()`  
[`shortcut`](https://doc.qt.io/qt-6/qabstractbutton.html#shortcut-prop) | Holds the keyboard shortcut associated with the button | `shortcut()` | `setShortcut()`  
Let's kick things off by learning how to set and get a button's text, icon, and keyboard shortcut. These actions can be an essential part of your GUI design process.
### Setting a Button's Text, Icon, and Shortcut
In previous sections, you've learned how to create buttons using different class constructors. Some of these constructors allow you to set the button's text directly. However, sometimes you need to manipulate a button's text at runtime. To accomplish this, you can use `setText()` and `text()`.
As its name suggests, the `setText()` method allows you to set the text of a given button. On the other hand, the `text()` lets you retrieve the current text of a button. Here's a toy example of how to use these methods:
  * PyQt6
  * PySide6


python ```
import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.button = QPushButton("Hello!")
    self.button.setFixedSize(120, 60)
    self.button.clicked.connect(self.onClick)
    layout = QVBoxLayout()
    layout.addWidget(self.button)
    self.setLayout(layout)
  def onClick(self):
    text = self.button.text()
    if text == "Hello!":
      self.button.setText(text[:-1] + ", World!")
    else:
      self.button.setText("Hello!")
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

python ```
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.button = QPushButton("Hello!")
    self.button.setFixedSize(120, 60)
    self.button.clicked.connect(self.onClick)
    layout = QVBoxLayout()
    layout.addWidget(self.button)
    self.setLayout(layout)
  def onClick(self):
    text = self.button.text()
    if text == "Hello!":
      self.button.setText(text[:-1] + ", World!")
    else:
      self.button.setText("Hello!")
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

In this example, we use `text()` and `setText()` inside the `onClick()` method to manipulate the text of our button object. These methods come in handy when we need to set and retrieve a button's text at run time, which would be useful in a few situations. For example, if we need a button to fold and unfold a tree of widgets or other objects.
Go ahead and run the app! You'll get a window like the following:
![Window with a single button, with the text Hello! Click to change the text.](https://www.pythonguis.com/static/docs/qpushbutton/B1fDPIg7i.png) _Window with a single button, with the text Hello! Click to change the text._
In this example, when you click the button, its text alternate between `Hello!` and `Hello, World!`.
`QPushButton` also has methods to manipulate the icon of a given button. In this case, the methods are `setIcon()` and `icon()`. You can set the button's icon at run time with the first method. The second method allows you to retrieve the icon of a given button. There's also a third method related to icons. It's called `.setIconSize()` and allows you to manipulate the icon size.
Here's an example that illustrates how to use these methods:
  * PyQt6
  * PySide6


python ```
import sys
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.btnOne = QPushButton(
      icon=QIcon("./icons/logo.svg"), text="Click me!", parent=self
    )
    self.btnOne.setFixedSize(100, 60)
    self.btnOne.clicked.connect(self.onClick)
    self.btnTwo = QPushButton(parent=self)
    self.btnTwo.setFixedSize(100, 60)
    self.btnTwo.setEnabled(False)
    self.btnTwo.clicked.connect(self.onClick)
    layout = QVBoxLayout()
    layout.addWidget(self.btnOne)
    layout.addWidget(self.btnTwo)
    self.setLayout(layout)
  def onClick(self):
    sender = self.sender()
    icon = sender.icon()
    if sender is self.btnOne:
      sender.setText("")
      sender.setIcon(QIcon())
      sender.setEnabled(False)
      self.btnTwo.setEnabled(True)
      self.btnTwo.setText("Click me!")
      self.btnTwo.setIcon(icon)
      self.btnTwo.setIconSize(QSize(20, 20))
    elif sender is self.btnTwo:
      sender.setText("")
      sender.setIcon(QIcon())
      sender.setEnabled(False)
      self.btnOne.setEnabled(True)
      self.btnOne.setText("Click me!")
      self.btnOne.setIcon(icon)
      self.btnOne.setIconSize(QSize(30, 30))
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

python ```
import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.btnOne = QPushButton(
      icon=QIcon("./icons/logo.svg"), text="Click me!", parent=self
    )
    self.btnOne.setFixedSize(100, 60)
    self.btnOne.clicked.connect(self.onClick)
    self.btnTwo = QPushButton(parent=self)
    self.btnTwo.setFixedSize(100, 60)
    self.btnTwo.setEnabled(False)
    self.btnTwo.clicked.connect(self.onClick)
    layout = QVBoxLayout()
    layout.addWidget(self.btnOne)
    layout.addWidget(self.btnTwo)
    self.setLayout(layout)
  def onClick(self):
    sender = self.sender()
    icon = sender.icon()
    if sender is self.btnOne:
      sender.setText("")
      sender.setIcon(QIcon())
      sender.setEnabled(False)
      self.btnTwo.setEnabled(True)
      self.btnTwo.setText("Click me!")
      self.btnTwo.setIcon(icon)
      self.btnTwo.setIconSize(QSize(20, 20))
    elif sender is self.btnTwo:
      sender.setText("")
      sender.setIcon(QIcon())
      sender.setEnabled(False)
      self.btnOne.setEnabled(True)
      self.btnOne.setText("Click me!")
      self.btnOne.setIcon(icon)
      self.btnOne.setIconSize(QSize(30, 30))
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

In this example, we create an app with two buttons. Both buttons are connected to the `onClick()` method. Inside the method, we first get the clicked button using the `sender()` method on our app's window, `self`.
Next, we get a reference to the sender button's icon using the `icon()` method. The `if` statement checks if the clicked object was `btnOne`. If that's the case, then we reset the icon with `setIcon()` and disable the button with `setEnabled()`. The following four lines enable the `btnTwo` button, set its text to `"Click me!"`, change the button's icon, and resize the icon. The `elif` clause does something similar, but this time the target button is `btnOne`. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
If you run this application, then you'll get a window like this:
![Window with two buttons, the top with a icon & label, the bottom empty. Click to toggle which button has the label & icon._](https://www.pythonguis.com/static/docs/qpushbutton/HJ-vwIlQj.png) _Window with two buttons, the top with a icon & label, the bottom empty. Click to toggle which button has the label & icon._
When we click the top button, the bottom button's text and icon will be set to `Click me!` and to the PythonGUIs.com logo, respectively. At the same time, the top button's text and icon will disappear. Note that the logo's size will change as well.
Another useful feature of buttons is that you can assign them a keyboard shortcut for those users that prefer the keyboard over the mouse. These methods are `.setShortcut()` and `.shortcut()`. Again, you can use the first method to set a shortcut and the second method to get the shortcut assigned to the underlying button.
These methods are commonly helpful in situations where we have a button that doesn't have any text. Therefore we can't assign it an automatic shortcut using the ampersand character `&`.
### Checking the Status of a Button
Sometimes you'd need to check the status of a given button and take action accordingly. The `QPushButton` class provides a few methods that can help you check different properties related to the current status of your buttons:
Property | Description | Access Method | Setter Method  
---|---|---|---  
[`down`](https://doc.qt.io/qt-6/qabstractbutton.html#down-prop) | Indicates whether the button is _pressed_ down or not | `isDown()` | `setDown()`  
[`checked`](https://doc.qt.io/qt-6/qabstractbutton.html#checked-prop) | Indicates whether the button is _checked_ or not | `isChecked()` | `setChecked()`  
[`enabled`](https://doc.qt.io/qt-6/qwidget.html#enabled-prop) | Indicates whether the button is _enabled_ or not | `isEnabled()` | `setEnabled()`  
The _down_ status is typically transitory and naturally happens between the _pressed_ and _released_ statuses. However, we can use the `setDown()` method to manipulate the _down_ status at runtime.
The _checked_ status is only available when we use checkable buttons. Only checkable buttons can be at either the _checked_ or _unchecked_ status.
Finally, when we enable or disable a given button, we allow or disallow the user's click on the button. In other words, _disabled_ buttons don't respond to the user's clicks or other events, while _enabled_ buttons do respond.
Here's an example that shows how these three sets of statuses work:
  * PyQt6
  * PySide6


python ```
import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.btnOne = QPushButton(text="I'm Down!", parent=self)
    self.btnOne.setFixedSize(150, 60)
    self.btnOne.setDown(True)
    self.btnOne.clicked.connect(self.onBtnOneClicked)
    self.btnTwo = QPushButton(text="I'm Disabled!", parent=self)
    self.btnTwo.setFixedSize(150, 60)
    self.btnTwo.setEnabled(False)
    self.btnThree = QPushButton(text="I'm Checked!", parent=self)
    self.btnThree.setFixedSize(150, 60)
    self.btnThree.setCheckable(True)
    self.btnThree.setChecked(True)
    self.btnThree.clicked.connect(self.onBtnThreeClicked)
    layout = QVBoxLayout()
    layout.addWidget(self.btnOne)
    layout.addWidget(self.btnTwo)
    layout.addWidget(self.btnThree)
    self.setLayout(layout)
  def onBtnOneClicked(self):
    if not self.btnOne.isDown():
      self.btnOne.setText("I'm Up!")
      self.btnOne.setDown(False)
  def onBtnThreeClicked(self):
    if self.btnThree.isChecked():
      self.btnThree.setText("I'm Checked!")
    else:
      self.btnThree.setText("I'm Unchecked!")
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

python ```
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.btnOne = QPushButton(text="I'm Down!", parent=self)
    self.btnOne.setFixedSize(150, 60)
    self.btnOne.setDown(True)
    self.btnOne.clicked.connect(self.onBtnOneClicked)
    self.btnTwo = QPushButton(text="I'm Disabled!", parent=self)
    self.btnTwo.setFixedSize(150, 60)
    self.btnTwo.setEnabled(False)
    self.btnThree = QPushButton(text="I'm Checked!", parent=self)
    self.btnThree.setFixedSize(150, 60)
    self.btnThree.setCheckable(True)
    self.btnThree.setChecked(True)
    self.btnThree.clicked.connect(self.onBtnThreeClicked)
    layout = QVBoxLayout()
    layout.addWidget(self.btnOne)
    layout.addWidget(self.btnTwo)
    layout.addWidget(self.btnThree)
    self.setLayout(layout)
  def onBtnOneClicked(self):
    if not self.btnOne.isDown():
      self.btnOne.setText("I'm Up!")
      self.btnOne.setDown(False)
  def onBtnThreeClicked(self):
    if self.btnThree.isChecked():
      self.btnThree.setText("I'm Checked!")
    else:
      self.btnThree.setText("I'm Unchecked!")
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

In this example, we first set `btnOne` _down_ using the `setDown()` method. Then we disable `btnTwo` using the `setEnabled()` with `False` as an argument. This will make this button unresponsive to user events. Finally, we set `btnThree` as checkable with `setCheckable()`. Being checkable means that we can use the _checked_ and _unchecked_ statuses in our code.
The `onBtnOneClicked()` method is connected to `btnOne`. This method checks if the button is not down and changes the button text accordingly.
The `onBtnThreeClicked()` is connected to `btnThree`. This method alternatively changes the button's text depending on its _checked_ status.
If you run this app, you'll get the following window:
![Window with 3 buttons: one starting in the down state, one disabled and one checked & toggleable.](https://www.pythonguis.com/static/docs/qpushbutton/rJGvD8gQs.png) _Window with 3 buttons: one starting in the down state, one disabled and one checked & toggleable._
First, note that these three buttons have different tones of gray. These different tones of gray indicate three different states. The first button is _down_ , the second button is _disabled_ , and the third button is _checked_.
If you click the first button, then it'll be released, and its text will be set to `I'm Up!`. The second button won't respond to your clicks or actions. The third button will alternate its status between _unchecked_ and _checked_.
### Exploring Other Properties of Button Objects
`QPushButton` has several other useful properties we can use in our GUI applications. Some of these properties with their corresponding setter and getter method include:
Property | Description | Access Method | Setter Method  
---|---|---|---  
[`default`](https://doc.qt.io/qt-6/qpushbutton.html#default-prop) | Indicates whether the button is the default button on the containing window or not | `isDefault()` | `setDefault()`  
[`flat`](https://doc.qt.io/qt-6/qpushbutton.html#flat-prop) | Indicates whether the button border is raised or not | `isFlat()` | `setFlat()`  
The `default` property comes in handy when you have several buttons on a window, and you need to set one of these buttons as the default window's action. For example, say we have a dialog with the _Ok_ and _Cancel_ buttons. In this case, the _Ok_ button can be your default action.
The `flat` property is closely related to the look and feel of your app's GUI. If we set `flat` to `True`, then the button's border won't be visible.
## Associating a Popup Menu to a Button
`QPushButton` objects can also display a menu when you click them. To set up this menu, you must have a proper popup menu beforehand. Then you can use the [`setMenu()`](https://doc.qt.io/qt-6/qpushbutton.html#setMenu) method to associate the menu with the button.
Here's an example that creates a button with an attached popup menu:
  * PyQt6
  * PySide6


python ```
import sys
from PyQt6.QtWidgets import (
  QApplication,
  QMenu,
  QPushButton,
  QVBoxLayout,
  QWidget,
)
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.btnOne = QPushButton(text="Menu!", parent=self)
    self.menu = QMenu(self)
    self.menu.addAction("First Item")
    self.menu.addAction("Second Item")
    self.menu.addAction("Third Item")
    self.btnOne.setMenu(self.menu)
    layout = QVBoxLayout()
    layout.addWidget(self.btnOne)
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
  QMenu,
  QPushButton,
  QVBoxLayout,
  QWidget,
)
class Window(QWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.btnOne = QPushButton(text="Menu!", parent=self)
    self.menu = QMenu(self)
    self.menu.addAction("First Item")
    self.menu.addAction("Second Item")
    self.menu.addAction("Third Item")
    self.btnOne.setMenu(self.menu)
    layout = QVBoxLayout()
    layout.addWidget(self.btnOne)
    self.setLayout(layout)
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec())

```

In this example, we create a button with an associated popup menu. To attach the menu to the target button, we use `setMenu()`, which turns the button into a menu button.
If you run this application, then you'll get a window that will look something like this:
![Window with a single button, with attached drop-down menu.](https://www.pythonguis.com/static/docs/qpushbutton/HJMDwUgQs.png) _Window with a single button, with attached drop-down menu._
In some window styles, the button will show a small triangle on the right end of the button. If we click the button, then the pop-up menu will appear, allowing us to select any available menu option.
## Conclusion
Push buttons are pretty useful widgets in any GUI application. Buttons can respond to the user's events and perform actions in our applications.
In this tutorial, you've learned how to create, use, and customize your button while building a GUI application.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Leo Well](https://www.pythonguis.com/static/theme/images/authors/leo-well.jpg)](https://www.pythonguis.com/authors/leo-well/)
**QPushButton** was written by [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
**QPushButton** was published in [docs](https://www.pythonguis.com/docs/) on November 24, 2022 (updated October 22, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [widgets](https://www.pythonguis.com/topics/widgets/) [qcombobox](https://www.pythonguis.com/topics/qcombobox/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
