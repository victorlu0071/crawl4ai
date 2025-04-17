# Content from: https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/

[](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/#menu)
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
# Use Tkinter to Design GUI Layouts
Create GUI layouts using the Frame widget, Tkinter, and Python
by [Joshua Willman](https://www.pythonguis.com/authors/joshua-willman/) Last updated Dec 30 Tkinter [ Getting started with Tkinter ](https://www.pythonguis.com/tkinter-tutorial/#tkinter-getting-started)
#### [ Tkinter Tutorial ](https://www.pythonguis.com/tkinter-tutorial/) — [Getting started with Tkinter](https://www.pythonguis.com/tkinter-tutorial/#tkinter-getting-started)
  * [Create a GUI Using Tkinter and Python](https://www.pythonguis.com/tutorials/create-gui-tkinter/)
  * [Use Tkinter to Design GUI Layouts](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/)
  * [Create Buttons in Tkinter](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/)
  * [Using the Pack Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/)
  * [Using the Grid Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/)
  * [Using the Place Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-place-layout-manager/)
  * [Create Radiobuttons and Checkbuttons in Tkinter](https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/)


When creating a GUI app, the layout or arrangement of widgets is important. Laying out an app involves determining a good disposition for widgets on a window to build an intuitive and user-friendly GUI. In this tutorial, you will learn how to create a well-structured layout using Tkinter's `Frame` widget in Python.
Table of Contents
  * [Planning an App's GUI Layout](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/#planning-an-apps-gui-layout)
  * [Getting to Know the Frame Widget](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/#getting-to-know-the-frame-widget)
  * [Creating Nested Frames](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/#creating-nested-frames)
  * [Create a GUI Layout With Frame](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/#create-a-gui-layout-with-frame)
  * [Summary](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/#summary)


## Planning an App's GUI Layout
When you start a new GUI project with Tkinter, the best thing you can do is have a good plan for organizing the graphical components on the app's windows. In this tutorial, you'll create a Tkinter app for managing images. To lay out its GUI, you will use the `Frame` widget and the [`grid`](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/) geometry manager.
Below, you have a diagram that sketches the GUI layout:
![Planned GUI design sketch for the image editor](https://www.pythonguis.com/static/tutorials/tkinter/use-tkinter-to-design-gui-layout/GUI_Layout.png) _Planned GUI design sketch for the image editor_
The large area on the right will display the target image. On the upper-left side of the GUI, a small label will let you keep track of what the original image looked like for reference. Underneath that, you have some basic options for editing the image.
## Getting to Know the `Frame` Widget
Tkinter's `Frame` widget allows you to organize the GUI quickly. Frames are like boxes or mini-windows within the parent window. To arrange a frame in a Tkinter window, you can use any of the available geometry managers, `pack`, `grid`, or `place`, depending on your needs.
Here's a quick example where you place a frame on a window with a blue background so that you can distinguish the frame:
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
python ```
import tkinter as tk
root = tk.Tk()
root.title("Frame Demo")
root.config(bg="skyblue")
# Create Frame widget
frame = tk.Frame(root, width=200, height=200)
frame.pack(padx=10, pady=10)
root.mainloop()

```

Here, we import `tkinter` as `tk` and set up the `root` window. Then, we create an instance of `Frame`. To do this, we specify the `width` and `height` to `200` pixels. The `root` window has a sky-blue background, which allows you to see the new frame in white. You can also change the color of the `Frame` widget to whatever color you need.
Next, we place `frame` in the main window using the `pack` geometry manager with a padding of `10` pixels in both directions, `x` and `y`.
Go ahead and run this demo app. You'll get a window that looks something like the following:
![A Tkinter window with a blue background and a frame in white](https://www.pythonguis.com/static/tutorials/tkinter/use-tkinter-to-design-gui-layout/frame-demo-tkinter.png) _A Tkinter window with a blue background and a frame in white_
That's it! You have created and added an empty frame to a Tkinter app using the `pack` geometry manager.
## Creating Nested Frames
Now, let's take a quick look at adding a frame within another frame:
python ```
import tkinter as tk
root = tk.Tk()
root.title("Nested Frames")
root.config(bg="skyblue")
frame = tk.Frame(root, width=200, height=200)
frame.pack(padx=10, pady=10)
nested_frame = tk.Frame(frame, width=190, height=190, bg="red")
nested_frame.pack(padx=10, pady=10)
root.mainloop()

```

![A Tkinter frame nested within another frame](https://www.pythonguis.com/static/tutorials/tkinter/use-tkinter-to-design-gui-layout/nested-frames-tkinter.png) _A Tkinter frame nested within another frame_
To nest a frame within another frame, you need to set the outer frame as the parent or master widget of the inner frame. In this example, you set the inner frame background color to red so that you can differentiate it from the outer frame in white.
## Create a GUI Layout With `Frame`
In this section, we'll use the `Frame` class to create a more elaborate GUI layout. We'll create a GUI for a basic image editor app. The app's GUI will look something like this: 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
![An Image Editor with a GUI layout based on Tkinter frames](https://www.pythonguis.com/static/tutorials/tkinter/use-tkinter-to-design-gui-layout/image-editor-gui-layout-tkinter.png) _An Image Editor with a GUI layout based on Tkinter frames_
Here's the code that implements this layout using `Frame` in Tkinter:
python ```
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Image Editor")
image = tk.PhotoImage(file="forest.png")
# Tools frame
tools_frame = tk.Frame(root, width=200, height=400, bg="skyblue")
tools_frame.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.Y)
tk.Label(
  tools_frame,
  text="Original Image",
  bg="skyblue",
).pack(padx=5, pady=5)
thumbnail_image = image.subsample(5, 5)
tk.Label(tools_frame, image=thumbnail_image).pack(padx=5, pady=5)
# Tools and Filters tabs
notebook = ttk.Notebook(tools_frame)
notebook.pack(expand=True, fill="both")
tools_tab = tk.Frame(notebook, bg="lightblue")
tools_var = tk.StringVar(value="None")
for tool in ["Resizing", "Rotating"]:
  tk.Radiobutton(
    tools_tab,
    text=tool,
    variable=tools_var,
    value=tool,
    bg="lightblue",
  ).pack(anchor="w", padx=20, pady=5)
filters_tab = tk.Frame(notebook, bg="lightgreen")
filters_var = tk.StringVar(value="None")
for filter in ["Blurring", "Sharpening"]:
  tk.Radiobutton(
    filters_tab,
    text=filter,
    variable=filters_var,
    value=filter,
    bg="lightgreen",
  ).pack(anchor="w", padx=20, pady=5)
notebook.add(tools_tab, text="Tools")
notebook.add(filters_tab, text="Filters")
# Image frame
image_frame = tk.Frame(root, width=400, height=400, bg="grey")
image_frame.pack(padx=5, pady=5, side=tk.RIGHT)
display_image = image.subsample(2, 2)
tk.Label(
  image_frame,
  text="Edited Image",
  bg="grey",
  fg="white",
).pack(padx=5, pady=5)
tk.Label(image_frame, image=display_image).pack(padx=5, pady=5)
root.mainloop()

```

In this example, we create a GUI for a basic image editor using Tkinter. The code leverages the `Frame` widget to lay out the GUI into two main sections. The `tools_frame` section holds the image editing tools and filters. The `image_frame` section displays the edited image.
The `tools_frame` frame on the left side of the window (`side=tk.LEFT`) serves as a vertical container for tools and filters. It includes a label to display the original image and a `Notebook` widget for tabbed options. Inside the notebook, you use two additional `Frame` widgets, `tools_tab`, and `filters_tab`, to group related radio buttons. The tools tab contains options like `"Resizing"` and `"Rotating"`, while the filters tab includes `"Blurring"` and `"Sharpening"`.
The `image_frame` frame on the right (`side=tk.RIGHT`) displays the edited image. It contains a label for a generic title and another label for the target image.
By placing this frame adjacent to the `tools_frame` frame, the layout visually separates the workspace into two areas: one for interacting with tools and filters and the other for viewing the image.
## Summary
We've learned that using the `Frame` widget is a great way to define a functional layout for a GUI app. When creating the layout, we should decide which geometry manager to use. In Tkinter, we have the `pack`, `grid`, or `place` geometry managers. You can also combine them according to your needs.
The `Frame` widget acts as a container that lets us group related widgets together and provide control over their arrangement. It's a great tool for creating well-organized GUIs in Tkinter.
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
Continue with [ Tkinter Tutorial ](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/ "Continue to next part")
Return to [Create Desktop GUI Applications with Tkinter ](https://www.pythonguis.com/tkinter-tutorial/)
[![Joshua Willman](https://www.pythonguis.com/static/theme/images/authors/joshua-willman.jpg)](https://www.pythonguis.com/authors/joshua-willman/)
**Use Tkinter to Design GUI Layouts** was written by [Joshua Willman](https://www.pythonguis.com/authors/joshua-willman/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) . 
**Use Tkinter to Design GUI Layouts** was published in [tutorials](https://www.pythonguis.com/tutorials/) on July 02, 2022 (updated December 30, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[python](https://www.pythonguis.com/topics/python/) [tkinter](https://www.pythonguis.com/topics/tkinter/) [gui](https://www.pythonguis.com/topics/gui/) [tk](https://www.pythonguis.com/topics/tk/) [layout](https://www.pythonguis.com/topics/layout/) [ foundation](https://www.pythonguis.com/topics/foundation/) [ tkinter-foundation](https://www.pythonguis.com/topics/tkinter-foundation/)
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
