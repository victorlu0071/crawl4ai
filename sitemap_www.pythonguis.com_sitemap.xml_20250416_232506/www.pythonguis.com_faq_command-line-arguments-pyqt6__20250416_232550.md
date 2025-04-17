# Content from: https://www.pythonguis.com/faq/command-line-arguments-pyqt6/

[](https://www.pythonguis.com/faq/command-line-arguments-pyqt6/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
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
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Handle command-line arguments with PyQt6/PySide6
Allow users to customize your application at launch
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Mar 15 [ FAQ ](https://www.pythonguis.com/faq/)
Sometimes you want to be able to pass command line arguments to your GUI applications. For example, you may want to be able to pass files which the application should open, or change the initial startup state.
In that case it can be helpful to be able to pass custom command-line arguments to your application. Qt supports this using the `QCommandLineOption` and `QCommandLineParser` classes, the first defining optional parameters to be identified from the command line, and the latter to actually perform the parsing.
In this short tutorial we'll create a small demo application which accepts arguments on the command line.
## Building the Parser
We'll start by creating an outline of our application. As usual we create a `QApplication` instance, however, we won't initially create any windows. Instead, we construct our command-line parser function, which accepts our app instance and uses `QCommandLineParser` to parse the command line arguments.
  * PyQt6
  * PySide6


python ```
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QCommandLineOption, QCommandLineParser
def parse(app):
  """Parse the arguments and options of the given app object."""
  parser = QCommandLineParser()
  parser.addHelpOption()
  parser.addVersionOption()
  parser.process(app)

app = QApplication(sys.argv)
app.setApplicationName("My Application")
app.setApplicationVersion("1.0")
parse(app)

```

python ```
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QCommandLineOption, QCommandLineParser
def parse(app):
  """Parse the arguments and options of the given app object."""
  parser = QCommandLineParser()
  parser.addHelpOption()
  parser.addVersionOption()
  parser.process(app)

app = QApplication(sys.argv)
app.setApplicationName("My Application")
app.setApplicationVersion("1.0")
parse(app)

```

We don't call `app.exec()` yet, to start the event loop. That's because we don't have any windows, so there would be no way to exit the app once it is started! We'll create the windows in a later step.
It is important to note that you _must_ pass `sys.argv` to `QApplication` for the command line parser to work -- the parser processes the arguments from app. If you don't pass the arguments, there won't be anything to process.
With this outline structure in place we can move on to creating our command line options. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
## Adding Optional Parameters
We'll add two _optional_ parameters -- the first to allow users to toggle the window start up as maximized, and the second to pass a Qt style to use for drawing the window.
The available styles are 'windows', 'windowsvista', 'fusion' and 'macos' -- although the platform specific styles are only available on their own platform. If you use `macos` on Windows, or vice versa, it will have no effect. However, 'fusion' can be used on all platforms.
  * PyQt6
  * PySide6


python ```
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QCommandLineOption, QCommandLineParser
QT_STYLES = ["windows", "windowsvista", "fusion", "macos"]
def parse(app):
  """Parse the arguments and options of the given app object."""
  parser = QCommandLineParser()
  parser.addHelpOption()
  parser.addVersionOption()
  maximize_option = QCommandLineOption(
    ["m", "maximize"],
    "Maximize the window on startup."
  )
  parser.addOption(maximize_option)
  style_option = QCommandLineOption(
    "s",
    "Use the specified Qt style, one of: " + ', '.join(QT_STYLES),
    "style"
  )
  parser.addOption(style_option)
  parser.process(app)

app = QApplication(sys.argv)
app.setApplicationName("My Application")
app.setApplicationVersion("1.0")
parse(app)
app.exec()

```

python ```
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QCommandLineOption, QCommandLineParser
QT_STYLES = ["windows", "windowsvista", "fusion", "macos"]
def parse(app):
  """Parse the arguments and options of the given app object."""
  parser = QCommandLineParser()
  parser.addHelpOption()
  parser.addVersionOption()
  maximize_option = QCommandLineOption(
    ["m", "maximize"],
    "Maximize the window on startup."
  )
  parser.addOption(maximize_option)
  style_option = QCommandLineOption(
    "s",
    "Use the specified Qt style, one of: " + ', '.join(QT_STYLES),
    "style"
  )
  parser.addOption(style_option)
  parser.process(app)

app = QApplication(sys.argv)
app.setApplicationName("My Application")
app.setApplicationVersion("1.0")
parse(app)
app.exec()

```

The _optional_ arguments are now in place. We'll now add positional arguments, which will be used to open specific files.
## Adding Positional Arguments
Strictly speaking, positional arguments are any arguments not interpreted as optional arguments. You can define multiple positional arguments if you like but this is only used for help text display. You will still need to handle them yourself internally, and limit the number if necessary by throwing an error.
In our example we are specifying a single position argument `file`, but noting in the help text that you can provide more than one. There is no limit in our example -- if you pass more files, more windows will open.
  * PyQt6
  * PySide6


python ```
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QCommandLineOption, QCommandLineParser
QT_STYLES = ["windows", "windowsvista", "fusion", "macos"]
def parse(app):
  """Parse the arguments and options of the given app object."""
  parser = QCommandLineParser()
  parser.addHelpOption()
  parser.addVersionOption()
  parser.addPositionalArgument("file", "Files to open.", "[file file file...]")
  maximize_option = QCommandLineOption(
    ["m", "maximize"],
    "Maximize the window on startup."
  )
  parser.addOption(maximize_option)
  style_option = QCommandLineOption(
    "s",
    "Use the specified Qt style, one of: " + ', '.join(QT_STYLES),
    "style"
  )
  parser.addOption(style_option)
  parser.process(app)
  has_maximize_option = parser.isSet(maximize_option)
  app_style = parser.value(style_option)
  # Check for positional arguments (files to open).
  arguments = parser.positionalArguments()
  print("Has maximize option?", has_maximize_option)
  print("App style:", app_style)
  print("Arguments (files): ", arguments)
app = QApplication(sys.argv)
app.setApplicationName("My Application")
app.setApplicationVersion("1.0")
parse(app)
app.exec()

```

python ```
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QCommandLineOption, QCommandLineParser
QT_STYLES = ["windows", "windowsvista", "fusion", "macos"]
def parse(app):
  """Parse the arguments and options of the given app object."""
  parser = QCommandLineParser()
  parser.addHelpOption()
  parser.addVersionOption()
  parser.addPositionalArgument("file", "Files to open.", "[file file file...]")
  maximize_option = QCommandLineOption(
    ["m", "maximize"],
    "Maximize the window on startup."
  )
  parser.addOption(maximize_option)
  style_option = QCommandLineOption(
    "s",
    "Use the specified Qt style, one of: " + ', '.join(QT_STYLES),
    "style"
  )
  parser.addOption(style_option)
  parser.process(app)
  has_maximize_option = parser.isSet(maximize_option)
  app_style = parser.value(style_option)
  # Check for positional arguments (files to open).
  arguments = parser.positionalArguments()
  print("Has maximize option?", has_maximize_option)
  print("App style:", app_style)
  print("Arguments (files): ", arguments)
app = QApplication(sys.argv)
app.setApplicationName("My Application")
app.setApplicationVersion("1.0")
parse(app)
app.exec()

```

We've added a series of `print` calls to display the arguments and options extracted by Qt's `QCommandLineParser`. If you run the application now you can experiment by passing different arguments and seeing the result on the command line.
For example --- with no arguments.
bash ```
$ python command_line.py
Has maximize option? False
App style:

```

With `-m` maximize flag and a single file
bash ```
$ python command_line.py -m example.txt
Has maximize option? True
App style:
Arguments (files): ['example.txt']

```

With a single file and using _Fusion_ style -- there is no window yet, so this will have effect yet!
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
bash ```
$ python command_line.py -s fusion example.txt
Has maximize option? False
App style: fusion
Arguments (files): ['example.txt']

```

With the argument handling in place, we can now write the remainder of the example.
## Using the Arguments & Options
We'll be using a standard `QPlainTextEdit` widget as our file viewer. In Qt any widget without a parent is a window, so these editors will be floating independently on the desktop. If the `-m` flag is used we'll set these windows to be displayed maximized.
If windows are created, we'll need to start the Qt _event loop_ to draw the windows and allow interaction with them. If no windows are created, we'll want to show the command-line help to help the user understand why nothing is happening! This will output the format of position and optional arguments that our app takes.
  * PyQt6
  * PySide6


python ```
import sys
from PySide6.QtWidgets import QApplication, QPlainTextEdit
from PySide6.QtCore import QCommandLineOption, QCommandLineParser
QT_STYLES = ["windows", "windowsvista", "fusion", "macos"]
windows = [] # Store references to our created windows.
def parse(app):
  """Parse the arguments and options of the given app object."""
  parser = QCommandLineParser()
  parser.addHelpOption()
  parser.addVersionOption()
  parser.addPositionalArgument("file", "Files to open.", "[file file file...]")
  maximize_option = QCommandLineOption(
    ["m", "maximize"],
    "Maximize the window on startup."
  )
  parser.addOption(maximize_option)
  style_option = QCommandLineOption(
    "s",
    "Use the specified Qt style, one of: " + ', '.join(QT_STYLES),
    "style"
  )
  parser.addOption(style_option)
  parser.process(app)
  has_maximize_option = parser.isSet(maximize_option)
  app_style = parser.value(style_option)
  if app_style and app_style in QT_STYLES:
    app.setStyle(app_style)
  # Check for positional arguments (files to open).
  arguments = parser.positionalArguments()
  # Iterate all arguments and open the files.
  for tfile in arguments:
    try:
      with open(tfile, 'r') as f:
        text = f.read()
    except Exception:
      # Skip this file if there is an error.
      continue
    window = QPlainTextEdit(text)
    # Open the file in a maximized window, if set.
    if has_maximize_option:
      window.showMaximized()
    # Keep a reference to the window in our global list, to stop them
    # being deleted. We can test this list to see whether to show the
    # help (below) or start the event loop (at the bottom).
    windows.append(window)
  if not windows:
    # If we haven't created any windows, show the help.
    parser.showHelp()

app = QApplication(sys.argv)
app.setApplicationName("My Application")
app.setApplicationVersion("1.0")
parse(app)
if windows:
  # We've created windows, start the event loop.
  app.exec()

```

python ```
import sys
from PySide6.QtWidgets import QApplication, QPlainTextEdit
from PySide6.QtCore import QCommandLineOption, QCommandLineParser
QT_STYLES = ["windows", "windowsvista", "fusion", "macos"]
windows = [] # Store references to our created windows.
def parse(app):
  """Parse the arguments and options of the given app object."""
  parser = QCommandLineParser()
  parser.addHelpOption()
  parser.addVersionOption()
  parser.addPositionalArgument("file", "Files to open.", "[file file file...]")
  maximize_option = QCommandLineOption(
    ["m", "maximize"],
    "Maximize the window on startup."
  )
  parser.addOption(maximize_option)
  style_option = QCommandLineOption(
    "s",
    "Use the specified Qt style, one of: " + ', '.join(QT_STYLES),
    "style"
  )
  parser.addOption(style_option)
  parser.process(app)
  has_maximize_option = parser.isSet(maximize_option)
  app_style = parser.value(style_option)
  if app_style and app_style in QT_STYLES:
    app.setStyle(app_style)
  # Check for positional arguments (files to open).
  arguments = parser.positionalArguments()
  # Iterate all arguments and open the files.
  for tfile in arguments:
    try:
      with open(tfile, 'r') as f:
        text = f.read()
    except Exception:
      # Skip this file if there is an error.
      continue
    window = QPlainTextEdit(text)
    # Open the file in a maximized window, if set.
    if has_maximize_option:
      window.showMaximized()
    # Keep a reference to the window in our global list, to stop them
    # being deleted. We can test this list to see whether to show the
    # help (below) or start the event loop (at the bottom).
    windows.append(window)
  if not windows:
    # If we haven't created any windows, show the help.
    parser.showHelp()

app = QApplication(sys.argv)
app.setApplicationName("My Application")
app.setApplicationVersion("1.0")
parse(app)
if windows:
  # We've created windows, start the event loop.
  app.exec()

```

The arguments are handled and processed as before however, now they actually have an effect!
Firstly, if the user passes the `-s <style>` option we will apply the specified style to our app instance -- first checking to see if it is one of the known valid styles.
python ```
if app_style and app_style in QT_STYLES:
  app.setStyle(app_style)

```

Next we take the list of position arguments and iterate, creating a `QPlainTextEdit` window and displaying the text in it. If `has_maximize_option` has been set, these windows are all set to be maximized with `window.showMaximized()`.
References to the windows are stored in a global list `windows`, so they are not cleaned up (deleted) on exiting the function. After creating windows we test to see if this is empty, and if not show the help:
bash ```
$ python command_line.py
Usage: command_line.py [options] [file file file...]
Options:
 -?, -h, --help Displays help on commandline options.
 --help-all   Displays help including Qt specific options.
 -v, --version  Displays version information.
 -m, --maximize Maximize the window on startup.
 -s <style>   Use the specified Qt style, one of: windows, windowsvista,
         fusion, macos
Arguments:
 file      Files to open.

```

If there _are_ windows, we finally start up the event loop to display them and allow the user to interact with the application.
python ```
if windows:
  # We've created windows, start the event loop.
  app.exec()

```

## Conclusion
In this short tutorial we've learned how to develop an app which accepts custom arguments and options on the command line, and uses them to modify the UI behavior. You can use this same approach in your own applications to provide command-line control over the behavior of your own applications. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Handle command-line arguments with PyQt6/PySide6** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) with contributions from [Boštjan Mejak](https://www.pythonguis.com/authors/bostjan-mejak/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/command-line-arguments-pyqt6/Python books) on the subject. 
**Handle command-line arguments with PyQt6/PySide6** was published in [faq](https://www.pythonguis.com/faq/) on March 15, 2023 . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [qt6](https://www.pythonguis.com/topics/qt6/) [app](https://www.pythonguis.com/topics/app/) [command-line](https://www.pythonguis.com/topics/command-line/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/)
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
