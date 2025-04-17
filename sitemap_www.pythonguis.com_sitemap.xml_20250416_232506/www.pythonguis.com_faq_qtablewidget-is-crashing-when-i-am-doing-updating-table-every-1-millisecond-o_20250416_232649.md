# Content from: https://www.pythonguis.com/faq/qtablewidget-is-crashing-when-i-am-doing-updating-table-every-1-millisecond-once/

[](https://www.pythonguis.com/faq/qtablewidget-is-crashing-when-i-am-doing-updating-table-every-1-millisecond-once/#menu)
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
# QTableWidget is crashing when i am doing updating table every 1 millisecond once
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
rajasekhar9035 | 2020-12-14 07:30:23 UTC | #1
I build an application with PyQt5 and i used QTableWidget for the table view i need to add 0th row and delete the 1000 th row every 1 millisecond once. my code has to receive the message payload every 1 millisecond once from the mqtt and update into the table every 1 millisecond once. i was tried with 100 milliSeconds once at that time it was working fine. If i test with 1 millisecond once its getting crashed and its giving python has crashed message. Please give me any sugestions.
Adding to QTableWidget: Data=[1,2,3,4] self.table.insertRow(0) for item in Data: self.table.setItem(0,i, QTableWidgetItem(str(item)))
Removing from QTableWidget: self.table.setRowCount(1000)
martin | 2020-12-14 19:41:54 UTC | #2
Hi @rajasekhar9035 welcome to the forum. Can you provide the error your seeing in Python?
Are you using threads to collect the data, these types of rate-dependent errors usually indicate that you're passing data between threads and triggering a segmentation fault. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
rajasekhar9035 | 2020-12-15 13:20:01 UTC | #3
Thanks for your response @martin, i am seeing this error.
![image|363x183](https://www.pythonguis.com/static/faq/forum/qtablewidget-is-crashing-when-i-am-doing-updating-table-every-1-millisecond-once/uqFbHI1hqccakZTd20ShaEgY4Qe.png)
I am using QRunnable Widget and multi process with message Queue for sharing memory. process1: MQTT subscription Queue.put(Message.payload) process2:(QRunnable) Updating into Table Queue.get(Message.payload)
martin | 2020-12-16 16:29:44 UTC | #4
What is in the message payload?
If it's complex data (i.e. a list of objects) you might want to consider serializing the data somehow/doing a complete deepcopy before passing it. The Queue only ensures the the outer object is not shared between threads, but not any nested objects. This isn't a problem e.g. if you have a list of simple types (strings, ints, etc.) but if you have nested structures it can cause issues.
If you can shared some of your code, I can see if that's likely to be a problem here.
rajasekhar9035 | 2020-12-18 13:07:00 UTC | #5
[quote="martin, post:4, topic:633"] If it’s complex data (i.e. a list of objects) you might want to consider serializing the data somehow/doing a complete deepcopy before passing it. The Queue only ensures the the outer object is not shared between threads, but not any nested objects. This isn’t a problem e.g. if you have a list of simple types (strings, ints, etc.) but if you have nested structures it can cause issues. [/quote]
My message payload is like this:
python ```
c,1608182721,500,8,1,2,3,4,5,6,7,8 \r\n
c,1608182722,400,8,11,22,33,44,55,66,77,88\r\n\r\n

```

Hear is my subscription code, i am taking the message payload and split with "\r\n" .the out put is nested list eg:
python ```
WholeData=['c,1608182721,500,8,1,2,3,4,5,6,7,8','c,1608182722,400,8,11,22,33,44,55,66,77,88']

```

Means list of strings. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
python ```
def on_message(client, userdata, message):
  msg=message.payload
  WholeData=[]
  WholeData=msg.decode("utf-8").split('\r\n')#for middle \r\n
  tableQue.put(WholeData)

```

And hear is my table updation [QRunnable widget] code
python ```
 def UpdateTable(self):
    while True:
      if not self.Que.empty():
        self.table.setRowCount(1000)
        WholeData = self.Que.get()
        for item in WholeData:
          if len(item)>0:
            try:
              RawData=[]
              RawData=item.split(',')
              dummy= RawData[-1].split("\r\n")#for ending \r\n
              RawData[-1]=dummy[0]
              Data=[]
              self.table.insertRow(0)
              for i in range(1,4):
                self.table.setItem(0, i-1, QTableWidgetItem(str(Data[i])))
              for i in range(0,int(Data[3])):
                self.table.setItem(0, i+3, QTableWidgetItem(str(Data[i+4])))
            except:
              print("exception updating into a table")

```

As per your suggestion i have tried with deep copy of my list like this
python ```
def on_message(client, userdata, message):
  msg=message.payload
  WholeData=[]
  WholeData=msg.decode("utf-8").split('\r\n')
  WholeData_copy = copy.deepcopy(WholeData)
  tableQue.put(WholeData_copy)

```

Still crashing is there.
I hope you can understand the code flow, if its not understandable please let me know i will provide my full code.
martin | 2020-12-18 13:19:31 UTC | #6
Where is the following bit of code running, is this in your thread? (... it _must_ be in another thread, or the `while True` would block the GUI).
python ```
 def UpdateTable(self):
    while True:

```

I think then that the problem is that you're updating your widgets from your other thread -- you can't do this! Widgets can only be updated from the GUI thread.
You can emit the data from your thread using Qt signals, and listen to this signal in your GUI thread to trigger the updates. There is an example of emitting data via signals [in this tutorial](https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/) .
I _think_ you could just replace your queue with this, then your `updateTable` method would be (on your mainwindow).
python ```
def UpdateTable(self, WholeData):
  # Defined on your main window. Receives updated data via signal.
  for item in WholeData:
    if len(item)>0:
      try:
        RawData=[]
        RawData=item.split(',')
        dummy= RawData[-1].split("\r\n")#for ending \r\n
        RawData[-1]=dummy[0]
        Data=[]
        self.table.insertRow(0)
        for i in range(1,4):
          self.table.setItem(0, i-1, QTableWidgetItem(str(Data[i])))
        for i in range(0,int(Data[3])):
          self.table.setItem(0, i+3, QTableWidgetItem(str(Data[i+4])))
      except:
        print("exception updating into a table")

```

The signal would be defined for the type of data you're sending (a list)
python ```
class Signals(QObject):
  data = pyqtSignal(list)
class MyRunner(QRunner):
  signals = Signals()
  ....

```

Then you would hook your runner up to this, e.g. (on the main window)
python ```
runner = MyRunner()
runner.signals.data.connect(self.updateTable)

```

Does that make sense? You eliminate the `while` loop since your handler method is only called when a signal is sent (i.e. when data is actually available) rather than waiting on a queue.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**QTableWidget is crashing when i am doing updating table every 1 millisecond once** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/qtablewidget-is-crashing-when-i-am-doing-updating-table-every-1-millisecond-once/Python books) on the subject. 
**QTableWidget is crashing when i am doing updating table every 1 millisecond once** was published in [faq](https://www.pythonguis.com/faq/) on December 14, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
