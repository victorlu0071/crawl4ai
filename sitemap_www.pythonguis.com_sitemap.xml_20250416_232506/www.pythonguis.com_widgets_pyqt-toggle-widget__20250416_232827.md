# Content from: https://www.pythonguis.com/widgets/pyqt-toggle-widget/

[](https://www.pythonguis.com/widgets/pyqt-toggle-widget/#menu)
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
# Toggle & AnimatedToggle
Toggle switch Widget QCheckBox replacement
by [Salem Al Bream](https://www.pythonguis.com/authors/salem-al-bream/) Last updated Jul 14 [ Python GUI Widget Library ](https://www.pythonguis.com/widgets/)
The standard `QCheckBox` widget provides a simple way to add toggleable options to your UI, mimicking a checkable box on a paper form. By clicking on the widget the user can toggle the widget on and off (in Qt is actually a 3rd semi-checked state).
This simple checkbox isn't always the best fit for a UI -- for example, if you have a definitive switch which controls an action, such as switching on/off a connection or device. In that case something that mimics an actual _switch_ may be better. Unfortunately, there is no such widget available in Qt itself.
This custom widget provides two alternative toggle switches for use in PyQt5 and PySide2 applications -- `Toggle` and `AnimatedToggle`. They are both a drop-in replacement for the standard `QCheckBox` and subclass from it, to provide an identical interface & signals. Both widgets can be customized to change the colors used for each element, and `AnimatedToggle` adds additional transition and pulse animations to give a more physical feel.
To use the widget install the `qtwidgets` Python library.
shell ```
pip3 install qtwidgets

```

You can then import the widget into your application using
python ```
from qtwidgets import Toggle

```

...or for the animated variant --
python ```
from qtwidgets import AnimatedToggle

```

This custom widget uses features covered in the [QPropertyAnimation](https://www.pythonguis.com/tutorials/qpropertyanimation/) and [bitmap graphics](https://www.pythonguis.com/tutorials/bitmap-graphics/) tutorials.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
There are [other widgets available](https://github.com/learnpyqt/python-qtwidgets) in the library too.
You can test the widget out using the following demo code.
  * PyQt5
  * PySide2


python ```
import PyQt5
from PyQt5 import QtWidgets
from qtwidgets import Toggle, AnimatedToggle
class Window(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    toggle_1 = Toggle()
    toggle_2 = AnimatedToggle(
      checked_color="#FFB000",
      pulse_checked_color="#44FFB000"
    )
    container = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(toggle_1)
    layout.addWidget(toggle_2)
    container.setLayout(layout)
    self.setCentralWidget(container)

app = QtWidgets.QApplication([])
w = Window()
w.show()
app.exec_()

```

python ```
import PySide2
from PySide2 import QtWidgets
from qtwidgets import Toggle, AnimatedToggle

class Window(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    toggle_1 = Toggle()
    toggle_2 = AnimatedToggle(
      checked_color="#FFB000",
      pulse_checked_color="#44FFB000"
    )
    container = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(toggle_1)
    layout.addWidget(toggle_2)
    container.setLayout(layout)
    self.setCentralWidget(container)

app = QtWidgets.QApplication([])
w = Window()
w.show()
app.exec_()

```

This creates a window containing two toggles -- the first using `Toggle` (no animations) with default colors and the second using `AnimatedToggle` with custom colors, in orange. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
![Two variants of the toggle widget](https://i.imgur.com/rHrkkG3.gif) _The two toggles_
You can customize the colors yourself, just remember that for transparency the values are specified in `AARRGGBB` order, that is alpha (transparency) then red, green, blue -- `#FFB000` is solid orange, while `#44FFB000` is semi-transparent orange of the same color.
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Salem Al Bream](https://www.pythonguis.com/static/theme/images/authors/salem-al-bream.jpg)](https://www.pythonguis.com/authors/salem-al-bream/)
**Toggle & AnimatedToggle** was written by [Salem Al Bream](https://www.pythonguis.com/authors/salem-al-bream/) . 
**Toggle & AnimatedToggle** was published in [widgets](https://www.pythonguis.com/widgets/) on January 06, 2021 (updated July 14, 2021) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[widget](https://www.pythonguis.com/topics/widget/) [toggle](https://www.pythonguis.com/topics/toggle/) [custom-widget](https://www.pythonguis.com/topics/custom-widget/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [python](https://www.pythonguis.com/topics/python/)
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
