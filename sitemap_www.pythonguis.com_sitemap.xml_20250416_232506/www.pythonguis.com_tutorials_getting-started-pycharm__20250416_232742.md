# Content from: https://www.pythonguis.com/tutorials/getting-started-pycharm/

[](https://www.pythonguis.com/tutorials/getting-started-pycharm/#menu)
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
# Getting Started With PyCharm for Python GUI Development
The Python-Specific Integrated Development Environment
by [Lalin Paranawithana](https://www.pythonguis.com/authors/lalin-paranawithana/) Last updated Apr 08 [ Tutorials ](https://www.pythonguis.com/tutorials/)
Setting up a good development environment for Python can make the coding process friendly and provide the necessary tools to maintain the codebase for many years to come. Choosing the right tools and being comfortable with them is a critical step for a Python developer.
Code editors are among the most common and used development tools. They're where we write the code. While most modern code editors support features like syntax highlighting, which shows visual cues to differentiate parts of the source code, we often need to rely on external tools to help us debug and look for errors, install packages, manage Python environments, and so on.
To have all these features in a single program, you'll need an integrated development environment (IDE). Although there are several Python IDEs, in this article, we'll be exploring PyCharm, which is a powerful IDE for Python developers.
Table of Contents
  * [Install Python](https://www.pythonguis.com/tutorials/getting-started-pycharm/#install-python)
  * [Install PyCharm](https://www.pythonguis.com/tutorials/getting-started-pycharm/#install-pycharm)
  * [Create a New Project](https://www.pythonguis.com/tutorials/getting-started-pycharm/#create-a-new-project)
  * [Get Familiar With PyCharm's Interface](https://www.pythonguis.com/tutorials/getting-started-pycharm/#get-familiar-with-pycharms-interface)
    * [Window Header](https://www.pythonguis.com/tutorials/getting-started-pycharm/#window-header)
    * [Editor](https://www.pythonguis.com/tutorials/getting-started-pycharm/#editor)
    * [Sidebar and Tool Windows](https://www.pythonguis.com/tutorials/getting-started-pycharm/#sidebar-and-tool-windows)
    * [Status Bar](https://www.pythonguis.com/tutorials/getting-started-pycharm/#status-bar)
  * [Install Python Packages](https://www.pythonguis.com/tutorials/getting-started-pycharm/#install-python-packages)
  * [Write the Code](https://www.pythonguis.com/tutorials/getting-started-pycharm/#write-the-code)
  * [Run the Code](https://www.pythonguis.com/tutorials/getting-started-pycharm/#run-the-code)
  * [Configure the Python Environment](https://www.pythonguis.com/tutorials/getting-started-pycharm/#configure-the-python-environment)
  * [Use Git for Version Control](https://www.pythonguis.com/tutorials/getting-started-pycharm/#use-git-for-version-control)
    * [Track Changes in a Project](https://www.pythonguis.com/tutorials/getting-started-pycharm/#track-changes-in-a-project)
    * [Share a Project on GitHub](https://www.pythonguis.com/tutorials/getting-started-pycharm/#share-a-project-on-github)
  * [Explore Other Useful Features in PyCharm](https://www.pythonguis.com/tutorials/getting-started-pycharm/#explore-other-useful-features-in-pycharm)
    * [Search Everywhere](https://www.pythonguis.com/tutorials/getting-started-pycharm/#search-everywhere)
    * [Code With Me](https://www.pythonguis.com/tutorials/getting-started-pycharm/#code-with-me)
    * [Sync Python Requirements](https://www.pythonguis.com/tutorials/getting-started-pycharm/#sync-python-requirements)
    * [Todos](https://www.pythonguis.com/tutorials/getting-started-pycharm/#todos)
    * [Scratches](https://www.pythonguis.com/tutorials/getting-started-pycharm/#scratches)
    * [Plugin Marketplace](https://www.pythonguis.com/tutorials/getting-started-pycharm/#plugin-marketplace)
  * [Summary](https://www.pythonguis.com/tutorials/getting-started-pycharm/#summary)


## Install Python
Before installing PyCharm, we need to make sure that Python is installed on the development machine. If it isn't intalled yet, then we can go to the official [download](https://www.python.org/downloads/) page and grab the specific installer for either Windows or macOS.
Make sure to select the _Add Python to PATH_ option during the installation process.
On Linux systems, you can check if Python is already installed by running `python3 --version` in a terminal. If this command returns an error, then you need to install Python from your distribution's repository or from the [source](https://www.python.org/downloads/source/).
If you're running a Debian-based distribution, such as Ubuntu and Linux Mint, you can install Python by running `sudo apt install python3`. It may be necessary to run `sudo apt install python3-pip python3-venv`, so that PyCharm can use `pip` and `venv` to install packages and manage virtual environments.
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
## Install PyCharm
We have a few different ways to install PyCharm. The recommended way is to head over to [the official download page](https://www.jetbrains.com/pycharm/) and grab the standalone installer for Windows, macOS, or Linux. Then, you'll need to run the installer and follow the on-screen instructions.
If you're using a [Linux distro that supports Snaps](https://snapcraft.io/docs/installing-snapd), you can also install it by running `sudo snap install pycharm-community --classic` in your terminal.
PyCharm has a Community edition, which is free and open-source. It also has a Professional edition, which is paid. While this tutorial uses PyCharm Community edition, the coverd topics applies to both editions. Check out the [comparison](https://www.jetbrains.com/products/compare/?product=pycharm&product=pycharm-ce) between both editions for the details.
Alternatively, you could install PyCharm via the [Toolbox](https://www.jetbrains.com/toolbox-app/) app, which makes it easier to update or rollback to any version of PyCharm. This app can also be used to install and manage other JetBrains products.
**NOTE:** For more platform-specific information, check out PyCharm's [installation guide](https://www.jetbrains.com/help/pycharm/installation-guide.html).
## Create a New Project
To demonstrate PyCharm's workflow, we'll create a basic Python GUI app using [PyQt](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/). Before we start writing code, we need to first launch PyCharm and create a new project. Creating a project helps you differentiate between files, code, packages, and settings.
Go ahead and laugh PyCharm. Depending on your operating system, you can run PyCharm by going to the _Start Menu_ on Windows, _Launchpad_ on macOS, or by running the `pycharm` executable (under `install-folder/bin`) on Linux. However, if you installed PyCharm using Toolbox, then open the Toolbox app and launch PyCharm from there.
Read the PyCharm documentation to learn how to [run PyCharm from the command-line interface](https://www.jetbrains.com/help/pycharm/working-with-the-ide-features-from-command-line.html).
When we launch PyCharm, the first thing we'll see is its _Welcome to PyCharm_ window:
![PyCharm's Welcome window](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-elcome-window.png) _PyCharm's Welcome window_
Here's where we can create new projects or open existing ones—either stored locally on our computer or in online code repositories like GitHub.
To continue, click the _New Project_ button and then choose a project's name and location folder in the _New Project_ window. You can also define the Python environment to use but keep the default configuration for now:
![PyCharm's New Project window](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-new-project-window.png) _PyCharm's New Project window_
Finally, click the _Create_ button on the lower, right corner to create the project and open it in PyCharm's main window, also known as _Project Window_.
## Get Familiar With PyCharm's Interface
The _Project Window_ is where we'll spend most of our time in PyCharm. It's where we manage files, write code, install packages, and do everything related to the project we are working on.
**NOTE:** This article covers PyCharm's [modern user interface](https://www.jetbrains.com/help/pycharm/new-ui.html). You can also use the [classic](https://www.jetbrains.com/help/pycharm/guided-tour-around-the-user-interface.html#-85wxb7_31) user interface by going to _File - > Settings_ and disabling _New UI_ under _Appearance & Behaviour_. On macOS, you can access the _Settings_ menu from the _Menu Bar_ at the top of your screen.
Let's examine the components of PyCharm's interface and see what they do:
![PyCharm's Project Window](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-project-window.png) _PyCharm's Project Window_
The _Project Window_ interface has the following four main components:
  1. Window Header
  2. Editor
  3. Sidebar
  4. Status bar


In the following sections, we'll explore these UI components in more detail.
### Window Header
The _Window Header_ is at the very top of PyCharm's _Project Window_ and gives us quick access to some commonly used features, most notably the _Run_ button. Using the _Run_ button, we can run or debug our Python project directly from PyCharm — without having to type the relevant Python command in a terminal.
The _Window Header_ looks something like this:
![PyCharm's Window Header](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-window-header.png) _PyCharm's Window Header_
Other significant components of the _Window Header_ are the _Main Menu_ and the _Project widget_.
PyCharm's _Main Menu_ is accessible by clicking on the _hamburger menu_ , whereas the _Project widget_ displays the name of the current project and allows us to switch between projects as well as create new ones.
On macOS, however, we doesn't have a _hamburger menu_ in the _Window Header_ but we can still access PyCharm's _Main Menu_ throuhg the _Menu Bar_ at the top of the screen, like with other macOS apps.
### Editor
The _Editor_ is where we actually read, write, and edit code. It has a scrollbar on the right to help us navigate large files. It also has a _Gutter_ on the left, which displays line numbers for the file. The _Gutter_ also provides us with context-dependent actions like running code or temporarily hiding functions and classes:
![PyCharm's Editor window](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-editor-window.png) _PyCharm's Editor window_
At the top, the _Editor_ has a tabbed interface to display the open files and switch between them at any time. To switch to another open file, we can either click the relevant tab or press `CTRL + TAB` to scroll through all of them. If necessary, we can also open files from external folders that are outside the project's folder by _attaching_ that folder to the current project.
The _Editor_ can open any plaintext file format, such as `.py` and `.md`, for editing. It also supports viewing both raster and vector image formats, such as PNG and SVG. However, note that most binary files, such as video, audio, and executable files are not supported by the _Editor_ and will be opened outside of PyCharm.
### Sidebar and Tool Windows
The _Sidebar_ has buttons to open and close **tool windows** , which are displayed at the bottom or left side of PyCharm's _Project Window_ :
![PyCharm's sidebar and the Project tool window](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-sidebar-project-tool-window.png) _PyCharm's sidebar and the Project tool window_
The _Project_ tool window is normally open by default. It displays the folder structure of the current project and allows us to open, create, and delete files and folders. If you have any external folders attached to the current project, the Project tool window will also display the structure of those folders.
PyCharm also has tool windows for running code, installing packages from PyPI using a graphical interface, and using version control software. Throughout the rest of this article, we'll learn how to use these tool windows as we build our sample Python GUI app.
### Status Bar
The _Status Bar_ is the horizontal bar at the bottom of PyCharm's workspace. It indicates the status of both our project and the entire IDE:
![PyCharm's status bar](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-status-bar.png) _PyCharm's status bar_
It provides information about the file that's currently opened in the _Editor_ , such as its encoding, line separator, cursor position, and indentation type. It also gives quick access to the _Python Interpreter_ settings, which we'll cover in more detail later.
## Install Python Packages
One thing we need to do before starting our GUI app is to install the [PyQt](https://www.pythonguis.com/pyqt6/) library. We'll use this library to build the app's GUI. This library doesn't come with Python but can be installed from the [PyPI](https://pypi.org/) software repository using the `pip` command.
However, PyCharm simplifies the installation by providing a tool window for us to search, install, and manage Python packages. To open the _Python Packages_ tool window, go to the _Sidebar_ and look for the _Python Packages_ button, which is shown in blue in the following screenshot:
![PyCharm's Python Packages tool window](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-python-packages-tool-window.png) _PyCharm's Python Packages tool window_
Using the search field, look for the `PyQt6` package. We can have a look at the `README` file (on the right side) for each package by clicking on the package's name (on the left side). Once we've found the package, we can click _Install_ next to the package's name and choose the package version we want to install.
A `README` file typically provides information about what a package does, how to install and use the package, what license the package is distributed under, and so on.
When we clear the search field, `PyQt6` should now be listed as _Installed_ :
![PyCharm's Python Packages tool window with PyQt6 ready to be installed](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-python-packages-tool-windowpyqt6-ready.png) _PyCharm's Python Packages tool window with PyQt6 ready to be installed_
If a newer version of an installed package is available, then PyCharm will indicate it by displaying a link with the current and next version (next to the package name) that we can click to upgrade:
![PyCharm's Python Packages tool window with PyQt6 installed](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-python-packages-tool-windowpyqt6-installed.png) _PyCharm's Python Packages tool window with PyQt6 installed_
You can also uninstall a Python package. To do this, click the package's name and go to the _kebab menu_ on the top-right corner of the `README` preview section. Then, click _Delete Package_ to uninstall the package:
![PyCharm's Python Packages tool window showing how to uninstall a package](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-python-packages-tool-window-uninstall-package.png) _PyCharm's Python Packages tool window showing how to uninstall a package_
Uninstalling Python packages from a virtual environment isn't something that we do often but PyCharm has a nice interface to do it if we need to.
## Write the Code
In this section, we will focus on writing and editing code in PyCharm to build our sample GUI app. For its GUI, the app will have one window with a _Press Me_ button. To start coding though, we need a Python file.
**NOTE:** This guide will not cover PyQt extensively. To learn more about this library, check out the [Creating your first app with PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/) tutorial.
To create a file, go to the _Projects_ tool window and right-click the project's folder to open its context menu. Then, go to _New_ and select _Python File_ as the desired file type:
![PyCharm's context menu to create a new Python file](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-create-new-python-file.png) _PyCharm's context menu to create a new Python file_
This action will open a dialog where PyCharm will ask you to enter a filename. For this project, we will just name the file as `app` and press _ENTER_ :
![PyCharm's dialog to name a new Python file](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-dialog-name-new-python-file.png) _PyCharm's dialog to name a new Python file_
The _Project_ tool window will now lists a file named `app.py` under the project's folder. To open that file in the _Editor_ , double-click on the filename and you'll see a blank Python file:
![The app.py file opened in PyCharm's Editor](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/file-opened-pycharm-ditor.png) _The`app.py` file opened in PyCharm's Editor_
The _Editor_ works like any other standard text editor or code editor. We enter text using the keyboard and press `ENTER` to create a new line. We can use the _Gutter_ to track the line number we are currently on.
Now that we have a Python file in our project folder, we can start coding. First, we will import the required Python modules, packages, and classes:
python ```
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

```

As we type the `import` statements in the _Editor_ , PyCharm will offer suggestions for matching keywords and Python packages using a pop-up:
![PyCharm's code suggestions pop-up](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-code-suggestions-pop-up.png) _PyCharm's code suggestions pop-up_
You can use the Up and Down arrow keys to navigate the list of suggestions. Then, press `TAB` to select the highlighted suggestion.
Another useful feature of PyCharm is its ability to detect errors and provide fixes for problematic code. The following code block deliberately includes a few errors to demonstrate this feature:
python ```
QApplication
window = MainWindow()
window.show()
app.exec()

```

In this code, we haven't instantiated `QApplication` correctly. This error produces a cascade of errors that PyCharm nicely spots for us:
![PyCharm's error detection feature](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-error-detection-feature.png) _PyCharm's error detection feature_
PyCharm detects a few errors in the code we just typed. It indicates the error by highlighting the relevant piece of code with a squiggly line.
The color of the squiggly line indicates the severity of the problem PyCharm detected. Any problem highlighted in red is a critical error that prevents the program from running and everything else is marked in yellow.
To discover what an error is about, we can drag the mouse pointer to the highlighted section and hover over it to see a tooltip as shown below:
![PyCharm's error tips: statement with no effect](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-error-tips-statement-with-no-effect.png) _PyCharm's error tips: statement with no effect_
PyCharm's tooltip says that the statement `QApplication` has no effect. This is because we are just referencing a class without creating a concrete object. As a result, PyCharm flags a critical error in the last line because the `app` name hasn't been assigned yet.
We can fix both errors by instantiating `QApplication` to create an object named `app`:
python ```
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

We've taken care of two problems detected by PyCharm, but there is still one critical error remaining. If we hover the mouse's pointer over the highlighted object, we'll see that PyCharm is complaining about `window = MainWindow()` because we are using a class that we haven't defined yet:
![PyCharm's error tips: unresolved reference](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-error-tips-unresolved-reference.png) _PyCharm's error tips: unresolved reference_
To fix the issue, right-click the highlighted object to open the associated _Context Menu_. Once you see the menu, select _Show Context Actions_. This will open another pop-up where PyCharm offers smart suggestions to fix the problem.
For this particular problem, we'll choose the option _Create class 'MainWindow' in module app.py_ as shown below:
![PyCharm's Context Actions pop-up](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-context-actions-pop-up.png) _PyCharm's Context Actions pop-up_
PyCharm automatically generates an empty class named `MainWindow`. Update the class as follows in order to specify how the app's GUI will look:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    button = QPushButton("Press Me!")
    self.setFixedSize(QSize(400, 300))
    self.setCentralWidget(button)

```

With this update done, the code for `app.py` should look something like the following:
python ```
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    button = QPushButton("Press Me!")
    self.setFixedSize(QSize(400, 300))
    self.setCentralWidget(button)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

Now you have a working PyQt app. The next step is to run the app using PyCharm's features but before that, let's summarize what we've leaned so far.
We learned how to create a file using the _Project_ tool window and then edit it using the Editor. We also learned how to use some of the assistive coding features provided by PyCharm to get code suggestions, fix problems in our code, and generate boilerplate code for a faster coding experience.
## Run the Code
PyCharm provides a convenient way to run code through its interface. To run our PyQt app, right-click on the _Editor's_ work area to open the _Context Menu_. Then, select the _Run 'app'_ option:
![Running code with PyCharm's Run option from the Editor's context menu](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/running-code-pycharm-run-option-editor-context-menu.png) _Running code with PyCharm's Run option from the Editor's context menu_
The option to run code using the Run option in the context menu can be appropriate for short apps or scripts. However, when you have a much larger project with more than one file, it's often convenient to configure a default Python file for a project to run.
To do so, right-click on the `app.py` file in the _Editor_ to show the _Context Menu_. Then, select _Modify Run Configuration..._ as in the following screenshot:
![Modifying the Run Configuration in PyCharm](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/modifying-run-configuration-pycharm.png) _Modifying the Run Configuration in PyCharm_
Once you select the _Modify Run Configuration..._ , you get presented with the _Edit Run Configuration_ dialog:
![PyCharm's Edit Run Configuration dialog](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-edit-run-configuration-dialog.png) _PyCharm's Edit Run Configuration dialog_
In the _Edit Run Configuration_ dialog, we can modify the path to the Python script or set additional command-line arguments to pass when running the project. We can also set a name for this configuration at the top of the dialog and click the _OK_ button.
Now, we'll see the `app` configuration next to the green _Run_ button on the _Window Header_. This indicates which script PyCharm will run by default. If we have more than one _Run Configuration_ , then we can switch between them by clicking on the dropdown menu next to the _Run_ button.
Once we have set the project's default _Run Configuration_ , we can run the associated script regardless of which file we are currently working on the _Editor_ by clicking on the _Run_ button in the _Window Header_ :
![Running code with PyCharm's Run button from the Window Header](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/running-code-pycharm-run-button-window-header.png) _Running code with PyCharm's Run button from the Window Header_
To terminate the app's execution from the PyCharm interface, click the _Stop_ button in the _Window Header_.
## Configure the Python Environment
Python's best practices recommend avoiding the system interpreter in favor of using a virtual environment. A Python virtual environment is an isolated copy of the system interpreter that we create for development purposes.
For most large projects, you should create a dedicated virtual environment. As we noted earlier, PyCharm creates a virtual environment by default whenever we create a new project. This allows us to manage the project's dependencies separately because they are installed in the dedicated Python environments rather than globally in your system.
We can see the installed packages in our current Python environment by clicking on the Python interpreter selector (in the _Status Bar_) and clicking on the _Manage Packages..._ option. This action opens the _Python Packages_ tool window, which we previously used to install PyQt:
![Managing Python packages in PyCharm](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/managing-python-packages-pycharm.png) _Managing Python packages in PyCharm_
We can create a new Python virtual environment for our project by going to _Add New Interpreter > Add Local Interpreter_:
![Creating a new Python virtual environment in PyCharm - Step 1](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/creating-new-python-virtual-environment-pycharm-step1.png) _Creating a new Python virtual environment in PyCharm - Step 1_
After clicking on the _Add Local Interpreter_ option, you get presented with the _Add Python Interpreter_ dialog. There, you'll find several options to create working environments for Python coding. For the purposes of this guide, we'll only look at creating a standard _Virtualenv Environment_ :
![Creating a new Python virtual environment in PyCharm - Step 2](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/creating-new-python-virtual-environment-pycharm-step2.png) _Creating a new Python virtual environment in PyCharm - Step 2_
Specify where to create the Python Virtual Environment and select a base interpreter from the dropdown list if you have more than one version of Python. Then, click the _OK_ button to create the new Python environment for the active project. We can see the current Python environment by looking at the Python interpreter selector in the right bottom corner of the _Status Bar_.
Because this is a brand new virtual environment, trying to run the app now will fail because we haven't installed PyQt in this Python environment.
To switch back to the previous Python environment, click on the interpreter selector and select the relevant interpreter from the list:
![Changing the Python virtual environment in PyCharm](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/changing-python-virtual-environment-pycharm.png) _Changing the Python virtual environment in PyCharm_
To get back to the original Python environment, select the _Python 3.10 (PyQt6app)_ menu option in the dropdown list.
## Use Git for Version Control
Version control systems (VCS) allow us to track changes to a project's codebase. They are useful because they let us know what has changed in the app and who is responsible, which is particularly important when working with teams. VCSs also make it easy to revert any changes we make, giving us more freedom to test out new features.
PyCharm has built-in support for several VCSs. In this tutorial, we'll focus on Git, which is one of the most popular. In this section, we'll go over how to create and manage a Git repository for a project in PyCharm.
**WARNING** : To use Git-related features in PyCharm, Git needs to be installed. If you haven't done so already, please follow this guide to [install and set up Git](https://www.pythonguis.com/tutorials/git-github-python/) on your computer.
### Track Changes in a Project
You can use Git via its command-line interface. However, PyCharm allows us to perform common version control tasks through a graphical interface.
To enable version control for the current project, go to the _Version Control_ tool window at the bottom of the _Sidebar_ and click on _Create Git Repository_ link:
![PyCharm's Version Control tool window](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-version-control-tool-window.png) _PyCharm's Version Control tool window_
Once you click the _Create Git Repository_ link, you get the _Create Git Repository_ dialog:
![PyCharm's Create Git Repository dialog](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-create-git-repository-dialog.png) _PyCharm's Create Git Repository dialog_
Once you create the Git, the tool window will update its view to provide additional information. It should be mostly blank right now because we haven't started tracking any files.
To start tracking project files, we need to commit to the Git repository. To do that, a tool window named _Commit_ will appear in the _Sidebar_ (near the top).
A commit is a snapshot of the current state of all the files in a project. Each time we make a significant change to our codebase, we make a commit to mark what changed and by whom.
Open the tool window and look at the section named _Changes_ :
![PyCharm's Commit tool window](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-commit-tool-window.png) _PyCharm's Commit tool window_
The _Changes_ section under _Commit_ shows any project files that have changed or aren't being tracked. Because we aren't tracking any files for now, all of our project files appear under _Unversioned Files_.
We can select which files we would like to include in a commit by marking the _checkbox_ next to each filename. For this project, select all of the _Unversioned Files_ in the first commit.
There's a text box right below the _Changes_ section where you can type a commit message to describe what changed in these files. Because this will be our first commit for the current project, we can write a message like "Initial commit":
![Select the files to commit and add a commit message in PyCharm](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/select-files-commit-add-commit-message-pycharm.png) _Select the files to commit and add a commit message in PyCharm_
Once we've selected the files to include in the commit and typed the commit message, we can make the commit by pressing the _Commit_ button underneath. The commit we made should now appear in the _Version Control_ tool window:
![PyCharm's Version Control tool window showing a commit](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-version-control-tool-window-showing-commit.png) _PyCharm's Version Control tool window showing a commit_
We'll make one more commit to this project by changing the text of the button in `app.py` from `"Press Me!"` to `"Press This Button!"`:
python ```
class MainWindow(QMainWindow):
  def __init__(self):
    ...
    button = QPushButton("Press This Button!")
    ...

```

When a project is version-controlled, PyCharm will indicate when a line has been added, modified, or deleted from a file by showing a colored indicator next to the line number in the gutter. The indicator disappears once we commit the changed file to the repository again:
![PyCarm showing a colored indicator for modified lines](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-showing-colored-indicator-modified-lines.png) _PyCharm showing a colored indicator for modified lines_
Go to the _Commit_ tool window, select `app.py` under _Changes_ , type a commit message like "Changed button text," and then press the Commit button again. You'll see the new commit appear above the previous one in the _Version Control_ tool window:
![PyCharm's Version Control tool window showing the commit history](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-version-control-tool-window-showing-commit-history.png) _PyCharm's Version Control tool window showing the commit history_
This is called the **commit history** , where we can see all the changes or commits that we've made in a project.
### Share a Project on GitHub
We've created a local Git repository and want to publish the project to a remote repository on GitHub. Before doing that, we need to authenticate so that PyCharm can access, create, and delete remote repositories on our GitHub account.
We could authenticate manually using SSH. However, PyCharm simplifies the process by integrating GitHub and GitLab right into the IDE. To authenticate, go to _Settings_ and look for _GitHub_ under _Version Control_. Then, click on the plus (+) sign and select the _Log In via GitHub_ option:
![Log in to GitHub through PyCharm's UI](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/login-github-through-pycharm.png) _Log in to GitHub through PyCharm's UI_
A browser window should open and ask you to confirm whether you want to authorize PyCharm to access your GitHub account. Once you confirm by selecting _Authorize in GitHub_ , you will be redirected to GitHub:
![Authorize PyCharm in GitHub](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/authorize-pycharm-github.png) _Authorize PyCharm in GitHub_
If you aren't already signed in, you will be shown the login page where you can sign up too if you don't already have a GitHub account:
![GitHub's log in page for authorizing PyCharm](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/github-login-page-authorizing-pycharm.png) _GitHub's log in page for authorizing PyCharm_
Once you provide your GitHub credentials and click the _Sign in_ button, you'll get your GitHub account listed in the _Version Control_ screen:
![GitHub account authorized in PyCharm](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/github-account-authorized-pycharm.png) _GitHub account authorized in PyCharm_
PyCharm only needs to be authorized once for each user on a computer.
Once PyCharm is authorized, we also need to create a new, empty remote repository. Go back to the GitHub website and click on the plus sign (+) at the top of your _Dashboard_ to create a new repository:
![Creating a new GitHub repository from the Dashboard](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/creating-new-github-repository-from-dashboard.png) _Creating a new GitHub repository from the Dashboard_
Let's give this repository a unique name related to the project we are working on:
![Create a new repository page on GitHub](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/create-new-repository-page-github.png) _Create a new repository page on GitHub_
Depending on who you plan to share this project with, you can also set the repository's visibility to be _public_ or _private_. Then, click the _Create Repository_ button and copy the remote repository URL:
![New repository on GitHub](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/new-repository-github.png) _New repository on GitHub_
Finally, click on the _VCS widget_ in PyCharm's _Window Header_ to _Push_ all the commits we've made in the local repository to the remote repository we just created on GitHub:
![Pushing to GitHub through PyCharm's UI](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pushing-github-through-pycharm.png) _Pushing to GitHub through PyCharm's UI_
Then, we need to specify where the remote repository is located. So, click on _Define Remote_ and paste the repository's URL into the corresponding input box:
![Setting the GitHub repository's URL through PyCharm's UI](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/setting-github-repository-url-through-pycharm.png) _Setting the GitHub repository's URL through PyCharm's UI_
Click _OK_ and then select the _Push_ button:
![Pushing commits to GitHub through PyCharm's UI](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pushing-commits-github-through-pycharm.png) _Pushing commits to GitHub through PyCharm's UI_
Now, any commits we made to our project will be visible in the remote repository on GitHub. If we go back to GitHub, we can see that it's no longer an empty repository:
![Populated repository on GitHub](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/populated-repository-github.png) _Populated repository on GitHub_
The _Version Control_ tool window should also display the name we set for the remote next to the latest commit:
![PyCharm's Version Control tool window showing the remote repository](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-version-control-tool-window-showing-remote-repository.png) _PyCharm's Version Control tool window showing the remote repository_
To make the next commit, make your changes and go to the _Commit_ tool window, where you can click the _Commit and Push..._ button to do both actions in on go:
![Committing new changes through PyCharm's UI](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/committing-new-changes-through-pycharm.png) _Committing new changes through PyCharm's UI_
We can also go to the _VCS widget_ and select _Push_ to do this at any time.
## Explore Other Useful Features in PyCharm
PyCharm has several features that help us write code more efficiently and make development smoother. In this section, we'll explore some of these features and learn how to use them.
### Search Everywhere
Projects can become quite large spanning multiple files and folders. By using the _Search Everywhere_ feature, we can look through the whole project for files, classes, lines of code and even specific actions like _Commit_ or _Push_. This feature also allows us to quickly find PyCharm's _Settings_ and tool windows without using our mouse.
To use _Search Everywhere_ , double-tap the _SHIFT_ key. You'll get presented with the _search window_ :
![PyCharm's Search Everywhere window](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-search-everywhere-window.png) _PyCharm's Search Everywhere window_
To specify what you are looking for, press _TAB_ to switch between _Classes_ , _Files_ , _Symbols_ , _Actions_ , and so on. It also supports evaluating mathematical expressions and filtering out certain file types via the _Filter_ button at the top-right corner.
### Code With Me
There are times when we need to give temporary access to other developers so that they can review our code and provide assistance. In these cases, we can use PyCharm's _Code With Me_ feature to create a shared session between a host and one or more guests.
The guests can see what the host is doing in PyCharm and can be allowed to edit files in the project in real time. We can also share the camera and microphone so we can discuss with others who joined that session.
To start a session, click on the _Code With Me_ icon at the top-right of the _window header_ next to the _Run_ button:
![PyCharm's Code With Me feature](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-code-with-me-feature.png) _PyCharm's Code With Me feature_
After selecting the _Start Session..._ option from the menu, PyCharm will allow you to configure what guests can and can't do in this session:
![PyCharm's Code With Me: Start Session dialog](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-code-with-me-start-session-dialog.png) _PyCharm's Code With Me: Start Session dialog_
**NOTE** : You can use _Code With Me_ for free in PyCharm Community edition but there are limits on the number of guests allowed and the session time. You can [learn more about the specific limits for the Community plan of _Code With Me_](https://www.jetbrains.com/code-with-me/buy/?section=personal&billing=yearly) on their website.
Once we set _permissions_ for our guests, PyCharm will create a link we need to send to the guests we are inviting. To copy the link, click on the _Code With Me_ icon again and select _Copy Session Link_ from the menu.
When a guest clicks the link, we will receive a _popup_ in PyCharm asking us to either _accept_ or _decline_ the guest. If we _accept_ , they will be able to use a lightweight installation of PyCharm just using their web browser through which we can collaborate.
It is always recommended to use Git for collaborating with others on a project. _Code With Me_ can't tell who made a change or why that change was made. More importantly, it requires an active connection to the host's computer to make changes to the project and guests have limited access to PyCharm's features.
### Sync Python Requirements
Earlier in this guide, we installed the `PyQt6` package to build the interface of our sample app. Most software we develop depends on third-party Python packages for essential features. In collaborative contexts, we often need to keep track of our project's dependencies so that everyone working with us knows what to install.
In Python, developers typically create a `requirements.txt` file that lists all the needed packages and their recommended versions. You can create this file manually. However, PyCharm provides tools to generate a `requirements.txt` file using its UI.
As a best practice, you should update a project's `requirements.txt` file whenever the dependencies change.
To generate the file, use _Search Everywhere_ to find the _Sync Python Requirements_ action:
![Searching for the Sync Python Requirements action in PyCharm's Search Everywhere](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/searching-sync-python-requirements-action-pycharm-search-everywhere.png) _Searching for the Sync Python Requirements action in PyCharm's Search Everywhere_
Selecting the _Sync Python Requirements_ action will open a dialog where we can specify how to handle package versions and manage the requirements file:
![PyCharm's Sync Python Requirements dialog](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-sync-python-requirements-dialog.png) _PyCharm's Sync Python Requirements dialog_
Once we click the _OK_ button, PyCharm will create the file and populate it with the names and versions of the required Python packages.
If we look at the _Project_ tool window, we'll see the new `requirements.txt` file in the project directory. If we open the file, we will see `PyQt6` listed with its package version:
![The requirements.txt file listed on PyCharm's Project tool window](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/requirements-file-pycharm-project-tool-window.png) _The`requirements.txt` file listed on PyCharm's Project tool window_
Remember to run the _Sync Python Requirements_ action again whenever you install or update Python packages in your project.
### Todos
Keeping track of changes already made in a project is important, but so is tracking what we still need to do. We can keep track of what needs to be done using **Todos**. A todo is a comment in our code that we start with `# TODO`:
![A TODO comment on PyCharm's editor and TODO tool window](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/todo-comment-pycharm-editor-todo-tool-window.png) _A TODO comment on PyCharm's editor and TODO tool window_
PyCharm will track these comments across the whole project, and we can view them all at any time in the _TODO_ tool window. This tool window has several options to filter the to-dos:
![PyCharm's TODO filtering options](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-todo-filtering-options.png) _PyCharm's TODO filtering options_
We can see every single todo across the project by selecting the _Project_ tab or just the ones in the current file with _Current File_. We can be even more specific by looking only at files that were recently viewed, changed, or are currently open by selecting the _Scope Based_ option.
When we use Git for version control, PyCharm will also show the number of remaining todos in each commit:
![PyCharm showing the number of remaining TODOs](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-showing-remaining-todos.png) _PyCharm showing the number of remaining TODOs_
### Scratches
Scratches are another interesting PyCharm feature that allows us to write temporary notes or draft code without touching any of the project files. To add a scratch, go to the _Project_ tool window and right-click on _Scratches and Consoles_ entry:
![Creating a Scratch file from PyCharm's Project tool window](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/creating-scratch-file-from-pycharm-project-tool-window.png) _Creating a Scratch file from PyCharm's Project tool window_
The _New - > Scratch File_ option will open a dialog where you can select the type of scratch file you want to create.
### Plugin Marketplace
While PyCharm is already packed with features to aid development, it is also highly extensible thanks to its _Plugin marketplace_. We can customize our PyCharm installation by getting themes and other plugins that provide additional functionality.
To use the _Plugin marketplace_ , click on the _Settings_ icon on the _Window Header_ and select _Plugins_ :
![PyCharm's Plugin marketplace](https://www.pythonguis.com/static/tutorials/developer/getting-started-pycharm/pycharm-plugin-marketplace.png) _PyCharm's Plugin marketplace_
In the _Plugin marketplace_ , we can see installed plugins as well as those that are available in the marketplace. To install a plugin, click the Install button and wait for PyCharm to download and install it.
## Summary
In this tutorial, you have learned how to install and set up the PyCharm IDE for Python development. You've also learned how to write and run Python code in PyCharm as well as how to install external Python packages using the IDE's interface You will now be able to create and set up a Python virtual environment and use Git for version control in your projects.
Finally, you went over a couple of additional useful features for working with GUI applications in PyCharm. With this knowledge, you are now able to confidently use PyCharm to develop your own Python apps and programs.
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Lalin Paranawithana](https://www.pythonguis.com/static/theme/images/authors/lalin-paranawithana.jpg)](https://www.pythonguis.com/authors/lalin-paranawithana/)
**Getting Started With PyCharm for Python GUI Development** was written by [Lalin Paranawithana](https://www.pythonguis.com/authors/lalin-paranawithana/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) and [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Lalin is a technology enthusiast with a focus on Linux and digital privacy. Lalin is currently trying to learn Python so he can build paid, open source applications and libraries with Linux as a first-class citizen. 
**Getting Started With PyCharm for Python GUI Development** was published in [tutorials](https://www.pythonguis.com/tutorials/) on January 04, 2025 (updated April 08, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[python](https://www.pythonguis.com/topics/python/) [pycharm](https://www.pythonguis.com/topics/pycharm/) [integrated development environment](https://www.pythonguis.com/topics/integrated-development-environment/)
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
