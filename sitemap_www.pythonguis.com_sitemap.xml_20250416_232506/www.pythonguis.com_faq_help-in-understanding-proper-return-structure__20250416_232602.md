# Content from: https://www.pythonguis.com/faq/help-in-understanding-proper-return-structure/

[](https://www.pythonguis.com/faq/help-in-understanding-proper-return-structure/#menu)
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
# Help in understanding proper Return Structure
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Normen_Zocch | 2020-08-18 20:24:22 UTC | #1
Hello everybody, after studying the tutorials and the book (really helpful) I'm stuck how do i return something back to the widget. The demos print a lot on the console. Well thats easy. What i want is when i push a button, the outcome of the function behind the pushed button should display its values in the widget or qlabel. What i have so far: a class A and functions that generates random values. a class B and functions where i keep the button1_clicked function which calls the functions from the first class a main class C with an init function and a InitUI functions in which all the widgets are created and displayed. So what i want is, click on button1 from the main class C, it calls the button_clicked function in class B which calls the random functions in class A and returns back to the widget/qlabel InitUi in class C.
Is that the way how it is done in Pyqt? How do i get my values back in the widget (not console) and how would i properly structurre such a program in terms of classes and functions? Any help and insight is highly appreciated! Thanks very much, best.
martin | 2020-08-20 19:12:14 UTC | #2
Hi @Normen_Zocch welcome to the forum!
To be able to get values into your widgets, you need to have kept a reference to the widget object somewhere accessible. If you have a class, and define your widgets in that class, storing them on that class object you can then access them from any method using `self`, e.g. `self.my_label.setText(...)`
In your example where you have 3 separate classes you have two options --
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
  1. Make sure your classes have a reference to the classes whos' widgets they are updating. For example, if you want to update class C from class A, class A would need to have a reference to the class C object. This works for small examples, but loses you the isolation of your classes (see below).
  2. Define custom signals to pass this data around. As well as Qt's built-in signals, you can also define your own signals and use them to hook parts of your application together. So for example, you could define a custom signal on class A and connect it directly to the widget on class C you want to update.


If you have some example code I can show how to achieve it with signals.
Lastly, just be careful you're not introducing classes for their own sake, where they don't give any benefits -- it's a judgement call, and depends on the app. The random number generators might be better suited to a submodule for example (do you need the instance?)
If you _do_ need a class for handling state, "a random number generator" sounds more like a "service" which should be to be used by class B, rather than interacting with class C directly. That is B should request a number from A, then pass it to C. A number generator shouldn't need to know about the UI (if that makes sense?) Signals give you this isolation, but you can also achieve it in other ways.
Normen_Zocch | 2020-09-07 11:46:47 UTC | #3
Hello Martin, thanks for this. This is really helpful. I have to mention, that im - just - learning Python and rerad about the concept of classes and functions. These three classes are my first dive into OOP. So i got the principle but im not there yet to play around in freestyle mode. To have a Project wich interests me and helps me learning Python, im writing a NPC Generator for a popular Pen & Paper Roleplay game. While studying the Internet for help, i now dropped Class B and put B and Mainclass C together. I got several functions in my NPCGen Class. That is class "A" where the real data is generated. Example Class A
python ```
class NPCGen:
  def generate_name(self):
    with open('swnames.csv') as f:
      swnames_reader = csv.reader(f)
      swnames = random.choice(list(swnames_reader))
      global swname
      firstname = (swnames[0])
      surename = (swnames[1])
      fullname = (firstname + " " + surename )
      return fullname

```

Then i created an Object
python ```
# Creating NPCGen Class Object
npcbuild = NPCGen()

```

Now in Class C, i create the Widgets:
python ```
  def initUI(self, birth):
    widget = QWidget()
    layout = QGridLayout()
    self.setWindowTitle("That famous Space Opera D6 NPC Generator") # self.title
    self.setGeometry(self.left, self.top, self.width, self.height)
    # Generate Button to initiate new random values
    self.button1 = QPushButton('Generate', self)
    self.button1.move(10,20)
    self.button1.clicked.connect(self.button1_clicked)
    # Displaying Labels
    self.npcswname = QLabel(self)
    self.swname = npcbuild.generate_name()
    self.npcswname.update()
    self.npcswname.setFixedWidth(100)
    self.npcswname.setText(self.swname)
    self.npcswname.move(260,80)
    self.npcswname.adjustSize()
 ```
So im not there yet to understand how a reference should work correctly, but here I have 15 different labels , then I activate them via:
```python
   layout.addWidget(self.npcswname)

```

Now comes the interesting part, in here in my main class in have my button1_clicked function where i update all the values like:
python ```
  def button1_clicked(self):
    # Update Random Values
    # Char Name
    self.swname = npcbuild.generate_name() # <- i call here again a new random name
    self.npcswname.setText(self.swname)

```

So this scenario works, but it looks "ugly" coz i would rather separate it and have more readable beautiful code. So here i would be interested how custom signals could do the job more professionally. In the end all my 15-20 QLabels should be upgraded by this, when i click on the Generate Button. I didn't choose the QMainWindow coz i did not fully comprehend where and what and why all the widgets should go. But i could imagine, this owuld be the way to go towards a "proper" PyQT Application. So, thanks vor any Wisdom you can share :slight_smile: Normen
martin | 2020-09-07 12:07:24 UTC | #4
Hi @Normen_Zocch ...sorry for the delay in replying this time, I just had a baby :) 
[quote="Normen_Zocch, post:3, topic:426"] 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
python ```
  def initUI(self, birth):
    widget = QWidget()
    layout = QGridLayout()
    self.setWindowTitle("That famous Space Opera D6 NPC Generator") # self.title
    self.setGeometry(self.left, self.top, self.width, self.height)
    # Generate Button to initiate new random values
    self.button1 = QPushButton('Generate', self)
    self.button1.move(10,20)
    self.button1.clicked.connect(self.button1_clicked)
    # Displaying Labels
    self.npcswname = QLabel(self)
    self.swname = npcbuild.generate_name()
    self.npcswname.update()
    self.npcswname.setFixedWidth(100)
    self.npcswname.setText(self.swname)
    self.npcswname.move(260,80)
    self.npcswname.adjustSize()

```

[/quote]
So there are a couple of things you can do here to make things simpler for yourself.
  1. Use Qt layouts, rather than positioning the widgets using width, move + adjustSize. Then you can just plop them into your layout.
  2. Storing the reference to the widgets on `self` is fine, but as you notice when you have multiple widgets it can get a bit out of hand.


So, first for the layouts. Since we just have a list of `QLabels` to display, we can stack them up using a `QVBoxLayout` (vertical box layout), e.g.
python ```
def initUI(self, birth):
   # ... your other code
  player_layout = QVBoxLayout()
  self.npcswname = QLabel(self) 
  player_layout.addWidget(self.npcswname)
  # etc.
  # Set the layout on the window.
  self.setLayout(player_layout)

```

If you have another layout (e.g. the grid) you can add one layout to another to nest them. Don't worry about using `QMainWindow`, this is only necessary if you want access to toolbars, etc. in your application.
For updating the widgets with the new values, you can do a few things. One option is to store your player stats in a dictionary _and_ store a dictionary that maps from each state name to a widget, you can iterate and copy the values over. 
python ```
def initUI(self, birth):
   # ... your other code
  player_layout = QVBoxLayout()
  npcswname = QLabel(self) 
  player_layout.addWidget(npcswname)
  # etc.
  stat_widgets = {
    'name': npcswname,
    'hp': hitpoints
  }
  # Set the layout on the window.
  self.setLayout(player_layout)

```

Here we've stored references to the `npcswname` widget in a dictionary, another named `hitpoints`. The dictionary maps from the statistic name, to the widget which displays that statistic.
If we store our statistics in a similar dictionary, e.g.
python ```
  player_stats = {
    'name': 'bilbo',
    'hitpoints': 45
  }

```

...we can then iterate the statistics, and update the widgets, with something like ...
python ```
  for k, v in player_stats.items():
    widget = self.stat_widgets[k]
    widget.setText(str(v))
````
As we iterate `player_stats`, `k` will get the key (the statistic name) and `v` will get the value of that statistic. We look up the k (statistic name) n the `stat_widgets` dictionary, to get the widget, and then call `setText` on that widget. We wrap it in `str` since `hitpoints` is a number, and `QLabel.setText` only accepts strings.
Note that using a dictionary like this doesn't have to complicate your creation. If you have a method that returns a random name, you can populate the dictionary directly like follows.
```python
player_stats = {
  'name': npcbuild.generate_name()
  'hitpoints': npcbuild.generate_hitpoints() 
}

```

... the resulting `player_stats` dictionary will contain the generated values.
If that's all a bit much, you can keep the pattern of storing data in a dictionary + just assign to the widgets in turn. Still, I would create a separate update method to keep it nice and tidy.
python ```

def update(self, player_stats):
   self.npcswname.setText(player_stats['name'])
   self.npcswhitpoints.setText(player_stats['hitpoints'])

```

Having your statistics in a dictionary (or any other structure) will make it a lot nicer when you want to do anything else with the values.
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Help in understanding proper Return Structure** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/help-in-understanding-proper-return-structure/Python books) on the subject. 
**Help in understanding proper Return Structure** was published in [faq](https://www.pythonguis.com/faq/) on August 18, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
