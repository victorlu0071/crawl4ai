# Content from: https://www.pythonguis.com/faq/adding-new-tabs-in-tabwidget-appears-as-a-seperate-window-when-tab-is-selected/

[](https://www.pythonguis.com/faq/adding-new-tabs-in-tabwidget-appears-as-a-seperate-window-when-tab-is-selected/#menu)
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
# Adding new Tabs in TabWidget appears as a seperate window when tab is selected
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
cookeh_a9 | 2020-12-05 00:13:58 UTC | #1
I've been working on a PyQT5 which has vertical tabs. However I am experiencing some odd behavior.
I have a class which inherits QApplication. When I create tabs within this class, behavior is as expected. However I want to add tabs via an event listener call. So within the class that inherits QApplication, I register a function which adds a tab.
When I add a tab via event listener call, the tab window goes outside the MainWindow. However if I just add it manually without event listener calls, the behavior is as expected.
Good and bad behaviors: ![behv1|690x346](https://www.pythonguis.com/static/faq/forum/adding-new-tabs-in-tabwidget-appears-as-a-seperate-window-when-tab-is-selected/uSXAzRGSWEOB0jI0huMguEYclrp.png)
My guess is that I am using an old state of QApplication or MainWindow. I've spent a while trying to debug this and I do not see anyone who has ran into tabs appearing outside issue.
Code is below. I have commented in caps-lock the events. This is a rather sized application, so posting all the code isn't really feasible. I am hoping to get any ideas from anyone. Appreciate it.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt5](https://www.pythonguis.com/static/theme/images/products/pyqt5-book.png)](https://www.pythonguis.com/pyqt5-book/)
[Take a look ](https://www.pythonguis.com/pyqt5-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/create-simple-gui-applications/) and [Amazon Paperback](https://www.amazon.com/dp/B08RB2HRS1/)
python ```
class MainWindow(QApplication):
def __init__(self, argv):
  super().__init__(argv)
  self.logic = None
  self.logic_thread = None
  self.basic_routine_cb = None
  self.advanced_routine_cb = None
  self.routine_frequency_drop_down = None
  self.current_action_text = None
  self.bot_running_time_value = None
  self.total_rallies_joined_value = None
  self.time_until_next_routine_value = None
  self.routine_executed_at_value = None
  self.bubble_time_checked_value = None
  self.total_marches_drop_down = None
  self.help_dialog = None
  self.login = None
  self.emulator_port_value = None
  self.start_stop_button = None
  self.total_preset_rotation_drop_down = None
  self.consume_stamina_cb = None
  self.w = None
  self.win = MainApplicationWindow()
  self.initialize_user_interface()
def initialize_user_interface(self):
  QtWidgets.QApplication.setStyle(ProxyStyle())
  self.setStyle('Fusion')
  self.win.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
  self.win.setGeometry(0, 0, 650, 525)
  self.win.setFixedSize(650, 525)
  self.win.setWindowTitle("Some Title")
  self.w = TabWidget()
  self.login = LoginForm(self)
  tab1 = self.create_new_bot_tab()
  self.w.addTab(tab1, QtGui.QIcon("./forum/images/RedSquare.png"), "1")
  self.w.addTab(QWidget(), QtGui.QIcon("zoom.png"), "+")
  self.w.currentChanged.connect(self.add_new_tab) #changed!
  event_list.append(self.insert_new_bot_tab) # EVENT LISTENER ADDED HERE
  self.win.setCentralWidget(self.w)
  self.win.show()
  self.login.show()
  self.w.show()
  sys.exit(self.exec_())
@pyqtSlot()
def add_new_tab(self):
  try:
    if Client.socket_connection.connected is False:
      self.w.setCurrentIndex(self.w.currentIndex() - 1)
      self.login.show()
      return
    if self.w.tabText(self.w.currentIndex()) != '+':
      return
    Client.attempt_add_tab() # THIS CALLS A FUNCTION WHICH EVENTUALLY CALLS THE REGISTERED EVENT
    # IF I CALL self.insert_new_bot_tab() HERE RATHER THAN USING EVENT LISTENER TO CALL IT, BEHAVIOUR IS AS EXPECTED
  except Exception as e:
    print(str(e))

# THE REGISTERED EVENT HERE
def insert_new_bot_tab(self):
  tab2 = self.create_new_bot_tab()
  self.w.insertTab(self.w.currentIndex(), tab2, QtGui.QIcon("./forum/images/RedSquare.png"),
           str(self.w.currentIndex() + 1))
  self.w.blockSignals(True)
  self.w.setCurrentIndex(self.w.currentIndex() - 1)
  self.w.blockSignals(False)
def create_new_bot_tab(self):
  wdg = CustomQWidget(self.win, self)
  layout = QtWidgets.QGridLayout(wdg)
  index = 0
  if self.w.currentIndex() > -1:
    index = self.w.currentIndex()
  tabs = QTabWidget()
  tab1 = StartMenuTab(self.login, self.w, index)
  tab2 = ProfileTab()
  tabs.resize(300, 200)
  # Add tabs
  tabs.addTab(tab1, "Start")
  tabs.addTab(tab2, "Profile")
  layout.addWidget(tabs)
  return wdg

```

CustomQWidget class:
python ```
class CustomQWidget(QWidget):
def __init__(self, win, win_instance):
  super().__init__(win)
  self.win_instance = win_instance

```

cookeh_a9 | 2020-12-05 06:40:39 UTC | #2
I'm using a hackish work around for now. If anyone has any idea I would really appreciate feedback!
martin | 2020-12-08 12:08:16 UTC | #3
Hi @cookeh_a9 welcome to the forum! 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
First up, it's a bit strange to inherit from `QApplication`, normally, you'd inherit from `QMainWindow` for your main window. You then create an instance of `QApplication` directly, create your window, and then start up the app event loop, e.g.
python ```
app = QApplication(sys.argv)
w = MainWindow()
app.exec_()

```

But I don't think that's the issue here. When you get windows popping out of the main window, it's usually an due to something going wrong with window parents -- any widget without a parent in Qt is a floating window. So if you create a `QTabWidget` but don't set a parent (either explicitly, or by adding it to a layout) it will be floating. The same happens if you remove the parent from a widget by setting parent to `None`.
Another way you can get caught out is by recreating a widget, e.g. if you have a tab widget as `self.w` and then recreate the `self.w = QTabWidget` again, the reference to the first tab widget is lost + it is destroyed. All widgets that had it as a parent (i.e. the tabs) are now parent-less and will free-float.
I'd start by checking the parent parameters you're passing to the various widgets when being created. Then double-check you're not recreating any widgets accidentally/unnecessarily.
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Adding new Tabs in TabWidget appears as a seperate window when tab is selected** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/adding-new-tabs-in-tabwidget-appears-as-a-seperate-window-when-tab-is-selected/Python books) on the subject. 
**Adding new Tabs in TabWidget appears as a seperate window when tab is selected** was published in [faq](https://www.pythonguis.com/faq/) on December 05, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
