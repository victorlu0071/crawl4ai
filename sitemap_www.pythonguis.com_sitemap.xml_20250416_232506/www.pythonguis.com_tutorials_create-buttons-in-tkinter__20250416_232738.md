# Content from: https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/

[](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/#menu)
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
# Create Buttons in Tkinter
Add button widgets to your Tkinter GUI
by [Joshua Willman](https://www.pythonguis.com/authors/joshua-willman/) Last updated Jan 10 Tkinter [ Getting started with Tkinter ](https://www.pythonguis.com/tkinter-tutorial/#tkinter-getting-started)
#### [ Tkinter Tutorial ](https://www.pythonguis.com/tkinter-tutorial/) — [Getting started with Tkinter](https://www.pythonguis.com/tkinter-tutorial/#tkinter-getting-started)
  * [Create a GUI Using Tkinter and Python](https://www.pythonguis.com/tutorials/create-gui-tkinter/)
  * [Use Tkinter to Design GUI Layouts](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/)
  * [Create Buttons in Tkinter](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/)
  * [Using the Pack Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/)
  * [Using the Grid Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/)
  * [Using the Place Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-place-layout-manager/)
  * [Create Radiobuttons and Checkbuttons in Tkinter](https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/)


With physical devices we push buttons to directly perform actions. For example, pushing the _ON_ button on the TV remote turns the TV on. The buttons on the elevator? Press the number for the floor to go to that floor. When we press a button we expect _something_ to happen. In graphical user interfaces buttons are used in the same way. Click the `X` (or red on macOS) button at the top corner of this window, and you will close it.
In this tutorial, we will learn how to make use of buttons in our Tkinter applications using the `Button` widget. By the end of this tutorial, you will be able to include buttons in your Tkinter GUIs, hook these buttons up to Python functions to make things happen and learn how to customize them to fit your projects.
![Push the button](https://www.pythonguis.com/static/tutorials/tkinter/create-buttons-in-tkinter/push-the-button.png) _Let's push that button!_
Table of Contents
  * [Create Button Widgets in Tkinter](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/#create-button-widgets-in-tkinter)
  * [Make Buttons Do Something When Clicked](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/#make-buttons-do-something-when-clicked)
  * [Explore Other Button Parameters](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/#explore-other-button-parameters)
  * [Display an Image on a Button](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/#display-an-image-on-a-button)
  * [Summary](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/#summary)


## Create Button Widgets in Tkinter
Buttons in Tkinter work as expected: you push a button to perform some action. In Tkinter the actions which buttons perform are handled by Python functions or methods. First let\'s build a simple interface which contains some buttons, and then we can start adding the functionality. 
We can use the `Button` class to create a minimalist TV remote with the following code:
python ```
import tkinter as tk
root = tk.Tk() # Create the main window
# Create a TV remote UI
turn_on = tk.Button(root, text="ON")
turn_on.pack()
turn_off = tk.Button(root, text="OFF", command=root.destroy)
turn_off.pack()
volume = tk.Label(root, text="VOLUME")
volume.pack()
vol_up = tk.Button(root, text="+")
vol_up.pack()
vol_down = tk.Button(root, text="-")
vol_down.pack()
root.mainloop()

```

In this example, we create four buttons and one label. The order in which we create them in the code is the same order in which they will appear on the window. We make the `turn_on` button from the `Button` class. 
The first argument is the main window, `root`, and the second is the text we want to display on the button, which is `"ON"` for the first button. Then, we use the `pack` geometry manager to display the button in the `root` window.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
You can check the tutorials on [creating the root window](https://www.pythonguis.com/tutorials/create-gui-tkinter/) and [how to create Labels](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/) for help with the above code.
We create the `turn_off`, `vol_up`, and `vol_down` buttons in a similar fashion and pack them with `pack()`. Only one of these buttons, `turn_off`, does something because we used the keyword `command` argument to make the button call `root.destroy()`, which closes the `root` window immediately:
![TV remote UI](https://www.pythonguis.com/static/tutorials/tkinter/create-buttons-in-tkinter/tv-remote-ui.png) _TV remote UI_
If you are developing your own GUI and have a few buttons that don't yet do anything, then there is also a way to make the button inactive. Just add `state=DISABLED` as one of the parameters, and the button cannot be clicked.
From here, we will be adding functions to each of our buttons and learning how to alter their appearances.
## Make Buttons Do Something When Clicked
Above, we have three buttons that don't do anything yet. Let's begin by creating a function and then set a button to call it:
python ```
import tkinter as tk
root = tk.Tk() # Create the main window
def volume_up():
  print("Volume Increased +1")
# Create the volume up button
vol_up = tk.Button(root, text="+", command=volume_up)
vol_up.pack()
root.mainloop()

```

The function `volume_up()` is called whenever the `vol_up` button is clicked in the window.
Now that we have a basic understanding of how to use the `Button` widget, the next step is to add more functionality to our TV remote. When the `turn_on` button is clicked, let's create a window that opens up and displays an image. For `vol_down`, let's also print out a message to keep things simple for now. The following displays the code, and each button has a command parameter:
python ```
import tkinter as tk
root = tk.Tk()
image = tk.PhotoImage(file="rain.gif")
def turn_tv_on():
  window = tk.Toplevel(root)
  window.title("TV")
  original_image = tk.Label(window, image=image)
  original_image.pack()
def volume_up():
  print("Volume Increase +1")
def volume_down():
  print("Volume Decrease -1")
turn_on = tk.Button(root, text="ON", command=turn_tv_on)
turn_on.pack()
turn_off = tk.Button(root, text="OFF", command=root.destroy)
turn_off.pack()
volume = tk.Label(root, text="VOLUME")
volume.pack()
vol_up = tk.Button(root, text="+", command=volume_up)
vol_up.pack()
vol_down = tk.Button(root, text="-", command=volume_down)
vol_down.pack()
root.mainloop()

```

Now, we have two functions to control the volume and one to turn the TV on. The next step is to pass the appropriate function to the `command` argument of our buttons. Here's what happens when we click the _ON_ button:
![Turning the TV window "on" by clicking a button](https://www.pythonguis.com/static/tutorials/tkinter/create-buttons-in-tkinter/turn-tv-on-by-clicking-a-button.png) _Turning the TV window "on" with the click of a button_
When the volume buttons are clicked, the following will display as output in the terminal: 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
![Changing the volume with our buttons - terminal output](https://www.pythonguis.com/static/tutorials/tkinter/create-buttons-in-tkinter/changing-volume-buttons-terminal-output.png) _Changing the volume with our buttons - terminal output_
This trick can be very useful for testing whether your buttons are working properly or for getting feedback from the function calls.
## Explore Other Button Parameters
The `Button` class also has some other options. Let's look at some of the more commonly used ones. Many of these parameters can help you create buttons that look nice or fit well into the style of our GUIs.
The `tkinter.ttk` module provides themed versions of Tkinter basic widgets. If you are interested, then check out the module's [documentation](https://docs.python.org/3/library/tkinter.ttk.html).
Here are some of the most common parameters used to create buttons:
  1. `activebackground` and `activeforeground` set the background and foreground colors when the cursor is over the button.
  2. `bd` sets the border width of a button in pixels.
  3. `bg` and `fg`: sets the background and foreground colors.
  4. `font` defines the text font to use for the button.
  5. `height` and `width` set the height and width of a button.
  6. `image` displays an image on the button rather than or along with text.


## Display an Image on a Button
Let's finish by showing how to add an image to a button. Modifying the code for the `"ON"` button from above, the following code will display an image on the button rather than text.
python ```
photo = tk.PhotoImage(file="on-button.gif")
photo = photo.subsample(10, 10)
turn_on = tk.Button(root, image=photo, command=turn_tv_on)
turn_on.pack()

```

Here, we load the image using `PhotoImage`. Then, we resize the image using the `subsample()` method. Finally, we remove the `text="ON"` parameter from earlier and add `image=photo`.
Here's how our GUI will look like:
![ON button with an image](https://www.pythonguis.com/static/tutorials/tkinter/create-buttons-in-tkinter/on-button-with-image.png) _ON button with an image_
## Summary
In this tutorial you have learned how to create buttons in Tkinter applications. You've added these buttons to your UI and then hooked them up to handler methods to make things happen. You have also learned how to customize the appearance of the buttons by adding images. You will now be able to add functional buttons to your own applications.
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
Continue with [ Tkinter Tutorial ](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/ "Continue to next part")
Return to [Create Desktop GUI Applications with Tkinter ](https://www.pythonguis.com/tkinter-tutorial/)
[![Joshua Willman](https://www.pythonguis.com/static/theme/images/authors/joshua-willman.jpg)](https://www.pythonguis.com/authors/joshua-willman/)
**Create Buttons in Tkinter** was written by [Joshua Willman](https://www.pythonguis.com/authors/joshua-willman/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) and [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
**Create Buttons in Tkinter** was published in [tutorials](https://www.pythonguis.com/tutorials/) on July 13, 2022 (updated January 10, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[python](https://www.pythonguis.com/topics/python/) [tkinter](https://www.pythonguis.com/topics/tkinter/) [gui](https://www.pythonguis.com/topics/gui/) [tk](https://www.pythonguis.com/topics/tk/) [button](https://www.pythonguis.com/topics/button/) [widgets](https://www.pythonguis.com/topics/widgets/) [ foundation](https://www.pythonguis.com/topics/foundation/) [ tkinter-foundation](https://www.pythonguis.com/topics/tkinter-foundation/)
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
