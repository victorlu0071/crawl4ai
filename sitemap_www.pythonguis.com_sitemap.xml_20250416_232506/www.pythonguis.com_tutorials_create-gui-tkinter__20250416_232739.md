# Content from: https://www.pythonguis.com/tutorials/create-gui-tkinter/

[](https://www.pythonguis.com/tutorials/create-gui-tkinter/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [Tkinter ](https://www.pythonguis.com/tkinter/)
  * [Tkinter Tutorial ](https://www.pythonguis.com/tkinter-tutorial/)
  * Basics
  * [First Tkinter GUI](https://www.pythonguis.com/tutorials/create-gui-tkinter/)
  * [Design Tkinter Layout](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/)
  * [Buttons in Tkinter](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/)
  * [Pack Layouts](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/)
  * [Grid Layouts](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/)
  * [Place Layouts](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-place-layout-manager/)
  * [Radio & Check Buttons](https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-tkinter-applications-windows-pyinstaller/)
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
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Create a GUI Using Tkinter and Python
Creating your first desktop application
by [Joshua Willman](https://www.pythonguis.com/authors/joshua-willman/) Last updated Jan 10 Tkinter [ Getting started with Tkinter ](https://www.pythonguis.com/tkinter-tutorial/#tkinter-getting-started)
#### [ Tkinter Tutorial ](https://www.pythonguis.com/tkinter-tutorial/) — [Getting started with Tkinter](https://www.pythonguis.com/tkinter-tutorial/#tkinter-getting-started)
  * [Create a GUI Using Tkinter and Python](https://www.pythonguis.com/tutorials/create-gui-tkinter/)
  * [Use Tkinter to Design GUI Layouts](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/)
  * [Create Buttons in Tkinter](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/)
  * [Using the Pack Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/)
  * [Using the Grid Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/)
  * [Using the Place Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-place-layout-manager/)
  * [Create Radiobuttons and Checkbuttons in Tkinter](https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/)


You look at windows every day on your computer but have you wondered how you could make your own? In this tutorial, we'll get started making our own window, or graphical user interface (GUI), using Tkinter and Python.
A rough idea of what a GUI could look like:
![Example Desktop GU](https://www.pythonguis.com/static/tutorials/tkinter/create-gui-tkinter/example-desktop-gui.png) _Example Desktop GUI_
Table of Contents
  * [What Is a GUI?](https://www.pythonguis.com/tutorials/create-gui-tkinter/#what-is-a-gui)
  * [What Is Tkinter?](https://www.pythonguis.com/tutorials/create-gui-tkinter/#what-is-tkinter)
  * [How Can We Create a Window?](https://www.pythonguis.com/tutorials/create-gui-tkinter/#how-can-we-create-a-window)
  * [How Can We Display Text in a Label?](https://www.pythonguis.com/tutorials/create-gui-tkinter/#how-can-we-display-text-in-a-label)
  * [Summary](https://www.pythonguis.com/tutorials/create-gui-tkinter/#summary)


## What Is a GUI?
The most common way to interact with computers is using a graphical user interface (GUI). These rectangular windows with buttons, icons and menus are an intuitive way to get things done. 
In this tutorial, we'll focus on building our own GUIs using Python and Tkinter. We'll begin by reviewing some of the basics, including creating a window and learning how to display images and text. With this knowledge, you can develop ideas for creating basic GUI applications.
## What Is Tkinter?
Tkinter is Python's default GUI package and included in the standard library. It is an object-orientated layer on top of the open-source [Tcl/Tk](https://www.tcl.tk/) widget toolkit. You don't need to understand Tcl/Tk to use it.
While there are more feature-complete GUI frameworks available (such as Qt) Tkinter remains popular for small and beginner projects, because it's simple and readily available. If you just want to try out GUI programming it's a fine place to start.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
## How Can We Create a Window?
Let's start with the basics: creating a window with Tkinter. First create a new file called `app.py` and then add the following code:
python ```
import tkinter as tk
root = tk.Tk()
root.mainloop()

```

The first line imports the `tkinter` package using the short name `tk` to save typing later. First, we create the `root` widget object by calling `tk.Tk()`. The `root` widget is the app's main window or parent window. It must be created before any other windows, and there can only be one root. 
The last line runs the app's main _event loop_. This handles mouse and keyboard inputs and communicates with the OS. That's it! 
Run this script, using `python` just like any other script.
bash ```
python app.py

```

You'll get a window like the following on your screen:
![A small, blank empty window](https://www.pythonguis.com/static/tutorials/tkinter/create-gui-tkinter/small-blank-empty-window.png) _A small, blank empty window_
We have our first window on the desktop. Next, let's look at some adjustments we can make like adding a title, changing the background color, and setting the window's size:
python ```
import tkinter as tk
root = tk.Tk()
# Setting some window properties
root.title("Tk Example")
root.configure(background="yellow")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("300x300+50+50")
root.mainloop()

```

Here, we changed the window's title to `"Tk Example"`. We also changed the background color to `"yellow"` using the `configure()` method. Then, we adjusted the window's size. We set the minimum size and maximum size for the window. 
Finally, let's talk about `geometry()`. This method allows us to define the window's geometry – Tkinter's terminology for size and shape – when we first run the program. This method take a string consisting of the window's width and height plus the `x`, and `y` coordinates on the screen. If the `x` and `y` coordinates aren't provided, then the window will show up in the top-left corner of the screen.
## How Can We Display Text in a Label?
In Tkinter **widget** is the name given to a component of the UI that the user can interact with. User interfaces are made up of multiple widgets, arranged within a window. Labels are one of the most basic widgets. You can use them to display either text or images.
Let's update our example to add a label to our window. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
python ```
import tkinter as tk
root = tk.Tk()
root.title("Tk Example")
root.minsize(200, 200)
root.geometry("300x300+50+50")
# Create two labels
tk.Label(root, text="Nothing will work unless you do.").pack()
tk.Label(root, text="- Maya Angelou").pack()
root.mainloop()

```

The first few lines are familiar by now, setting the window title, size and geometry. But we now create two `Label` widgets to display text. The first argument is our `root` window, followed by the text that we want to display.
By passing in `root` we tell Tkinter that these labels belong in the main window – the main window is their _parent_. Notice that after creating the label, we call `.pack()` on it. The `pack()` method is a geometry manager used to pack or place the widget on the current window. If we adjust the window size, the label will stay in the top-center part of the window.
This could also be written as follows, if you prefer – assigning the label object to a variable `label1` and then calling `.pack()` on that.
python ```
label1 = tk.Label(root, text="Nothing will work unless you do.")
label1.pack()

```

You can also use labels to display images. You'll have a couple of ways to load images in Tkinter. For this example, we'll use the `PhotoImage` class:
python ```
import tkinter as tk
root = tk.Tk()
root.title("Tk Example")
root.minsize(200, 200)
root.geometry("300x300+50+50")
# Create two labels
tk.Label(root, text="Nothing will work unless you do.").pack()
tk.Label(root, text="- Maya Angelou").pack()
# Display an image
image = tk.PhotoImage(file="025.gif")
tk.Label(root, image=image).pack()
root.mainloop()

```

Here, we use `PhotoImage` class to load the image file we want to use. You can pass your own image file to `PhotoImage`.
Then, we instantiate the `Label` class with the `image` argument holding the path to the image we want to display. The `PhotoImage` class can load GIF, PGM, PPM, and PNG image formats. For other image formats you can use the [Pillow](https://python-pillow.org/) library.
Here's how your window will look now:
![Window complete with text and an image.](https://www.pythonguis.com/static/tutorials/tkinter/create-gui-tkinter/window-with-text-and-image.png) _Window with a text and an image._
## Summary
In this tutorial, you learned how to create a window and add text and images using the `Label` widget in Tkinter.
It is important to apply what you learn. Take some time to experiment with the window's geometry or the images and text that can be displayed on labels.
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
Continue with [ Tkinter Tutorial ](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/ "Continue to next part")
Return to [Create Desktop GUI Applications with Tkinter ](https://www.pythonguis.com/tkinter-tutorial/)
[![Joshua Willman](https://www.pythonguis.com/static/theme/images/authors/joshua-willman.jpg)](https://www.pythonguis.com/authors/joshua-willman/)
**Create a GUI Using Tkinter and Python** was written by [Joshua Willman](https://www.pythonguis.com/authors/joshua-willman/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) and [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
**Create a GUI Using Tkinter and Python** was published in [tutorials](https://www.pythonguis.com/tutorials/) on June 14, 2022 (updated January 10, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[python](https://www.pythonguis.com/topics/python/) [tkinter](https://www.pythonguis.com/topics/tkinter/) [gui](https://www.pythonguis.com/topics/gui/) [tk](https://www.pythonguis.com/topics/tk/) [ getting-started](https://www.pythonguis.com/topics/getting-started/) [ tkinter-getting-started](https://www.pythonguis.com/topics/tkinter-getting-started/)
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
