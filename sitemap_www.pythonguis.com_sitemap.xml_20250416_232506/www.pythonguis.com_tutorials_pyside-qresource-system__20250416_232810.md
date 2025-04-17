# Content from: https://www.pythonguis.com/tutorials/pyside-qresource-system/

[](https://www.pythonguis.com/tutorials/pyside-qresource-system/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PySide2 ](https://www.pythonguis.com/pyside2/)
  * [PySide2 Tutorial ](https://www.pythonguis.com/pyside2-tutorial/)
  * Basics
  * [Create a PySide2 app](https://www.pythonguis.com/tutorials/pyside-creating-your-first-window/)
  * [PySide2 Signals](https://www.pythonguis.com/tutorials/pyside-signals-slots-events/)
  * [PySide2 Widgets](https://www.pythonguis.com/tutorials/pyside-widgets/)
  * [PySide2 Layouts](https://www.pythonguis.com/tutorials/pyside-layouts/)
  * [PySide2 Menus](https://www.pythonguis.com/tutorials/pyside-actions-toolbars-menus/)
  * [PySide2 Dialogs](https://www.pythonguis.com/tutorials/pyside-dialogs/)
  * [Multi-window PySide2](https://www.pythonguis.com/tutorials/pyside-creating-multiple-windows/)
  * Qt Designer
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/pyside-qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/)
  * [The QResource System in PySide2](https://www.pythonguis.com/tutorials/pyside-qresource-system/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyside-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/pyside-qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/pyside-modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/pyside-qtableview-modelviews-numpy-pandas/)
  * Plotting
  * [Plotting With PyQtGraph and PySide2](https://www.pythonguis.com/tutorials/pyside-plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PySide2](https://www.pythonguis.com/tutorials/pyside-plotting-matplotlib/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/pyside-bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/pyside-creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/pyside-animated-widgets/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/pyside-embed-pyqtgraph-custom-widgets/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/pyside-transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/pyside-system-tray-mac-menu-bar-applications/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyside2-applications-windows-pyinstaller/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyside2-applications-pyinstaller-macos-dmg/)
  * [Packaging QResources](https://www.pythonguis.com/tutorials/packaging-data-files-pyside2-with-qresource-system/)
  * [Packaging with fbs](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/)
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


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# The QResource System in PySide2
Using the QResource system to package additional data with your applications
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Mar 15 PySide2 [ Creating applications with Qt Designer ](https://www.pythonguis.com/pyside2-tutorial/#pyside-qt-designer)
#### [ PySide2 Tutorial ](https://www.pythonguis.com/pyside2-tutorial/) — [Creating applications with Qt Designer](https://www.pythonguis.com/pyside2-tutorial/#pyside-qt-designer)
  * [First Steps With Qt Designer and PySide2](https://www.pythonguis.com/tutorials/pyside-first-steps-qt-designer/)
  * [Creating Dialogs With Qt Designer and PySide2](https://www.pythonguis.com/tutorials/pyside-creating-dialogs-qt-designer/)
  * [The QResource System in PySide2](https://www.pythonguis.com/tutorials/pyside-qresource-system/)


This tutorial is also available for [PySide6](https://www.pythonguis.com/tutorials/pyside6-qresource-system/) and [PyQt5](https://www.pythonguis.com/tutorials/qresource-system/)
Building applications takes more than just code. Usually your interface will need icons for actions, you may want to add illustrations or branding logos, or perhaps your application will need to load data files to pre-populate widgets. These _data files_ are separate from the source code of your application but will ultimately need to be packaged and distributed with it in order for it to work.
Distributing data files with applications is a common cause of problems. If you reference data files with paths, your application won't work properly unless the exact same paths are available on the target computer. This can get even trickier when packaging applications for cross-platform (Windows, macOS and Linux) use. Thankfully, Qt comes to the rescue with it's _resource system_. Resources are _bundled_ into Python files which can be distributed along with your source code, guaranteeing they will continue to work on other platforms. You can manage resources through Qt Designer and use the resource library to load icons (and other data) in your apps.
Table of Contents
  * [The example application](https://www.pythonguis.com/tutorials/pyside-qresource-system/#the-example-application)
  * [The QRC file](https://www.pythonguis.com/tutorials/pyside-qresource-system/#the-qrc-file)
    * [Simple QRC example](https://www.pythonguis.com/tutorials/pyside-qresource-system/#simple-qrc-example)
  * [Using a QRC file](https://www.pythonguis.com/tutorials/pyside-qresource-system/#using-a-qrc-file)
  * [Resources in Qt Designer and Qt Creator](https://www.pythonguis.com/tutorials/pyside-qresource-system/#resources-in-qt-designer-and-qt-creator)
    * [Adding Resources in Qt Designer](https://www.pythonguis.com/tutorials/pyside-qresource-system/#adding-resources-in-qt-designer)
    * [Adding Resources in Qt Creator](https://www.pythonguis.com/tutorials/pyside-qresource-system/#adding-resources-in-qt-creator)
    * [Using resources in Qt Creator and Qt Designer](https://www.pythonguis.com/tutorials/pyside-qresource-system/#using-resources-in-qt-creator-and-qt-designer)
  * [Using a QRC file with compiled UI files](https://www.pythonguis.com/tutorials/pyside-qresource-system/#using-a-qrc-file-with-compiled-ui-files)
  * [When to use QResource?](https://www.pythonguis.com/tutorials/pyside-qresource-system/#when-to-use-qresource)


## The example application
To demonstrate how to use the resource system, we'll create a simple application that uses two data files -- in this case, two icon image files. However, remember you can package any type of data you like as resources, including data files that your application depends on.
The example below shows a single button, which when pressed changes it's icon.
python ```
import sys
from PySide2 import QtGui, QtWidgets
class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Hello World")
    self.button = QtWidgets.QPushButton("My button")
    icon = QtGui.QIcon("animal-penguin.png")
    self.button.setIcon(icon)
    self.button.clicked.connect(self.change_icon)
    self.setCentralWidget(self.button)
    self.show()
  def change_icon(self):
    icon = QtGui.QIcon("animal-monkey.png")
    self.button.setIcon(icon)

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()

```

Save this file to your computer as `app.py`. Run it and you'll see the window appear with the button, but with no icons visible. This is what happens when you create `QIcon()` objects with files that cannot be found -- they are simply omitted. _If you've had issues when packaging your applications, this will be familiar to you._
![No icons showing](https://www.pythonguis.com/static/tutorials/qt/qresources/window-noicons.png) _Without the icons available, nothing is shown._
Download and place the [animal-penguin.png](https://www.pythonguis.com/static/tutorials/qt/qresources/animal-penguin.png) and [animal-monkey.png](https://www.pythonguis.com/static/tutorials/qt/qresources/animal-monkey.png) icons in the same folder as the script, and run it again. _These icons are from the[Fugue icon set by Yusuke Kamiyamane](http://p.yusukekamiyamane.com/)._ Run the application again and you'll see the icons as expected. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyside2-book/) _by Martin Fitzpatrick_ — (PySide2 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside2-book/) [Get the book](https://secure.pythonguis.com/01hf778jyaajk5vk1q6824sd44/)
![Icons showing](https://www.pythonguis.com/static/tutorials/qt/qresources/window-icons.png) _With the icons in the same folder as the script, they are now visible._
Now the application is working as expected, we'll switch to using the `QResource` system to load these two files. First we need to define our QRC file and add our resources to it.
This might seem like overkill for 2 files, but as your projects get larger the advantages become clearer!
## The QRC file
The core of the Qt Resources system is the _resource file_ or QRC. The `.qrc` file is a simple XML file, which can be opened in any text editor.
You can also create QRC files and add and remove resources using Qt Designer, which we'll cover later.
### Simple QRC example
A very simple resource file is shown below, containing a single resource (a single icon `animal-penguin.png` we might add to a button).
xml ```
<!DOCTYPE RCC>
<RCC version="1.0">
  <qresource prefix="icons">
    <file alias="animal-penguin.png">animal-penguin.png</file>
    <file alias="animal-monkey.png">animal-monkey.png</file>
  </qresource>
</RCC>

```

The name between the `<file>` `</file>` tags is the path to the file, relative to the resource file. The `alias` is the name which this resource will be known by from within your application. You can use this _rename_ icons to something more logical or simpler in your app, while keeping the original name externally.
For example, if we want to use the name `penguin.png` internally, we can change these lines to.
xml ```
<file alias="penguin.png">animal-penguin.png</file>
<file alias="monkey.png">animal-monkey.png</file>

```

This only changes the name used _inside_ your application, the filename remains unchanged.
Outside this tag is the `qresource` tag which specifies a `prefix`. This is a _namespace_ which can be used to group resources together. This is effectively a virtual folder, under which nested resources can all be found. With our current structure, our two icons are grouped under the virtual folder `icons/`.
Save the following file as `resources.qrc`, this is our resource file which we'll use from now on.
xml ```
<!DOCTYPE RCC>
<RCC version="1.0">
  <qresource prefix="icons">
    <file alias="penguin.png">animal-penguin.png</file>
    <file alias="monkey.png">animal-monkey.png</file>
  </qresource>
</RCC>

```

## Using a QRC file
To use a `.qrc` file in your application you first need to compile it to Python. PySide comes with a command line tool to do this, which takes a `.qrc` file as input and outputs a Python file containing the compiled data. This can then be imported into your app as for any other Python file or module.
To compile our `resources.qrc` file to a Python file named `resources.py` we can use:
bash ```
pyside2-rcc resources.qrc -o resources.py

```

To use the resource file in our application we need to make a few small changes. Firstly, we need to `import resources` at the top of our app, to load the resources into the Qt resource system, and then secondly we need to update the path to the icon file to use the resource path format as follows:
The prefix `:/` indicates that this is a _resource path_. The first name "icons" is the _prefix_ namespace and the filename is taken from the file _alias_ , both as defined in our `resources.qrc` file.
The updated application is shown below.
python ```
import sys
from PySide2 import QtGui, QtWidgets
import resources
class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Hello World")
    self.button = QtWidgets.QPushButton("My button")
    icon = QtGui.QIcon(":/icons/penguin.png")
    self.button.setIcon(icon)
    self.button.clicked.connect(self.change_icon)
    self.setCentralWidget(self.button)
    self.show()
  def change_icon(self):
    icon = QtGui.QIcon(":/icons/monkey.png")
    self.button.setIcon(icon)

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()

```

If you run this now, it will look exactly as before, but now the icons are being loaded from the `resources.py` compile resource file.
![Icons visible](https://www.pythonguis.com/static/tutorials/qt/qresources/window-icons.png) _Icons visible, loading from the QRC file._
## Resources in Qt Designer and Qt Creator
While it's fairly straightforward to manage your resources by editing the QRC file directly, _Qt Designer_ can also be used to edit the resource library. This allows you to see all the icons (and other data) visually, rearrange them and edit them by drag-and-drop.
### Adding Resources in Qt Designer
If you're using the standalone Qt Designer, the resource browser is available as a dockable widget, visible in the bottom right by default. If the Resource Browser is hidden you can show it through the "View" menu on the toolbar.
To add, edit and remove resource files click on the pencil icon in the Resource browser panel. This will open the resource editor.
![Standalone Qt Designer view](https://www.pythonguis.com/static/tutorials/qt/qresources/qt_designer.png) _Standalone Qt Designer view_
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
In the resource editor view you can open an existing resource file by clicking on the document folder icon (middle icon) on the bottom left.
![Edit Resources in Qt Designer](https://www.pythonguis.com/static/tutorials/qt/qresources/qt_designer_resource_editor.png) _Edit Resources in Qt Designer_
On the left hand panel you can also create and delete resource files from your UI. While on the right you can create new prefixes, add files to the prefix and delete items. Changes to the resource file are saved automatically.
### Adding Resources in Qt Creator
In order to be able to add icons using the Qt Resource system from within Qt Creator you need to have an active Qt Project, and add both your UI and resource files to it.
If you don't have a Qt Creator project set up you can create one in your existing source folder. Qt Creator will prompt before overwriting any of your files. Click on "+ New", choose "Qt for Python - Empty" for project type. Select the folder _above_ your source folder for "Create in", and provide the name of your source folder as the project name. You can delete any files created, except the `.pyproject` which holds the project settings.
![Select the location](https://www.pythonguis.com/static/tutorials/qt/qresources/qt_python_location_exists.png) _Select the location_
To add resources to your existing project, select the "Edit" view on the left hand panel. You will see a file tree browser in the left hand panel. Right-click on the folder and choose "Add existing files…" and add your existing `.qrc` file to the project.
![The Edit view, showing the added files](https://www.pythonguis.com/static/tutorials/qt/qresources/qt_python_edit_view.png) _The Edit view, showing the added files_
The UI doesn't update when you add/remove things here, this seems to be a bug in Qt Creator. If you close and re-open Qt Creator the files will be there.
Once you have added the QRC file to the file listing you should be able to expand the file as if it were a folder, and browser the resources within. You can also add and remove resources using this interface.
### Using resources in Qt Creator and Qt Designer
Once the Resource file is loaded you will be able to access it from the designer properties. The screenshot below shows the Designer with our counter app open, and the _increment_ button selected. The icon for the button can be chosen by clicking the small black down arrow and selecting "Choose Resource…"
![Select the location](https://www.pythonguis.com/static/tutorials/qt/qresources/qt_python_designer.png) _Select the location_
The Resource chooser window that appears allows you to pick icons from the resource file(s) in the project to use in your UI.
![Select the location](https://www.pythonguis.com/static/tutorials/qt/qresources/qt_python_designer_resource.png) _Select the location_
Selecting the icons from the resource file in this way ensures that they will always work, as long as you compile and bundle the compiled resource file with your app.
## Using a QRC file with compiled UI files
If you're designing your UIs in Qt Designer and compiling the resulting UI file to Python, then UI compiler automatically adds imports to a _compiled_ version of your Qt Resource file for you. For example, if you run the following --
bash ```
pyside2-uic mainwindow.ui -o MainWindow.py

```

This build process also adds imports to `MainWindow.py` for the compiled version of the resources using in the UI, in our case `resources.qrc`. This means you do not need to import the resources separately into your app. However, we still need to build them, and use the specific name that is used for the import in `MainWindow.py`, here `resources_rc`.
bash ```
pyside2-rcc resources.qrc -o resources_rc.py

```

The command line tools follow the pattern `<resource name>_rc.py` when adding imports for the resource file, so you will need to follow this when compiling resources yourself. You can check your compiled UI file (e.g. `MainWindow.py`) to double check the name of the import if you have problems.
## When to use `QResource`?
You may be wondering when (or even _whether_) you should use the `QResource` system.
The main advantage comes when packaging and distributing your applications. Because your data is bundled with the Python source code, you eliminate all the potential path problems and guarantee your data files will be accessible to your app. You can also use _Qt Designer_ to manage and group icons for your application. The downside of course is you need to re-compile your resources any time you add/remove new resources.
Whether this trade-off is worth it for your project is up to you, but if you plan to distribute your application to other people it almost always is.
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**The QResource System in PySide2** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/pyside-qresource-system/Python books) on the subject. 
**The QResource System in PySide2** was published in [tutorials](https://www.pythonguis.com/tutorials/) on December 16, 2020 (updated March 15, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [ packaging](https://www.pythonguis.com/topics/packaging/) [ qt-designer](https://www.pythonguis.com/topics/qt-designer/) [qt-creator](https://www.pythonguis.com/topics/qt-creator/) [ pyside2-packaging](https://www.pythonguis.com/topics/pyside2-packaging/) [ pyside2-qt-designer](https://www.pythonguis.com/topics/pyside2-qt-designer/) [python](https://www.pythonguis.com/topics/python/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
