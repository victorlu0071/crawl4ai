# Content from: https://www.pythonguis.com/tutorials/restore-window-geometry-pyqt/

[](https://www.pythonguis.com/tutorials/restore-window-geometry-pyqt/#menu)
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
# How to Restore the Window's Geometry in a PyQt6 App
Make Your Windows Remember Their Last Geometry
by [Leo Well](https://www.pythonguis.com/authors/leo-well/) Last updated Nov 04 PyQt6 [ Tutorials ](https://www.pythonguis.com/tutorials/)
This tutorial is also available for [PyQt5](https://www.pythonguis.com/tutorials/restore-window-geometry-pyqt5/)
In GUI applications the window's position & size are known as the window _geometry_. Saving and restoring the geometry of a window between executions is a useful feature in many applications. With persistent geometry users can arrange applications on their desktop for an optimal workflow and have the applications return to those positions every time they are launched.
In this tutorial, we will explore how to save and restore the geometry and state of a PyQt window using the [`QSettings`](https://www.pythonguis.com/faq/pyqt5-qsettings-how-to-use-qsettings/) class. With this functionality, you will be able to give your applications a usability boost.
To follow along with this tutorial, you should have prior knowledge of creating GUI apps with Python and [PyQt](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/). Additionally, having a basic understanding of using the `QSettings` class to manage an application's [settings](https://www.pythonguis.com/faq/pyqt5-qsettings-how-to-use-qsettings/) will be beneficial.
Table of Contents
  * [Understanding a Window's Geometry](https://www.pythonguis.com/tutorials/restore-window-geometry-pyqt/#understanding-a-windows-geometry)
  * [Keeping an App's Geometry Settings: The QSetting Class](https://www.pythonguis.com/tutorials/restore-window-geometry-pyqt/#keeping-an-apps-geometry-settings-the-qsetting-class)
  * [Restoring the Window's Geometry With pos and size](https://www.pythonguis.com/tutorials/restore-window-geometry-pyqt/#restoring-the-windows-geometry-with-pos-and-size)
  * [Restoring the Window's Geometry With geometry](https://www.pythonguis.com/tutorials/restore-window-geometry-pyqt/#restoring-the-windows-geometry-with-geometry)
  * [Restoring the Window's Geometry and State](https://www.pythonguis.com/tutorials/restore-window-geometry-pyqt/#restoring-the-windows-geometry-and-state)
  * [Conclusion](https://www.pythonguis.com/tutorials/restore-window-geometry-pyqt/#conclusion)


## Understanding a Window's Geometry
PyQt defines the [geometry](https://doc.qt.io/qt-6/application-windows.html#window-geometry) of a window using a few properties. These properties represent a window's **position** on the screen and **size**. Here's a summary of PyQt's geometry-related properties:
Property | Description | Access Method  
---|---|---  
[`x`](https://doc.qt.io/qt-6/qwidget.html#x-prop) | Holds the `x` coordinate of a widget relative to its parent. If the widget is a window, `x` includes any window frame and is relative to the desktop. This property defaults to `0`. | `x()`  
[`y`](https://doc.qt.io/qt-6/qwidget.html#y-prop) | Holds the `y` coordinate of a widget relative to its parent. If the widget is a window, `y` includes any window frame and is relative to the desktop. This property defaults to `0`. | `y()`  
[`pos`](https://doc.qt.io/qt-6/qwidget.html#pos-prop) | Holds the position of the widget within its parent widget. If the widget is a window, the position is relative to the desktop and includes any frame. | `pos()`  
[`geometry`](https://doc.qt.io/qt-6/qwidget.html#geometry-prop) | Holds the widget's geometry relative to its parent and excludes the window frame. | `geometry()`  
[`width`](https://doc.qt.io/qt-6/qwidget.html#width-prop) | Holds the width of the widget, excluding any window frame. | `width()`  
[`height`](https://doc.qt.io/qt-6/qwidget.html#height-prop) | Holds the height of the widget, excluding any window frame. | `height()`  
[`size`](https://doc.qt.io/qt-6/qwidget.html#size-prop) | Holds the size of the widget, excluding any window frame. | `size()`  
In PyQt, the [`QWidget`](https://doc.qt.io/qt-6/qwidget.html) class provides the access methods in the table above. Note that when your widget is a window or form, the first three methods operate on the window and its frame, while the last four methods operate on the **client area** , which is the window's workspace without the external frame.
Additionally, the `x` and `y` coordinates are relative to the screen of your computer. The origin of coordinates is the upper left corner of the screen, at which point both `x` and `y` are `0`.
Let's create a small demo app to inspect all these properties in real time. To do this, go ahead and fire up your code editor or IDE and create a new Python file called `geometry_properties.py`. Then add the following code to the file and save it in your favorite working directory: 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
python ```
from PyQt6.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QWidget,
)
class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Window's Geometry")
    self.resize(400, 200)
    self.central_widget = QWidget()
    self.global_layout = QVBoxLayout()
    self.geometry_properties = [
      "x",
      "y",
      "pos",
      "width",
      "height",
      "size",
      "geometry",
    ]
    for prop in self.geometry_properties:
      self.__dict__[f"{prop}_label"] = QLabel(f"{prop}:")
      self.global_layout.addWidget(self.__dict__[f"{prop}_label"])
    button = QPushButton("Update Geometry Properties")
    button.clicked.connect(self.update_labels)
    self.global_layout.addWidget(button)
    self.central_widget.setLayout(self.global_layout)
    self.setCentralWidget(self.central_widget)
  def update_labels(self):
    for prop in self.geometry_properties:
      self.__dict__[f"{prop}_label"].setText(
        f"{prop}: {getattr(self, prop)()}"
      )
if __name__ == "__main__":
  app = QApplication([])
  window = Window()
  window.show()
  app.exec()

```

Wow! There's a lot of code in this file. First, we import the required classes from `PyQt6.QtWidgets`. Then, we create our app's main window by inheriting from [`QMainWindow`](https://doc.qt.io/qt-6/qmainwindow.html).
In the initializer method, we set the window's title and size using [`setWindowTitle()`](https://doc.qt.io/qt-6/qwidget.html#windowTitle-prop) and [`resize()`](https://doc.qt.io/qt-6/qwidget.html#resize-1), respectively. Next, we define a central widget and a layout for our main window.
We also define a list of properties. We'll use that list to add some [`QLabel`](https://www.pythonguis.com/tutorials/pyside6-widgets/#qlabel) objects. Each label will show a geometry property and its current values. The _Update Geometry Properties_ [button](https://www.pythonguis.com/docs/qpushbutton/) allows us to update the value of the window's geometry properties.
Finally, we define the `update_labels()` method to update the values of all the geometry properties using their corresponding access methods. That's it! Go ahead and run the app. You'll get the following window on your screen:
![A Window Showing Labels for Every Geometry Property](https://www.pythonguis.com/static/tutorials/qt/restore-window-geometry-pyqt/window-geometry-properties.png) _A Window Showing Labels for Every Geometry Property_
Looking good! Now go ahead and click the _Update Geometry Properties_ button. You'll see how all the properties get updated. Your app's window will look something like this:
![A Window Showing the Current Value of Every Geometry Property](https://www.pythonguis.com/static/tutorials/qt/restore-window-geometry-pyqt/window-geometry-properties-update.png) _A Window Showing the Current Value of Every Geometry Property_
As you can see, `x` and `y` are numeric values, while `pos` is a [`QPoint`](https://doc.qt.io/qt-6/qpoint.html) object with `x` and `y` as its coordinates. These properties define the position of this window on your computer screen.
The `width` and `height` properties are also numeric values, while the `size` property is a [`QSize`](https://doc.qt.io/qt-6/qsize.html) object defined after the current width and height.
Finally, the `geometry` property is a [`QRect`](https://doc.qt.io/qt-6/qrect.html) object. In this case, the rectangle comprises `x`, `y`, `width`, and `height`.
Great! With this first approach to how PyQt defines a window's geometry, we're ready to continue digging into this tutorial's main topic: restoring the geometry of a window in PyQt.
## Keeping an App's Geometry Settings: The `QSetting` Class
Users of GUI apps will generally expect the apps to remember their settings across sessions. This information is often referred to as **settings** or **preferences**. In PyQt applications, you'll manage settings and preferences using the [`QSettings`](https://doc.qt.io/qt-6/qsettings.html) class. This class allows you to have persistent platform-independent settings in your GUI app.
A commonly expected feature is that the app remembers the geometry of its windows, particularly the main window.
In this section, you'll learn how to save and restore the window's geometry in a PyQt application. Let's start by creating a skeleton PyQt application to kick things off. Go ahead and create a new Python file called `geometry.py`. Once you have the file opened in your favorite code editor or IDE, then add the following code:
python ```
from PyQt6.QtWidgets import QApplication, QMainWindow
class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Window's Geometry")
    self.move(50, 50)
    self.resize(400, 200)
if __name__ == "__main__":
  app = QApplication([])
  window = Window()
  window.show()
  app.exec()

```

This code creates a minimal PyQt app with an empty main window. The window will appear at 50 pixels from the upper left corner of your computer screen and have a size of 400 by 200 pixels.
We'll use the above code as a starting point to make the app remember and restore the main window's geometry across sessions.
First, we need to have a `QSettings` instance in our app. Therefore, you have to import `QSettings` from `PyQt6.QtCore` and instantiate it as in the code below:
python ```
from PyQt6.QtCore import QSettings
from PyQt6.QtWidgets import QApplication, QMainWindow
class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Window's Geometry")
    self.move(50, 50)
    self.resize(400, 200)
    self.settings = QSettings("PyhonGUIs", "GeometryApp")

```

When instantiating `QSettings`, we must provide the name of our company or organization and the name of our application. We use `"PyhonGUIs"` as the organization and `"GeometryApp"` as the application name.
Now that we have a `QSettings` instance, we should implement two methods. The first method should allow you to save the app's settings and preferences. The second method should help you read and load the settings. In this tutorial, we'll call these methods `write_settings()` and `read_settings()`, respectively:
python ```
class Window(QMainWindow):
  # ...
  def write_settings(self):
    # Write settings here...
  def read_settings(self):
    # Read settings here...

```

Note that our methods don't do anything yet. You'll write them in a moment. For now, they're just placeholders.
The `write_settings()` method must be called when the user closes or terminates the application. This way, you guarantee that all the modified settings get saved for the next session. So, the appropriate place to call `write_settings()` is from the main window's close event handler.
Let's override the `closeEvent()` method as in the code below:
python ```
class Window(QMainWindow):
  # ...
  def closeEvent(self, event):
    self.write_settings()
    super().closeEvent(event)
    event.accept()

```

In this code, we override the `closeEvent()` handler method. The first line calls `write_settings()` to ensure that we save the current state of our app's settings. Then, we call the `closeEvent()` of our superclass `QMainWindow` to ensure the app's window closes correctly. Finally, we accept the current event to signal that it's been processed.
Now, where should we call `read_settings()` from? In this example, the best place for calling the `read_settings()` method is `.__init__()`. Go ahead and add the following line of code to the end of your `__init__()` method:
python ```
class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Window's Geometry")
    self.move(50, 50)
    self.resize(400, 200)
    self.settings = QSettings("PythonGUIs", "GeometryApp")
    self.read_settings()

```

By calling the `read_settings()` method from `__init__()`, we ensure that our app will read and load its settings every time the main window gets created and initialized.
Great! We're on the way to getting our application to remember and restore its window's geometry. First, you need to know that you have at least two ways to restore the geometry of a window in PyQt: 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
  * Using the `pos` and `size` properties
  * Using the `geometry` property


In both cases, you need to save the current value of the selected property and load the saved value when the application starts. To kick things off, let's start with the first approach.
## Restoring the Window's Geometry With `pos` and `size`
In this section, we'll first write the required code to save the current value of `pos` and `size` by taking advantage of our `QSettings` object. The code snippet below shows the changes that you need to make on your `write_settings()` method to get this done:
python ```
class Window(QMainWindow):
  # ...
  def write_settings(self):
    self.settings.setValue("pos", self.pos())
    self.settings.setValue("size", self.size())

```

This code is straightforward. We call the [`setValue()`](https://doc.qt.io/qt-6/qsettings.html#setValue) method on our setting object to set the `"pos"` and `"size"` configuration parameters. Note that we get the current value of each property using the corresponding access method.
With the `write_settings()` method updated, we're now ready to read and load the geometry properties from our app's settings. Go ahead and update the `read_settings()` method as in the code below:
python ```
class Window(QMainWindow):
  # ...
  def read_settings(self):
    self.move(self.settings.value("pos", defaultValue=QPoint(50, 50)))
    self.resize(self.settings.value("size", defaultValue=QSize(400, 200)))

```

The first line inside `read_settings()` retrieves the value of the `"pos"` setting parameter. If there's no saved value for this parameter, then we use `QPoint(50, 50)` as the default value. Next, the [`move()`](https://doc.qt.io/qt-6/qwidget.html#move-1) method moves the app's window to the resulting position on your screen.
The second line in `read_settings()` does something similar to the first one. It retrieves the current value of the `"size"` parameter and resizes the window accordingly.
Great! It's time for a test! Go ahead and run your application. Then, move the app's window to another position on your screen and resize the window as desired. Finally, close the app's window to terminate the current session. When you run the app again, the window will appear in the same position. It will also have the same size.
If you have any issues completing and running the example app, then you can grab the entire code below:
python ```
from PyQt6.QtCore import QPoint, QSettings, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow
class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Window's Geometry")
    self.move(50, 50)
    self.resize(400, 200)
    self.settings = QSettings("PyhonGUIs", "GeometryApp")
    self.read_settings()
  def write_settings(self):
    self.settings.setValue("pos", self.pos())
    self.settings.setValue("size", self.size())
  def read_settings(self):
    self.move(self.settings.value("pos", defaultValue=QPoint(50, 50)))
    self.resize(self.settings.value("size", defaultValue=QSize(400, 200)))
  def closeEvent(self, event):
    self.write_settings()
    super().closeEvent(event)
    event.accept()
if __name__ == "__main__":
  app = QApplication([])
  window = Window()
  window.show()
  app.exec()

```

Now you know how to restore the geometry of a window in a PyQt app using the `pos` and `size` properties. It's time to change gears and learn how to do this using the `geometry` property.
## Restoring the Window's Geometry With `geometry`
We can also restore the geometry of a PyQt window using its `geometry` property and the [`restoreGeometry()`](https://doc.qt.io/qt-6/qwidget.html#restoreGeometry) method. To do that, we first need to save the current geometry using our `QSettings` object.
Go ahead and create a new Python file in your working directory. Once you have the file in place, add the following code to it:
python ```
from PyQt6.QtCore import QByteArray, QSettings
from PyQt6.QtWidgets import QApplication, QMainWindow
class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Window's Geometry")
    self.move(50, 50)
    self.resize(400, 200)
    self.settings = QSettings("PythonGUIs", "GeometryApp")
    self.read_settings()
  def write_settings(self):
    self.settings.setValue("geometry", self.saveGeometry())
  def read_settings(self):
    self.restoreGeometry(self.settings.value("geometry", QByteArray()))
  def closeEvent(self, event):
    self.write_settings()
    super().closeEvent(event)
    event.accept()
if __name__ == "__main__":
  app = QApplication([])
  window = Window()
  window.show()
  app.exec()

```

There are only two changes in this code compared to the code from the previous section. We've modified the implementation of the `write_settings()` and `read_settings()` methods.
In `write_settings()`, we use the `setValue()` to save the current `geometry` of our app's window. The [`saveGeometry()`](https://doc.qt.io/qt-6/qwidget.html#saveGeometry) allows us to access and save the current window's geometry. In `read_settings()`, we call the `value()` method to retrieve the saved `geometry` value. Then, we use `restoreGeometry()` to restore the geometry of our window.
Again, you can run the application consecutive times and change the position and size of its main window to ensure your code works correctly.
## Restoring the Window's Geometry and State
If your app's window has [toolbars](https://www.pythonguis.com/tutorials/pyqt6-actions-toolbars-menus/) and [dock widgets](https://doc.qt.io/qt-6/qdockwidget.html), then you want to restore their _state_ on the parent window. To do that, you can use the [`restoreState()`](https://doc.qt.io/qt-6/qmainwindow.html#restoreState) method. To illustrate this, let's reuse the code from the previous section.
Update the content of `write_settings()` and `read_settings()` as follows:
python ```
class Window(QMainWindow):
  # ...
  def write_settings(self):
    self.settings.setValue("geometry", self.saveGeometry())
    self.settings.setValue("windowState", self.saveState())
  def read_settings(self):
    self.restoreGeometry(self.settings.value("geometry", QByteArray()))
    self.restoreState(self.settings.value("windowState", QByteArray()))

```

In `write_settings()`, we add a new setting value called `"windowState"`. To keep this setting, we use the [`saveState()`](https://doc.qt.io/qt-6/qmainwindow.html#saveState) method, which saves the current state of this window's toolbars and dock widgets. Meanwhile, in `read_settings()`, we restore the window's state by calling the `value()` method, as usual, to get the state value back from our `QSettings` object. Finally, we use `restoreState()` to restore the state of toolbars and dock widgets.
Now, to make sure that this new code works as expected, let's add a sample toolbar and a dock window to our app's main window. Go ahead and add the following methods right after the `__init__()` method:
python ```
from PyQt6.QtCore import QByteArray, QSettings, Qt
from PyQt6.QtWidgets import QApplication, QDockWidget, QMainWindow
class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Window's State")
    self.resize(400, 200)
    self.settings = QSettings("PythonGUIs", "GeometryApp")
    self.create_toolbar()
    self.create_dock()
    self.read_settings()
  def create_toolbar(self):
    toolbar = self.addToolBar("Toolbar")
    toolbar.addAction("One")
    toolbar.addAction("Two")
    toolbar.addAction("Three")
  def create_dock(self):
    dock = QDockWidget("Dock", self)
    dock.setAllowedAreas(
      Qt.DockWidgetArea.LeftDockWidgetArea
      | Qt.DockWidgetArea.RightDockWidgetArea
    )
    self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)
  # ...

```

In this new update, we first import the `Qt` namespace from `PyQt6.QtCore` and `QDockWidget` from `PyQt6.QtWidgets`. Then we call the two new methods from `__init__()` to create the toolbar and dock widget at initialization time.
In the `create_toolbar()` method, we create a sample toolbar with three sample buttons. This toolbar will show at the top of our app's window by default.
Next, we create a dock widget in `create_dock()`. This widget will occupy the rest of our window's working area.
That's it! You're now ready to give your app a try. You'll see a window like the following:
![A Window Showing a Sample Toolbar and a Dock Widget](https://www.pythonguis.com/static/tutorials/qt/restore-window-geometry-pyqt/window-state.png) _A Window Showing a Sample Toolbar and a Dock Widget_
Play with the toolbar and the dock widget. Move them around. Then close the app's window and run the app again. Your toolbar and dock widget will show in the last position you left them.
## Conclusion
Through this tutorial, you have learned how to restore the **geometry** and **state** of a window in PyQt applications using the `QSettings` class. By utilizing the `pos`, `size`, `geometry`, and state properties, you can give your users the convenience of persistent position and size on your app's windows.
With this knowledge, you can enhance the usability of your PyQt applications, making your app more intuitive and user-friendly.
1:1 Coaching & Tutoring for your Python GUIs project
[![Martin Fitzpatrick Python GUIs Coaching & Training](https://www.pythonguis.com/static/theme/images/products/coaching.jpg)](https://calendly.com/martinfitzpatrick/60min-python-guis-coaching)
[60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/) [Book Now](https://www.pythonguis.com/live/)
1:1 Python GUIs Coaching & Training
**Comprehensive code review** • **Bugfixes** & improvements • **Maintainability** advice and **architecture** improvements • **Design and usability** assessment • Suggestions and tips to **expand your knowledge** • **Packaging and distribution** help for Windows, Mac & Linux • [Find out more.](https://www.pythonguis.com/live)
Mark As Complete 
[![Leo Well](https://www.pythonguis.com/static/theme/images/authors/leo-well.jpg)](https://www.pythonguis.com/authors/leo-well/)
**How to Restore the Window's Geometry in a PyQt6 App** was written by [Leo Well](https://www.pythonguis.com/authors/leo-well/) with contributions from [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
**How to Restore the Window's Geometry in a PyQt6 App** was published in [tutorials](https://www.pythonguis.com/tutorials/) on November 13, 2023 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
