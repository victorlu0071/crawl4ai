# Content from: https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/

[](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/#menu)
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
# Using the Pack Geometry Manager in Tkinter
Laying out widgets with the Pack geometry manager
by [Joshua Willman](https://www.pythonguis.com/authors/joshua-willman/) Last updated Jan 12 Tkinter [ Getting started with Tkinter ](https://www.pythonguis.com/tkinter-tutorial/#tkinter-getting-started)
#### [ Tkinter Tutorial ](https://www.pythonguis.com/tkinter-tutorial/) — [Getting started with Tkinter](https://www.pythonguis.com/tkinter-tutorial/#tkinter-getting-started)
  * [Create a GUI Using Tkinter and Python](https://www.pythonguis.com/tutorials/create-gui-tkinter/)
  * [Use Tkinter to Design GUI Layouts](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/)
  * [Create Buttons in Tkinter](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/)
  * [Using the Pack Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/)
  * [Using the Grid Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/)
  * [Using the Place Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-place-layout-manager/)
  * [Create Radiobuttons and Checkbuttons in Tkinter](https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/)


When we create graphical user interfaces (GUIs), we need a way to arrange widgets on the window. Placing widgets on a window using their relative position can be cumbersome and hard to achieve correctly. We'd need to compute each widget's position relative to other widgets to build the GUI. Unfortunately, the position will have to be calculated again every time we resize the window.
In Tkinter, we can gracefully solve this issue using a **geometry manager**. Tkinter has some useful geometry managers, including `pack`, `place`, and `grid`. Each of them lets us arrange widgets in a different way.
To find out more about the differences between the three methods, please check out the [When To Use Pack, Place Or Grid In Tkinter](https://www.pythonguis.com/faq/pack-place-and-grid-in-tkinter/) tutorial.
In this tutorial, we'll learn the basics about using the `pack` geometry manager to create functional GUIs in Tkinter.
Table of Contents
  * [The pack Geometry Manager](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/#the-pack-geometry-manager)
  * [A Demo GUI With pack](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/#a-demo-gui-with-pack)
  * [A Sing-in Form With pack](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/#a-sing-in-form-with-pack)
  * [Summary](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/#summary)


## The `pack` Geometry Manager
The `pack` geometry manager turns each individual widget into a rectangular area known as a **parcel**. Each widget has its own size, and `pack` lets you arrange them all together either vertically or horizontally.
Each widget has its own size, which you can change to better suit your needs. Once you determine the desired size of a widget, the `pack` manager arranges it in the window.
The `pack` geometry manager stacks widgets on top of each other vertically by default. You can also achieve a horizontal layout by changing the `side` parameter to `"left"`, `"right"`, or the equivalent constants `tkinter.LEFT` and `tkinter.RIGHT`. You can also change a widget's height, width, and location.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
Some of the `pack` manager's more useful arguments are listed below:
  * `side`: specifies the general location of the widget in the window. Its possible values are `"right"`.
  * `fill`: defines which directions you want the widget to fill in the parent window. It can be wither the `"x"` or `"y"` directions or `"both"`. 
  * `padx`, `pady`: represent the number of pixels surrounding the widget as padding.
  * `ipadx`, `ipady`: defines the horizontal or vertical padding inside the widget.
  * `expand`: if set to `True`, the widget stretches when the parent window expands.
  * `anchor`: defines where the widget is placed in the parent widget. It can be `"n"` (North), `"s"` (South), `"e"` (East), `"w"` (West), or some combination of them. The default is `"center"`.


## A Demo GUI With `pack`
The `pack` geometry manager is useful for different types of GUIs. Below is a quick example of how to create a GUI and arrange widgets in the window with `pack`:
python ```
import tkinter as tk
root = tk.Tk()
root.title("The Pack Geometry Manager")
root.geometry("340x100")
tk.Button(root, text="Top Button!").pack()
tk.Label(root, text="Hello, Left!").pack(side="left")
tk.Label(root, text="Hello, Right!").pack(side="right")
tk.Checkbutton(
  root,
  text="An option at the bottom!",
).pack(side=tk.BOTTOM)
root.mainloop()

```

In this example, we first import `tkinter` as `tk`. Then, we build an app with a main window with a title and fixed size `(340x100)`.
Next, we use the pack geometry manager to arrange widgets in specified positions. A button with the text `"Top Button!"` appears at the top by default, followed by two labels: `"Hello, Left!"` aligned to the left and `"Hello, Right!"` aligned to the right.
At the bottom of the window, we have a check button labeled `"An option at the bottom!"` placed using `side=tk.BOTTOM`. The program runs with `mainloop()` and looks like shown below:
![Demo GUI using the grid geometry manager in Tkinter](https://www.pythonguis.com/static/tutorials/tkinter/create-ui-with-tkinter-pack-layout-manager/pack-geometry-manager-tkinter.png) __Demo GUI using the grid geometry manager in Tkinter_._
## A Sing-in Form With `pack`
Now it's time for a more realistic example. Say that you need to create a login dialog. The dialog's GUI should look something like the following:
![Login form with Tkinter's pack geometry manager](https://www.pythonguis.com/static/tutorials/tkinter/create-ui-with-tkinter-pack-layout-manager/sign-in-form-pack-tkinter.png) _Login form with Tkinter's pack geometry manager_
Now let's get to code for the login UI: 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
python ```
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Sign in")
root.resizable(False, False)
tk.Label(
  root,
  text="Sign in to Tkinter",
  font=("Font", 30),
).pack(ipady=5, fill="x")
image = tk.PhotoImage(file="profile.png").subsample(5, 5)
tk.Label(
  root,
  image=image,
  relief=tk.RAISED,
).pack(pady=5)
def check_input():
  secret_username = "username"
  secret_password = "password"
  username = username_entry.get()
  password = password_entry.get()
  if username == secret_username and password == secret_password:
    messagebox.showinfo("Info", "Used logged in!")
  else:
    messagebox.showerror("Error", "Invalid username or password")
# Username and password
tk.Label(root, text="Your username").pack(anchor="w", padx=30)
username_entry = tk.Entry(root)
username_entry.pack()
tk.Label(root, text="Password").pack(anchor="w", padx=30)
password_entry = tk.Entry(root)
password_entry.pack()
# Sign in button
tk.Button(
  root,
  text="Sign in",
  command=check_input,
  width=18,
).pack(pady=10, padx=30, fill="x")
# Remember me and forgot password
tk.Checkbutton(
  root,
  text="Remember me",
  command=lambda: print("The check button works."),
).pack(side="left", padx=20, pady=5)
tk.Label(
  root,
  text="Forgot password?",
  fg="blue",
  cursor="hand2",
).pack(side="right", padx=20, pady=5)
root.mainloop()

```

In this example, you create a graphical user interface for a sign-in form. The `pack` geometry manager is used to organize widgets. It arranges widgets in the window relative to their order of creation. 
In the first `Label` widget, the `pack` method uses the `ipady` and `fill` arguments to add vertical internal padding and stretch the widget horizontally (`fill="x"`). Similarly, a second `Label` widget displays a profile picture, where `pady=5` adds vertical spacing around it.
For the username and password fields, `pack` arranges labels and entry widgets in a straightforward vertical stack. Each label is aligned to the left with `anchor="w"` and `padx=30`, which adds horizontal padding from the left edge of the window. The corresponding `Entry` widgets are packed directly below their labels without additional arguments.
The _Sign in_ button is packed with `pady=10` and `padx=30` to add spacing, while `fill="x"` ensures it stretches horizontally to match the window's width.
The bottom section contains a `Checkbutton` (`"Remember me"`) and a `Label` (`"Forgot password?"`). The `pack` geometry manager uses `side="left"` and `side="right"` to position these widgets on opposite sides of the window horizontally.
The overall layout relies on the sequential and relative placement of widgets through the `pack` geometry manager, resulting in a clean, well-organized sign-in interface.
## Summary
In this tutorial, we learned how to use the `pack` geometry manager to arrange widgets in Tkinter-based GUIs.
First, we looked at a few arguments to `pack()` that can help us manipulate the geometry or layout of our GUIs. Then, we built a generic GUI to help us practice the concepts of geometry management with `pack` in Tkinter.
Finally, we created a sign-in form using the `pack` geometry manager for arranging widgets and building the GUI. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Mark As Complete 
Continue with [ Tkinter Tutorial ](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/ "Continue to next part")
Return to [Create Desktop GUI Applications with Tkinter ](https://www.pythonguis.com/tkinter-tutorial/)
[![Joshua Willman](https://www.pythonguis.com/static/theme/images/authors/joshua-willman.jpg)](https://www.pythonguis.com/authors/joshua-willman/)
**Using the Pack Geometry Manager in Tkinter** was written by [Joshua Willman](https://www.pythonguis.com/authors/joshua-willman/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
**Using the Pack Geometry Manager in Tkinter** was published in [tutorials](https://www.pythonguis.com/tutorials/) on September 28, 2022 (updated January 12, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[python](https://www.pythonguis.com/topics/python/) [tkinter](https://www.pythonguis.com/topics/tkinter/) [gui](https://www.pythonguis.com/topics/gui/) [tk](https://www.pythonguis.com/topics/tk/) [layout](https://www.pythonguis.com/topics/layout/) [pack](https://www.pythonguis.com/topics/pack/) [geometry-manager](https://www.pythonguis.com/topics/geometry-manager/) [ foundation](https://www.pythonguis.com/topics/foundation/) [ tkinter-foundation](https://www.pythonguis.com/topics/tkinter-foundation/)
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
