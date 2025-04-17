# Content from: https://www.pythonguis.com/tutorials/pyside-qscrollarea/

[](https://www.pythonguis.com/tutorials/pyside-qscrollarea/#menu)
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
# Add Scrollable Regions With QScrollArea in PySide6
Run out of space in your GUI? Add a scrollable region to your application
by [John Lim](https://www.pythonguis.com/authors/john-lim/) Last updated Mar 15 PySide6 [ Tutorials ](https://www.pythonguis.com/tutorials/)
This tutorial is also available for [PyQt6](https://www.pythonguis.com/tutorials/pyqt6-qscrollarea/) , [PySide2](https://www.pythonguis.com/tutorials/pyside2-qscrollarea/) and [PyQt5](https://www.pythonguis.com/tutorials/qscrollarea/)
When you start building apps that display long documents, large amounts of data or large numbers of widgets, it can be difficult to arrange things within a fixed-size window. Resizing the window beyond the size of the screen isn't an option, and shrinking widgets to fit can make the information unreadable.
To illustrate the problem below is a window in which we've created a large number of `QLabel` widgets. These widgets have the size _Vertical Policy_ set to _Preferred_ which automatically resizes the widgets down to fit the available space. The results are unreadable.
![Problem of Too Many Widgets.png](https://www.pythonguis.com/static/tutorials/qt/qscrollarea/Problem_of_Too_Many_Widgets.png) _Problem of Too Many Widgets.png_
Settings the _Vertical Policy_ to _Fixed_ keeps the widgets at their natural size, making them readable again.
![Problem of Too Many Widgets With Fixed Heights](https://www.pythonguis.com/static/tutorials/qt/qscrollarea/Problem_of_Too_Many_Widgets_With_Fixed_Heights.png) _Problem of Too Many Widgets With Fixed Heights_
However, while we can still add as many labels as we like, eventually they start to fall off the bottom of the layout.
To solve this problem GUI applications can make use of _scrolling_ regions to allow the user to move around _within_ the bounds of the application window while keeping widgets at their usual size. By doing this an almost _unlimited_ amount of data or widgets can be shown, navigated and viewed within a window — although care should be taken to make sure the result is still usable! 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
In this tutorial, we'll cover adding a scrolling region to your PyQt application using `QScrollArea`.
Table of Contents
  * [Adding a QScrollArea in Qt Designer](https://www.pythonguis.com/tutorials/pyside-qscrollarea/#adding-a-qscrollarea-in-qt-designer)
    * [Inserting Widgets](https://www.pythonguis.com/tutorials/pyside-qscrollarea/#inserting-widgets)
  * [Adding a QScrollArea from code](https://www.pythonguis.com/tutorials/pyside-qscrollarea/#adding-a-qscrollarea-from-code)
  * [Conclusion.](https://www.pythonguis.com/tutorials/pyside-qscrollarea/#conclusion)


## Adding a QScrollArea in Qt Designer
First we'll look at how to add a `QScrollArea` from _Qt Designer_.
![Qt Creator — Select MainWindow for widget type](https://www.pythonguis.com/static/tutorials/qt/qscrollarea/Screenshot_2019-05-30_at_23.01.09.png) _Qt Creator — Select MainWindow for widget type_
So we will choose the scroll area widget and add it to our layout as below.
First, create an empty `MainWindow` in _Qt Designer_ and save it as `mainwindow.ui`
![Add Scroll Area](https://www.pythonguis.com/static/tutorials/qt/qscrollarea/Add_Scroll_Area.png) _Add Scroll Area_
Next choose to lay out the `QScrollArea` vertically or horizontally, so that it scales with the window.
![Lay Out The Scroll Area Vertically Or Horizontally](https://www.pythonguis.com/static/tutorials/qt/qscrollarea/Lay_Out_The_Scroll_Area_If_You_Wish.png) _Lay Out The Scroll Area Vertically Or Horizontally_
Voila, we now have a completed scroll area that we can populate with anything we need.
![The Scroll Area Is Created](https://www.pythonguis.com/static/tutorials/qt/qscrollarea/The_Scroll_Area_Is_Created.png) _The Scroll Area Is Created_
### Inserting Widgets
We will now add labels to that scroll area. Lets take two labels and place it inside the `QScrollArea`. We will then proceed to right click inside the scroll area and select _Lay Out Vertically_ so our labels will be stacked vertically.
![Add Labels to The Scroll Area And Set the Layout](https://www.pythonguis.com/static/tutorials/qt/qscrollarea/Add_Labels_to_The_Scroll_Area_And_Set_the_Layout.png) _Add Labels to The Scroll Area And Set the Layout_
We've set the background to _blue_ so the illustration of this this works is clear. We can now add more labels to the `QScrollArea` and see what happens. By default, the _Vertical Policy_ of the label is set to _Preferred_ which means that the label size is adjusted according to the constraints of widgets above and below.
Next, we'll add a bunch of widgets.
![Adding More Labels to QScrollArea](https://www.pythonguis.com/static/tutorials/qt/qscrollarea/Adding_Labels_to_QScrollArea.png) _Adding More Labels to QScrollArea_
Any widget can be added into a `QScrollArea` although some make more sense than others. For example, it's a great way to show multiple widgets containing data in a expansive dashboard, but less appropriate for control widgets — scrolling around to control an application can get frustrating.
Note that the scroll functionality has not been triggered, and no scrollbar has appeared on the right hand side. Instead the labels are still progressively getting smaller in height to accommodate the widgets.
However, if we set _Vertical Policy_ to _Fixed_ and set the _minimumSize_ of _height_ to 100px the labels will no longer be able to shrink vertically into the available space. As the layout overflows this will now trigger the `QScrollArea` to display a scrollbar.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
![Setting Fixed Heights for Labels](https://www.pythonguis.com/static/tutorials/qt/qscrollarea/Setting_Fixed_Heights_for_Labels.png) _Setting Fixed Heights for Labels_
With that, our scrollbar appears on the right hand side. What has happened is that the scroll area only appears when necessary. Without a fixed height constraint on the widget, Qt assumes the most logical way to handle the many widgets is to resize them. But by imposing size constraints on our widgets, the scroll bar appears to allow all widgets to keep their fixed sizes.
Another important thing to note is the properties of the scroll area. Instead of adjusting fixed heights, we can keep it in `Preferred` , we can set the properties of the `verticalScrollBar` to `ScrollBarAlwaysOn` which will enable the scroll bar to appear sooner as below
![ScrollArea Properties](https://www.pythonguis.com/static/tutorials/qt/qscrollarea/ScrollArea_Properties_oiTZQy8.png) _ScrollArea Properties_
Saving and running the code at the start of this tutorial gives us this scroll area app which is what we wanted.
![App With Scroll Bar](https://www.pythonguis.com/static/tutorials/qt/qscrollarea/App_With_Scroll_Bar.png) _App With Scroll Bar_
## Adding a QScrollArea from code
As with all widgets you can also add a `QScrollArea` directly from code. Below we repeat the above example, with a flexible scroll area for a given number of widgets, using code.
python ```
from PySide6.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
               QHBoxLayout, QVBoxLayout, QMainWindow)
from PySide6.QtCore import Qt, QSize
from PySide6 import QtWidgets
import sys

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.scroll = QScrollArea()       # Scroll Area which contains the widgets, set as the centralWidget
    self.widget = QWidget()         # Widget that contains the collection of Vertical Box
    self.vbox = QVBoxLayout()        # The Vertical Box that contains the Horizontal Boxes of labels and buttons
    for i in range(1,50):
      object = QLabel("TextLabel")
      self.vbox.addWidget(object)
    self.widget.setLayout(self.vbox)
    #Scroll Area Properties
    self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
    self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.scroll.setWidgetResizable(True)
    self.scroll.setWidget(self.widget)
    self.setCentralWidget(self.scroll)
    self.setGeometry(600, 100, 1000, 900)
    self.setWindowTitle('Scroll Area Demonstration')
    self.show()

app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
sys.exit(app.exec())

```

If you run the above code you should see the output below, with a custom widget repeated multiple times down the window, and navigable using the scrollbar on the right.
![Scroll Area App](https://www.pythonguis.com/static/tutorials/qt/qscrollarea/Screenshot_from_2019-12-03_11-54-46.png) _Scroll Area App_
Next, we'll step through the code to explain how this view is constructed.
First we create our layout hierarchy. At the top level we have our `QMainWindow` which we can set the `QScrollArea` onto using `.setCentralWidget`. This places the `QScrollArea` in the window, taking up the entire area.
To add content to the `QScrollArea` we need to add a widget using `.setWidget`, in this case we are adding a custom `QWidget` onto which we have applied a `QVBoxLayout` containing multiple sub-widgets.
python ```
  self.scroll = QScrollArea()       # Scroll Area which contains the widgets, set as the centralWidget
  self.widget = QWidget()         # Widget that contains the collection of Vertical Box
  self.vbox = QVBoxLayout()        # The Vertical Box that contains the Horizontal Boxes of labels and buttons
  for i in range(1,50):
    object = QLabel("TextLabel")
    self.vbox.addWidget(object)

```

This gives us the following hierarchy in the window:
Finally we set up properties on the `QScrollArea`, setting the vertical scrollbar _Always On_ and the horizontal _Always Off_. We allow the widget to be resized, and then add the central placeholder widget to complete the layout.
python ```
#Scroll Area Properties
self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
self.scroll.setWidgetResizable(True)
self.scroll.setWidget(self.widget)

```

Finally, we will add the `QScrollArea` as the central widget for our `QMainWindow` and set up the window dimensions, title and show the window.
python ```
self.setCentralWidget(self.scroll)
self.setGeometry(600, 100, 1000, 900)
self.setWindowTitle('Scroll Area Demonstration')
self.show()

```

## Conclusion.
In this tutorial we've learned how to add a scrollbar with an unlimited number of widgets, programmatically or using Qt Designer. Adding a `QScrollArea` is a good way to include multiple widgets especially on apps that are data intensive and require objects to be displayed as lists.
Have a go at making your own apps with `QScrollArea` and share with us what you have made!
For more information about using QScrollArea check out [the PyQt5 documentation](https://doc.qt.io/qt-5/qscrollarea.html). 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
[![John Lim Ji Xiong](https://www.pythonguis.com/static/theme/images/authors/john-lim.jpg)](https://www.pythonguis.com/authors/john-lim/)
**Add Scrollable Regions With QScrollArea in PySide6** was written by [John Lim](https://www.pythonguis.com/authors/john-lim/) . 
John is a developer from Kuala Lumpur, Malaysia who works as a Senior R&D Engineer. 
**Add Scrollable Regions With QScrollArea in PySide6** was published in [tutorials](https://www.pythonguis.com/tutorials/) on December 03, 2021 (updated March 15, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
