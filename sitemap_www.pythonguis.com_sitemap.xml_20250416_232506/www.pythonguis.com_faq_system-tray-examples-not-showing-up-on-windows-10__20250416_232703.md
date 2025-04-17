# Content from: https://www.pythonguis.com/faq/system-tray-examples-not-showing-up-on-windows-10/

[](https://www.pythonguis.com/faq/system-tray-examples-not-showing-up-on-windows-10/#menu)
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
# System tray examples not showing up on Windows 10
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
Virginia | 2020-05-14 12:00:40 UTC | #1
I just started this tutorial: https://www.pythonguis.com/courses/adanced-ui-features/system-tray-mac-menu-bar-applications-pyqt/ I am using a Windows 10 computer. When I run the two example code blocks in the tutorial, nothing happens. I have to force the programs to stop executing. The icons are not showing up anywhere that I can see. Please can you help me to get this running? I have searched online and haven't found a solution yet. Other examples from other sites also have this issue. Thank you.
Virginia | 2020-05-14 12:22:36 UTC | #2
Just to add, I have been able to get an icon to appear using an example from stackoverflow but unfortunately nothing happens and the program just keeps running because I can't exit.
Here's the code from https://stackoverflow.com/questions/893984/pyqt-show-menu-in-a-system-tray-application:
import sys from PyQt5 import QtWidgets, QtCore, QtGui class SystemTrayIcon(QtWidgets.QSystemTrayIcon): def **init**(self, icon, parent=None): QtWidgets.QSystemTrayIcon.**init**(self, icon, parent) menu = QtWidgets.QMenu(parent) exitAction = menu.addAction("Exit") self.setContextMenu(menu) menu.triggered.connect(self.exit) def exit(self): QtCore.QCoreApplication.exit() def main(image): app = QtWidgets.QApplication(sys.argv) w = QtWidgets.QWidget() trayIcon = SystemTrayIcon(image, w) trayIcon.show() sys.exit(app.exec_()) if **name** == '**main** ': on=QtGui.QIcon('color.png') main(on)
martin | 2020-05-14 14:31:55 UTC | #3
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Hey @Virginia I have just tested the example now on Windows 10 and it works fine for me. I did notice though that when I didn't have the icon available it wouldn't show _anything_ in the system tray. The code as-is expects the `icon.png` to be in the same folder as the script.
![windows-10-systray|611x54](https://www.pythonguis.com/static/faq/forum/system-tray-examples-not-showing-up-on-windows-10/8fQC9ks11MVCvtm0O76sEtZ47QJ.png)
You could of course use the built-in icons we discovered recently.
python ```
# Create the icon
style = app.style()
icon = QIcon(style.standardIcon(QStyle.SP_TitleBarMenuButton))

```

![windows-10-systray-qt|587x54](https://www.pythonguis.com/static/faq/forum/system-tray-examples-not-showing-up-on-windows-10/hcTlQ4PIAWzI12gCoQ8ixgKr7bJ.png)
(`SP_TitleBarMenuButton` is the Qt icon on the left)
To add a quit option to the menu you can add another action e.g.
python ```
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

```

I'll add this to the article.
Virginia | 2020-05-14 15:39:17 UTC | #4
The icon was in the same folder, and it still didn't work. However now when I run it, your code is working - sort of. The icon shows up in the system tray, and I can right click on it to access the dropdown. This problem may be related to my software - Spyder is behaving strangely. Sometimes when I run it, the icon shows up and it works fine. Other times it shows up, but in the hidden icons - I have to expand my system tray to see it. Then I can "quit" and the code stops but the icon is still there. Normally when I close something in the system tray, the icon disappears. Maybe that is what happened before - it ran but the system tray put it with the hidden icons. I also didn't pick up on the fact that I was supposed to right click on it, not left click. The code from Stack Overflow works now too. Maybe this is Spyder's issue.
Thank you for adding the "quit" button - before I was having trouble getting it to stop running because Spyder doesn't always respond to break commands. That was what caused a large amount of my problems earlier. Then I was left clicking instead of right clicking when I tried the other code.
martin | 2020-05-14 15:37:23 UTC | #5
How long does the icon hang around after you quit? If it's via the "Quit" menu icon it _should_ be fairly quick (a few seconds). If you quit the command window it was launched from the process is sill going for a while, so it will take a bit longer. It could be Windows hiding all the icons together you're right.
Eolinwen | 2020-05-14 16:15:29 UTC | #6
@ Virginia
In the past, I have used Spyder and Eric6, Pycharm. I have keep Pycharm and remove Spyder and Eric6.
[Pycharm](https://www.jetbrains.com/pycharm/) is really a great IDE done in Java (search the error) for Python (and Django too but not with the community version).
Since Martin's tutorials, I also use Qt Creator which is really great and complementary to Pycharm. I understand very well what you are living with your IDE because I lived it too.
I don't know if we can share some files in PM but I could send you a basic tray app that I have done based in a big part with the system tray tutorial. This app is basic and do nothing. Under to display it in the systray and show a bunch of action with their respective icons. This can be helpful for you to know if it s come from you or your IDE . I will include the icons folder with and all the links in the code.
[Deepin](http://pix.toile-libre.org/upload/original/1589042815.png)
Virginia | 2020-05-14 20:00:54 UTC | #7
Thank you very much, Eolinwen! I have Anaconda Navigator, which included Spyder and some other code editors. I took your advice and tried it in a different IDE - Jupyter Notebook. This does the same thing. The code stops running, but the icon remains. I can see using the Task Manager that, even after I close Jupyter Notebook, I have to use the task manager end the task jupyter-notebook.exe to get the icon to go away. It's possible that the script is very, very slow to stop and that it would stop on its own, but I think I have to force it with the task manager.
I'm not sure if I want to keep playing around with scripts that aren't completely stopping right now - I think I should move on and focus on some different tutorials, then maybe come back to this later - but I would appreciate it if you could send me another program to test, just to try one more example. I tried the one from Stack Overflow again and it's now crashing both IDE's.
Thank you again for your help.
Virginia | 2020-05-14 20:02:21 UTC | #8
It's hanging on after I quit via the menu icon, and it seems like I have to shut the IDE down and sometimes also have to use the Task Manager to get the icon to go away (although the menu no longer appears).
martin | 2020-05-14 20:33:48 UTC | #9
Weird. Have you tried running it from the command line -- as in, save it to a file `systray.py` and then execute it with `python systray.py` outside of an IDE? 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
If it doesn't return after the `app.quit()` call then it suggests it's not shutting down the main loop cleanly, I'll have a dig there might be some step I've missed to do this properly.
Virginia | 2020-05-14 21:22:00 UTC | #10
Thank you for suggesting that. It works fine in the command line, but in the IDEs I have to basically force it to shut down with the Task Manager. At least I know that if I do decide to make an app with this feature, I can run it that way. Does this have something to do with kernels?
Eolinwen | 2020-05-15 13:43:28 UTC | #11
[quote="Virginia, post:7, topic:198"] Thank you very much, Eolinwen! I have Anaconda Navigator, which included Spyder and some other code editors. I took your advice and tried it in a different IDE - Jupyter Notebook. This does the same thing. The code stops running, but the icon remains. I can see using the Task Manager that, even after I close Jupyter Notebook, I have to use the task manager end the task jupyter-notebook.exe to get the icon to go away. It’s possible that the script is very, very slow to stop and that it would stop on its own, but I think I have to force it with the task manager. [/quote]
I have had the same issue there are a long time ago when I have tried this one. I have removed it more quickly than I have installed. In fact , I had the same issue using Ipyhton in spyder (which is also used by Jupyter) . My kernel was died and nothing was responding. Obliged to kill the app.
Try Pycharm community (you can get in Anaconda I have checked) After you 'll Adopt it and love it. This IDE is really done for Python and PyQt5.
To check if it comes from your IDE (or anaconda rather), we are going together a little thing.
  1. Create a folder that you name like you want
  2. Copie/paste the following file with the name that you want in a python file. For me it is basic_tray.py


python ```
  import os
  from PyQt5.QtGui import QIcon
  from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
  app = QApplication([])
  app.setQuitOnLastWindowClosed(False)
  #Création de l'icone qui se situe dans le dossier image
  icon_path_tray = os.path.join(os.path.dirname(__file__), "images/mascot.png")
  tray_icon = QIcon(icon_path_tray)
  #Création du tray
  tray_menu = QSystemTrayIcon()
  tray_menu.setIcon(tray_icon)
  tray_menu.setVisible(True)
  #Création du menu
  menulist_tray = QMenu()
  #Display another icon
  icon_path = os.path.join(os.path.dirname(__file__), "images/")
  #Show the main window
  actionshow = QAction(QIcon(os.path.join(icon_path, "desktop.png")), "Show Main Window")
  menulist_tray.addAction(actionshow)
  #Hide the main window
  actionHide = QAction(QIcon(os.path.join(icon_path, "mouse.png")), "Hide the Window")
  menulist_tray.addAction(actionHide)
  #add a separtor
  menulist_tray.addSeparator()
  #add a help item
  actionHelp = QAction(QIcon(os.path.join(icon_path, "reboot.png")), "Help")
  menulist_tray.addAction(actionHelp)
  #Quit the application
  actionQuit = QAction(QIcon(os.path.join(icon_path, "application-exit.png")), "Quit")
  menulist_tray.addAction(actionQuit)
  #add a separator
  menulist_tray.addSeparator()
  #Ajout du menu au tray
  tray_menu.setContextMenu(menulist_tray)
  app.exec_()

```

  1. Create a folder right next to the python file that you 'll call _images_.
  2. On pills (where you can add icons), download a icon theme (if it is not already done :stuck_out_tongue_winking_eye: ) put 4 icons.
  3. Rename this 4 icons with the following names :
  4. desktop.png
  5. mouse.png
  6. reboot.png
  7. application-exit.png


Finally, do 2 tests : - one opening a console in the first folder (where you have the python file) and run it (python hisname.py)
  * one with your IDE and see the result.


Normally, you should get the same result that the Deepin picture that I have shared with before (obviously, you 'll have some different icons).
Eolinwen | 2020-05-15 13:42:39 UTC | #12
[quote="martin, post:9, topic:198, full:true"] Weird. Have you tried running it from the command line – as in, save it to a file `systray.py` and then execute it with `python systray.py` outside of an IDE?
If it doesn’t return after the `app.quit()` call then it suggests it’s not shutting down the main loop cleanly, I’ll have a dig there might be some step I’ve missed to do this properly. [/quote]
Perhaps, that 's come from :
python ```
  app = QApplication([])
  app.setQuitOnLastWindowClosed(False)

```

I have experimented some isssues with and I have replaced by (like I done usually):
python ```
app = QApplication(sys.argv])
  app.setQuitOnLastWindowClosed(False)

```

You need to add at the beginning :
python ```
import sys

```

Normally, the main loop shouldn't be at the end ?
Virginia | 2020-05-15 19:46:02 UTC | #13
Hi @Eolinwen! Thank you for these other suggestions about using sys and PyCharm. Unfortunately neither made a difference for the code from this tutorial site. I still had to shut it down in PyCharm manually. But I have confirmed, thanks to @Martin's earlier suggestion, that it will shut down properly when run from the command line. That may be what I have to do for now whenever I want to run something with a system tray icon. I will try your code later.
Virginia | 2020-05-17 12:01:14 UTC | #14
I added a 'quit' action to this code, which has no actions, and it does the same thing as the other code. It's possible that the 'quit' command is part of the issue, but using other similar commands such as 'exit' doesn't change the outcome. I think this may be part of a more general issue. It seems from my web searches that other people have problems with IDE's not running or stopping programs. However, I do know that I can run these in the terminal. Thank you again for all your help on this issue.
Virginia | 2020-05-18 12:15:11 UTC | #15
I have now discovered, based on advice I found here https://gist.github.com/hogelog/5338905 that if I replace PyQt5 with PySide2, and run it in PyCharm with a virtual environment that does not have PyQt5 in it, it works as expected. However I have not been able to get that to work in Spyder yet because of issues with Spyder and PySide2. I haven't tried it in any other IDE's yet. Now I have at least one option beyond using the terminal. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**System tray examples not showing up on Windows 10** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/system-tray-examples-not-showing-up-on-windows-10/Python books) on the subject. 
**System tray examples not showing up on Windows 10** was published in [faq](https://www.pythonguis.com/faq/) on May 14, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
