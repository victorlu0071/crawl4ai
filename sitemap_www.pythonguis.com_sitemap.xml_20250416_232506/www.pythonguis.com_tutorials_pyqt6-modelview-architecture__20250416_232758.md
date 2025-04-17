# Content from: https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/

[](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/#menu)
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
# The ModelView Architecture in PyQt6
Qt's MVC-like interface for displaying data in views
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 01 PyQt6 [ PyQt6 ModelViews and Databases ](https://www.pythonguis.com/pyqt6-tutorial/#pyqt6-model-views)
#### [ PyQt6 Tutorial ](https://www.pythonguis.com/pyqt6-tutorial/) — [PyQt6 ModelViews and Databases](https://www.pythonguis.com/pyqt6-tutorial/#pyqt6-model-views)
  * [The ModelView Architecture in PyQt6](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/)
  * [Displaying Tabular Data in PyQt6 ModelViews](https://www.pythonguis.com/tutorials/pyqt6-qtableview-modelviews-numpy-pandas/)


This tutorial is also available for [PySide6](https://www.pythonguis.com/tutorials/pyside6-modelview-architecture/) , [PySide2](https://www.pythonguis.com/tutorials/pyside-modelview-architecture/) and [PyQt5](https://www.pythonguis.com/tutorials/modelview-architecture/)
As you start to build more complex applications with PyQt6 you'll likely come across issues keeping widgets in sync with your data. Data stored in widgets (e.g. a simple `QListWidget`) is not readily available to manipulate from Python — changes require you to get an item, get the data, and then set it back. The default solution to this is to keep an external data representation in Python, and then either duplicate updates to the both the data and the widget, or simply rewrite the whole widget from the data. This can get ugly quickly, and results in a lot of boilerplate just for fiddling the data.
Thankfully Qt has a solution for this — ModelViews. ModelViews are a powerful alternative to the standard display widgets, which use a regular model interface to interact with data sources — from simple data structures to external databases. This isolates your data, allowing it to be kept in any structure you like, while the view takes care of presentation and updates.
This tutorial introduces the key aspects of Qt's ModelView architecture and uses it to build simple desktop Todo application in PyQt6.
Table of Contents
  * [Model View Controller](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/#model-view-controller)
  * [The Model View](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/#the-model-view)
  * [A simple Model View — a Todo List](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/#a-simple-model-view-a-todo-list)
    * [The UI](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/#the-ui)
    * [The Model](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/#the-model)
    * [Basic implementation](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/#basic-implementation)
    * [Hooking up the other actions](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/#hooking-up-the-other-actions)
    * [Using Qt.ItemDataRole.DecorationRole](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/#using-qtitemdataroledecorationrole)
  * [A persistent data store](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/#a-persistent-data-store)


## Model View Controller
**Model–View–Controller** (MVC) is an architectural pattern used for developing user interfaces which divides an application into three interconnected parts. This separates the internal representation of data from how information is presented to and accepted from the user.
The MVC design pattern decouples three major components —
  * **Model** holds the data structure which the app is working with.
  * **View** is any representation of information as shown to the user, whether graphical or tables. Multiple views of the same data model are allowed.
  * **Controller** accepts input from the user, transforming it into commands to for the model or view.


It Qt land the distinction between the View & Controller gets a little murky. Qt accepts input events from the user (via the OS) and delegates these to the widgets (Controller) to handle. However, widgets also handle presentation of the current state to the user, putting them squarely in the View. Rather than agonize over where to draw the line, in Qt-speak the View and Controller are instead merged together creating a Model/ViewController architecture — called "Model View" for simplicity sake.
Importantly, the distinction between the _data_ and _how it is presented_ is preserved. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
## The Model View
The Model acts as the interface between the data store and the ViewController. The Model holds the data (or a reference to it) and presents this data through a standardised API which Views then consume and present to the user. Multiple Views can share the same data, presenting it in completely different ways.
You can use any "data store" for your model, including for example a standard Python list or dictionary, or a database (via e.g. SQLAlchemy) — it's entirely up to you.
The two parts are essentially responsible for —
  1. The **model** stores the data, or a reference to it and returns individual or ranges of records, and associated metadata or _display_ instructions.
  2. The **view** requests data from the model and displays what is returned on the widget.


There is an in-depth discussion of the Qt architecture [in the documentation](http://doc.qt.io/qt-6/model-view-programming.html).
## A simple Model View — a Todo List
To demonstrate how to use the ModelViews in practise, we'll put together a very simple implementation of a desktop Todo List. This will consist of a `QListView` for the list of items, a `QLineEdit` to enter new items, and a set of buttons to add, delete, or mark items as done.
### The UI
The simple UI was laid out using Qt Creator and saved as `mainwindow.ui`. The `.ui` file and all the other parts can be downloaded below.
[Todo application Source Code](https://www.pythonguis.com/d/todo.zip)
![Designing a Simple Todo app in Qt Creator](https://www.pythonguis.com/static/tutorials/qt/modelview-architecture/qt-creator.png) _Designing a Simple Todo app in Qt Creator_
The running app is shown below.
![The running Todo GUI \(nothing works yet\)](https://www.pythonguis.com/static/tutorials/qt/modelview-architecture/mainwindow.png) _The running Todo GUI (nothing works yet)_
The widgets available in the interface were given the IDs shown in the table below.
objectName | Type | Description  
---|---|---  
`todoView` | `QListView` | The list of current todos  
`todoEdit` | `QLineEdit` | The text input for creating a new todo item  
`addButton` | `QPushButton` | Create the new todo, adding it to the todos list  
`deleteButton` | `QPushButton` | Delete the current selected todo, removing it from the todos list  
`completeButton` | `QPushButton` | Mark the current selected todo as done  
We'll use these identifiers to hook up the application logic later.
### The Model
We define our custom model by subclassing from a base implementation, allowing us to focus on the parts unique to our model. Qt provides a number of different model bases, including lists, trees and tables (ideal for spreadsheets).
For this example we are displaying the result to a `QListView`. The matching base model for this is `QAbstractListModel`. The outline definition for our model is shown below.
python ```
class TodoModel(QtCore.QAbstractListModel):
  def __init__(self, *args, todos=None, **kwargs):
    super().__init__(*args, **kwargs)
    self.todos = todos or []
  def data(self, index, role):
    if role == Qt.ItemDataRole.DisplayRole:
      # See below for the data structure.
      status, text = self.todos[index.row()]
      # Return the todo text only.
      return text
  def rowCount(self, index):
    return len(self.todos)

```

The`.todos` variable is our data store and the two methods `rowcount()` and `data()` are standard Model methods we must implement for a list model. We'll go through these in turn below.
#### .todos list
The data store for our model is `.todos`, a simple Python list in which we'll store a `tuple` of values in the format `[(bool, str), (bool, str), (bool, str)]` where `bool` is the _done_ state of a given entry, and `str` is the text of the todo.
We initialise `self.todo` to an empty list on startup, unless a list is passed in via the `todos` keyword argument.
`self.todos = todos or []` will set `self.todos` to the provided todos value if it is _truthy_ (i.e. anything other than an empty list, the boolean `False` or `None` the default value), otherwise it will be set to the empty list `[]`.
To create an instance of this model we can simply do —
python ```
model = TodoModel()  # create an empty todo list

```

Or to pass in an existing list —
python ```
todos = [(False, 'an item'), (False, 'another item')]
model = TodoModel(todos)

```

#### .rowcount()
The `.rowcount()` method is called by the view to get the number of rows in the current data. This is required for the view to know the maximum index it can request from the data store (`row count-1`). Since we're using a Python list as our data store, the return value for this is simply the `len()` of the list.
#### .data()
This is the core of your model, which handles requests for data from the view and returns the appropriate result. It receives two parameters `index` and `role.`
`index` is the position/coordinates of the data which the view is requesting, accessible by two methods `.row()` and `.column()` which give the position in each dimension.
For our `QListView` the column is always 0 and can be ignored, but you would need to use this for 2D data in a spreadsheet view.
`role` is a flag indicating the _type_ of data the view is requesting. This is because the `.data()` method actually has more responsibility than just the core data. It also handles requests for style information, tooltips, status bars, etc. — basically anything that could be informed by the data itself.
The naming of `Qt.ItemDataRole.DisplayRole` is a bit weird, but this indicates that the _view_ is asking us "please give me data for display". There are other _roles_ which the `data` can receive for styling requests or requesting data in "edit-ready" format.
Role | Value | Description  
---|---|---  
`Qt.ItemDataRole.DisplayRole` | `0` | The key data to be rendered in the form of text. ([QString](https://doc.qt.io/qt-5/qstring.html))  
`Qt.ItemDataRole.DecorationRole` | `1` | The data to be rendered as a decoration in the form of an icon. ([QColor](https://doc.qt.io/qt-5/qcolor.html), [QIcon](https://doc.qt.io/qt-5/qicon.html) or [QPixmap](https://doc.qt.io/qt-5/qpixmap.html))  
`Qt.ItemDataRole.EditRole` | `2` | The data in a form suitable for editing in an editor. ([QString](https://doc.qt.io/qt-5/qstring.html))  
`Qt.ItemDataRole.ToolTipRole` | `3` | The data displayed in the item's tooltip. ([QString](https://doc.qt.io/qt-5/qstring.html))  
`Qt.ItemDataRole.StatusTipRole` | `4` | The data displayed in the status bar. ([QString](https://doc.qt.io/qt-5/qstring.html))  
`Qt.ItemDataRole.WhatsThisRole` | `5` | The data displayed for the item in "What's This?" mode. ([QString](https://doc.qt.io/qt-5/qstring.html))  
`Qt.ItemDataRole.SizeHintRole` | `13` | The size hint for the item that will be supplied to views. ([QSize](https://doc.qt.io/qt-5/qsize.html))  
For a full list of available _roles_ that you can receive see [the Qt ItemDataRole documentation](https://doc.qt.io/qt-5/qt.html#ItemDataRole-enum). Our todo list will only be using `Qt.ItemDataRole.DisplayRole` and `Qt.ItemDataRole.DecorationRole`.
### Basic implementation
Below is the basic stub application needed to load the UI and display it. We'll add our model code and application logic to this base.
python ```
import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt

qt_creator_file = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)

class TodoModel(QtCore.QAbstractListModel):
  def __init__(self, *args, todos=None, **kwargs):
    super().__init__(*args, **kwargs)
    self.todos = todos or []
  def data(self, index, role):
    if role == Qt.ItemDataRole.DisplayRole:
      status, text = self.todos[index.row()]
      return text
  def rowCount(self, index):
    return len(self.todos)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self):
    QtWidgets.QMainWindow.__init__(self)
    Ui_MainWindow.__init__(self)
    self.setupUi(self)
    self.model = TodoModel()
    self.todoView.setModel(self.model)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

We define our `TodoModel` as before, and initialise the `MainWindow` object. In the `__init__` for the MainWindow we create an instance of our todo model and set this model on the `todo_view`. Save this file as `todo.py` and run it with — 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
bash ```
python3 todo.py

```

While there isn't much to see yet, the `QListView` and our model are actually working — if you add some default data you'll see it appear in the list.
python ```
self.model = TodoModel(todos=[(False, 'my first todo')])

```

![QListView showing hard-coded todo item](https://www.pythonguis.com/static/tutorials/qt/modelview-architecture/my-first-todo.png) _QListView showing hard-coded todo item_
You can keep adding items manually like this and they will show up in order in the `QListView`. Next we'll make it possible to add items from within the application.
First create a new method on the `MainWindow` named `add`. This is our callback which will take care of adding the current text from the input as a new todo. Connect this method to the `addButton.pressed` signal at the end of the `__init__` block.
python ```
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self):
    QtWidgets.QMainWindow.__init__(self)
    Ui_MainWindow.__init__(self)
    self.setupUi(self)
    self.model = TodoModel()
    self.todoView.setModel(self.model)
    # Connect the button.
    self.addButton.pressed.connect(self.add)
  def add(self):
    """
    Add an item to our todo list, getting the text from the QLineEdit .todoEdit
    and then clearing it.
    """
    text = self.todoEdit.text()
    if text: # Don't add empty strings.
      # Access the list via the model.
      self.model.todos.append((False, text))
      # Trigger refresh.
      self.model.layoutChanged.emit()
      # Empty the input
      self.todoEdit.setText("")

```

In the `add` block notice the line `self.model.layoutChanged.emit()`. Here we're emitting a model signal `.layoutChanged` to let the view know that the _shape_ of the data has been altered. This triggers a refresh of the entirety of the view. If you omit this line, the todo will still be added but the `QListView` won't update.
If just the data is altered, but the number of rows/columns are unaffected you can use the `.dataChanged()` signal instead. This also defines an altered region in the data using a top-left and bottom-right location to avoid redrawing the entire view.
### Hooking up the other actions
We can now connect the rest of the button's signals and add helper functions for performing the _delete_ and _complete_ operations. We add the button signals to the `__init__` block as before.
python ```
    self.addButton.pressed.connect(self.add)
    self.deleteButton.pressed.connect(self.delete)
    self.completeButton.pressed.connect(self.complete)

```

Then define a new `delete` method as follows —
python ```
  def delete(self):
    indexes = self.todoView.selectedIndexes()
    if indexes:
      # Indexes is a list of a single item in single-select mode.
      index = indexes[0]
      # Remove the item and refresh.
      del self.model.todos[index.row()]
      self.model.layoutChanged.emit()
      # Clear the selection (as it is no longer valid).
      self.todoView.clearSelection()

```

We use `self.todoView.selectedIndexes` to get the indexes (actually a list of a single item, as we're in single-selection mode) and then use the `.row()` as an index into our list of todos on our model. We delete the indexed item using Python's `del` operator, and then trigger a `layoutChanged` signal because the shape of the data has been modified.
Finally, we clear the active selection since the item it relates to may now out of bounds (if you had selected the last item).
You could try make this smarter, and select the last item in the list instead
The `complete` method looks like this —
python ```

  def complete(self):
    indexes = self.todoView.selectedIndexes()
    if indexes:
      index = indexes[0]
      row = index.row()
      status, text = self.model.todos[row]
      self.model.todos[row] = (True, text)
      # .dataChanged takes top-left and bottom right, which are equal
      # for a single selection.
      self.model.dataChanged.emit(index, index)
      # Clear the selection (as it is no longer valid).
      self.todoView.clearSelection()

```

This uses the same indexing as for delete, but this time we fetch the item from the model `.todos` list and then replace the status with `True`.
We have to do this fetch-and-replace, as our data is stored as Python tuples which cannot be modified.
The key difference here vs. standard Qt widgets is that we make changes directly to our data, and simply need to notify Qt that some change has occurred — updating the widget state is handled automatically.
### Using Qt.ItemDataRole.DecorationRole
If you run the application now you should find that adding and deleting both work, but while completing items is working, there is no indication of it in the view. We need to update our model to provide the view with an indicator to display when an item is complete. The updated model is shown below.
python ```
tick = QtGui.QImage('tick.png')

class TodoModel(QtCore.QAbstractListModel):
  def __init__(self, *args, todos=None, **kwargs):
    super().__init__(*args, **kwargs)
    self.todos = todos or []
  def data(self, index, role):
    if role == Qt.ItemDataRole.DisplayRole:
      _, text = self.todos[index.row()]
      return text
    if role == Qt.ItemDataRole.DecorationRole:
      status, _ = self.todos[index.row()]
      if status:
        return tick
  def rowCount(self, index):
    return len(self.todos)

```

We're using a tick icon `tick.png` to indicate completed items, which we load into a `QImage` object named `tick`. In the model we've implemented a handler for the `Qt.ItemDataRole.DecorationRole` which returns the tick icon for rows who's `status` is `True` (for complete).
The icon I'm using is taken from the Fugue set by [p.yusukekamiyamane](http://p.yusukekamiyamane.com/)
Instead of an icon you can also return a color, e.g. `QtGui.QColor('green')` which will be drawn as solid square.
Running the app you should now be able to mark items as complete.
![Todos Marked Complete](https://www.pythonguis.com/static/tutorials/qt/modelview-architecture/todos_complete.png) _Todos Marked Complete_
## A persistent data store
Our todo app works nicely, but it has one fatal flaw — it forgets your todos as soon as you close the application While thinking you have nothing to do when you do may help to contribute to short-term feelings of Zen, long term it's probably a bad idea.
The solution is to implement some sort of persistent data store. The simplest approach is a simple file store, where we load items from a JSON or Pickle file at startup, and write back on changes.
To do this we define two new methods on our `MainWindow` class — `load` and `save`. These load data from a JSON file name `data.json` (if it exists, ignoring the error if it doesn't) to `self.model.todos` and write the current `self.model.todos` out to the same file, respectively.
python ```
  def load(self):
    try:
      with open('data.json', 'r') as f:
        self.model.todos = json.load(f)
    except Exception:
      pass
  def save(self):
    with open('data.json', 'w') as f:
      json.dump(self.model.todos, f)

```

To persist the changes to the data we need to add the `.save()` handler to the end of any method that modifies the data, and the `.load()` handler to the `__init__` block after the model has been created.
The final code looks like this —
python ```
import sys
import json
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt

qt_creator_file = "mainwindow.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)
tick = QtGui.QImage('tick.png')

class TodoModel(QtCore.QAbstractListModel):
  def __init__(self, *args, todos=None, **kwargs):
    super().__init__(*args, **kwargs)
    self.todos = todos or []
  def data(self, index, role):
    if role == Qt.ItemDataRole.DisplayRole:
      _, text = self.todos[index.row()]
      return text
    if role == Qt.ItemDataRole.DecorationRole:
      status, _ = self.todos[index.row()]
      if status:
        return tick
  def rowCount(self, index):
    return len(self.todos)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.model = TodoModel()
    self.load()
    self.todoView.setModel(self.model)
    self.addButton.pressed.connect(self.add)
    self.deleteButton.pressed.connect(self.delete)
    self.completeButton.pressed.connect(self.complete)
  def add(self):
    """
    Add an item to our todo list, getting the text from the QLineEdit .todoEdit
    and then clearing it.
    """
    text = self.todoEdit.text()
    if text: # Don't add empty strings.
      # Access the list via the model.
      self.model.todos.append((False, text))
      # Trigger refresh.
      self.model.layoutChanged.emit()
      # Empty the input
      self.todoEdit.setText("")
      self.save()
  def delete(self):
    indexes = self.todoView.selectedIndexes()
    if indexes:
      # Indexes is a list of a single item in single-select mode.
      index = indexes[0]
      # Remove the item and refresh.
      del self.model.todos[index.row()]
      self.model.layoutChanged.emit()
      # Clear the selection (as it is no longer valid).
      self.todoView.clearSelection()
      self.save()
  def complete(self):
    indexes = self.todoView.selectedIndexes()
    if indexes:
      index = indexes[0]
      row = index.row()
      status, text = self.model.todos[row]
      self.model.todos[row] = (True, text)
      # .dataChanged takes top-left and bottom right, which are equal
      # for a single selection.
      self.model.dataChanged.emit(index, index)
      # Clear the selection (as it is no longer valid).
      self.todoView.clearSelection()
      self.save()
  def load(self):
    try:
      with open('data.db', 'r') as f:
        self.model.todos = json.load(f)
    except Exception:
      pass
  def save(self):
    with open('data.db', 'w') as f:
      json.dump(self.model.todos, f)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

If the data in your application has the potential to get large or more complex, you may prefer to use an actual database to store it. In this case the model will wrap the interface to the database and query it directly for data to display. I'll cover how to do this in an upcoming tutorial.
For another interesting example of a `QListView` see [this example media player application](https://www.pythonguis.com/examples/failamp-multimedia-player/). It uses the Qt built-in `QMediaPlaylist` as the datastore, with the contents displayed to a `QListView`.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
Continue with [ PyQt6 Tutorial ](https://www.pythonguis.com/tutorials/pyqt6-qtableview-modelviews-numpy-pandas/ "Continue to next part")
Return to [Create Desktop GUI Applications with PyQt6 ](https://www.pythonguis.com/pyqt6-tutorial/)
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**The ModelView Architecture in PyQt6** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/Python books) on the subject. 
**The ModelView Architecture in PyQt6** was published in [tutorials](https://www.pythonguis.com/tutorials/) on June 01, 2021 (updated April 01, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[mvc](https://www.pythonguis.com/topics/mvc/) [model-view](https://www.pythonguis.com/topics/model-view/) [qt](https://www.pythonguis.com/topics/qt/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ data-science](https://www.pythonguis.com/topics/data-science/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyqt6-data-science](https://www.pythonguis.com/topics/pyqt6-data-science/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
