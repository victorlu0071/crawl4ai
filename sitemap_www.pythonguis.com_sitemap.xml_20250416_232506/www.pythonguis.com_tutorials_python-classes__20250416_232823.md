# Content from: https://www.pythonguis.com/tutorials/python-classes/

[](https://www.pythonguis.com/tutorials/python-classes/#menu)
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
# Working With Classes in Python and PyQt
Understanding the Intricacies of Python Classes
by [Leo Well](https://www.pythonguis.com/authors/leo-well/) Last updated Oct 18 [ Tutorials ](https://www.pythonguis.com/tutorials/)
Python supports [object-oriented programming (OOP)](https://en.wikipedia.org/wiki/Object-oriented_programming) through classes, which allow you to bundle data and behavior in a single entity. Python classes allow you to quickly model concepts by creating representations of real objects that you can then use to organize your code.
Most of the currently available GUI frameworks for Python developers, such as PyQt, PySide, and Tkinter, rely on classes to provide apps, windows, widgets, and more. This means that you'll be actively using classes for designing and developing your GUI apps.
In this tutorial, you'll learn how OOP and classes work in Python. This knowledge will allow you to quickly grasp how GUI frameworks are internally organized, how they work, and how you can use their classes and APIs to create robust GUI applications.
Table of Contents
  * [Defining Classes in Python](https://www.pythonguis.com/tutorials/python-classes/#defining-classes-in-python)
    * [Adding Class and Instance Аttributes](https://www.pythonguis.com/tutorials/python-classes/#adding-class-and-instance-ttributes)
    * [Providing Behavior With Methods](https://www.pythonguis.com/tutorials/python-classes/#providing-behavior-with-methods)
    * [Writing Getter & Setter Methods](https://www.pythonguis.com/tutorials/python-classes/#writing-getter-setter-methods)
    * [Writing Special Methods](https://www.pythonguis.com/tutorials/python-classes/#writing-special-methods)
  * [Reusing Code With Inheritance](https://www.pythonguis.com/tutorials/python-classes/#reusing-code-with-inheritance)
  * [Using Classes in PyQt GUI Apps](https://www.pythonguis.com/tutorials/python-classes/#using-classes-in-pyqt-gui-apps)
  * [Wrapping Up Classes-Related Concepts](https://www.pythonguis.com/tutorials/python-classes/#wrapping-up-classes-related-concepts)
  * [Conclusion](https://www.pythonguis.com/tutorials/python-classes/#conclusion)


## Defining Classes in Python
Python classes are templates or blueprints that allow us to create objects through **instantiation**. These objects will contain data representing the object's state, and methods that will act on the data providing the object's behavior.
Instantiation is the process of creating instances of a class by calling the **class constructor** with appropriate arguments.
Attributes and methods make up what is known as the class **interface** or [API](https://en.wikipedia.org/wiki/API). This interface allows us to operate on the objects without needing to understand their internal implementation and structure.
Alright, it is time to start creating our own classes. We'll start by defining a `Color` class with minimal functionality. To do that in Python, you'll use the `class` keyword followed by the class name. Then you provide the class body in the next [indentation](https://en.wikipedia.org/wiki/Indentation_\(typesetting\)) level:
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
python ```
>>> class Color:
...   pass
...
>>> red = Color()
>>> type(red)
<class '__main__.Color'>

```

In this example, we defined our `Color` class using the `class` keyword. This class is empty. It doesn't have attributes or methods. Its body only contains a `pass` statement, which is Python's way to do nothing.
Even though the class is minimal, it allows us to create instances by calling its constructor, `Colo()`. So, `red` is an instance of `Color`. Now let's make our `Color` class more fun by adding some attributes.
### Adding Class and Instance Аttributes
Python classes allow you to add two types of attributes. You can have **class** and **instance attributes**. A class attribute belongs to its containing class. Its data is common to the class and all its instances. To access a class attribute, we can use either the class or any of its instances.
Let's now add a class attribute to our `Color` class. For example, let's say we need to keep note of how many instance of `Color` your code creates. Then you can have a `color_count` attribute:
python ```
>>> class Color:
...   color_count = 0
...   def __init__(self):
...     Color.color_count += 1
...
>>> red = Color()
>>> green = Color()
>>> Color.color_count
2
>>> red.color_count
2

```

Now `Color` has a class attribute called `color_count` that gets incremented every time we create a new instance. We can quickly access that attribute using either the class directly or one of its instances, like `red`.
To follow up with this example, say that we want to represent our `Color` objects using red, green, and blue attributes as part of the [RGB color model](https://en.wikipedia.org/wiki/RGB_color_model). These attributes should have specific values for specific instances of the class. So, they should be instance attributes.
To add an instance attribute to a Python class, you must use the `.__init__()` special method, which we introduced in the previous code but didn't explain. This method works as the instance initializer because it allows you to provide initial values for instance attributes:
python ```
>>> class Color:
...   color_count = 0
...   def __init__(self, red, green, blue):
...     Color.color_count += 1
...     self.red = red
...     self.green = green
...     self.blue = blue
...
>>> red = Color(255, 0, 0)
>>> red.red
255
>>> red.green
0
>>> red.blue
0
>>> Color.red
Traceback (most recent call last):
  ...
AttributeError: type object 'Color' has no attribute 'red'

```

Cool! Now our `Color` class looks more useful. It has the usual class attributes and also three new instance attributes. Note that, unlike class attributes, instance attributes can't be accessed through the class itself. They're specific to a concrete instance.
There's something that jumps into sight in this new version of `Color`. What is the `self` argument in the definition of `.__init__()`? This attribute holds a reference to the current instance. Using the name `self` to identify the current instance is a strong convention in Python.
We'll use `self` as the first or even the only argument to instance methods like `.__init__()`. Inside an instance method, we'll use `self` to access other methods and attributes defined in the class. To do that, we must prepend `self` to the name of the target attribute or method instance of the class.
For example, our class has an attribute `.red` that we can access using the syntax `self.red` inside the class. This will return the number stored under that name. From outside the class, you need to use a concrete instance instead of `self`.
### Providing Behavior With Methods
A class bundles data (attributes) and behavior (methods) together in an object. You'll use the data to set the object's state and the methods to operate on that data or state.
Methods are just functions that we define inside a class. Like functions, methods can take arguments, return values, and perform different computations on an object's attributes. They allow us to make our objects usable.
In Python, we can define three types of methods in our classes:
  1. **Instance method** s, which need the instance (`self`) as their first argument
  2. **Class methods** , which take the class (`cls`) as their first argument
  3. **Static methods** , which take neither the class nor the instance


Let's now talk about instance methods. Say that we need to get the attributes of our `Color` class as a tuple of numbers. In this case, we can add an `.as_tuple()` method like the following:
python ```
class Color:
  representation = "RGB"
  def __init__(self, red, green, blue):
    self.red = red
    self.green = green
    self.blue = blue
  def as_tuple(self):
    return self.red, self.green, self.blue

```

This new method is pretty straightforward. Since it's an instance method, it takes `self` as its first argument. Then it returns a tuple containing the attributes `.red`, `.green`, and `.blue`. Note how you need to use `self` to access the attributes of the current instance inside the class.
This method may be useful if you need to iterate over the RGB components of your color objects:
python ```
>>> red = Color(255, 0, 0)
>>> red.as_tuple()
(255, 0, 0)
>>> for level in red.as_tuple():
...   print(level)
...
255
0
0

```

Our `as_tuple()` method works great! It returns a tuple containing the RGB components of our color objects.
We can also add class methods to our Python classes. To do this, we need to use the [`@classmethod`](https://docs.python.org/3/library/functions.html#classmethod) decorator as follows:
python ```
class Color:
  representation = "RGB"
  def __init__(self, red, green, blue):
    self.red = red
    self.green = green
    self.blue = blue
  def as_tuple(self):
    return self.red, self.green, self.blue
  @classmethod
  def from_tuple(cls, rbg):
    return cls(*rbg)

```

The `from_tuple()` method takes a tuple object containing the RGB components of a desired color as an argument, creates a valid color object from it, and returns the object back to the caller:
python ```
>>> blue = Color.from_tuple((0, 0, 255))
>>> blue.as_tuple()
(0, 0, 255)

```

In this example, we use the `Color` class to access the class method `from_tuple()`. We can also access the method using a concrete instance of this class. However, in both cases, we'll get a completely new object.
Finally, Python classes can also have static methods that we can define with the [`@staticmethod`](https://docs.python.org/3/library/functions.html#staticmethod) decorator:
python ```
class Color:
  representation = "RGB"
  def __init__(self, red, green, blue):
    self.red = red
    self.green = green
    self.blue = blue
  def as_tuple(self):
    return self.red, self.green, self.blue
  @classmethod
  def from_tuple(cls, rbg):
    return cls(*rbg)
  @staticmethod
  def color_says(message):
    print(message)

```

Static methods don't operate either on the current instance self or the current class `cls`. These methods can work as independent functions. However, we typically put them inside a class when they are related to the class, and we need to have them accessible from the class and its instances.
Here's how the method works:
python ```
>>> Color.color_says("Hello from the Color class!")
Hello from the Color class!
>>> red = Color(255, 0, 0)
>>> red.color_says("Hello from the red instance!")
Hello from the red instance!

```

This method accepts a message and prints it on your screen. It works independently from the class or instance attributes. Note that you can call the method using the class or any of its instances.
### Writing Getter & Setter Methods
Programming languages like Java and C++ rely heavily on setter and getter methods to retrieve and update the attributes of a class and its instances. These methods encapsulate an attribute allowing us to get and change its value without directly accessing the attribute itself.
For example, say that we have a `Label` class with a `text` attribute. We can make `text` a non-public attribute and provide getter and setter methods to manipulate the attributes according to our needs:
python ```
class Label:
  def __init__(self, text):
    self.set_text(text)
  def text(self):
    return self._text
  def set_text(self, value):
    self._text = str(value)

```

In this class, the `text()` method is the getter associated with the `._text` attribute, while the `set_text()` method is the setter for `._text`. Note how `._text` is a non-public attribute. We know this because it has a leading underscore on its name.
The setter method calls `str()` to convert any input value into a string. Therefore, we can call this method with any type of object. It will convert any input argument into a string, as you will see in a moment.
If you come from programming languages like Java or C++, you need to know Python doesn't have the notion of **private** , **protected** , and **public** attributes. In Python, you'll use a naming convention to signal that an attribute is non-public. This convention consists of adding a leading underscore to the attribute's name. Note that this naming pattern only indicates that the attribute isn't intended to be used directly. It doesn't prevent direct access, though.
This class works as follows:
python ```
>>> label = Label("Python!")
>>> label.text()
'Python!'
>>> label.set_text("PyQt!")
>>> label.text()
'PyQt!'
>>> label.set_text(123)
>>> label.text()
'123'

```

In this example, we create an instance of `Label`. The original text is passed to the class constructor, `Label()`, which automatically calls `__init__()` to set the value of `._text` by calling the setter method `text()`. You can use `text()` to access the label's text and `set_text()` to update it. Remember that any input will be converted into a string, as we can see in the final example above.
Note that the `Label` class above is just a toy example, don't confuse this class with similarly named classes from GUI frameworks like PyQt, PySide, and Tkinter.
The getter and setter pattern is pretty common in languages like Java and C++. Because PyQt and PySide are Python bindings to the Qt library, which is written in C++, you'll be using this pattern a lot in your Qt-based GUI apps. However, this pattern is less popular among Python developers. Instead, they use the `@property` decorator to hide attributes behind properties.
Here's how most Python developer will write their `Label` class:
python ```
class Label:
  def __init__(self, text):
    self.text = text
  @property
  def text(self):
    return self._text
  @text.setter
  def text(self, value):
    self._text = str(value)

```

This class defines `.text` as a property. This property has getter and setter methods. Python calls them automatically when we access the attribute or update its value in an assignment: 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
python ```
>>> label = Label("Python!")
>>> label.text
'Python!'
>>> label.text = "PyQt"
>>> label.text
'PyQt'
>>> label.text = 123
>>> label.text
'123'

```

Python properties allow you to add function behavior to your attributes while permitting you to use them as normal attributes instead of as methods.
### Writing Special Methods
Python supports many [special methods](https://docs.python.org/3/glossary.html#term-special-method), also known as **dunder** or **magic** methods, that are part of its class mechanism. We can identify these methods because their names start and end with a double underscore, which is the origin of their other name: dunder methods.
These methods accomplish different tasks in Python's class mechanism. They all have a common feature: _Python calls them automatically depending on the operation we run._
For example, all Python objects are printable. We can print them to the screen using the `print()` function. Calling `print()` internally falls back to calling the target object's `__str__()` special method:
python ```
>>> label = Label("Python!")
>>> print(label)
<__main__.Label object at 0x10354efd0>

```

In this example, we've printed our `label` object. This action provides some information about the object and the memory address where it lives. However, the actual output is not very useful from the user's perspective.
Fortunately, we can improve this by providing our `Label` class with an appropriate `__str__()` method:
python ```
class Label:
  def __init__(self, text):
    self.text = text
  @property
  def text(self):
    return self._text
  @text.setter
  def text(self, value):
    self._text = str(value)
  def __str__(self):
    return self.text

```

The `__str__()` method must return a user-friendly string representation for our objects. In this case, when we print an instance of `Label` to the screen, the label's text will be displayed:
python ```
>>> label = Label("Python!")
>>> print(label)
Python!

```

As you can see, Python takes care of calling `__str__()` automatically when we use the `print()` function to display our instances of `Label`.
Another special method that belongs to Python's class mechanism is `__repr__()`. This method returns a developer-friendly string representation of a given object. Here, developer-friendly implies that the representation should allow a developer to recreate the object itself.
python ```
class Label:
  def __init__(self, text):
    self.text = text
  @property
  def text(self):
    return self._text
  @text.setter
  def text(self, value):
    self._text = str(value)
  def __str__(self):
    return self.text
  def __repr__(self):
    return f"{type(self).__name__}(text='{self.text}')"

```

The `__repr__()` method returns a string representation of the current objects. This string differs from what `__str__()` returns:
python ```
>>> label = Label("Python!")
>>> label
Label(text='Python!')

```

Now when you access the instance on your REPL session, you get a string representation of the current object. You can copy and paste this representation to recreate the object in an appropriate environment.
## Reusing Code With Inheritance
Inheritance is an advanced topic in object-oriented programming. It allows you to create hierarchies of classes where each subclass inherits all the attributes and behaviors from its parent class or classes. Arguably, **code reuse** is the primary use case of inheritance.
Yes, we code a base class with a given functionality and make that functionality available to its subclass through inheritance. This way, we implement the functionality only once and reuse it in every subclass.
Python classes support **single** and **multiple** inheritance. For example, let's say we need to create a button class. This class needs `.width` and `.height` attributes that define its rectangular shape. The class also needs a label for displaying some informative text.
We can code this class from scratch, or we can use inheritance and reuse the code of our current `Label` class. Here's how to do this:
python ```
class Button(Label):
  def __init__(self, text, width, height):
    super().__init__(text)
    self.width = width
    self.height = height
  def __repr__(self):
    return (
      f"{type(self).__name__}"
      f"(text='{self.text}', "
      f"width={self.width}, "
      f"height={self.height})"
    )

```

To inherit from a parent class in Python, we need to list the parent class or classes in the subclass definition. To do this, we use a pair of parentheses and a comma-separated list of parent classes. If we use several parent classes, then we're using multiple inheritance, which can be challenging to reason about.
The first line in `__init__()` calls the `__init__()` method on the parent class to properly initialize its `.text` attribute. To do this, we use the built-in `super()` function. Then we define the `.width` and `.height` attributes, which are specific to our `Button` class. Finally, we provide a custom implementation of `__repr__()`.
Here's how our `Button` class works:
python ```
>>> button = Button("Ok", 10, 5)
>>> button.text
'Ok'
>>> button.text = "Click Me!"
>>> button.text
'Click Me!'
>>> button.width
10
>>> button.height
5
>>> button
Button(text='Ok', width=10, height=5)
>>> print(button)
Click Me!

```

As you can conclude from this code, `Button` has inherited the `.text` attribute from `Label`. This attribute is completely functional. Our class has also inherited the `__str__()` method from `Label`. That's why we get the button's text when we print the instance.
## Using Classes in PyQt GUI Apps
Everything we've learned so far about Python classes is the basis of our future work in GUI development. When it comes to working with PyQt, PySide, Tkinter, or any other GUI framework, we'll heavily rely on our knowledge of classes and OOP because most of them are based on classes and class hierarchies.
We'll now look at how to use inheritance to create some GUI-related classes. For example, when we create an application with PyQt or PySide, we usually have a main window. To create this window, we typically inherit from `QMainWindow`:
  * PyQt6
  * PySide6


python ```
from PyQt6.QtWidgets import QMainWindow
class Window(QMainWindow):
  def __init__(self):
    super().__init__()

```

python ```
from PySide6.QtWidgets import QMainWindow
class Window(QMainWindow):
  def __init__(self):
    super().__init__()

```

In the definition of our `Window` class, we use the `QMainWindow` class as the parent class. This tells Python that we want to define a class that inherits all the functionalities that `QMainWindow` provides.
We can continue adding attributes and methods to our `Window` class. Some of these attributes can be GUI widgets, such as labels, buttons, comboboxes, checkboxes, line edits, and many others. In PyQt, we can create all these GUI components using classes such as `QLabel`, [`QPushButton`](https://www.pythonguis.com/docs/qpushbutton/), [`QComboBox`](https://www.pythonguis.com/docs/qcombobox/), [`QCheckBox`](https://www.pythonguis.com/docs/qcheckbox/), and `QLineEdit`.
All of them have their own sets of attributes and methods that we can use according to our specific needs when designing the GUI of a given application.
## Wrapping Up Classes-Related Concepts
As we've seen, Python allows us to write classes that work as templates that you can use to create concrete objects that bundle together data and behavior. The building blocks of Python classes are:
  * **Attributes** , which hold the data in a class
  * **Methods** , which provide the behaviors of a class


The attributes of a class define the class's data, while the methods provide the class's behaviors, which typically act on that data.
To better understand OOP and classes in Python, we should first discuss some terms that are commonly used in this aspect of Python development:
  * **Classes** are blueprints or templates for creating objects -- just like a blueprint for creating a car, plane, house, or anything else. In programming, this blueprint will define the data (attributes) and behavior (methods) of the object and will allow us to create multiple objects of the same kind.
  * **Objects** or **Instances** are the realizations of a class. We can create objects from the blueprint provided by the class. For example, you can create John's car from a `Car` class.
  * **Methods** are functions defined within a class. They provide the behavior of an object of that class. For example, our `Car` class can have methods to start the engine, turn right and left, stop, and so on.
  * **Attributes** are properties of an object or class. We can think of attributes as variables defined in a class or object. Therefore, we can have:
    * **class attributes** , which are specific to a concrete class and common to all the instances of that class. You can access them either through the class or an object of that class. For example, if we're dealing with a single car manufacturer, then our `Car` class can have a manufacturer attribute that identifies it.
    * **instance attributes** , which are specific to a concrete instance. You can access them through the specific instance. For example, our `Car` class can have attributes to store properties such as the maximum speed, the number of passengers, the car's weight, and so on.
  * **Instantiation** is the process of creating an individual _instance_ from a class. For example, we can create John's car, Jane's car, and Linda's car from our `Car` class through instantiation. In Python, this process runs through two steps:
    1. **Instance creation** : Creates a new object and allocates memory for storing it.
    2. **Instance initialization** : Initializes all the attributes of the current object with appropriate values.
  * **Inheritance** is a mechanism of code reuse that allows us to inherit attributes and methods from one or multiple existing classes. In this context, we'll hear terms like:
    * **Parent class** : The class we're inheriting from. This class is also known as the **superclass** or **base class**. If we have one parent class, then we're using **single inheritance**. If we have more than one parent class, then we're using **multiple inheritance**.
    * **Child class** : The class that inherits from a given parent. This class is also known as the **subclass**.


Don't feel frustrated or bad if you don't understand all these terms immediately. They'll become more familiar with use as you use them in your own Python code. Many of our GUI tutorials make use of some or all of these concepts.
## Conclusion
Now you know the basics of Python classes. You also learned fundamental concepts of object-oriented programming, such as inheritance. You also learned that most GUI frameworks are heavily based on classes. Therefore knowing about classes will open the door to begin building your own GUI app using PyQt, PySide, Tkinter, or any other GUI framework for Python.
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Leo Well](https://www.pythonguis.com/static/theme/images/authors/leo-well.jpg)](https://www.pythonguis.com/authors/leo-well/)
**Working With Classes in Python and PyQt** was written by [Leo Well](https://www.pythonguis.com/authors/leo-well/) with contributions from [Boštjan Mejak](https://www.pythonguis.com/authors/bostjan-mejak/) . 
**Working With Classes in Python and PyQt** was published in [tutorials](https://www.pythonguis.com/tutorials/) on March 06, 2023 (updated October 18, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[python](https://www.pythonguis.com/topics/python/) [classes](https://www.pythonguis.com/topics/classes/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [tkinter](https://www.pythonguis.com/topics/tkinter/) [qt](https://www.pythonguis.com/topics/qt/) [qt6](https://www.pythonguis.com/topics/qt6/) [tk](https://www.pythonguis.com/topics/tk/)
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
