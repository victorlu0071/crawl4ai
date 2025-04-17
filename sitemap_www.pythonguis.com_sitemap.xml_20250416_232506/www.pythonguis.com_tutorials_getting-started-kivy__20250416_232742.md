# Content from: https://www.pythonguis.com/tutorials/getting-started-kivy/

[](https://www.pythonguis.com/tutorials/getting-started-kivy/#menu)
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
# Getting Started With Kivy for GUI Development
Your First Steps With the Kivy Library for GUI Development
by [Francis Ali](https://www.pythonguis.com/authors/francis-ali/) Last updated Mar 26 [ Tutorials ](https://www.pythonguis.com/tutorials/)
Kivy is an open-source Python software library for developing graphical user interfaces. It supports cross-platform development for the desktop as well as the creation of multi-touch apps for mobile devices.
Kivy apps can run across several platforms, including Windows, Linux, macOS, Android, and IOS. One place where Kivy particularly shines is in game development. By combining Kivy's 2D physics capabilities with a simple physics engine, you can create impressive 2D simulations and games.
In this article, you'll learn about using Kivy to develop Python apps. We will go through an introduction to Kivy and what it can do. You'll learn how to create a simple Kivy app in Python and learn the basics of Kivy's styling language, known as _Kv_. Finally, you'll use Kivy's `graphics` module to draw 2D shapes on the Kivy canvas.
To get the most out of this tutorial, you should have basic knowledge of Python. Previous knowledge of general concepts of GUI programming, such as event loops, widgets, layouts, and forms, is also a plus.
Table of Contents
  * [Installing Kivy](https://www.pythonguis.com/tutorials/getting-started-kivy/#installing-kivy)
  * [Writing Your First Kivy GUI App in Python](https://www.pythonguis.com/tutorials/getting-started-kivy/#writing-your-first-kivy-gui-app-in-python)
  * [Exploring Widgets and Layouts](https://www.pythonguis.com/tutorials/getting-started-kivy/#exploring-widgets-and-layouts)
    * [Widgets](https://www.pythonguis.com/tutorials/getting-started-kivy/#widgets)
    * [Layouts](https://www.pythonguis.com/tutorials/getting-started-kivy/#layouts)
  * [Using Widgets and Layouts: A Practical Example](https://www.pythonguis.com/tutorials/getting-started-kivy/#using-widgets-and-layouts-a-practical-example)
  * [Drawing Shapes in Kivy: The canvas Property](https://www.pythonguis.com/tutorials/getting-started-kivy/#drawing-shapes-in-kivy-the-canvas-property)
  * [Styling Your GUIs With the Kivy Language](https://www.pythonguis.com/tutorials/getting-started-kivy/#styling-your-guis-with-the-kivy-language)
    * [Relying on the Automatic Widget Loading](https://www.pythonguis.com/tutorials/getting-started-kivy/#relying-on-the-automatic-widget-loading)
    * [Loading Widgets Through the Builder Class](https://www.pythonguis.com/tutorials/getting-started-kivy/#loading-widgets-through-the-builder-class)
  * [More Resources](https://www.pythonguis.com/tutorials/getting-started-kivy/#more-resources)
  * [Conclusion](https://www.pythonguis.com/tutorials/getting-started-kivy/#conclusion)


There are many different Python GUI libraries available, and choosing one for your project can be a really tough and confusing decision to make. For advice see our guide [Which Python GUI Library to Choose for your Project](https://www.pythonguis.com/faq/which-python-gui-library/).
Let's get started. We'll first take a few moments to install and set up Kivy on your computer.
## Installing Kivy
Before using a third-party library like Kivy, we must install it in our working environment. Installing Kivy is as quick as running the `python -m pip install kivy` command on your terminal or command line. This command will install the library from the [Python package index (PyPI)](https://pypi.org/).
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Note that as of the time of writing this tutorial, Kivy only officially supports Python versions up to 3.10. For detailed information about installing Kivy, visit the official [installation guide](https://kivy.org/doc/stable/gettingstarted/installation.html).
However, when working with third-party libraries, it's good practice to create a Python [virtual environment](https://docs.python.org/3/tutorial/venv.html), which is a self-contained Python installation for a particular version of Python that you can use to isolate the dependencies of a given project.
To create a virtual environment, you'll typically use Python's [`venv`](https://docs.python.org/3/library/venv.html#module-venv) module from the [standard library](https://docs.python.org/3/library/index.html). Fire up a command-line window and type in the following command in your working directory.
sh ```
$ python -m venv kivy_env

```

This command will create a folder called `kivy_env` containing a Python virtual environment. The Python version in this environment is the same as you get when you run `python --version` on your command line.
Next, we need to activate the virtual environment. Use the appropriate command, depending on whether you're on Windows, macOS, or Linux:
  * Windows
  * macOS
  * Linux


sh ```
C:/> .\kivy_env\Scripts\activate

```

sh ```
$ source kivy_env/bin/activate

```

sh ```
$ source kivy_env/bin/activate

```

Once that's confirmed to be working, you can then install Kivy within the virtual environment you just created by running the following:
sh ```
(kivy_env) $ python -m pip install kivy

```

With this command, you'll install Kivy in your active Python virtual environment, so you're now ready to go.
You can also install Kivy by downloading its source code directly from GitHub and doing a manual installation on the command line. For more information on following this installation path, check out the section about installing Kivy from [source](https://kivy.org/doc/stable/gettingstarted/installation.html#from-source) in the documentation.
## Writing Your First Kivy GUI App in Python
Without further ado, let's get right into creating our first app with Kivy and Python. For this app, we will use a [`Label`](https://kivy.org/doc/stable/api-kivy.uix.label.html#module-kivy.uix.label) object to display the traditional `"Hello, World!"` message on our screen. To write a [minimal Kivy GUI app](https://kivy.org/doc/stable/guide/basic.html#create-an-application), we need to run a few steps:
  1. Subclassing the [`App`](https://kivy.org/doc/stable/api-kivy.app.html#kivy.app.App) class
  2. Implementing its [`build()`](https://kivy.org/doc/stable/api-kivy.app.html#kivy.app.App.build) method, which returns a [`Widget`](https://kivy.org/doc/stable/api-kivy.uix.widget.html#module-kivy.uix.widget) instance
  3. Instantiating this class and calling its [`run()`](https://kivy.org/doc/stable/api-kivy.app.html#kivy.app.App.run) method


Let's start by importing the required classes. For our example, we only need the `App` and `Label` classes. Create a Python file called `app.py` and add the following imports:
python ```
from kivy.app import App
from kivy.uix.label import Label

```

The `App` class provides the base functionality required to create GUI apps with Kivy, such as managing the event loop. Meanwhile, the `Label` class will work as the root visual element or _widget_ for our GUI.
Next, we can create our subclass of `App`. We have called it `MainApp` here. However, you can call it whatever you like:
python ```
from kivy.app import App
from kivy.uix.label import Label
class MainApp(App):
  def build(self):
    return Label(text="Hello, World!")

```

This subclass uses the concept of **inheritance** in object-oriented programming (OOP) in Python. All the attributes and methods defined in the superclass, `App`, are automatically _inherited_ by the subclass, `MainApp`.
In order for our app to create a UI, we need to define a `build()` method. In `build()`, we create and return either a widget or layout, which will be the root object in our UI structure.
The `build()` method is the entry point to whatever will be drawn on the screen. In our example, it creates and returns a label with the `"Hello, World!"` text on it.
Finally, we need to create an instance of `MainApp` and call its `run()` method:
python ```
from kivy.app import App
from kivy.uix.label import Label
class MainApp(App):
  def build(self):
    return Label(text="Hello, World!")
MainApp().run()

```

In the final line, we create an instance of `MainApp` and call its `run()` method. This method launches the application and runs its main loop. That's it! We're ready to run our first Kivy app. Open your command line and run the following command:
sh ```
$ python app.py

```

You'll see the following window on your screen:
![First Kivy GUI Application](https://www.pythonguis.com/static/tutorials/kivy/getting-started-kivy/kivy-first-app.png) _First Kivy GUI Application_
Great! You've just written your first Kivy GUI app using Python. It shows a black window with the message `"Hello, World!"` In its center. Note that the window's title bar shows the title `Main`, which comes from the name of your `App` subclass.
The next step is to explore some other essential features of Kivy that will allow you to write fully-functional GUI apps with this library.
## Exploring Widgets and Layouts
In the previous section, we mentioned **widgets** and **layouts** a few times -- you may be wondering what they are! A widget is an element of a GUI that displays information or provides a specific function. They allow your users to interact with your app's GUI.
A layout, on the other hand, provides a way of arranging widgets into a particular structure in your application's windows. A layout can also give certain behaviors to widgets that belong to it, like the [`ScatterLayout`](https://kivy.org/doc/stable/api-kivy.uix.scatterlayout.html), which enables multi-touch resizing of a child widget.
In Kivy, you'll find widget and layout classes in their corresponding module under the [`kivy.uix`](https://kivy.org/doc/stable/api-kivy.uix.html?highlight=uix#module-kivy.uix) module. For example, to import the `Button` class, we can use:
python ```
from kivy.uix.button import Button

```

In Kivy, widgets and layout classes are usually located in modules named after the class itself. However, the class uses [CamelCase](https://en.wikipedia.org/wiki/Camel_case), and the containing module uses lower casing.
For example, take the following imports:
python ```
# Widgets
from kivy.uix.label import Label
from kivy.uix.image import Image
# Layouts
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

```

You'll find some exceptions to this naming convention. For example:
python ```
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import FadeTransition

```

This commonly happens with modules that define multiple and closely related classes, such as `Image` and `AsyncImage`.
### Widgets
Widgets are the building blocks of Kivy-based GUIs. Some of the most commonly used GUI widgets in Kivy apps include the following:
  * [`Widget`](https://kivy.org/doc/stable/api-kivy.uix.widget.html) is the base class required for creating widgets.
  * [`Label`](https://kivy.org/doc/stable/api-kivy.uix.label.html) is used for rendering text on windows and dialogs.
  * [`TextInput`](https://kivy.org/doc/stable/api-kivy.uix.textinput.html) provides a box for editable plain text.
  * [`Button`](https://kivy.org/doc/stable/api-kivy.uix.button.html) triggers actions when the user presses it.
  * [`CheckBox`](https://kivy.org/doc/stable/api-kivy.uix.checkbox.html) provides a two-state button that can be either checked or unchecked.
  * [`Image`](https://kivy.org/doc/stable/api-kivy.uix.image.html) is used to display an image on your GUIs.
  * [`ProgressBar`](https://kivy.org/doc/stable/api-kivy.uix.progressbar.html) visualizes the progress of some tasks.
  * [`DropDown`](https://kivy.org/doc/stable/api-kivy.uix.dropdown.html) provides a versatile drop-down list that can list different widgets.


With these widgets and some others that Kivy provides, you can build complex and user-friendly interfaces for your applications.
### Layouts
Kivy also has a rich set of layout classes that allows you to arrange your widgets coherently and functionally to build up GUIs. Some examples of common layouts include:
  * [`BoxLayout`](https://kivy.org/doc/stable/api-kivy.uix.boxlayout.html#module-kivy.uix.boxlayout) arranges widgets sequentially in either a vertical or horizontal fashion.
  * [`FloatLayout`](https://kivy.org/doc/stable/api-kivy.uix.floatlayout.html#module-kivy.uix.floatlayout) arranges widgets in a specific position on the containing window.
  * [`RelativeLayout`](https://kivy.org/doc/stable/api-kivy.uix.relativelayout.html#module-kivy.uix.relativelayout) arranges child widgets according to relative positions.
  * [`GridLayout`](https://kivy.org/doc/stable/api-kivy.uix.gridlayout.html#module-kivy.uix.gridlayout) arranges widgets in a grid defined by the rows and columns.
  * [`PageLayout`](https://kivy.org/doc/stable/api-kivy.uix.pagelayout.html#module-kivy.uix.pagelayout) creates multi-page layouts in a way that allows flipping from one page to another.
  * [`ScatterLayout`](https://kivy.org/doc/stable/api-kivy.uix.scatterlayout.html#module-kivy.uix.scatterlayout) positions its child widgets similarly to a `RelativeLayout`.
  * [`StackLayout`](https://kivy.org/doc/stable/api-kivy.uix.stacklayout.html#module-kivy.uix.stacklayout) stacks in a left-to-right and then top-to-bottom order, or top-to-bottom then left-to-right order.


You can combine and nest layouts together to build complex user interfaces.
## Using Widgets and Layouts: A Practical Example
As an example of how to use widgets and layouts in Kivy, let's look at a commonly used layout class: the `GridLayout`. With this class, we can create a grid of rows and columns. Each cell of the grid has a unique pair of zero-based coordinates. Consider the following example:
python ```
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
ROWS = COLS = 3
class GridApp(App):
  def build(self):
    root = GridLayout(rows=ROWS, cols=COLS)
    for i in range(ROWS):
      for j in range(COLS):
        root.add_widget(Button(text=f"({i}, {j})"))
    return root
GridApp().run()

```

In the `build()` method, we instantiate the `GridLayout` with three rows and three columns. Then use a `for` loop to add button widgets to the layout using the `add_widget()` method.
When we run this app, we get the window that is shown below:
![Grid Layout in Kivy](https://www.pythonguis.com/static/tutorials/kivy/getting-started-kivy/kivy-grid-layout-app.png) _Grid Layout in Kivy_
Each button on the grid shows its corresponding pair of coordinates. The first coordinate represents the row, while the second represents the column. Like the rest of the layout classes, `GridLayout` can take several arguments that you can use to fine-tune its behavior.
## Drawing Shapes in Kivy: The `canvas` Property
To deeply customize a GUI or design a 2D video game, we may need to draw 2D shapes, such as a rectangle, circle, ellipse, or triangle. Doing this is straightforward in Kivy. The library provides a rich set of shape classes that you can find in the [`kivy.graphics`](https://kivy.org/doc/stable/api-kivy.graphics.html#module-kivy.graphics) package. Some of these classes include:
  * [`Ellipse`](https://kivy.org/doc/stable/api-kivy.graphics.html#kivy.graphics.Ellipse)
  * [`Line`](https://kivy.org/doc/stable/api-kivy.graphics.html?highlight=graphics#kivy.graphics.Line)
  * [`Rectangle`](https://kivy.org/doc/stable/api-kivy.graphics.html#kivy.graphics.Rectangle)
  * [`Triangle`](https://kivy.org/doc/stable/api-kivy.graphics.html#kivy.graphics.Triangle)


To draw a shape on the screen with Kivy, we need to use the `canvas` property of a `Widget` object. This property holds an instance of the [`Canvas`](https://kivy.org/doc/stable/api-kivy.graphics.instructions.html#module-kivy.graphics.instructions) class, which lives in the `kivy.graphics` package.
Let's see how this works with an example of a white square drawn on the screen:
python ```
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
class CanvasApp(App):
  def build(self):
    root = Widget()
    size = 200
    width, height = Window.size
    pos_x = 1/2 * (width - size)
    pos_y = 1/2 * (height - size)
    with root.canvas:
      Rectangle(size=[size, size], pos=[pos_x, pos_y])
    return root
CanvasApp().run()

```

Inside `build()`, we create the `root` widget and define the `size` of our shape. It'll be a square shape, so each side is equal. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Next, we compute the coordinates to center our shape on the window. The coordinates passed when creating the shape are for the _top left_ corner of the window.
To calculate the correct values, we take the `width` and `height` of our main window, halving these values to get the center. We then subtract half of the width or height of our shape to position the center of our shape in the middle of the window. This can be simplified to `1/2 * (width - size)` or `1/2 * (height - size)`. We store the resulting top left coordinates in `pos_x` and `pos_y`.
Next, we use the `canvas` property of our root window to draw the shape. This property supports the `with` statement, which provides the appropriate context for creating our shapes. Inside the `with` block, we define our `Rectangle` instance with the `size` and `pos` arguments.
Finally, we return the `root` widget as expected. The final line of code creates the app instance and calls its `run()` method. If you run this app from your command line, then you'll get the following window on the screen:
![Drawing Shapes in Kivy With Canvas](https://www.pythonguis.com/static/tutorials/kivy/getting-started-kivy/kivy-canvas-white-square.png) _Drawing Shapes in Kivy With Canvas_
Cool! You've drawn a square on your Kivy app. The computed coordinates place the square in the center of the window. The default color is white. However, we can change it:
python ```
# ...
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
# ...
class CanvasApp(App):
  def build(self):
    # ...
    with root.canvas:
      Color(1, 1, 0, 1)
      Rectangle(size=[side, side], pos=[pos_x, pos_y])
 # ...

```

In this code snippet, we have added an import for the `Color` class from the `graphics` package. The `Color` class accepts four numeric arguments between `0` and `1` representing the red, green, blue, and transparency components of our target color.
For example, the values `(1, 0, 0, 1)` represent an entirely red and fully opaque color. The value `(0, 1, 0, 0.5)` is fully green, half opaque, and half transparent. Consequently, the value `(1, 1, 0, 1)` gives a fully opaque yellow color. So, if you run the app, then you'll get the following output:
![Drawing Shapes in Color With Kivy](https://www.pythonguis.com/static/tutorials/kivy/getting-started-kivy/kivy-canvas-yellow-square.png) _Drawing Shapes in Color With Kivy_
We can experiment with different color values and also with different shape classes, which is cool.
Finally, note that to see the effect of the `Color()` on the drawn rectangle, the `Color` class must be instantiated before the `Rectangle` class. You can think of this as dipping your paintbrush on a palette before using it to paint on your canvas! Interestingly, any drawing that comes after the `Color` instance is painted accordingly so long as a different color has not been applied.
Using the `with` statement is pretty convenient and facilitates working with shapes. Alternatively, we can use the `canvas.add()` method:
python ```
root.canvas.add(Color(1, 1, 0, 1))
root.canvas.add(
  Rectangle(size=[side, side], pos=[pos_x, pos_y])
)

```

These statements are equivalent to the statements we have in the `with` block. Go ahead and give it a try yourself.
## Styling Your GUIs With the Kivy Language
Kivy also provides a declarative [language](https://kivy.org/doc/stable/guide/lang.html) known as the Kv language, which aims at separating your application's GUI design and business logic. In this tutorial, we will not go deep into using the Kv language. However, we will highlight some of its main features and strengths.
With Kv language, you can declare and style the widgets and graphical components of your GUI apps. You will put your Kv code in files with the `.kv` extension. Then you can load the content of these files into your app to build the GUI. You'll have at least two ways to load the content of a `.kv` file:
  * Relying on the automatic loading mechanism
  * Using the `Builder` class for manual loading


In the following sections, you'll learn the basics of these two ways of using the Kv language to build the GUI of your Kivy apps.
### Relying on the Automatic Widget Loading
As stated earlier, the Kv language helps you separate business logic from GUI design. Let's illustrate this possibility with an updated version of our `"Hello, World!"` app:
python ```
from kivy.app import App
from kivy.uix.label import Label
class CustomLabel(Label):
  pass
class MainApp(App):
  def build(self):
    root = CustomLabel()
    return root
MainApp().run()

```

As you can see we have subclassed the `Label` class to create a new `CustomLabel` haven't made any modifications to the subclass, so it functions exactly like the `Label` class but with a different name. We add a `pass` statement, which is a Python _placeholder_ statement which makes the code syntactically valid.
Next, create a file called `main.kv` alongside your app's file. Define a label using the following code:
kv ```
<CustomLabel>:
  text: "Hello, World!"

```

Note that your label must have the same name as your custom Python class in the app's file. Additionally, the `.kv` file must have the same name as your subclass of `App`, but without the _App_ suffix and in lowercase. In this example, your subclass is named `MainApp`, so your `.kv` file must be `main.kv`.
Now you can run the app from your command line. You'll get the following window on your screen:
![Kivy Application Using the Kv Language](https://www.pythonguis.com/static/tutorials/kivy/getting-started-kivy/kivy-app-kv-lang.png) _Kivy Application Using the Kv Language_
The Kv language, also known as kivy language or just kvlang, allows us to create widget trees in a declarative way. It also lets you bind widget properties to each other or to callbacks.
### Loading Widgets Through the `Builder` Class
When your Kivy project grows, your `.kv` file will grow as well. So, it is recommended that you split up the file into different files for readability. In such cases, you will end up with multiple `.kv` files, and the automatic loading mechanism will not be sufficient. You'll have to use the `Builder` class from `kivy.lang.Builder`.
To explore how to use `Builder`, let's build a sample GUI consisting of a label and button in a `BoxLayout`. The label will be provided in the `labels.kv` file, while the buttons will live in the `buttons.kv` file.
Here's the Python code for this app:
python ```
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
Builder.load_file("labels.kv")
Builder.load_file("buttons.kv")
class CustomLabel(Label):
  pass
class CustomButton(Button):
  pass
class MainApp(App):
  def build(self):
    root = BoxLayout(orientation="vertical")
    root.add_widget(CustomLabel())
    root.add_widget(CustomButton())
    return root
MainApp().run()

```

After importing the required classes, we call the `load_file()` method. This method takes the filename of a `.kv` file as an argument and loads it into your app.
Next, you create the custom label and button following the pattern used in the previous section. Inside `build()`, you create a `BoxLayout` and add the two widgets to it. Now you need to provide the required `.kv` files.
Go ahead and create a `labels.kv` file with the following content:
kv ```
<CustomLabel>:
  text: "This is a custom label!"
  font_size: 50
  bold: True

```

This file provides a label with the text `"This is a custom label!"`. Its font will have a size of `50` pixels and will be bold.
The `buttons.kv` will have the following code:
kv ```
<CustomButton>:
  text: "Click me!"

```

Your custom button will be quite minimal. It'll only have the text `"Click me!"` on it. Go ahead and run the app from your command line. You'll get the following window on your screen:
![Kivy Application Using the Kv Language With Multiple kv Files](https://www.pythonguis.com/static/tutorials/kivy/getting-started-kivy/kivy-app-multiple-kv-files.png) _Kivy Application Using the Kv Language With Multiple kv Files_
In addition to using the `load_file()` to build Kv language files, you can also parse and load Kv language directly in a multi-line string in your Python file:
python ```
Builder.load_string("""
<CustomLabel>:
  text: "This is a custom label!"
  font_size: 50
  bold: True
""")
Builder.load_string("""
<CustomButton>:
  text: "Click me!"
""")

```

These calls to `load_string()` are completely equivalent to the corresponding calls to `load_file()` in our original code example.
Let's take a look at a final example of using the Kv language. This time we'll use the language to draw shapes. Create a `rectangle.py` file with the following content:
python ```
from kivy.app import App
from kivy.uix.widget import Widget
class CustomRectangle(Widget):
  pass
class MainApp(App):
  def build(self):
    return CustomRectangle()
MainApp().run()

```

Now go ahead and create another file in the same directory and save it as `main.kv`. Then add the following content:
kv ```
<CustomRectangle>:
 canvas:
  Color:
   rgba: 1, 1, 0, 1
  Rectangle:
   size: 200, 200
   pos: 0, 0

```

If you run the `rectangle.py` file, then you will see a 200×200 pixels rectangle ---square in this case--- at the lower left corner of your window! For more guidelines on using Kv Language, check out its official [documentation](https://kivy.org/doc/stable/api-kivy.lang.html#module-kivy.lang).
## More Resources
For some more examples of what you can do with Kivy, take a look at the [Kivy examples](https://kivy.org/doc/stable/examples/) section in the documentation. Depending on your interest, you can also the other resources. For example:
  * If you're interested in 3D, then the [Kivy 3D demo](https://kivy.org/doc/stable/examples/gen__3Drendering__main__py.html) gives a good demonstration of the framework's rendering abilities.
  * If you're interested in using Kivy to develop for mobile, you can write functional Android apps (APKs) with Python and pack them using tools like [Buildozer](https://buildozer.readthedocs.io/en/latest/) and [Python-For-Android](https://python-for-android.readthedocs.io/en/latest/) without learning Java.
  * If you want a complete vision of where you can use Kivy, then check out the [gallery](https://kivy.org/gallery.html) of examples provided by the Kivy community.


## Conclusion
What you've learned in this tutorial is just the tip of the Kivy iceberg. There's so much more to Kivy than what meets the eye. It's a powerful GUI library that provides a well-structured hierarchy of classes and objects that you can use to create modern and cross-platform GUIs for your applications.
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Francis Ali](https://www.pythonguis.com/static/theme/images/authors/francis-ali.jpg)](https://www.pythonguis.com/authors/francis-ali/)
**Getting Started With Kivy for GUI Development** was written by [Francis Ali](https://www.pythonguis.com/authors/francis-ali/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) and [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Francis is a Python programming hobbyist and aspiring mechatronics engineer. 
**Getting Started With Kivy for GUI Development** was published in [tutorials](https://www.pythonguis.com/tutorials/) on May 31, 2023 (updated March 26, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ kivy](https://www.pythonguis.com/topics/kivy/) [widget](https://www.pythonguis.com/topics/widget/) [layout](https://www.pythonguis.com/topics/layout/) [application](https://www.pythonguis.com/topics/application/) [kvlang](https://www.pythonguis.com/topics/kvlang/)
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
