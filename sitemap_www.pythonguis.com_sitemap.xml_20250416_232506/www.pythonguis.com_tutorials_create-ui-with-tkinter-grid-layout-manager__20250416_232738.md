# Content from: https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/

[](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/#menu)
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
# Using the Grid Geometry Manager in Tkinter
Laying out widgets with the grid geometry manager
by [Joshua Willman](https://www.pythonguis.com/authors/joshua-willman/) Last updated Nov 15 Tkinter [ Getting started with Tkinter ](https://www.pythonguis.com/tkinter-tutorial/#tkinter-getting-started)
#### [ Tkinter Tutorial ](https://www.pythonguis.com/tkinter-tutorial/) — [Getting started with Tkinter](https://www.pythonguis.com/tkinter-tutorial/#tkinter-getting-started)
  * [Create a GUI Using Tkinter and Python](https://www.pythonguis.com/tutorials/create-gui-tkinter/)
  * [Use Tkinter to Design GUI Layouts](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/)
  * [Create Buttons in Tkinter](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/)
  * [Using the Pack Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/)
  * [Using the Grid Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/)
  * [Using the Place Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-place-layout-manager/)
  * [Create Radiobuttons and Checkbuttons in Tkinter](https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/)


In this tutorial, we are going to take a look at how to arrange widgets with the `grid` geometry manager in Tkinter.
In similar tutorials, we talked about designing GUI layouts with other geometry managers. Check out the following tutorials to learn more:
  * [Create UI with Pack Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/)
  * [When to Use Pack, Place or Grid](https://www.pythonguis.com/faq/pack-place-and-grid-in-tkinter/)


So for this tutorial, we will jump right into more examples of designing GUIs with Tkinter and the `grid` geometry manager.
Table of Contents
  * [The grid Geometry Manager](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/#the-grid-geometry-manager)
  * [A Demo GUI With grid](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/#a-demo-gui-with-grid)
  * [A Profile Form With grid](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/#a-profile-form-with-grid)
  * [Summary](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/#summary)


## The `grid` Geometry Manager
Using the `grid` geometry manager works like a matrix, with rows and columns. The upper left corner cell has a row index of `0` and a column index of `0`. If you move to the right, you'll have cells `(0, 1)`, `(0, 2)`, and so on. If you move down, you'll have cells `(1, 0)`, `(2, 0)`, and so on.
Check out the diagram below for a visual example:
![The grid geometry manager in Tkinter](https://www.pythonguis.com/static/tutorials/tkinter/create-ui-with-tkinter-grid-layout-manager/grid-layout-tkinter.png) _The grid geometry manager in Tkinter_
You can place widgets within cells by specifying their row and column indices. Now, let's examine some of the main arguments that can help you arrange widgets using the `grid` geometry manager:
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
  * `row`, `column`: specify the row and column indices to place a given widget
  * `columnspan`, `rowspan`: specify how many columns or rows a widget will occupy
  * `padx`, `pady`: define the number of pixels for horizontal or vertical padding
  * `ipadx`, `ipady`: specify how many pixels to use for internal padding
  * `sticky`: specifies which side of the cell the widget will _stick_ to.


The `sticky` argument can take the values `S`, `N`, `E`, or `W` for south, north, east, and west. It can also be a combination of them `NW`, `NE`, `SW`, or `SE`. If you use `W+E+N+S`, then the widget will fill the cell. The default behavior is to center the widget within the cell.
## A Demo GUI With `grid`
The following is just a quick example of how to lay out a window using the `grid` geometry manager in Tkinter. In the following GUI, we combine `Button` widgets to showcase some features of `grid`:
![Demo GUI using the grid geometry manager in Tkinter](https://www.pythonguis.com/static/tutorials/tkinter/create-ui-with-tkinter-grid-layout-manager/tkinter-grid-geometry-manager.png) _Demo GUI using the grid geometry manager in Tkinter_
Let's see what the code looks like:
python ```
import tkinter as tk
root = tk.Tk()
root.title("The Grid Geometry Manager")
for row in range(3):
  for col in range(3):
    tk.Button(
      root,
      text=f"Cell ({row}, {col})",
      width=10,
      height=5,
    ).grid(row=row, column=col)
tk.Button(root, text="Span 2 columns", height=5).grid(
  row=3,
  column=0,
  columnspan=2,
  sticky="ew",
)
tk.Button(root, text="Span 2 rows", width=10, height=10).grid(
  row=4,
  column=0,
  rowspan=2,
  sticky="ns",
)
root.mainloop()

```

In this example, we first run loops to create a 3 by 3 grid of buttons. The external loop defines the row indices, while the inner loop defines the column indices.
Next, we create a button that spans two columns and another button that spans two rows. To do this, we use the `columnspan` and `rowspan` arguments respectively.
## A Profile Form With `grid`
Now it's time for a more realistic example. Say that you need to create a dialog to collect personal information from the users registered in a given system. The dialog's GUI should look something like the following:
![A Profile form using the grid geometry manager in Tkinter](https://www.pythonguis.com/static/tutorials/tkinter/create-ui-with-tkinter-grid-layout-manager/profile-form-tkinter-grid.png) _A Profile form using the grid geometry manager in Tkinter_
This GUI uses `Label`, `Entry`, and `Menu` widgets. To arrange the widgets and build the form layout, you'll use the `grid` geometry manager: 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
python ```
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Complete Your Profile")
root.resizable(False, False)
# Profile image
image = tk.PhotoImage(file="profile.png").subsample(6, 6)
tk.Label(
  root,
  image=image,
  relief=tk.RAISED,
).grid(row=0, column=0, rowspan=5, padx=10, pady=10)
# Name field
tk.Label(
  root,
  text="Name:",
).grid(row=0, column=1, padx=5, pady=5, sticky=tk.E)
name = ttk.Entry(root)
name.grid(row=0, column=2, padx=5, pady=5, ipadx=5)
# Gender field
tk.Label(
  root,
  text="Gender:",
).grid(row=1, column=1, padx=5, pady=5, sticky=tk.E)
gender = ttk.Combobox(
  root,
  values=["Male", "Female", "Other"],
  state="readonly",
)
gender.grid(row=1, column=2, padx=5, pady=5)
# Eye color field
tk.Label(
  root,
  text="Eye Color:",
).grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)
eye_color = ttk.Combobox(
  root,
  values=["Brown", "Green", "Blue", "Black", "Other"],
  state="readonly",
)
eye_color.grid(row=2, column=2, padx=5, pady=5)
# Height field
tk.Label(
  root,
  text="Height (cm):",
).grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)
height = ttk.Entry(root)
height.grid(row=3, column=2, padx=5, pady=5, ipadx=5)
# Weight field
tk.Label(
  root,
  text="Weight (kg):",
).grid(row=4, column=1, padx=5, pady=5, sticky=tk.E)
weight = ttk.Entry(root)
weight.grid(row=4, column=2, padx=5, pady=5, ipadx=5)
# Submit button
submit = ttk.Button(
  root,
  text="Submit",
)
submit.grid(row=5, column=2, padx=5, pady=5, sticky=tk.E)
root.mainloop()

```

In this code, we create a basic GUI for a profile form that allows the user to input their name, gender, eye color, height, and weight.
The first widget in this code is a label with a placeholder profile picture. To create the image, we use the `tk.PhotoImage`, which loads the image file named `profile.png`. Then, we position this label in the first row (`row=0`) and first column (`column=0`) of the grid. The label spans `5` rows to accommodate the rest of the form elements on its right side.
Next, we create a label with the text `"Name:"` in the first row and second column, aligning it to the right by setting `sticky` to `tk.E`. The `name` entry provides an input field for the user's name. We place the `name` entry field in the first row, third column of the grid.
Then, in the second row, we have a label for `"Gender"`. To the right of this label, we have a combo box, which provides a dropdown list of gender options. The grid geometry manager positions the gender dropdown in the second row and third column.
We create similar combinations of widgets for the Eye Color, Height, and Weight fields. We use the `grid` geometry manager to position each widget in the correct cell.
Finally, we add a _Submit_ button, which we place in the sixth row, third column, aligning it to the right with `sticky=tk.E`.
## Summary
In this tutorial, we learned how to use the `grid` geometry manager to arrange widgets in Tkinter-based GUIs.
First, we looked at a few arguments to `grid()` that can help us manipulate the geometry or layout of our GUIs. Then, we built a generic GUI to help us practice the concepts of geometry management with `grid` in Tkinter.
Finally, we create a more realistic form using the `grid` geometry manager for arranging widgets and building the GUI. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
Continue with [ Tkinter Tutorial ](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-place-layout-manager/ "Continue to next part")
Return to [Create Desktop GUI Applications with Tkinter ](https://www.pythonguis.com/tkinter-tutorial/)
[![Joshua Willman](https://www.pythonguis.com/static/theme/images/authors/joshua-willman.jpg)](https://www.pythonguis.com/authors/joshua-willman/)
**Using the Grid Geometry Manager in Tkinter** was written by [Joshua Willman](https://www.pythonguis.com/authors/joshua-willman/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
**Using the Grid Geometry Manager in Tkinter** was published in [tutorials](https://www.pythonguis.com/tutorials/) on October 09, 2022 (updated November 15, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[python](https://www.pythonguis.com/topics/python/) [tkinter](https://www.pythonguis.com/topics/tkinter/) [gui](https://www.pythonguis.com/topics/gui/) [tk](https://www.pythonguis.com/topics/tk/) [layout](https://www.pythonguis.com/topics/layout/) [grid](https://www.pythonguis.com/topics/grid/) [geometry-manager](https://www.pythonguis.com/topics/geometry-manager/) [ foundation](https://www.pythonguis.com/topics/foundation/) [ tkinter-foundation](https://www.pythonguis.com/topics/tkinter-foundation/)
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
