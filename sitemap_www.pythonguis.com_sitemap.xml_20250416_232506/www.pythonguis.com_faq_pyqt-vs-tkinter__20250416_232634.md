# Content from: https://www.pythonguis.com/faq/pyqt-vs-tkinter/

[](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#menu)
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
# PyQt vs. Tkinter — Which Should You Choose for Your Next GUI Project?
What Are the Major Differences Between these Popular Python GUI Libraries
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 08 [ FAQ ](https://www.pythonguis.com/faq/)
Graphical User Interfaces (GUIs) allow users to interact with software through intuitive and user-friendly graphical elements such as buttons, icons, text boxes, and windows. GUIs provide a simple way to perform complex tasks and navigate a software system using the mouse and keyboard and without needing to remember complex commands. By using familiar visual concepts across different tools and platforms, GUIs help make new software feel intuitive and user-friendly, even for beginners.
While Python is more commonly used for command-line tools, data science, and web apps, it is also perfectly capable of building graphical desktop applications. The Python ecosystem makes it possible to build almost anything, from small user-friendly interfaces for your scripts to more complex data analysis or engineering tools. Whether you're a Python beginner or a seasoned developer, learning how to build GUI apps with Python is an excellent addition to your skill set.
Table of Contents
  * [An Introduction to Python GUI Libraries in Python](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#an-introduction-to-python-gui-libraries-in-python)
  * [The Tkinter GUI Library](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#the-tkinter-gui-library)
    * [How Do You Install Tkinter?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#how-do-you-install-tkinter)
    * [How Can You Write a Tkinter App?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#how-can-you-write-a-tkinter-app)
    * [What Is Tkinter Commonly Used for?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#what-is-tkinter-commonly-used-for)
    * [Is Tkinter Outdated?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#is-tkinter-outdated)
    * [Why Does Tkinter Look Old-Fashioned?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#why-does-tkinter-look-old-fashioned)
    * [How Can You Design GUIs for Tkinter?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#how-can-you-design-guis-for-tkinter)
    * [What Are Tkinter's Pros & Cons?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#what-are-tkinters-pros-cons)
  * [The PyQt GUI Framework](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#the-pyqt-gui-framework)
    * [How Do You Install PyQt?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#how-do-you-install-pyqt)
    * [How Can You Write a PyQt App?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#how-can-you-write-a-pyqt-app)
    * [What Is PyQt Commonly Used for?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#what-is-pyqt-commonly-used-for)
    * [Can You Use PyQt for Open-Source and Commercial Apps?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#can-you-use-pyqt-for-open-source-and-commercial-apps)
    * [How Can You Design GUIs for PyQt Apps?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#how-can-you-design-guis-for-pyqt-apps)
    * [What Are PyQt's Pros and Cons?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#what-are-pyqts-pros-and-cons)
  * [Tkinter vs. PyQt: A Feature Comparison](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#tkinter-vs-pyqt-a-feature-comparison)
  * [Decision Time: How to Choose the Best GUI Library for Your Project](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#decision-time-how-to-choose-the-best-gui-library-for-your-project)
    * [What Are Your Goals?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#what-are-your-goals)
    * [Do You Need a GUI Library or a GUI Framework?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#do-you-need-a-gui-library-or-a-gui-framework)
    * [Is Tkinter Easier to Learn Than PyQt?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#is-tkinter-easier-to-learn-than-pyqt)
    * [Which One Should You Learn First, Tkinter or PyQt?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#which-one-should-you-learn-first-tkinter-or-pyqt)
  * [What Next?](https://www.pythonguis.com/faq/pyqt-vs-tkinter/#what-next)


## An Introduction to Python GUI Libraries in Python
One of Python's core strengths is the rich ecosystem of libraries and frameworks available. GUI programming libraries are not an exception -- you'll find [several GUI libraries for Python](https://www.pythonguis.com/faq/which-python-gui-library/).
While having multiple choice is great, it means that if you want to learn how to write GUI applications with Python, the first question you will need to answer is -- _Which library should I use?_
Even though many GUI libraries are available, none has the widespread adoption of [Tkinter](https://www.pythonguis.com/topics/tkinter-foundation/) and [PyQt](https://www.pythonguis.com/pyqt6/). So, if you're starting with GUI programming in Python, it'll make sense to start with one of these. There are far more tutorials, help & resources available to get you up and running, and you're more likely to find help if you need it.
![Google Trends Plot Ranking Tkinter, PyQt, and Other Python GUI Libraries](https://www.pythonguis.com/static/faq/tkinter-vs-pyqt/google-trends-plot-tkinter-vs-pyqt.png) _Google Trends Plot Ranking Tkinter, PyQt, and Other Python GUI Libraries_
The popularity of Tkinter largely stems from it being bundled with Python and, therefore, being the _default_ Python GUI library. Most beginners will find this library first. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
PyQt is often seen as the next logical step in your GUI journey when you want to start building real applications or commercial-quality software with Python.
Whether you choose Tkinter or PyQt will largely depend on your goals for writing GUI applications.
In this article, we'll explore and compare **Tkinter** and **PyQt**. We'll assess their pros & cons for different use cases and help you decide which library to use for _your_ project.
## The Tkinter GUI Library
_**Best for** simple tool GUIs, small portable applications_.
Tkinter is the default GUI library for Python. It comes bundled with Python on both Windows and macOS. On Linux, you may have to install additional packages to get it set up.
The library is a wrapper around the [Tcl/Tk GUI toolkit](https://www.tcl.tk/). Its name is an amalgamation of the words Tk and Interface.
Tkinter supports standard layouts and basic widgets, as well as more complex widgets, such as tabbed views & progress bars. Tkinter is a pure GUI library rather than a GUI framework. It only provides a set of graphical components for building GUIs.
It doesn't provide support for GUIs-driven data sources, databases, or for displaying or manipulating multimedia or hardware. However, if you need to make something simple that doesn't require any additional dependencies, Tkinter may be what you are looking for.
Tkinter is a cross-platform GUI library. It was first released in 1990, and it has continued to evolve until today. For example, the addition of the _Themed Tk_ extensions in 2009 improved the appearance of widgets, giving a native look & feel to your Tkinter GUIs.
Tkinter is a limited library with a friendly [API (application programming interface)](https://en.wikipedia.org/wiki/API) that makes it easy to understand and learn. Because of this, Tkinter tends to be the first choice for creating quick GUIs for relatively small Python programs.
To learn more about how to use Tkinter, check out [Build your own desktop apps with Python & Tkinter](https://www.pythonguis.com/tkinter-tutorial/).
### How Do You Install Tkinter?
Tkinter comes installed by default with Python on macOS and Windows. On some Linux systems, you may need to [install an additional package](https://www.pythonguis.com/installation/install-tkinter-linux/). Tkinter also runs fine on a Raspberry Pi, although depending on your distribution, you may need to [install it first](https://www.pythonguis.com/installation/install-tkinter-linux/).
### How Can You Write a Tkinter App?
A minimal _Hello, World!_ GUI application in Tkinter will look something like this:
python ```
import tkinter as tk
# Create the app's main window
window = tk.Tk()
window.title("Hello, World!")
def handle_button_press():
  window.destroy()
button = tk.Button(text="My simple app.", command=handle_button_press)
button.pack()
# Start the event loop
window.mainloop()

```

In this example, we first import `tkinter` as `tk`, a common practice when using Tkinter. We then create our app's main window by instantiating the `Tk` class. The `title()` method allows us to give a descriptive title to the app's windows. Next we write a function to responding to a click on the button. In this case our method closes the application window & terminates it.
To create the button, we use the `Button` class with an appropriate text. In order to trigger our `handle_button_press()` function when the button is pressed, we pass the function to `Button` as the _command_ argument.
Next, we call `pack()` on our button object. This organizes our widget into the window layout -- although in this case, there is only a single widget. Finally, we run the app by calling `mainloop()` on our `window` object.
If you run the example, you'll see a simple window like follows.
![A Tkinter App Using Tk Standard Widgets](https://www.pythonguis.com/static/faq/tkinter-vs-pyqt/tkinter-demo-app.png) _A Tkinter App Using Tk Standard Widgets_
As you can see, by default, Tkinter has very rudimentary-looking widgets.
We can modify the example to use Themed Tk widgets, which give a native appearance to widgets. The changes are minor, adding a `from tkinter import ttk` import and using `ttk.<Widget>` when constructing widgets.
python ```
import tkinter as tk
from tkinter import ttk
# Create the app's main window
window = tk.Tk()
window.title("Hello, World!")
def handle_button_press():
  window.destroy()
button = ttk.Button(text="My simple app.", command=handle_button_press)
button.pack()
# Start the event loop
window.mainloop()

```

If you run this example, the simple window will appear again but now using platform-native widgets (what you see will depend on your own system).
![A Tkinter App Using Themed Tk Widgets](https://www.pythonguis.com/static/faq/tkinter-vs-pyqt/tkinter-demo-app-ttk-theme.png) _A Tkinter App Using Themed Tk Widgets_
### What Is Tkinter Commonly Used for?
Tkinter is typically used for simple GUIs. For example, small proof-of-concept, research, or educational apps built by Python hobbyists, and the like. The non-native appearance of Tkinter apps and lack of a real application framework make this library unsuitable for building professional applications, particularly commercial software.
While it's possible to put something simple together with Tkinter, as your application grows or your requirements become more complex, you'll likely end up spending more time reinventing the wheel than you saved by using a "simple" system. So, if you expect your project to grow in the future, then you should start with PyQt instead.
### Is Tkinter Outdated?
The complaints of Tkinter being outdated largely stem from how the apps built with the library look on modern systems compared to other apps. Another important complaint driver is the library's limited set of widgets.
Tk, the library around which Tkinter was built, was first released in 1991. However, it's been continuously developed & maintained. In 2009, Tkinter added support for Tk 8.5 "Themed Tk" (Ttk), which allows Tk widgets to be more easily themed to _look like_ the native on different desktop environments. Ttk also added some additional widgets, such as combo boxes, progress bars, tree views, notebooks, separators, and size grips, which weren't available in default Tk.
### Why Does Tkinter Look Old-Fashioned?
It doesn't have to! Tkinter's reputation for looking _bad_ stems from earlier versions of Tk without the native platform-theming support. These early versions used an old cross-platform "Motif" style, which was blocky and a bit ugly.
Tk 8.5 added support for desktop native theming, so your applications now follow the style of the desktop they are running on. This new look is provided through Themed Tk, which was added to Tkinter in 2009.
If you don't want a native appearance but still want to improve how your Tkinter applications look, there are other options too. For example, [Tkinter Designer](https://github.com/ParthJadhav/Tkinter-Designer) allows you to design graphical interfaces using [Figma](https://www.figma.com/). Once you have the interface ready, then you can export it into a working Tkinter app.
### How Can You Design GUIs for Tkinter?
There isn't an official design tool for Tkinter GUIs. However, you can find some tools available online. For example, [Visual Tk](https://visualtk.com/) allows you to build a GUI using a drag-drop interface in your browser & will then generate the Python code for you to create the interface in Tkinter itself.
Alternatively, [Tkinter Designer](https://github.com/ParthJadhav/Tkinter-Designer) will take a design drawn in the Figma software and use it to build a Tkinter-based GUI.
### What Are Tkinter's Pros & Cons?
You can find plenty of reasons to consider Tkinter for your next project and reasons you may want to try something else. Let's take a look at some of the pros & cons of using Tkinter to build GUI applications with Python so that you can be in a better position to decide.
The pros of using Tkinter include the following:
  * It is part of the Python standard library and comes installed by default (on Windows and macOS). Once you install Python, you're ready to start building GUIs with Tkinter.
  * It doesn't have additional dependencies for your applications unless you need third-party libraries for additional functionality.
  * It is relatively simple, meaning there isn't much to take in while learning to use it.
  * It is a cross-platform library
  * It has a lot of documentation and tutorials available.
  * It can be used freely for commercial software because its license is the same as Python's.


On the other hand, the cons of using Tkinter include the following:
  * It doesn't come with advanced widgets, such as data-driven views, database interfaces, vector graphics canvas, or multimedia GUI elements. To implement any of these in your applications, you need to write them yourself. This is achievable but will add to your development & maintenance burden.
  * It has no official GUI designer application. You'll find a few third-party options available with varying degrees of completeness and flexibility.
  * It lacks bundled features, which means that you're more likely to need third-party libraries to complete your applications. Luckily, there is no shortage of those in the Python ecosystem!
  * It doesn't have a native look & feel by default. The default appearance of Tkinter applications is old-fashioned. However, this is largely fixed by the Themed Tk extensions.


Now that you have a better idea of what Tkinter is and what are its main features and limitations, it's time for you to know its closest competitor, PyQt.
## The PyQt GUI Framework
_**Best for** desktop applications, multimedia, scientific, and engineering software._
PyQt is a Python GUI framework built around the C++ Qt framework, which is developed and maintained by the Qt Company. It allows us to create modern interfaces that look right at home on any platform, including Windows, macOS, Linux, and even Android. It also has solid tooling, with the most notable being [Qt Creator](https://www.pythonguis.com/faq/why-is-the-qt-creator-used-in-the-tutorial/), which includes a WYSIWYG editor for designing GUI interfaces quickly and easily.
PyQt is developed and maintained by Riverbank Computing and was first released in 1998, four years after Tkinter.
The free-to-use version of PyQt is licensed under [GNU General Public License (GPL) v3](https://www.gnu.org/licenses/gpl-3.0.en.html). This means that PyQt is limited to GPL-licensed applications unless you purchase its [commercial license](https://www.riverbankcomputing.com/commercial/buy).
The Qt Company has its own Python binding for Qt, which is called PySide. This library was released in 2009. The main difference between PyQt and PySide is in licensing. PySide is licensed under GNU Lesser General Public License (LGPL), which means that you use PySide in non-GPL applications without any additional fee.
Qt, and by extension PyQt, is not just a GUI library. It's a complete GUI application development framework. In addition to standard GUI components, such as widgets and layouts, Qt provides:
  * [MVC (model-view-controller)](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) data-driven views (spreadsheets, tables)
  * Database interfaces and models
  * Graph plotting
  * Vector graphics visualization
  * Multimedia playback
  * Sound effects and playlists
  * Interfaces for hardware, such as printing devices


Qt's signals and slots mechanism for event programming allows us to properly architect complex applications from reusable and isolated components.
To learn more about how to use PyQt, check out [Build your own desktop apps with Python & PyQt6](https://www.pythonguis.com/pyqt6-tutorial/).
While other toolkits can work great when building small Python tools, PyQt really comes into its own for building commercial-quality applications where we benefit from the pre-built components. These benefits come at the expense of a steep learning curve but don't feel overwhelmed yet, you can just focus on the parts your project needs.
PyQt-based applications use platform-native widgets to ensure that they look and feel native on Windows, macOS, and Qt-based Linux desktop environments.
### How Do You Install PyQt?
PyQt v6.4.2 is the latest version of the library. To run it on your computer, make sure you have Python v3.6.1 or later installed. To install it, just run the following command:
sh ```
$ python -m pip install pyqt6

```

This command will install the PyQt6 library for your platform and your version of Python. The library will be automatically downloaded from [PyPI](https://pypi.org/project/PyQt6/).
If you want to use Qt's own _official_ Python library, you can install PySide with `python -m pip install pyside6`
As of writing, only [PyQt5](https://www.pythonguis.com/pyqt5/) is currently supported on Raspberry Pi. But you can use both the Qt Widgets (standard) and QML/Qt Quick (declarative) APIs. You can use QML to build modern touchscreen interfaces with animations, transitions, and effects.
To install PyQt5 on a Raspberry Pi, run the following command:
sh ```
$ sudo apt-get install python3-pyqt5

```

This command will install PyQt5 from your Raspberry Pi current repository. Note that the Qt framework will also be installed as a dependency.
For other installation options, see [our complete installation guides](https://www.pythonguis.com/installation/).
### How Can You Write a PyQt App?
A minimal _Hello, World!_ GUI application in PyQt6, using the Qt Widgets is shown below:
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
python ```
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# Create the app's main window
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Hello, World!")
    button = QPushButton("My simple app.")
    button.pressed.connect(self.close)
    self.setCentralWidget(button)
    self.show()
# Create the app, the main window, and run the app
app = QApplication([])
window = MainWindow()
app.exec()

```

In this example, we first import the required classes from `PyQt6.QtWidgets`. We then define the `MainWindow` class, which will provide the app's main window. The window will have a title and a button. This button is connected to the `close()` method inherited from `QMainWindow`.
Finally, we instantiated `QApplication` and `MainWindow`. To run the application, we call the `exec()` method on the `app` instance.
When run, you'll get a window with the title "Hello, World!" and containing a single push button that says "My simple app."
![A Windowed App With a Push Button](https://www.pythonguis.com/static/faq/tkinter-vs-pyqt/pyqt-demo-app.png) _A Windowed App With a Push Button_
That's a very simple example. To showcase the real capabilities of PyQt and the Qt framework, below is a more complex example consisting of a minimal but working web browser:
python ```
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication, QMainWindow
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.browser = QWebEngineView()
    self.browser.setUrl(QUrl("https://www.google.com"))
    self.setCentralWidget(self.browser)
    self.show()
app = QApplication([])
window = MainWindow()
app.exec()

```

To make this code work, you need the Qt WebEngine extensions. This is a core part of Qt's library but is installed separately due to its size. Run the following to install this from the command line.
bash ```
pip install PyQt6-WebEngine

```

With `PyQt6-WebEngine` installed, you can now use the `QWebEngineView` class in your own applications.
If you run the code above, you'll get a minimal web browser that loads up Google & lets you browse from there.
![A Minimal Web Browser, Written in PyQt](https://www.pythonguis.com/static/faq/tkinter-vs-pyqt/pyqt-webbrowser.png) _A Minimal Web Browser, Written in PyQt_
For a final example, we'll create a quick video player. This example uses layouts to build a simple GUI with a viewer and a button. You can press the button to launch a platform native file picker dialog:
python ```
from PyQt6.QtCore import QSize, QUrl
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtWidgets import (
  QApplication,
  QFileDialog,
  QPushButton,
  QVBoxLayout,
  QWidget,
)
class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Video Player")
    self.viewer = QVideoWidget()
    self.viewer.setMinimumSize(QSize(800, 400))
    self.player = QMediaPlayer()
    self.loadVideoBtn = QPushButton("Open video file...")
    self.loadVideoBtn.pressed.connect(self.openVideFile)
    layout = QVBoxLayout()
    layout.addWidget(self.viewer)
    layout.addWidget(self.loadVideoBtn)
    self.setLayout(layout)
  def openVideFile(self):
    filename, _ = QFileDialog.getOpenFileName(
      self,
      caption="Open video file",
      filter="MP4 Video (*.mp4)",
    )
    if filename:
      video = QUrl(filename)
      self.player.setSource(video)
      self.player.setVideoOutput(self.viewer)
      self.player.play()
app = QApplication([])
window = Window()
window.show()
app.exec()

```

When you run this example you'll get a very basic video player that's capable of loading and playing videos in MP4 format.
![A Minimal MP4 Video Player, Written in PyQt](https://www.pythonguis.com/static/faq/tkinter-vs-pyqt/pyqt-video-player.png) _A Minimal MP4 Video Player, Written in PyQt_
The above examples should give you an idea of how powerful PyQt actually is. As you can see, there is much more to it than just a set of simple GUI widgets.
For some more demo PyQt applications, [see our library of examples](https://www.pythonguis.com/examples/).
### What Is PyQt Commonly Used for?
PyQt is most commonly used for, and particularly well suited for, building full-featured GUI desktop applications. As you already learned, PyQt supports (MVC-like) data-driven views, vector graphics, animations & transitions, databases, and threading/concurrency.
Qt Designer, the GUI creator provided by Qt, allows you to build professional quality software in no time. The signals and slots mechanism makes it possible to properly decouple the components of an application, allowing for robust and maintainable system architectures.
You can also use PyQt for building touchscreen user interfaces for Raspberry Pi-powered hardware -- both using the Qt Widgets and QML/Qt Quick APIs. While PyQt can technically be used to build apps for mobile devices, this type of apps is rarely seen outside of the hobbyist space.
### Can You Use PyQt for Open-Source and Commercial Apps?
Yes, you can! PyQt is free to use for personal development and GPL-licensed open-source software. For non-GPL software, such as commercially licensed software, a license is required from Riverbank Computing.
The Qt for Python framework ---PySide--- by the Qt Company is licensed under the LGPL. If you use PySide, then you don't need to license your software under the GPL (or LGPL). As a result, you don't have to share your application's source code. So, if you don't want to buy a commercial license for PyQt, then you can use PySide, which [doesn't require a license for use in commercial software](https://www.pythonguis.com/faq/pyqt6-vs-pyside6/).
### How Can You Design GUIs for PyQt Apps?
The Qt framework provides Qt Designer, which is a drag-drop UI editor. You can use Qt Designer to design modern and intuitive interfaces for your PyQt applications quickly. The interfaces generated using Qt Designer can be either loaded as-is in your applications or converted to Python code that you can then import into your apps.
On Windows, you can install Qt Designer and other Qt tools by using `pip` as follows:
bash ```
$ python -m pip install pyqt6-tools

```

This command installs Qt Designer from PyPI. To run the GUI editor, you can execute the `designer.exe` app from your `Script` directory.
If you use PySide, then Qt Designer will be installed by default with the library.
Finally, you can also build GUIs from scratch using Python code. Whether you use Qt Designer or code is entirely up to you. The best choice will largely depend on your project.
### What Are PyQt's Pros and Cons?
There are a number of reasons you may want to choose PyQt for your project and reasons you may not. Let's take a look at some of the pros and cons of using PyQt to build GUI applications with Python.
To kick things off, let's start with the pros:
  * It is a powerful & modern GUI framework that is suitable for building professional applications.
  * It includes several advanced widgets, including data-driven views, charts, database interfaces, vector graphics canvas, video playback, and a fully-functional web browser component.
  * It can take advantage of Qt Designer, which allows you to design GUIs using a graphical drag-and-drop editor.
  * It is cross-platform and can run on Windows, Linux, macOS, and mobile devices.
  * It provides modern and native-looking GUI components out of the box in all the major platforms. These components can be largely customized if required.
  * It is a batteries-included library, which means that you can accomplish many things with PyQt directly. This characteristic means less need for third-party dependencies.
  * It has plenty of support and online learning resources, including our own complete [PyQt tutorial](https://www.pythonguis.com/pyqt6-tutorial/).
  * It allows the creation of touchscreen interfaces with the QML/Qt Quick API.


Even though PyQt has many neat features and advantages, it also has some cons:
  * It can be intimidating to beginners. The size of the library and its complex feature set can make it overwhelming, to begin with.
  * It has poor and incomplete Python [documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html). As an alternative, you can use the official Qt documentation. However, this documentation is for the C++ library and can be hard to translate.
  * It will take time to fully learn the framework and how it works.
  * It allows for a GPL or commercial license only.


Up to this point, you've learned a lot about Tkinter and PyQt. To make your life more pleasant, the following section provides a quick and summarized comparison between these two GUI tools.
## Tkinter vs. PyQt: A Feature Comparison
Now that we have a good understanding of Tkinter and PyQt, let's put them head-to-head on some key features:
Feature | Tkinter | PyQt  
---|---|---  
Installation & Setup | It's part of the Python installer on Windows and macOS. It may require additional packages on Linux. | It needs to be installed separately using `pip`. It can also be installed from the source.  
License | It uses the Python license. | It uses GPL or a commercial license.  
GUI Builder Tools | It has no standard GUI builder app, but some third-party tools are available. | It can use Qt Designer for building GUIs.  
Widgets Set | It has a basic set of widgets for most common applications. | It has basic and advanced widgets for building quite complex interfaces.  
Application framework | It's not a framework, so you'll have to use third-party Python libraries to implement many features. | It's a full GUI framework that includes databases, plotting, vector graphics, threading, multimedia, networking, and more.  
As you can see, PyQt is the most feature-rich of the two libraries. It is more capable of both building the GUI and the backend of your application. That said, if you're building simple GUI tools, then Tkinter may still be more than enough. It'll all depend on your project.
## Decision Time: How to Choose the Best GUI Library for Your Project
So far, we've looked in detail at each library, seen some example code, and explored the pros and cons of using each library. We've also addressed some common questions that come up when looking at the two libraries.
By now, you have everything you need to decide which is best for your project. However, you may still be stuck on making the decision. In the following sections, we'll recap what we've learned about PyQt and Tkinter in the context of your own project and goals.
### What Are Your Goals?
Which GUI library you pick is heavily dependent on your goals in writing GUI applications. If you are learning Python and just want to experiment, then Tkinter is a perfectly decent way to do that. On the other hand, if you are learning GUI development with a view to building professional applications, then it will make more sense to start with PyQt.
Qt, which PyQt is built on, is a complete GUI application framework that provides tools and components for building modern applications. This feature offloads a lot of the manual and repetitive work, helping you build well-architected systems.
Take, for example, loading a CSV file and displaying it in a table. In PyQt, you can write a small model to interface between the data source and the built-in table view. PyQt does all the work for you. It takes the data and displays it in an efficient way.
In Tkinter, you will need to create the table by yourself, widget by widget, in a grid layout. Then, you would have to use some external tool for loading the data from the CSV file. Finally, you would have to find a way to display the data in your custom Tkinter table.
In PyQt, you can have millions of rows in a table without problems using a _single_ widget created to render the entire table. In Tkinter, each cell will be an individual widget object ---even those outside the view--- meaning you'll quickly encounter problems if you work with large data.
### Do You Need a GUI Library or a GUI Framework?
Tkinter is a _GUI library_ , while PyQt is a _GUI framework_. While both allow you to build graphical user interfaces, they differ in the scope of what they include and what parts of your application they help you build.
While a GUI library will help you add, position, and draw widgets in your application's GUI and hook those widgets up to your own code, a GUI framework provides additional functionalities, which are commonly required when building applications.
For example, PyQt provides components for connecting to databases and creating semi-automatic model-views of database entries. It provides a vector graphics canvas, plotting, 3D rendering, networking, threading/concurrency, and more.
Even though many of these features are already available in the Python standard library or in third-party libraries, most of them will not integrate as cleanly into a GUI program as those provided natively by the framework itself.
The trade-off is between using a single, big dependency (PyQt) vs. lots of small dependencies (standard-library or third-party) to build your apps. Using a framework can speed up the development of complex projects because much of what you need is available out of the box. As mentioned, whether you get any benefit from the PyQt framework will largely depend on your specific project.
### Is Tkinter Easier to Learn Than PyQt?
It _can_ be. Previously, there was a lack of beginner tutorials available for PyQt. This condition made it difficult to get started. That's no longer the case. Now you'll find lots of PyQt5 and PyQt6 tutorials available online.
Our own [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/) takes you from the absolute basics of GUI development concepts to building relatively complex applications. We're adding new tutorials regularly, covering both basic and advanced topics.
There are more beginner-friendly tutorials available for Tkinter than PyQt. Basic Tkinter examples tend to avoid using subclasses, while PyQt examples default to using them, which can imply more reasoning if you're not familiar with object-oriented programming and inheritance.
PyQt introduces additional and complex concepts, such as signals and slots, which can be confusing for new developers. However, they are one of the most powerful parts of the framework, making it possible to build well-architected and maintainable software. The time taken to understand these things is well rewarded.
### Which One Should You Learn First, Tkinter or PyQt?
There is little benefit in starting with Tkinter if you plan to switch to PyQt later. While PyQt is a large framework with thousands of classes and features, you don't need to learn all of it at once. While some of the basic GUI concepts you learn with Tkinter -- widgets, layouts, event-based programming -- will transfer over to PyQt, there are many other concepts that won't.
As a developer, you'll be looking for tools that are easy to use, well-designed for the job, and at the same time, can grow with your projects. If you want to move on to develop professional or commercial software with Python, you don't want to start over again with an entirely new stack. If you think you are likely to want to migrate to PyQt later, then you may as well start there first.
## What Next?
Now you have enough knowledge to make an informed decision between using PyQt or Tkinter for your GUI projects. On [Python GUIs](https://www.pythonguis.com/), we have lots of tutorials to help you take the next step of _actually building something great_!
Our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/) is pretty complete and takes you from basic examples to complex applications. This way, you'll get the required skills to build multimedia, scientific, and engineering software at a professional level.
On the other hand, if you're just looking to create simple GUIs for your automation and utility tools, then our [Tkinter tutorial](https://www.pythonguis.com/tkinter-tutorial/) will give you the basics you need to get a window on the screen and start experimenting.
In any case, you will have fun building GUIs!
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PyQt vs. Tkinter — Which Should You Choose for Your Next GUI Project?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) with contributions from [Khumbo Klein](https://www.pythonguis.com/authors/khumbo-klein/) , [Lalin Paranawithana](https://www.pythonguis.com/authors/lalin-paranawithana/) and [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyqt-vs-tkinter/Python books) on the subject. 
**PyQt vs. Tkinter — Which Should You Choose for Your Next GUI Project?** was published in [faq](https://www.pythonguis.com/faq/) on April 12, 2023 (updated April 08, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[tkinter](https://www.pythonguis.com/topics/tkinter/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [qt](https://www.pythonguis.com/topics/qt/) [upgrade](https://www.pythonguis.com/topics/upgrade/) [ licensing](https://www.pythonguis.com/topics/licensing/) [tk](https://www.pythonguis.com/topics/tk/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
