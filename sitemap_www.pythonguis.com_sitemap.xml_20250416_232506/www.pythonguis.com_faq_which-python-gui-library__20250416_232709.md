# Content from: https://www.pythonguis.com/faq/which-python-gui-library/

[](https://www.pythonguis.com/faq/which-python-gui-library/#menu)
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
# Which Python GUI library should you use?
Comparing the Python GUI libraries available in 2025
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 08 [ FAQ ](https://www.pythonguis.com/faq/)
Python is a popular programming used for everything from scripting routine tasks to building websites and performing complex data analysis. While you can accomplish a lot with command line tools, some tasks are better suited to graphical interfaces. You may also find yourself wanting to build a desktop front-end for an existing tool to improve usability for non-technical users. Or maybe you're building some hardware or a mobile app and want an intuitive touchscreen interface.
To create _graphical user interfaces_ with Python, you need a GUI library. Unfortunately, at this point things get pretty confusing -- there are many different GUI libraries available for Python, all with different capabilities and licensing. _Which Python GUI library should you use for your project?_
In this article, we will look at a selection of the most popular Python GUI frameworks currently available and why you should consider using them for your own projects. You'll learn about the relative strengths of each library, understand the licensing limitations and see a simple _Hello, World!_ application written in each. By the end of the article you should feel confident choosing the right library for your project.
**tldr** If you're looking to build professional quality software, start with PySide6 or PyQt6. The Qt framework is batteries-included — whatever your project, you'll be able to get it done. We have a complete [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/).
There is _some_ bias here -- I have been working with Qt for about 10 years, writing books & developing commercial software. But I chose it and continue to use it because it's the best option for getting things done. That said, the other libraries all have their place & may be a better fit for your own project -- read on to find out!
If you're looking for more demos to see what you can do with Python, we have a Github respository full of [Python GUI examples](https://github.com/pythonguis/pythonguis-examples) to get you started.
Table of Contents
  * [PyQt or PySide](https://www.pythonguis.com/faq/which-python-gui-library/#pyqt-or-pyside)
  * [Tkinter](https://www.pythonguis.com/faq/which-python-gui-library/#tkinter)
  * [Kivy](https://www.pythonguis.com/faq/which-python-gui-library/#kivy)
  * [BeeWare Toga](https://www.pythonguis.com/faq/which-python-gui-library/#beeware-toga)
  * [PyQt/PySide with QML](https://www.pythonguis.com/faq/which-python-gui-library/#pyqtpyside-with-qml)
  * [PySimpleGUI](https://www.pythonguis.com/faq/which-python-gui-library/#pysimplegui)
  * [WxPython](https://www.pythonguis.com/faq/which-python-gui-library/#wxpython)
  * [PyGObject (GTK+)](https://www.pythonguis.com/faq/which-python-gui-library/#pygobject-gtk)
  * [Remi](https://www.pythonguis.com/faq/which-python-gui-library/#remi)
  * [Conclusion](https://www.pythonguis.com/faq/which-python-gui-library/#conclusion)


## PyQt or PySide
_**Best for** commercial, multimedia, scientific or engineering desktop applications. Best all-rounder with batteries included._
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
PyQt and PySide are wrappers around the Qt framework. They allow you to easily create modern interfaces that look right at home on any platform, including Windows, macOS, Linux and even Android. They also have solid tooling with the most notable being _Qt Creator_ , which includes a WYSIWYG editor for designing GUI interfaces quickly and easily. Being backed by a commercial project means that you will find plenty of support and online learning resources to help you develop your application.
Qt (and by extension PyQt & PySide) is not just a GUI library, but a complete application development framework. In addition to standard UI elements, such as widgets and layouts, Qt provides MVC-like data-driven views (spreadsheets, tables), database interfaces & models, graph plotting, vector graphics visualization, multimedia playback, sound effects & playlists and built-in interfaces for hardware such as printing. The Qt signals and slots models allows large applications to be built from re-usable and isolated components.
While other toolkits can work great when building small & simple tools, Qt really comes into its own for building real _commercial-quality_ applications where you will benefit from the pre-built components. This comes at the expense of a slight learning curve. However, for smaller projects Qt is not really any more complex than other libraries. Qt Widgets-based applications use platform native widgets to ensure they look and feel at home on Windows, macOS and Qt-based Linux desktops.
**Installation** `pip install pyqt6` or `pip install pyside6`
A simple _hello world_ application in PyQt6, using the Qt Widgets API is shown below.
  * PyQt6
  * PySide6


python ```
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Hello World")
    button = QPushButton("My simple app.")
    button.pressed.connect(self.close)
    self.setCentralWidget(button)
    self.show()

app = QApplication(sys.argv)
w = MainWindow()
app.exec()

```

python ```
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Hello World")
    button = QPushButton("My simple app.")
    button.pressed.connect(self.close)
    self.setCentralWidget(button)
    self.show()

app = QApplication(sys.argv)
w = MainWindow()
app.exec()

```

As you can see, the code is almost identical between PyQt & PySide, so it's not something to be concerned about when you start developing with either: you can always migrate easily if you need to.
![PyQt6 Application Screenshot](https://www.pythonguis.com/static/faq/python-gui-libraries/pyqt6-windows.jpg) _Hello world application built using PyQt6, running on Windows 11_
Before the Qt Company (under Nokia) released the officially supported PySide library in 2009, Riverbank Computing had released PyQt in 1998. The main difference between these two libraries is in _licensing_.
  * **PyQt** The free-to-use version of PyQt is licensed under **GNU General Public License (GPL) v3**. This means that you must also license your applications with the GPL _unless_ you purchase a commercial version
  * **PySide** is licensed under **GNU Lesser General Public License (LGPL)**. This means PySide may be used in your applications without any additional fee.


Note that both these libraries are separate from Qt itself which also has a free-to-use, open source version and a paid, commercial version.
For a more information see our article on [PyQt vs PySide licensing](https://www.pythonguis.com/faq/pyqt-vs-pyside/). **tldr** If you want to develop closed-source software without paying for a license, use PySide6.
  * **PySide6**
    * [PySide6 Book](https://www.pythonguis.com/pyside6-book/)
    * [PySide6 Tutorial](https://www.pythonguis.com/pyside6-tutorial/)
    * [PySide Website](https://www.qt.io/qt-for-python)
    * [PySide Documentation](https://doc.qt.io/qtforpython/)
    * [GitHub Repository](https://github.com/PySide)
  * **PyQt6**
    * [PyQt6 Book](https://www.pythonguis.com/pyqt6-book/)
    * [PyQt6 Tutorial](https://www.pythonguis.com/pyqt6-tutorial/)
    * [PyQt6 Video Course](https://www.martinfitzpatrick.com/pyqt6-crash-course/)
    * [PyQt Website](https://www.riverbankcomputing.com/software/pyqt/intro)
    * [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
  * **PyQt5**
    * [PyQt5 Book](https://www.pythonguis.com/pyqt5-book/)
    * [PyQt5 Tutorial](https://www.pythonguis.com/pyqt5-tutorial/)
    * [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)


## Tkinter
_**Best for** simple portable Python GUIs and applications_
Tkinter is the defacto GUI framework for Python. It comes bundled with Python on both Windows and macOS. (On Linux, it may require downloading an additional package from your distribution's repo.) Tkinter is a wrapper written around the Tk GUI toolkit. Its name is an amalgamation of the words _Tk_ and _Interface_.
Tkinter is a simple library with support for standard layouts and widgets, as well as more complex widgets such as tabbed views & progressbars. Tkinter is a pure GUI library, not a framework. There is no built-in support for GUIs driven from data sources, databases, or for displaying or manipulating multimedia or hardware. However, if you need to make something simple that doesn't require any additional dependencies, Tkinter may be what you are looking for. Tkinter is cross-platform however the widgets can look outdated, particularly on Windows.
**Installation** Already installed with Python on Windows and macOS. Ubuntu/Debian Linux `sudo apt install python3-tk`
A simple _hello world_ application in Tkinter is shown below.
  * Standard
  * Class-based


python ```
import tkinter as tk
window = tk.Tk()
window.title("Hello World")

def handle_button_press(event):
  window.destroy()

button = tk.Button(text="My simple app.")
button.bind("", handle_button_press)
button.pack()
# Start the event loop.
window.mainloop()

```

python ```
from tkinter import Tk, Button

class Window(Tk):
  def __init__(self):
    super().__init__()
    self.title("Hello World")
    self.button = Button(text="My simple app.")
    self.button.bind("", self.handle_button_press)
    self.button.pack()
  def handle_button_press(self, event):
    self.destroy()

# Start the event loop.
window = Window()
window.mainloop()

```

![Tkinter Application Screenshot](https://www.pythonguis.com/static/faq/python-gui-libraries/tkinter-windows.jpg) _Hello world application built using Tkinter, running on Windows 11_
Tkinter was originally developed by Steen Lumholt and Guido Van Rossum, who designed Python itself. Both the GUI framework and the language are licensed under the same Python Software Foundation (PSF) License. While the license is compatible with the GPL, it is a 'permissive' license (similar to the MIT License) that allows it to be used for proprietary applications and modifications.
  * [Tkinter tutorial](https://www.pythonguis.com/tkinter/)
  * [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)


## Kivy
_**Best for** Python mobile app development_
While most other GUI frameworks are _bindings_ to toolkits written in other programming languages, Kivy is perhaps the only framework which is primarily written in pure Python. If you want to create touchscreen-oriented interfaces with a focus on mobile platforms such as Android and iOS, this is the way to go. This does run on desktop platforms (Windows, macOS, Linux) as well but note that your application may not look and behave like a _native application_. However, there is a pretty large community around this framework and you can easily find resources to help you learn it online.
The look and feel of Kivy is extremely customizable, allowing it to be used as an alternative to libraries like Pygame (for making games with Python). The developers have also released a number of separate libraries for Kivy. Some provide Kivy with better integration and access to certain platform-specific features, or help package your application for distribution on platforms like Android and iOS. Kivy has it's own design language called Kv, which is similar to QML for Qt. It allows you to easily separate the interface design from your application's logic.
There is a 3rd party add-on for Kivy named KivyMD that replaces Kivy's widgets with ones that are compliant with Google's Material Design.
A simple _hello world_ application in Kivy is shown below.
**Installation** `pip install kivy`
A simple _hello world_ application in Kivy is shown below.
python ```
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
Window.size = (300, 200)

class MainWindow(BoxLayout):
  def __init__(self):
    super().__init__()
    self.button = Button(text="Hello, World?")
    self.button.bind(on_press=self.handle_button_clicked)
    self.add_widget(button)
  def handle_button_clicked(self, event):
    self.button.text = "Hello, World!"

class MyApp(App):
  def build(self):
    self.title = "Hello, World!"
    return MainWindow()

app = MyApp()
app.run()

```

![Kivy Application Screenshot](https://www.pythonguis.com/static/faq/python-gui-libraries/kivy-windows.jpg) _Hello world application built using Kivy, running on Windows 11_
An equivalent application built using the Kv declarative language is shown below.
  * main.py
  * controller.kv


python ```
import kivy
kivy.require('1.0.5')
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty

class Controller(FloatLayout):
  '''Create a controller that receives a custom widget from the kv lang file.
  Add an action to be called from the kv lang file.
  '''
  def button_pressed(self):
    self.button_wid.text = 'Hello, World!'

class ControllerApp(App):
  def build(self):
    return Controller()

if __name__ == '__main__':
  ControllerApp().run()

```

python ```
#:kivy 1.0
:
  button_wid: custom_button
  BoxLayout:
    orientation: 'vertical'
    padding: 20
    Button:
      id: custom_button
      text: 'Hello, World?'
      on_press: root.button_pressed()

```

The name of the Kv file _must_ match the name of the class from the main application -- here `Controller` and `controller.kv`.
![Kivy Kv Application Screenshot](https://www.pythonguis.com/static/faq/python-gui-libraries/kivykv-windows.jpg) _Hello world application built using Kivy + Kv, running on Windows 11_
In February 2011, Kivy was released as the spiritual successor to a similar framework called **PyMT**. While they shared similar goals and was also led by the current core developers of Kivy, where Kivy differs is in its underlying design and a professional organization which actively develops and maintains it. Kivy is licensed under the MIT license, which is a 'permissive' license that allows you to use it freely in both open source and proprietary applications. As such, you are even allowed to make proprietary modifications to the framework itself.
  * [Kivy Website](https://kivy.org)
  * [Kivy Documentation](https://kivy.org/doc/stable/)
  * [GitHub Repository](https://github.com/kivy)
  * [KivyMD Documentation](https://kivymd.readthedocs.io/en/latest/)
  * [Kv language documentation](https://kivy.org/doc/stable/guide/lang.html)


## BeeWare Toga
_**Best for** simple cross-platform native GUI development_
BeeWare is a collection of tools and libraries which work together to help you write cross platform Python applications with _native_ GUIs. That means, the applications you create use the OS-provided widgets and behaviors, appearing just like any other application despite being written in Python.
The BeeWare system includes -
  * **Toga** a cross platform widget toolkit, which we'll demo below.
  * **Briefcase** a tool for packaging Python projects as distributable artefacts.
  * Libraries for accessing platform-native APIs.
  * Pre-compiled builds of Python for platforms where official Python installers aren't avaiable.


**Installation** `pip install toga`
A simple _hello world_ application using BeeWare/Toga is shown below.
python ```
import toga
from toga.style import Pack

class HelloWorld(toga.App):
  def startup(self):
    layout = toga.Box()
    self.button = toga.Button(
      "Say Hello!",
      on_press=self.say_hello,
      style=Pack(margin=5),
    )
    layout.add(self.button)
    self.main_window = toga.MainWindow(title="Hello world!")
    self.main_window.content = layout
    self.main_window.show()
  def say_hello(self, source_widget):
    # Receives the button that was clicked.
    source_widget.text = "Hello, world!"

app = HelloWorld(formal_name="Hello, world!", app_id="hello.world")
app.main_loop()

```

![Toga Application Screenshot](https://www.pythonguis.com/static/faq/python-gui-libraries/toga-windows.jpg) _Hello world application built using BeeWare Toga, running on Windows 11_
BeeWare is developed by Russell Keith-Magee. It is licensed under the BSD 3-Clause "New" or "Revised" License. The above example is using a single Python file for simplicity, see the linked tutorial below to see how to set up an application using Briefcase for cross-platform deployment.
  * [Toga tutorial](https://docs.beeware.org/en/latest/)
  * [BeeWare Homepage](https://beeware.org/)
  * [Toga Source Code](https://github.com/beeware/toga)


## PyQt/PySide with QML
_**Best for** Raspberry Pi, microcontrollers, industrial and consumer electronics_
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
When using PyQt and PySide you actually have _two_ options for building your GUIs. We've already introduced the Qt Widgets API which is well-suited for building desktop applications. But Qt also provides a _declarative_ API in the form of Qt Quick/QML.
Using Qt Quick/QML you have access to the entire Qt framework for building your applications. Your UI consists of two parts: the Python code which handles the business logic and the QML which defines the structure and behavior of the UI itself. You can control the UI from Python, or use embedded Javascript code to handle events and animations.
Qt Quick/QML is ideally suited for building modern touchscreen interfaces for microcontrollers or device interfaces -- for example, building interfaces for microcontrollers like the Raspberry Pi. However you can also use it on desktop to build completely customized application experiences, like those you find in media player applications like Spotify, or to desktop games.
**Installation** `pip install pyqt6` or `pip install pyside6`
A simple _Hello World_ app in PyQt6 with QML. Save the QML file in the same folder as the Python file, and run as normally.
  * main.py
  * main.qml


python ```
import sys
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('main.qml')
sys.exit(app.exec())

```

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

Licensing for Qt Quick/QML applications is the same as for other PyQt/PySide apps.
  * **PyQt**
    * [QML/PyQt5 Tutorial](https://www.pythonguis.com/tutorials/qml-qtquick-python-application/)
    * [QML/PyQt6 Tutorial](https://www.pythonguis.com/tutorials/pyqt6-qml-qtquick-python-application/)
    * [PyQt Website](https://www.riverbankcomputing.com/software/pyqt/intro)
    * [PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
  * **PySide**
    * [QML/PySide2 Tutorial](https://www.pythonguis.com/tutorials/pyside-qml-qtquick-python-application/)
    * [QML/PySide6 Tutorial](https://www.pythonguis.com/tutorials/pyside6-qml-qtquick-python-application/)
    * [PySide Website](https://www.qt.io/qt-for-python)
    * [PySide Documentation](https://doc.qt.io/qtforpython/)
    * [GitHub Repository](https://github.com/PySide)


![PyQt6 QML Application Screenshot](https://www.pythonguis.com/static/faq/python-gui-libraries/pyqt6qml-windows.jpg) _Hello world application built using PyQt6 & QML, running on Windows 11_
## PySimpleGUI
PySimpleGUI is no longer being developed. We do not recommend it if you are starting a new project in 2025. Take a look at [PySide6](https://www.pythonguis.com/faq/which-python-gui-library/#pyqt-or-pyside) instead.
PySimpleGUI aims to simplify GUI application development for Python. It doesn't reinvent the wheel but provides a wrapper around other existing frameworks such as Tkinter, Qt (PySide 2), WxPython and Remi. By doing so, it lowers the barrier to creating a GUI but also allows you to easily migrate from one GUI framework to another by simply changing the import statement.
While there is a separate port of PySimpleGUI for each of these frameworks, the Tkinter version is considered the most feature complete. Wrapping other libraries comes at a cost however — your applications will not be able to exploit the full capabilities or performance of the underlying libraries. The pure-Python event loop can also hinder performance by bottlenecking events with the GIL. However, this is only really a concern when working with live data visualization, streaming or multimedia applications.
There is a fair amount of good resources to help you learn to use PySimpleGUI, including an official Cookbook and a Udemy course offered by the developers themselves. According to their project website, PySimpleGUI was initially made (and later released in 2018) because the lead developer wanted a 'simplified' GUI framework to use in his upcoming project and wasn't able to find any that met his needs.
**Installation** `pip install pysimplegui`
python ```
import PySimpleGUI as sg

layout = [
  [sg.Button("My simple app.")]
]
window = sg.Window("Hello World", layout)
while True:
  event, values = window.read()
  print(event, values)
  if event == sg.WIN_CLOSED or event == "My simple app.":
    break
window.close()

```

![PySimpleGUI Application Screenshot](https://www.pythonguis.com/static/faq/python-gui-libraries/pysimplegui-windows.jpg) _Hello world application built using PySimpleGUI, running on Windows 11_
PySimpleGUI 4 was licensed under the same LGPL v3 license as PySide. PySimpleGUI 5 switched to a paid commercial license model. There is a fork of PySimpleGUI 4 called _FreeSimpleGUI_ which retains the original LGPL license.
  * [PySimpleGUI Website](https://pysimplegui.readthedocs.io/en/latest/)
  * [PySimpleGUI Cookbook](https://www.pysimplegui.org/en/latest/cookbook/)
  * [GitHub Repository](https://github.com/PySimpleGUI/PySimpleGUI)
  * [FreeSimpleGUI](https://github.com/spyoungtech/FreeSimpleGui)


## WxPython
_**Best for** simple portable desktop applications_
WxPython is a wrapper for the popular, cross-platform GUI toolkit called WxWidgets. It is implemented as a set of Python extension modules that wrap the GUI components of the popular wxWidgets cross platform library, which is written in C++.
WxPython uses native widgets on most platforms, ensure that your application looks and feels at home. However, WxPython is known to have certain platform-specific quirks and it also doesn't provide the same level of abstraction between platforms as Qt for example. This may affect how easy it is to maintain cross-platform compatibility for your application.
WxPython is under active development and is also currently being _reimplemented from scratch_ under the name 'WxPython Phoenix'. The team behind WxWidgets is also responsible for WxPython, which was initially released in 1998.
**Installation** `pip install wxpython`
python ```
import wx

class MainWindow(wx.Frame):
  def __init__(self, parent, title):
    wx.Frame.__init__(self, parent, title=title, size=(200, -1))
    self.button = wx.Button(self, label="My simple app.")
    self.Bind(
      wx.EVT_BUTTON, self.handle_button_click, self.button
    )
    self.sizer = wx.BoxSizer(wx.VERTICAL)
    self.sizer.Add(self.button)
    self.SetSizer(self.sizer)
    self.SetAutoLayout(True)
    self.Show()
  def handle_button_click(self, event):
    self.Close()

app = wx.App(False)
w = MainWindow(None, "Hello World")
app.MainLoop()

```

![WxPython Application Screenshot](https://www.pythonguis.com/static/faq/python-gui-libraries/wxpython-windows.jpg) _Hello world application built using WxPython, running on Windows 11_
Both WxWidgets and WxPython are licensed under a WxWindows Library License, which is a 'free software' license similar to LGPL (with a special exception). It allows both proprietary and open source applications to _use and modify_ WxPython.
  * [WxPython Website](https://www.wxpython.org/)
  * [WxPython Wiki](https://wiki.wxpython.org/)
  * [GitHub Repository](https://github.com/wxWidgets/Phoenix/)


## PyGObject (GTK+)
_**Best for** developing applications for GNOME desktop_
If you intend to create an application that integrates well with _GNOME_ and other GTK-based desktop environments for Linux, PyGObject is the right choice. PyGObject itself is a language-binding to the GTK+ widget toolkit. It allows you to create modern, adaptive user interfaces that conform to [GNOME's Human Interface Guidelines (HIG)](https://developer.gnome.org/hig/).
It also enables the development of 'convergent' applications that can run on both Linux desktop and mobile platforms. There are a few first-party and community-made, third-party tools available for it as well. This includes the likes of GNOME Builder and Glade, which is yet another WYSIWYG editor for building graphical interfaces quickly and easily.
Unfortunately, there aren't a whole lot of online resources to help you learn PyGObject application development, apart from [this one rather well-documented tutorial](https://python-gtk-3-tutorial.readthedocs.io/). While cross-platform support does exist (e.g. Inkscape, GIMP), the resulting applications won't feel completely native on other desktops. Setting up a development environment for this, especially on Windows and macOS, also requires more steps than for most other frameworks in this article, which just need a working Python installation.
**Installation** Ubuntu/Debian `sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-4.0`, macOS Homebrew `brew install pygobject4 gtk+4`
python ```
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
def on_activate(app):
  win = Gtk.ApplicationWindow(application=app)
  btn = Gtk.Button(label="Hello, World!")
  btn.connect('clicked', lambda x: win.close())
  win.set_child(btn)
  win.present()
app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)

```

![PyGObject Application Screenshot](https://www.pythonguis.com/static/faq/python-gui-libraries/gobject-ubuntu.jpg) _Hello world application built using PyGObject, running on Ubuntu Linux 21.10_
PyGObject is developed and maintained under the GNOME Foundation, who is also responsible for the GNOME desktop environment. PyGObject replaces several separate Python modules, including PyGTK, GIO and python-gnome, which were previously required to create a full GNOME/GTK application. Its initial release was in 2006 and it is licensed under an older version of LGPL (v2.1). While there are some differences with the current version of LGPL (v3), the license still allows its use in proprietary applications but requires any modification to the library itself to be released as open source.
  * [PyGObject Project Homepage](https://www.gtk.org/docs/language-bindings/python/)
  * [PyGObject Documentation](https://pygobject.readthedocs.io/)
  * [GitLab Repository](https://gitlab.gnome.org/GNOME/pygobject/)


## Remi
_**Best for** web based UIs for Python applications_
Remi, which stands for _REMote Interface_ , is the ideal solution for applications that are intended to be run on servers and other headless setups. (For example, on a Raspberry Pi.) Unlike most other GUI frameworks/libraries, Remi is rendered completely in the browser using a built-in web server. Hence, it is completely platform-independent and runs equally well on all platforms.
That also makes the application's interface accessible to any computer or device with a web browser that is connected to the same network. Although access can be restricted with a username and password, it doesn't implement any security strategies by default. Note that Remi is meant to be used as a _desktop GUI framework_ and not for _serving up web pages_. If more than one user connects to the application at the same time, they will see and interact with the exact same things as if a single user was using it.
Remi requires no prior knowledge of HTML or other similar web technologies. You only need to have a working understanding of Python to use it, which is then automatically translated to HTML. It also comes included with a _drag n drop GUI editor_ that is akin to Qt Designer for PyQt and PySide.
python ```
import remi.gui as gui
from remi import start, App
class MyApp(App):
  def main(self):
    container = gui.VBox(width=120, height=100)
    # Create a button, with the label "Hello, World!"
    self.bt = gui.Button('Hello, World?')
    self.bt.onclick.do(self.on_button_pressed)
    # Add the button to the container, and return it.
    container.append(self.bt)
    return container
  def on_button_pressed(self, widget):
    self.bt.set_text('Hello, World!')
start(MyApp)

```

Remi is licensed under the Apache License v2.0, which is another 'permissive' license similar to the MIT License. The license allows using it in both open source and proprietary applications, while also allowing proprietary modifications to be made to the framework itself. Its main conditions revolve around the preservation of copyright and license notices.
![Remi Application Screenshot](https://www.pythonguis.com/static/faq/python-gui-libraries/remi-windows.jpg) _Hello world application built using Remi, running on Chrome on Windows 11_
  * [GitHub Repository](https://github.com/rawpython/remi)
  * [Reddit (r/RemiGUI)](https://www.reddit.com/r/RemiGUI)


## Conclusion
If you're looking to build GUI applications with Python, there is probably a GUI framework/library listed here that fits the bill for your project. Try and weigh up the capabilities & licensing of the different libraries with the scale of your project, both now and in the future.
Don't be afraid to experiment a bit with different libraries, to see which feel the best fit. While the APIs of GUI libraries are very different, they share many underlying concepts in common and things you learn in one library will often apply in another.
You are only limited by your own imagination. So go out there and make something!
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Which Python GUI library should you use?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) and [Lalin Paranawithana](https://www.pythonguis.com/authors/lalin-paranawithana/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/which-python-gui-library/Python books) on the subject. 
**Which Python GUI library should you use?** was published in [faq](https://www.pythonguis.com/faq/) on February 26, 2025 (updated April 08, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [tkinter](https://www.pythonguis.com/topics/tkinter/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [pygobject](https://www.pythonguis.com/topics/pygobject/) [pysimplegui](https://www.pythonguis.com/topics/pysimplegui/) [ kivy](https://www.pythonguis.com/topics/kivy/) [wxpython](https://www.pythonguis.com/topics/wxpython/) [remi](https://www.pythonguis.com/topics/remi/) [beeware](https://www.pythonguis.com/topics/beeware/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt6](https://www.pythonguis.com/topics/qt6/) [tk](https://www.pythonguis.com/topics/tk/) [wx](https://www.pythonguis.com/topics/wx/)
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
