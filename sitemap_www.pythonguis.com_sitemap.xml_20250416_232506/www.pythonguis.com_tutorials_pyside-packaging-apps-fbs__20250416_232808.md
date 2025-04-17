# Content from: https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/

[](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/#menu)
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
# Packaging PySide apps with fbs
Distribute cross-platform GUI applications with the fman Build System
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PySide2 [ Packaging and distribution ](https://www.pythonguis.com/pyside2-tutorial/#pyside-packaging-and-distribution)
#### [ PySide2 Tutorial ](https://www.pythonguis.com/pyside2-tutorial/) — [Packaging and distribution](https://www.pythonguis.com/pyside2-tutorial/#pyside-packaging-and-distribution)
  * [Packaging PySide2 applications for Windows with PyInstaller & InstallForge](https://www.pythonguis.com/tutorials/packaging-pyside2-applications-windows-pyinstaller/)
  * [Packaging PySide2 applications into a macOS app with PyInstaller](https://www.pythonguis.com/tutorials/packaging-pyside2-applications-pyinstaller-macos-dmg/)
  * [Using QResource to Package Data Files With PyInstaller and PySide2](https://www.pythonguis.com/tutorials/packaging-data-files-pyside2-with-qresource-system/)
  * [Packaging PySide apps with fbs](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/)


This tutorial is also available for [PyQt5](https://www.pythonguis.com/tutorials/packaging-pyqt5-apps-fbs/)
**fbs** is a cross-platform PySide packaging system which supports building desktop applications for Windows, Mac and Linux (Ubuntu, Fedora and Arch). Built on top of _PyInstaller_ it wraps some of the rough edges and defines a standard project structure which allows the build process to be entirely automated. The included resource API is particularly useful, simplifying the handling of external data files, images or third-party libraries — a common pain point when bundling apps.
This tutorial will take you through the steps of creating PySide applications using **fbs** from scratch, and for converting existing projects over to the system.
If you're impatient, you can grab the Moonsweeper installers directly for [Windows](https://downloads.pythonguis.com/MoonsweeperSetup.exe), [MacOS](https://downloads.pythonguis.com/Moonsweeper.dmg) or [Linux (Ubuntu)](https://downloads.pythonguis.com/Moonsweeper.deb).
**fbs** is licensed under the GPL. This means you can use the **fbs** system for free in packages distributed with the GPL. For non-GPL packages you must buy a commercial license. See the fbs licensing page for up-to-date information.
**fbs** is built on top of PyInstaller. You can also use PyInstaller directly to package applications, see our [Packaging PySide2 applications for Windows, with PyInstaller](https://www.pythonguis.com/tutorials/packaging-pyside2-applications-windows-pyinstaller/) tutorial.
Table of Contents
  * [Install requirements](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/#install-requirements)
  * [Starting an app](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/#starting-an-app)
    * [Running your new project](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/#running-your-new-project)
    * [The application structure](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/#the-application-structure)
    * [The ApplicationContext](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/#the-applicationcontext)
  * [Building a real application](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/#building-a-real-application)
    * [The cached_property decorator](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/#the-cached_property-decorator)
    * [Accessing resources with .get_resource](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/#accessing-resources-with-get_resource)
    * [Using the ApplicationContext from app](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/#using-the-applicationcontext-from-app)
  * [Freezing the app](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/#freezing-the-app)
  * [Creating the Installer](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/#creating-the-installer)
  * [Windows installer](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/#windows-installer)
  * [Mac installer](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/#mac-installer)
  * [Linux installer](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/#linux-installer)


## Install requirements
**fbs** is compatible with Python `PySide2`. The only other requirement is `PyInstaller` which handles the packaging itself. You can install these in a virtual environment (or your applications virtual environment) to keep your environment clean.
fbs only supports Python versions 3.5 and 3.6 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
bash ```
python3 -m venv fbsenv

```

Once created, activate the virtual environment by running from the command line —
bash ```
# On Mac/Linux:
source fbsenv/bin/activate
# On Windows:
call fbsenv\scripts\activate.bat

```

Finally, install the required libraries. For PySide2 you would use —
python ```
pip3 install fbs PySide2 PyInstaller==3.4

```

**fbs** installs a command line tool `fbs` into your path which provides access to all **fbs** management commands. To see the complete list of commands available run `fbs`.
bash ```
martin@Martins-Laptop testapp $ fbs
usage: fbs [-h]
      {startproject,run,freeze,installer,sign_installer,repo,
      upload,release,test,clean,buildvm,runvm,gengpgkey,register,login,init_licensing}
      ...
fbs
positional arguments:
 {startproject,run,freeze,installer,sign_installer,repo,
 upload,release,test,clean,buildvm,runvm,gengpgkey,register,login,init_licensing}
  startproject    Start a new project in the current directory
  run         Run your app from source
  freeze       Compile your code to a standalone executable
  installer      Create an installer for your app
  sign_installer   Sign installer, so the user's OS trusts it
  repo        Generate files for automatic updates
  upload       Upload installer and repository to fbs.sh
  release       Bump version and run clean,freeze,...,upload
  test        Execute your automated tests
  clean        Remove previous build outputs
  buildvm       Build a Linux VM. Eg.: buildvm ubuntu
  runvm        Run a Linux VM. Eg.: runvm ubuntu
  gengpgkey      Generate a GPG key for Linux code signing
  register      Create an account for uploading your files
  login        Save your account details to secret.json
  init_licensing   Generate public/private keys for licensing
optional arguments:
 -h, --help      show this help message and exit

```

Now you're ready to start packaging applications with **fbs**.
## Starting an app
If you’re starting a PySide2 application from scratch, you can use the `fbs startproject` management command to create a complete, working and packageable application stub in the current folder. This has the benefit of allowing you to test (and continue to test) the packageability of your application as you develop it, rather than leaving it to the end.
bash ```
fbs startproject

```

The command walks you through a few questions, allowing you to fill in details of your application. These values will be written into your app source and configuration. The bare-bones app will be created under the `src/` folder in the current directory.
bash ```
martin@Martins-Laptop ~ $ fbs startproject
App name [MyApp] : HelloWorld
Author [Martin] : Martin Fitzpatrick
Mac bundle identifier (eg. com.martin.helloworld, optional):

```

If you already have your own working PySide2 app you will need to either a) use the generated app as a guideline for converting yours to the same structure, or b) create a new app using `startproject` and migrate the code over.
### Running your new project
You can run this new application using the following **fbs** command in the same folder you ran `startproject` from.
bash ```
fbs run

```

If everything is working this should show you a small empty window with your apps' title — exciting eh?
![Hello World App on Windows](https://www.pythonguis.com/static/tutorials/qt/packaging-apps-fbs/hello-world-windows.png) _Hello World App on Windows_
![Hello World App on Mac](https://www.pythonguis.com/static/tutorials/qt/packaging-apps-fbs/hello-world-mac.png) _Hello World App on Mac_
![Hello World App on Linux](https://www.pythonguis.com/static/tutorials/qt/packaging-apps-fbs/hello-world-ubuntu.png) _Hello World App on Linux_
### The application structure
The `startproject` command generates the required folder structure for a **fbs** PySide2 application. This includes a `src/build` which contains the build settings for your package, `main/icons` which contains the application icons, and `src/python` for the source.
bash ```
.
└── src
  ├── build
  │   └── settings
  │     ├── base.json
  │     ├── linux.json
  │     └── mac.json
  └── main
    ├── icons
    │   ├── Icon.ico
    │   ├── README.md
    │   ├── base
    │   │   ├── 16.png
    │   │   ├── 24.png
    │   │   ├── 32.png
    │   │   ├── 48.png
    │   │   └── 64.png
    │   ├── linux
    │   │   ├── 1024.png
    │   │   ├── 128.png
    │   │   ├── 256.png
    │   │   └── 512.png
    │   └── mac
    │     ├── 1024.png
    │     ├── 128.png
    │     ├── 256.png
    │     └── 512.png
    └── python
      └── main.py

```

Your bare-bones PySide2 application is generated in `src/main/python/main.py` and is a complete working example you can use to base your own code on.
python ```
from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow
import sys
class AppContext(ApplicationContext):      # 1. Subclass ApplicationContext
  def run(self):               # 2. Implement run()
    window = QMainWindow()
    version = self.build_settings['version']
    window.setWindowTitle("HelloWorld v" + version)
    window.resize(250, 150)
    window.show()
    return self.app.exec_()         # 3. End run() with this line
if __name__ == '__main__':
  appctxt = AppContext()           # 4. Instantiate the subclass
  exit_code = appctxt.run()          # 5. Invoke run()
  sys.exit(exit_code)

```

If you’ve built PySide applications before you’ll notice that building an application with **fbs** introduces a new concept — the `ApplicationContext`.
### The `ApplicationContext`
When building PySide2 applications there are typically a number of components or resources that are used throughout your app. These are commonly stored in the `QMainWindow` or as global vars which can get a bit messy as your application grows. The `ApplicationContext` provides a central location for initializing and storing these components, as well as providing access to some core **fbs** features.
The `ApplicationContext` object also creates and holds a reference to a global `QApplication` object — available under `ApplicationContext.app`. Every Qt application must have one (and only one) `QApplication` to hold the event loop and core settings. Without **fbs** you would usually define this at the base of your script, and call `.exec()` to start the event loop.
Without **fbs** this would look something like this — 
python ```
if __name__ == '__main__':
  app = QApplication()
  w = MyCustomWindow()
  app.exec_()

```

The equivalent with **fbs** would be —
python ```
if __name__ == '__main__':
  ctx = ApplicationContext()
  w = MyCustomWindow()
  ctx.app.exec_()

```

If you want to create your own custom `QApplication` initialization you can overwrite the `.app` property on your `ApplicationContext` subclass using `cached_property` (see below).
This basic example is clear to follow. However, once you start adding custom styles and translations to your application the initialization can grow quite a bit. To keep things nicely structured **fbs** recommends creating a `.run` method on your `ApplicationContext`.
This method should handle the setup of your application, such as creating and showing a window, finally starting up the event loop on the `.app` object. This final step is performed by calling `self.app.exec_()` at the end of the method.
python ```
class AppContext(ApplicationContext):
  def run(self):
    ...
    return self.app.exec_()

```

As your initialization gets more complicated you can break out subsections into separate methods for clarity, for example —
python ```
class AppContext(ApplicationContext):
  def run(self):
    self.setup_fonts()
    self.setup_styles()
    self.setup_translations()
    return self.app.exec_()
  def setup_fonts(self):
    # ...do something ...
  def setup_styles(self):
    # ...do something ...
  def setup_translations(self):
    # ...do something ...

```

On execution the `.run()` method will be called and your event loop started. Execution continues in this event loop until the application is exited, at which point your `.run()` method will return (with the appropriate exit code).
## Building a real application
The bare-bones application doesn’t do very much, so below we’ll look at something more complete — the _Moonsweeper_ application from my [15 minute apps](http://github.com/mfitzp/15-minute-apps/). The updated source code is available to download below.
[Moonsweeper Source (fbs) PySide2](https://www.pythonguis.com/d/moonsweeper-fbs-pyside2.zip)
Only the changes required to convert _Moonsweeper_ over to **fbs** are covered here. If you want to see how_ Moonsweeper_ itself works, see the original App article. The custom application icons were created using icon art by [Freepik](https://www.flaticon.com/authors/freepik/).
The project follows the same basic structure as for the stub application we created above.
python ```
.
├── README.md
├── requirements.txt
├── screenshot-minesweeper1.jpg
├── screenshot-minesweeper2.jpg
└── src
  ├── build
  │   └── settings
  │     ├── base.json
  │     ├── linux.json
  │     └── mac.json
  └── main
    ├── Installer.nsi
    ├── icons
    │   ├── Icon.ico
    │   ├── README.md
    │   ├── base
    │   │   ├── 16.png
    │   │   ├── 24.png
    │   │   ├── 32.png
    │   │   ├── 48.png
    │   │   └── 64.png
    │   ├── linux
    │   │   ├── 1024.png
    │   │   ├── 128.png
    │   │   ├── 256.png
    │   │   └── 512.png
    │   └── mac
    │     ├── 1024.png
    │     ├── 128.png
    │     ├── 256.png
    │     └── 512.png
    ├── python
    │   ├── __init__.py
    │   └── main.py
    └── resources
      ├── base
      │   └── images
      │     ├── bomb.png
      │     ├── bug.png
      │     ├── clock-select.png
      │     ├── cross.png
      │     ├── flag.png
      │     ├── plus.png
      │     ├── rocket.png
      │     ├── smiley-lol.png
      │     └── smiley.png
      └── mac
        └── Contents
          └── Info.plist

```

The `src/build/settings/base.json` stores the basic details about the application, including the entry point to run the app with `fbs run` or once packaged.
json ```
{
  "app_name": "Moonsweeper",
  "author": "Martin Fitzpatrick",
  "main_module": "src/main/python/main.py",
  "version": "0.0.0"
}

```

The script _entry point_ is at the base of `src/main/python/main.py`. This creates the `AppContext` object and calls the `.run()` method to start up the app.
python ```
if __name__ == '__main__':
  appctxt = AppContext()
  exit_code = appctxt.run()
  sys.exit(exit_code)

```

The `ApplicationContext` defines a `.run()` method to handle initialization. In this case that consists of creating and showing the main window, then starting up the event loop.
python ```
from fbs_runtime.application_context.PySide2 import ApplicationContext, \
  cached_property

class AppContext(ApplicationContext):
  def run(self):
    self.main_window.show()
    return self.app.exec_()
  @cached_property
  def main_window(self):
    return MainWindow(self) # Pass context to the window.
  # ... snip ...

```

### The `cached_property` decorator
The `.run()` method accesses `self.main_window`. You’ll notice that this method is wrapped in an **fbs** `@cached_property` decorator. This decorator turns the method into a property (like the Python `@property` decorator) and caches the return value.
The first time the property is accessed the method is executed and the return value cached. On subsequent calls, the cached value is returned directly without executing anything. This also has the side-effect of postponing creation of these objects until they are needed.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
You can use `@cached_property` to define each application component (a window, a toolbar, a database connection or other resources). However, you don’t _have_ to use the `@cached_property` — you could alternatively declare all properties in your `ApplicationContext.__init__` block as shown below.
python ```
from fbs_runtime.application_context.PySide2 import ApplicationContext
class AppContext(ApplicationContext):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.window = Window()
  def run(self):
    self.window.show()
    return self.app.exec_()

```

### Accessing resources with `.get_resource`
Applications usually require additional data files beyond the source code — for example files icons, images, styles (Qt’s `.qss` files) or documentation. You may also want to bundle platform-specific libraries or binaries. To simplify this **fbs** defines a folder structure and access method which work seamlessly across development and distributed versions.
The top level folder `resources/` should contain a folder `base` plus any combination of the other folders shown below. The `base` folder contains files common to all platforms, while the platform-specific folders can be used for any files specific to a given OS.
bash ```
base/      # for files required on all OSs
windows/    # for files only required on Windows
mac/      # " "   "  "    " Mac
linux/     # " "   "  "    " Linux
arch/      # " "   "  "    " Arch Linux
fedora/     # " "   "  "    " Debian Linux
ubuntu/     # " "   "  "    " Ubuntu Linux

```

Getting files into the right place to load from a distributed app across all platforms is usually one of the faffiest bits of distributing PySide applications. It’s really handy that **fbs** handles this for you.
To simplify the loading of resources from your `resources/` folder in your applications **fbs** provides the `ApplicationContext.get_resource()` method. This method takes the name of a file which can be found somewhere in the `resources/` folder and returns the absolute path to that file. You can use this returned absolute path to open the file as normal.
python ```
from fbs_runtime.application_context.PySide2 import ApplicationContext, cached_property

class AppContext(ApplicationContext):
  # ... snip ...
  @cached_property
  def img_bomb(self):
    return QImage(self.get_resource('images/bug.png'))
  @cached_property
  def img_flag(self):
    return QImage(self.get_resource('images/flag.png'))
  @cached_property
  def img_start(self):
    return QImage(self.get_resource('images/rocket.png'))
  @cached_property
  def img_clock(self):
    return QImage(self.get_resource('images/clock-select.png'))
  @cached_property
  def status_icons(self):
    return {
      STATUS_READY: QIcon(self.get_resource("images/plus.png")),
      STATUS_PLAYING: QIcon(self.get_resource("images/smiley.png")),
      STATUS_FAILED: QIcon(self.get_resource("images/cross.png")),
      STATUS_SUCCESS: QIcon(self.get_resource("images/smiley-lol.png"))
    }
  # ... snip ...

```

In our _Moonsweeper_ application above, we have a _bomb_ image file available at `src/main/resources/base/images/bug.jpg`. By calling `ctx.get_resource('images/bug.png')` we get the absolute path to that image file on the filesystem, allowing us to open the file within our app.
If the file does not exist `FileNotFoundError` will be raised instead.
The handy thing about this method is that it transparently handles the platform folders under `src/main/resources` giving OS-specific files precedence. For example, if the same file was also present under `src/main/resources/mac/images/bug.jpg` and we called `ctx.get_resource('images/bug.jpg')` we would get the Mac version of the file.
Additionally `get_resource` works both when running from source and when running a frozen or installed version of your application. If your `resources/` load correctly locally you can be confident they will load correctly in your distributed applications.
### Using the `ApplicationContext` from app
As shown above, our `ApplicationContext` object has cached properties to load and return the resources. To allow us to access these from our `QMainWindow` we can pass the context in and store a reference to it in our window `__init__`.
python ```
class MainWindow(QMainWindow):
  def __init__(self, ctx):
    super().__init__()
    self.ctx = ctx # Store a reference to the context for resources, etc.
# ... snip ...

```

Now that we have access to the context via `self.ctx` we can use it this in any place we want to reference these external resources.
python ```
    l = QLabel()
    l.setPixmap(QPixmap.fromImage(self.ctx.img_bomb))
    l.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
    hb.addWidget(l)
# ... snip ...
    l = QLabel()
    l.setPixmap(QPixmap.fromImage(self.ctx.img_clock))
    l.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    hb.addWidget(l)

```

The first time we access `self.ctx.img_bomb` the file will be loaded, the `QImage` created and returned. On subsequent calls, we’ll get the image from the cache.
python ```
  def init_map(self):
    # Add positions to the map
    for x in range(0, self.b_size):
      for y in range(0, self.b_size):
        w = Pos(x, y, self.ctx.img_flag, self.ctx.img_start, self.ctx.img_bomb)
        self.grid.addWidget(w, y, x)
        # Connect signal to handle expansion.
        w.clicked.connect(self.trigger_start)
        w.expandable.connect(self.expand_reveal)
        w.ohno.connect(self.game_over)
# ... snip ...
    self.button.setIcon(self.ctx.status_icons[STATUS_PLAYING])
# ... snip ...
  def update_status(self, status):
    self.status = status
    self.button.setIcon(self.ctx.status_icons[self.status])

```

Those are all the changes needed to get the _Moonsweeper_ app packageable with **fbs**. If you open up the source folder you should be able to start it up as before.
bash ```
fbs run

```

If that’s working, you’re ready to move onto freezing and building in the installer.
## Freezing the app
_Freezing_ is the process of turning a Python application into a standalone executable that can run on another user’s computer. Use the following command to turn the app's source code into a standalone executable:
python ```
fbs freeze

```

The resulting executable depends on the platform you _freeze_ on — the executable will only work on the OS you built it on (e.g. an executable built on Windows will run on another Windows computer, but not on a Mac).
  * Windows will create an `.exe` executable in the folder `target/<AppName>`
  * MacOS X will create an `.app` application bundle in `target/<AppName>.app`
  * Linux will create an executable in the folder `target/<AppName>`


On Windows you may need to install the [Windows 10 SDK](https://dev.windows.com/en-us/downloads/windows-10-sdk), although **fbs** will prompt you if this is the case.
## Creating the Installer
While you can share the executable files with users, desktop applications are normally distributed with _installers_ which handle the process of putting the executable (and any other files) in the correct place. See the following sections for platform-specific notes before creating
You must _freeze_ your app first _then_ create the installer.
## Windows installer
The Windows installer allows your users to pick the installation directory for the executable and adds your app to the user’s Start Menu. The app is also added to installed programs, allowing it to be uninstalled by your users.
Before you create installers on Windows you will need to install [NSIS](http://nsis.sourceforge.net/Main_Page) and ensure its installation directory is in your `PATH`. You can then build an installer using —
bash ```
fbs installer

```

The Windows installer will be created at `target/<AppName>Setup.exe`.
[Moonsweeper Windows Installer](https://www.pythonguis.com/d/MoonsweeperSetup_baG7uxK.exe)
![Moonsweeper Windows NSIS installer](https://www.pythonguis.com/static/tutorials/qt/packaging-apps-fbs/moonsweeper-installer-windows.png) _Moonsweeper Windows NSIS installer_
## Mac installer
There are no additional steps to create a MacOS installer. Just run the **fbs** command —
bash ```
fbs installer

```

On Mac the command will generate a disk image at `target/<AppName>.dmg`. This disk image will contain the app bundle and a shortcut to the Applications folder. When your users open it they can drag the app to the Applications folder to install it.
[Download the _Moonsweeper_ .dmg bundle here](https://downloads.pythonguis.com/Moonsweeper.dmg)
[Moonsweeper macOS Installer](https://www.pythonguis.com/d/Moonsweeper_rbQAuYf.dmg)
![Moonsweeper Mac Disk Image](https://www.pythonguis.com/static/tutorials/qt/packaging-apps-fbs/moonsweeper-installer-mac_JGHs5Ez.png) _Moonsweeper Mac Disk Image_
## Linux installer
To build installers on Linux you need to install the Ruby tool [Effing package management!](https://github.com/jordansissel/fpm) — use [the installation guide](https://fpm.readthedocs.io/en/latest/installing.html) to get it set up. Once that is in place you can use the standard command to create the Linux package file.
bash ```
fbs installer

```

The resulting package will be created under the `target/` folder. Depending on your platform the package file will be named `<AppName>.deb`, `<AppName>.pkg.tar.xz` or `<AppName>.rpm`. Your users can install this file with their package manager.
[Moonsweeper Ubuntu Installer](https://www.pythonguis.com/d/Moonsweeper_vZmFhBa.deb)
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Packaging PySide apps with fbs** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/pyside-packaging-apps-fbs/Python books) on the subject. 
**Packaging PySide apps with fbs** was published in [tutorials](https://www.pythonguis.com/tutorials/) on March 20, 2019 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[fbs](https://www.pythonguis.com/topics/fbs/) [ packaging](https://www.pythonguis.com/topics/packaging/) [distribution](https://www.pythonguis.com/topics/distribution/) [qt](https://www.pythonguis.com/topics/qt/) [pyside](https://www.pythonguis.com/topics/pyside/) [python](https://www.pythonguis.com/topics/python/)
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
