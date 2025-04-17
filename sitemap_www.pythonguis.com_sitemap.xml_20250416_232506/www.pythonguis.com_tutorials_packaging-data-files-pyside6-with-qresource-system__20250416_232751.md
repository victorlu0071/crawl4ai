# Content from: https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/

[](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PySide6 ](https://www.pythonguis.com/pyside6/)
  * [PySide6 Tutorial ](https://www.pythonguis.com/pyside6-tutorial/)
  * Basics
  * [Create a PySide6 app](https://www.pythonguis.com/tutorials/pyside6-creating-your-first-window/)
  * [PySide6 Signals](https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/)
  * [PySide6 Widgets](https://www.pythonguis.com/tutorials/pyside6-widgets/)
  * [PySide6 Layouts](https://www.pythonguis.com/tutorials/pyside6-layouts/)
  * [PySide6 Menus](https://www.pythonguis.com/tutorials/pyside6-actions-toolbars-menus/)
  * [PySide6 Dialogs](https://www.pythonguis.com/tutorials/pyside6-dialogs/)
  * [Multi-window PySide6](https://www.pythonguis.com/tutorials/pyside6-creating-multiple-windows/)
  * Qt Designer
  * [First Qt Designer app](https://www.pythonguis.com/tutorials/pyside6-first-steps-qt-designer/)
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/pyside6-qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/pyside6-creating-dialogs-qt-designer/)
  * [The QResource System in PySide6](https://www.pythonguis.com/tutorials/pyside6-qresource-system/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/pyside6-qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/pyside6-modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/pyside6-qtableview-modelviews-numpy-pandas/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/pyside6-bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/pyside6-creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/pyside6-animated-widgets/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/pyside6-embed-pyqtgraph-custom-widgets/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/pyside6-transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/pyside6-system-tray-mac-menu-bar-applications/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyside6-applications-windows-pyinstaller-installforge/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyside6-applications-pyinstaller-macos-dmg/)
  * [Packaging QResources](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/)
  * Resources
  * [Books](https://www.pythonguis.com/books/)
  * Services
  * [Consulting](https://www.pythonguis.com/hire/)
  * [1:1 Coaching](https://www.pythonguis.com/live/)
  * [Contact](https://www.pythonguis.com/contact/)
  * [About](https://www.pythonguis.com/about/)
  * Libraries
  * [PyQt6](https://www.pythonguis.com/pyqt6/)
  * [PyQt5](https://www.pythonguis.com/pyqt5/)
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Using QResource to Package Data Files With PyInstaller and PySide6
Serialize data files for easy packaging in Python
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Mar 15 PySide6 [ Packaging and Distributing PySide6 Applications ](https://www.pythonguis.com/pyside6-tutorial/#pyside6-packaging-and-distribution)
#### [ PySide6 Tutorial ](https://www.pythonguis.com/pyside6-tutorial/) — [Packaging and Distributing PySide6 Applications](https://www.pythonguis.com/pyside6-tutorial/#pyside6-packaging-and-distribution)
  * [Packaging PySide6 applications for Windows with PyInstaller & InstallForge](https://www.pythonguis.com/tutorials/packaging-pyside6-applications-windows-pyinstaller-installforge/)
  * [Packaging PySide6 applications into a macOS app with PyInstaller](https://www.pythonguis.com/tutorials/packaging-pyside6-applications-pyinstaller-macos-dmg/)
  * [Using QResource to Package Data Files With PyInstaller and PySide6](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/)


This tutorial is also available for [PyQt5](https://www.pythonguis.com/tutorials/packaging-data-files-pyqt5-with-qresource-system/) and [PySide2](https://www.pythonguis.com/tutorials/packaging-data-files-pyside2-with-qresource-system/)
Bundling data files with _PyInstaller_ usually works quite well. However, there can be issues with using relative paths, particularly when bundling cross-platform applications, as different systems have different standards for dealing with data files. If you hit these problems they can unfortunately be quite difficult to debug.
Thankfully, Qt comes to the rescue with it's _resource system_. Since we're using Qt for our GUI we can make use of Qt Resources to bundle, identify and load resources in our application. The resulting bundled data is included in your application as Python code, so _PyInstaller_ will automatically pick it up and we can be sure it will end up in the right place.
In this section we'll look at how to bundle files with our application using the Qt Resources system.
Table of Contents
  * [The QRC file](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#the-qrc-file)
  * [Example Build: Bundling Qt Designer UIs and Icons](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#example-build-bundling-qt-designer-uis-and-icons)
    * [Resources](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#resources)
    * [The finished app](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#the-finished-app)
  * [Building a Windows Installer with Installforge](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#building-a-windows-installer-with-installforge)
    * [Packaging Resources](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#packaging-resources)
    * [The UI in Qt Designer](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#the-ui-in-qt-designer)
    * [Building the app](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#building-the-app)
  * [Creating an installer](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#creating-an-installer)
    * [General](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#general)
    * [Setup](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#setup)
    * [Dialogs](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#dialogs)
    * [System](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#system)
    * [Build](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#build)
    * [Running the installer](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#running-the-installer)
  * [Wrapping up](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/#wrapping-up)


### The QRC file
The core of the Qt Resources system is the _resource file_ or QRC. The `.qrc` file is a simple XML file, which can be opened and edited with any text editor.
You can also create QRC files and add and remove resources using Qt Designer, which we'll cover later.
#### Simple QRC example
A very simple resource file is shown below, containing a single resource (our application icon).
xml ```
<!DOCTYPE RCC>
<RCC version="1.0">
  <qresource prefix="icons">
    <file alias="hand_icon.ico">hand_icon.ico</file>
  </qresource>
</RCC>

```

The name between the `<file>` `</file>` tags is the path to the file, relative to the resource file. The `alias` is the name which this resource will be known by from within your application. You can use this _rename_ icons to something more logical or simpler in your app, while keeping the original name externally.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
For example, if we wanted to use the name `application_icon.ico` internally, we could change this line to.
xml ```
<file alias="application_icon.ico">hand_icon.ico</file>

```

This only changes the name used *inside* your application, the filename remains unchanged.
Outside this tag is the `qresource` tag which specifies a `prefix`. This is a _namespace_ which can be used to group resources together. This is effectively a virtual folder, under which nested resources can all be found.
#### Using a QRC file
To use a `.qrc` file in your application you first need to compile it to Python. PySide6 comes with a command line tool to do this, which takes a `.qrc` file as input and outputs a Python file containing the compiled data. This can then be imported into your app as for any other Python file or module.
To compile our `resources.qrc` file to a Python file named `resources.py` we can use
python ```
pyside6-rcc resources.qrc -o resources.py

```

To use the resource file in our application we need to make a few small changes. Firstly, we need to `import resources` at the top of our app, to load the resources into the Qt resource system, and then secondly we need to update the path to the icon file to use the resource path format as follows:
python ```
app.setWindowIcon(QtGui.QIcon(':/icons/hand_icon.ico'))

```

The prefix `:/` indicates that this is a _resource path_. The first name "icons" is the _prefix_ namespace and the filename is taken from the file _alias_ , both as defined in our `resources.qrc` file.
The updated application is shown below.
python ```
from PySide6 import QtWidgets, QtGui
try:
  from ctypes import windll # Only exists on Windows.
  myappid = 'mycompany.myproduct.subproduct.version'
  windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
  pass

import sys
import resources # Import the compiled resource file.
class MainWindow(QtWidgets.QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setWindowTitle("Hello World")
    l = QtWidgets.QLabel("My simple app.")
    l.setMargin(10)
    self.setCentralWidget(l)
    self.show()
if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  app.setWindowIcon(QtGui.QIcon(':/icons/hand_icon.ico'))
  w = MainWindow()
  app.exec()

```

You can run the build as follows,
bash ```
pyinstaller --windowed --icon=hand_icon.ico app.py

```

or re-run it using your existing `.spec` file.
bash ```
pyinstaller app.spec

```

If you run the resulting application in `dist` you should see the icon is working as intended.
![The hand icon showing on the toolbar](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/taskbar_icon_custom.png) _The hand icon showing on the toolbar_
The advantage of this method is that your data files are guaranteed to be bundled as they are treated as code — _PyInstaller_ finds them through the imports in your source. You also don't need to worry about platform-specific locations for data files. You only need to take care to rebuild the `resources.py` file any time you add or remove data files from your project.
Of course, this approach isn't appropriate for any files you want to be readable or editable by end-users. However, there is nothing stopping you from combining this approach with the previous one as needed.
## Example Build: Bundling Qt Designer UIs and Icons
We've now managed to build a simple app with a single external icon file as a dependency. Now for something a bit more realistic!
In complex Qt applications it's common to use Qt Designer to define the the UI, including icons on buttons and menus. How can we distribute UI files with our applications and ensure the linked icons continue to work as expected?
Below is the UI for a demo application we'll use to demonstrate this. The app is a simple counter, which allows you to increase, decrease or reset the counter by clicking the respective buttons. You can also [download the source code and associated files](https://downloads.pythonguis.com/counter-pyinstaller-windows.zip).
![The counter UI created in Qt Designer](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/mainwindow.ui_for_Counter_App_WxtORs7.png) _The counter UI created in Qt Designer_
The UI consists of a `QMainWindow` with a vertical layout containing a single `QLabel` and 3 `QPushButton` widgets. The buttons have Increment, Decrement and Reset labels, along with icons from [the Fugue set by p.yusukekamiyamane](https://p.yusukekamiyamane.com/). The application icon is a free icon from [Freepik](https://www.flaticon.com/authors/freepik).
The UI was created in Qt Designer as described in this [tutorial](https://www.pythonguis.com/tutorials/first-steps-qt-creator/).
### Resources
The icons in this project were added to the buttons from within Qt Designer. When doing this you have two options —
  1. add the icons as files, and ensure that the relative path locations of icons are maintained after installation (not always possible, or fun)
  2. add the icons using the Qt Resource system


Here we're using approach (2) because it's less prone to errors.
The method for Qt Resources in your UI differs depending on whether you're using Qt Creator or Qt Designer standalone. The steps are described below.
#### Adding Resources in Qt Designer (Preferred)
If you're using the standalone Qt Designer, the resource browser is available as a dockable widget, visible in the bottom right by default. If the Resource Browser is hidden you can show it through the "View" menu on the toolbar.
To add, edit and remove resource files click on the pencil icon in the Resource browser panel. This will open the resource editor.
![Qt Designer resource browser](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/qt_designer.png) _Qt Designer resource browser_
In the resource editor view you can open an existing resource file by clicking on the document folder icon (middle icon) on the bottom left.
![Qt Designer resource editor](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/qt_designer_resource_editor.png) _Qt Designer resource editor_
In this screenshot above we've included the `.ui` file in the QResource bundle, but I recommend you compile the UI file to Python instead (see below).
On the left hand panel you can also create and delete resource files from your UI. While on the right you can create new prefixes, add files to the prefix and delete items. Changes to the resource file are saved automatically.
#### Adding Resources in Qt Creator
In order to be able to add icons using the Qt Resource system from within Qt Creator you need to have an active Qt Project, and add both your UI and resource files to it.
If you don't have a Qt Creator project set up you can create one in your existing source folder. Qt Creator will prompt before overwriting any of your files. Click on "+ New", choose "Qt for Python - Empty" for project type. Select the folder _above_ your source folder for "Create in", and provide the name of your source folder as the project name. You can delete any files created, except the `.pyproject` which holds the project settings.
![This message will be shown when creating a new Qt Creator project in an existing folder](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/qt_python_location_exists.png) _This message will be shown when creating a new Qt Creator project in an existing folder_
To add resources to your existing project, select the "Edit" view on the left hand panel. You will see a file tree browser in the left hand panel. Right-click on the folder and choose "Add existing files…" and add your existing `.qrc` file to the project.
![Qt Creator "Edit" view, showing a list of files in the project](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/qt_python_edit_view.png) _Qt Creator "Edit" view, showing a list of files in the project_
The UI doesn't update when you add/remove things here, this seems to be a bug in Qt Creator. If you close and re-open Qt Creator the files will be there.
Once you have added the QRC file to the file listing you should be able to expand the file as if it were a folder, and browser the resources within. You can also add and remove resources using this interface.
#### Using resources in Qt Creator and Qt Designer
Once the Resource file is loaded you will be able to access it from the designer properties. The screenshot below shows the Designer with our counter app open, and the _increment_ button selected. The icon for the button can be chosen by clicking the small black down arrow and selecting "Choose Resource…"
![Setting the icon for a button in Qt Designer \(or Qt Creator\)](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/qt_python_designer.png) _Setting the icon for a button in Qt Designer (or Qt Creator)_
The Resource chooser window that appears allows you to pick icons from the resource file(s) in the project to use in your UI.
![Selecting a resource in the Qt Designer resource dialog](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/qt_python_designer_resource.png) _Selecting a resource in the Qt Designer resource dialog_
Selecting the icons from the resource file in this way ensures that they will always work, as long as you compile and bundle the compiled resource file with your app.
#### Compiling the UI file
The simplest way to bundle your UIs using resources is to compile them into Python. The resulting Python file will be automatically packaged by PyInstaller (once it's imported) and will also itself automatically load the related resources file.
bash ```
pyside6-uic mainwindow.ui -o MainWindow.py

```

You may want to wrap this in a function if you're using it a lot.
### The finished app
Below is our updated `app.py` which loads the `mainwindow.ui` file and defines 3 custom slots to increment, decrement and reset the number. These are connected to signals of the widgets defined in the UI (`btn_inc`, `btn_dec` and `btn_reset` for the 3 buttons respectively) along with a method to update the displayed number (`label` for the `QLabel`).
python ```
from PySide6 import QtWidgets, QtCore, QtGui, uic
import sys
from MainWindow import Ui_MainWindow
try:
  from ctypes import windll # Only exists on Windows.
  myappid = 'mycompany.myproduct.subproduct.version'
  windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
  pass

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # Load the UI
    self.setupUI(self)
    # Set value of counter
    self.counter = 0
    self.update_counter()
    # Bind
    self.btn_inc.clicked.connect(self.inc)
    self.btn_dec.clicked.connect(self.dec)
    self.btn_reset.clicked.connect(self.reset)
  def update_counter(self):
    self.label.setText(str(self.counter))
  def inc(self):
    self.counter += 1
    self.update_counter()
  def dec(self):
    self.counter -= 1
    self.update_counter()
  def reset(self):
    self.counter = 0
    self.update_counter()

if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  app.setWindowIcon(QtGui.QIcon(':/icons/counter.ico'))
  main = MainWindow()
  main.show()
  sys.exit(app.exec())

```

If you have made any changes to the `resources.qrc` file, or haven't compiled it yet do so now using `pyrcc5 resources.qrc -o resources.py`
If you run this application you should see the following window.
![Counter app, with all icons showing](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/counter_icons.png) _Counter app, with all icons showing_
We'll build our app as before using the command line to perform an initial build and generate a `.spec` file for us. We can use that `.spec` file in future to repeat the build.
bash ```
pyinstaller --windowed --icon=resources/counter.ico app.py

```

_PyInstaller_ will analyse our `app.py` file, bundling all the necessary dependencies, including our compiled `resources.py` and `MainWindow.py` into the `dist` folder.
Once the build process is complete, open the `dist` folder and run the application. You should find it works, with all icons — from the application itself, through to the icons embedded in our UI file — working as expected.
![Counter app, with all icons showing](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/counter_icons.png) _Counter app, with all icons showing_
This shows the advantage of using this approach — if your application works before bundling, you can be pretty sure it will continue to work after.
## Building a Windows Installer with Installforge
The applications so far haven't done very much. Next we'll look at something more complete — our custom _Piecasso_ Paint application. The source code is [available to download here](https://downloads.pythonguis.com/piecasso.zip) or in the [15 minute apps repository](https://github.com/learnpyqt/15-minute-apps/tree/master/paint).
The source code is not covered in depth here, only the steps required to package the application. The source and more info is available in the [15 minute apps](https://github.com/learnpyqt/15-minute-apps/tree/master/paint) repository of example Qt applications. The custom application icons were created using icon art by [Freepik](https://www.flaticon.com/authors/freepik/). 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Prepared for packaging the project has the following structure (truncated for clarity).
python ```
.
├── paint.py
├── Piecasso.spec
├── mainwindow.ui
├── MainWindow.py
├── README.md
├── requirements.txt
├── resources.qrc
├── resources_rc.py
├── screenshot-paint1.jpg
├── screenshot-paint2.jpg
├── icons
│  ├── blue-folder-open-image.png
│  ├── border-weight.png
│  ├── cake.png
│  ├── disk.png
│  ├── document-image.png
│  ├── edit-bold.png
│  ...
└── stamps
  ├── pie-apple.png
  ├── pie-cherry.png
  ├── pie-cherry2.png
  ├── pie-lemon.png
  ├── pie-moon.png
  ├── pie-pork.png
  ├── pie-pumpkin.png
  └── pie-walnut.png

```

The main source of the application is in the `paint.py` file.
### Packaging Resources
The resources for _Piecasso_ are bundled using the [Qt Resource system](https://www.pythonguis.com/tutorials/pyside-qresource-system/), referenced from the `resources.qrc` file in the root folder. There are two folders of images, `icons` which contains the icons for the interface and `stamps` which contains the pictures of pie for "stamping" the image when the application is running.
The `icons` were added to the UI in Qt Designer, while the stamps are loaded in the application itself using Qt Resource paths, e.g. `:/stamps/<image name>`.
The `icons` folder also contains the application icon, in `.ico` format.
### The UI in Qt Designer
The UI for Piecasso was designed using Qt Designer. Icons on the buttons and actions were set from the Qt resources file already described.
![Piecasso UI, created in Qt Designer](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/piecasso_qt_designer.png) _Piecasso UI, created in Qt Designer_
The resulting UI file was saved in the root folder of the project as `mainwindow.ui` and then compiled using the UI compiler to produce an importable `.py` file, as follows.
bash ```
pyuic5 mainwindow.ui -o MainWindow.py

```

T> For more on building UIs with Qt Designer see the [introductory tutorial](https://www.pythonguis.com/tutorials/first-steps-qt-creator/).
This build process also adds imports to `MainWindow.py` for the compiled version of the resources using in the UI, in our case `resources.qrc`. This means we do not need to import the resources separately into our app. However, we still need to build them, and use the specific name that is used for the import in `MainWindow.py`, here `resources_rc`.
bash ```
pyrcc5 resources.qrc -o resources_rc.py

```

`pyuic5` follows the pattern `&lt;resource name&gt;_rc.py` when adding imports for the resource file, so you will need to follow this when compiling resources yourself. You can check your compiled UI file (e.g. `MainWindow.py`) to double check the name of the import if you have problems.
### Building the app
With all the above setup, we can build _Piecasso_ as follows from the source folder.
bash ```
pyinstaller --windowed --icon=icons/piecasso.ico --name Piecasso paint.py

```

If you download the source code, you will also be able to run the same build using the provided `.spec` file.
bash ```
pyinstaller Piecasso.spec

```

This packages everything up ready to distribute in the `dist/Piecasso` folder. We can run the executable to ensure everything is bundled correctly, and see the following window, minus the terrible drawing.
![Piecasso Screenshot, with a poorly drawn cat](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/piecasso_cat.png) _Piecasso Screenshot, with a poorly drawn cat_
## Creating an installer
So far we've used _PyInstaller_ to bundle applications for distribution. The output of this bundling process is a folder, named `dist` which contains all the files our application needs to run.
While you _could_ share this folder with your users as a ZIP file it's not the best user experience. Desktop applications are normally distributed with _installers_ which handle the process of putting the executable (and any other files) in the correct place, adding _Start Menu_ shortcuts and the like.
Now we've successfully bundled our complex application, we'll next look at how we can take our `dist` folder and use it to create a functioning Windows installer.
To create our installer we'll be using a tool called [InstallForge](https://installforge.net/). InstallForge is free and you can download the installer from [this page](https://installforge.net/download/).
The InstallForge configuration is also in the Piecasso source folder, `Piecasso.ifp` however bear in mind that the source paths will need to be updated for your system.
Another popular tool is [NSIS](https://nsis.sourceforge.io/Main_Page) which is a _scriptable_ installer, meaning you configure it's behaviour by writing custom scripts. If you're going to be building your application frequently and want to automate the process, it's definitely worth a look.
We'll now walk through the basic steps of creating an installer with _InstallForge_. If you're impatient, you can download the [Piecasso Installer for Windows here](https://downloads.pythonguis.com/PiecassoSetup.exe).
### General
When you first run _InstallForge_ you'll be presented with this General tab. Here you can enter the basic information about your application, including the name, program version, company and website.
![InstallForge initial view, showing General settings](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/installforge_basic.png) _InstallForge initial view, showing General settings_
You can also select the target platforms for the installer, from various versions of Windows that are available. For desktop applications you currently _probably_ only want to target Windows 7, 8 and 10.
### Setup
Click on the left sidebar to open the "Files" page under "Setup". Here you can specify the files to be bundled in the installer.
Use "Add Files…" and select _all the files_ in the `dist/Piecasso` folder produced by _PyInstaller_. The file browser that pops up allows multiple file selections, so you can add them all in a single go, however you need to add folders separately. Click "Add Folder…" and add any folders under `dist/Piecasso`.
![InstallForge Files view, add all files & folders to be packaged](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/installforge_files.png) _InstallForge Files view, add all files & folders to be packaged_
Once you're finished scroll through the list to the bottom and ensure that the folders are listed to be included. You want all files and folders _under_ `dist/Piecasso` to be present. But the folder `dist/Piecasso` itself _should not_ be listed.
The default install path can be left as-is. The values between angled brackets, e.g. `&lt;company&gt;` , are variables and will be filled automatically.
Next, it's nice to allow your users to uninstall your application. Even though it's undoubtedly awesome, they may want to remove it at some time in the future. You can do this under the "Uninstall" tab, simply by ticking the box. This will also make the application appear in "Add or Remove Programs".
![InstallForge add Uninstaller for your app](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/installforge_uninstall.png) _InstallForge add Uninstaller for your app_
### Dialogs
The "Dialogs" section can be used to show custom messages, splash screens or license information to the user. The "Finish" tab lets you control what happens once the installer is complete, and it's helpful here to give the user the _option_ to run your program.
To do this you need to tick the box next to "Run program" and add your own application EXE into the box. Since `<installpath>\` is already specified, we can just add `Piecasso.exe`.
![InstallForge configure optional run program on finish install](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/installforge_finish.png) _InstallForge configure optional run program on finish install_
### System
Under "System" select "Shortcuts" to open the shortcut editor. Here you can specify shortcuts for both the Start Menu and Desktop if you like.
![InstallForge configure Shortcuts, for Start Menu and Desktop](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/installforge_shortcuts.png) _InstallForge configure Shortcuts, for Start Menu and Desktop_
Click "Add…" to add new shortcuts for your application. Choose between Start menu and Desktop shortcuts, and fill in the name and target file. This is the path your application EXE will end up at once installed. Since `<installpath>\` is already specified, you simply need to add your application's EXE name onto the end, here `Piecasso.exe`
![InstallForge, adding a Shortcut](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/installforge_shortcut_settings.png) _InstallForge, adding a Shortcut_
### Build
With the basic settings in place, you can now build your installer.
At this point you can save your _InstallForge_ project so you can re-build the installer from the same settings in future.
Click on the "Build" section at the bottom to open the build panel.
![InstallForge, ready to build](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/installforge_build.png) _InstallForge, ready to build_
Click on the large icon button to start the build process. If you haven't already specified a setup file location you will be prompted for one. This is the location where you want the _completed installer_ to be saved.
**Don't** save it in your `dist` folder.
The build process will began, collecting and compressing the files into the installer.
![InstallForge, build complete](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/installforge_build_done.png) _InstallForge, build complete_
Once complete you will be prompted to run the installer. This is entirely optional, but a handy way to find out if it works.
### Running the installer
The installer itself shouldn't have any surprises, working as expected. Depending on the options selected in _InstallForge_ you may have extra panels or options.
![InstallForge, running the resulting installer](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/installforge_installing.png) _InstallForge, running the resulting installer_
Step through the installer until it is complete. You can optionally run the application from the last page of the installer, or you can find it in your start menu.
![Piecasso in the Start Menu on Windows 10](https://www.pythonguis.com/static/tutorials/qt/qresource-system-in-packaging/installforge_installed_in_start_menu.png) _Piecasso in the Start Menu on Windows 10_
## Wrapping up
In this tutorial we've covered how to build your PySide6 applications into a distributable EXE using _PyInstaller_. Following this we walked through the steps of using _InstallForge_ to build [an installer for the app](https://downloads.pythonguis.com/PiecassoSetup.exe). Following these steps you should be able to package up your own applications and make them available to other people.
For a complete view of all _PyInstaller_ bundling options take a look at the [PyInstaller usage documentation](https://pyinstaller.readthedocs.io/en/stable/usage.html).
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Using QResource to Package Data Files With PyInstaller and PySide6** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/packaging-data-files-pyside6-with-qresource-system/Python books) on the subject. 
**Using QResource to Package Data Files With PyInstaller and PySide6** was published in [tutorials](https://www.pythonguis.com/tutorials/) on June 10, 2021 (updated March 15, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyside6](https://www.pythonguis.com/topics/pyside6/) [setup.exe](https://www.pythonguis.com/topics/setupexe/) [qresources](https://www.pythonguis.com/topics/qresources/) [setup](https://www.pythonguis.com/topics/setup/) [package](https://www.pythonguis.com/topics/package/) [pyinstaller](https://www.pythonguis.com/topics/pyinstaller/) [exe](https://www.pythonguis.com/topics/exe/) [ packaging](https://www.pythonguis.com/topics/packaging/) [installer](https://www.pythonguis.com/topics/installer/) [windows](https://www.pythonguis.com/topics/windows/) [qt](https://www.pythonguis.com/topics/qt/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ qt-designer](https://www.pythonguis.com/topics/qt-designer/) [qt-creator](https://www.pythonguis.com/topics/qt-creator/) [ pyside6-packaging](https://www.pythonguis.com/topics/pyside6-packaging/) [ pyside6-qt-designer](https://www.pythonguis.com/topics/pyside6-qt-designer/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
