# Content from: https://www.pythonguis.com/faq/qsettings-usage/

[](https://www.pythonguis.com/faq/qsettings-usage/#menu)
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
# QSettings Usage
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
PedanticHacker | 2021-04-30 23:12:04 UTC | #1
@martin, would you be willing to document the usage of `QSettings`? Maybe in your book, or here.
I haven't found any good information while roaming throughout the Internet. Well, I have some rough ideas, but I want to know how to use `QSettings` by having a dialog window (with radio buttons and all that) and have that to serve the purpose of a settings UI and then have `QSettings` to serve the purpose of a settings manager. I'm having a hard time putting those two things together to work in concert.
PedanticHacker | 2021-04-09 09:37:25 UTC | #2
I don't want to introduce another dependency in my application by using [pyqtconfig](https://github.com/learnpyqt/pyqtconfig). I'd like to master `QSettings` and make them work in concert with my custom settings dialog. A little help would be very welcome.
So far, I have implemented this API to handle loading and saving the settings:
python ```
from PyQt6.QtCore import QSettings

class SettingsManager:
  """Create a settings manager for the SuperChess application."""
  def __init__(self):
    self.settings = QSettings("SuperChess", "settings")
  def load(self):
    """Manage loading all the settings."""
    self.settings.value("engine white")
  def save(self):
    """Manage saving all the settings."""
    is_engine_white_checked = settings_dialog.engine_white.isChecked()
    self.settings.beginGroup("chess engine");
    self.settings.setValue("engine white", is_engine_white_checked)
    self.settings.endGroup()

```

And this is an implementation of my custom settings dialog: 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
python ```
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QGroupBox, QRadioButton, QVBoxLayout

class SettingsDialog(QDialog):
  """Create a settings dialog to edit all the settings of the application."""
  def __init__(self):
    super().__init__()
    self.set_attributes()
    self.create_elements()
    self.set_layout()
    self.connect_signals_to_slots()
  def set_attributes(self):
    """
    Set attributes to the settings dialog.
    Move the settings dialog to the top left corner and give it a title.
    """
    self.move(0, 0)
    self.setWindowTitle("Settings")
  def create_elements(self):
    """Create groups of radio buttons as settings elements."""
    self.engine_settings = QGroupBox("Chess engine")
    self.engine_black = QRadioButton(text="Plays as Black")
    self.engine_black.setChecked(True)
    self.engine_white = QRadioButton(text="Plays as White")
    self.engine_white.setChecked(False)
    _buttons = QDialogButtonBox.StandardButtons
    self.button_box = QDialogButtonBox(_buttons.Ok | _buttons.Cancel)
  def set_layout(self):
    """Set a layout for the settings elements."""
    _engine_settings_vertical_layout = QVBoxLayout()
    _engine_settings_vertical_layout.addWidget(self.engine_white)
    _engine_settings_vertical_layout.addWidget(self.engine_black)
    self.engine_settings.setLayout(_engine_settings_vertical_layout)
    _window_vertical_layout = QVBoxLayout()
    _window_vertical_layout.addWidget(self.engine_settings)
    _window_vertical_layout.addWidget(self.button_box)
    self.setSizePolicy(attributes.minimum_size_policy)
    self.setLayout(_window_vertical_layout)
  def connect_signals_to_slots(self):
    """Execute the proper action when a signal is emitted."""
    self.button_box.accepted.connect(self.accept)
    self.button_box.rejected.connect(self.reject)

```

I can't seem to hook this up in my application. By hooking up, I mean to use the value (True or False) of a settings element so that my application responds according to it. How can I do that?
martin | 2021-04-14 18:27:29 UTC | #3
To use the value, you can read it back out of your settings object in your application, using `.value()`. You'll need to make sure you're using the same `QSettings` instance to write and read to. But also, unfortunately, there is no way to know that a setting has been updated (another thing I added to pyqtconfig!)
A very rough workaround is to connect (using signals) anything that might be affected by a dialog setting change, to update after the dialog has been OKd. For example, add a `settings_changed` /`xxxx_settings_changed` (if you have settings groups) signal to your settings manager. If you ensure this signal is emitted after the modified settings have been written then things should work OK.
The downside is that this could potentially update/refresh a lot of things that don't need it, but as long as the dialog is fairly related stuff it should be OK.
martin | 2021-04-15 07:19:11 UTC | #4
Here's a more complete working example. This creates a window with a pushbutton to show a settings dialog, and a text display of the current setting state. The dialog uses the _settings manager_ to set the initial state of it's widgets, and when the dialog is accepted, the value fo those widgets is written back to settings.
![Screenshot 2021-04-15 at 09.18.38|560x499](https://www.pythonguis.com/static/faq/forum/qsettings-usage/aoa81eODreMhT0jutfuULtXgO62.png)
The manager has a custom signal to notify the application that the settings have been saved (you could also check explicitly for changes).
The mapping from widgets to the settings is handled as described above (same as in pyqtconfig basically). The settings are stored using `QSettings` and will persist between runs of the application -- edit the settings, shutdown and restart, and they will be as you left them.
python ```
from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QDialog, QApplication, QVBoxLayout, QGroupBox, QRadioButton, QDialogButtonBox
from PyQt6.QtCore import QSettings, pyqtSignal, QObject
class SettingsManager(QObject):
  """Create a settings manager for the SuperChess application."""
  widget_mappers = {
    'QCheckBox': ('checkState', 'setCheckState'),
    'QLineEdit': ('text', 'setText'),
    'QSpinBox': ('value', 'setValue'),
    'QRadioButton': ('isChecked', 'setChecked'),
  }
  settings_changed = pyqtSignal()
  def __init__(self):
    super().__init__()
    self.settings = QSettings("MyApp", "settings")
  def update_widgets_from_settings(self, map):
    for name, widget in map.items():
      cls = widget.__class__.__name__
      getter, setter = self.widget_mappers.get(cls, (None, None))
      value = self.settings.value(name)
      print("load:", getter, setter, value)
      if setter and value is not None:
        fn = getattr(widget, setter)
        fn(value) # Set the widget.
  def update_settings_from_widgets(self, map):
    for name, widget in map.items():
      cls = widget.__class__.__name__
      getter, setter = self.widget_mappers.get(cls, (None, None))
      print("save:", getter, setter)
      if getter:
        fn = getattr(widget, getter)
        value = fn()
        print("-- value:", value)
        if value is not None:
          self.settings.setValue(name, value) # Set the settings.
    # Notify watcher of changed settings.
    self.settings_changed.emit()

# Define this in another module, import to use.
settings_manager = SettingsManager()

class SettingsDialog(QDialog):
  """Create a settings dialog to edit all the settings of the application."""
  def __init__(self):
    super().__init__()
    """Create groups of radio buttons as settings elements."""
    self.player = QGroupBox("Player")
    self.player_name = QLineEdit()
    self.engine = QGroupBox("Chess engine")
    self.engine_black = QRadioButton(text="Plays as Black")
    self.engine_black.setChecked(True)
    self.engine_white = QRadioButton(text="Plays as White")
    self.engine_white.setChecked(False)
    _buttons = QDialogButtonBox.StandardButtons
    self.button_box = QDialogButtonBox(_buttons.Ok | _buttons.Cancel)
    self.button_box.accepted.connect(self.accept)
    self.button_box.rejected.connect(self.reject)
    slayout = QVBoxLayout()
    slayout.addWidget(self.player)
    slayout.addWidget(self.player_name)
    slayout.addWidget(self.engine)
    slayout.addWidget(self.engine_white)
    slayout.addWidget(self.engine_black)
    slayout.addWidget(self.button_box)
    self.setLayout(slayout)
    self.map = {
      'player': self.player_name,
      'black': self.engine_black,
      'white': self.engine_white
    }
    self.load_settings()
    self.accepted.connect(self.save_settings)
  def load_settings(self):
    """ Reload the settings from the settings store """
    settings_manager.update_widgets_from_settings(self.map)

  def save_settings(self):
    """ Triggered when the dialog is accepted; copys settings values to the settings manager """
    settings_manager.update_settings_from_widgets(self.map)

class MainWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.button = QPushButton("Press for settings")
    self.label = QLabel()
    self.button.pressed.connect(self.edit_settings)
    settings_manager.settings_changed.connect(self.update_label)
    self.update_label()
    layout = QVBoxLayout()
    layout.addWidget(self.button)
    layout.addWidget(self.label)
    self.setLayout(layout)
  def edit_settings(self):
    dlg = SettingsDialog()
    dlg.exec()
  def update_label(self):
    data = {
      'player': settings_manager.settings.value('player'),
      'white': settings_manager.settings.value('white'),
      'black': settings_manager.settings.value('black'),
    }
    self.label.setText(str(data))

app = QApplication([])
w = MainWindow()
w.show()
app.exec()

```

Now I just need to write the article ;)
PedanticHacker | 2021-04-19 11:52:47 UTC | #5
python ```
Traceback (most recent call last):
 File "C:\Users\Boštjan\Desktop\SuperChess\superchess.py", line 85, in <module>
  app_instance.run()
 File "C:\Users\Boštjan\Desktop\SuperChess\superchess.py", line 70, in run
  from source.frontend.main.window import main_window
 File "C:\Users\Boštjan\Desktop\SuperChess\source\frontend\main\window.py", line 32, in <module>
  from source.frontend.settings.dialog import settings_dialog
 File "C:\Users\Boštjan\Desktop\SuperChess\source\frontend\settings\dialog.py", line 99, in <module>
  settings_dialog = SettingsDialog()
 File "C:\Users\Boštjan\Desktop\SuperChess\source\frontend\settings\dialog.py", line 38, in __init__
  self.create_elements()
 File "C:\Users\Boštjan\Desktop\SuperChess\source\frontend\settings\dialog.py", line 68, in create_elements
  self.load()
 File "C:\Users\Boštjan\Desktop\SuperChess\source\frontend\settings\dialog.py", line 91, in load
  settings_manager.update_widgets_from_settings(self.map)
 File "C:\Users\Boštjan\Desktop\SuperChess\source\backend\settings\manager.py", line 40, in update_widgets_from_settings
  function(value)
TypeError: setChecked(self, bool): argument 1 has unexpected type 'str'

```

I get this error because of `cls = widget.__class__.__name__`. The `__name__` part is the culprit. This should be `cls = widget.__class__` in both instances.
martin | 2021-04-19 13:16:51 UTC | #6
The name is used for the lookup into the `widget_mappers` dictionary (with the string keys), so would need to be a string for it work, unless you change that too. If you don't, it will just never match. The idea is to avoid needing to import all the classes just to map them.
python ```
>>> from PyQt5.QtWidgets import QApplication, QLabel
>>> app = QApplication([])
>>> l = QLabel()
>>> l.__class__.__name__
'QLabel'

```

The error you're seeing shows that it's trying to call `setChecked` with a string in this block
python ```
      value = self.settings.value(name)
      print("load:", getter, setter, value)
      if setter and value is not None:
        fn = getattr(widget, setter)
        fn(value) # Set the widget.

```

...which suggests that a string has got into the matching value slot in your Qt settings object. What's the value of _value_ you're seeing alongside the load (just before the error). For checkboxes the value should be a bool.
PedanticHacker | 2021-04-19 18:29:01 UTC | #7
This is how my `SettingsManager` class looks like now:
python ```
from PyQt6.QtCore import pyqtSignal, QObject, QSettings

class SettingsManager(QObject):
  """Create a settings manager for the SuperChess application."""
  settings_changed = pyqtSignal()
  widget_mappers = {"QRadioButton": ("isChecked", "setChecked")}
  def __init__(self):
    """Initialize the SettingsManager object."""
    super().__init__()
    self.settings = QSettings("SuperChess", "settings")
  def update_widgets_from_settings(self, map):
    """Docstring."""
    for name, widget in map.items():
      widget_name = widget.__class__.__name__
      getter, setter = self.widget_mappers.get(widget_name, (None, None))
      value = self.settings.value(name)
      if setter and value is not None:
        function = getattr(widget, setter)
        function(value)
  def update_settings_from_widgets(self, map):
    """Docstring."""
    for name, widget in map.items():
      widget_name = widget.__class__.__name__
      getter, setter = self.widget_mappers.get(widget_name, (None, None))
      if getter:
        function = getattr(widget, getter)
        value = function()
        if value is not None:
          self.settings.setValue(name, value)
    self.settings_changed.emit()

settings_manager = SettingsManager()

```

And my `SettingsDialog` class looks like this:
python ```
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import (QDialog, QDialogButtonBox, QGroupBox,
               QRadioButton, QVBoxLayout)
from source.backend.game.manager import game_manager
from source.backend.app.resources import app_resources
from source.backend.settings.manager import settings_manager

LOGO_ICON = QIcon("source/frontend/icons/logo.svg")

class SettingsDialog(QDialog):
  """Create a settings dialog to edit SuperChess settings."""
  def __init__(self):
    """Initialize the SettingsDialog object."""
    super().__init__()
    self.set_attributes()
    self.create_elements()
    self.set_layout()
    self.connect_signals_with_slots()
  def set_attributes(self):
    """
    Set attributes to the settings dialog.
    Move the settings dialog to the top left corner, give it a logo
    icon depicting a bare chessboard and apply a style.
    """
    self.move(0, 0)
    self.setWindowIcon(LOGO_ICON)
    self.setWindowTitle("Settings")
    self.setStyleSheet(app_resources.default_style)
  def create_elements(self):
    """Create groups of radio buttons as settings elements."""
    self.engine_settings = QGroupBox("Chess engine")
    self.engine_black = QRadioButton(text="Plays as Black")
    self.engine_black.setChecked(True)
    self.engine_white = QRadioButton(text="Plays as White")
    self.engine_white.setChecked(False)
    _buttons = QDialogButtonBox.StandardButtons
    self.button_box = QDialogButtonBox(_buttons.Ok | _buttons.Cancel)
    self.map = {game_manager.engine_turn: self.engine_black,
          game_manager.engine_turn: self.engine_white}
    self.load()
  def set_layout(self):
    """Set a layout for the settings elements."""
    _engine_settings_vertical_layout = QVBoxLayout()
    _engine_settings_vertical_layout.addWidget(self.engine_white)
    _engine_settings_vertical_layout.addWidget(self.engine_black)
    self.engine_settings.setLayout(_engine_settings_vertical_layout)
    _window_vertical_layout = QVBoxLayout()
    _window_vertical_layout.addWidget(self.engine_settings)
    _window_vertical_layout.addWidget(self.button_box)
    self.setSizePolicy(app_resources.minimum_size_policy)
    self.setLayout(_window_vertical_layout)
  def connect_signals_with_slots(self):
    """Connect signals with appropriate slots/methods."""
    self.accepted.connect(self.save)
    self.button_box.accepted.connect(self.accept)
    self.button_box.rejected.connect(self.reject)
  def load(self):
    """Manage loading all the SuperChess settings."""
    settings_manager.update_widgets_from_settings(self.map)
  @pyqtSlot()
  def save(self):
    """Manage saving all the SuperChess settings."""
    settings_manager.update_settings_from_widgets(self.map)

settings_dialog = SettingsDialog()

```

Now I get a new error:
python ```
Traceback (most recent call last):
 File "C:\Users\Boštjan\Desktop\SuperChess\superchess.py", line 85, in <module>
  app_instance.run()
 File "C:\Users\Boštjan\Desktop\SuperChess\superchess.py", line 70, in run
  from source.frontend.main.window import main_window
 File "C:\Users\Boštjan\Desktop\SuperChess\source\frontend\main\window.py", line 32, in <module>
  from source.frontend.settings.dialog import settings_dialog
 File "C:\Users\Boštjan\Desktop\SuperChess\source\frontend\settings\dialog.py", line 100, in <module>
  settings_dialog = SettingsDialog()
 File "C:\Users\Boštjan\Desktop\SuperChess\source\frontend\settings\dialog.py", line 39, in __init__
  self.create_elements()
 File "C:\Users\Boštjan\Desktop\SuperChess\source\frontend\settings\dialog.py", line 69, in create_elements
  self.load()
 File "C:\Users\Boštjan\Desktop\SuperChess\source\frontend\settings\dialog.py", line 92, in load
  settings_manager.update_widgets_from_settings(self.map)
 File "C:\Users\Boštjan\Desktop\SuperChess\source\backend\settings\manager.py", line 37, in update_widgets_from_settings
  value = self.settings.value(name)
TypeError: value(self, str, defaultValue: Any = None, type: type = None): argument 1 has unexpected type 'bool'

```

Am I missing something in my code?
martin | 2021-04-19 19:03:53 UTC | #8
[quote="PedanticHacker, post:7, topic:846"]
python ```
self.map = {game_manager.engine_turn: self.engine_black,
          game_manager.engine_turn: self.engine_white}

```

[/quote]
In this block, the map keys must be strings -- these are the _names_ used to refer to the value in `QSettings`. They need to be unique (it's just a Python dictionary).
python ```
>>> {'a':1,'a':2,'b':3}
{'a': 2, 'b': 3}

```

For a radio like this you can maybe just store the checked state from one of the two radio buttons -- they're automatically exclusive. Setting either to true/false should set the other.
If you want those values to then be available in the manager, you'll need either
  1. another mechanism to do that, e.g. use the `settings_changed` signal to trigger a method which copies the values over.
  2. user `@property` on the values you want to get from settings


For the 2nd, e.g. on `game_manager`.
python ```
@property
def engine_turn(self):
  return 'black' if settings.settings.value('engine_turn') else 'white'

```

PedanticHacker | 2021-04-19 20:39:26 UTC | #9
I'll try this.
But, uhm, is it possible I implement the recommended approach by using `setValue` and `value` methods? Can you give me some hint based on my code?
PedanticHacker | 2021-04-20 00:16:06 UTC | #10
So since `game_manager` is an instance of my `GameManager` class -- does my group need to be defined like this:
python ```
settings = QSettings("SuperChess", "settings")
...
settings.beginGroup("game_manager")
settings.setValue("engine_turn", False)
settings.endGroup()

```

or
python ```
settings.beginGroup("GameManager")
settings.setValue("engine_turn", False)
settings.endGroup()

```

Does the name of a group really matter or must it be named after a widget's name (the name of the class or the name of its instance)? What about the value names? After what must those be named (if it even matters)?
I really don't understand how should I put this all together. And I want to do it like [THESE](https://doc.qt.io/qt-6/qsettings.html#beginGroup) docs say. Reading from the widgets seems like a hack to me. I really am pedantic and wanna have clean code.
Properly implementing `QSettings` is a really tough son of a b****, at least for me.
martin | 2021-04-20 06:12:31 UTC | #11
This is using value methods the line `settings.settings.value('engine_turn')` is retrieving that value from the `QSettings` object. `QSettings` is just a key-value store, it doesn't update your widgets for you or modify other objects -- you have to do that yourself.
martin | 2021-04-20 06:21:55 UTC | #12 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
I think there is a misunderstanding here -- `QSettings` is just a key-value store (like a dictionary), that is persisted in a platform-dependent way. It doesn't do anything else. The _groups_ you create are just conceptual "folders" in which to contain a bunch of related settings. (If you're on Windows, take a look in the registry to see how the values are stored -- it'll be under your defined organisation/app name -- the groups are folders I think).
`QSettings` doesn't do anything for you to update your widgets, or modify other variables in your application. If you want to store values you need to call `setValue` on the settings object, and to read it call `value` with the key name.
To store the state of the widgets, you need to read them -- there is no other way. But to properly decouple things, you can read the value, put it in your settings object and then read from the settings object elsewhere (like in the example using `@property` -- that reads from settings, not the widget).
fyi You might prefer to subclass `SettingsManager` from `QSettings`, or add the `.value()` and `.setValue()` methods on it to avoid the `settings.settings.` when you use it. If you re-implement `.setValue()` you can also fire your updated signal.
PedanticHacker | 2021-04-23 08:49:46 UTC | #15
I'm trying a million things. Now my settings dialog is
python ```
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot, QSettings
from PyQt6.QtWidgets import (QDialog, QDialogButtonBox, QGroupBox,
               QRadioButton, QVBoxLayout)
from source.backend.app.resources import app_resources

LOGO_ICON = QIcon("source/frontend/icons/logo.svg")

class SettingsDialog(QDialog):
  """Create a settings dialog to edit SuperChess settings."""
  def __init__(self):
    """Initialize the SettingsDialog object."""
    super().__init__()
    self.set_attributes()
    self.create_elements()
    self.set_layout()
    self.connect_signals_with_slots()
    self.load()
  def set_attributes(self):
    """
    Set attributes to the settings dialog.
    Move the settings dialog to the top left corner, give it a logo
    icon depicting a bare chessboard and apply a style.
    """
    self.move(0, 0)
    self.setWindowIcon(LOGO_ICON)
    self.setWindowTitle("Settings")
    self.setStyleSheet(app_resources.default_style)
  def create_elements(self):
    """Create groups of radio buttons as settings elements."""
    self.settings = QSettings("SuperChess", "settings")
    self.engine_settings = QGroupBox("Chess engine")
    self.engine_black = QRadioButton(text="Plays as Black")
    self.engine_black.setChecked(True)
    self.engine_white = QRadioButton(text="Plays as White")
    self.engine_white.setChecked(False)
    okay_button = QDialogButtonBox.StandardButtons.Ok
    cancel_button = QDialogButtonBox.StandardButtons.Cancel
    self.button_box = QDialogButtonBox(okay_button | cancel_button)
  def set_layout(self):
    """Set a layout for the settings elements."""
    _engine_settings_vertical_layout = QVBoxLayout()
    _engine_settings_vertical_layout.addWidget(self.engine_white)
    _engine_settings_vertical_layout.addWidget(self.engine_black)
    self.engine_settings.setLayout(_engine_settings_vertical_layout)
    _window_vertical_layout = QVBoxLayout()
    _window_vertical_layout.addWidget(self.engine_settings)
    _window_vertical_layout.addWidget(self.button_box)
    self.setSizePolicy(app_resources.minimum_size_policy)
    self.setLayout(_window_vertical_layout)
  def connect_signals_with_slots(self):
    """Connect signals with appropriate slots/methods."""
    self.button_box.accepted.connect(self.save)
    self.button_box.rejected.connect(self.reject)
  def load(self):
    """Manage loading all the SuperChess settings."""
    self.settings.value("black", defaultValue=True, type=bool)
    self.settings.value("white", defaultValue=False, type=bool)
  @pyqtSlot()
  def save(self):
    """Manage saving all the SuperChess settings."""
    self.settings.beginGroup("chess engine")
    self.settings.setValue("black", self.engine_black.isChecked())
    self.settings.setValue("white", self.engine_white.isChecked())
    self.settings.endGroup()
    self.accept()

settings_dialog = SettingsDialog()

```

I basically merged my settings dialog with my settings manager.
PedanticHacker | 2021-04-23 09:10:58 UTC | #16
The persisting issue I have is that by clicking the `Cancel` button in my settings dialog after changes were made, the changed settings (radio buttons states changed) are not discarded. So when I reopen the settings dialog, I see radio buttons in the same states as they were left before, even though the `Cancel` button was clicked.
@martin, how can I implement my settings dialog to do the right thing?
martin | 2021-04-27 12:06:25 UTC | #17
Hey hey, sorry for the delay been busy on a few things!
The key thing is that you shouldn't persist the data to the settings store until the dialog is accepted. In my earlier example I did that by connecting the `update_settings_from_widgets` method to the dialogs `.accept` signal -- that only fires when the dialog is accepted. It shouldn't run in any other case.
Below is an updated version which also handles properly typing the values returned from settings.
python ```
from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QDialog, QApplication, QVBoxLayout, QGroupBox, QRadioButton, QDialogButtonBox
from PyQt6.QtCore import QSettings, pyqtSignal, QObject
class SettingsManager(QSettings):
  """Create a settings manager for the SuperChess application."""
  widget_mappers = {
    'QCheckBox': ('checkState', 'setCheckState', bool),
    'QLineEdit': ('text', 'setText', str),
    'QSpinBox': ('value', 'setValue', int),
    'QRadioButton': ('isChecked', 'setChecked', bool),
  }
  settings_changed = pyqtSignal()
  def __init__(self):
    super().__init__()
    self.settings = QSettings("MyApp", "settings")
    print("Settings file located at:", self.settings.fileName())
  def update_widgets_from_settings(self, map):
    for name, widget in map.items():
      cls = widget.__class__.__name__
      getter, setter, dtype = self.widget_mappers.get(cls, (None, None))
      value = self.settings.value(name, type=dtype)
      print("load:", getter, setter, value, type(value), dtype)
      if setter and value is not None:
        fn = getattr(widget, setter)
        try:
          fn(value) # Set the widget.
        except Exception as e:
          print(e) # handle type error
  def update_settings_from_widgets(self, map):
    for name, widget in map.items():
      cls = widget.__class__.__name__
      getter, setter, dtype = self.widget_mappers.get(cls, (None, None))
      print("save:", getter, setter)
      if getter:
        fn = getattr(widget, getter)
        value = fn()
        print("-- value:", value, type(value), dtype)
        if value is not None:
          self.settings.setValue(name, value) # Set the settings.
    # Notify watcher of changed settings.
    self.settings_changed.emit()

# Define this in another module, import to use.
settings = SettingsManager()

class SettingsDialog(QDialog):
  """Create a settings dialog to edit all the settings of the application."""
  def __init__(self):
    super().__init__()
    """Create groups of radio buttons as settings elements."""
    self.player = QGroupBox("Player")
    self.player_name = QLineEdit()
    self.engine = QGroupBox("Chess engine")
    self.engine_black = QRadioButton(text="Plays as Black")
    self.engine_black.setChecked(True)
    self.engine_white = QRadioButton(text="Plays as White")
    self.engine_white.setChecked(False)
    _buttons = QDialogButtonBox.StandardButtons
    self.button_box = QDialogButtonBox(_buttons.Ok | _buttons.Cancel)
    self.button_box.accepted.connect(self.accept)
    self.button_box.rejected.connect(self.reject)
    slayout = QVBoxLayout()
    slayout.addWidget(self.player)
    slayout.addWidget(self.player_name)
    slayout.addWidget(self.engine)
    slayout.addWidget(self.engine_white)
    slayout.addWidget(self.engine_black)
    slayout.addWidget(self.button_box)
    self.setLayout(slayout)
    self.map = {
      'player': self.player_name,
      'black': self.engine_black,
      'white': self.engine_white
    }
    self.load_settings()
    self.accepted.connect(self.save_settings)
  def load_settings(self):
    """ Reload the settings from the settings store """
    settings.update_widgets_from_settings(self.map)

  def save_settings(self):
    """ Triggered when the dialog is accepted; copys settings values to the settings manager """
    settings.update_settings_from_widgets(self.map)

class MainWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.button = QPushButton("Press for settings")
    self.label = QLabel()
    self.button.pressed.connect(self.edit_settings)
    settings.settings_changed.connect(self.update_label)
    self.update_label()
    layout = QVBoxLayout()
    layout.addWidget(self.button)
    layout.addWidget(self.label)
    self.setLayout(layout)
  def edit_settings(self):
    dlg = SettingsDialog()
    dlg.exec()
  def update_label(self):
    data = {
      'player': settings.value('player'),
      'white': settings.value('white'),
      'black': settings.value('black'),
    }
    self.label.setText(str(data))

app = QApplication([])
w = MainWindow()
w.show()
app.exec()

```

The important line is here (and that save_settings isn't called anywhere else!)
python ```
self.accepted.connect(self.save_settings)

```

If we run this you can see that the settings aren't saved unless I press OK.
https://vimeo.com/540626816
> I basically merged my settings dialog with my settings manager.
I wouldn't recommend that, as you're then mixing your GUI with non-GUI logic. In the code above I've turned the manager into a subclass of `QSettings` which simplifies things a bit. Ideally I'd recommend you putting your settings object definition in a file by itself, creating a single instance, and then importing it anywhere you need it in your app.
martin | 2021-04-23 12:18:26 UTC | #18
[quote="PedanticHacker, post:16, topic:846"] The persisting issue I have is that by clicking the `Cancel` button in my settings dialog after changes were made, the changed settings (radio buttons states changed) are not discarded. S [/quote]
This might also be because you've merged your dialog and settings object, the dialog is not being destroyed between views -- the widgets will remain in their previous state. If the update/setting the widgets from settings isn't working they will always appear to be "saved" (even though they're not).
PedanticHacker | 2021-04-29 08:18:38 UTC | #20
@martin, I've been playing with your code. I have some questions and unresolved issues.
1) I don't understand why the Python's built-in `map` function needs to be overshadowed. (`pylint` is nagging about it.)
2) Would you recommend I connect the `rejected` signal of my `QDialog` subclass (my `SettingsDialog`) with the `load_settings()` method? That's the only way the settings actually get loaded for me between views of the settings dialog. (My code currently doesn't do this, but I tried it and it worked.)
3) You said I could override the `setValue()` and `value()` methods of `QSettings`. Can you show how would **you** override the `setValue()` and `value()` methods in a `QSettings` subclass?
4) Is it really necessary I subclass my `SettingsManager` class from `QSettings`? (I don't see a point in that, other than for being able to override the aforementioned `setValue()` and `value()` methods.)
Here's the code of my settings manager:
python ```
from PyQt6.QtCore import QSettings

class SettingsManager:
  """Create a settings manager to handle all SuperChess settings."""
  widget_mappers = {"QCheckBox": ("isChecked", "setChecked", bool),
           "QRadioButton": ("isChecked", "setChecked", bool)}
  def __init__(self):
    """Use QSettings to create a repository of all the settings."""
    self.settings = QSettings("SuperChess", "settings")
  def update_widgets_from_settings(self, repository):
    """Get setting values to set widget states from them."""
    for setting_name, widget in repository.items():
      widget_name = widget.__class__.__name__
      getter, setter, data_type = self.widget_mappers.get(widget_name)
      setting_value = self.settings.value(setting_name, type=data_type)
      if setter and setting_value is not None:
        update_value = getattr(widget, setter)
        update_value(setting_value)
  def update_settings_from_widgets(self, repository):
    """Get widget states to set setting values from them."""
    for setting_name, widget in repository.items():
      widget_name = widget.__class__.__name__
      getter, setter, data_type = self.widget_mappers.get(widget_name)
      if getter:
        widget_state = getattr(widget, getter)
        setting_value = widget_state()
        if setting_value is not None:
          self.settings.setValue(setting_name, setting_value)

settings_manager = SettingsManager()

```

And here's the code of my settings dialog:
python ```
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import (QCheckBox, QDialog, QDialogButtonBox,
               QGroupBox, QRadioButton, QVBoxLayout)
from source.backend.settings.manager import settings_manager

LOGO_ICON = QIcon("source/frontend/icons/logo.svg")

class SettingsDialog(QDialog):
  """Create a settings dialog to edit all SuperChess settings."""
  def __init__(self):
    """Initialize the settings dialog."""
    super().__init__()
    self.set_attributes()
    self.engine_group = QGroupBox(title="Chess engine")
    self.engine_black = QRadioButton(text="Plays as Black")
    self.engine_black.setChecked(True)
    self.engine_white = QRadioButton(text="Plays as White")
    self.engine_white.setChecked(False)
    self.engine_pondering = QCheckBox(text="Pondering")
    self.engine_pondering.setChecked(False)
    okay_button = QDialogButtonBox.StandardButtons.Ok
    cancel_button = QDialogButtonBox.StandardButtons.Cancel
    self.button_box = QDialogButtonBox(okay_button | cancel_button)
    self.engine_layout = QVBoxLayout()
    self.engine_layout.addWidget(self.engine_black)
    self.engine_layout.addWidget(self.engine_white)
    self.engine_layout.addWidget(self.engine_pondering)
    self.engine_group.setLayout(self.engine_layout)
    self.dialog_layout = QVBoxLayout()
    self.dialog_layout.addWidget(self.engine_group)
    self.dialog_layout.addWidget(self.button_box)
    self.setLayout(self.dialog_layout)
    self.repository = {"engine/black": self.engine_black,
              "engine/white": self.engine_white,
              "engine/pondering": self.engine_pondering}
    self.accepted.connect(self.save_settings)
    self.button_box.accepted.connect(self.accept)
    self.button_box.rejected.connect(self.reject)
    self.load_settings()
  def set_attributes(self):
    """
    Set settings dialog attributes.
    Set a logo icon and a title.
    """
    self.setWindowIcon(LOGO_ICON)
    self.setWindowTitle("Settings")
  def load_settings(self):
    """Load the settings from the settings repository."""
    settings_manager.update_widgets_from_settings(self.repository)
  @pyqtSlot()
  def save_settings(self):
    """
    Save the settings if the user accepts the settings dialog.
    """
    settings_manager.update_settings_from_widgets(self.repository)

settings_dialog = SettingsDialog()

```

martin | 2021-04-30 23:05:44 UTC | #21
  1. Re: the map issue, you can name the variable anything you like. Call it `widget_map` or something similar -- I named it that because it's used to "map" from one thing to another. That was OK when it was `self.map` but should have renamed when reworked the code.
  2. Not sure about this: if the `load_settings` method is only being used to modify the values of the widgets in the dialog there is no point on calling it on reject, since you're closing the dialog. If you want to use it to update other widgets in your application you could do that -- but again, "rejecting" the dialog should always mean that no changes have taken place. So updates shouldn't be neccessary?
  3. This only really makes sense if your settings manager is a subclass of QSettings. It's just to give you the access to those methods, but also trigger the update signals (see below)
  4. It's not necessary, no. It just simplifies things a bit since all your settings related behaviour is handled by a single object & you can avoid needing to do settings_manager.settings.setValue(). You can also just implement the same interface, and pass the calls through if you like (see below)


python ```

class SettingsManager(QObject):
  settings_updated = pyqtSignal()
  def setValue(self, name, value):
    self.settings.setValue(name, value) # pass to settings on property
    # super().setValue(name, value) if using subclass of QSettings
    self.settings_updated.emit()

```

By doing this you can hook behaviours elsewhere in your app onto changes in settings (refresh something for example). To avoid unnecessary refresh/etc. you could pass the name of the updated setting too,.
```
PedanticHacker | 2021-05-06 13:14:47 UTC | #22
I still have a little issue. When I read the values from the settings, I must read it like this:
`settings_manager.settings.value("black", type=bool)`
If I don't pass the `type` argument, I don't get the `bool` type, I just get the `str` type with either `"true"` or `"false"`.
Also, I **must** do `settings_manager.settings.value`, since `settings_manager.value` doesn't work.
martin | 2021-05-06 17:18:07 UTC | #23
The need for the `type` is inconvenient (it's because the values are stored in ini files as text). In some ways writing your own storage with JSON/something is easier.
But you have a couple of options
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
  1. Keep a dictionary of "default" values on your settings manager. You can use these to set the initial values (in absence of a saved setting) but _also_ to get the correct type of any saved values -- since the type will be the same as the type of the default.
  2. When retrieving a value from settings first _get_ the value from the widget (e.g. via .value()) and use that get the type for the setting.


Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**QSettings Usage** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/qsettings-usage/Python books) on the subject. 
**QSettings Usage** was published in [faq](https://www.pythonguis.com/faq/) on April 05, 2021 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
