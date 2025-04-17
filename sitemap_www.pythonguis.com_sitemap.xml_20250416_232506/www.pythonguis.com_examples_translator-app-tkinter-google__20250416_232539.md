# Content from: https://www.pythonguis.com/examples/translator-app-tkinter-google/

[](https://www.pythonguis.com/examples/translator-app-tkinter-google/#menu)
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
# Building a Translation Application Using Tkinter
Translate Your Text With Python and Tkinter
by [Khumbo Klein](https://www.pythonguis.com/authors/khumbo-klein/) Last updated Apr 01 Tkinter [ Example applications ](https://www.pythonguis.com/examples/)
[ Translator Application Assets ](https://downloads.pythonguis.com/translator-app-assets-google.zip)
Whether learning a new natural language or just browsing foreign websites, you sometimes come across a text that you want to read but is written in a language you don't fully understand. To translate one natural language into your native language, you can use a _translator_ tool.
In this tutorial, we'll build a desktop translator application to translate natural language using the Google Translate APIs. The UI will be built using the Tkinter GUI library from the Python standard library.
Table of Contents
  * [Demo: A Translator App with Tkinter](https://www.pythonguis.com/examples/translator-app-tkinter-google/#demo-a-translator-app-with-tkinter)
  * [Installing the Required Packages](https://www.pythonguis.com/examples/translator-app-tkinter-google/#installing-the-required-packages)
  * [Building the Window](https://www.pythonguis.com/examples/translator-app-tkinter-google/#building-the-window)
  * [Creating the GUI](https://www.pythonguis.com/examples/translator-app-tkinter-google/#creating-the-gui)
  * [Implementing the Translation Functionality](https://www.pythonguis.com/examples/translator-app-tkinter-google/#implementing-the-translation-functionality)
  * [Using the Translator App](https://www.pythonguis.com/examples/translator-app-tkinter-google/#using-the-translator-app)
  * [Conclusion](https://www.pythonguis.com/examples/translator-app-tkinter-google/#conclusion)


## Demo: A Translator App with Tkinter
We'll work through the process of building the app step by step. Once we finish the tutorial, the app will look and work like the following:
You can select the source and target languages. Then, you can paste or type some text in the left-hand area and hit the _Translate_ button to get the translated text in the right-hand area.
## Installing the Required Packages
Our _Translator_ uses the `deep-translator` library to perform the actual translation via Google. Tkinter is already available in the standard library, so we just need to install `deep-translator`.
The first task will be to set up a Python [virtual environment](https://www.pythonguis.com/tutorials/python-virtual-environments/). Open the terminal, and run the following commands:
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
  * Windows
  * macOS/Linux


bat ```
> mkdir translator
> cd translator
> python -m venv venv
> .\venv\Scripts\activate
> python -m pip install deep-translator

```

sh ```
$ mkdir translator
$ cd translator/
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install deep-translator

```

Working through these instructions, we first create a root directory for the _Translator_ app with the `mkdir` command. Next, we create and activate a Python virtual environment for the project. Finally, we install the `deep-translator` package.
Now, create a file named `translator.py` in the root of your project. Additionally, create a folder called `images/` where you'll store the icons for the application. The folder structure should look like this:
python ```
translator/
│
├── images/
│  ├── arrow.png
│  └── logo.png
│
└── translator.py

```

The images for this project can be [downloaded here](https://downloads.pythonguis.com/translator-app-assets-google.zip).
The `images/` folder contains the two icons that you'll use for the application. The `translator.py` is the app's source file.
## Building the Window
Open the `translator.py` file with your favorite Python code editor. We'll start by creating our main window:
python ```
import tkinter as tk
class TranslatorApp(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Language Translator")
    self.resizable(width=False, height=False)
if __name__ == "__main__":
  app = TranslatorApp()
  app.mainloop()

```

This code imports Tkinter and then defines the application's main class, which we have called `TranslatorApp`. This class will hold the application's main window and allow us to run the main loop.
Importing `tkinter` under the alias `tk` is a common practice in Tkinter code.
Inside the class, we define the `__init__()` method, which handles the class's initialization. In this method, we first call the initializer `__init__()` of the parent class, `tk.Tk`, to initialize the app's window. Then, we set the window's title using the `title()` method. To make the window unresizable, we use the `resizable()` method with `width` and `height` set to `False`.
At the bottom of the code, we have the `if __name__ == "__main__"` idiom to check whether the file is being run directly as an executable program. Inside the condition block, we first create an instance of `TranslatorApp` and then run the application's main loop or event loop.
If you run this code, you'll get an empty Tkinter window on your desktop:
sh ```
$ python translator.py

```

![The empty Tkinter window](https://www.pythonguis.com/static/examples/translator-app-tkinter-google/empty-window.png) _The empty Tkinter window_
## Creating the GUI
Now that the main window is set up, let's start adding widgets to build the GUI. To do this, we'll create a method called `setup_ui()`, as shown below:
python ```
import tkinter as tk
class TranslatorApp(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Language Translator")
    self.resizable(width=False, height=False)
    self.setup_ui()
  def setup_ui(self):
    frame = tk.Frame(self)
    frame.pack(padx=10, pady=10)
if __name__ == "__main__":
  app = TranslatorApp()
  app.mainloop()

```

The `setup_ui()` method will define the application's GUI. In this method, we first create a frame widget using the `tk.Frame` class whose `master` argument is set to `self` (the application's main window). Next, we position the frame inside the main window using the [`pack()` geometry manager](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-pack-layout-manager/), using `padx` and `pady` arguments to set some padding around the frame. Finally, we add the call to `self.setup_ui()` to the `__init__()` method.
We'll continue to develop the UI by adding code to the `setup_ui()` method. Next, we'll add the app's logo. In the `setup_ui()` method, add the following code below the `frame` definition:
python ```
import tkinter as tk
class TranslatorApp(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Language Translator")
    self.resizable(width=False, height=False)
    self.setup_ui()
  def setup_ui(self):
    frame = tk.Frame(self)
    frame.pack(padx=10, pady=10)
    self.logo = tk.PhotoImage(file="images/logo.png").subsample(5, 5)
    tk.Label(frame, image=self.logo).grid(row=0, column=0, sticky="w")
if __name__ == "__main__":
  app = TranslatorApp()
  app.mainloop()

```

This code loads the logo using the `tk.PhotoImage` class. To resize it, we use the `subsample()` method. Then, we add the logo to the frame using a `tk.Label` widget. The label takes the frame and the logo as arguments. To position the logo, we use the [`grid()` geometry manager](https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/) with appropriate values for the `row`, `column`, and `sticky` arguments.
The `sticky` argument determines which side of a cell the widget should align -- North (top), South (bottom), East (right) or West (left). Here, we're aligning it on the West or left of the cell with `"w"`:
![Tkinter window with the Google Translate logo in it](https://www.pythonguis.com/static/examples/translator-app-tkinter-google/window-with-logo.png) _Tkinter window with the Google Translate logo in it_
Let's start adding some inputs to the UIs. First, we'll create the language selection drop-down boxes:
python ```
import tkinter as tk
import tkinter.ttk as ttk
from deep_translator import GoogleTranslator
DEFAULT_SOURCE = "english"
DEFAULT_DEST = "dutch"
translator = GoogleTranslator(source=DEFAULT_SOURCE, target=DEFAULT_DEST)

class TranslatorApp(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Language Translator")
    self.resizable(width=False, height=False)
    self.languages = translator.get_supported_languages(as_dict=True)
    self.language_names = list(self.languages.keys())
    self.setup_ui()
  def setup_ui(self):
    frame = tk.Frame(self)
    frame.pack(padx=10, pady=10)
    self.logo = tk.PhotoImage(file="images/logo.png").subsample(5, 5)
    tk.Label(frame, image=self.logo).grid(row=0, column=0, sticky="w")
    # Source language combobox
    self.from_language = ttk.Combobox(frame, values=self.language_names)
    self.from_language.current(self.language_names.index(DEFAULT_SOURCE))
    self.from_language.grid(row=1, column=0, sticky="we")
    # Arrow icon
    self.arrows = tk.PhotoImage(file="images/arrow.png").subsample(15, 15)
    tk.Label(frame, image=self.arrows).grid(row=1, column=1)
    # target language combobox
    self.to_language = ttk.Combobox(frame, values=self.language_names)
    self.to_language.current(self.language_names.index(DEFAULT_DEST))
    self.to_language.grid(row=1, column=2, sticky="we")
if __name__ == "__main__":
  app = TranslatorApp()
  app.mainloop()

```

We define the default languages for when the application starts up, using constants `DEFAULT_SOURCE` and `DEFAULT_DEST`. We create our instance of `GoogleTranslator` passing in these two default values.
In our window `__init__()` method we get a list of available languages by calling the `get_supported_languages()` method on a `GoogleTranslator` class inside `__init__()`. This method can return both a list or a dictionary with a language name as the key, and the language code in the values.
In this case we're getting the dictionary, so we can show the full name in the combo box while using the language code internally. We extract the names to a separate variable `self.language_names` so we can (a) pass this to the combo box, and (b) lookup the currently selected index to get the code later.
Next, we create two combo boxes to hold the list of source and target languages. The combo boxes are created using the `ttk.Combobox` class. One to the left and another to the right. Between the combo boxes, we add an arrow icon loaded using the `tk.PhotoImage` class. Again, we've added the icon to the app's window using `ttk.Label`.
Both combo boxes take `frame` and `values` as arguments. The `values` argument populates the combo boxes with languages. To specify the default language, we use the `current()` method, looking up the position of our default language in the `self.language_names` list with `index()`.
To position the combo boxes inside the frame, we use the `grid()` geometry manager with the appropriate arguments. Run the application, and you will see the following window:
![Source and target languages](https://www.pythonguis.com/static/examples/translator-app-tkinter-google/source-target-languages.png) _Source and target languages_
If you click on the sources combo box on the left, then you get the following:
![Source language combo box](https://www.pythonguis.com/static/examples/translator-app-tkinter-google/source-language-combobox.png) _Source language combo box_
Similarly, if you click on the target combo box on the right, you get the following:
![target combo box](https://www.pythonguis.com/static/examples/translator-app-tkinter-google/target-language-combobox.png) _target combo box_
With the source and target combo boxes in place, let's add three more widgets: two scrollable text widgets and a button. The scrollable text on the left will hold the source text, while the scrollable text on the right will hold the translated text. The button will allow us to run the actual translation.
Get back to the code editor and update the `setup_ui()` method as follows. Note that we also need to import the `ScrollText` class:
python ```
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
from deep_translator import GoogleTranslator
DEFAULT_SOURCE = "english"
DEFAULT_DEST = "dutch"
translator = GoogleTranslator(source=DEFAULT_SOURCE, target=DEFAULT_DEST)
class TranslatorApp(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Language Translator")
    self.resizable(width=False, height=False)
    self.languages = translator.get_supported_languages(as_dict=True)
    self.language_names = list(self.languages.keys())
    self.setup_ui()
  def setup_ui(self):
    frame = tk.Frame(self)
    frame.pack(padx=10, pady=10)
    self.logo = tk.PhotoImage(file="images/logo.png").subsample(5, 5)
    tk.Label(frame, image=self.logo).grid(row=0, column=0, sticky="w")
    # Source language combobox
    self.from_language = ttk.Combobox(frame, values=self.language_names)
    self.from_language.current(self.language_names.index(DEFAULT_SOURCE))
    self.from_language.grid(row=1, column=0, sticky="we")
    # Arrow icon
    self.arrows = tk.PhotoImage(file="images/arrow.png").subsample(15, 15)
    tk.Label(frame, image=self.arrows).grid(row=1, column=1)
    # target language combobox
    self.to_language = ttk.Combobox(frame, values=self.language_names)
    self.to_language.current(self.language_names.index(DEFAULT_DEST))
    self.to_language.grid(row=1, column=2, sticky="we")
    # Source text
    self.from_text = ScrolledText(
      frame,
      font=("Arial", 16),
      width=50,
      height=20,
    )
    self.from_text.grid(row=2, column=0)
    # Translated text
    self.to_text = ScrolledText(
      frame,
      font=("Arial", 16),
      width=50,
      height=20,
      state="disabled",
    )
    self.to_text.grid(row=2, column=2)
    # Translate button
    self.translate_button = ttk.Button(
      frame,
      text="Translate",
      command=self.translate,
    )
    self.translate_button.grid(row=3, column=0, columnspan=3, pady=10)
  def translate(self):
    pass
if __name__ == "__main__":
  app = TranslatorApp()
  app.mainloop()

```

In the code snippet, we use the `ScrolledText` class to create the two scrolled text areas. Both text areas take `frame`, `font`, `width`, and `height` as arguments. The second text area also takes `state` as an additional argument. Setting `state` to `"disabled"` allows us to create a read-only text area.
Then, we use the `ttk.Button` class to create a button with `frame`, `text`, and `command` as arguments. The `command` argument allows us to bind the button's click event to the `self.translate()` method, which we will define in a moment. For now, we've added a placeholder.
To position all these widgets on the app's window, we use the `grid()` geometry manager. Now, the app will look like the following:
![Translator app's GUI](https://www.pythonguis.com/static/examples/translator-app-tkinter-google/translator-finished-gui.png) _Translator app's GUI_
Our translation app's GUI is ready! Finally, we can start adding functionality to the application.
## Implementing the Translation Functionality
We'll implement the language translation functionality in the `translate()` method. This gets the current values from the UI and then uses `GoogleTranslator` to perform the translation. We need our imports as shown below:
python ```
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showerror
from tkinter.scrolledtext import ScrolledText
from deep_translator import GoogleTranslator
DEFAULT_SOURCE = "english"
DEFAULT_DEST = "dutch"

```

Here we've imported the `showerror` helper for displaying error boxes in our application.
Now we can implement the `translate()` method:
python ```

class TranslatorApp(tk.Tk):
  # ...
  def translate(self):
    source_language = self.languages[self.from_language.get()]
    target_language = self.languages[self.to_language.get()]
    text = self.from_text.get(1.0, tk.END).strip()
    if not source_language or not target_language:
      showerror(
        title="Error",
        message="Make sure to set the source and target language",
      )
      return
    if not text:
      showerror(
        title="Error",
        message="Make sure to enter some text to translate",
      )
      return
    try:
      translator.source = source_language
      translator.target = target_language
      translation = translator.translate(text)
    except Exception as e:
      showerror(
        title="Error",
        message=f"An error occurred: {e}",
      )
      return
    self.to_text.config(state="normal")
    self.to_text.delete(1.0, tk.END)
    self.to_text.insert(tk.END, translation)
    self.to_text.config(state="disabled")

```

The `translate()` method handles the entire translation process. It starts by retrieving the source and target languages from the corresponding combo boxes. If either language is not defined, then we display a message to inform the user about the problem. To do this, we use a `showerror` dialog.
We get the currently selected _source_ and _target_ languages from the comboboxes. We get the current name with `.get()` and then look this up in `self.languages` to get the language code. Next, we try to get the input text from the source scrolled area on the left. If the user doesn't provide any text, then we display an error with the appropriate message.
Once we have the source and target language and some text to translate, we can perform the actual translation. To do this we first set the `source` and `target` language codes on our `translator` object (the instance of `GoogleTranslator`) and then call `translate()`.
If the call to `translate()` finds an error, we inform the user about it. To handle any exceptions, we catch the generic `Exception` class and display an error message with the exception details.
If the translation is successful, then we enable the target scrolled area, display the translated text, and disable the area again so it remains read-only.
The complete final code is shown below:
python ```
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showerror
from tkinter.scrolledtext import ScrolledText
from deep_translator import GoogleTranslator
DEFAULT_SOURCE = "english"
DEFAULT_DEST = "dutch"
translator = GoogleTranslator(source=DEFAULT_SOURCE, target=DEFAULT_DEST)

class TranslatorApp(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Language Translator")
    self.resizable(width=False, height=False)
    self.languages = translator.get_supported_languages(as_dict=True)
    self.language_names = list(self.languages.keys())
    self.setup_ui()
  def setup_ui(self):
    frame = tk.Frame(self)
    frame.pack(padx=10, pady=10)
    self.logo = tk.PhotoImage(file="images/logo.png").subsample(5, 5)
    tk.Label(frame, image=self.logo).grid(row=0, column=0, sticky="w")
    # Source language combobox
    self.from_language = ttk.Combobox(frame, values=self.language_names)
    self.from_language.current(self.language_names.index(DEFAULT_SOURCE))
    self.from_language.grid(row=1, column=0, sticky="we")
    # Arrow icon
    self.arrows = tk.PhotoImage(file="images/arrow.png").subsample(15, 15)
    tk.Label(frame, image=self.arrows).grid(row=1, column=1)
    # Tartget language combobox
    self.to_language = ttk.Combobox(frame, values=self.language_names)
    self.to_language.current(self.language_names.index(DEFAULT_DEST))
    self.to_language.grid(row=1, column=2, sticky="we")
    # Source text
    self.from_text = ScrolledText(
      frame,
      font=("Arial", 16),
      width=50,
      height=20,
    )
    self.from_text.grid(row=2, column=0)
    # Translated text
    self.to_text = ScrolledText(
      frame,
      font=("Arial", 16),
      width=50,
      height=20,
      state="disabled",
    )
    self.to_text.grid(row=2, column=2)
    # Translate button
    self.translate_button = ttk.Button(
      frame,
      text="Translate",
      command=self.translate,
    )
    self.translate_button.grid(row=3, column=0, columnspan=3, pady=10)
  def translate(self):
    source_language = self.languages[self.from_language.get()]
    target_language = self.languages[self.to_language.get()]
    text = self.from_text.get(1.0, tk.END).strip()
    if not source_language or not target_language:
      showerror(
        title="Error",
        message="Make sure to set the source and target language",
      )
      return
    if not text:
      showerror(
        title="Error",
        message="Make sure to enter some text to translate",
      )
      return
    try:
      translator.source = source_language
      translator.target = target_language
      translation = translator.translate(text)
    except Exception as e:
      showerror(
        title="Error",
        message=f"An error occurred: {e}",
      )
      return
    self.to_text.config(state="normal")
    self.to_text.delete(1.0, tk.END)
    self.to_text.insert(tk.END, translation)
    self.to_text.config(state="disabled")

if __name__ == "__main__":
  app = TranslatorApp()
  app.mainloop()

```

## Using the Translator App
The video below demonstrates how we can use our app to translate some text from one natural language to another:
Great! You have successfully built a language translator using Python, Tkinter, and the `googletrans` package.
## Conclusion
In this tutorial we built a Translator application using the Tkinter GUI library from the Python standard library. We worked step by step through building the UI using a grid layout, and then implemented the language translation functionality with the `GoogleTranslator` class.
Try and take what you've learned in this tutorial and apply it to your own projects!
Mark As Complete 
[![Khumbo Klein](https://www.pythonguis.com/static/theme/images/authors/khumbo-klein.jpg)](https://www.pythonguis.com/authors/khumbo-klein/)
**Building a Translation Application Using Tkinter** was written by [Khumbo Klein](https://www.pythonguis.com/authors/khumbo-klein/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) and [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
**Building a Translation Application Using Tkinter** was published in [examples](https://www.pythonguis.com/examples/) on November 29, 2024 (updated April 01, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[Tkinter](https://www.pythonguis.com/topics/tkinter/) [translator](https://www.pythonguis.com/topics/translator/)
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
