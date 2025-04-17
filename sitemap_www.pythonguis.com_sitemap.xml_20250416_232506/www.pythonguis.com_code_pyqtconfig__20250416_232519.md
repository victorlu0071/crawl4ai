# Content from: https://www.pythonguis.com/code/pyqtconfig/

[](https://www.pythonguis.com/code/pyqtconfig/#menu)
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
# PyQtConfig
A simple API for keeping your PyQt Widgets and config in sync
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Mar 17 [ Code & snippet library ](https://www.pythonguis.com/code/)
PyQtConfig: a simple API for handling, persisting and synchronising configuration within PyQt applications. This module was built initially as part of the Pathomx data analysis platform but spun out into a standalone module when it became clear it was quite useful.
This post gives a brief overview of the API features and use. It is still in development so suggestions, comments, [bug reports and pull-requests](https://github.com/mfitzp/pyqtconfig) are very welcome.
![Demo of config setting with widgets #1](https://www.pythonguis.com/static/code/pyqtconfig/demo-1.png)
## Features
  * consistent interface to read values from widgets, always `get` and `set`
  * seamlessly handle conversion of types from QSettings strings
  * integrated mapping handles conversions between display and internal settings, e.g. nice text in combo boxes to integer values
  * save and load configuration via `dict` (to JSON) or `XML`
  * [open source](https://github.com/mfitzp/pyqtconfig) and BSD licensed


## Introduction
The core of the API is a `ConfigManager` instance that holds configuration settings (either as a Python dict, or a QSettings instance) and provides standard methods to `get` and `set` values.
Configuration parameters can have Qt widgets attached as _handlers_. Once attached the widget and the configuration value will be kept in sync. Setting the value on the `ConfigManager` will update any attached widgets and changes to the value on the widget will be reflected immmediately in the `ConfigManager`. Qt signals are emitted on each update.
Default values can be set and will be returned transparently if a parameter remains unset. The current state of config can be saved and reloaded via XML or exported to a flat dict.
A small application has been included in PyQtConfig to demonstrate these features (interaction with widgets requires a running QApplication). Go to the pyqtconfig install folder and run it with: 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
python ```
python -m pyqtconfig.demo

```

![Demo of config setting with widgets #2](https://www.pythonguis.com/static/code/pyqtconfig/demo-2.png)
![Demo of config setting with widgets #3](https://www.pythonguis.com/static/code/pyqtconfig/demo-3.png)
![Demo of config setting with widgets #4](https://www.pythonguis.com/static/code/pyqtconfig/demo-4.png)
![Demo of config setting with widgets #4](https://www.pythonguis.com/static/code/pyqtconfig/demo-5.png)
## Simple usage (dictionary)
To store your settings you need to create a `ConfigManager` instance. This consists of a settings dictionary, a default settings dictionary and a number of helper functions to handle setting, getting and other functions.
python ```
from pyqtconfig import ConfigManager
config = ConfigManager()
config.set_defaults({
  'number': 13,
  'text': 'hello',
  'array': ['1','2'],
  'active': True,
})

```

Before values are set the default value will be returned when queried.
python ```
config.get('number')
13
config.set('number', 42)
config.get('number')
42

```

## Simple usage (QSettings)
The `QSettingsManager` provides exactly the same API as the standard `QConfigManager`, the only difference is in the storage of values.
python ```
from pyqtconfig import QSettingsManager
settings = QSettingsManager()
settings.set('number', 42)
settings.set('text', "bla")
settings.set('array', ["a", "b"])
settings.set('active', True)
settings.get('number')
>> 42

```

On some platforms, versions of Qt, or Qt APIs QSettings will return strings for all values which can lead to complicated code and breakage. However, PyQtConfig is smart enough to use the `type` of the config parameter in defaults to auto-convert returned values.
However, you do not have to set defaults manually. As of v0.7 default values are auto-set when attaching widgets (handlers) to the config manager _if they're not already set_.
From this point on we'll be referring to the `ConfigManager` class only, but all features work identically in `QSettingsManager`.
## Adding widget handlers
So far we could have achieved the same thing with a standard Python dict/QSettings object. The real usefulness of PyQtConfig is in the ability to interact with QWidgets maintaining synchronisation between widgets and internal config, and providing a simple standard interface to retrieve values.
It's difficult to demonstrate the functionality since you need a running QApplication to make it work, and you can't do that in the interactive interpreter. The examples that follow are contrived outputs that you would see _if it were possible to do that_. For a real example, see the demo included in the package.
python ```
lineEdit = QtGui.QLineEdit()
config.add_handler('text', lineEdit)
checkbox = QtGui.QCheckBox('active')
config.add_handler('active', checkbox)

```

![Demo of config setting with widgets #2](https://www.pythonguis.com/static/code/pyqtconfig/demo-6.png)
The values of the widgets are automatically set to the pre-set defaults. Note that if we hadn't pre-set a default value the _reverse_ would happen, and the default would be set to the value in the widget. This allows you to define the defaults in either way. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Next we'll change the value of both widgets.
We can read out the values of the widgets via the `ConfigManager` using the standard `get` interface rather than using the widget-specific access functions.
python ```
config.get('text')
>> 'hello'
config.get('active')
>> True

```

We can also update the widgets via the `ConfigManager` using `set`.
python ```
config.set('text', 'new value')
config.set('active', False)

```

![Demo of config setting with widgets #2](https://www.pythonguis.com/static/code/pyqtconfig/demo-7.png)
## Mapping
Sometimes you want to display a different value in a widget than you store in the configuration. The most obvious example would be in a combo box where you want to list nice descriptive names, but want to store short names or numbers in the configuration.
To enable this PyQtConfig allows a `mapper` to be defined when attaching a widget to a config. Mappers are provided as tuple of 2 functions `set` and `get` that each perform the conversion required when setting and getting the value from the widget. To simplify map creation however you can also specify the mapping as a dict and PyQtConfig will create the necessary lambdas behind the scenes.
python ```
CHOICE_A = 1
CHOICE_B = 2
CHOICE_C = 3
CHOICE_D = 4
map_dict = {
  'Choice A': CHOICE_A,
  'Choice B': CHOICE_B,
  'Choice C': CHOICE_C,
  'Choice D': CHOICE_D,
}
config.set_default('combo', CHOICE_C)
config.get('combo')
>> 3
comboBox = QtGui.QComboBox()
comboBox.addItems( map_dict.keys() )
config.add_handler('combo', comboBox, mapper=map_dict)

```

![Demo of config setting with widgets #2](https://www.pythonguis.com/static/code/pyqtconfig/demo-8.png)
Note how the config is set to `3` (the value of `CHOICE_C`) but displays "Choice C" as text.
## Saving and loading data
`QSettingsManager` uses a `QSettings` object as a config store and so the saving of configuration is automatic through the Qt APIs. However, if you're using `ConfigManager` you will need another approach to load and save your settings (note that these functions are also available in `QSettingsManager` if you want them).
The simplest access is to output the stored data as a `dict` using `as_dict()`.
python ```
config.as_dict()

```

This dict contains all values in the internal dictionary, with defaults used where values are not set. You can take this dict and set the defaults on a new `ConfigManager` to persist state.
python ```
config2 = ConfigManager()
config2.set_defaults( config.as_dict() )
config2.get('combo')
>> 3

```

You can also export and import data as XML. The two functions for handling XML import take an `ElementTree` root element and search for config settings under `Config/ConfigSetting`. This allows you to use PyQtConfig to write config into an XML file without worrying about the format.
python ```
import ElementTree as et
config.set('combo', CHOICE_D)
root = et.Element("MyXML")
root = config.getXMLConfig( root )
config2.setXMLConfig(root)
config2.get('combo')
>> 4

```

## Finishing up
Hope you find PyQtConfig useful in your PyQt projects. Let me know if you have any comments, suggestions, [bug reports and pull-requests](https://github.com/mfitzp/pyqtconfig).
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PyQtConfig** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/code/pyqtconfig/Python books) on the subject. 
**PyQtConfig** was published in [code](https://www.pythonguis.com/code/) on November 21, 2014 (updated March 17, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[pyqtconfig](https://www.pythonguis.com/topics/pyqtconfig/) [qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [python](https://www.pythonguis.com/topics/python/) [software](https://www.pythonguis.com/topics/software/) [programming](https://www.pythonguis.com/topics/programming/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
