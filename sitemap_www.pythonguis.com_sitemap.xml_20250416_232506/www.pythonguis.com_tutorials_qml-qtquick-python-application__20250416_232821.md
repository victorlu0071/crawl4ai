# Content from: https://www.pythonguis.com/tutorials/qml-qtquick-python-application/

[](https://www.pythonguis.com/tutorials/qml-qtquick-python-application/#menu)
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
# Create Applications with QtQuick in PyQt5
Build modern applications with declarative QML
by [Amoh-Gyebi Ampofo](https://www.pythonguis.com/authors/amoh-gyebi-ampofo/) Last updated Apr 04 PyQt5 [ QtQuick & QML in PyQt5 ](https://www.pythonguis.com/pyqt5-tutorial/#qt-quick)
#### [ PyQt5 Tutorial ](https://www.pythonguis.com/pyqt5-tutorial/) — [QtQuick & QML in PyQt5](https://www.pythonguis.com/pyqt5-tutorial/#qt-quick)
  * [Create Applications with QtQuick in PyQt5](https://www.pythonguis.com/tutorials/qml-qtquick-python-application/)
  * [Animations and Transformations With QtQuick in PyQt5](https://www.pythonguis.com/tutorials/qml-animations-transformations/)


This tutorial is also available for [PySide2](https://www.pythonguis.com/tutorials/pyside-qml-qtquick-python-application/) , [PySide6](https://www.pythonguis.com/tutorials/pyside6-qml-qtquick-python-application/) and [PyQt6](https://www.pythonguis.com/tutorials/pyqt6-qml-qtquick-python-application/)
In previous tutorials we've used the Qt Widgets API for building our applications. This has been the standard method for building applications since Qt was first developed. However, Qt provides another API for building user interfaces: Qt Quick. This is a modern mobile-focused API for app development, with which you can create dynamic and highly customizable user interfaces.
Table of Contents
  * [QtQuick](https://www.pythonguis.com/tutorials/qml-qtquick-python-application/#qtquick)
  * [Getting started](https://www.pythonguis.com/tutorials/qml-qtquick-python-application/#getting-started)
  * [Creating a “Hello World” app](https://www.pythonguis.com/tutorials/qml-qtquick-python-application/#creating-a-hello-world-app)
    * [Updating the UI design](https://www.pythonguis.com/tutorials/qml-qtquick-python-application/#updating-the-ui-design)
  * [Getting the time from Python](https://www.pythonguis.com/tutorials/qml-qtquick-python-application/#getting-the-time-from-python)
  * [Updating our app time display](https://www.pythonguis.com/tutorials/qml-qtquick-python-application/#updating-our-app-time-display)
  * [Updating the time using timers](https://www.pythonguis.com/tutorials/qml-qtquick-python-application/#updating-the-time-using-timers)
    * [setProperty](https://www.pythonguis.com/tutorials/qml-qtquick-python-application/#setproperty)
    * [Using signals](https://www.pythonguis.com/tutorials/qml-qtquick-python-application/#using-signals)
  * [Removing the window decorations](https://www.pythonguis.com/tutorials/qml-qtquick-python-application/#removing-the-window-decorations)
  * [The complete final code](https://www.pythonguis.com/tutorials/qml-qtquick-python-application/#the-complete-final-code)


## QtQuick
Qt Quick uses a declarative scripting language -- the Qt Modeling Language (QML) -- to define user interfaces. With it you can build completely custom UIs, with dynamic graphical elements and fluid transitions and effects. UIs built with QML have more in common with mobile apps than traditional desktop applications, reflecting it's origin with Nokia, but Qt Quick can be used on all platforms supported by Qt.
QML syntax also supports embedded Javascript which can be used to handle application logic -- in simple applications the entire app can be implemented in the QML! But using PyQt/PySide you can also write your application code in Python and hook this up to your QML. This has the advantage of keeping your UI design (QML) and business logic (Python) implementation properly isolated, and gives you access to all the Python libraries to power the backend of your app.
Before starting this tutorial you will need to install PyQt or PySide, see [the installation guides](https://www.pythonguis.com/installation/).
For building QML applications you can use PyQt5, PySide2, PyQt6 or PySide6. If using Qt 6 you will need v6.1 or later.
## Getting started
In this tutorial we will be using PyQt/PySide with the Qt Quick/QML API. If you've used Qt Widgets before, many of the Qt Quick concepts will seem familiar. While QML does not make use of `QtWidget` classes, all the other parts of Qt (`QtCore`, `QtGui`, etc.) are still available.
Before we start writing out application, we can set up our project folder with the files we'll need in the right structure below. You can also [download a zip file containing these files](https://www.pythonguis.com/). 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
  * Create a project folder for the app, in our example we will call it: `clock`
  * Inside your `clock` folder create an empty file named `main.py`
  * Create a file alongside `main.py` named `main.qml`, to hold our UI definition in QML
  * Create an empty folder alongside the `main.py` and `main.qml` called `images`


## Creating a “Hello World” app
Open up the `main.py` in your editor and add the following skeleton code. This is the bare minimum code required to load a QML file and display it using the QML application engine.
**_main.py_**
python ```
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')
sys.exit(app.exec())

```

The above code calls `QGuiApplication` and `QQmlApplicationEngine` Which will use QML instead of QtWidgets as the UI layer for the Qt Application. It then connects the UI layers quit function with the app’s main quit function. So both can close when the UI has been closed by the user. Next it loads the QML file as the QML code for the UI. The `app.exec()` starts the Qt event loop and launches the application, just as in Qt Widgets.
Here the call to `app.exec()` is wrapped inside `sys.exit()` to return the exit code to the calling process in case of errors, but this isn't strictly necessary.
Next, add the following code to the `main.qml`.
**_main.qml_**
qml ```
import QtQuick 2.15
import QtQuick.Controls 2.15
ApplicationWindow {
  visible: true
  width: 600
  height: 500
  title: "HelloApp"
  Text {
    anchors.centerIn: parent
    text: "Hello World"
    font.pixelSize: 24
  }
}

```

The above code creates a Window with a width and height as specified, a title of HelloApp and a Text object that is centered in the parent (in this case the window). The text displayed is “Hello World”, with a pixel size of 24px.
The `visible: true` is very important, without that the UI will be created but will be invisible!
Once you have entered the above code into the two files and saved them, you can run it and see the result. You can run the code like any other Python script -- navigate into the folder containing the `main.py` script and run it using `python` (or `python3` depending on your system).
shell ```
$ cd clock
$ python main.py

```

When the application launches you should see a window which looks like the following.
![Hello World shown in an application](https://www.pythonguis.com/static/tutorials/qt/first-qml-project/initial_shot.jpeg)
Success! We have a QML application, although it's very basic to start with. Next we'll modify the UI to make it a little more interesting and build towards a simple clock.
### Updating the UI design
First lets add an image as a background.
Place [this image](https://www.pythonguis.com/static/tutorials/qt/first-qml-project/background.png) in the folder we created earlier named `images`. This will be the background for our application window.
![A simple background image with a gradient effect](https://www.pythonguis.com/static/tutorials/qt/first-qml-project/background.png) _A simple background image with a gradient effect_
If you like, you can substitute any other image you have. We'll be placing white text over it, so dark simple images will work better.
**_main.qml_**
qml ```
import QtQuick 2.15
import QtQuick.Controls 2.15
ApplicationWindow {
  visible: true
  width: 400
  height: 600
  title: "Clock"
  Rectangle {
    anchors.fill: parent
    Image {
      anchors.fill: parent
      source: "./images/background.png"
      fillMode: Image.PreserveAspectCrop
    }
    Rectangle {
      anchors.fill: parent
      color: "transparent"
      Text {
        text: "16:38:33"
        font.pixelSize: 24
        color: "white"
      }
    }
  }
}

```

In this QML file we've defined our main application window using the `ApplicationWindow` object type. Within this we've defined a `Rectangle` and an `Image` which holds our background image, filling the parent. The `fillMode` defines how the image will be sized. In this example we've set the image to fill the parent window using `anchors.fill: parent` while preserving aspect ratio and cropping. This ensures the image fills the window area, without being deformed. You can also control the size of the image in memory by setting the `sourceSize` property, e.g.
qml ```
    Image {
      sourceSize.width: parent.width
      sourceSize.height: parent.height
      source: "./images/background.png"
      fillMode: Image.PreserveAspectCrop
    }

```

This approach allows you some more control -- for example, you could scale an image to half the size of the parent window by dividing the sizes in two and use this to tile multiple images.
qml ```
    Image {
      sourceSize.width: parent.width/2
      sourceSize.height: parent.height/2
      source: "./images/background.png"
      fillMode: Image.PreserveAspectCrop
    }

```

Alongside the `Image` we've also defined a transparent `Rectangle` which also fills the window. Since the rectangle is defined alongside the `Image` you might think it would appear adjacent in the UI, however since there isn't a layout defined on the window the elements are stacked -- the `Rectangle` appears on top of the `Image`.
By default `Rectangle` objects have a white background.
Finally, inside the rectangle, we've defined a `Text` object with the text "16:38:33" to mock up a standard time display.
If you run the app now, the text will appear at the top-left corner of our application window.
shell ```
$ python main.py

```

![By default text appears in the top left](https://www.pythonguis.com/static/tutorials/qt/first-qml-project/screenshot-bg-top-left.png) _By default text appears in the top left_
Let's move it somewhere else -- down to the bottom-left, with some margins to make it look nicer. In your QML code, update the `Text` object to include position anchors for the `Text` and change the size and color of the font.
**_main.qml_**
qml ```
      Text {
        anchors {
          bottom: parent.bottom
          bottomMargin: 12
          left: parent.left
          leftMargin: 12
        }
        text: "16:38:33"
        font.pixelSize: 48
        color: "white"
      }

```

Run the application again as before.
shell ```
$ python main.py

```

You will see the text has now moved to the bottom left.
![Application window with text in the bottom left](https://www.pythonguis.com/static/tutorials/qt/first-qml-project/screenshot-bg-bottom-left.png) _Application window with text in the bottom left_
So far, our time display is just a fixed text string -- it doesn't update, and unless you run it at the right time, it's going to be wrong. Not the most useful of clocks! Next we'll add some Python code to get the current system time and update our clock display automatically.
## Getting the time from Python
The Python standard library provides functions for handling time and date, including a number of options for getting the current time. For example, the Python function `time.gmtime()` provides a struct containing the current GMT time, while `time.localtime()` will give the time in your current local timezone.
Once you have a time `struct` you can pass this to the `time.strftime()` function to get a properly formatted string. The `strftime` function accepts two arguments -- first a time format string, and second the time struct to use. The time format string uses tokens such as `%H` to place specific parts of the time date in a specific format.
For example, if you enter the following in a Python shell you'll get the current GMT (UTC) time output.
python ```
from time import strftime, gmtime
strftime("%H:%M:%S", gmtime())

```

The `%H`, `%M` and `%S` tokens tell `strftime` to insert the hours (24 hour, zero padded), minutes (zero padded) and seconds (zero padded) into the string.
You can read more about format codes for `strftime` [in the Python documentation](https://docs.python.org/3/library/datetime.html?highlight=strftime#strftime-and-strptime-format-codes).
For local time, you can use the `localtime` method instead of `gmtime`.
python ```
from time import strftime, localtime
strftime("%H:%M:%S", localtime())

```

This adjusts to your computers local time settings and should output the same time displayed on your computer's clock.
If you're used to working with `datetime` objects, every `datetime` has a `.strftime()` method, which uses the same format strings and returns the same output. For example, the following will give the same output as the `localtime` example above.
python ```
from time import strftime
from datetime import datetime
datetime.now().strftime("%H:%M:%S")

```

## Updating our app time display
To pass our formatted time string from Python to QML we can use QML properties. First, let's define a property on our QML `ApplicationWindow` called `currTime`. Update your QML code in `main.qml` as follows:
**_main.qml_**
qml ```
...
ApplicationWindow {
  ...
  title: "Clock"
  property string currTime: "00:00:00"
  ...

```

The `...` marks indicate where existing code should be left as it is.
Next, modify the text object to use the `currTime` property as its `text` value. When the `currTime` property is modified the text label will update automatically (along with any other places it is used).
**_main.qml_**
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
qml ```
...
      Text {
        ...
        text: currTime // used to be; text: "16:38:33"
        font.pixelSize: 48
        color: "white"
      }
...

```

Finally, we need to send the _current time_ , stored in the `curr_time` variable, from our Python code through to QML. Modify the Python code to add the time formatting code, using `localtime()` and then set this property onto the QML object. The following code will set the QML property `currTime` to value of the Python variable `curr_time`.
**_main.py_**
python ```
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from time import strftime, localtime
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')
# Pass the current time to QML.
curr_time = strftime("%H:%M:%S", localtime())
engine.rootObjects()[0].setProperty('currTime', curr_time)
sys.exit(app.exec())

```

The code `engine.rootObjects()[0]` gets all the root objects from the QML engine as a list. Our `ApplicationWindow` object is a _root_ object because it appears at the top of the hierarchy. Next we use `[0]` to select the first item in that list -- in our case, there is only one item, our `ApplicationWindow` and that is what is returned. The `.setProperty` method is then called on that object.
If you run the application now, you should see the correct time displayed in the window. This means the time will be correct when the application starts -- try closing it and re-running it to see the time update. But you'll notice that the time doesn't update yet -- we'll do that next.
![The correct time \(at least it was when I took the screenshot\)](https://www.pythonguis.com/static/tutorials/qt/first-qml-project/screenshot-bg-correct-time.png) _The correct time (at least it was when I took the screenshot)_
## Updating the time using timers
To update the timer we need to run our time fetching and formatting code on a regular interval (every second). There are two options for implementing this
  1. using a timer which fires every 1/10th second triggering our time method
  2. using a long-running thread, which calculates the time with a delay (sleep) between each update


In Qt timers are handled on the GUI thread main loop, meaning that each time the timer is triggered the GUI is blocked while the function is executed. If that function is long running this can become noticeable in the UI. In that case, using a thread makes more sense. But here, our time fetching and formatting code is very quick -- there will be no noticeable delay. For that reason, in this example we'll use a simple timer.
### setProperty
Based on the code we have so far, the simplest approach to updating the time automatically is to just take our update code, wrap it inside a function and then call that function repeatedly using a timer. The following code shows this approach in action, using a `QTimer` with an interval of 100 msecs (1/10th second).
**_main.py_**
python ```
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QTimer
from time import strftime, localtime
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')
def update_time():
  # Pass the current time to QML.
  curr_time = strftime("%H:%M:%S", localtime())
  engine.rootObjects()[0].setProperty('currTime', curr_time)
timer = QTimer()
timer.setInterval(100) # msecs 100 = 1/10th sec
timer.timeout.connect(update_time)
timer.start()
sys.exit(app.exec())

```

If you run this you'll see the time updating correctly.
You may also notice that when the application is first run the time displays as '00:00:00' (the default value) for a second. That is because the UI is rendered before the first interval timer executes. You can avoid this by adding a call to `update_time()` just before `app.exec()` is called, e.g.
  * PyQt
  * PySide


python ```
update_time() # initial startup
sys.exit(app.exec())

```

python ```
update_time() # initial startup
sys.exit(app.exec_())

```

Now, when the app launches it will be showing the correct time immediately.
### Using signals
While this approach of setting properties from the Python code works well for this small example it's not ideal as your applications grow in size. By hooking your Python code to change specific properties in your QML you are tying your Python code to the structure of the UI. That makes it easy to break things when restructuring your applications. Just like in the Qt Widgets API you can use Qt signals to avoid this problem: your code can emit signals without needing to know where they will be received, or how they will be used -- and you can even hook a single signal up to multiple receivers. This keeps your logic and UI code nicely decoupled.
If you're not familiar with Qt signals, take a look at our [Signals, Slots & Events tutorials](https://www.pythonguis.com/signals-slots-events/).
Let's rework our example to make use of Qt signals in Python & QML to achieve the same result.
First we must define our signals in the `main.py` file. Signals can only be defined on objects that are subclassed from `QObject` so we'll need to implement a small class. This is also a logical place to put our time-handling code to keep things nicely self-contained. We'll also define our signal for passing the current time to QML.
Multiple signals can be handled under a single `QObject` class and it often makes sense to use a single class for simplicity.
**_main.py_**
python ```
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QTimer, QObject, pyqtSignal
from time import strftime, localtime
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')

class Backend(QObject):
  updated = pyqtSignal(str, arguments=['time'])
  def __init__(self):
    super().__init__()
    # Define timer.
    self.timer = QTimer()
    self.timer.setInterval(100) # msecs 100 = 1/10th sec
    self.timer.timeout.connect(self.update_time)
    self.timer.start()
  def update_time(self):
    # Pass the current time to QML.
    curr_time = strftime("%H:%M:%S", localtime())
    self.updated.emit(curr_time)

# Define our backend object, which we pass to QML.
backend = Backend()
engine.rootObjects()[0].setProperty('backend', backend)
# Initial call to trigger first update. Must be after the setProperty to connect signals.
backend.update_time()
sys.exit(app.exec())

```

While this looks like a lot of changes, the majority of the code is exactly the same, just reorganized to put everything under the container class. Everything in `__init__` will be run when we create an instance of the `Backend` class using `backend = Backend()`.
The signal definition (repeated below) creates a signal which accepts a single parameter -- a string. This will be sent with the signal to the receivers. The `arguments=` parameter is used to define the names under which the arguments will be known in QML (if using keyword arguments).
  * PyQt
  * PySide


python ```
  updated = pyqtSignal(str, arguments=['time'])

```

python ```
  updated = Signal(str, arguments=['time'])

```

You'll also notice that we pass our `backend` object through to a QML property (also named `backend`). This allows the signal we've just implemented to be used from the QML code and hooked up to an appropriate target.
python ```
engine.rootObjects()[0].setProperty('backend', backend)

```

As before we need to implement the property in QML which these will set. Previously when defining our property to receive the formatted time string, we used a `string` type. This isn't appropriate for the `Backend` object, as it's not a string. To receive the `Backend` object (which is a `QObject`) from Python we need to use the `QtObject` type.
**_main.qml_**
qml ```
...
property string currTime: "00:00:00"
property QtObject backend
...

```

There are not that many types. QML converts python base types into `bool`, `int`, `double`, `string`, `list`, `QtObject` and `var`. The `var` type is a generic handler which can handle any Python type.
To receive the signal itself, we need to define a `Connections` object, setting it's `target` as our `backend` property (in QML).
**_main.qml_**
qml ```
ApplicationWindow {
  ...
  Connections {
    target: backend
  }
  ...
}

```

We can now implement any other logic we like inside this `Connections` object to handle the signals on the `backend` object. Let's create a signal handler to handle our `updated` signal. Signal handlers are automatically named using the capitalized form of the signal name we chose in Python, preceded by lowercase `on`. Underscores and existing capitalization are ignored.
Python name | QML name  
---|---  
mySignal | onMySignal  
mysignal | onMysignal  
my_signal | onMy_signal  
**_main.qml_**
qml ```
ApplicationWindow {
  ...
  Connections {
  target: backend
  function onUpdated(msg) {
    currTime = msg;
  }
  ...
}

```

The above code shows the signal handler for the `updated` signal, named `onUpdated`. This receives the current time as a string (named `msg`) and sets that onto the QML property `currTime`. As before, setting this property automatically updates the associated text label.
If you run the application now, you'll see the time updating exactly the same as before!
We could replace the Python time formatting with formatting code in Javascript inside QML if we wanted and send a timestamp as a signal. In fact, you can get the time and define timers in QML too!
## Removing the window decorations
To create a desktop-widget like application you can hide the window decorations on your QML app. This removes the title bar and buttons for closing/minimizing the app. However, you can still close the window from the taskbar if you need to. Make the following changes to the top of the QML file, setting the `flags` property and positioning the widget into the bottom right of the display.
**_main.qml_**
qml ```
...
ApplicationWindow {
  visible: true
  width: 400
  height: 600
  x: screen.desktopAvailableWidth - width - 12
  y: screen.desktopAvailableHeight - height - 48
  title: "Clock"
  flags: Qt.FramelessWindowHint | Qt.Window
...

```

The code sets `x`, `y` for the window and adds the flag `Qt.FramelessWindowHint` to make the window frameless. The `Qt.Window` flag ensures that even though the window is frameless, we still get an entry on the taskbar. Run it, and you will see the window we've created.
![The final view with the updating clock and no window decorations](https://www.pythonguis.com/static/tutorials/qt/first-qml-project/screenshot-final-no-decorations.png) _The final view with the updating clock and no window decorations_
In the next tutorial we'll expand on this simple clock by using image manipulations, transitions and animations to build a fully-functional analog clock.
## The complete final code
Below is the complete final code for PyQt5.
**_main.py_**
python ```
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QTimer, QObject, pyqtSignal
from time import strftime, localtime
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')

class Backend(QObject):
  updated = pyqtSignal(str, arguments=['time'])
  def __init__(self):
    super().__init__()
    # Define timer.
    self.timer = QTimer()
    self.timer.setInterval(100) # msecs 100 = 1/10th sec
    self.timer.timeout.connect(self.update_time)
    self.timer.start()
  def update_time(self):
    # Pass the current time to QML.
    curr_time = strftime("%H:%M:%S", localtime())
    self.updated.emit(curr_time)

# Define our backend object, which we pass to QML.
backend = Backend()
engine.rootObjects()[0].setProperty('backend', backend)
# Initial call to trigger first update. Must be after the setProperty to connect signals.
backend.update_time()
sys.exit(app.exec())

```

**_main.qml_**
qml ```
import QtQuick 2.15
import QtQuick.Controls 2.15
ApplicationWindow {
  visible: true
  width: 400
  height: 600
  x: screen.desktopAvailableWidth - width - 12
  y: screen.desktopAvailableHeight - height - 48
  title: "Clock"
  flags: Qt.FramelessWindowHint | Qt.Window
  property string currTime: "00:00:00"
  property QtObject backend
  Rectangle {
    anchors.fill: parent
    Image {
      sourceSize.width: parent.width
      sourceSize.height: parent.height
      source: "./images/background.png"
      fillMode: Image.PreserveAspectCrop
    }
    Rectangle {
      anchors.fill: parent
      color: "transparent"

      Text {
        anchors {
          bottom: parent.bottom
          bottomMargin: 12
          left: parent.left
          leftMargin: 12
        }
        text: currTime // used to be; text: "16:38:33"
        font.pixelSize: 48
        color: "white"
      }
    }
  }
  Connections {
    target: backend
    function onUpdated(msg) {
      currTime = msg;
    }
  }
}

```

Now you have your basic QML application, you should experiment with customizing and changing the behavior. Try changing the background image, modifying the text color or sending different (or multiple bits) of information from Python to your app.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt5](https://www.pythonguis.com/static/theme/images/products/pyqt5-book.png)](https://www.pythonguis.com/pyqt5-book/)
[Take a look ](https://www.pythonguis.com/pyqt5-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/create-simple-gui-applications/) and [Amazon Paperback](https://www.amazon.com/dp/B08RB2HRS1/)
Mark As Complete 
Continue with [ PyQt5 Tutorial ](https://www.pythonguis.com/tutorials/qml-animations-transformations/ "Continue to next part")
Return to [Create Desktop GUI Applications with PyQt5 ](https://www.pythonguis.com/pyqt5-tutorial/)
[![Amoh Gyebi Ampofo](https://www.pythonguis.com/static/theme/images/authors/amoh-gyebi-ampofo.jpg)](https://www.pythonguis.com/authors/amoh-gyebi-ampofo/)
**Create Applications with QtQuick in PyQt5** was written by [Amoh-Gyebi Ampofo](https://www.pythonguis.com/authors/amoh-gyebi-ampofo/) . 
Amoh is a Python GUI developer from Ghana. 
**Create Applications with QtQuick in PyQt5** was published in [tutorials](https://www.pythonguis.com/tutorials/) on April 07, 2021 (updated April 04, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[python](https://www.pythonguis.com/topics/python/) [ qml](https://www.pythonguis.com/topics/qml/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [desktop-application](https://www.pythonguis.com/topics/desktop-application/) [qtquick](https://www.pythonguis.com/topics/qtquick/) [clock](https://www.pythonguis.com/topics/clock/) [qt](https://www.pythonguis.com/topics/qt/) [ getting-started](https://www.pythonguis.com/topics/getting-started/) [ pyqt5-getting-started](https://www.pythonguis.com/topics/pyqt5-getting-started/) [ pyqt5-qml](https://www.pythonguis.com/topics/pyqt5-qml/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
