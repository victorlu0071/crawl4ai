# Content from: https://www.pythonguis.com/tutorials/customized-windows-tkinter/

[](https://www.pythonguis.com/tutorials/customized-windows-tkinter/#menu)
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
# Customizing Your Tkinter App's Windows
Make Your Tkinter App's Windows Have Different Looks
by [Khumbo Klein](https://www.pythonguis.com/authors/khumbo-klein/) Last updated Sep 13 Tkinter [ Tutorials ](https://www.pythonguis.com/tutorials/)
Different desktop applications have different design requirements. If you look at the applications on your computer, you will see that most of them have different window designs. Some applications, like games, run in full-screen mode. Utility applications, like calculators, run in fixed-size mode with the maximize or minimize button disabled.
Forms or windows have different appearances based on their app's requirements. As you create your own Tkinter applications, you might also want to have windows without a title bar, windows that can't be resized, windows that are zoomed, and even windows that show some level of transparency.
In this tutorial, you will learn some Tkinter tricks and techniques that you can use to customize your applications' windows.
Table of Contents
  * [Getting to Know Window Configurations](https://www.pythonguis.com/tutorials/customized-windows-tkinter/#getting-to-know-window-configurations)
  * [Creating a Simple Window in Tkinter](https://www.pythonguis.com/tutorials/customized-windows-tkinter/#creating-a-simple-window-in-tkinter)
  * [Removing the Window's Title Bar in Tkinter](https://www.pythonguis.com/tutorials/customized-windows-tkinter/#removing-the-windows-title-bar-in-tkinter)
  * [Disabling the Window's Maximize/Minimize Button](https://www.pythonguis.com/tutorials/customized-windows-tkinter/#disabling-the-windows-maximizeminimize-button)
  * [Displaying the App's Window in Zoomed Mode](https://www.pythonguis.com/tutorials/customized-windows-tkinter/#displaying-the-apps-window-in-zoomed-mode)
  * [Changing the Window's Transparency Level](https://www.pythonguis.com/tutorials/customized-windows-tkinter/#changing-the-windows-transparency-level)
  * [Conclusion](https://www.pythonguis.com/tutorials/customized-windows-tkinter/#conclusion)


## Getting to Know Window Configurations
In Tkinter, a window configuration is either a setting or an attribute that you can use to specify a property of that window. These properties may include the window's width, height, position, transparency, title bar, background color, and more.
These configurations allow you to tweak and customize the look and feel of your application's windows and forms so that they look modern and nice in the eyes of your app's users.
For example, let's say you want to create a game, and you need to remove the main window's title bar. Keep reading to learn how to do this in Tkinter.
## Creating a Simple Window in Tkinter
To kick things off, let's create a minimal Tkinter app that will work as our starting point for learning how to remove a window's title bar. Here's the required code:
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
python ```
from tkinter import Tk
# Create the app's main window
root = Tk()
root.title("Window With a Title Bar")
root.geometry("400x300+300+120")
# Run the app's main loop
root.mainloop()

```

Here, we import `Tk` from `tkinter`. Then we create the app's main window, `root`, by instantiating `Tk`. Next, we give our window a title and geometry using the `title()` and `geometry()` methods, respectively.
Go ahead and save this code to a file called `app.py`. Then run the file from your command line. The output will look something like this:
![A Tkinter app showing a window with the default title bar](https://www.pythonguis.com/static/tutorials/tkinter/customized-windows-tkinter/window-with-title-bar.png) _A Tkinter app showing a window with the default title bar_
On your screen, you'll get a regular Tkinter window with the title bar and the decoration provided by your current operating system.
## Removing the Window's Title Bar in Tkinter
Tkinter makes it possible for you to remove the system-provided title bar of your app's main window. This tweak is handy when building a custom GUI that doesn't use the default window decorations.
![The default title bar highlighted on our example window](https://www.pythonguis.com/static/tutorials/tkinter/customized-windows-tkinter/window-with-title-bar-highlighted.png) _The default title bar highlighted on our example window_
In the image above, the red border highlights the window's title bar. That's what we want to remove. To do that, we can use a method called `overrideredirect()`. If we pass `True` as an argument to this method, then we'll get a frameless window.
Go ahead and update your code. Make it look something like this:
python ```
from tkinter import Tk
# Create the app's main window
root = Tk()
root.geometry("400x300+300+120")
# Removes the window's title bar
root.overrideredirect(True)
# Run the app's main loop
root.mainloop()

```

By calling `root.overrideredirect(True)`, we tell the window manager (which manages windows on your desktop) not to wrap the window in the usual window decorations. If you run the app again, then you will get the following output:
![A Tkinter app showing a window without title bar](https://www.pythonguis.com/static/tutorials/tkinter/customized-windows-tkinter/window-without-title-bar.png) _A Tkinter app showing a window without title bar_
You have successfully created a Tkinter app with a window that doesn't have the standard window decorations from your desktop window manager.
Because the app's window has no close button, you must press _Alt+F4_ to close the window and terminate the app.
## Disabling the Window's Maximize/Minimize Button
There are some situations where we would want to have a window with a title bar but with a fixed size. That would be the case with a calculator application, for example. To do that, we can use the `resizable()` method, which takes two boolean arguments:
  1. **`width`**specifies whether the window can be horizontally resized.
  2. **`height`**specifies whether the window can be vertically resized.


If you pass `False` for both arguments, you will disable resizing in both directions. Below we've modified the code for our simple Tkinter app, preventing users from resizing the main window:
python ```
from tkinter import Tk
# Create the app's main window
root = Tk()
root.title("Fixed Size Window")
root.geometry("400x300+300+120")
# Disable the window's resizing capability
root.resizable(False, False)
# Run the app's main loop
root.mainloop()

```

In this example, the code calls `resizable()` with its `width` and `height` argument set to `False`. This call makes the window unresizable. If you run this app, then you'll get the output shown below:
![A Tkinter app showing a fixed size window](https://www.pythonguis.com/static/tutorials/tkinter/customized-windows-tkinter/fixed-size-window.png) _A Tkinter app showing a fixed size window_
Try to resize this window by dragging any of its borders, and you'll find that you can't resize it in either direction. You will also discover that the maximize/minimize buttons are now also disabled, preventing you from resizing the window in this way.
## Displaying the App's Window in Zoomed Mode
Tkinter also allows you to display an app's window in **zoomed mode**. In zoomed mode, your application's window will display in fullscreen. A common scenario where this mode comes in handy is when you want to provide an immersive experience to your users.
On Windows and macOS, the method for displaying the app's window in zoomed mode is `state()`. You can pass the `"zoomed"` string as an argument to this method to get the desired result. The code for that will look like below:
python ```
from tkinter import Tk
# Create the app's main window
root = Tk()
root.title("Zoomed Window")
root.geometry("400x300+300+120")
# Set the window to a zoomed mode
root.state("zoomed")
# Run the app's main loop
root.mainloop()

```

The line `root.state("zoomed")` makes the window display already zoomed on both Windows and macOS. If you are on Linux, then use `root.attributes("-zoomed", True)` instead. The app's window looks something like this:
![A Tkinter app showing a zoomed window](https://www.pythonguis.com/static/tutorials/tkinter/customized-windows-tkinter/zommed-window.png) _A Tkinter app showing a zoomed window_
In this screenshot, you can see that the application's main window occupies the entire screen, which gives you a larger working area.
## Changing the Window's Transparency Level
What if you wanted to change the transparency of your app's main window? You can do this using the `attributes()` method. To set the transparency, you provide two arguments: first the string `"-alpha"`, then a floating-point number that ranges from `0.0` to `1.0`. A value of `0.0` represents the highest transparency level (full transparency, your window will become invisible), while a value of `1.0` value represents the lowest level (no transparency).
Let's create a window with a `0.6` transparency level:
python ```
from tkinter import Tk
# Create the app's main window
root = Tk()
root.title("0.6 Transparency Window")
root.geometry("400x300+300+120")
# Set the -alpha value to 0.6
root.attributes("-alpha", 0.6)
# Run the app's main loop
root.mainloop()

```

In this example, we set the `"-alpha"` attribute to `0.6`. This tweak generates a window that looks something like this:
![A Tkinter app showing a transparent window](https://www.pythonguis.com/static/tutorials/tkinter/customized-windows-tkinter/window-transparency.png) _A Tkinter app showing a transparent window_
Your app's main window is now 60% transparent. Isn't that cool? Do you have any creative ideas for your next application?
## Conclusion
In this tutorial, you've gone through the process of customizing the root window of a Tkinter application using several different methods, attributes, and properties. You've learned how to remove the title bar of a window, make a window have a fixed size, display a window in zoomed mode, and more.
Mark As Complete 
[![Khumbo Klein](https://www.pythonguis.com/static/theme/images/authors/khumbo-klein.jpg)](https://www.pythonguis.com/authors/khumbo-klein/)
**Customizing Your Tkinter App's Windows** was written by [Khumbo Klein](https://www.pythonguis.com/authors/khumbo-klein/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) and [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
**Customizing Your Tkinter App's Windows** was published in [tutorials](https://www.pythonguis.com/tutorials/) on July 25, 2023 (updated September 13, 2023) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[Tkinter](https://www.pythonguis.com/topics/tkinter/) [window](https://www.pythonguis.com/topics/window/) [titlebar](https://www.pythonguis.com/topics/titlebar/) [minimize](https://www.pythonguis.com/topics/minimize/) [maximize](https://www.pythonguis.com/topics/maximize/) [transparency](https://www.pythonguis.com/topics/transparency/)
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
