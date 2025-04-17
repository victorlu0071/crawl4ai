# Content from: https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/

[](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PySide2 ](https://www.pythonguis.com/pyside2/)
  * [PySide2 Tutorial ](https://www.pythonguis.com/pyside2-tutorial/)
  * Basics
  * [Create a PySide2 app](https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/)
  * [PySide2 Signals](https://www.pythonguis.com/tutorials/pyside-signals-slots-events/)
  * [PySide2 Widgets](https://www.pythonguis.com/tutorials/pyside-widgets/)
  * [PySide2 Layouts](https://www.pythonguis.com/tutorials/pyside-layouts/)
  * [PySide2 Menus](https://www.pythonguis.com/tutorials/pyside-actions-toolbars-menus/)
  * [PySide2 Dialogs](https://www.pythonguis.com/tutorials/pyside-dialogs/)
  * [Multi-window PySide2](https://www.pythonguis.com/tutorials/pyside-creating-multiple-windows/)
  * Qt Designer
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/)
  * [The QResource System in PySide2](https://www.pythonguis.com/tutorials/pyside-qresource-system/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/pyside-qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/pyside-modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/pyside-qtableview-modelviews-numpy-pandas/)
  * Plotting
  * [Plotting With PyQtGraph and PySide2](https://www.pythonguis.com/tutorials/pyside-plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PySide2](https://www.pythonguis.com/tutorials/pyside-plotting-matplotlib/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/pyside-bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/pyside-creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/pyside-animated-widgets/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/pyside-embed-pyqtgraph-custom-widgets/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/pyside-transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/pyside-system-tray-mac-menu-bar-applications/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyside2-applications-windows-pyinstaller/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyside2-applications-pyinstaller-macos-dmg/)
  * [Packaging QResources](https://www.pythonguis.com/tutorials/packaging-data-files-pyside2-with-qresource-system/)
  * [Packaging with fbs](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/)
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


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Creating Dialogs With Qt Designer and PySide2
Using the drag and drop editor to build PySide2 dialogs
by [Leodanis Pozo Ramos](https://www.pythonguis.com/authors/leodanis-pozo-ramos/) Last updated Mar 17 PySide2 [ Creating applications with Qt Designer ](https://www.pythonguis.com/pyside2-tutorial/#pyside-qt-designer)
#### [ PySide2 Tutorial ](https://www.pythonguis.com/pyside2-tutorial/) — [Creating applications with Qt Designer](https://www.pythonguis.com/pyside2-tutorial/#pyside-qt-designer)
  * [First Steps With Qt Designer and PySide2](https://www.pythonguis.com/tutorials/pyside-first-steps-qt-designer/)
  * [Creating Dialogs With Qt Designer and PySide2](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/)
  * [The QResource System in PySide2](https://www.pythonguis.com/tutorials/pyside-qresource-system/)


This tutorial is also available for [PySide6](https://www.pythonguis.com/tutorials/pyside6-creating-dialogs-qt-designer/) , [PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-dialogs-qt-designer/) and [PyQt5](https://www.pythonguis.com/tutorials/creating-dialogs-qt-designer/)
Most PySide GUI applications consist of a main window and several dialogs. [Dialogs](https://www.pythonguis.com/tutorials/pyside-dialogs/) are small-sized windows that allow you to communicate with your users, either by showing messages on the screen or by taking the user's input. You can use [Qt Designer](https://www.pythonguis.com/tutorials/pyside-first-steps-qt-designer/) to create dialogs taking advantage of the variety of options that this tool offers.
In this tutorial, we'll learn how to create and customize dialogs using Qt Designer. We'll also learn two different ways of using and launching dialogs in our GUI applications. With this knowledge, we'll be able to add dialogs to our applications quickly and easily.
For a better understanding of the topics we'll cover in this tutorial, it will help to have some previous knowledge about [PySide applications](https://www.pythonguis.com/courses/pyside-getting-started/), [widgets](https://www.pythonguis.com/tutorials/pyside-widgets/), [layouts](https://www.pythonguis.com/tutorials/pyside-layouts/) and [signals and slots](https://www.pythonguis.com/tutorials/pyside-signals-slots-events/).
Table of Contents
  * [Getting Started With PySide Dialogs](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/#getting-started-with-pyside-dialogs)
  * [Creating Dialogs With Qt Designer](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/#creating-dialogs-with-qt-designer)
    * [Using Qt Designer's Dialog Templates](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/#using-qt-designers-dialog-templates)
    * [Adding Widgets and Layouts](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/#adding-widgets-and-layouts)
    * [Setting Tab Order of Input Widgets](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/#setting-tab-order-of-input-widgets)
    * [Defining Buddies](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/#defining-buddies)
    * [Using Button Boxes to Lay Out Dialog's Buttons](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/#using-button-boxes-to-lay-out-dialogs-buttons)
    * [Connecting Built-in Signals and Slots](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/#connecting-built-in-signals-and-slots)
  * [Using Dialogs in a GUI Application](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/#using-dialogs-in-a-gui-application)
    * [Generating the Dialog's GUI With pyside2-uic](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/#generating-the-dialogs-gui-with-pyside2-uic)
    * [Loading the Dialog's GUI With uic.loadUi()](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/#loading-the-dialogs-gui-with-uicloadui)
  * [Conclusion](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/#conclusion)


## Getting Started With PySide Dialogs
In GUI programming, [dialogs](https://www.pythonguis.com/tutorials/pyqt-dialogs/) are small-sized windows that offer auxiliary functionalities and allow you to communicate with your users. Some common examples of dialogs include the _Open Document_ dialog in a word processor or a text editor, the _Settings_ or _Preferences_ dialogs in most GUI applications, the _Search_ dialog in a file manager or a text editor, and so on.
Dialogs are also often used to show error messages or general information on a given operation. They can also be used to ask the users their confirmation to continue with an operation or to take input from the user for a database.
PySide offers a rich collection of built-in dialog classes that you can use directly in your applications. Some of them are:
  * [QFontDialog](https://doc.qt.io/qt-5/qfontdialog.html) for selecting a font
  * [QPrintDialog](https://doc.qt.io/qt-5/qprintdialog.html) for specifying the printer's configuration
  * [QProgressDialog](https://doc.qt.io/qt-5/qprogressdialog.html) for providing feedback on the progress of a slow operation
  * [QColorDialog](https://doc.qt.io/qt-5/qcolordialog.html) for specifying colors
  * [QInputDialog](https://doc.qt.io/qt-5/qinputdialog.html) for getting a single value from the user
  * [QFileDialog](https://doc.qt.io/qt-5/qfiledialog.html) for selecting files or directories


Additionally, PySide provides the [QDialog](https://doc.qt.io/qt-5/qdialog.html) class for creating entirely custom dialogs when there is no built-in available for the operation that you need to perform. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyside2-book/) _by Martin Fitzpatrick_ — (PySide2 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside2-book/) [Get the book](https://secure.pythonguis.com/01hf778jyaajk5vk1q6824sd44/)
While we can use the `QDialog` class to build dialogs in Python code, we can also use [Qt Designer](https://www.pythonguis.com/tutorials/pyside-first-steps-qt-designer/) to create custom dialogs in the drag and drop editor. Qt Designer is a [Qt](https://www.qt.io/) tool that offers a user-friendly GUI that will allow us to quickly create and set up our dialogs and windows.
## Creating Dialogs With Qt Designer
You can use Qt Designer to create and customize the user interface of your custom dialogs. With Qt Designer, you can create a dialog's GUI using a built-in template or you can create a dialog entirely from scratch. You can add widgets to your dialogs, [arrange widgets in layouts](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/), set their appearance, provide initial values for their attributes, set their tab order, create buddies to provide keyboard shortcuts, and connect the widgets' built-in signals to slots.
When we create a dialog using Qt Designer, the dialog's GUI is stored in a `.ui` file, which is an `XML` file that provides all the information we'll need to later build the dialog GUI in our applications.
In the next few sections we'll look at how to create and customize dialog's GUI using Qt Designer.
### Using Qt Designer's Dialog Templates
When we launch Qt Designer, we are presented with the application's main window and with a dialog called **New Form**. This dialog allows us to select a template for the GUI we want to create. These templates include options to create dialogs, main windows, and custom widgets.
In this tutorial, we're just interested in how to create dialogs with Qt Designer. So, we'll just cover the 3 templates Qt Designer offers for creating dialogs:
  1. **Dialog with Buttons Bottom** to create a form (or dialog) with an `OK` and a `Cancel` buttons horizontally-arranged on the bottom-right corner of the form
  2. **Dialog with Buttons Right** to create a form with an `OK` and a `Cancel` buttons vertically-arranged on the top-right corner of the form
  3. **Dialog without Buttons** to create an empty form without buttons


The following screencast shows how we can use Qt Designer to create custom dialogs using the different (default) dialog templates:
To create a dialog using a Qt Designer's template, we just need to select the desired template from the **New Form** dialog and then click on the `Create` button or hit `Alt+R` on our keyboard.
If when you launch Qt Designer, the **New Form** dialog doesn't appear, then you can click on the **New** button on Qt Designer's toolbar. You can also click on the **File >New...** main menu option or press the `Ctrl+N` key combination on your keyboard.
### Adding Widgets and Layouts
Widgets are the building blocks of any PySide GUI application. You can use widgets to display information, get the user's input, and provide containers for other widgets that should be grouped. With Qt Designer, you can add widgets to our dialogs and windows by dragging and doping them from Qt Designer's **Widget Box** panel to your form. Once you have all the required widgets in place, you can [arrange them using Qt's layouts](https://www.pythonguis.com/tutorials/qt-designer-gui-layout/).
Say your company is creating a database application to manage the employees' relevant information. You're asked to add a new PySide dialog to enter or update general information about employees. The dialog must include options to enter the following info: _Employee name_ , _Employment date_ , _Department_ , _Position_ , _Annual salary_ and _Job description_.
The following screencast shows how we can quickly create the GUI for the dialog at hand using Qt Designer:
Here, we first create a dialog using the **Dialog with Buttons Bottom** template. Then, we add `QLabel` objects to ask for the needed information. Every field needs a specific input widget. For example, we add a `QLineEdit` object for the Employee name, a `QDateEdit` object for the Employment date, two `QComboBox` objects for the Department and the Position, a `QDoubleSpinBox` object for the Annual salary, and a `QTextEdit` object for the Job description field.
Once we have all the widgets in place, we select all of them and arrange them using a `QFormLayout` object. The final step is to add a main layout to the dialog. To do that, we use a `QVBoxLayout` object that allows us to arrange the widgets and the dialog's buttons in a vertical column. That's all, we've created our first dialog using Qt Designer. Let's save the dialog's GUI file with the name `employee.ui` for later use.
If you want to have a preview of how your dialog will look like in production, then you can press the `Ctrl+R` key combination or click on the **Form >Preview...** option on Qt Designer's main menu.
In this section, we've used Qt Designer in **Edit Widgets** mode, which is the default mode. In this mode, we can add widgets to our dialogs, edit widget's properties, lay out the widgets on the dialog's GUI, and so on. To activate the Edit Widgets mode, we can choose any of the three following options:
  1. Press the `F3` key
  2. Select the **Edit >Edit Widgets** option from the main menu
  3. Click on the **Edit Widgets** button on Qt Designer's toolbar.


### Setting Tab Order of Input Widgets
An element that can improve the usability of your dialogs is the **tab order** of the input widgets. The tab order is the order in which the input widgets get the focus when you hit the `Tab` or `Shift+Tab` keys. The default tab order is based on the order in which you place the widgets on the form.
For example, in our employee dialog, we placed the `QDoubleSpinBox` object for the _Annual salary_ after the `QTextEdit` object for the _Job description_. If the user hits the `Tab` key for moving around the dialog, then they'll note that when they hit `Tab` to move from the _Position_ `QComboBox` to the _Annual salary_ `QDoubleSpinBox` what happens is that the focus goes to the _Job description_ `QTextEdit`. This is a kind of annoying behavior. The following screencast shows the problem:
Note that when the focus is on the _Position_ `QComboBox` and the user hits `Tab`, the focus jumps directly to the _Job description_ `QTextEdit` instead of jumping to the _Annual Salary_ `QDoubleSpinBox` as we would expect.
To fix this problem, we need to change the tab order of the input widgets on our dialog. Firstly, we need to switch to the **Edit Tab Order** mode in Qt Designer. To do that, we can either select the **Edit >Edit Tab Order** option on the main menu or click on the **Edit Tab Order** button on the toolbar.
In Edit Tab Order mode, each input widget in the form is shown with a number that indicates its position in the tab order chain. We can change the tab order by clicking on the number of each widget in the correct order. You can see how to do this in the following screencast:
In this example, we change the tab order of the input widgets by clicking on each number in the correct order. When we select a number, it changes to red to indicate that this is the currently edited position in the tab order. When we click on another number, then that number will be second in the tab order, and so on.
In case of a mistake, we can restart numbering by choosing **Restart** from the form's context menu. To partially edit the tab order, we can select a number with the `Ctrl` key pressed. The tab order will be changed from that widget on. We can also right-click on a given number and then choose **Start from Here** from the context menu.
### Defining Buddies
In Qt, buddies are connections between related widgets. Normally between a `QLabel` widget and an input widget like a `QLineEdit` or a `QComboBox`. These connections allow you to provide a quick keyboard shortcut to move the focus to a given input widget. By setting buddies, you'll improve the usability of your dialogs because you'll provide the user with a fast way to move around dialogs and windows.
In our employee dialog, to move the focus to the _Annual salary_ `QDoubleSpinBox`, we can set a buddy between it and the _Annual salary_ `QLabel` widget. The buddy will automatically provide a key combination of the form `Alt+Letter`, in which `Letter` represents a single letter in the text of the label.
In our _Annual salary_ `QLabel`, that letter could be `A` or `s` or any other letter in the text of the label. The only restriction is that the selected letter doesn't clash with the letter of any other buddy in the dialog or window at hand.
To select a letter to use in our buddy, we need to place an ampersand (`&`) before the letter in the text of the label. With this addition, we provide the letter to use in the keyboard shortcut. For example, if we place the ampersand before the letter `s` in our _Annual salary_ `QLabel`, then we'll be able to access the _Annual salary_ `QDoubleSpinBox` by hitting the `Alt+S` shortcut on our keyboard.
Once we have selected the letters to use and placed the corresponding ampersands, we need to set the buddies. To do that, we'll activate the **Edit Buddies** mode in Qt Designer by either selecting the **Edit >Edit Buddies** option from the main menu or by clicking the **Edit Buddies** button on the toolbar.
To define the buddies, we'll click on a label and drag it over the corresponding input widget. The whole process is illustrated in the following screencast:
To create buddies between labels and input widgets, we can select a label with our mouse and drag it to the input widget that we want to set as its buddy. The label and the input widget will become buddies. From this point on, our users will be able to quickly move the focus to a specific input widget by pressing `Alt+Letter`, where `Letter` will be the letter that we used to define the buddy relation. Note that the buddy letters will be underlined to point the right key combination to use.
### Using Button Boxes to Lay Out Dialog's Buttons
There is a standard set of buttons that you can use when it comes to creating dialogs. Even though Qt Designer's templates provide an `OK` button and a `Cancel` button, in practice you'll see dialogs that use different buttons like `Apply`, `Close`, `Yes`, `No`, and so on.
In our employee example, we've used a `Cancel` and an `OK` button, which were placed in that same order from left to right. This is the usual order for buttons on Linux or macOS but not for Windows, where the order should be swapped.
If we want that our GUI applications look as native as possible on different platforms, then we'll need to deploy different dialogs for different platforms just to show the buttons in the right order for the platform at hand.
Fortunately, PySide provides an effective solution for this particular problem. Instead of adding a `Cancel` and an `OK` button directly, we can use the [`QDialogButtonBox`](https://doc.qt.io/qt-5/qdialogbuttonbox.html) class and select the buttons according to our needs. This PySide class will automatically handle the order of the buttons for us according to the standard practice on the underlying platform.
Here's how our employee dialog looks like on Windows 10, Linux, and macOS:
![Button Box on Windows](https://www.pythonguis.com/static/tutorials/qt/creating-dialogs-qt-designer/button-box-window.png) _Button Box on Windows_
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
![Button Box on Linux](https://www.pythonguis.com/static/tutorials/qt/creating-dialogs-qt-designer/button-box-linux.png) _Button Box on Linux_
![Button Box on macOS](https://www.pythonguis.com/static/tutorials/qt/creating-dialogs-qt-designer/button-box-macos.png) _Button Box on macOS_
n Windows, the buttons at the bottom-right corner of the dialog are shown swapped if you compare them with the same dialog running on Linux or macOS. That's because Qt Designer's dialog templates use a `QDialogButtonBox` object by default to lay out the buttons on the dialog. This is quite convenient if you're creating multi-platform GUI applications with PySide.
We can select the buttons that we want to show on our dialogs by changing the `.standardButtons` property of the `QDialogButtonBox` object on Qt Designer's **Property Editor**. Take a look at the following screencast:
The Property Editor allows us to set the `.standardButtons` property of a `QDialogButtonBox` object and to select different sets of standard buttons. Note that when we change the buttons in the `QDialogButtonBox`, they get placed according to the standard practice on the current platform.
### Connecting Built-in Signals and Slots
In PySide, the user's actions over the widget of a GUI applications are called **events**. When an event occurs, the widget at hand emits a **signal** to let you know that the event has occurred. To give life to your applications, you need to connect those signals to specific **slots**. Slots are methods that are executed as a response to events.
Most widgets implement built-in signals that are emitted when a given event (like a mouse click) occurs on the widget. Widgets also provide built-in slots that allow you to perform certain actions on the widget. For example, a `QTextEdit` object provides a `.clear()` slot that you can connect to a button or to a menu option to clear the content of the widget.
You can use Qt Designer to connect these built-in signals and slots. To establish a signal and slot connection between two widgets in a dialog, you first need to switch to Qt Designer's **Edit Signals/Slots** mode. To do that, you can press the `F4` key, select the **Edit >Edit Signals/Slots** option in the main menu, or click on the **Edit Signals/Slots** button on the toolbar.
Once in the Edit Signals/Slots mode, you select the signal-provider widget with your mouse and then drag and drop this widget over the slot-provider widget. This will launch Qt Designer's **Configure Connection** dialog.
The Configure Connection dialog has two panels. In the left panel, you can select a signal and in the right panel, you can select a slot. Then, you need to press the `OK` button to create the connection. This will draw an arrow from the signal-provider widget to the slot-provider widget indicating that the connection is established. Additionally, you'll see the name of the signal and the slot that you just connect.
For example, suppose we have a dialog with a `QTextEdit` and a `QPushButton`. We need to connect the `.clicked()` signal of the button with the `.clear()` slot of the text edit, so we can clear the content of the text edit by clicking on the button. Check out the following example:
In this example, we first switch to the Edit Signals/Slots mode. Then, we select the `Clear` button, drag it, and drop it over the `QTextEdit` object. This presents us with the Configure Connection dialog. In this dialog, we select the `.clicked()` signal in the left panel and the `.clear()` slot in the right panel. When we press `OK`, the connection gets established. We can also click on the `Cancel` button to cancel the connection operation.
The connection appears as an arrow connecting the two widgets with two labels indicating the name of the signal and the slot that each widget provides.
To modify a connection, you can double-click on the arrow or one of the labels. This will display the Configure Connection dialog, where you can change the signal or the slot involved in the connection.
To delete a connection, you can select the arrow that represents the connection or one of the labels that identify the signal and the slot, and then press the `Del` key.
Since dialogs are also widgets, you can connect a signal of a widget (say a button) with a slot of the dialog or form. The process is the same, you just need to drag and drop the widget over the form and then configure the desired signal and slot from the Configure Connection dialog.
Finally, if you use a Qt Designer's template for creating a dialog with a button box, then you'll note that the `.accepted()` signal of the `QDialogButtonBox` object is connected by default with the `.accept()` slot of the form. Likewise, the `.rejected()` signal is connected with the `reject()` slot. So, your dialog is fully functional from the very beginning.
## Using Dialogs in a GUI Application
So far, you've learned how to create custom dialogs with Qt Designer but how can you use those dialogs in your GUI applications? PySide provides at least two ways for doing that. We can:
  1. Generate the Python code for the dialog's GUI using a command-line tool called `pyside2-uic` on the `.ui` file
  2. Dynamically load the code for the dialog's GUI using the `QtUiTools.QUiLoader` class


The first option is the most common and widely used because it's more efficient when it comes to working with complex dialogs. However, it has the drawback that every time you modify the dialog with Qt Designer, you have to generate the code again.
The second option may be suitable when you're working with quite small and simple dialogs that don't involve substantial loading time.
### Generating the Dialog's GUI With `pyside2-uic`
You can use the command-line tool `pyside2-uic` to convert your `.ui` files into `.py` files that contain the Python code to build your dialogs' GUI. To do that, you need to open a command-line or terminal and run a command like this:
```sh:PySide2 $ pyside2-uic -o dialog.py dialog.ui
python ```

This command will generate a Python module called `dialog.py` from the `dialog.ui` file that we just created using Qt Designer.
Let's run the command targeting our employee dialog:
```sh:PySide2
$ pyside2-uic -o employee_dlg.py employee.ui

```

This command generates a Python module called `employee_dlg.py`. This module contains the Python code for the dialog's GUI. Here's a small piece of the code:
python ```
# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_Dialog(object):
  def setupUi(self, Dialog):
    if not Dialog.objectName():
      Dialog.setObjectName(u"Dialog")
    Dialog.resize(431, 431)
    self.verticalLayout = QVBoxLayout(Dialog)
    ...

```

The `Ui_Dialog` class has all the code we need to generate the dialog's GUI. The `.setupUi()` method contains the code that adds the widgets and lay them out on the dialog's GUI. The `retranslateUi()` method contains code for internationalization and localization but this topic is beyond the scope of this tutorial. So, we'll just consider `.setupUi()` here.
Let's create a [PySide main window-style application](https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/) that allows us to use this Python module for launching our employee dialog. Here's the code:
python ```
import sys
from PySide2.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
from employee_dlg import Ui_Dialog
class Window(QMainWindow):
  """Main window."""
  def __init__(self, parent=None):
    """Initializer."""
    super().__init__(parent)
    # Use a QPushButton for the central widget
    self.centralWidget = QPushButton("Employee...")
    # Connect the .clicked() signal with the .onEmployeeBtnClicked() slot
    self.centralWidget.clicked.connect(self.onEmployeeBtnClicked)
    self.setCentralWidget(self.centralWidget)
  # Create a slot for launching the employee dialog
  def onEmployeeBtnClicked(self):
    """Launch the employee dialog."""
    dlg = EmployeeDlg(self)
    dlg.exec()

class EmployeeDlg(Ui_Dialog, QDialog):
  """Employee dialog."""
  def __init__(self, parent=None):
    super().__init__(parent)
    # Run the .setupUi() method to show the GUI
    self.setupUi(self)

# Create the application
app = QApplication(sys.argv)
# Create and show the application's main window
w = Window()
w.show()
# Run the application's main loop
app.exec_()

```

We first import the required classes from the PySide package. Then, we import the `Ui_Dialog` class from our `employee_dlg` module.
The `Window` class will be the main window of our application. In this case, we use a `QPushButton` as a central widget. This means that our application will show a window with a single button on it. Then, we'll connect the `.clicked()` signal of the button with the `onEmployeeBtnClicked()` slot.
Inside `onEmployeeBtnClicked()`, we create an instance of `EmployeeDlg` using our main window (`self`) as its `parent` and then launch it using its `.exec()` method.
In the `EmployeeDlg` class, we implement our dialog inheriting from the `QDialog` and `Ui_Dialog` classes. Inside the `__init__()` method, we call the `.setupUi()` method to apply the designed UI to our class.
Finally, we complete the application by running the following steps:
  1. Create an instance of the `QApplication` class
  2. Create an instance of our `Window` class
  3. Call the `.show()` method on our `Window` object
  4. Run the application's main loop calling `app.exec()`


Let's run the application and click on the `Employee...` button. Here's how it works:
The application's main window has a single widget, the `Employee...` button. When we click on this button, our employee dialog appears on the screen.
The final ellipsis in the text of the `Employee...` button is a common convention that you can use to point that this button (or menu option) doesn't perform an immediate action but launches a dialog for further processing.
Even though we used a `QPushButton` to launch our dialog, in real-world applications we normally connect a slot like `onEmployeeBtnClicked()` to a toolbar button, a main menu option, or a context menu option.
### Loading the Dialog's GUI With `uic.loadUi()`
You also have the option of dynamically loading the dialog's GUI directly from your `.ui` file using the `uic.loadUi()` function. `uic.loadUi()` takes a `.ui` file as an argument and returns a `QWidget` subclass that implements the GUI.
To dynamically load our employee dialog, for example, we need to make some changes to our `employeeapp.py` file.
python ```
import sys
from PySide2.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
from PySide2.QtUiTools import QUiLoader
loader = QUiLoader()
class Window(QMainWindow):
  """Main window."""
  def __init__(self, parent=None):
    """Initializer."""
    super().__init__(parent)
    # Use a QPushButton for the central widget
    self.centralWidget = QPushButton("Employee...")
    # Connect the .clicked() signal with the .onEmployeeBtnClicked() slot
    self.centralWidget.clicked.connect(self.onEmployeeBtnClicked)
    self.setCentralWidget(self.centralWidget)
  # Create a slot for launching the employee dialog
  def onEmployeeBtnClicked(self):
    """Launch the employee dialog."""
    dlg = loader.load("dialog.ui", None)
    dlg.exec_()

# Create the application
app = QApplication(sys.argv)
# Create and show the application's main window
w = Window()
w.show()
# Run the application's main loop
app.exec_()

```

Rather than subclass to use the dialog, we can now load the UI object and call `exec_()` on it directly. With this last change, we're done. Our application will work as expected. The rest of the code remains the same. You can now run the application by yourself and see the result.
This way of loading dialogs is rarely used in practice, although it may be useful when you're working with simple and small dialogs. It has the advantage that you don't need to generate the Python code for the dialog's GUI every time you modify the `.ui` file using Qt Designer, which can be a productivity and maintainability win in some cases.
## Conclusion
When it comes to creating PySide GUI applications you commonly use a main window and several dialogs. [Dialogs](https://www.pythonguis.com/tutorials/pyside-dialogs/) allow you to communicate with your users (hence the name dialog). You can use dialogs to show messages on the screen or to take the user's input. [Qt](https://www.qt.io/) provides [Qt Designer](https://www.pythonguis.com/tutorials/pyside-first-steps-qt-designer/) for creating dialogs in a fast and productive way.
In this tutorial, we covered how to create and customize dialogs using Qt Designer. We also learned about two different ways of using and launching dialogs in our GUI applications, either by generating the dialog's GUI code or by loading it dynamically.
With this knowledge, you'll be able to use Qt Designer to create fully-functional dialogs for your GUI applications in a quick and productive way.
1:1 Coaching & Tutoring for your Python GUIs project
[![Martin Fitzpatrick Python GUIs Coaching & Training](https://www.pythonguis.com/static/theme/images/products/coaching.jpg)](https://calendly.com/martinfitzpatrick/60min-python-guis-coaching)
[60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/) [Book Now](https://www.pythonguis.com/live/)
1:1 Python GUIs Coaching & Training
**Comprehensive code review** • **Bugfixes** & improvements • **Maintainability** advice and **architecture** improvements • **Design and usability** assessment • Suggestions and tips to **expand your knowledge** • **Packaging and distribution** help for Windows, Mac & Linux • [Find out more.](https://www.pythonguis.com/live)
Mark As Complete 
Continue with [ PySide2 Tutorial ](https://www.pythonguis.com/tutorials/pyside-qresource-system/ "Continue to next part")
Return to [Create Desktop GUI Applications with PySide2 ](https://www.pythonguis.com/pyside2-tutorial/)
[![Leodanis Pozo Ramos](https://www.pythonguis.com/static/theme/images/authors/leodanis-pozo-ramos.jpg)](https://www.pythonguis.com/authors/leodanis-pozo-ramos/)
**Creating Dialogs With Qt Designer and PySide2** was written by [Leodanis Pozo Ramos](https://www.pythonguis.com/authors/leodanis-pozo-ramos/) . 
**Creating Dialogs With Qt Designer and PySide2** was published in [tutorials](https://www.pythonguis.com/tutorials/) on September 18, 2020 (updated March 17, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ qt-designer](https://www.pythonguis.com/topics/qt-designer/) [qt-creator](https://www.pythonguis.com/topics/qt-creator/) [qdialog](https://www.pythonguis.com/topics/qdialog/) [dialog](https://www.pythonguis.com/topics/dialog/) [qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [ pyside2-qt-designer](https://www.pythonguis.com/topics/pyside2-qt-designer/) [python](https://www.pythonguis.com/topics/python/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
