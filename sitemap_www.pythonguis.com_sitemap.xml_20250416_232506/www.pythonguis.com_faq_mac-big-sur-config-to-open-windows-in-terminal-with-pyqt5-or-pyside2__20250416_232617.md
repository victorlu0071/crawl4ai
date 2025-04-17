# Content from: https://www.pythonguis.com/faq/mac-big-sur-config-to-open-windows-in-terminal-with-pyqt5-or-pyside2/

[](https://www.pythonguis.com/faq/mac-big-sur-config-to-open-windows-in-terminal-with-pyqt5-or-pyside2/#menu)
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
# Mac Big Sur config to open windows in Terminal with PyQt5 or PySide2?
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 02 [ FAQ ](https://www.pythonguis.com/faq/)
_Stephen E van Dellen_ wrote
> I updated my mac's OS from Catalina to Big Sur a few days ago. Since then, scripts that open a window with PyQt5 or PySide2 work as expected when started with IDLE's File, Open Module command. But if I run them with a Terminal command or in Visual Studio Code, they start OK with no indications of trouble but no window ever opens. The Python icon appears in the Dock and Activity Monitor says a Python process is running and using 99% of a CPU. I have to Force Quit it to stop it. This happens even with the simplest scripts in the "basic" source code folder with the Learning PyQt book. I don't know a lot about Python configuration. I probably didn't get everything setup properly for the new OS. I'd appreciate suggestions. 
python ```
macOS About shows: Version 11.0.1
python3 -V returns Python 3.9.0
(On mac, Python commands without a suffix name version 2 programs which comes with macOS. Version 3 commands have a "3" suffix.)
pip3 -V returns: pip 20.2.4
pip3 list returns:
  PyQt5       5.15.1
  PySide2      5.15.1
In a Terminal window, %echo $PATH returns:
/Library/Frameworks/Python.framework/Versions/3.9/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/share/dotnet

```

_Martin Fitzpatrick_
Hey, I haven't upgraded my Mac laptops yet (will give it a go with one at the weekend) but I've read elsewhere that downgrading PyQt5 to v5.13 helps fix the issue -- I wonder if it's just the act of re-installing that helps though to be honest, have had to do that on previous Mac upgrades.
So either
python ```
pip3 install --force-reinstall pyqt5

```

or...
python ```
pip3 install pyqt5==5.13

```

_Stephen E van Dellen_
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
I did pip3 install pyqt5==5.13. Same problem.
Before that, I uninstalled/removed everything related to Python 3, restarted the mac and reinstalled Python 3.9.0 and PySide2. Same problem.
A script that opens a window with Tkinter works OK when started with a Terminal command, Visual Studio Code or IDLE3.
I'd sure appreciate hearing whether other Big Sur users are or are not having the same problem.
Here's the PySide2 script I've been experimenting with:
python ```
from PySide2.QtWidgets import QApplication, QWidget
import sys
app = QApplication(sys.argv)
window = QWidget()
window.show()
app.exec_()

```

and here's the Tkinter script:
python ```
from tkinter import Label
widget = Label(None, text='Hello GUI world!')
widget.pack()
widget.mainloop()

```

_SJ Childerley_
Not that this helps much, however I two conda environments, which according to conda both contain pyqt-5.9.2
However when I run the following script:
python ```
import inspect
from PyQt5 import Qt
vers = ['%s = %s' % (k,v) for k,v in vars(Qt).items() if k.lower().find('version') >= 0 and not inspect.isbuiltin(v)]
print('\n'.join(sorted(vers)))

```

I discover one environment, the one that works, contains pyqt5 5.9.2 (PYQT_VERSION_STR = 5.9.2) and the environment that doesn't work contains pyqt5 5.15.1 (PYQT_VERSION_STR = 5.15.1) 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Where "works" = generates a window containing widgets.
_Stephen E van Dellen_
Thanks for the suggestion. When I try to install versions earlier than 5.13, Pip says:
bash ```
% pip install PyQt5==5.9
Collecting PyQt5==5.9
Using cached PyQt5-5.9-5.9.1-cp35.cp36.cp37-abi3-macosx_10_6_intel.whl (82.2 MB)
ERROR: Could not find a version that satisfies the requirement sip<4.20,>=4.19.3 (from PyQt5==5.9) (from versions: 5.0.0, 5.0.1, 5.1.0, 5.1.1, 5.1.2, 5.2.0, 5.3.0, 5.4.0)
ERROR: No matching distribution found for sip<4.20,>=4.19.3 (from PyQt5==5.9)

```

I don't know enough about Python to understand the problem. I was able to install 5.13 and 5.14. They work the same as 5.15.
_SJ Childerley_
Martin is likely to have a better handle on the changes made 5.13 -> 5.15 and one would hope that Riverbank might have some release notes.
For my part I've discovered that 9.5.2 is a pure Anaconda installation, however the environment that didn't work for me containing pyqt5 5.15.1 was a result of me piping on top of a previous Anaconda installation.
When I pip3 uninstalled pyqt5 and then used conda install pyqt5 again things went back to normal and started working.
_Stephen E van Dellen_
Fixed in PyQt5 5.15.2. Doesn't seem to be fixed in PySide2 5.15.2. I've reported that at bugreports.qt.io
1:1 Coaching & Tutoring for your Python GUIs project
[![Martin Fitzpatrick Python GUIs Coaching & Training](https://www.pythonguis.com/static/theme/images/products/coaching.jpg)](https://calendly.com/martinfitzpatrick/60min-python-guis-coaching)
[60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/) [Book Now](https://www.pythonguis.com/live/)
1:1 Python GUIs Coaching & Training
**Comprehensive code review** • **Bugfixes** & improvements • **Maintainability** advice and **architecture** improvements • **Design and usability** assessment • Suggestions and tips to **expand your knowledge** • **Packaging and distribution** help for Windows, Mac & Linux • [Find out more.](https://www.pythonguis.com/live)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Mac Big Sur config to open windows in Terminal with PyQt5 or PySide2?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/mac-big-sur-config-to-open-windows-in-terminal-with-pyqt5-or-pyside2/Python books) on the subject. 
**Mac Big Sur config to open windows in Terminal with PyQt5 or PySide2?** was published in [faq](https://www.pythonguis.com/faq/) on November 15, 2020 (updated September 02, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyside](https://www.pythonguis.com/topics/pyside/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
