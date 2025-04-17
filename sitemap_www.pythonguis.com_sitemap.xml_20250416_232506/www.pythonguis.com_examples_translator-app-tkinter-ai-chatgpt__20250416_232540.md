# Content from: https://www.pythonguis.com/examples/translator-app-tkinter-ai-chatgpt/

[](https://www.pythonguis.com/examples/translator-app-tkinter-ai-chatgpt/#menu)
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
# Build a Translation Application Using Tkinter and OpenAI
Use ChatGPT to Translate Your Text from Python
by [Khumbo Klein](https://www.pythonguis.com/authors/khumbo-klein/) Last updated Apr 04 Tkinter [ Example applications ](https://www.pythonguis.com/examples/)
[ Translator Application Assets ](https://downloads.pythonguis.com/translator-app-assets-ai.zip)
Translation tools have existed for many years and are incredibly useful if you're learning a new language or wanting to read foreign websites. One of the most popular tools is _Google Translate_ , but there is now another alternative: using OpenAI's ChatGPT tool to translate text.
In this tutorial, we'll build a desktop translator application to translate natural language using ChatGPT APIs. We'll be building the UI using the Tkinter library from the Python standard library:
![Example translation of text via OpenAI](https://www.pythonguis.com/static/examples/translator-app-tkinter-ai/translator-demo-ai.png) _Example translation of text via OpenAI_
Table of Contents
  * [Installing the Required Packages](https://www.pythonguis.com/examples/translator-app-tkinter-ai-chatgpt/#installing-the-required-packages)
  * [Building the Window](https://www.pythonguis.com/examples/translator-app-tkinter-ai-chatgpt/#building-the-window)
  * [Creating the GUI for the Translator App](https://www.pythonguis.com/examples/translator-app-tkinter-ai-chatgpt/#creating-the-gui-for-the-translator-app)
  * [Getting a List of Languages](https://www.pythonguis.com/examples/translator-app-tkinter-ai-chatgpt/#getting-a-list-of-languages)
    * [Adding the Interface](https://www.pythonguis.com/examples/translator-app-tkinter-ai-chatgpt/#adding-the-interface)
  * [Building the Input UI](https://www.pythonguis.com/examples/translator-app-tkinter-ai-chatgpt/#building-the-input-ui)
  * [Getting an OpenAI API Key](https://www.pythonguis.com/examples/translator-app-tkinter-ai-chatgpt/#getting-an-openai-api-key)
  * [Implementing the Translation Functionality](https://www.pythonguis.com/examples/translator-app-tkinter-ai-chatgpt/#implementing-the-translation-functionality)
  * [Conclusion](https://www.pythonguis.com/examples/translator-app-tkinter-ai-chatgpt/#conclusion)


## Installing the Required Packages
Our _Translator_ uses the `openai` library to perform the actual translation via OpenAI's ChatGPT tool. Tkinter is already available in the standard library.
The first task will be to set up a Python [virtual environment](https://www.pythonguis.com/tutorials/python-virtual-environments/). Open the terminal, and run the following commands:
  * Windows
  * macOS/Linux


bat ```
> mkdir translator
> cd translator
> python -m venv venv
> .\venv\Scripts\activate
> python -m pip install openai

```

sh ```
$ mkdir translator
$ cd translator/
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install openai

```

Working through these instructions, first we create a root directory for the _Translator_ app. Next we create and activate a Python virtual environment for the project. Finally, we install the `openai` package.
Next, create a file named `translator.py` in the root of your project. Also add a folder called `images/` where you'll store the icons for the application. The folder structure should look like this:
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
python ```
translator/
│
├── images/
│  ├── arrow.png
│  └── logo.png
│
└── translator.py

```

The images for this project can be [downloaded here](https://downloads.pythonguis.com/translator-app-assets-ai.zip).
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
Importing `tkinter` under the alias `tk` is a common convention in Tkinter code.
Inside the class we define the `__init__()` method, which handles initialization of the class. In this method, we first call the initializer `__init__()` of the parent class, `tk.Tk`, to initialize the app's window. Then, we set the window's title using the `title()` method. To make the window unresizable, we use the `resizable()` method with `width` and `height` set to `False`.
At the bottom of the code, we have the `if __name__ == "__main__"` idiom to check whether the file is being run directly as an executable program. Inside the condition block we first create an instance of `TranslatorApp` and then run the application's main loop or event loop.
If you run this code, you'll get an empty Tkinter window on your desktop:
python ```
$ python translator.py

```

![The empty Tkinter window](https://www.pythonguis.com/static/examples/translator-app-tkinter-ai/empty-window.png) _The empty Tkinter window_
## Creating the GUI for the Translator App
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

The `setup_ui()` method will define the application's GUI. In this method, we first create a frame widget using the `tk.Frame` class whose `master` argument is set to `self` (the application's main window). Next, we position the frame inside the main window using the `pack()` geometry manager, using `padx` and `pady` arguments to set some padding around the frame.
Finally, we add the call to `self.setup_ui()` to the `__init__()` method.
We'll continue to develop the UI by adding code to the `setup_ui()` method.
Net, we'll add the app's logo. In the `setup_ui()` method add the following code below the `frame` definition:
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
    self.logo = tk.PhotoImage(file="images/logo.png")
    tk.Label(frame, image=self.logo).grid(row=0, column=0, sticky="w")

if __name__ == "__main__":
  app = TranslatorApp()
  app.mainloop()

```

This code loads the logo using the `tk.PhotoImage` class. To resize it, we use the `subsample()` method. Then, we add the logo to the frame using a `tk.Label` widget. The label takes the frame and the logo as arguments. Finally, to position the logo, we use the `grid()` geometry manager with appropriate values for the `row`, `column`, and `sticky` arguments.
The `sticky` argument determines which side of a cell the widget should align -- North (top), South (bottom), East (right) or West (left). Here we're aligning it on the Wiest or left of the cell with `"w"`:
![Tkinter window with the OpenAI logo in it](https://www.pythonguis.com/static/examples/translator-app-tkinter-ai/window-with-logo.png) _Tkinter window with the OpenAI logo in it_
## Getting a List of Languages
We need list of languages to shown in the dropdown. There are various lists available online. But since we're using OpenAI for the translations, why not use it to give us the list of languages too. Since this is just for testing purposes, lets grab the top 20 human languages (by first and second language speakers).
We can prompt ChatGPT with something like:
> Give me a list of the top 20 human languages with the most first and second language speakers in Python list format
..and it will return the following list:
python ```
languages = [
  "English",
  "Mandarin Chinese",
  "Hindi",
  "Spanish",
  "French",
  "Standard Arabic",
  "Bengali",
  "Russian",
  "Portuguese",
  "Urdu"
]

```

I'm going to add Dutch to the list, because it's my second language. Feel free to add your own languages to the list.
### Adding the Interface
Let's start adding some inputs to the UIs. First we'll create the language selection drop down boxes:
python ```
import tkinter as tk
import tkinter.ttk as ttk
LANGUAGES = [
  "English",
  "Mandarin Chinese",
  "Hindi",
  "Spanish",
  "French",
  "Standard Arabic",
  "Bengali",
  "Russian",
  "Portuguese",
  "Urdu",
  "Dutch", # Gekoloniseerd.
]

DEFAULT_SOURCE = "English"
DEFAULT_DEST = "Dutch"

class TranslatorApp(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Language Translator")
    self.resizable(width=False, height=False)
    self.setup_ui()
  def setup_ui(self):
    frame = tk.Frame(self)
    frame.pack(padx=10, pady=10)
    self.logo = tk.PhotoImage(file="images/logo.png")
    tk.Label(frame, image=self.logo).grid(row=0, column=0, sticky="w")
    # Source language combobox
    self.from_language = ttk.Combobox(frame, values=LANGUAGES)
    self.from_language.current(LANGUAGES.index(DEFAULT_SOURCE))
    self.from_language.grid(row=1, column=0, sticky="we")
    # Arrow icon
    self.arrows = tk.PhotoImage(file="images/arrow.png").subsample(15, 15)
    tk.Label(frame, image=self.arrows).grid(row=1, column=1)
    # Destination language combobox
    self.to_language = ttk.Combobox(frame, values=LANGUAGES)
    self.to_language.current(LANGUAGES.index(DEFAULT_DEST))
    self.to_language.grid(row=1, column=2, sticky="we")

if __name__ == "__main__":
  app = TranslatorApp()
  app.mainloop()

```

We have added our language list as the constant `LANGUAGES`. We also define the default languages for when the application starts up, using constants `DEFAULT_SOURCE` and `DEFAULT_DEST`.
Next, we create two combo boxes to hold the list of source and destination languages. The combo boxes are created using the `ttk.Combobox` class. One to the left and another to the right. Between the combo boxes, we've also added an arrow icon loaded using the `tk.PhotoImage` class. Again, we've added the icon to the app's window using `ttk.Label`.
Both combo boxes take `frame` and `values` as arguments. The `values` argument populates the combo boxes with languages. To specify the default language, we use the `current()` method, looking up the position of our default languages in the `languages` list with `.index()`.
To position the combo boxes inside the frame, we use the `grid()` geometry manager with the appropriate arguments. Run the application, and you will see the following window: 
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
![Source and destination languages](https://www.pythonguis.com/static/examples/translator-app-tkinter-ai/source-destination-languages.png) _Source and destination languages_
With the source and destination combo boxes in place, let's add three more widgets: two scrollable text widgets and a button. The scrollable text on the left will hold the source text, while the scrollable text on the right will hold the translated text. The button will allow us to run the actual translation.
## Building the Input UI
Get back to the code editor and update the `setup_ui()` method as follows. Note that we also need to import the `ScrollText` class:
python ```
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
LANGUAGES = [
  "English",
  "Mandarin Chinese",
  "Hindi",
  "Spanish",
  "French",
  "Standard Arabic",
  "Bengali",
  "Russian",
  "Portuguese",
  "Urdu",
  "Dutch",
]

DEFAULT_SOURCE = "English"
DEFAULT_DEST = "Dutch"

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
    # Source language combobox
    languages = [lang.title() for lang in LANGUAGES.values()]
    self.from_language = ttk.Combobox(frame, values=languages)
    self.from_language.current(languages.index(DEFAULT_SOURCE))
    self.from_language.grid(row=1, column=0, sticky="we")
    # Arrow icon
    self.arrows = tk.PhotoImage(file="images/arrow.png").subsample(15, 15)
    tk.Label(frame, image=self.arrows).grid(row=1, column=1)
    # Destination language combobox
    self.to_language = ttk.Combobox(frame, values=languages)
    self.to_language.current(languages.index(DEFAULT_DEST))
    self.to_language.grid(row=1, column=2, sticky="we")
    # Source text
    self.from_text = ScrolledText(
      frame,
      font=("Dotum", 16),
      width=50,
      height=20,
    )
    self.from_text.grid(row=2, column=0)
    # Translated text
    self.to_text = ScrolledText(
      frame,
      font=("Dotum", 16),
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
To position all these widgets on the app's window, we use the `grid()` geometry manager. Now, the app will look something like the following:
![Translator app's GUI](https://www.pythonguis.com/static/examples/translator-app-tkinter-ai/translator-finished-gui.png) _Translator app's GUI_
Our translation app's GUI is ready! Finally, we can start adding functionality to the application.
## Getting an OpenAI API Key
You can use OpenAPI's APIs for free, with some limitations. To get an OpenAI API key you will need to [create an account](https://platform.openai.com/signup/). Once you have created an account go ahead and get an [API key](https://platform.openai.com/api-keys).
Click "Create new secret key" in the top right hand corner to create a key. Give the key a name (it doesn't matter what you use) and then click "Create secret key". **Copy** the resulting key and keep it safe. You'll need it in the next step.
## Implementing the Translation Functionality
We'll implement the language translation functionality in the `translate()` method. This gets the current text from the UI and then uses `openai` to perform the translation. We need a few more imports, and to create the OpenAI client instance at the top of the application:
python ```
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showerror
from tkinter.scrolledtext import ScrolledText
import httpcore
from openai import OpenAI
client = OpenAI(
  api_key="<YOUR API KEY HERE>"
)

```

Here we've imported the `showerror` helper for displaying error boxes in our application. We've imported `httpcore` which we'll use to handle HTTP errors when accessing the API. Finally, we've added an import for the `OpenAI` class from `openai`. This is what handles the actual translation.
To use it, we create an instance of the class as `OpenAI`. Replace `<YOUR API KEY HERE>` with the API key you generated on OpenAI just now.
We'll continue by implementing the `translate()` method. Below we're just showing the function itself:
python ```

class TranslatorApp(tk.Tk):
  # ...
  def translate(self):
    source_language = self.from_language.get()
    destination_language = self.to_language.get()
    text = self.from_text.get(1.0, tk.END).strip()
    try:
      completion = client.chat.completions.create(
        messages=[
          {"role": "system", "content": "You are a language interpreter."},
          {
            "role": "user",
            "content": (
              f"Translate the following text from {source_language} "
              f"to {destination_language}, only reply with the text: "
              f"{text}"
            ),
          },
        ],
        model="gpt-3.5-turbo",
      )
      reply = completion.choices[0].message.content
    except httpcore.ConnectError:
      showerror(
        title="Error",
        message="Make sure you have an internet connection",
      )
      return
    except Exception as e:
      showerror(
        title="Error",
        message=f"An unexpected error occurred: {e}",
      )
      return
    self.to_text.config(state="normal")
    self.to_text.delete(1.0, tk.END)
    self.to_text.insert(tk.END, reply)
    self.to_text.config(state="disabled")

```

The `translate()` method handles the entire translation process. It starts by retrieving the source and destination languages from the corresponding combo boxes, and the input text from the box on the left.
If any of these are not defined, we use a `showerror` dialog to inform the user of the problem.
Once we have the source and destination language and some text to translate, we can perform the actual translation through ChatGPT. First, we give the language model a hint about what we want it to do -- interpret language:
python ```
  {"role": "system", "content": "You are a language interpreter."},

```

Next we build the message we want it to respond to. We ask it to translate the provided text from the source to destination language, and to respond with _only_ the translated text. If we don't specify this, we'll get some additional description or context.
You might want to experiment with asking for the text _and_ context separately, as that is often helpful when learning languages.
python ```
  {
    "role": "user",
    "content": (
      f"Translate the following text from {source_language} "
      f"to {destination_language}, only reply with the text: "
      f"{text}"
    ),
  },

```

The created completion is submitted to the API and we can retrieve the resulting text from the object:
python ```
reply = completion.choices[0].message.content

```

If the call to `translate()` finds a connection error, then we tell the user to check their internet connection. To handle any other exceptions, we catch the generic `Exception` class and display an error message with the exception details.
If the translation is successful, then we enable the destination scrolled area, display the translated text, and disable the area again so it remains read-only.
The complete final code is shown below:
python ```
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showerror
from tkinter.scrolledtext import ScrolledText
import httpcore
from openai import OpenAI
client = OpenAI(
  api_key="<YOUR API KEY HERE>"
)
LANGUAGES = [
  "English",
  "Mandarin Chinese",
  "Hindi",
  "Spanish",
  "French",
  "Standard Arabic",
  "Bengali",
  "Russian",
  "Portuguese",
  "Urdu",
  "Dutch",
]
DEFAULT_SOURCE = "English"
DEFAULT_DEST = "Dutch"

class TranslatorApp(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Language Translator")
    self.resizable(width=False, height=False)
    self.setup_ui()
  def setup_ui(self):
    frame = tk.Frame(self)
    frame.pack(padx=10, pady=10)
    self.logo = tk.PhotoImage(file="images/logo.png")
    tk.Label(frame, image=self.logo).grid(row=0, column=0, sticky="w")
    # Source language combobox
    self.from_language = ttk.Combobox(frame, values=LANGUAGES)
    self.from_language.current(LANGUAGES.index(DEFAULT_SOURCE))
    self.from_language.grid(row=1, column=0, sticky="we")
    # Arrow icon
    self.arrows = tk.PhotoImage(file="images/arrow.png").subsample(15, 15)
    tk.Label(frame, image=self.arrows).grid(row=1, column=1)
    # Destination language combobox
    self.to_language = ttk.Combobox(frame, values=LANGUAGES)
    self.to_language.current(LANGUAGES.index(DEFAULT_DEST))
    self.to_language.grid(row=1, column=2, sticky="we")
    # Source text
    self.from_text = ScrolledText(
      frame,
      font=("Dotum", 16),
      width=50,
      height=20,
    )
    self.from_text.grid(row=2, column=0)
    # Translated text
    self.to_text = ScrolledText(
      frame,
      font=("Dotum", 16),
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
    source_language = self.from_language.get()
    destination_language = self.to_language.get()
    text = self.from_text.get(1.0, tk.END).strip()
    try:
      completion = client.chat.completions.create(
        messages=[
          {"role": "system", "content": "You are a language interpreter."},
          {
            "role": "user",
            "content": (
              f"Translate the following text from {source_language} "
              f"to {destination_language}, only reply with the text: "
              f"{text}"
            ),
          },
        ],
        model="gpt-3.5-turbo",
      )
      reply = completion.choices[0].message.content
    except httpcore.ConnectError:
      showerror(
        title="Error",
        message="Make sure you have an internet connection",
      )
      return
    except Exception as e:
      showerror(
        title="Error",
        message=f"An unexpected error occurred: {e}",
      )
      return
    self.to_text.config(state="normal")
    self.to_text.delete(1.0, tk.END)
    self.to_text.insert(tk.END, reply)
    self.to_text.config(state="disabled")

if __name__ == "__main__":
  app = TranslatorApp()
  app.mainloop()


```

The finished app is shown below:
![The completed Translator app](https://www.pythonguis.com/static/examples/translator-app-tkinter-ai/translator-demo-ai.png) _The completed Translator app_
## Conclusion
In this tutorial we built a Translator application using the Tkinter GUI library from the Python standard library. We worked step by step through building the UI using a grid layout, and then implemented the language translation functionality with `openai` & ChatGPT.
Try and take what you've learnt in this tutorial & applying it to your own projects! 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Khumbo Klein](https://www.pythonguis.com/static/theme/images/authors/khumbo-klein.jpg)](https://www.pythonguis.com/authors/khumbo-klein/)
**Build a Translation Application Using Tkinter and OpenAI** was written by [Khumbo Klein](https://www.pythonguis.com/authors/khumbo-klein/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) and [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
**Build a Translation Application Using Tkinter and OpenAI** was published in [examples](https://www.pythonguis.com/examples/) on September 05, 2024 (updated April 04, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[tkinter](https://www.pythonguis.com/topics/tkinter/) [translator](https://www.pythonguis.com/topics/translator/) [ai](https://www.pythonguis.com/topics/ai/) [chatgpt](https://www.pythonguis.com/topics/chatgpt/) [translation](https://www.pythonguis.com/topics/translation/) [tk](https://www.pythonguis.com/topics/tk/)
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
