# Content from: https://www.pythonguis.com/tutorials/custom-title-bar-pyqt5/

[](https://www.pythonguis.com/tutorials/custom-title-bar-pyqt5/#menu)
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
# How to Create a Custom Title Bar for a PyQt5 Window
Customize Your Python App's Title Bars
by [Leo Well](https://www.pythonguis.com/authors/leo-well/) Last updated Oct 18 PyQt5 [ Tutorials ](https://www.pythonguis.com/tutorials/)
[ Source and image files ](https://downloads.pythonguis.com/custom-title-bar-pyqt5.zip)
This tutorial is also available for [PyQt6](https://www.pythonguis.com/tutorials/custom-title-bar-pyqt6/)
PyQt provides plenty of tools for creating unique and visually appealing graphical user interfaces (GUIs). One aspect of your applications that you may not have considered customizing is the **title bar**. The _title bar_ is the topmost part of the window, where your users find the app's name, window controls & other elements.
This part of the window is usually drawn by the operating system or desktop environment and it's default look & feel may not gel well with the rest of your application. However, you may want to customize it to add additional functionality. For example, in web browsers the document tabs are now typically collapsed into the title bar to maximize available space for viewing pages.
In this tutorial, you will learn how to create custom title bars in PyQt. By the end of this tutorial, you will have the necessary knowledge to enhance your PyQt applications with personalized and (hopefully!) stylish title bars.
Table of Contents
  * [Creating Frameless Windows in PyQt](https://www.pythonguis.com/tutorials/custom-title-bar-pyqt5/#creating-frameless-windows-in-pyqt)
  * [Setting Up the Main Window](https://www.pythonguis.com/tutorials/custom-title-bar-pyqt5/#setting-up-the-main-window)
  * [Creating a Custom Title Bar for a PyQt Window](https://www.pythonguis.com/tutorials/custom-title-bar-pyqt5/#creating-a-custom-title-bar-for-a-pyqt-window)
  * [Updating the Window's State](https://www.pythonguis.com/tutorials/custom-title-bar-pyqt5/#updating-the-windows-state)
  * [Handling Window's Moves](https://www.pythonguis.com/tutorials/custom-title-bar-pyqt5/#handling-windows-moves)
  * [Making the Title Bar Look More Beautiful](https://www.pythonguis.com/tutorials/custom-title-bar-pyqt5/#making-the-title-bar-look-more-beautiful)
  * [Conclusion](https://www.pythonguis.com/tutorials/custom-title-bar-pyqt5/#conclusion)


## Creating Frameless Windows in PyQt
The first step to providing a PyQt application with a custom **title bar** is to remove the default title bar and window decoration provided by the operating system. If we don't take this step, we'll end up with multiple title bars at the top of our windows.
In PyQt, we can create a frameless window using the [`setWindowFlags()`](https://doc.qt.io/qt-6/qwidget.html#windowFlags-prop) method available on all [`QWidget`](https://doc.qt.io/qt-6/qwidget.html) subclasses, including [`QMainWindow`](https://doc.qt.io/qt-6/qmainwindow.html). We call this method, passing in the `FramelessWindowHint` flag, which lives in the `Qt` namespace under the `WindowType` enumeration.
Here's the code of a minimal PyQt app whose main window is frameless:
python ```
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Custom Title Bar")
    self.resize(400, 200)
    self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
if __name__ == "__main__":
  app = QApplication([])
  window = MainWindow()
  window.show()
  app.exec()

```

After importing the required classes, we create a window by subclassing `QMainWindow`. In the class initializer method, we set the window's title and resize the window using the `resize()` method. Then we use the `setWindowFlags()` to make the window frameless. The rest is the usual boilerplate code for creating PyQt applications.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt5](https://www.pythonguis.com/static/theme/images/products/pyqt5-book.png)](https://www.pythonguis.com/pyqt5-book/)
[Take a look ](https://www.pythonguis.com/pyqt5-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/create-simple-gui-applications/) and [Amazon Paperback](https://www.amazon.com/dp/B08RB2HRS1/)
If you run this app from your command line, you'll get the following window on your screen:
![A frameless window in PyQt](https://www.pythonguis.com/static/tutorials/qt/custom-title-bar/frameless-window-pyqt.png) _A frameless window in PyQt_
As you can see, the app's main window doesn't have a title bar or any other decoration. It's only a gray rectangle on your screen.
Because the window has no buttons, you need to press _Alt-F4_ on Windows and Linux or _Cmd+Q_ on macOS to close the app.
This isn't very helpful, of course, but we'll be adding back in our custom title bar shortly.
## Setting Up the Main Window
Before creating our custom title bar, we'll finish the initialization of our app's main window, import some additional classes and create the window's central widget and layouts.
Here's the code update:
python ```
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QVBoxLayout,
  QWidget,
)
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Custom Title Bar")
    self.resize(400, 200)
    self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    central_widget = QWidget()
    self.title_bar = CustomTitleBar(self)
    work_space_layout = QVBoxLayout()
    work_space_layout.setContentsMargins(11, 11, 11, 11)
    work_space_layout.addWidget(QLabel("Hello, World!", self))
    centra_widget_layout = QVBoxLayout()
    centra_widget_layout.setContentsMargins(0, 0, 0, 0)
    centra_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
    centra_widget_layout.addWidget(self.title_bar)
    centra_widget_layout.addLayout(work_space_layout)
    central_widget.setLayout(centra_widget_layout)
    self.setCentralWidget(central_widget)
# ...

```

First, we import the `QLabel`, `QVBoxLayout`, and `QWidget` classes. In our window's initializer, we create a central widget by instantiating `QWidget()`. Next, we create an instance attribute called `title_bar` by instantiating a class called `CustomTitleBar`. We still need to implement this class -- we'll do this in a moment.
The next step is to create a layout for our window's workspace. In this example, we're using a `QVBoxLayout,` but you can use the layout that better fits your needs. We also set some margins for the layout content and added a label containing the phrase `"Hello, World!"`.
Next, we create a global layout for our central widget. Again, we use a `QVBoxLayout`. We set the layout's margins to `0` and aligned it on the top of our frameless window. In this layout, we need to add the title bar at the top and the workspace at the bottom. Finally, we set the central widget's layout and the app's central widget.
That's it! We have all the boilerplate code we need for our window to work correctly. Now we're ready to write our custom title bar.
## Creating a Custom Title Bar for a PyQt Window
In this section, we will create a custom title bar for our main window. To do this, we will create a new class by inheriting from `QWidget`. First, go ahead and update your imports like in the code below:
python ```
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import (
  QApplication,
  QHBoxLayout,
  QLabel,
  QMainWindow,
  QStyle,
  QToolButton,
  QVBoxLayout,
  QWidget,
)
# ...

```

Here, we've imported a few new classes. We will use these classes as building blocks for our title bar. Without further ado, let's get into the title bar code. We'll introduce the code in small consecutive chunks to facilitate the explanation. Here's the first piece:
python ```
# ...
class CustomTitleBar(QWidget):
  def __init__(self, parent):
    super().__init__(parent)
    self.setAutoFillBackground(True)
    self.setBackgroundRole(QPalette.ColorRole.Highlight)
    self.initial_pos = None
    title_bar_layout = QHBoxLayout(self)
    title_bar_layout.setContentsMargins(1, 1, 1, 1)
    title_bar_layout.setSpacing(2)

```

In this code snippet, we create a new class by inheriting from `QWidget`. This way, our title bar will have all the standard features and functionalities of any PyQt widgets. In the class initializer, we set `autoFillBackground` to true because we want to give a custom color to the bar. The next line of code sets the title bar's background color to `QPalette.ColorRole.Highlight`, which is a blueish color.
The next line of code creates and initializes an instance attribute called `initial_pos`. We'll use this attribute later on when we deal with moving the window around our screen.
The final three lines of code allow us to create a layout for our title bar. Because the title bar should be horizontally oriented, we use a `QHBoxLayout` class to structure it.
The piece of code below deals with our window's title:
python ```
# ...
class CustomTitleBar(QWidget):
  def __init__(self, parent):
    # ...
    self.title = QLabel(f"{self.__class__.__name__}", self)
    self.title.setStyleSheet(
      """font-weight: bold;
        border: 2px solid black;
        border-radius: 12px;
        margin: 2px;
      """
    )
    self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    if title := parent.windowTitle():
      self.title.setText(title)
    title_bar_layout.addWidget(self.title)

```

The first line of new code creates a `title` attribute. It's a `QLable` object that will hold the window's title. Because we want to build a cool title bar, we'd like to add some custom styling to the title. To do this, we use the `setStyleSheet()` method with a string representing a CSS style sheet as an argument. The style sheet tweaks the font, borders, and margins of our title label.
Next, we center the title using the `setAlignment()` method with the `Qt.AlignmentFlag.AlignCenter` flag as an argument.
In the conditional statement, we check whether our window has a title. If that's the case, we set the text of our `title` label to the current window's title. Finally, we added the `title` label to the title bar layout.
The next step in our journey to build a custom title bar is to provide standard window controls. In other words, we need to add the _minimize_ , _maximize_ , _close_ , and _normal_ buttons. These buttons will allow our users to interact with our window. To create the buttons, we'll use the `QToolButton` class.
Here's the required code:
python ```
# ...
class CustomTitleBar(QWidget):
  def __init__(self, parent):
    # ...
    # Min button
    self.min_button = QToolButton(self)
    min_icon = self.style().standardIcon(
      QStyle.StandardPixmap.SP_TitleBarMinButton
    )
    self.min_button.setIcon(min_icon)
    self.min_button.clicked.connect(self.window().showMinimized)
    # Max button
    self.max_button = QToolButton(self)
    max_icon = self.style().standardIcon(
      QStyle.StandardPixmap.SP_TitleBarMaxButton
    )
    self.max_button.setIcon(max_icon)
    self.max_button.clicked.connect(self.window().showMaximized)
    # Close button
    self.close_button = QToolButton(self)
    close_icon = self.style().standardIcon(
      QStyle.StandardPixmap.SP_TitleBarCloseButton
    )
    self.close_button.setIcon(close_icon)
    self.close_button.clicked.connect(self.window().close)
    # Normal button
    self.normal_button = QToolButton(self)
    normal_icon = self.style().standardIcon(
      QStyle.StandardPixmap.SP_TitleBarNormalButton
    )
    self.normal_button.setIcon(normal_icon)
    self.normal_button.clicked.connect(self.window().showNormal)
    self.normal_button.setVisible(False)

```

In this code snippet, we define all the required buttons by instantiating the `QToolButton` class. The _minimize_ , _maximize_ , and _close_ buttons follow the same pattern. We create the button, define an icon for the buttons at hand, and set the icon using the `setIcon()` method.
Note that we use the standard icons that PyQt provides. For example, the _minimize_ button uses the `SP_TitleBarMinButton` icon. Similarly, the _maximize_ and _close_ buttons use the `SP_TitleBarMaxButton` and `SP_TitleBarCloseButton` icons. We find all these icons in the `QStyle.StandardPixmap` namespace.
Finally, we connect the button's `clicked()` signal with the appropriate slot. For the minimize buttons, the proper slot is `.showMinimized()`. For the maximize and close buttons, the right slots are `.showMaximized()` and `close()`, respectively. All these slots are part of the main window's class.
The _normal_ button at the end of the above code uses the `SP_TitleBarNormalButton` icon and `showNormal()` slot. This button has an extra setting. We've set its visibility to `False`, meaning that the button will be hidden by default. It'll only appear when we maximize the window to allow us to return to the normal state.
Now that we've created and tweaked the buttons, we must add them to our title bar. To do this, we can use the following `for` loop:
python ```
# ...
class CustomTitleBar(QWidget):
  def __init__(self, parent):
    # ...
    buttons = [
      self.min_button,
      self.normal_button,
      self.max_button,
      self.close_button,
    ]
    for button in buttons:
      button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
      button.setFixedSize(QSize(28, 28))
      button.setStyleSheet(
        """QToolButton { border: 2px solid white;
                 border-radius: 12px;
                }
        """
      )
      title_bar_layout.addWidget(button)

```

This loop iterates over our four buttons in a predefined order. The first thing to do inside the loop is to define the focus policy of each button. We don't want these buttons to steal focus from buttons in the window's working space , therefore we set their focus policy to `NoFocus`.
Next, we set a fixed size of 28 by 28 pixels for the three buttons using the `setFixedSize()` method with a `QSize` object as an argument.
Our main goal in this section is to create a custom title bar. A handy way to customize the look and feel of PyQt widgets is to use CSS style sheets. In the above piece of code, we use the `setStyleSheet()` method to apply a custom CSS style sheet to our four buttons. The sheet defines a white and round border for each button.
The final line in the above code calls the `addWidget()` method to add each custom button to our title bar's layout. That's it! We're now ready to give our title bar a try. Go ahead and run the application from your command line. You'll see a window like the following:
![A PyQt window with a custom title bar](https://www.pythonguis.com/static/tutorials/qt/custom-title-bar/window-with-custom-title-bar.png) _A PyQt window with a custom title bar_
This is pretty simple styling, but you get the idea. You can tweak the title bar further, depending on your needs. For example, you can change the colors and borders, customize the title's font, add other widgets to the bar, and more.
We'll apply some nicer styles later, once we have the functionality in place! Keep reading.
Even though the title bar looks different, it has limited functionality. For example, if you click the _maximize_ button, then the window will change to its maximized state. However, the _normal_ button won't show up to allow you to return the window to its previous state.
In addition to this, if you try to move the window around your screen, you'll quickly notice a problem: it's impossible to move the window!
In the following sections, we'll write the necessary code to fix these issues and make our custom title bar fully functional. To kick things off, let's start by fixing the state issues.
## Updating the Window's State
To fix the issue related to the window's state, we'll write two new methods. We need to override one method and write another. In the `MainWindow` class, we'll override the `changeEvent()` method. The `changeEvent()` method is called directly by Qt whenever the window state changes: for example if the window is maximized or hidden. By overriding this event we can add our own custom behavior.
Here's the code that overrides the `changeEvent()` method:
python ```
from PyQt5.QtCore import QSize, Qt, QEvent
# ...
class MainWindow(QMainWindow):
  # ...
  def changeEvent(self, event):
    if event.type() == QEvent.Type.WindowStateChange:
      self.title_bar.window_state_changed(self.windowState())
    super().changeEvent(event)
    event.accept()

```

This method is fairly straightforward. We check the event type to see if it is a `WindowStateChange`. If that's the case, we call the `window_state_changed()` method of our custom title bar, passing the current window's state as an argument. In the final two lines, we call the parent class's `changeEvent()` method and accept the event to signal that we've correctly processed it.
Here's the implementation of our `window_state_changed()` method:
python ```
# ...
class CustomTitleBar(QWidget):
  # ...
  def window_state_changed(self, state):
    if state == Qt.WindowState.WindowMaximized:
      self.normal_button.setVisible(True)
      self.max_button.setVisible(False)
    else:
      self.normal_button.setVisible(False)
      self.max_button.setVisible(True)

```

This method takes a window's state as an argument. Depending on the value of the state parameter we will optionally show and hide the maximize & restore buttons.
First, if the window is currently maximized we will show the _normal_ button and hide the _maximize_ button. Alternatively, if the window is currently _not_ maximized we will hide the _normal_ button and show the _maximize_ button.
The effect of this, together with the order we added the buttons above, is that when you maximize the window the _maximize_ button will _appear to be_ replaced with the _normal_ button. When you restore the window to it's normal size, the _normal_ button will be replaced with the _maximize_ button.
Go ahead and run the app again. Click the _maximize_ button. You'll note that when the window gets maximized, the middle button changes its icon. Now you have access to the _normal_ button. If you click it, then the window will recover its previous state. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
## Handling Window's Moves
Now it's time to write the code that enables us to move the window around the screen while holding your mouse's left-click button on the title bar. To fix this issue, we only need to add code to the `CustomTitleBar` class.
In particular, we need to override three mouse events:
  * `mousePressEvent()` will let us know when the user clicks on our custom title bar using the mouse's left-click button. This may indicate that the window movement should start.
  * `mouseMoveEvent()` will let us process the window movements.
  * `mouseReleaseEvent()` will let us know when the user has released the mouse's left-click button so that we can stop moving the window.


Here's the code that overrides the `mousePressEvent()` method:
python ```
# ...
class CustomTitleBar(QWidget):
  # ...
  def mousePressEvent(self, event):
    if event.button() == Qt.MouseButton.LeftButton:
      self.initial_pos = event.pos()
    super().mousePressEvent(event)
    event.accept()

```

In this method, we first check if the user clicks on the title bar using the mouse's left-click button. If that's the case, then we update our `initial_pos` attribute to the clicked point. Remember that we defined `initial_pos` and initialized it to `None` back in the `__init__()` method of `CustomTitleBar`.
Next, we need to override the `mousePressEvent()` method. Here's the required code:
python ```
# ...
class CustomTitleBar(QWidget):
  # ...
  def mouseMoveEvent(self, event):
    if self.initial_pos is not None:
      delta = event.pos() - self.initial_pos
      self.window().move(
        self.window().x() + delta.x(),
        self.window().y() + delta.y(),
      )
    super().mouseMoveEvent(event)
    event.accept()

```

This `if` statement in `mouseMoveEvent()` checks if the `initial_pos` attribute is not `None`. If this condition is true, then the `if` code block executes because we have a valid initial position.
The first line in the `if` code block calculates the difference, or `delta`, between the current and initial mouse positions. To get the current position, we call the `pos()` method on the `event` object.
The following four lines update the position of our application's main window by adding the `delta` values to the current window position. The `move()` method does the hard work of moving the window.
In summary, this code updates the window position based on the movement of our mouse. It tracks the initial position of the mouse, calculates the difference between the initial position and the current position, and applies that difference to the window's position.
Finally, we can complete the `mouseReleaseEvent()` method:
python ```
# ...
class CustomTitleBar(QWidget):
  # ...
  def mouseReleaseEvent(self, event):
    self.initial_pos = None
    super().mouseReleaseEvent(event)
    event.accept()

```

This method's implementation is pretty straightforward. Its purpose is to reset the initial position by setting it back to `None` when the mouse is released, indicating that the drag is complete.
That's it! Go ahead and run your app again. Click on your custom title bar and move the window around while holding the mouse's left-click button. Can you move the window? Great! Your custom title bar is now fully functional.
The completed code for the custom title bar is shown below:
python ```
from PyQt5.QtCore import QSize, Qt, QEvent
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import (
  QApplication,
  QHBoxLayout,
  QLabel,
  QMainWindow,
  QStyle,
  QToolButton,
  QVBoxLayout,
  QWidget,
)
class CustomTitleBar(QWidget):
  def __init__(self, parent):
    super().__init__(parent)
    self.setAutoFillBackground(True)
    self.setBackgroundRole(QPalette.ColorRole.Highlight)
    self.initial_pos = None
    title_bar_layout = QHBoxLayout(self)
    title_bar_layout.setContentsMargins(1, 1, 1, 1)
    title_bar_layout.setSpacing(2)
    self.title = QLabel(f"{self.__class__.__name__}", self)
    self.title.setStyleSheet(
      """font-weight: bold;
        border: 2px solid black;
        border-radius: 12px;
        margin: 2px;
      """
    )
    self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    if title := parent.windowTitle():
      self.title.setText(title)
    title_bar_layout.addWidget(self.title)
    # Min button
    self.min_button = QToolButton(self)
    min_icon = self.style().standardIcon(
      QStyle.StandardPixmap.SP_TitleBarMinButton
    )
    self.min_button.setIcon(min_icon)
    self.min_button.clicked.connect(self.window().showMinimized)
    # Max button
    self.max_button = QToolButton(self)
    max_icon = self.style().standardIcon(
      QStyle.StandardPixmap.SP_TitleBarMaxButton
    )
    self.max_button.setIcon(max_icon)
    self.max_button.clicked.connect(self.window().showMaximized)
    # Close button
    self.close_button = QToolButton(self)
    close_icon = self.style().standardIcon(
      QStyle.StandardPixmap.SP_TitleBarCloseButton
    )
    self.close_button.setIcon(close_icon)
    self.close_button.clicked.connect(self.window().close)
    # Normal button
    self.normal_button = QToolButton(self)
    normal_icon = self.style().standardIcon(
      QStyle.StandardPixmap.SP_TitleBarNormalButton
    )
    self.normal_button.setIcon(normal_icon)
    self.normal_button.clicked.connect(self.window().showNormal)
    self.normal_button.setVisible(False)
    # Add buttons
    buttons = [
      self.min_button,
      self.normal_button,
      self.max_button,
      self.close_button,
    ]
    for button in buttons:
      button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
      button.setFixedSize(QSize(28, 28))
      button.setStyleSheet(
        """QToolButton { border: 2px solid white;
                 border-radius: 12px;
                }
        """
      )
      title_bar_layout.addWidget(button)
  def window_state_changed(self, state):
    if state == Qt.WindowState.WindowMaximized:
      self.normal_button.setVisible(True)
      self.max_button.setVisible(False)
    else:
      self.normal_button.setVisible(False)
      self.max_button.setVisible(True)
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Custom Title Bar")
    self.resize(400, 200)
    self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    central_widget = QWidget()
    self.title_bar = CustomTitleBar(self)
    work_space_layout = QVBoxLayout()
    work_space_layout.setContentsMargins(11, 11, 11, 11)
    work_space_layout.addWidget(QLabel("Hello, World!", self))
    centra_widget_layout = QVBoxLayout()
    centra_widget_layout.setContentsMargins(0, 0, 0, 0)
    centra_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
    centra_widget_layout.addWidget(self.title_bar)
    centra_widget_layout.addLayout(work_space_layout)
    central_widget.setLayout(centra_widget_layout)
    self.setCentralWidget(central_widget)
  def changeEvent(self, event):
    if event.type() == QEvent.Type.WindowStateChange:
      self.title_bar.window_state_changed(self.windowState())
    super().changeEvent(event)
    event.accept()
  def window_state_changed(self, state):
    self.normal_button.setVisible(state == Qt.WindowState.WindowMaximized)
    self.max_button.setVisible(state != Qt.WindowState.WindowMaximized)
  def mousePressEvent(self, event):
    if event.button() == Qt.MouseButton.LeftButton:
      self.initial_pos = event.pos()
    super().mousePressEvent(event)
    event.accept()
  def mouseMoveEvent(self, event):
    if self.initial_pos is not None:
      delta = event.pos() - self.initial_pos
      self.window().move(
        self.window().x() + delta.x(),
        self.window().y() + delta.y(),
      )
    super().mouseMoveEvent(event)
    event.accept()
  def mouseReleaseEvent(self, event):
    self.initial_pos = None
    super().mouseReleaseEvent(event)
    event.accept()
if __name__ == "__main__":
  app = QApplication([])
  window = MainWindow()
  window.show()
  app.exec()

```

## Making the Title Bar Look More Beautiful
So far we've covered the technical aspects of styling our window with a custom title bar, and added the code to make it function as expected. But it doesn't look _great_. In this section we'll take our existing code & tweak the styling and buttons to produce something that's a little more professional looking.
One common reason for wanting to apply custom title bars to a window is to integrate the title bar with the rest of the application. This technique is called a _unified title bar_ and can be seen in some popular applications such as web browsers, or Spotify.
![Unified title bar in Spotify](https://www.pythonguis.com/static/tutorials/qt/custom-title-bar/unified-titlebar.png)
In this section we'll look at how we can reproduce the same effect in PyQt using a combination of stylesheets & icons. Below is a screenshot of the final result which we'll be building.
![Style custom title bar in PyQt5](https://www.pythonguis.com/static/tutorials/qt/custom-title-bar/styled-window-custom-title-bar.png)
As you can see the window & the toolbar blend nicely together and the window has rounded corners. There are a few different ways to do this, but we'll cover a simple approach using Qt stylesheets to apply styling over the entire window.
In order to customize the shape of the window, we need to first tell the OS to stop drawing the default window outline and background for us. We do that by setting a _window attribute_ on the window. This is similar to the flags we already discussed, in that it turns on & off different window manager behaviors:
python ```
# ...
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Custom Title Bar")
    self.resize(400, 200)
    self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    # ...

```

We've added a call to `self.setAttribute` which sets the attribute `Qt.WidgetAttribute.WA_TranslucentBackground` on the window. If you run the code now you will see the window has become transparent, with only the widget text & toolbar visible.
Next, we'll tell Qt to draw a new _custom_ background for us. If you've worked with QSS before, the quickest way to apply curved edges to the window using QSS stylesheets would be to set `border-radius:` styles on the main window directly:
python ```
#...
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    # ...
    self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    self.setStyleSheet("background-color: gray; border-radius: 10px;")
#...

```

However, if you try this you'll notice that it doesn't work. If you enable a translucent background, the background of the window is not drawn (including your styles). If you _don't_ set translucent background, the window is filled to the edges with a solid color ignoring the border radius.
![Stylesheets can't alter window shape](https://www.pythonguis.com/static/tutorials/qt/custom-title-bar/stylesheet-window-styling.jpg).
The good news is that, with a bit of lateral thinking, there is a simple solution. We already know that we can construct interfaces by nesting widgets in layouts. Since we can't style the `border-radius` of a window, but we _can_ style any other widget, the solution is to simply add a container widget into our window & apply the curved-edge and background styles to that.
On our `MainWindow` object we already have a _central widget_ which contains our layout, so we can apply the styles there:
python ```
# ...
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    # ...
    central_widget = QWidget()
    # This container holds the window contents, so we can style it.
    central_widget.setObjectName("Container")
    central_widget.setStyleSheet("""#Container {
      background: qlineargradient(x1:0 y1:0, x2:1 y2:1, stop:0 #051c2a stop:1 #44315f);
      border-radius: 5px;
    }""")
    self.title_bar = CustomTitleBar(self)
    # ...

```

We've taken the existing `central_widget` object and assigned an _object name_ to it. This is a ID which we can use to refer to the widget from QSS, to apply our styles specifically to that widget.
If you're familiar with CSS you might expect that IDs like `#Container` must be unique. However, they are not: you can give multiple widgets the same object name if you like. So you can re-use this technique and QSS on multiple windows in your application without problems.
With this style applied on our window, we have a nice gradient background with curved corners.
Unfortunately, the title bar we created is drawn filled, and so the background and curved corners of our window are over-written. To make things look coherent we need to make our title bar also transparent by removing the background color & auto-fill behavior we set earlier.
We don't need to set any flags or attributes this widget because it is not a window. A `QWidget` object is transparent by default.
We can also make some tweaks to the style of the title label, such as adjusting the font size and making the title capitalized using `text-transform: uppercase` -- feel free to customize this yourself:
python ```
# ...
class CustomTitleBar(QWidget):
  def __init__(self, parent):
    super().__init__(parent)
    # self.setAutoFillBackground(True) # <-- remove
    # self.setBackgroundRole(QPalette.ColorRole.Highlight) # <-- remove
    self.initial_pos = None
    title_bar_layout = QHBoxLayout(self)
    title_bar_layout.setContentsMargins(1, 1, 1, 1)
    title_bar_layout.setSpacing(2)
    self.title = QLabel(f"{self.__class__.__name__}", self)
    self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.title.setStyleSheet("""
    QLabel { text-transform: uppercase; font-size: 10pt; margin-left: 48px; }
    """)

```

QSS is _very_ similar to CSS, especially for text styling.
The `margin-left: 48px` is to compensate for the 3 * 16px window icons on the right hand side so the text align centrally.
The icons are currently using built-in Qt icons which are a little bit plain & ugly. Next let's update the icons, using custom SVG icons of simple colored circles, for the minimize, maximize, close & restore buttons:
python ```
from PyQt5.QtGui import QIcon
# ...
class CustomTitleBar(QWidget):
  def __init__(self, parent):
    super().__init__(parent)
    # ...
    # Min button
    self.min_button = QToolButton(self)
    min_icon = QIcon()
    min_icon.addFile('min.svg')
    self.min_button.setIcon(min_icon)
    self.min_button.clicked.connect(self.window().showMinimized)
    # Max button
    self.max_button = QToolButton(self)
    max_icon = QIcon()
    max_icon.addFile('max.svg')
    self.max_button.setIcon(max_icon)
    self.max_button.clicked.connect(self.window().showMaximized)
    # Close button
    self.close_button = QToolButton(self)
    close_icon = QIcon()
    close_icon.addFile('close.svg') # Close has only a single state.
    self.close_button.setIcon(close_icon)
    self.close_button.clicked.connect(self.window().close)
    # Normal button
    self.normal_button = QToolButton(self)
    normal_icon = QIcon()
    normal_icon.addFile('normal.svg')
    self.normal_button.setIcon(normal_icon)
    self.normal_button.clicked.connect(self.window().showNormal)
    self.normal_button.setVisible(False)
    # ...

```

This code follows the same basic structure as before, but instead of using the built-in icons here we're loading our icons from SVG images. These images are very simple, consisting of a single circle in green, red or yellow for the different states mimicking macOS.
The `normal.svg` file for returning a maximized window to normal size shows a semi-transparent green circle for simplicity's sake, but you can include iconography and hover behaviors on the buttons if you prefer.
You can download these icons & all source code for this tutorial here: https://downloads.pythonguis.com/custom-title-bar-pyqt5.zip
The final step is to iterate through the created buttons, adding them to the title bar layout. This is slightly tweaked from before to remove the border styling, replacing it with simple padding & setting the icon sizes to 16px. Because we are using SVG files, the icons will automatically scale to the available space:
python ```
# ...
class CustomTitleBar(QWidget):
  def __init__(self, parent):
    super().__init__(parent)
    # ...
    for button in buttons:
      button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
      button.setFixedSize(QSize(16, 16))
      button.setStyleSheet(
        """QToolButton {
          border: none;
          padding: 2px;
        }
        """
      )
      title_bar_layout.addWidget(button)

```

And that's it! With these changes, you can now run your application and you'll see a nice sleek modern-looking UI with unified title bar and custom controls.
![Style custom titlebar in PyQt5](https://www.pythonguis.com/static/tutorials/qt/custom-title-bar/pyqt5-custom-modern-title-bar.jpg) _The final result, showing our unified title bar and window design._
The complete code is shown below:
python ```
from PyQt5.QtCore import QEvent, QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
  QApplication,
  QHBoxLayout,
  QLabel,
  QMainWindow,
  QStyle,
  QToolButton,
  QVBoxLayout,
  QWidget,
)
class CustomTitleBar(QWidget):
  def __init__(self, parent):
    super().__init__(parent)
    self.initial_pos = None
    title_bar_layout = QHBoxLayout(self)
    title_bar_layout.setContentsMargins(1, 1, 1, 1)
    title_bar_layout.setSpacing(2)
    self.title = QLabel(f"{self.__class__.__name__}", self)
    self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.title.setStyleSheet(
      """
    QLabel { text-transform: uppercase; font-size: 10pt; margin-left: 48px; }
    """
    )
    if title := parent.windowTitle():
      self.title.setText(title)
    title_bar_layout.addWidget(self.title)
    # Min button
    self.min_button = QToolButton(self)
    min_icon = QIcon()
    min_icon.addFile("min.svg")
    self.min_button.setIcon(min_icon)
    self.min_button.clicked.connect(self.window().showMinimized)
    # Max button
    self.max_button = QToolButton(self)
    max_icon = QIcon()
    max_icon.addFile("max.svg")
    self.max_button.setIcon(max_icon)
    self.max_button.clicked.connect(self.window().showMaximized)
    # Close button
    self.close_button = QToolButton(self)
    close_icon = QIcon()
    close_icon.addFile("close.svg") # Close has only a single state.
    self.close_button.setIcon(close_icon)
    self.close_button.clicked.connect(self.window().close)
    # Normal button
    self.normal_button = QToolButton(self)
    normal_icon = QIcon()
    normal_icon.addFile("normal.svg")
    self.normal_button.setIcon(normal_icon)
    self.normal_button.clicked.connect(self.window().showNormal)
    self.normal_button.setVisible(False)
    # Add buttons
    buttons = [
      self.min_button,
      self.normal_button,
      self.max_button,
      self.close_button,
    ]
    for button in buttons:
      button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
      button.setFixedSize(QSize(16, 16))
      button.setStyleSheet(
        """QToolButton {
          border: none;
          padding: 2px;
        }
        """
      )
      title_bar_layout.addWidget(button)
  def window_state_changed(self, state):
    if state == Qt.WindowState.WindowMaximized:
      self.normal_button.setVisible(True)
      self.max_button.setVisible(False)
    else:
      self.normal_button.setVisible(False)
      self.max_button.setVisible(True)
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Custom Title Bar")
    self.resize(400, 200)
    self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    central_widget = QWidget()
    # This container holds the window contents, so we can style it.
    central_widget.setObjectName("Container")
    central_widget.setStyleSheet(
      """#Container {
      background: qlineargradient(x1:0 y1:0, x2:1 y2:1, stop:0 #051c2a stop:1 #44315f);
      border-radius: 5px;
    }"""
    )
    self.title_bar = CustomTitleBar(self)
    work_space_layout = QVBoxLayout()
    work_space_layout.setContentsMargins(11, 11, 11, 11)
    work_space_layout.addWidget(QLabel("Hello, World!", self))
    centra_widget_layout = QVBoxLayout()
    centra_widget_layout.setContentsMargins(0, 0, 0, 0)
    centra_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
    centra_widget_layout.addWidget(self.title_bar)
    centra_widget_layout.addLayout(work_space_layout)
    central_widget.setLayout(centra_widget_layout)
    self.setCentralWidget(central_widget)
  def changeEvent(self, event):
    if event.type() == QEvent.Type.WindowStateChange:
      self.title_bar.window_state_changed(self.windowState())
    super().changeEvent(event)
    event.accept()
  def window_state_changed(self, state):
    self.normal_button.setVisible(state == Qt.WindowState.WindowMaximized)
    self.max_button.setVisible(state != Qt.WindowState.WindowMaximized)
  def mousePressEvent(self, event):
    if event.button() == Qt.MouseButton.LeftButton:
      self.initial_pos = event.pos()
    super().mousePressEvent(event)
    event.accept()
  def mouseMoveEvent(self, event):
    if self.initial_pos is not None:
      delta = event.pos() - self.initial_pos
      self.window().move(
        self.window().x() + delta.x(),
        self.window().y() + delta.y(),
      )
    super().mouseMoveEvent(event)
    event.accept()
  def mouseReleaseEvent(self, event):
    self.initial_pos = None
    super().mouseReleaseEvent(event)
    event.accept()
if __name__ == "__main__":
  app = QApplication([])
  window = MainWindow()
  window.show()
  app.exec()

```

## Conclusion
In this tutorial, we have learned the fundamentals of creating custom title bars in PyQt. To do this, we have combined PyQt's widgets, layouts, and styling capabilities to create a visually appealing title bar for a PyQt app.
With this skill under your belt, you're now ready to create title bars that align perfectly with your application's unique style and branding. This will allow you to break away from the standard window decoration provided by your operating system and add a personal touch to your user interface.
Now let your imagination run and transform your PyQt application's UX. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Leo Well](https://www.pythonguis.com/static/theme/images/authors/leo-well.jpg)](https://www.pythonguis.com/authors/leo-well/)
**How to Create a Custom Title Bar for a PyQt5 Window** was written by [Leo Well](https://www.pythonguis.com/authors/leo-well/) with contributions from [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
**How to Create a Custom Title Bar for a PyQt5 Window** was published in [tutorials](https://www.pythonguis.com/tutorials/) on February 18, 2023 (updated October 18, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [window](https://www.pythonguis.com/topics/window/) [title bar](https://www.pythonguis.com/topics/title-bar/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
