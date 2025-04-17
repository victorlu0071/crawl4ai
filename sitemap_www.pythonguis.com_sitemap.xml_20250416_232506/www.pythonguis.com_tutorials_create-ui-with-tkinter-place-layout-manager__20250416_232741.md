# Content from: https://www.pythonguis.com/tutorials/create-ui-with-tkinter-place-layout-manager/

[](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-place-layout-manager/#menu)
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
# Using the Place Geometry Manager in Tkinter
Laying out widgets with the Place geometry manager
by [Joshua Willman](https://www.pythonguis.com/authors/joshua-willman/) Last updated Jan 12 Tkinter [ Getting started with Tkinter ](https://www.pythonguis.com/tkinter-tutorial/#tkinter-getting-started)
#### [ Tkinter Tutorial ](https://www.pythonguis.com/tkinter-tutorial/) — [Getting started with Tkinter](https://www.pythonguis.com/tkinter-tutorial/#tkinter-getting-started)
  * [Create a GUI Using Tkinter and Python](https://www.pythonguis.com/tutorials/create-gui-tkinter/)
  * [Use Tkinter to Design GUI Layouts](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/)
  * [Create Buttons in Tkinter](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/)
  * [Using the Pack Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/)
  * [Using the Grid Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/)
  * [Using the Place Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-place-layout-manager/)
  * [Create Radiobuttons and Checkbuttons in Tkinter](https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/)


In this tutorial, we will look at how Tkinter's `place` geometry managers help you lay out your GUI application interface. 
In previous tutorials we've introduced Tkinter's [pack](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/) and [grid](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/) geometry managers and shown how you can use those to layout most user interfaces. In this tutorial we'll look at the final geometry manager that Tkinter offers: `place`. 
If you're confused about which layout manager to use, you can see our guide to the [differences between pack, place and grid](https://www.pythonguis.com/faq/pack-place-and-grid-in-tkinter/).
Table of Contents
  * [The place Geometry Manager](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-place-layout-manager/#the-place-geometry-manager)
  * [A Demo GUI With place](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-place-layout-manager/#a-demo-gui-with-place)
  * [Summary](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-place-layout-manager/#summary)


## The `place` Geometry Manager
The `place` geometry manager allows you to have absolute control over the arrangement of your widgets. With `place`, you can specify the size of the widget, as well as the exact x and y coordinates to arrange it within the parent window. The `place` manager is useful for arranging buttons or other smaller widgets together within a simple dialog window.
A few of the parameters you can play around with are listed below:
  * `in_`: specifies the master window for the widget
  * `x`, `y`: specifies the specific x and y values of the widget in the parent window
  * `relx`, `rely`: horizontal and vertical offset relative to the size of the parent widget, values between `0.0` and `1.0`
  * `relwidth`, `relheight`: set the height and width of widgets relative to the size of the parent widget, values between `0.0` and `1.0`
  * `anchor`: defines where the widget is placed in the parent widget, specified by `'n'`, `'s'`, `'e'`, `'w'`, or some combination of them. The default is `'center'`


## A Demo GUI With `place`
Let's take a look at a quick example that shows how to lay out widgets on a dialog using the `place` geometry manager. Below, we create an app that asks the user a question and allows them to select an option from a `Listbox`:
python ```
import tkinter as tk
root = tk.Tk()
root.title("Place layout Example")
root.geometry("300x300+50+100")
def display_selection(event):
  selection = cities_listbox.curselection()
  print(cities_listbox.get(selection))
# Label to display the question
tk.Label(
  root,
  text="Which of the following cities would you like to travel to?",
  wraplength=200,
).place(x=50, y=20)
# Listbox to display the cities
cities_listbox = tk.Listbox(root, selectmode=tk.BROWSE, width=24)
cities_listbox.place(x=40, y=65)
cities = ["Beijing", "Singapore", "Tokyo", "Dubai", "New York"]
for city in cities:
  cities_listbox.insert(tk.END, city)
# Bind the listbox's selection
cities_listbox.bind("<<ListboxSelect>>", display_selection)
# Button to close the app
end_button = tk.Button(root, text="End", command=quit)
end_button.place(x=125, y=250)
root.mainloop()

```

The code above will produce the following GUI: 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
![Tkinter window using the place geometry manager](https://www.pythonguis.com/static/tutorials/tkinter/create-ui-with-tkinter-place-layout-manager/tkinter-window-with-place-geometry-manager.png) _Tkinter GUI window using place geometry manager_
The GUI application itself is very minimal, consisting of a label, a listbox, and a button. The example above shows how to use absolute positioning by using the `x` and `y` arguments with the `place` geometry manager.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
While `place` may seem like an easier way to create the layout of your UI, it also means that you need to manually tweak positions as your UI grows and changes. For that reason, use it with caution. For complex UIs it's usually better to use automatic pack and grid layouts instead.
## Summary
In this article, you learned the basics of using `place` for geometry management in a Tkinter-based GUI application. While this geometry manager can get fiddly with complex UIs, it is useful when you want more control over the exact position of your widgets in your windows, or simple dialogs. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
Continue with [ Tkinter Tutorial ](https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/ "Continue to next part")
Return to [Create Desktop GUI Applications with Tkinter ](https://www.pythonguis.com/tkinter-tutorial/)
[![Joshua Willman](https://www.pythonguis.com/static/theme/images/authors/joshua-willman.jpg)](https://www.pythonguis.com/authors/joshua-willman/)
**Using the Place Geometry Manager in Tkinter** was written by [Joshua Willman](https://www.pythonguis.com/authors/joshua-willman/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) and [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
**Using the Place Geometry Manager in Tkinter** was published in [tutorials](https://www.pythonguis.com/tutorials/) on November 19, 2022 (updated January 12, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[python](https://www.pythonguis.com/topics/python/) [tkinter](https://www.pythonguis.com/topics/tkinter/) [gui](https://www.pythonguis.com/topics/gui/) [tk](https://www.pythonguis.com/topics/tk/) [layout](https://www.pythonguis.com/topics/layout/) [geomerty](https://www.pythonguis.com/topics/geomerty/) [place](https://www.pythonguis.com/topics/place/) [geometry-manager](https://www.pythonguis.com/topics/geometry-manager/) [ foundation](https://www.pythonguis.com/topics/foundation/) [ tkinter-foundation](https://www.pythonguis.com/topics/tkinter-foundation/)
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
