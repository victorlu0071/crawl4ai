# Content from: https://www.pythonguis.com/faq/qapplication-sysargv-command-line-arguments/

[](https://www.pythonguis.com/faq/qapplication-sysargv-command-line-arguments/#menu)
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
# Q&A: Why do I need to pass sys.argv or [] when creating an instance of QApplication?
Using command-line arguments to configure Qt
by [Boštjan Mejak](https://www.pythonguis.com/authors/bostjan-mejak/) Last updated Mar 11 [ FAQ ](https://www.pythonguis.com/faq/)
The `QApplication` object is the core of every Qt Widgets application. Every application needs one and only one `QApplication` object to function. This object starts and holds the main _event loop_ of your application which governs all user interaction with the GUI.
When developing applications with _PyQt_ or _PySide_ you will have created an instance of `QApplication` like in the example below, passing in `sys.argv` or an empty list `[]`.
  * PySide6
  * PyQt6


python ```
import sys
from PySide6.QtWidgets import QApplication
app = QApplication(sys.argv)
# or: app = QApplication([])

```

python ```
import sys
from PyQt6.QtWidgets import QApplication
app = QApplication(sys.argv)
# or: app = QApplication([])

```

While this works, you may have asked yourself: what is the meaning of `sys.argv` or the empty list `[]` and _why_ do you need to pass it to `QApplication`?
## What is `sys.argv`?
When your application starts, `sys.argv` contains the _arguments_ used to launch your application. If you start a _Python_ application from the command line, `sys.argv` will contain the name of your _Python_ script file as the first entry.
The name `argv` is an abbreviation of _argument vector_. This name originates from the C programming language, where "vector" is the name used for a dynamic array or `list`.
For example, see the example command line below:
bash ```
python argtest.py

```

When executing this script `sys.argv` will contain the list `['argtest.py']`. Anything further you add to the end of the command above will be appended to `sys.argv`.
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
To see this in action create the following simple _Python_ script and save it under the name `argtest.py`.
python ```
import sys
print("Arguments:", sys.argv)

```

Now, run your `argtest.py` script from the command line and experiment with passing in your own arguments. For example, the following command line:
bash ```
python argtest.py --info

```

...will output...
bash ```
Arguments: ['argtest.py', '--info']

```

As you can see, the `--info` command-line argument is retrieved from `sys.argv`, beside the filename of the _Python_ script.
Command-line arguments are split on spaces, so anything separated with a space will be treated as a new argument. To pass arguments that include spaces, you need to wrap those in quotes.
When we pass `sys.argv` to `QApplication` we are passing the command-line arguments to _Qt_. This allows us to pass any configuration settings to _Qt_ at the startup of an application.
## What command-line arguments are available?
_Qt_ provides some built-in command-line arguments which are also available in _PyQt_ and _PySide_. 
### _Qt_ -specific command-line arguments
  * `--platform` _platformName[:options]_ Specifies the _Qt Platform Abstraction_ (QPA) plugin. This overrides the _QT_QPA_PLATFORM_ environment variable.


This is commonly used when developing applications on the Raspberry Pi to redirect Qt output to a linux framebuffer device (e.g. a custom screen) without using XWindows. For example, `-platform linuxfb:fb=/dev/fb1`
  * `--platformpluginpath` _path_ Specifies the path to platform plugins. This overrides the _QT_QPA_PLATFORM_PLUGIN_PATH_ environment variable.
  * `--platformtheme` _theme_ Specifies the platform theme. This overrides the _QT_QPA_PLATFORMTHEME_ environment variable.
  * `--plugin` _plugin_ Specifies additional plugins to load. The _plugin_ value may be passed multiple times. This is concatenated with the plugins in the _QT_QPA_GENERIC_PLUGINS_ environment variable.
  * `--qmljsdebugger` _value_ Activates the QML/JavaScript debugger with a specified port passed as _value_. The _value_ must be of format `port:1234[,block]`, where _block_ is optional and will make the application wait until a debugger connects to it. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
  * `--qwindowgeometry` _geometry_ Specifies a geometry for the main window using the _X11_ syntax which should be passed like `--qwindowgeometry` _100x100+50+50_.
  * `--qwindowicon` _icon_ Sets the default icon of a window.
  * `--qwindowtitle` _title_ Sets a title of the first window.
  * `--reverse` Sets the application's layout direction to `Qt.RightToLeft`. This option is intended to aid debugging and should not be used in production. The default value is automatically detected from the system's locale.
  * `--session` _session_ Restores the application from an earlier session.


### General command-line arguments
  * `-h` or `--help` or `-?` Displays help on all the general command-line arguments, including this one. Note that the `-?` argument is only available on Windows.
  * `--help-all` Displays what `--help` does plus all the _Qt_ -specific command-line arguments.
  * `-v` or `--version` Displays the version of an application.


## Do I need to pass `sys.argv`?
No. While passing `sys.argv` allows you to pass command-line configuration through to _Qt_ at the startup of your application, if you don't need or want to _prevent_ configuration of _Qt_ from the command line, you can instead either pass an empty list `[]` (using _PyQt6_ , _PyQt5_ , _PySide2_) or nothing at all (using _PySide6_).
python ```
# PyQt6
import sys
from PyQt6.QtWidgets import QApplication
app = QApplication([])

```

python ```
# PySide6
import sys
from PySide6.QtWidgets import QApplication
app = QApplication()

```

If you do not pass `sys.argv`, you are not forwarding command-line arguments to _Qt_. Therefore, you can not customize _Qt_ 's behavior from the command line. 
## Conclusion
Passing `sys.argv` to `QApplication` at startup allows you to customize the behavior of _Qt_ from the command-line. If you don't want to pass command-line arguments to _Qt_ you can skip passing `sys.argv` and instead pass nothing (_PySide6_) or `[]` (other _PyQt_ or _PySide_ versions).
Be sure to double check if you need any of Qt's command-line configuration — for example, you're developing for Raspberry Pi — before disabling this behavior. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Boštjan Mejak](https://www.pythonguis.com/static/theme/images/authors/bostjan-mejak.jpg)](https://www.pythonguis.com/authors/bostjan-mejak/)
**Q &A: Why do I need to pass sys.argv or [] when creating an instance of QApplication?** was written by [Boštjan Mejak](https://www.pythonguis.com/authors/bostjan-mejak/) with contributions from [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Boštjan Mejak has been developing Python apps for about ten years. He started with Tkinter, then switched to wxPython, PyQt, and recently to PySide. 
**Q &A: Why do I need to pass sys.argv or [] when creating an instance of QApplication?** was published in [faq](https://www.pythonguis.com/faq/) on July 07, 2022 (updated March 11, 2023) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [qt](https://www.pythonguis.com/topics/qt/) [qt6](https://www.pythonguis.com/topics/qt6/) [qapplication](https://www.pythonguis.com/topics/qapplication/) [sys](https://www.pythonguis.com/topics/sys/) [argv](https://www.pythonguis.com/topics/argv/) [arguments](https://www.pythonguis.com/topics/arguments/) [python](https://www.pythonguis.com/topics/python/)
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
