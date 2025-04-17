# Content from: https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/

[](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/#menu)
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
# Laying Out Your PySide2 GUIs With Qt Designer
Use Qt Designer to effortlessly build your application UI
by [Leodanis Pozo Ramos](https://www.pythonguis.com/authors/leodanis-pozo-ramos/) Last updated Mar 03 PySide2 [ Tutorials ](https://www.pythonguis.com/tutorials/)
This tutorial is also available for [PySide6](https://www.pythonguis.com/tutorials/pyside6-qt-designer-gui-layout/) , [PyQt6](https://www.pythonguis.com/tutorials/pyqt6-qt-designer-gui-layout/) and [PyQt5](https://www.pythonguis.com/tutorials/qt-designer-gui-layout/)
When laying out your PySide2 GUIs it can be quite a tricky task to place every widget in the right position on your forms. Fortunately, Qt offers a set of layout managers that simplify the process of widget positioning and will allow you to easily create any kind of layout. To lay out the widget in a form, you can [create everything in code](https://www.pythonguis.com/tutorials/pyside-layouts/), or you can create your layout with Qt Designer. In this tutorial, you'll learn how to use Qt's layouts with Qt Designer to build complex GUIs for your applications.
Additionally, we'll create a dialog example using several widgets with a coherent layout to reinforce your knowledge and put everything together into a fully functional dialog just like you would create in a real-world application.
Table of Contents
  * [Using Layouts With Qt Designer](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/#using-layouts-with-qt-designer)
    * [Horizontal Layouts, QHBoxLayout](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/#horizontal-layouts-qhboxlayout)
    * [Vertical Layouts, QVBoxLayout](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/#vertical-layouts-qvboxlayout)
    * [Grid Layouts, QGridLayout](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/#grid-layouts-qgridlayout)
    * [Form Layouts, QFormLayout](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/#form-layouts-qformlayout)
    * [Splitter Layouts](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/#splitter-layouts)
  * [Building Other Layouts With Qt Designer](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/#building-other-layouts-with-qt-designer)
    * [Inserting Objects into an Existing Layout](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/#inserting-objects-into-an-existing-layout)
    * [Nesting Layouts to Build Complex GUIs](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/#nesting-layouts-to-build-complex-guis)
  * [Setting a Top Level or Main Layout](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/#setting-a-top-level-or-main-layout)
  * [Laying Out a Dialog With Qt Designer](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/#laying-out-a-dialog-with-qt-designer)
  * [Using the designed UI in Python](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/#using-the-designed-ui-in-python)
  * [Conclusion](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/#conclusion)


## Using Layouts With Qt Designer
[Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html) is the Qt tool for designing and creating graphical user interfaces (GUI) for desktop applications. With Qt Designer, you can create windows, dialogs, and forms. It allows you to add different kind of widgets to create your GUIs using on-screen forms and a drag-and-drop based interface.
Qt Designer's main interface looks as follows —
![Qt Designer — Main Interface](https://www.pythonguis.com/static/tutorials/qt/qt-designer-gui-layout/qt-designer-gui.png) _Qt Designer — Main Interface_
Qt Designer has a clear and user-friendly interface that allows you to create any kind of GUI by dragging widget onto an empty form. After you place all the widgets on your form, you need to place them in a coherent layout. This will ensure that all your widgets will be displayed and resized properly when the form is previewed or used in an application.
Qt's layout managers are structured containers which automatically arrange child widgets ensuring that they make good use of the available space. Placing widgets within a layout manager automatically lays them out according to the defined rules. One of Qt Designer's most useful features is the ability to drag and drop hierarchies of layout managers to arrange widgets into clean and functional interfaces. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
In Qt Designer, you can create layout objects by applying a layout to a group of existing widgets. Although it's _possible_ to drag layouts onto a form and then drag widgets into the layouts, this can be a bit fiddly. The best practice is to instead drag all the widgets and spacers you need onto the form and then select related widgets and spacers and apply the layouts to them. Use the following steps —
  1. Drag and drop the widgets on the form trying to place them near their desired position
  2. Select the widgets that should be managed with a given layout, by holding the `Ctrl` key and clicking on them
  3. Apply the appropriate layout (horizontal, vertical, grid, or form) using Qt Designer's toolbar, main menu, or the form's context menu


Before you go into an example, take a look at the layout related options that Qt Designer offers —
  1. Use layout options on the main toolbar
  2. Use layout options on the main menu
  3. Use layout options on the form's context menu


The most accessible way for creating layouts is using the layout section of Qt Designer's main toolbar. This section looks as follows —
![Qt Designer —&nbsp;Layout toolbar](https://www.pythonguis.com/static/tutorials/qt/qt-designer-gui-layout/layout-toolbar.png) _Qt Designer — Layout toolbar_
From left to right, you'll find the following buttons —
  * **Lay Out Horizontally** arranges selected widgets in a horizontal layout next to each other (Key combination, `Ctrl+1`). This option uses a standard `QHBoxLayout` object
  * **Lay Out Vertically** arranges selected widgets in a vertical layout, one below another (key combination, `Ctrl+2`). This option uses a standard `QVBoxLayout` object
  * **Lay Out Horizontally in Splitter** arranges the widgets horizontally using a splitter (Key combination, `Ctrl+3`)
  * **Lay Out Vertically in Splitter** arranges the widgets vertically using a splitter (Key combination, `Ctrl+4`)
  * **Lay Out in a Grid** arranges widgets in a table-like grid (rows and columns). By default, each widget occupies one cell of the grid, but you can modify this behavior and make the widgets to span several cells (Key combination, `Ctrl+5`). This option uses a standard `QGridLayout` object
  * **Lay Out in a Form Layout** arranges selected widgets in a two-column layout. The left column is usually for labels asking for some information and the right column includes widgets for entering, editing, or showing that information (Key combination, `Ctrl+6`)
  * **Break Layout** this key allows you to brake an existing layout. Once widgets are arranged in a layout, you cannot move and resize them individually, because their geometry is controlled by the layout. To modify individual widgets, you'll need to break the layout and redo it later (Key combination `Ctrl+0`)
  * **Adjust Size** adjusts the size of the layout to accommodate contained widgets and to ensure that each has enough space to be visible (Key combination `Ctrl+J`)


These same layout related options are also available through Qt Designer's main menu under the `Form` menu and through the form's context menu, so you can choose the one you like better.
Now we have the theory out of the way, we can put these layouts into practise. In the next few sections, we'll be using Qt Designer to lay out the widgets on our forms and build nice and elegant GUIs for your desktop applications. But before we start experimenting with the different layout managers that Qt offers, we're first going to create a custom widget to visualize the layouts as we go through this tutorial.
The completed .ui file can be downloaded below if you would like to skip this step.
[layout-labels.ui](https://www.pythonguis.com/d/layout-labels.ui)
Go ahead and fire up your Qt Designer, then run the following steps —
  1. Select `Widget` at the `templates/forms` tab of the `New Form` dialog. This will create a new empty form to work on.
  2. Save your form as `layout-labels.ui`.
  3. Look for a Label widget on the `Widget Box` and drag it onto the form.
  4. Go to the `Property Editor` and set the `text` property to `0`.
  5. Open the `Text Edit` dialog and set the text color to white. Set the font size to `20` points and justify the text. Press `OK` to apply the changes.
  6. Go to the `Property Editor` and set the `autoFillBackground` property to `True` by selecting the check box.
  7. Look up the `palette` property and open the `Edit Palette` dialog. Use the `Quick` option to set the color to red.


If you feel lost, take a look at the following screencast to see the steps in action —
In this example, you create a new window based on the `Widget` template. Then, you add a Label, set its `text` property to `0`, and set its background color to red.
To complete this example, repeat all the steps to add three more labels with their respective text set to `1`, `2`, and `3` and their colors set to green, yellow, and blue. You'll end up with a form like this:
![Qt Designer —&nbsp;Form with colored labels](https://www.pythonguis.com/static/tutorials/qt/qt-designer-gui-layout/form-labels.png) _Qt Designer — Form with colored labels_
The above screenshot shows the initial form that you'll use for the next few sections. It's a clean form with four label objects on it. You can set a background color to each label to be able to see and differentiate them more easily in the following sections.
### Horizontal Layouts, `QHBoxLayout`
You can use a horizontal layout manager ([QHBoxLayout](https://doc.qt.io/qt-5/qhboxlayout.html)) to arrange the widgets in one row. To create this kind of layout in code, you need to instantiate the `QHBoxLayout` class and then add your widgets to the layout object. In Qt Designer it's easier to work in the other way around.
With your `layout-labels.ui` file open, first select all your labels. To do this, you can click each widget in turn while you hold the `Ctrl` key or you can also click and drag with the mouse pointer inside the form to select the widgets.
Once you have selected the widgets, put them in a horizontal layout by selecting the `Lay Out Horizontally` button in the Qt Designer's main toolbar. You can also use the option `Lay out->Lay Out Horizontally` from the context menu shown below or you can press `Ctrl+1`. The following screencast will guide you through these steps —
If the layout is wrong, then you can easily undo everything and restart laying things out again. To undo things, you can press `Ctrl+z` or use the `Edit` menu from Qt Designer's main menubar. If that isn't possible or doesn't work, then you can just break the layout using the `Break Layout` button from Qt Designer's main toolbar. Another way to break a layout is to press `Ctrl+0` or choose `Break Layout` from the form's context menu.
### Vertical Layouts, `QVBoxLayout`
You can use a vertical layout ([QVBoxLayout](https://doc.qt.io/qt-5/qvboxlayout.html)) to arrange your widgets in one column one above the other. This can be very useful when you're creating groups of widgets and you need to ensure that they are vertically aligned.
Starting up with your original `layout-labels.ui` file, the first step will be to select the widgets that you need to include in the vertical layout. After that, you can click on the `Lay Out Vertically` button over the main toolbar, or you can use the context menu, or you can also press `Ctrl+2`. The following screencast will guide you through these steps —
If you take a closer look at the screencast, then you can see that the layout object is indicated by a thin red frame surrounding the labels on the form. This red frame isn't visible at preview or at runtime it's just a guide you can use when you're designing the form. Also notices that, the layout object appears in the Object Inspector and its properties (margins and constraints) are shown in the Property Editor.
### Grid Layouts, `QGridLayout`
Sometimes you need to lay out your widgets both horizontally and vertically within the same layout. To do this, you can use a grid layout manager ([QGridLayout](https://doc.qt.io/qt-5/qgridlayout.html)). Grid layout managers lay out your widgets in a square or rectangular grid, with all widgets aligning vertically and horizontally with their neighbours. This kind of layout can give you much more freedom to arrange your widgets on a form, while maintaining some degree of structure. This arrangement can be more suitable than nested arrangement of horizontal and vertical layouts, particularly when you care about the alignment of adjacent rows or columns.
You can build a grid layout with Qt Designer in the same way as for other layouts. The first step is to select the group of widgets that you want to lay out using a grid layout manager. Then, you can use the toolbar, the context menu, or you can press `Ctrl+5` to set up the layout. Watch the following screencast —
In this case, we use a _2 x 2_ grid layout to arrange the labels on your form. Notice that, to use this kind of layout, you should first place your widgets in rows and columns on the form, as shown in the screencast above. Qt Designer is quite clever and will try to keep your design as similar as possible to what you initially created by hand. It can even create difficult multi-column arrangements automatically or automatically fill empty cells.
### Form Layouts, `QFormLayout`
While a `QGridLayout` can be used to layout forms with inputs and labels in two columns, Qt also provides a layout designed specifically for this purpose — ([QFormLayout](https://doc.qt.io/qt-5/qformlayout.html)). This type of layout is ideal when you're creating a structured data-entry or database application. The left column will commonly hold labels that ask for some information. The right column holds the input widgets such as line edits ([QLineEdit](https://doc.qt.io/qt-5/qlineedit.html)), spin boxes ([QSpinBox](https://doc.qt.io/qt-5/qspinbox.html)), date edits ([QDateEdit](https://doc.qt.io/qt-5/qdateedit.html)), combo boxes ([QComboBox](https://doc.qt.io/qt-5/qcombobox.html)), and so on.
The advantage of using this layout over QGridLayout is that it is simpler to work with when you only need two columns. The following screencast shows it in action —
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
In this example, we first add four new labels. These labels will hold information about the data you need to be entered or edited in the second column. In this case, the second column holds your tests colored labels, but usually this column will be used to place input widget like line edits, spin boxes, combo boxes, and so on.
### Splitter Layouts
Splitters are container objects that arrange widgets horizontally or vertically in two resizeable panels. With this kind of layout, you can freely adjust the amount of space that each panel occupy on your form, while keeping the total space used constant. In Qt splitter layouts are managed using [QSplitter](https://doc.qt.io/qt-5/qsplitter.html).
Even though splitters are technically a container widget (not a layout), Qt Designer treats them as layouts that can be applied to existing widgets. To place a group of widgets into a splitter, you first select them as usually and then apply the splitter by using the appropriate toolbar button, keyboard shortcut, or context menu option in Qt Designer Take a look at the following screencast —
In this example, we first apply a horizontal splitter to your labels. Notice that, you'll need to launch the form preview if you want to see the splitter in action. You can launch the form preview by pressing `Ctrl+R`. Later on, we apply a vertical splitter to the labels. In each case, you can freely resize the widget using your mouse's pointer.
## Building Other Layouts With Qt Designer
There are a few more things you can do with layouts in Qt Designer. For example, suppose you need to add a new widget to an existing layout, or to use nested layouts to arrange your widgets in a complex GUI. In the following few sections, we'll cover how to accomplish some of these tasks.
### Inserting Objects into an Existing Layout
Objects can be inserted into an existing layout by dragging them from their current positions and dropping them at the required position in the layout. A blue cursor is displayed in the layout when an object is dragged over it to indicate where the object will be placed.
Take a look at the following screencast where we put three of our labels in a vertical layout and then realize the we left the blue label out of the game —
It's also possible to move or change the position of a given widget in a layout. To do this, just drag and drop the widget to its new position in the layout. Remember to follow the blue line to get this right.
### Nesting Layouts to Build Complex GUIs
You can also nest layout managers one inside another using Qt Designer. The inner layout then becomes a child of the enclosing layout. By doing this you can iteratively create very complex, yet well-structured user interfaces.
Layouts can be nested as deep as you need. For example, to create a dialog with a horizontal row of buttons at the bottom and a bunch of other widgets aligned vertically on the form, you can use a horizontal layout for the buttons and a vertical layout for the rest of the widgets, then wrap these layouts in a vertical layout.
Coming back to our colored labels example, the following screencast shows the process of arranging a nested layout in Qt Designer —
In this example, we first arrange widgets in pair using a horizontal layout. Then we nest both of these layouts in a third layout, but this time a vertical one. The layouts can be nested as deep as required.
When you select a child layout, its parent layout can be selected by pressing the `Shift` key while clicking on it. This allows you to quickly select a specific layout in a hierarchy, which otherwise will be difficult to do because of the small frame delimiting each layout manager.
## Setting a Top Level or Main Layout
The final step you need to perform when building a form is to combine all the layouts and widget into one **main layout** or **top level layout**. This layout is at the top of the hierarchy of all other layouts and widgets. It's vital that you have a layout because otherwise the widgets on your form won't resize when you resize the window.
To set the main layout just right click anywhere on your form that doesn't contain a widget or layout. Then, you can select `Lay Out Horizontally`, or `Lay Out Horizontally`, or you can also select `Lay Out in a Grid` like in the following screencast —
In this example, we use each of the three different layouts as our top level layout in turn. We first use a horizontal layout, then _break_ the layout and use a vertical layout. Finally we set a grid layout. Which top level layout you choose for your top-level layout will depend on your specific requirements for your app.
It's important that you note that top level layouts are not visible as a separate object in the Object Inspector. Its properties appear below the widget properties of the main form. Also, note that if your form doesn't have a layout, then its icon appears with a red circle on the Object Inspector. Another way to check if you've properly set a main layout is trying to resize the form, if a main layout is in place, then your widgets should resize accordingly.
As you start to build more complex applications, you'll discover that other container widgets also require you to set a top level layout, for example [QGroupBox](https://doc.qt.io/qt-5/qgroupbox.html), [QTabWidget](https://doc.qt.io/qt-5/qtabwidget.html), [QToolBox](https://doc.qt.io/qt-5/qtoolbox.html), and so on. To do this, you can run the same steps you've seen here, but this time you need to right click on the container widget.
## Laying Out a Dialog With Qt Designer
For a final and more complete example of how to use layouts with Qt Designer, we're now going to create a dialog to introduce some information in a database application. Suppose we're building a Human Resources Management software for our company Poyqote Inc.. We're now working in a form to introduce some data about our employees. The dialog should present users with a user-friendly GUI for introducing the following data:
  * Employee name
  * Employment date
  * Department
  * Position
  * Annual salary
  * Job description


What is the best way to lay out this form? There are many options, and it's largely a matter of taste and practise. But here we're using a `QFormLayout` to arrange the entry fields into two columns with labels on the left and input boxes on the right. The process of creating the layout is shown in the following screencast — 
The base dialog is created using Qt Designer's Dialog with Buttons Bottom template. Then, we add some labels and some input widget, including line edits, date edits, text edits, and combo boxes. Next we put all those widgets in a form layout and finally define a top level or main layout for the form.
The finished dialog .ui file [can be downloaded here](https://www.pythonguis.com/documents/26/dialog-layout-example.ui).
## Using the designed UI in Python
You can now save the completed UI to file and then import and display the dialog in PySide as before. For example, if you save the file as `dialog.ui` you can then launch the dialog from within Python as follows.
python ```
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
dialog = loader.load("dialog.ui", None)
dialog.show()
app.exec_()

```

However, dialogs are usually launched from another window -- and should block it waiting on a response. To launch the UI as a dialog, we instead call `.exec_()` on it. Since the dialog is defined using `QDialog` it inherits the usual Qt dialog behaviors, blocking the main window and returning the value of the pressed button.
python ```
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide2.QtUiTools import QUiLoader
loader = QUiLoader()
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    btn = QPushButton("Launch dialog")
    btn.pressed.connect(self.launch_dialog)
    self.setCentralWidget(btn)
  def launch_dialog(self):
    dialog = loader.load("dialog.ui", None)
    result = dialog.exec_()
    if result:
      print("Success!")
    else:
      print("Cancelled.")
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

```

## Conclusion
Qt Designer is a powerful tool when it comes to creating GUIs using Qt. One of its most straightforward and useful features is the ability to arrange your widgets in different types of layouts. Learning how to effectively create layouts with Qt Designer can sky rocket your productivity, particularly when creating complex GUIs. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
[![Leodanis Pozo Ramos](https://www.pythonguis.com/static/theme/images/authors/leodanis-pozo-ramos.jpg)](https://www.pythonguis.com/authors/leodanis-pozo-ramos/)
**Laying Out Your PySide2 GUIs With Qt Designer** was written by [Leodanis Pozo Ramos](https://www.pythonguis.com/authors/leodanis-pozo-ramos/) . 
**Laying Out Your PySide2 GUIs With Qt Designer** was published in [tutorials](https://www.pythonguis.com/tutorials/) on June 09, 2020 (updated March 03, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ qt-designer](https://www.pythonguis.com/topics/qt-designer/) [qt-creator](https://www.pythonguis.com/topics/qt-creator/) [gui](https://www.pythonguis.com/topics/gui/) [layouts](https://www.pythonguis.com/topics/layouts/) [qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [ pyside2-qt-designer](https://www.pythonguis.com/topics/pyside2-qt-designer/) [python](https://www.pythonguis.com/topics/python/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
