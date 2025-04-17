# Content from: https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/

[](https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/#menu)
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
# Create Radiobuttons and Checkbuttons in Tkinter
Add selectable button widgets to your Tkinter GUI
by [Joshua Willman](https://www.pythonguis.com/authors/joshua-willman/) Last updated Jan 10 Tkinter [ Getting started with Tkinter ](https://www.pythonguis.com/tkinter-tutorial/#tkinter-getting-started)
#### [ Tkinter Tutorial ](https://www.pythonguis.com/tkinter-tutorial/) — [Getting started with Tkinter](https://www.pythonguis.com/tkinter-tutorial/#tkinter-getting-started)
  * [Create a GUI Using Tkinter and Python](https://www.pythonguis.com/tutorials/create-gui-tkinter/)
  * [Use Tkinter to Design GUI Layouts](https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/)
  * [Create Buttons in Tkinter](https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/)
  * [Using the Pack Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/)
  * [Using the Grid Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/)
  * [Using the Place Geometry Manager in Tkinter](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-place-layout-manager/)
  * [Create Radiobuttons and Checkbuttons in Tkinter](https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/)


In the previous tutorials we've taken the first steps building apps with Tkinter, creating windows and adding simple label and button widgets. We've also looked at geometry managers for laying out widgets in a window.
In this tutorial, we'll focus on two more commonly used Tkinter widgets – `Checkbutton` and `Radiobutton`. These inputs are clickable widgets with which you can present options for users to select. Check buttons let you select multiple choices, while radio buttons allow a unique option.
Table of Contents
  * [Creating a Checkbutton Widget](https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/#creating-a-checkbutton-widget)
  * [Creating a Radiobutton Widget](https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/#creating-a-radiobutton-widget)
  * [Building a Demo Food Ordering GUI](https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/#building-a-demo-food-ordering-gui)
  * [Summary](https://www.pythonguis.com/tutorials/tkinter-radiobutton-and-checkbutton/#summary)


## Creating a `Checkbutton` Widget
Checkbuttons (also called checkboxes) are simple widgets which can be checked and unchecked by the user. They are commonly used for switching features (or behavior) on and off in settings panels, or for selecting items from a list of choices. When checked a checkbox is considered "on" and when unchecked it is "off". Different checkboxes should behave independently of one another, although sometimes you may want to enable/disable some checkboxes based on the state of another.
When toggled `Checkbutton` widgets can call methods or functions using the `command` argument. The current state of a `Checkbutton` is stored in an external control variable. Control variables are created using Tkinter's variable classes, such as `IntVar`, `DoubleVar`, `BooleanVar`, and `StringVar`. The linked control variable will be updated to reflect any changes in the widget.
Let's take a look at a basic app that sets up a `Checkbutton` widget:
python ```
import tkinter as tk
root = tk.Tk()
root.title("Checkbutton")
root.geometry("200x100")
def select_items():
  label.config(text=f"Selected: {bool(variable.get())}")
variable = tk.IntVar()
item = tk.Checkbutton(
  root,
  text="Tuna fish",
  command=select_items,
  variable=variable,
)
item.pack(anchor="w", padx=10, pady=10)
label = tk.Label(root, text="Selected: False")
label.pack(
  anchor="w",
  padx=10,
  pady=10,
)
root.mainloop()

```

In this example, the main window contains a `Checkbutton` labeled `"Tuna fish"` and a `Label` that displays whether the checkbox is selected. The state of the `Checkbutton` is linked to a `tk.IntVar` variable, which stores `1` when the button is checked and `0` when unchecked.
When you select and unselect the check button, the `select_items()` function is called, updating the `Label` to show the selection status (`True` or `False`) based on the value of the variable. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Save the code as `app.py` and run it as for any other Python script.
bash ```
python app.py

```

You'll see the following window:
![Tkinter demo app showing a checkbutton](https://www.pythonguis.com/static/tutorials/tkinter/tkinter-radiobutton-and-checkbutton/checkbutton-demo-tkinter.png) _Tkinter demo app showing a Check button_
## Creating a `Radiobutton` Widget
Whereas the `Checkbutton` widgets are useful for selecting several choices, the `Radiobutton` widget is used for picking one choice out of many.
To achieve exclusivity among the radio buttons in a group, they must share the same variable. This means that when one radio button in a group is selected any other selected widgets will be deselected.
Here's an example demonstrating how to use `Radiobutton` widgets:
python ```
import tkinter as tk
root = tk.Tk()
root.title("Radiobutton")
root.geometry("180x240")
countries = ["USA", "France", "Germany", "Sweden", "Brazil"]
label = tk.Label(
  root,
  text=f"Selected: {countries[0]}",
)
label.pack(anchor="w", padx=10, pady=10)
def selection():
  label.config(text=f"Selected: {variable.get()}")
variable = tk.StringVar(root, f"{countries[0]}")
for country in countries:
  tk.Radiobutton(
    root,
    text=country,
    variable=variable,
    value=country,
    command=selection,
  ).pack(anchor="w", padx=10, pady=5)
root.mainloop()

```

In this code, we create a `Label` that shows the currently selected country, initialized to `"USA"`. A `StringVar` variable stores the selected value among a list of countries.
Then, you start a loop to generate a `Radiobutton` widget for each country, binding its `value` to the corresponding country name. When you select a given `Radiobutton`, the `selection()` function updates the `Label` to display the new selection.
You can see how the radio button group looks in the following screenshot:
![Tkinter demo app showing a Radiobutton group](https://www.pythonguis.com/static/tutorials/tkinter/tkinter-radiobutton-and-checkbutton/radiobutton-demo-tkinter.png) _Tkinter demo app showing a Radio button group_
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
As you can see, the process for creating radio buttons is similar to check buttons. However, we need one additional argument called `value` associated with each individual radio button. If you have a bunch of radio button widgets you need to create, try using a `for` loop to instantiate them.
## Building a Demo Food Ordering GUI
Now let's take code an example that combines `Checkbutton` and `Radiobutton` widgets to create a food ordering form that will look something like the following:
![Food ordering form](https://www.pythonguis.com/static/tutorials/tkinter/tkinter-radiobutton-and-checkbutton/food-ordering-form-tkinter.png) _Food ordering form_
Here's the code for our demos app:
python ```
import tkinter as tk
from tkinter import messagebox, ttk
class FoodOrderingApp(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Food Order Form")
    self.foods_list = ["Burger", "Pizza", "Fries", "Nuggets"]
    self.payment_methods = ["Cash", "Card", "Mobile App"]
    self.setup_header()
    self.setup_foods()
    self.setup_payment()
  def setup_header(self):
    self.image = tk.PhotoImage(file="food.png").subsample(3, 4)
    tk.Label(self, image=self.image).pack()
    tk.Label(
      self,
      text="Order Your Food!",
      font=("Helvetica", 20),
      bd=10,
    ).pack()
    line = ttk.Separator(self, orient=tk.HORIZONTAL)
    line.pack(fill="x")
    order_label = tk.Label(self, text="What would you like to order?")
    order_label.pack(anchor="w", padx=10, pady=5)
  def setup_foods(self):
    for food_item in self.foods_list:
      var = tk.IntVar()
      self.__dict__[food_item] = tk.Checkbutton(
        self, text=food_item, variable=var
      )
      self.__dict__[food_item].var = var
      self.__dict__[food_item].pack(anchor="w", padx=10, pady=5)
  def setup_payment(self):
    payment_label = tk.Label(
      self,
      text="How would you like to pay?",
    )
    payment_label.pack(anchor="w", padx=10, pady=5)
    self.var = tk.IntVar()
    self.var.set(0)
    for value, method in enumerate(self.payment_methods):
      tk.Radiobutton(
        self,
        text=method,
        variable=self.var,
        value=value,
      ).pack(anchor="w", padx=10, pady=5)
    next_button = tk.Button(
      self,
      text="Check out!",
      command=self.print_results,
      font=("Helvetica", 14),
    )
    next_button.pack(padx=10, pady=5)
  def print_results(self):
    msg = ""
    for food_name in self.foods_list:
      food_button = getattr(self, food_name)
      if food_button.var.get() == 1:
        msg += f"Item selected: {food_button['text']}\n"
    index = self.var.get()
    msg += f"Payment method: {self.payment_methods[index]}"
    messagebox.showinfo("Order Summary", msg)
if __name__ == "__main__":
  app = FoodOrderingApp()
  app.mainloop()

```

In this example, we use the `Checkbutton` widgets to allow users to select multiple food items from a predefined list of foods. Each `Checkbutton` is linked to an `IntVar` variable to track its selection state (`1` for selected, `0` for unselected). We display the check buttons vertically, aligned to the left (`anchor="w"`), with padding for spacing (`padx=10, pady=5`).
The `Radiobutton` widgets enable the user to select a single payment method from a list of possibilities. The `Radiobutton` widgets are linked to a shared `IntVar` variable (`self.var`). This ensures that only one button can be active at a time, reflecting the mutually exclusive nature of the payment options. The `Radiobutton` widgets are also packed vertically with padding and alignment to the left for consistent layout.
When the user clicks the _Check out!_ button, the `print_results()` method is called, gathering the selected items and the chosen payment method. The results are then displayed in a `messagebox` for user confirmation.
## Summary
In this tutorial, we took a quick look at the `Checkbutton` and `Radiobutton` widgets. These two types of widgets are useful for allowing a user to select choices from a group of options. Check buttons are used when a user needs to select multiple options, while radio buttons are used when a user only needs to select one choice from many.
You will now be able to add selectable options to your own applications.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
Mark As Complete 
[![Joshua Willman](https://www.pythonguis.com/static/theme/images/authors/joshua-willman.jpg)](https://www.pythonguis.com/authors/joshua-willman/)
**Create Radiobuttons and Checkbuttons in Tkinter** was written by [Joshua Willman](https://www.pythonguis.com/authors/joshua-willman/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) and [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
**Create Radiobuttons and Checkbuttons in Tkinter** was published in [tutorials](https://www.pythonguis.com/tutorials/) on March 30, 2022 (updated January 10, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[python](https://www.pythonguis.com/topics/python/) [tkinter](https://www.pythonguis.com/topics/tkinter/) [gui](https://www.pythonguis.com/topics/gui/) [tk](https://www.pythonguis.com/topics/tk/) [radiobutton](https://www.pythonguis.com/topics/radiobutton/) [checkbutton](https://www.pythonguis.com/topics/checkbutton/) [widgets](https://www.pythonguis.com/topics/widgets/) [ foundation](https://www.pythonguis.com/topics/foundation/) [ tkinter-foundation](https://www.pythonguis.com/topics/tkinter-foundation/)
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
