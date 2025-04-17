# Content from: https://www.pythonguis.com/widgets/gradient/

[](https://www.pythonguis.com/widgets/gradient/#menu)
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
# Gradient
Gradient designer with add, drag and edit stops
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 13 [ Python GUI Widget Library ](https://www.pythonguis.com/widgets/)
[ Gradient designer Source Code ](https://www.pythonguis.com/d/gradient_cu8CGhV.zip)
This custom PyQt5/PySide2-compatible widget provides a gradient designer providing a handy interface to design linear gradients in your applications. A new gradient can be created simply by creating an instance of the object.
python ```
gradient = Gradient()

```

The default gradient is black to white. The stop points are marked by a red box with a white line drawn vertically through it so they are visible on any gradient.
![Initial state of the gradient designer](https://www.pythonguis.com/static/widgets/gradient/Screenshot_2019-06-15_at_18.37.58.png) _Initial state of the gradient designer_
## User Interface
The widget allows editing of the gradient using the mouse. The controls are —
  * _Double-click_ to add a new stop to the gradient at the clicked location. This is set to the same colour as the point to the right.
  * _Right-click_ on a stop marker to edit the colour of that stop, by opening up a platform-native colour selector tool.
  * _Click & drag_ a stop to move it, you can drag a stop past another stop to reverse the order. The two outermost points cannot be dragged.


## Setting a Gradient
The gradient is defined as a list of 2-`tuple` containing a stop point as `float` between 0 and 1, and a colour as either a hex `str` or `QColor` or colour name. These can be set/retrieved through the API.
python ```
gradient.setGradient([(0, 'black'), (1, 'red')])
>>> gradient.gradient()
[(0, 'black'), (1, 'red')]

```

If you set a gradient out of order it will be sorted.
python ```
gradient.setGradient([(0, 'black'), (1, 'green'), (0.5, 'red')])
>>> gradient.gradient()
[(0.0, 'black'), (0.5, 'red'), (1.0, 'green')]

```

If any stop is outside the range 0..1 it will throw an assertion. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
![Gradient auto-sorted when set.](https://www.pythonguis.com/static/widgets/gradient/Screenshot_2019-06-15_at_19.22.35.png) _Gradient auto-sorted when set._
## Modifying the Gradient
Alongside the GUI interface you can edit the gradient by adding/removing stop points through the API. The methods available are —
`.addStop(stop, color=None)` to add a new stop to the gradient. The `stop` is a `float` between 0 and 1, and the optional second parameter is a colour (hex, `QColor`, color name) for that point. If no colour is provided it defaults to the same colour as the following stop.
`.removeStopAtPosition(n)` removes a stop by index (i.e. order, the first stop would be zero). You cannot remove the end stop points. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
`.setColorAtPosition(n, color)` set the color of a given stop by index (i.e. order).
`.chooseColorAtPosition(n, current_color=None)` pops up a window to choose the colour for the specified stop by index. If optional parameter `current_color` is provided the colour chooser will default to this initially.
![The colour picker popped-up by the Gradient widget](https://www.pythonguis.com/static/widgets/gradient/Screenshot_2019-06-15_at_19.24.14.png) _The colour picker popped-up by the Gradient widget_
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Gradient** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/widgets/gradient/Python books) on the subject. 
**Gradient** was published in [widgets](https://www.pythonguis.com/widgets/) on June 15, 2019 (updated September 13, 2023) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[designer](https://www.pythonguis.com/topics/designer/) [custom-widget](https://www.pythonguis.com/topics/custom-widget/) [shader](https://www.pythonguis.com/topics/shader/) [gradient](https://www.pythonguis.com/topics/gradient/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [python](https://www.pythonguis.com/topics/python/)
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
