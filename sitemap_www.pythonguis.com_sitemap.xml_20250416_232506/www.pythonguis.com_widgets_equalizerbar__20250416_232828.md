# Content from: https://www.pythonguis.com/widgets/equalizerbar/

[](https://www.pythonguis.com/widgets/equalizerbar/#menu)
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
# EqualizerBar
Visualize audio frequency changes
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Mar 03 [ Python GUI Widget Library ](https://www.pythonguis.com/widgets/)
[ EqualizerBar Source Code ](https://www.pythonguis.com/d/equalizer_bar_qawKQhy.zip)
This custom PyQt5/PySide2-compatible widget provides a frequency visualizer output for audio applications. It is completely configurable from the number of bars, the number of segments and colours to the animated decay. It's ready to drop into your Python-Qt5 applications.
The download package includes a demo animation using random data and some custom colour configuration so you can explore how the widget works.
## Basic setup
To create an Equalizer object pass in the number of bars and a number of segments per bar.
python ```
equalizer = Equalizer(5, 10)

```

![The default appearance of the widget.](https://www.pythonguis.com/static/widgets/equalizerbar/Screenshot_2019-06-15_at_16.44.36.png) _The default appearance of the widget._
The default range for each of the equalizer bars is 0...100. This can be adjusted using `.setRange`.
python ```
equalizer.setRange(0, 1000)

```

## Decay animation
The equalizer bar includes a decay animation where peaks of values slowly fade over time. This is created by gradually subtracting a set value from the current value of each bar, using a recurring timer.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
The frequency of the decay timer (in milliseconds) can be configured using `.setDecayFrequencyMs`. The default value is 100ms.
python ```
equalizer.setDecayFrequencyMs()

```

Passing 0 will disable the decay mechanism.
On each tick a set value is removed from the current value of each bar. This is configured by using `.setDecay`. Adjust this based on your equalizer's range of possible values.
python ```
equalizer.setDecay(0, 1000)

```

## Bar style configuration
The number of bars to display and the number of segments in the bars/the colours of those bars are defined at startup.
python ```
equalizer = EqualizerBar(10, ["#2d004b", "#542788", "#8073ac", "#b2abd2", "#d8daeb", "#f7f7f7", "#fee0b6", "#fdb863", "#e08214", "#b35806", "#7f3b08"])

```

![Purple Orange theme with 10 bars](https://www.pythonguis.com/static/widgets/equalizerbar/Screenshot_2019-06-15_at_16.49.33.png) _Purple Orange theme with 10 bars_
To set the colours after startup, either provide a list of colors (`QColor` or hex values) at startup, or use the `.setColors` method. Passing a list of colours to this method will change the number of segments to match the colours provided. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
python ```
equalizer.setColors(["#810f7c", "#8856a7", "#8c96c6", "#b3cde3", "#edf8fb"])

```

You can also use `.setColor` to set a single colour for all segments, without changing the number of bars.
python ```
equalizer.setColor('red')

```

The spacing around the equalizer graphic is configured with `.setBarPadding` providing an integer value to add in pixels.
python ```
equalizer.setBarPadding(20)

```

The proportion of each segment in the bar which is solid/empty is configured using `.setBarSolidXPercent` or `.setBarSolidYPercent` with a float value between 0...1. This can be used to make bar segments thinner and narrower if you prefer.
python ```
equalizer.setBarSolidXPercent(0.4)
equalizer.setBarSolidYPercent(0.4)

```

Finally, the background color can be configured using `.setBackgroundColor`
python ```
equalizer.setBackgroundColor('#0D1F2D')

```

![Customising bar padding and sizing.](https://www.pythonguis.com/static/widgets/equalizerbar/Screenshot_2019-06-15_at_16.55.22.png) _Customising bar padding and sizing._
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**EqualizerBar** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/widgets/equalizerbar/Python books) on the subject. 
**EqualizerBar** was published in [widgets](https://www.pythonguis.com/widgets/) on June 15, 2019 (updated March 03, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[equalizer](https://www.pythonguis.com/topics/equalizer/) [custom-widget](https://www.pythonguis.com/topics/custom-widget/) [audio](https://www.pythonguis.com/topics/audio/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [python](https://www.pythonguis.com/topics/python/)
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
