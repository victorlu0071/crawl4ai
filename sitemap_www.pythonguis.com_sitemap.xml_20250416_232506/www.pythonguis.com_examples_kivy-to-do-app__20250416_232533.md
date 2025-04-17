# Content from: https://www.pythonguis.com/examples/kivy-to-do-app/

[](https://www.pythonguis.com/examples/kivy-to-do-app/#menu)
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
# Build a To-do App With Python and Kivy
Magange Your Todo Items With Ease
by [Francis Ali](https://www.pythonguis.com/authors/francis-ali/) Last updated Apr 03 [ Example applications ](https://www.pythonguis.com/examples/)
A To-do app is a program for managing tasks or activities that you intend to do at some point. It is a classic programming project for beginners, especially for those learning to create graphical user interfaces or GUIs for the desktop.
In this tutorial, we will learn how to create a minimal To-do app with Kivy. The app will allow you to create new tasks, save them to an [SQLite](https://sqlite.org/) database, mark them as done, and remove them when finished.
Table of Contents
  * [Setting Up the Working Environment](https://www.pythonguis.com/examples/kivy-to-do-app/#setting-up-the-working-environment)
  * [Creating the To-do App's Project Layout](https://www.pythonguis.com/examples/kivy-to-do-app/#creating-the-to-do-apps-project-layout)
  * [Developing the To-do App's Interface](https://www.pythonguis.com/examples/kivy-to-do-app/#developing-the-to-do-apps-interface)
  * [Managing the To-do Database](https://www.pythonguis.com/examples/kivy-to-do-app/#managing-the-to-do-database)
  * [Completing the To-do App's GUI](https://www.pythonguis.com/examples/kivy-to-do-app/#completing-the-to-do-apps-gui)
  * [Conclusion](https://www.pythonguis.com/examples/kivy-to-do-app/#conclusion)


## Setting Up the Working Environment
In this tutorial, we'll use the Kivy library to build the To-do app's GUI. So, we assume that you have a basic understanding of Kivy's widgets and apps.
To learn the basics about Kivy, check out the [Getting Started With Kivy for GUI Development](https://www.pythonguis.com/tutorials/getting-started-kivy/) tutorial.
For the database functionalities, we will use the [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3) package from the Python standard library. To use `sqlite3` yourself you will need to have some basic SQL knowledge However, if you are not familiar with SQL, don't fret, we won't be going deep into that topic & have working examples you can copy.
With that in mind, let's create a [virtual environment](https://www.pythonguis.com/tutorials/python-virtual-environments/) and install Kivy in it. To do this, you can run the following commands:
  * macOS
  * Windows
  * Linux


sh ```
$ mkdir notes/
$ cd notes
$ python -m venv venv
$ source venv/bin/activate
(venv)$ pip install kivy

```

cmd ```
> mkdir notes/
> cd notes
> python -m venv venv
> venv\Scripts\activate.bat
(venv)> pip install kivy

```

sh ```
$ mkdir notes/
$ cd notes
$ python -m venv venv
$ source venv/bin/activate
(venv)$ pip install kivy

```

With these commands, you create a `todo/` folder for storing your project. Inside that folder, you create a new virtual environment, activate it, and install Kivy from [PyPI](https://pypi.org/project/Kivy/).
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
For platform-specific troublshooting, check the [Working With Python Virtual Environments](https://www.pythonguis.com/tutorials/python-virtual-environments/) tutorial.
## Creating the To-do App's Project Layout
To begin with the To-do app, we will create three files in the `todo/` directory. This way, we will separate the GUI-related code from the database logic:
  * A `main.py` file where we will have our Kivy [`App`](https://kivy.org/doc/stable/api-kivy.app.html#kivy.app.App) subclass
  * A `widgets.py` file containing widget classes or GUI components
  * A `database.py` containing the database-related code


Throughout the tutorial, we will work on these three files simultaneously. You can open them in your favorite code editor.
## Developing the To-do App's Interface
Before we proceed, let's take a look at how our To-do application will look like when we finish writing the code:
![Kivy To-do app demo](https://www.pythonguis.com/static/examples/kivy-to-do-app/kivy-todo-app-demo.png) _Kivy To-do app demo_
As you can see in the image above, the app's window displays the name followed by a text input field and a list of tasks. In addition to the text input field, we have a **_+_** button, which we will use to add the task description in the text field to the to-do list below.
Next are the tasks or to-do items. Each item contains the following widgets:
  * A button displaying the to-do task description
  * A **_Done_** button to mark an item as done
  * A **_-_** button to remove the item from the list


To create this interface, let's go to the `main.py` file and import the `App` and `Window` classes from their corresponding modules:
python ```
from kivy.app import App
from kivy.core.window import Window

```

It's important to note that the `Window` class is not intended to create the application's window. We will use this class to set the background color of our app's window.
Now, we can quickly head over to our `widgets.py` file and create our `root` widget, which we will call `MainWindow`. To do this, we will subclass the `FloatLayout` class:
python ```
from kivy.uix.floatlayout import FloatLayout
TEAL = (0, 0.31, 0.31, 1.0)
class MainWindow(FloatLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

```

Before defining `MainWindow`, we have a color tuple, `TEAL`, for defining a teal color in RGBA format. We will use this color to give the app's window a teal background.
Changing the values of the tuple will vary the window's background color. So, you can play around with the values and tweak the color as you prefer. Then, we define the `MainWindow` class as a subclass of Kivy's [`FloatLayout`](https://kivy.org/doc/stable/api-kivy.uix.floatlayout.html).
Now, let's head to `main.py` and import our recently defined `MainWindow` class. Let's also import the `MainWindow` class and the `TEAL` constant at once, and set the window's background color:
python ```
from kivy.app import App
from kivy.core.window import Window
from widgets import MainWindow, TEAL
Window.clearcolor = TEAL

```

Then, we need to define a `TodoApp` class by inheriting from `App`. Let's name this class `TodoApp`:
python ```
# ...
class TodoApp(App):
  title = "Todo App"
  def build(self):
    return MainWindow()
if __name__ == "__main__":
  todoapp = TodoApp()
  todoapp.run()

```

Inside the `TodoApp` class, we need a `build()` method that returns an instance of `MainWindow`. This instance acts as the root widget upon which every other widget in our app will be added.
At this point, we will have the following code in our `main.py` file:
python ```
from kivy.app import App
from kivy.core.window import Window
from widgets import MainWindow, TEAL
Window.clearcolor = TEAL
class TodoApp(App):
  title = "Todo App"
  def build(self):
    return MainWindow()
if __name__ == "__main__":
  todoapp = TodoApp()
  todoapp.run()

```

Also, we should have the following code in our `widgets.py` file:
python ```
from kivy.uix.floatlayout import FloatLayout
TEAL = (0, 0.31, 0.31, 1.0)
class MainWindow(FloatLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

```

Running the `main.py` file, you should get a blank teal window like the following on your screen:
![Kivy To-do app's main window](https://www.pythonguis.com/static/examples/kivy-to-do-app/kivy-todo-app-main-window.png) _Kivy To-do app's main window_
Once again back on the `widgets.py` file, let's import all the widget classes that we will need:
python ```
from kivy.effects.scroll import ScrollEffect
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

```

We will use all these Kivy widgets to build our app's GUI. But first, let's define some more colors:
python ```
# ...
TEAL = (0, 0.31, 0.31, 1.0)
YELLOW = (1.0, 0.85, 0, 1.0)
LIGHT_TEAL = (0, 0.41, 0.41, 1.0)
# ...

```

Next, we modify the `MainWindow` class by adding a couple of widgets:
python ```
# ...
class MainWindow(FloatLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    todo_list_container = BoxLayout(
      orientation="vertical",
      size_hint=[.85, None],
      height=350,
      pos_hint={"center_x":0.5, "top":0.85},
      spacing=10
    )
    title_label = Label(
      font_size=35,
      text="[b]Todo App[/b]",
      size_hint=[1, None],
      markup=True,
    )
    todo_list_container.add_widget(title_label)
    self.add_widget(todo_list_container)

```

In the class initializer, we have a `BoxLayout` instance called `todo_list_container`, with a vertical orientation, a specified size and position, and some spacing.
In addition to that, we have a label called `title_label`. This label will display the app's name, `"Todo App"`, in a larger font size and formatted as bold text. Finally, we add the label to the `todo_list_container`, and the `todo_list_container` to the `MainWindow`.
Run `main.py` again. The app's interface should look something like this now:
![Kivy To-do app's main window with the title](https://www.pythonguis.com/static/examples/kivy-to-do-app/kivy-todo-app-main-window-with-title.png) _Kivy To-do app's main window with the title_
From the image above, we notice that the label is centered on the app's window. This is because no other widgets have been added to the `todo_list_container` layout yet.
Now, let's create some more classes. First, we create a subclass of `TextInput` and call it `Input`. Our aim with this class is to limit the number of characters that the text input. In this example, we chose to allow for 65 characters:
python ```
# ...
class Input(TextInput):
  max_length = 65
  multiline = False
  def insert_text(self, *args):
    if len(self.text) < self.max_length:
      super().insert_text(*args)

```

What we've done here is override the `insert_text()` method of the `TextInput` class, adding just a little touch to it. This method is called every time we type a character into the text input, which now only accepts the maximum number of characters given by `max_length`.
Next, we'll create some customized `Button` subclasses:
python ```
# ...
class NoBackgroundButton(Button):
  background_down = ""
  background_normal = ""
  background_disabled = ""
class YellowButton(NoBackgroundButton):
  background_color = YELLOW
  color = TEAL
class LightTealButton(NoBackgroundButton):
  background_color = LIGHT_TEAL

```

We've created a `Button` subclass called `NoBackgroundButton` and adjusted some of its parent's properties. We remove the default backgrounds for its pressed, unpressed, and disabled states, allowing us to apply any color to its background without interference from its texture. With that done, we used the `NoBackgroundButton` class to define two subclasses with different color setups.
Now, we can create the input field widget, which we will call `InputFrame`. This widget will contain `Input` and `YellowButton` widgets arranged horizontally. To do this, we will use a `BoxLayout` widget:
python ```
# ...
class InputFrame(BoxLayout):
  spacing = 8
  height = 45
  size_hint_y = None
  def __init__(self, main_window, **kwargs):
    super().__init__(**kwargs)
    self.todo_input_widget = Input(
      hint_text="Enter a todo activity",
      font_size=22
    )
    self.todo_input_widget.padding = [10, 10, 10, 10]
    add_item_button = YellowButton(
      width=self.height,
      size_hint=[None, 1], text="+"
    )
    add_item_button.bind(
      on_release=lambda *args: main_window.add_todo_item(
        self.todo_input_widget.text
      )
    )
    self.add_widget(self.todo_input_widget)
    self.add_widget(add_item_button)

```

The above code defines the `InputFrame` class, which inherits from `BoxLayout`. The `InputFrame` class sets some properties, such as spacing and height. Its `size_hint_y` property was disabled, so we could set an absolute value for its height.
In the class initializer, we create an instance of `Input` named `todo_input_widget`, with its hint text set to `"Enter a todo activity"`. Then, we create an instance of `YellowButton` named `add_item_button`, which has the text `"+"` and is bound to a function that adds a to-do item when clicked.
Finally, `todo_input_widget` and `add_item_button` are added as widgets to the `InputFrame`.
Furthermore, note that we added an argument to its initializer named `main_window`. This will be an instance of the `MainWindow` class so that we can access its methods.
Now, we just add an `InputFrame` widget instance to `MainWindow`. However, rather than add it to `MainWindow` directly, we add it to the box layout, `todo_list_container`:
python ```
# ...
class MainWindow(FloatLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    # ...
    self.inputframe = InputFrame(self)
    todo_list_container.add_widget(title_label)
    todo_list_container.add_widget(self.inputframe)
    # ...

```

Next, we create the widget that will contain our list of to-do tasks in our `widgets.py` file. For this, we will create a `ScrollView` subclass, which we will call `ScrollableList`:
python ```
# ...
class ScrollableList(ScrollView):
  effect_cls = ScrollEffect
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.height = 400

```

First, we set the `effect_cls` (read as "effect class") property to `ScrollEffect`. This is not entirely necessary, but it helps prevent the `ScrollView` from scrolling beyond its contents.
Then, we create a `BoxLayout` instance with its `orientation` argument set to `vertical`. Scroll views only accept one child widget, therefore we will only add a `BoxLayout` instance to the `ScrollableList` instance. Then, we'll add new to-do items to the `BoxLayout`:
python ```
# ...
class ScrollableList(ScrollView):
  effect_cls = ScrollEffect
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.height = 400
    self.todoitems = BoxLayout(
      orientation="vertical",
      size_hint_y = None,
      spacing=14
    )

```

It's important to note that a `ScrollView` can only scroll when the height of its child, `self.todoitems` in our case, exceeds its own height. This behavior makes sense because otherwise, there wouldn't be anything to scroll to.
Therefore, whenever we add or remove a to-do item from the list, we must dynamically increase or decrease the height of the `self.todoitems` layout.
To implement this behavior, we will bind a method `adjust_height()` to a change in its property `children`: 
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
python ```
# ...
class ScrollableList(ScrollView):
  effect_cls = ScrollEffect
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.height = 400
    self.todoitems = BoxLayout(
      orientation="vertical",
      size_hint_y = None,
      spacing=14
    )
    self.todoitems.bind(children=self.adjust_height)
    self.add_widget(self.todoitems)
  def adjust_height(self, *args):
    ITEM_HEIGHT = 40
    SPACING = 14
    self.todoitems.height = (ITEM_HEIGHT + SPACING) * (
      len(self.todoitems.children)
    ) - SPACING

```

In the `ScrollableList` class, the `adjust_height()` method increases or decreases the height of the box layout `self.todoitems`. This adjustment is made by adding or subtracting the height of an `Item` widget and the vertical spacing between each `Item` widget when adding or removing items, respectively.
Now, we add an instance of `ScrollableList` to our `MainWindow`:
python ```
# ...
class MainWindow(FloatLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    # ...
    self.inputframe = InputFrame(self)
    self.scrollablelist = ScrollableList()
    self.todoitems = self.scrollablelist.todoitems
    todo_list_container.add_widget(title_label)
    todo_list_container.add_widget(self.inputframe)
    todo_list_container.add_widget(self.scrollablelist)
    self.add_widget(todo_list_container)

```

Let's now create the `Item` class that will represent each to-do item. To do this, we will use a `BoxLayout` class with its default `horizontal` orientation:
python ```
# ...
class Item(BoxLayout):
  size_hint = [1, None]
  spacing = 5
  def __init__(self, main_window, item_id, todo_item, done=False, **kwargs):
    super().__init__(**kwargs)
    self.height = 40
    self.item_id = item_id
    item_display_box = LightTealButton(text=todo_item, size_hint=[0.6, 1])
    self.mark_done_button = YellowButton(
      text="Done", size_hint=[None, 1], width=100, disabled=done
    )
    self.mark_done_button.bind(
      on_release=lambda *args: main_window.mark_as_done(item_id)
    )
    remove_button = YellowButton(
      text="-",
      size_hint=[None, 1],
      width=40
    )
    remove_button.bind(
      on_release=lambda *args: main_window.delete_todo_item(item_id)
    )
    self.add_widget(item_display_box)
    self.add_widget(self.mark_done_button)
    self.add_widget(remove_button)

```

We have defined the `Item` class inheriting from `BoxLayout`. The class will hold a button for displaying the to-do item's description, another button for marking the item as done, and a final button for deleting the item. Furthermore, we bind the `self.mark_done_button` and `remove_button` buttons to methods in the `MainWindow` class.
However, note that we haven't defined the methods that we have bound to the `on_release` event of each button. We still won't define them because they contain calls to methods of the `Database` class. We will define this class in `database.py` and when we are done there, we return to modify `widgets.py` as needed.
That aside, we can run the `main.py` again and see how far we've come. We should get the same result as shown in the image below:
![Kivy To-do app's main window with task input](https://www.pythonguis.com/static/examples/kivy-to-do-app/kivy-todo-app-main-window-with-task-input.png) _Kivy To-do app's main window with task input_
With this result, let's move to our `database.py` file so that we can implement the database operations.
## Managing the To-do Database
Now that we are partly done with the GUI, we need to store our to-do items in a database so that we can view, delete, or mark them as done.
If you are not familiar with SQL, do not fret. We will only carry out five basic [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) (create, read, update, delete) operations. We need code for retrieving, updating, and deleting items. Additionally, we have to create a database table.
Now, let's head over to `database.py` and import the `sqlite3` and `pathlib` modules:
python ```
import pathlib
import sqlite3

```

Then, we set our database filename to `todo.db`. This file will live in the project's directory. Next, we will create our `Database` class:
python ```
# ...
DATABASE_PATH = pathlib.Path(__file__).parent / "todo.db"
class Database:
  def __init__(self, db_path=DATABASE_PATH):
    self.db = sqlite3.connect(db_path)
    self.cursor = self.db.cursor()
    self.create_table()

```

Note that your file name and extension can be anything you want. Common file extensions are `.db`, `.sqlite`, and `.sqlite3`.
Next, we get a database cursor. This object allows us to execute transactions on the SQLite database from our code. Finally, we call the `create_table()` method. We'll define this method in a moment.
We will carry out only five operations on the database. Therefore, we need five different SQL queries. To run the queries, we will create five dedicated methods.
To get started, let's define the `create_table()` method for creating a database table. A table is a collection of related data organized in rows and columns. We can achieve this in just a few lines:
python ```
# ...
class Database:
  # ...
  def create_table(self):
    query = """
      CREATE TABLE IF NOT EXISTS todo(
        item_id INTEGER PRIMARY KEY,
        item TEXT,
        done INTEGER
      );
    """
    self._run_query(query)
  def _run_query(self, query, *query_args):
    result = self.cursor.execute(query, [*query_args])
    self.db.commit()
    return result

```

This method creates a table called `todo`. The SQL query is contained in the multiline string assigned to the `query` variable. This query creates that table only if it doesn't already exist.
The table will have the following three columns:
  1. **`item_id`**is a unique integer value that defines the to-do item's id.
  2. **`item`**is a string value that describes the to-do task.
  3. **`done`**is an integer value that can take either a`0` or `1` as its value. This column will allow us to mark an item as completed or done.


Once you have the target query, you can run it on the database. To do this, you use the `_run_query()` method, which takes the `query` and `*query_args` as arguments. The call to `self.cursor.execute()` runs the query on the database while the call to `self.db.commit()` saves the changes. Finally, the function returns the query result. You'll use this helper method to define a few other methods in `Database`.
We define the `add_todo_item()` method. This time for adding an item to the database:
python ```
# ...
class Database:
  # ...
  def add_todo_item(self, item):
    self._run_query(
      "INSERT INTO todo VALUES (NULL, ?, 0);",
      item,
    )

```

This method accepts a string describing a to-do item and adds it to the database with the appropriate SQL query.
Now, let's define three more methods to execute other required operations:
python ```
# ...
class Database:
  # ...
  def delete_todo_item(self, item_id):
    self._run_query(
      "DELETE FROM todo WHERE item_id=(?);",
      item_id,
    )
  def mark_as_done(self, item_id):
    self._run_query(
      "UPDATE todo SET done=1 WHERE item_id=?;",
      item_id,
    )
  def retrieve_all_items(self):
    result = self._run_query("SELECT * FROM todo;")
    return result.fetchall()

```

The `delete_todo_item()` and `mark_as_done()` methods use the `_run_query()` method to run queries that remove an item form the database and mark an item as done, respectively.
The `retrieve_all_items()` method calls `fetchall()` on `result`, which is an instance of the `sqlite3.Cursor` class. This call converts our results to a list so that we can use it latter in the app.
## Completing the To-do App's GUI
Returning to `widgets.py`, we must define additional methods within the `MainWindow` class. Before that, we need to modify its initializer by including an additional argument. This argument will be an instance of the `Database` class previously defined in `database.py`.
Now, let's update the `MainWindow` class:
python ```
# ...
class MainWindow(FloatLayout):
  def __init__(self, db, **kwargs):
    super().__init__(**kwargs)
    self.db = db
    # ...

```

Here, we've added a `db` argument to the class initializer. This argument will accept an instance of `Database`. Then, we create the `db` attribute so that we can access the database from other methods.
We'll now define other methods, starting with `add_todo_item()`. This method requires an argument called `todo_item`, which should be a string representing the to-do task or activity:
python ```
# ...
class MainWindow(FloatLayout):
  # ...
  def add_todo_item(self, todo_item):
    if todo_item.isspace() or todo_item == "":
      return
    self.db.add_todo_item(todo_item)
    self.todoitems.clear_widgets()
    self.show_existing_items()
    self.inputframe.todo_input_widget.text = ""

```

When `add_todo_item()` is called, it verifies whether the `todo_item` value contains only whitespaces or is an empty string. If this is the case, then the method returns immediately. Otherwise, the method proceeds to add the to-do activity to the database.
Afterward, the method clears the current list of to-do items using the `clear_widgets()` method and then reloads the updated list using the `show_existing_items()` method, which we'll define in a moment.
Finally, we remove the current task description by setting the `text` property of the `Input` instance to an empty string right after adding an item to the database and to-do list.
Now let's define a method called `delete_todo_item()` for deleting a to-do item:
python ```
# ...
class MainWindow(FloatLayout):
  # ...
  def delete_todo_item(self, item_id):
    for item in self.todoitems.children:
      if item.item_id == item_id:
        self.db.delete_todo_item(item_id)
        item.parent.remove_widget(item)

```

The method takes an `item_id` integer argument, finds the corresponding `Item` instance in the to-do list, and removes it from both the database and the to-do list.
Next up, we'll define the `.mark_as_done()` method to indicate that an item has been completed:
python ```
# ...
class MainWindow(FloatLayout):
  # ...
  def mark_as_done(self, item_id):
    for item in self.todoitems.children:
      if item.item_id == item_id:
        self.db.mark_as_done(item_id)
        item.mark_done_button.disabled = True

```

This method accepts an `item_id` integer argument, but this time, it marks the item as done in the database. It finds the corresponding `Item` instance in the list and disables the button used for marking the item as done.
Finally, we will code the `show_existing_items()` method. This method will display all the to-do items we have in our database, with the most recent task displayed at the top:
python ```
# ...
class MainWindow(FloatLayout):
  # ...
  def show_existing_items(self):
    items = self.db.retrieve_all_items()
    for item in reversed(items):
      item_id, todo_item, done = item
      item = Item(self, item_id, todo_item, done)
      self.todoitems.add_widget(item)

```

Here, we loop through each item in the database and create the corresponding `Item` widgets for them. Shortly after creation, each `Item` instance is added to the list, `self.todoitems`.
Head back to the `main.py` and import the `Database` class from `database.py` as follows:
python ```
# ...
from database import Database
from widgets import TEAL, MainWindow
# ...

```

Afterward, pass an instance of `Database` as an argument to `MainWindow` in the `build()` method:
python ```
# ...
class TodoApp(App):
  title = "Todo App"
  def build(self):
    return MainWindow(db=Database())
# ...

```

Now, go ahead and run `main.py`, type in a to-do activity, and add it to the list using the **_+_** button. Add other items as you like. Here's a demo of how the app should work:
![Kivy To-do app with sample tasks](https://www.pythonguis.com/static/examples/kivy-to-do-app/kivy-todo-app-main-window-with-sample-tasks.png) _Kivy To-do app with sample tasks_
## Conclusion
A journey of a thousand miles begins with a single step. In this tutorial, you have taken your first steps building more complex applications with Kivy. Furthermore, you have been introduced to storing, retrieving, and updating data to and from a local database with SQLite, using Python's `sqlite3` library.
Think about some additional features you'd like or expect to see in a Todo application and see if you can add them yourself! 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Francis Ali](https://www.pythonguis.com/static/theme/images/authors/francis-ali.jpg)](https://www.pythonguis.com/authors/francis-ali/)
**Build a To-do App With Python and Kivy** was written by [Francis Ali](https://www.pythonguis.com/authors/francis-ali/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) and [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Francis is a Python programming hobbyist and aspiring mechatronics engineer. 
**Build a To-do App With Python and Kivy** was published in [examples](https://www.pythonguis.com/examples/) on March 01, 2025 (updated April 03, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ kivy](https://www.pythonguis.com/topics/kivy/) [application](https://www.pythonguis.com/topics/application/) [to-do](https://www.pythonguis.com/topics/to-do/)
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
