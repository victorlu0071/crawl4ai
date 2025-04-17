# Content from: https://www.pythonguis.com/examples/simple-sales-tax-calculator/

[](https://www.pythonguis.com/examples/simple-sales-tax-calculator/#menu)
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
# Simple Sales Tax Calculator
Using Qt creator to create a simple GUI
by [Shantnu Tiwari](https://www.pythonguis.com/authors/shantnu-tiwari/) Last updated Sep 11 PyQt5 [ Example applications ](https://www.pythonguis.com/examples/)
[ Tax Calculator Demo Application ](https://www.pythonguis.com/d/tax.zip)
This is a simple step-by-step walkthrough creating a GUI app using Qt Creator and PyQt5. Since GUIs are entirely visual it's hard to convey what to do through text, so this tutorial is full of step-by-step screenshots.
The app a simple sales tax calculator, which takes an input value, a tax rate and outputs the resulting total price with tax. It's not very exciting, but it _is_ easy to understand!
## Designing In Qt Creator
You will need a copy of Qt Creator to follow this tutorial. Get this by downloading Qt from here: <https://www.qt.io/download> — you can opt to install only Qt Creator during installation.
Start Qt Creator. To start designing create a window we need a blank design. From the File menu select "New file or project. In the popup window that appears choose:
  1. Qt Designer Form
  2. Main Window (other Widget types are available)
  3. Select a location to save the resulting `.ui` file
  4. Revision control (can skip this)
  5. Click Done to create the design.


The steps are shown visually below.
![Qt Creator — Initial View](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.00.40.png) _Qt Creator — Initial View_
![Qt Creator — Start new design](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.00.49.png) _Qt Creator — Start new design_
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
![Qt Creator —&nbsp;Create a new Qt Designer Form](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.01.01.png) _Qt Creator — Create a new Qt Designer Form_
![Qt Creator — Select MainWindow for widget type](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.01.09.png) _Qt Creator — Select MainWindow for widget type_
![Qt Creator —&nbsp;Select Save location for the .ui file](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.02.46.png) _Qt Creator — Select Save location for the .ui file_
![Qt Creator —&nbsp;Project management / revision control](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.03.10.png) _Qt Creator — Project management / revision control_
Phew. After all that you should be presented with a blank empty canvas on which to construct your new application.
![Qt Designer —&nbsp;Blank Canvas](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.03.42.png) _Qt Designer — Blank Canvas_
Now we can start designing our UI, using the drag-drop interface. First select a _Line Edit_ (QLineEdit) box from the left.
![Qt Designer —&nbsp;with Line Edit highlighted](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.03.42_RHkpOiO.png) _Qt Designer — with Line Edit highlighted_
Drag _Line Edit_ to the main window, to get a box like that shown below.
![Qt Designer —&nbsp;Line Edit on MainWindow](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.05.09.png) _Qt Designer — Line Edit on MainWindow_
The red highlight in the box below shows `objectName` which is the name of the object is. The name entered here is the name that will be used to refer to this object from our Python code, so call it something sensible.
I'm calling it price_box, as we will enter the price into this box.
![Qt Designer —&nbsp;Editing the objectName](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.05.35.png) _Qt Designer — Editing the objectName_
The next thing we will do is attach a label to the box, to make it clear to the _user_ what this box is for.
Find the _Label_ in the list of widgets on the left, and drag it onto the main window. It gets the default text of "TextLabel". Double click the widget and type to change it to "Price".
Don't worry about positioning too much, we'll sort the layout right at the end. Just put the widgets in roughly the right place.
![Qt Creator —&nbsp;Adding a Label](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.06.08.png) _Qt Creator — Adding a Label_
You can also make the text large and bold, as seen here:
![Qt Creator — QLabel font properties](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.06.36.png) _Qt Creator — QLabel font properties_
For the tax box, we are going to use something different — a _Spin Box_ (`QSpinBox`). This is a numeric input which limits the values you can enter. We don’t need a _Spin Box_ , it’s just good to see how you can use different widgets that Qt Creator provides.
Drag a _Spin Box_ to the window. The first thing we do is change the `objectName` to something sensible, `tax_rate` in our case. Remember, this is how this object will be called from Python.
![Qt Creator —&nbsp;The Spin Box](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.07.00.png) _Qt Creator — The Spin Box_
We can choose a default value for our _Spin Box_. I'm choosing 20:
![Qt Designer —&nbsp;Setting default value on a QSpinBox](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.07.29.png) _Qt Designer — Setting default value on a QSpinBox_
One neat feature of `QSpinBox` is that you can also set the minimum and maximum limits. We're keeping them to what they are for our app, but feel free to tweak them for yours.
![Qt Designer —&nbsp;QSpinBox properties](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-31_at_00.07.04.png) _Qt Designer — QSpinBox properties_
Add another label called Tax Rate, editing it the same as before and drag it into place next to the _Spin Box_.
![Qt Designer — Adding another label](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.09.49.png) _Qt Designer — Adding another label_
Next look for the widget called _Push Button_ in the widget panel and drag it to the window.
The button just says PushButton, which isn't very helpful. Change the `objectName` to `calc_tax_button` and then double click to edit the _label_ text on the button to "Calculate Tax".
![Qt Designer —&nbsp;Adding a QButton](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.10.19.png) _Qt Designer — Adding a QButton_
Drag another _Label_ on to the window. This label will be where we write out the result of our calculation. So double-click and edit to delete the default text. Change it's `objectName` to `results_output`.
![Qt Designer —&nbsp;QLabel as output](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.12.03.png) _Qt Designer — QLabel as output_
Finally, if you want to you can add a header. This is a simple label box with the font increased:
![Screenshot 2019-05-30 at 23.12.39.png](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.12.39.png) _Screenshot 2019-05-30 at 23.12.39.png_
## Adjusting the layout
So we now have the bones of our UI in place, but it's not looking particularly pretty. Firstly, we have a lot of empty space because our window is way too big.
To shrink the window, first select all the widgets and move them out of the way (top left), and then drag the window down to size using the blue handles in the corner.
![Qt Designer —&nbsp;Resized QMainWIndow](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.14.14.png) _Qt Designer — Resized QMainWIndow_
That certainly helped a bit, but the alignments are still a bit wonky.
Helpfully, Qt provides a system of _layouts_ which can be used to automatically position elements within a window. In our case we have a classic _form_ layout, where we have a vertical stack of widgets and labels. Qt has a specific _Form Layout_ for exactly this purpose. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
To apply it, right-click on your _Main Window_ and select "Lay out" at the bottom (yes, there is a space between Lay and out, I don't know why) and then choose "Lay Out in a Form Layout" (snappy title).
![Qt Designer —&nbsp;Layout with a Form Layout](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.14.30.png) _Qt Designer — Layout with a Form Layout_
You should see the widgets instantly snap into position. If the positions are not _correct_ just drag them around — they will continue to snap to a regular grid, with both sides aligned.
![Qt Designer —&nbsp;Form Layout applied](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.14.44.png) _Qt Designer — Form Layout applied_
The big label (if you've added it) doesn't have a "pair" so can't align. If you drag it around, it'll throw the other elements off. To fix this, just drag-resize it out of the form layout, and it will be ignored.
The last 2 final tweaks are —
  1. Set the input box to right-aligned, which is more natural for numbers.
  2. Update the name of the _Main Window_ `windowTitle` property (choose a good name).


![Qt Designer —&nbsp;Setting alignment on an input](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.22.15.png) _Qt Designer — Setting alignment on an input_
![Qt Designer —&nbsp;Setting the windowTitle](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-30_at_23.33.53.png) _Qt Designer — Setting the windowTitle_
## Done!
That's the design complete. Save your `.ui` file by File -> Save (it will default to the name & location you gave during setup.
In the next part we'll write the code to bring our UI to life.
## Writing the code
The UI file we've created is just an XML definition, containing the positions attributes and names of the widgets. Open it in a text editor, if you want, and you will find something like this:
xml ```
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
 <property name="geometry">
  <rect>
  <x>0</x>
  <y>0</y>
  <width>328</width>
  <height>273</height>
  </rect>
 </property>
 <property name="windowTitle">
  <string>Sales Tax Calulator</string>
 </property>
 <widget class="QWidget" name="centralwidget">
  <layout class="QFormLayout" name="formLayout">
  <item row="0" column="0" colspan="2">
   <widget class="QLabel" name="label_3">
   <property name="font">
    <font>
    <pointsize>28</pointsize>
    <weight>75</weight>
    <bold>true</bold>
...

```

Each of the widgets we added is an object, with a set of common and widget-specific methods e.g. `text()` (to read the value in a `LineEdit`).
This example uses the `loadUI` method to load the UI file, for other options take a look at [First steps with Qt Creator](https://www.pythonguis.com/tutorials/first-steps-qt-creator/)
## Loading your UI
To use your UI file in your app you need to load it into your Python code. PyQt provides a `uic.loadUIType()` method to load a file and create a `QWidget` (or `QMainWindow`) object.
The following skeleton file can be used to load any UI file generated from Qt Creator and display it.
  * PyQt5
  * PySide2


python ```
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
qtcreator_file = "your .ui file" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self):
    QtWidgets.QMainWindow.__init__(self)
    Ui_MainWindow.__init__(self)
    self.setupUi(self)
if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  window = MyWindow()
  window.show()
  sys.exit(app.exec_())

```

python ```
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
qtcreator_file = "your .ui file" # Enter file here.
loader = QUiLoader()
file = QtCore.QFile(qtcreator_file)
file.open(QtCore.QFile.ReadOnly)
file.close()
if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  window = loader.load(file, None)
  window.show()
  sys.exit(app.exec_())

```

Let's take a quick look at the code. At the bottom of the file we define our entrypoint which first creates a `QApplication` instance, passing in `sys.argv` allows Qt to be configured from the command line while running your app (we won't be doing that here).
Next we create an instance of `MyWindow`, show it using `window.show()` and then execute the application event loop, with `app.exec_()`.
python ```
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  window = MyWindow()
  window.show()
  sys.exit(app.exec_())
````
To load your own UI file just change the filename on this line
```python
qtcreator_file = "your .ui file" # Enter file here.

```

Save the file as `tax.py` and then run it from the command line.
bash ```
python3 tax.py

```

You should see your UI appear, looking something not unlike the following —
![Simple Tax Calculator —&nbsp;Skeleton UI](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-31_at_11.15.02.png) _Simple Tax Calculator — Skeleton UI_
## Hooking up the logic
You'll probably notice that while you can enter numbers and click the button when you do this nothing happens. This is because we still need to implement the actual application logic in our Python code.
The key widget in our GUI was the button. Once you press the button, something happens. What? We need to tell our code what to do when the user presses the Calculate Tax button. In the **init** function, add this line:
python ```
self.calc_tax_button.clicked.connect(self.calculate_tax)

```

Remember that in Qt Creator we called our button `calc_tax_button` — this was the name of the object, not the text that was displayed on it. The button is attached by `loadUI` to our `MyMainWindow` instance (here available as `self`) using the name we defined for it.
_All_ the objects you create in Qt Creator are available in this same way (even the labels which you didn't rename).
`.clicked` is an internal _signal_ that is triggered when someone clicks on a `QButton`. We connect this _signal_ to a handler using `.connect(self.calculate_tax)`. This means that every time the button is pressed and the `.clicked` signal fires, the connected method `self.calculate_tax` is called.
You can connect multiple target functions or methods (called _slots_ in Qt terminology) to a signal, and they will _all_ be called when the signal fires.
We haven’t written the target method `self.calculate_tax` yet, so let's do it now. In the `MyWindow` class, add the method with the following code:
python ```
def calculate_tax(self):
  price = Decimal(self.price_box.text())
  tax = Decimal(self.tax_rate.value())
  total_price = price + ((tax / 100) * price)
  total_price_string = "The total price with tax is: {:.2f}".format(total_price)
  self.results_output.setText(total_price_string)

```

We're using the Python builtin type [Decimal](https://docs.python.org/3/library/decimal.html) for our calculations, as it prevents rounding errors for fixed-point currency calculations. It otherwise works exactly like `float`, which you should already be familiar with. To use `Decimal` we need to import it at the top of the file, by adding the following —
python ```
from decimal import Decimal

```

Save the file, and run it again from the command line. You should now have a fully functioning application!
bash ```
python3 tax.py

```

![Simple Tax Calculator — Running, with logic](https://www.pythonguis.com/static/examples/simple-sales-tax-calculator/Screenshot_2019-05-31_at_11.32.43.png) _Simple Tax Calculator — Running, with logic_
Let's step through the code line by line to see what it is doing.
We have to do two things: Read the price box, read the tax box, and calculate the final price. Remember, we will call the objects by the names we gave them in Qt Creator (which is why it's a good idea to rename them, as names like `box1` become confusing fast!)
python ```
price = Decimal(self.price_box.text())

```

First we read our `price_box` by calling `.text()`. This method returns the current value of the `QLineEdit`.
You don't have to remember these all these names yourself, just Google "Qt5 QLineEdit" to get to [the documentation page](https://doc.qt.io/qt-5/qlineedit.html), which lists [all the available methods](https://doc.qt.io/qt-5/qlineedit.html#public-functions).
The read value is a string, so we convert it to an `Decimal` and store it in a variable called `price`.
Next, we read the tax rate from the [QSpinBox](https://doc.qt.io/qt-5/qspinbox.html) widget named `tax_rate` using the builtin method `.value()`. This returns a `float` which we convert to a `Decimal` for accuracy.
python ```
tax = Decimal(self.tax_rate.value())

```

Now that we have both these values, we can calculate the final price using very complex maths:
python ```
total_price = price + ((tax / 100) * price)
total_price_string = "The total price with tax is: {:.2f}".format(total_price)
self.results_output.setText(total_price_string)

```

We create a string with our final price, rounding the result down to 2 decimal places. Finally we output it to our `QLabel` widget `results_output`, replacing the text there (initially empty).
The complete code is shown below.
python ```
import sys
from decimal import Decimal
from PyQt5 import QtCore, QtGui, QtWidgets, uic

qtCreatorFile = "mainwindow.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self):
    QtWidgets.QMainWindow.__init__(self)
    Ui_MainWindow.__init__(self)
    self.setupUi(self)
    self.calc_tax_button.clicked.connect(self.calculate_tax)
  def calculate_tax(self):
    price = Decimal(self.price_box.text())
    tax = Decimal(self.tax_rate.value())
    total_price = price + ((tax / 100) * price)
    total_price_string = "The total price with tax is: {:.2f}".format(total_price)
    self.results_output.setText(total_price_string)

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  window = MyWindow()
  window.show()
  sys.exit(app.exec_())

```

So, we've successfully made a simple PyQt5 application using Qt Creator and implemented the logic with Python! If you want to learn more about PyQt check out the [Getting started with PyQt5](https://www.pythonguis.com/courses/start/) course. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Shantnu Tiwari](https://www.pythonguis.com/static/theme/images/authors/shantnu-tiwari.jpg)](https://www.pythonguis.com/authors/shantnu-tiwari/)
**Simple Sales Tax Calculator** was written by [Shantnu Tiwari](https://www.pythonguis.com/authors/shantnu-tiwari/) . 
Shantnu trained as an Electronics Engineer, and spent several years working with low level code, including DSPs, embedded systems and embedded Linux. Soon, he grew disillusioned by fixing dangling pointers, memory leaks, race conditions, bugs which only appeared once every two weeks. He's been programming in Python ever since. 
**Simple Sales Tax Calculator** was published in [examples](https://www.pythonguis.com/examples/) on July 06, 2019 (updated September 11, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [qt5](https://www.pythonguis.com/topics/qt5/) [app](https://www.pythonguis.com/topics/app/) [tax-calculator](https://www.pythonguis.com/topics/tax-calculator/) [simple-app](https://www.pythonguis.com/topics/simple-app/) [tax](https://www.pythonguis.com/topics/tax/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/)
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
