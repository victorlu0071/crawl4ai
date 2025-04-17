# Content from: https://www.pythonguis.com/faq/pyqt5-gridlayout-issues-arranging-stuffs-non-format/

[](https://www.pythonguis.com/faq/pyqt5-gridlayout-issues-arranging-stuffs-non-format/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PyQt5 ](https://www.pythonguis.com/pyqt5/)
  * [PyQt5 Tutorial ](https://www.pythonguis.com/pyqt5-tutorial/)
  * Basics
  * [Create a PyQt5 app](https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/)
  * [PyQt5 Signals](https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/)
  * [PyQt5 Widgets](https://www.pythonguis.com/tutorials/pyqt-basic-widgets/)
  * [PyQt5 Layouts](https://www.pythonguis.com/tutorials/pyqt-layouts/)
  * [PyQt5 Menus](https://www.pythonguis.com/tutorials/pyqt-actions-toolbars-menus/)
  * [PyQt5 Dialogs](https://www.pythonguis.com/tutorials/pyqt-dialogs/)
  * [Multi-window PyQt5](https://www.pythonguis.com/tutorials/creating-multiple-windows/)
  * Qt Designer
  * [First Qt Designer app](https://www.pythonguis.com/tutorials/first-steps-qt-creator/)
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/creating-dialogs-qt-designer/)
  * [The QResource System in PyQt5](https://www.pythonguis.com/tutorials/qresource-system/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/)
  * Plotting
  * [Plotting With PyQtGraph and PyQt5](https://www.pythonguis.com/tutorials/plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PyQt5](https://www.pythonguis.com/tutorials/plotting-matplotlib/)
  * QGraphics
  * [Vector Graphics](https://www.pythonguis.com/tutorials/pyqt-qgraphics-vector-graphics/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/qpropertyanimation/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/system-tray-mac-menu-bar-applications-pyqt/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/)
  * [Packaging for Linux](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-linux-pyinstaller/)
  * [Packaging QResources](https://www.pythonguis.com/tutorials/packaging-data-files-pyqt5-with-qresource-system/)
  * [Packaging with fbs](https://www.pythonguis.com/tutorials/packaging-pyqt5-apps-fbs/)
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
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Pyqt5 gridlayout issues arranging stuffs non format
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
meshelleva4815 | 2020-06-19 00:49:01 UTC | #1
I suppose am a new buddy here...well, greetings. I have the issue with a project am working on. It's actually a school management system. What i basically want to do is create a frame that displays a group box in maybe 3 columns and n rows, depending on the length of data from the database. I manage to create it but am having problem making the frame resize itself to display the groupbox properly and also spacing out the groupbox. I will appreciate a simple sample. Thanks in advance
Luca | 2020-06-19 20:52:18 UTC | #2
Hi, Could you send what you've done and describe more clearly what you want to obtain? Maybe with a drawing?
meshelleva4815 | 2020-06-21 01:31:13 UTC | #3
![20200621_014844|375x500](https://www.pythonguis.com/static/faq/forum/pyqt5-gridlayout-issues-arranging-stuffs-non-format/e9wPRVxM11eCH6rtNAfVjslG8t0.jpeg) This is what I get when I have just 15 staffs but...
meshelleva4815 | 2020-06-21 01:32:27 UTC | #4
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
![20200621_014956|375x500](https://www.pythonguis.com/static/faq/forum/pyqt5-gridlayout-issues-arranging-stuffs-non-format/rduxUU14Q7hik5eG8JBFLMquH8w.jpeg) This is what it becomes with 30 staffs.
meshelleva4815 | 2020-06-30 11:30:12 UTC | #8
This is the QFrame that holds the gridlayout
python ```
self.info_staff_main = QGroupBox(self.info_staff_panel)
self.info_staff_main.setGeometry(10, 50, 920, 560)
self.info_staff_main.setStyleSheet('background-color:white;border:0px;border-radius:0px')
self.staff_scroll = QScrollArea(self.info_staff_main)
self.staff_scroll.setGeometry(5, 0, 918, 560)
self.staff_scroll.setStyleSheet('border:none;border-radius:0px;')
self.staff_main = QFrame()
self.staff_main.setFixedWidth(900)
self.staff_main.setMinimumHeight(900)
self.staff_main.setStyleSheet('background-color:white;border:0px;')
self.staff_scroll.setWidget(self.staff_main)
self.staff_grid = QGridLayout()
self.staff_grid.setContentsMargin(0, 10, 0, 0)
self.staff_grid.setSpacing(10)
self.staff_main.setLayout(self.staff_grid)

```

This is how I generated the Groupbox to the gridlayout
python ```
self.staff_sub = QGroupBox()
self.staff_sub.setFixedSize(250,130)
self.staff_sub.setStyleSheet(...)

```

And this how I positioned the widget.
python ```
self.staff_grid.addWidget(self.staff_sub, x, y)
self.staff_grid.setColumnStretch(x % 3, 1)
self.staff_grid.setRowStretch(y, 1)

```

Now my problems these: 1, it worked fine when I assumed only 15 users I.e when I set number = 15 As soon as it becomes 30 or more, the whole thing becomes a mess like the picture above. How do I make the frame resize automatically 2, how can I get the location of each group box on the layout. I will like to have buttons on each group box to delete, update or view profile. I hope this is clear a bit. Thanks in advance. And sorry it has to be in picture, I tried coping the code but the whole thing was a mess when I previewed.
Luca | 2020-06-22 00:03:22 UTC | #9
Hi @meshelleva4815,
Yes, you must learn to add the code :weary: I admit that I was tempted to use an OCR :rofl:
To add some code you have to:
  1. Add an empty line
  2. Add four spaces at the beginning of each line of code


I normally select all the code in the editor, add an indentation to all of them and then copy and paste them in here.
Using a better formatting, being clear, and concise takes a few seconds for the writer but you'll have more chances of receiving an answer and the right answer. Less time you invest on the quality of your question more time and effort will be necessary for receiving the right answer.
Hahaha so please don't open another Topic formatted like this one :stuck_out_tongue_winking_eye:
Going back to your problem here a working example that I wrote for you:
python ```
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import sys
class Window(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.create_gui()
    self.create_boxes()
  def create_gui(self):
    self.setGeometry(0, 0, 920, 560)
    self.centralwidget = QWidget(self)
    self.centralwidget_layout = QGridLayout(self.centralwidget)
    self.staff_scroll = QScrollArea(self.centralwidget)
    self.staff_scroll.setWidgetResizable(True)
    self.centralwidget_layout.addWidget(self.staff_scroll, 0, 0)
    self.staff_scroll_content = QWidget()
    self.staff_scroll_content.setGeometry(QRect(0, 0, 1000, 200))
    self.staff_scroll_layout = QGridLayout(self.staff_scroll_content)
    self.staff_main = QFrame(self.staff_scroll_content)
    self.staff_main_layout = QGridLayout(self.staff_main)
    self.staff_grid = QGridLayout()
    self.staff_main_layout.addLayout(self.staff_grid, 0, 0)
    self.staff_scroll_layout.addWidget(self.staff_main, 0, 0)
    self.staff_scroll.setWidget(self.staff_scroll_content)
    self.setCentralWidget(self.centralwidget)
  def create_boxes(self):
    number = 1000
    columns = 3
    for x in range(number//columns):
      for y in range(columns):
        staff_sub = QGroupBox()
        staff_sub.setFixedSize(250, 130)
        self.staff_grid.addWidget(staff_sub, x, y)
        layout = QHBoxLayout()
        staff_sub.setLayout(layout)
        button = QPushButton(str((x, y)))
        button.pressed.connect(lambda x=x, y=y: self.staff_sub_click(x*columns + y))
        layout.addWidget(button)
  def staff_sub_click(self, index):
    print("staff_sub", index, " clicked")
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec_())

```

meshelleva4815 | 2020-06-22 04:46:36 UTC | #10
Really dont know how to thank you for this boss. Thank you and for my errors, I will take to the steps next time and doit well :grin:..you know first time thing..thanks buddy for this but just to add, in cases where I have numbers like 31 as an example, will it also cater for the extra line..., I mean the extra 1 in a new line?
Luca | 2020-06-22 08:09:58 UTC | #11
You're welcome :rofl: don't worry we are in here to learn.
Yes, you're right I used your initial for loops and it works just if _number_ is multiple of _columns_.
Substitute the lines:
python ```
for x in range(number//columns):
  for y in range(columns):

```

with:
python ```
for index in range(number):
  x = index // columns
  y = index % columns

```

and try to understand why it works :wink:
meshelleva4815 | 2020-06-22 18:36:42 UTC | #12
I think I did my assignment well to understand it today, Thanks to you though. But please, I have one last favour to ask, am trying to get picture data and name from sqlite db to two labels on each of those group boxes but am really not getting my way round. Do you care helping me with something like a demo?
Luca | 2020-06-22 23:12:14 UTC | #13
Come on @meshelleva4815, I think that with a bit of effort you can easily come up with a solution by yourself. To really learn something you need to get your hands dirty first else you'll always need the support of somebody else. I think that what you need to do is not so complex and it is not impossible to come up with a solution without any support.
From your question I see that you've already clear what you need to do:
[quote="meshelleva4815, post:12, topic:283, full:true"] I think I did my assignment well to understand it today, Thanks to you though. But please, I have one last favour to ask, am trying to **get picture data and name from sqlite db to two labels** on each of those group boxes but am really not getting my way round. Do you care helping me with something like a demo? [/quote]
Split it in smaller tasks and focus on each one separately: 1. Get some text from a database 2. Show the text on the gui 3. Get an image from a database 4. Show the image on the gui
I bet there is a lot of material online about it.
We'll be all waiting for a working solution from you :stuck_out_tongue_winking_eye:
meshelleva4815 | 2020-06-23 05:28:10 UTC | #14
:scream: :ok_woman:we** you mean every one...God help me. I've actually been getting myself around it and two major problems am encountering are 1. I manage to get the picture to work but I could get only one pictures, don't know how to write multiple pictures at a time 2. I could also get all the data, I mean the name now, loop through the rows but how to implement it is the problem :grinning:
Luca | 2020-06-23 10:38:23 UTC | #15
Ok great, so current state: 1. Get some text from a database **DONE** 2. Show the text on the gui **(1 line of code, you know how to do it)** 3. Get an image from a database **DONE** 4. Show the image on the gui **(few lines of code, there are many examples online)**
If it looks difficult, begin making it to work for one box and then extend it to more boxes **(you already have the for loop)**.
Then once you've done it, if you want, you can try to improve it to make it more efficient.
meshelleva4815 | 2020-06-23 10:53:47 UTC | #16
Am seriously having issues with it, when I added a line to loop each row of the data, it's not showing anything in the gui. As if a for loop with range cant work with normal loop.. I have this from your previous assistan
for index in range(number): for i in data:
# it doesn't show any error but it seem to me like the new loop i added have an effect on the old to make it not work at all, like the old loop not working as to display the groupbox again.
Then for the pictures I could only get one to work with this code
pm = QPixmap() for a in self.pix: pm.loadFromData(a[0])
It only get one pics for all the widgets....
Luca | 2020-06-23 11:15:24 UTC | #17
Please show the full code and better format your messages.
meshelleva4815 | 2020-06-23 12:23:02 UTC | #18
python ```
  #this is how i implimented it though
  def create_boxes(self):
    self.load_pics()
    db = lit.connect('Testdb.db')
    self.c = db.cursor()
    self.result = self.c.execute("SELECT name FROM users")
    number = len(self.result.fetchall())
    columns = 3
    for index in range(number):
      for row in (self.result):
        x = index // columns
        y = index % columns
        self.staff_sub = QGroupBox()
        self.staff_sub.setFixedSize(250, 130)
        self.staff_grid.addWidget(self.staff_sub, x, y)
        self.staff_dp = QLabel(self.staff_sub)
        self.staff_dp.setGeometry(5, 65, 60, 60)
        self.staff_dp.setPixmap(self.pxmap)
        self.staff_dp.setScaledContents(True)
        self.staff_name = QLabel(self.staff_sub)
        self.staff_name.setGeometry(80, 60, 160, 25)
        self.staff_name.setText(str(self.result))
      #this is for the pictures
  def load_pics(self):
    db = lit.connect('Testdb.db')
    self.c = db.cursor()
    self.result = self.c.execute("SELECT dp FROM users WHERE id = 4")
    pm = QPixmap()
    for x in self.result:
      pm.loadFromData(x[0])
      self.pxmap = QPixmap(pm)

```

Luca | 2020-06-23 13:07:36 UTC | #19
Ok, there are mistakes in the logic and in the data structures used.
I'll give you some advice: 1. You need to get the data from the database
python ```
  names, images = get_info_from_db()

```

you have many names so you will need a data structure to contain multiple items, the same for the images (for example they could be 2 lists). Can you find those data structures in your code?
  1. Now that you have the data structures you want to show them. For each user, you'll have an item in the names data structure and an image in the images data structure.


python ```
  for user_index in range(len(names)):
   gui_user = create_gui_user()
   gui_user.set_name(names[user_index])
   gui_user.set_image(images[user_index])

```

Does this logic seems similar to your?
meshelleva4815 | 2020-06-23 13:16:40 UTC | #20
Thanks buddy! It looks completely strange though, am a kind new to it so its really a puzzle-like right now :smiley: maybe if i try looking well at it, maybe I might get it. Really thank you for the long stress I put you through man
meshelleva4815 | 2020-06-28 15:39:25 UTC | #21
Afternoon here boss. Am back with same trouble. I still can't get it to work after series of efforts can you just help me out, please :wink:..
Luca | 2020-06-29 00:58:28 UTC | #22
Ok begin to solve some problems and answer these questions: _What does load_pics should do?_ Which output would you expect from it? * Check the output with:
python ```
  print(type(self.pxmap))

```

  * What is the inner loop for? It is executed for each user. Is it necessary?


python ```
  for index in range(number):
    for row in (self.result):

```

  * If you noticed something strange in the load_pics() function maybe you'll need to change something even in here:


python ```
  self.staff_dp.setPixmap(self.pxmap)

```

and in here:
python ```
  self.staff_name.setText(str(self.result))

```

With this answer and the previous one you should have enough insights to solve your problems.
meshelleva4815 | 2020-07-05 13:38:47 UTC | #23
Thanks boss. I got a way around it using Qtablewidget. Really appreciate the much contributions :hugs:
Luca | 2020-07-06 15:32:18 UTC | #24
You're welcome :wink:, well done @meshelleva4815!
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Pyqt5 gridlayout issues arranging stuffs non format** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyqt5-gridlayout-issues-arranging-stuffs-non-format/Python books) on the subject. 
**Pyqt5 gridlayout issues arranging stuffs non format** was published in [faq](https://www.pythonguis.com/faq/) on June 19, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
