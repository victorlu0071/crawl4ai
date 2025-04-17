# Content from: https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/

[](https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/#menu)
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
# PySide6 Toolbars & Menus — QAction
Defining toolbars, menus, and keyboard shortcuts with QAction
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 11 This article has been updated for PySide6. PySide6 [ Getting started with PySide6 ](https://www.pythonguis.com/pyside6-tutorial/#pyside6-getting-started)
#### [ PySide6 Tutorial ](https://www.pythonguis.com/pyside6-tutorial/) — [Getting started with PySide6](https://www.pythonguis.com/pyside6-tutorial/#pyside6-getting-started)
  * [Creating your first app with PySide6](https://www.pythonguis.com/tutorials/pyside6-creating-your-first-window/)
  * [PySide6 Signals, Slots & Events](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/)
  * [PySide6 Widgets](https://www.pythonguis.com/tutorials/pyside6-widgets/)
  * [PySide6 Layouts](https://www.pythonguis.com/tutorials/pyside6-layouts/)
  * [PySide6 Toolbars & Menus — QAction](https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/)
  * [PySide6 Dialogs and Alerts](https://www.pythonguis.com/tutorials/pyside6-dialogs/)
  * [Creating Additional Windows in PySide6](https://www.pythonguis.com/tutorials/pyside6-creating-multiple-windows/)


This tutorial is also available for [PyQt6](https://www.pythonguis.com/tutorials/pyqt6-actions-toolbars-menus/) , [PySide2](https://www.pythonguis.com/tutorials/pyside-actions-toolbars-menus/) and [PyQt5](https://www.pythonguis.com/tutorials/pyqt-actions-toolbars-menus/)
Next, we'll look at some of the common user interface elements you've probably seen in many other applications — toolbars and menus. We'll also explore the neat system Qt provides for minimizing the duplication between different UI areas — `QAction`.
Table of Contents
  * [Basic App](https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/#basic-app)
  * [Toolbars](https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/#toolbars)
  * [Adding a Toolbar](https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/#adding-a-toolbar)
  * [Menus](https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/#menus)
  * [Adding a Menu](https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/#adding-a-menu)


## Basic App
We'll start this tutorial with a simple skeleton application, which we can customize. Save the following code in a file named `app.py` -- this code all the imports you'll need for the later steps:
python ```
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
  QApplication,
  QCheckBox,
  QLabel,
  QMainWindow,
  QStatusBar,
  QToolBar,
)
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
app = QApplication([])
window = MainWindow()
window.show()
app.exec()

```

This file contains the imports and the basic code that you'll use to complete the examples in this tutorial.
If you're migrating to PySide6 from PySide2, notice that `QAction` is now available via the `QtGui` module.
## Toolbars
One of the most commonly seen user interface elements is the toolbar. Toolbars are bars of icons and/or text used to perform common tasks within an application, for which access via a menu would be cumbersome. They are one of the most common UI features seen in many applications. While some complex applications, particularly in the Microsoft Office suite, have migrated to contextual 'ribbon' interfaces, the standard toolbar is usually sufficient for the majority of applications you will create.
![Standard GUI elements](https://www.pythonguis.com/static/tutorials/qt/actions-toolbars-menus/toolbar.png) _Standard GUI elements_
## Adding a Toolbar
Let's start by adding a toolbar to our application. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
In Qt, toolbars are created from the `QToolBar` class. To start, you create an instance of the class and then call `addToolbar` on the `QMainWindow`. Passing a string in as the first argument to `QToolBar` sets the toolbar's name, which will be used to identify the toolbar in the UI:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    label = QLabel("Hello!")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setCentralWidget(label)
    toolbar = QToolBar("My main toolbar")
    self.addToolBar(toolbar)

```

**Run it!** You'll see a thin grey bar at the top of the window. This is your toolbar. Right-click the name to trigger a context menu and toggle the bar off.
![A window with a toolbar.](https://www.pythonguis.com/static/tutorials/qt/actions-toolbars-menus/window-with-toolbar.png) _A window with a toolbar._
**How can I get my toolbar back?** Unfortunately, once you remove a toolbar, there is now no place to right-click to re-add it. So, as a general rule, you want to either keep one toolbar un-removeable, or provide an alternative interface in the menus to turn toolbars on and off.
We should make the toolbar a bit more interesting. We could just add a `QButton` widget, but there is a better approach in Qt that gets you some additional features — and that is via `QAction`. `QAction` is a class that provides a way to describe abstract user interfaces. What this means in English is that you can define multiple interface elements within a single object, unified by the effect that interacting with that element has.
For example, it is common to have functions that are represented in the toolbar but also the menu — think of something like _Edit- >Cut_, which is present both in the _Edit_ menu but also on the toolbar as a pair of scissors, and also through the keyboard shortcut `Ctrl-X` (`Cmd-X` on Mac).
Without `QAction`, you would have to define this in multiple places. But with `QAction` you can define a single `QAction`, defining the triggered action, and then add this action to both the menu and the toolbar. Each `QAction` has names, status messages, icons, and signals that you can connect to (and much more).
In the code below, you can see this first `QAction` added:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    label = QLabel("Hello!")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setCentralWidget(label)
    toolbar = QToolBar("My main toolbar")
    self.addToolBar(toolbar)
    button_action = QAction("Your button", self)
    button_action.setStatusTip("This is your button")
    button_action.triggered.connect(self.toolbar_button_clicked)
    toolbar.addAction(button_action)
  def toolbar_button_clicked(self, s):
    print("click", s)

```

To start with, we create the function that will accept the signal from the `QAction` so we can see if it is working. Next, we define the `QAction` itself. When creating the instance, we can pass a label for the action and/or an icon. You must also pass in any `QObject` to act as the parent for the action — here we're passing `self` as a reference to our main window. Strangely, for `QAction`, the parent element is passed in as the final argument.
Next, we can opt to set a status tip — this text will be displayed on the status bar once we have one. Finally, we connect the `triggered` signal to the custom function. This signal will fire whenever the `QAction` is _triggered_ (or activated).
**Run it!** You should see your button with the label that you have defined. Click on it, and then our custom method will print "click" and the status of the button.
![Toolbar showing our QAction button.](https://www.pythonguis.com/static/tutorials/qt/actions-toolbars-menus/toolbar-with-qaction-button.png) _Toolbar showing our`QAction` button._
**Why is the signal always false?** The signal passed indicates whether the button is _checked_ , and since our button is not checkable — just clickable — it is always false. We'll show how to make it checkable shortly.
Next, we can add a status bar.
We create a status bar object by calling `QStatusBar` to get a new status bar object and then passing this into `setStatusBar`. Since we don't need to change the status bar settings, we can also just pass it in as we create it, in a single line:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    label = QLabel("Hello!")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setCentralWidget(label)
    toolbar = QToolBar("My main toolbar")
    self.addToolBar(toolbar)
    button_action = QAction("Your button", self)
    button_action.setStatusTip("This is your button")
    button_action.triggered.connect(self.toolbar_button_clicked)
    toolbar.addAction(button_action)
    self.setStatusBar(QStatusBar(self))
  def toolbar_button_clicked(self, s):
    print("click", s)

```

**Run it!** Hover your mouse over the toolbar button, and you will see the status text in the status bar.
![Status bar text is updated as we hover our actions.](https://www.pythonguis.com/static/tutorials/qt/actions-toolbars-menus/statusbar-hover-action.png) _Status bar text updated as we hover over the action._
Next, we're going to turn our `QAction` toggleable — so clicking will turn it on, and clicking again will turn it off. To do this, we simply call `setCheckable(True)` on the `QAction` object:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    label = QLabel("Hello!")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setCentralWidget(label)
    toolbar = QToolBar("My main toolbar")
    self.addToolBar(toolbar)
    button_action = QAction("Your button", self)
    button_action.setStatusTip("This is your button")
    button_action.triggered.connect(self.toolbar_button_clicked)
    button_action.setCheckable(True)
    toolbar.addAction(button_action)
    self.setStatusBar(QStatusBar(self))
  def toolbar_button_clicked(self, s):
    print("click", s)

```

**Run it!** Click on the button to see it toggle from checked to unchecked state. Note that the custom slot method we create now alternates outputting `True` and `False`.
![The toolbar button toggled on.](https://www.pythonguis.com/static/tutorials/qt/actions-toolbars-menus/toolbar-button-toggled.png) _The toolbar button toggled on._
There is also a `toggled` signal, which only emits a signal when the button is toggled. But the effect is identical, so it is mostly pointless.
Things look pretty shabby right now — so let's add an icon to our button. For this, I recommend you download the [fugue icon set](http://p.yusukekamiyamane.com/) by designer Yusuke Kamiyamane. It's a great set of beautiful 16x16 icons that can give your apps a nice professional look. It is freely available with only attribution required when you distribute your application — although I am sure the designer would appreciate some cash too if you have some spare.
![Fugue Icon Set — Yusuke Kamiyamane](https://www.pythonguis.com/static/tutorials/qt/actions-toolbars-menus/fugue-icons.png) _Fugue Icon Set — Yusuke Kamiyamane_
Select an image from the set (in the examples here, I've selected the file `bug.png`) and copy it into the same folder as your source code.
We can create a `QIcon` object by passing the file name to the class, e.g. `QIcon("bug.png")` -- if you place the file in another folder, you will need a full relative or absolute path to it.
Finally, to add the icon to the `QAction` (and therefore the button), we simply pass it in as the first argument when creating the `QAction`.
You also need to let the toolbar know how large your icons are. Otherwise, your icon will be surrounded by a lot of padding. You can do this by calling `setIconSize()` with a `QSize` object: 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    label = QLabel("Hello!")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setCentralWidget(label)
    toolbar = QToolBar("My main toolbar")
    toolbar.setIconSize(QSize(16, 16))
    self.addToolBar(toolbar)
    button_action = QAction(QIcon("bug.png"), "Your button", self)
    button_action.setStatusTip("This is your button")
    button_action.triggered.connect(self.toolbar_button_clicked)
    button_action.setCheckable(True)
    toolbar.addAction(button_action)
    self.setStatusBar(QStatusBar(self))
  def toolbar_button_clicked(self, s):
    print("click", s)

```

**Run it!** The `QAction` is now represented by an icon. Everything should work exactly as it did before.
![Our action button with an icon.](https://www.pythonguis.com/static/tutorials/qt/actions-toolbars-menus/action-button-with-icon.png) _Our action button with an icon._
Note that Qt uses your operating system's default settings to determine whether to show an icon, text, or an icon and text in the toolbar. But you can override this by using `setToolButtonStyle()`. This slot accepts any of the following flags from the `Qt` namespace:
Flag | Behavior  
---|---  
`Qt.ToolButtonStyle.ToolButtonIconOnly` | Icon only, no text  
`Qt.ToolButtonStyle.ToolButtonTextOnly` | Text only, no icon  
`Qt.ToolButtonStyle.ToolButtonTextBesideIcon` | Icon and text, with text beside the icon  
`Qt.ToolButtonStyle.ToolButtonTextUnderIcon` | Icon and text, with text under the icon  
`Qt.ToolButtonStyle.ToolButtonFollowStyle` | Follow the host desktop style  
The default value is `Qt.ToolButtonStyle.ToolButtonFollowStyle`, meaning that your application will default to following the standard/global setting for the desktop on which the application runs. This is generally recommended to make your application feel as _native_ as possible.
Finally, we can add a few more bits and bobs to the toolbar. We'll add a second button and a checkbox widget. As mentioned, you can literally put any widget in here, so feel free to go crazy:
python ```
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
  QApplication,
  QCheckBox,
  QLabel,
  QMainWindow,
  QStatusBar,
  QToolBar,
)
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    label = QLabel("Hello!")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setCentralWidget(label)
    toolbar = QToolBar("My main toolbar")
    toolbar.setIconSize(QSize(16, 16))
    self.addToolBar(toolbar)
    button_action = QAction(QIcon("bug.png"), "&Your button", self)
    button_action.setStatusTip("This is your button")
    button_action.triggered.connect(self.toolbar_button_clicked)
    button_action.setCheckable(True)
    toolbar.addAction(button_action)
    toolbar.addSeparator()
    button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
    button_action2.setStatusTip("This is your button2")
    button_action2.triggered.connect(self.toolbar_button_clicked)
    button_action2.setCheckable(True)
    toolbar.addAction(button_action2)
    toolbar.addWidget(QLabel("Hello"))
    toolbar.addWidget(QCheckBox())
    self.setStatusBar(QStatusBar(self))
  def toolbar_button_clicked(self, s):
    print("click", s)
app = QApplication([])
window = MainWindow()
window.show()
app.exec()

```

**Run it!** Now you see multiple buttons and a checkbox.
![Toolbar with an action and two widgets.](https://www.pythonguis.com/static/tutorials/qt/actions-toolbars-menus/toolbar-action-widgets.png) _Toolbar with an action and two widgets._
## Menus
Menus are another standard component of UIs. Typically, they are at the top of the window or the top of a screen on macOS. They allow you to access all standard application functions. A few standard menus exist — for example _File_ , _Edit_ , _Help_. Menus can be nested to create hierarchical trees of functions, and they often support and display keyboard shortcuts for fast access to their functions.
![Standard GUI elements - Menus](https://www.pythonguis.com/static/tutorials/qt/actions-toolbars-menus/menus.png) _Standard GUI elements - Menus_
## Adding a Menu
To create a menu, we create a menubar we call `menuBar()` on the `QMainWindow`. We add a menu to our menu bar by calling `addMenu()`, passing in the name of the menu. I've called it `'&File'`. The ampersand defines a quick key to jump to this menu when pressing Alt.
This won't be visible on macOS. Note that this is different from a keyboard shortcut — we'll cover that shortly.
This is where the power of actions comes into play. We can reuse the already existing QAction to add the same function to the menu. To add an action, you call `addAction()` passing in one of our defined actions:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    label = QLabel("Hello!")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setCentralWidget(label)
    toolbar = QToolBar("My main toolbar")
    toolbar.setIconSize(QSize(16, 16))
    self.addToolBar(toolbar)
    button_action = QAction(QIcon("bug.png"), "&Your button", self)
    button_action.setStatusTip("This is your button")
    button_action.triggered.connect(self.toolbar_button_clicked)
    button_action.setCheckable(True)
    toolbar.addAction(button_action)
    toolbar.addSeparator()
    button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
    button_action2.setStatusTip("This is your button2")
    button_action2.triggered.connect(self.toolbar_button_clicked)
    button_action2.setCheckable(True)
    toolbar.addAction(button_action2)
    toolbar.addWidget(QLabel("Hello"))
    toolbar.addWidget(QCheckBox())
    self.setStatusBar(QStatusBar(self))
    menu = self.menuBar()
    file_menu = menu.addMenu("&File")
    file_menu.addAction(button_action)
  def toolbar_button_clicked(self, s):
    print("click", s)

```

**Run it!** Click the item in the menu, and you will notice that it is toggleable — it inherits the features of the `QAction`.
![Menu shown on the window -- on macOS this will be at the top of the screen.](https://www.pythonguis.com/static/tutorials/qt/actions-toolbars-menus/menu-shown-on-window.png) _Menu shown on the window -- on macOS this will be at the top of the screen._
Let's add some more things to the menu. Here, we'll add a separator to the menu, which will appear as a horizontal line in the menu, and then add the second `QAction` we created:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    label = QLabel("Hello!")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setCentralWidget(label)
    toolbar = QToolBar("My main toolbar")
    toolbar.setIconSize(QSize(16, 16))
    self.addToolBar(toolbar)
    button_action = QAction(QIcon("bug.png"), "&Your button", self)
    button_action.setStatusTip("This is your button")
    button_action.triggered.connect(self.toolbar_button_clicked)
    button_action.setCheckable(True)
    toolbar.addAction(button_action)
    toolbar.addSeparator()
    button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
    button_action2.setStatusTip("This is your button2")
    button_action2.triggered.connect(self.toolbar_button_clicked)
    button_action2.setCheckable(True)
    toolbar.addAction(button_action2)
    toolbar.addWidget(QLabel("Hello"))
    toolbar.addWidget(QCheckBox())
    self.setStatusBar(QStatusBar(self))
    menu = self.menuBar()
    file_menu = menu.addMenu("&File")
    file_menu.addAction(button_action)
    file_menu.addSeparator()
    file_menu.addAction(button_action2)
  def toolbar_button_clicked(self, s):
    print("click", s)

```

**Run it!** You should see two menu items with a line between them.
![Our actions showing in the menu.](https://www.pythonguis.com/static/tutorials/qt/actions-toolbars-menus/actions-shown-in-menu.png) _Our actions showing in the menu._
You can also use ampersand to add _accelerator keys_ to the menu to allow a single key to be used to jump to a menu item when it is open. Again this doesn't work on macOS.
To add a submenu, you simply create a new menu by calling `addMenu()` on the parent menu. You can then add actions to it as usual. For example:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    label = QLabel("Hello!")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setCentralWidget(label)
    toolbar = QToolBar("My main toolbar")
    toolbar.setIconSize(QSize(16, 16))
    self.addToolBar(toolbar)
    button_action = QAction(QIcon("bug.png"), "&Your button", self)
    button_action.setStatusTip("This is your button")
    button_action.triggered.connect(self.toolbar_button_clicked)
    button_action.setCheckable(True)
    toolbar.addAction(button_action)
    toolbar.addSeparator()
    button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
    button_action2.setStatusTip("This is your button2")
    button_action2.triggered.connect(self.toolbar_button_clicked)
    button_action2.setCheckable(True)
    toolbar.addAction(button_action2)
    toolbar.addWidget(QLabel("Hello"))
    toolbar.addWidget(QCheckBox())
    self.setStatusBar(QStatusBar(self))
    menu = self.menuBar()
    file_menu = menu.addMenu("&File")
    file_menu.addAction(button_action)
    file_menu.addSeparator()
    file_submenu = file_menu.addMenu("Submenu")
    file_submenu.addAction(button_action2)
  def toolbar_button_clicked(self, s):
    print("click", s)

```

**Run it!** You will see a nested menu in the _File_ menu.
![Submenu nested in the File menu.](https://www.pythonguis.com/static/tutorials/qt/actions-toolbars-menus/submenu-nested-in-file-menu.png) _Submenu nested in the File menu._
Finally, we'll add a keyboard shortcut to the `QAction`. You define a keyboard shortcut by passing `setKeySequence()` and passing in the key sequence. Any defined key sequences will appear in the menu.
Note that the keyboard shortcut is associated with the `QAction` and will still work whether or not the `QAction` is added to a menu or a toolbar.
Key sequences can be defined in multiple ways - either by passing as text, using key names from the `Qt` namespace, or using the defined key sequences from the `Qt` namespace. Use the latter wherever you can to ensure compliance with the operating system standards.
The completed code, showing the toolbar buttons and menus, is shown below:
python ```
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
  QApplication,
  QCheckBox,
  QLabel,
  QMainWindow,
  QStatusBar,
  QToolBar,
)
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    label = QLabel("Hello!")
    # The `Qt` namespace has a lot of attributes to customize
    # widgets. See: http://doc.qt.io/qt-6/qt.html
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    # Set the central widget of the Window. Widget will expand
    # to take up all the space in the window by default.
    self.setCentralWidget(label)
    toolbar = QToolBar("My main toolbar")
    toolbar.setIconSize(QSize(16, 16))
    self.addToolBar(toolbar)
    button_action = QAction(QIcon("bug.png"), "&Your button", self)
    button_action.setStatusTip("This is your button")
    button_action.triggered.connect(self.toolbar_button_clicked)
    button_action.setCheckable(True)
    # You can enter keyboard shortcuts using key names (e.g. Ctrl+p)
    # Qt.namespace identifiers (e.g. Qt.CTRL + Qt.Key_P)
    # or system agnostic identifiers (e.g. QKeySequence.Print)
    button_action.setShortcut(QKeySequence("Ctrl+p"))
    toolbar.addAction(button_action)
    toolbar.addSeparator()
    button_action2 = QAction(QIcon("bug.png"), "Your &button2", self)
    button_action2.setStatusTip("This is your button2")
    button_action2.triggered.connect(self.toolbar_button_clicked)
    button_action2.setCheckable(True)
    toolbar.addAction(button_action2)
    toolbar.addWidget(QLabel("Hello"))
    toolbar.addWidget(QCheckBox())
    self.setStatusBar(QStatusBar(self))
    menu = self.menuBar()
    file_menu = menu.addMenu("&File")
    file_menu.addAction(button_action)
    file_menu.addSeparator()
    file_submenu = file_menu.addMenu("Submenu")
    file_submenu.addAction(button_action2)
  def toolbar_button_clicked(self, s):
    print("click", s)
app = QApplication([])
window = MainWindow()
window.show()
app.exec()

```

Experiment with building your own menus using `QAction` and `QMenu`.
1:1 Coaching & Tutoring for your Python GUIs project
[![Martin Fitzpatrick Python GUIs Coaching & Training](https://www.pythonguis.com/static/theme/images/products/coaching.jpg)](https://calendly.com/martinfitzpatrick/60min-python-guis-coaching)
[60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/) [Book Now](https://www.pythonguis.com/live/)
1:1 Python GUIs Coaching & Training
**Comprehensive code review** • **Bugfixes** & improvements • **Maintainability** advice and **architecture** improvements • **Design and usability** assessment • Suggestions and tips to **expand your knowledge** • **Packaging and distribution** help for Windows, Mac & Linux • [Find out more.](https://www.pythonguis.com/live)
Mark As Complete 
Continue with [ PySide6 Tutorial ](https://www.pythonguis.com/tutorials/pyside6-dialogs/ "Continue to next part")
Return to [Create Desktop GUI Applications with PySide6 ](https://www.pythonguis.com/pyside6-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PySide6 Toolbars & Menus — QAction** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/Python books) on the subject. 
**PySide6 Toolbars & Menus — QAction** was published in [tutorials](https://www.pythonguis.com/tutorials/) on April 11, 2025 . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[menus](https://www.pythonguis.com/topics/menus/) [toolbars](https://www.pythonguis.com/topics/toolbars/) [QMenu](https://www.pythonguis.com/topics/qmenu/) [QAction](https://www.pythonguis.com/topics/qaction/) [QToolbar](https://www.pythonguis.com/topics/qtoolbar/) [actions](https://www.pythonguis.com/topics/actions/) [qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [ foundation](https://www.pythonguis.com/topics/foundation/) [ pyside6-foundation](https://www.pythonguis.com/topics/pyside6-foundation/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
