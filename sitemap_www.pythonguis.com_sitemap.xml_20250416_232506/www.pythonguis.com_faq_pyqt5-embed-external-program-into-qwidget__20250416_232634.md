# Content from: https://www.pythonguis.com/faq/pyqt5-embed-external-program-into-qwidget/

[](https://www.pythonguis.com/faq/pyqt5-embed-external-program-into-qwidget/#menu)
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
# Pyqt5 embed external program into qwidget
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
mike2750 | 2020-06-23 14:18:07 UTC | #1
I do not know if anyone here has done this but I have been trying off and off for last few months to be allow a user to specify their desired terminal and have that embedded into a widget in my app.
I have done some extensive research but have not been able to find a way to make this really work despite there being some almost there examples.
Wondering if anyone here had any advise.
Resources: https://stackoverflow.com/questions/41474647/run-a-foreign-exe-inside-a-python-gui-pyqt https://stackoverflow.com/questions/32703557/qx11embedcontainer-equivalent-in-qt5 https://stackoverflow.com/questions/52123693/open-window-within-main-window-pyqt5 https://stackoverflow.com/questions/29112349/how-to-use-a-terminal-embedded-in-a-pyqt-gui
This looks promising but only applies to the cef browser. https://github.com/cztomczak/cefpython/issues/325 https://github.com/cztomczak/cefpython/blob/79a8ebcc51ab7e96adbb8d0d44eec4c89c7c1cc9/examples/qt.py
Rough idea #!/usr/bin/env python # -_- coding:utf-8 -_ - import psutil import os import platform import sys from pathlib import Path from subprocess import call 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
python ```
from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication
platform = platform.system()
print(str(platform))
term_dir = Path(os.path.abspath(os.path.dirname(__file__))) / 'terminus'
if platform == 'Windows':
  term_bin = str(term_dir) + '/' + str(platform.lower()) + '/' + 'terminus.exe'
elif platform == 'Linux':
  term_bin = str(term_dir) + '/' + str(platform.lower()) + '/' + 'terminus'
print(term_bin)

class embeddedTerminal(QWidget):
  def __init__(self):
    QWidget.__init__(self)
    self._processes = []
    self.resize(800, 600)
    self.terminal = QWidget(self)
    layout = QVBoxLayout(self)
    layout.addWidget(self.terminal)
    self._stop_process()
    self._start_process(
      'xterm',
      ['-into', str(self.terminal.winId()),
       '-e', 'tmux', 'new', '-s', 'my_session']
    )
    button = QPushButton('List files')
    layout.addWidget(button)
    button.clicked.connect(self._list_files)
  def _start_process(self, prog, args):
    child = QProcess()
    self._processes.append(child)
    child.start(prog, args)
  def _list_files(self):
    self._start_process(
      'tmux', ['send-keys', '-t', 'my_session:0', 'ls', 'Enter'])
  @classmethod
  def _stop_process(self):
    call(["tmux", "kill-session", "-t", "my_session"])

if __name__ == "__main__":
  app = QApplication(sys.argv)
  main = embeddedTerminal()
  main.show()
  sys.exit(app.exec_())

```

mike2750 | 2020-06-30 03:55:05 UTC | #2
Here are all the different things i tried code wise.
[embed_terminal_1.py](https://wizardassistant.com/embedded_terminal/embed_terminal_1.py) https://pastebin.com/vixqvyeZ
[embed_terminal_2.py](https://wizardassistant.com/embedded_terminal/embed_terminal_2.py) https://pastebin.com/hu3jPkaq
[embed_terminal_3.py](https://wizardassistant.com/embedded_terminal/embed_terminal_3.py) https://pastebin.com/3UXq8edc
[embed_terminal_4.py](https://wizardassistant.com/embedded_terminal/embed_terminal_4.py) https://pastebin.com/1x1XTzhW
[embed_terminal_5.py](https://wizardassistant.com/embedded_terminal/embed_terminal_5.py) https://pastebin.com/hWNcPGbi
[embed_terminal_6.py](https://wizardassistant.com/embedded_terminal/embed_terminal_6.py) https://pastebin.com/mgpRVzdp
[embed_terminal_7_urxvt.py](https://wizardassistant.com/embedded_terminal/embed_terminal_7_urxvt.py) https://pastebin.com/SFMrhWkG
embed_terminal_xterm.py https://pastebin.com/s5Wq92WR
Zip file with all the different code for ease of use. https://wizardassistant.com/embedded_terminal/pyqt_embed_terminal_attempts.zip
Honestly the objective it to embed a native bash/xterm/ or user selectable terminal executable but if i could get something like the below to work properly with better context menu support would probably work. https://pypi.org/project/py3qterm/0.4/
The only issue i have with the websockets thing is the pyqt webengine doesn't play nice on some older systems even when compiled with older version.
martin | 2020-06-30 11:24:10 UTC | #3
What are the main problems you're having with the py3qterm approach? Is it getting it to run full stop, or handling the communication with the running terminal once it's up? The screenshots show something, but is that for an older version? 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
mike2750 | 2020-06-30 16:17:59 UTC | #4
With the Py3term approach it does attach to a local bash terminal fine in linux and does work for htop/top stuff which is pretty huge considering how lightweight this is compared to websockets approach.
![image|640x500](https://www.pythonguis.com/static/faq/forum/pyqt5-embed-external-program-into-qwidget/elmeeMl4QTubNSxNWzxn3YN0FPb.png) ![image|690x424](https://www.pythonguis.com/static/faq/forum/pyqt5-embed-external-program-into-qwidget/mkOmw0XVZsoSPQVFbA885vbSN2q.png)
pros: term ptt curses and env variables all work
cons:
The main issue is how it works with mouse text selection and doesn't feature a right click context menu. This is going to be used cross platform thats going to be weird for alot of people not having a standard context menu(copy/paste) if i were to switch to this. I haven't really been able to figure out the key events and context menu overrides although i have read the chapters in the book about it. I gotta really experiment more as thats probably fixable.
Also when i ported this to python3 awhile back while mostly functional there are some weird oddities.
  1. like not being able to use the tilde "~" symbol unless i type it in twice or paste it in twice for some reason. This is a huge deal breaker as tons of the commands i use are based on variable expansion and homedir functions of bash and i cannot copy and paste if its going to just silently discard it the first time and have unpredictable results. There are some other characters this happens to but i forgot which they were the tilde one i remember well due to how frustrated i got with it.


I think that has something to do with this portion of how original author did stuff. I'm not that advanced in my knowledge of pyqt or backend terminal coding mechanics to understand why this is needed. https://gitlab.com/mikeramsey/py3qtermwidget/-/blob/master/py3qterm/backend.py#L110
  1. Cursor is pretty fugly. not end of the world.
  2. selection is a bit rough too.


For comparison: the current xterm.js websocket is pretty slick but due pyqt webgine requirements its heavy and requires more effort to connect to stuff vs attaching to a local bash session and then jumping via ssh to desired server which would simplify things for people on Linux/Mac and Windows with the linux subsystem and bash installed.
![image|690x426](https://www.pythonguis.com/static/faq/forum/pyqt5-embed-external-program-into-qwidget/5WBpiQnbNmREgHGzni9xuF6Tp8.png)
I did find another project which text and mouse stuff works really nice but it is not a proper terminal and ptty so it doesn't support the interactive or environmental variables. https://github.com/Axel-Erfurt/QTerminal
If there was a way to basically splice the interface of this project to the backend of the py3term that would be near perfect. I know there tons of other people looking for a proper Pyqt terminal without any drawbacks just not at that level of skill to make it happen yet :frowning:
![image|690x243](https://www.pythonguis.com/static/faq/forum/pyqt5-embed-external-program-into-qwidget/cJchU83CPCohhUs0TWSRaRGiIZY.png)
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt5](https://www.pythonguis.com/static/theme/images/products/pyside2-book.png)](https://www.pythonguis.com/pyside2-book/)
[Take a look ](https://www.pythonguis.com/pyside2-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/create-gui-applications-pyside/) and [Amazon Paperback](https://www.amazon.com/dp/B08R92BW7R/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Pyqt5 embed external program into qwidget** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyqt5-embed-external-program-into-qwidget/Python books) on the subject. 
**Pyqt5 embed external program into qwidget** was published in [faq](https://www.pythonguis.com/faq/) on June 23, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
