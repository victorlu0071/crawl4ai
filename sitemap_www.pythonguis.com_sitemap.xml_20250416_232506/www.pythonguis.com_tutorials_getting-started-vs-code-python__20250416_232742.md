# Content from: https://www.pythonguis.com/tutorials/getting-started-vs-code-python/

[](https://www.pythonguis.com/tutorials/getting-started-vs-code-python/#menu)
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
# Getting started with VS Code for Python
Setting up a Development Environment for Python programming
by [Lalin Paranawithana](https://www.pythonguis.com/authors/lalin-paranawithana/) Last updated Apr 08 [ Tutorials ](https://www.pythonguis.com/tutorials/)
Setting up a working development environment is the first step for any project. Your development environment setup will determine how easy it is to develop and maintain your projects over time. That makes it important to choose the _right tools for your project_. This article will guide you through how to set up Visual Studio Code, which is a popular free-to-use, cross-platform code editor developed by Microsoft, in order to develop Python applications.
_Visual Studio Code_ is not to be confused with _Visual Studio_ , which is a separate product also offered by Microsoft. Visual Studio is a fully-fledged IDE that is mainly geared towards Windows application development using C# and the .NET Framework.
Table of Contents
  * [Setup a Python environment](https://www.pythonguis.com/tutorials/getting-started-vs-code-python/#setup-a-python-environment)
  * [Setup Visual Studio Code](https://www.pythonguis.com/tutorials/getting-started-vs-code-python/#setup-visual-studio-code)
  * [Usage and Configuration](https://www.pythonguis.com/tutorials/getting-started-vs-code-python/#usage-and-configuration)
  * [Linting and Formatting Support (Optional)](https://www.pythonguis.com/tutorials/getting-started-vs-code-python/#linting-and-formatting-support-optional)
  * [Working With Virtual Environments](https://www.pythonguis.com/tutorials/getting-started-vs-code-python/#working-with-virtual-environments)
  * [Understanding Workspaces in VS Code](https://www.pythonguis.com/tutorials/getting-started-vs-code-python/#understanding-workspaces-in-vs-code)
  * [Working With Git in VS Code (Optional)](https://www.pythonguis.com/tutorials/getting-started-vs-code-python/#working-with-git-in-vs-code-optional)
  * [Community-driven & open source alternatives](https://www.pythonguis.com/tutorials/getting-started-vs-code-python/#community-driven-open-source-alternatives)
  * [Conclusion](https://www.pythonguis.com/tutorials/getting-started-vs-code-python/#conclusion)


## Setup a Python environment
In case you haven't already done this, Python needs to be installed on the development machine. You can do this by going to [python.org](https://www.python.org/downloads/) and grabbing the specific installer for either Windows or macOS. Python is also available for installation via Microsoft Store on Windows devices.
Make sure that you select the option to _Add Python to PATH_ during installation (via the installer).
If you are on Linux, you can check if Python is already installed on your machine by typing `python3 --version` in a terminal. If it returns an error, you need to install it from your distribution's repository. On Ubuntu/Debian, this can be done by typing `sudo apt install python3`. Both `pip` (or `pip3`) and `venv` are distributed as separate packages on Ubuntu/Debian and can also be installed by typing `sudo apt install python3-pip python3-venv`.
## Setup Visual Studio Code
First, head over to to [code.visualstudio.com](https://code.visualstudio.com/) and grab the installer for your specific platform.
If you are on a Raspberry Pi (with Raspberry Pi OS), you can also install VS Code by simply typing `sudo apt install code`. On [Linux distributions that support Snaps](https://snapcraft.io/docs/installing-snapd), you can do it by typing `sudo snap install code --classic`. 
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
Once VS Code is installed, head over to the _Extensions_ tab in the sidebar on the left by clicking on it or by pressing `CTRL+SHIFT+X`. Search for the 'Python' extension published by Microsoft and click on _Install_.
![The Extensions tab in the left-hand sidebar](https://www.pythonguis.com/static/tutorials/developer/vscode/extensions.png) _The Extensions tab in the left-hand sidebar._
## Usage and Configuration
Now that you have finished setting up VS Code, you can go ahead and create a new Python file. Remember that the Python extension only works if you open a `.py` file or have selected the language mode for the active file as Python.
To change the language mode for the active file, simply press `CTRL+K` once and then press `M` after releasing the previous keys. This kind of keyboard shortcut is called a _chord_ in VS Code. You can see more of them by pressing `CTRL+K CTRL+S` (another chord).
The Python extension in VS Code allows you to directly run a Python file by clicking on the 'Play' button on the top-right corner of the editor (without having to type `python file.py` in the terminal).
You can also do it by pressing `CTRL+SHIFT+P` to open the _Command Palette_ and running the `> Python: Run File in Terminal` command.
Finally, you can configure VS Code's settings by going to `File > Preferences > Settings` or by pressing `CTRL+COMMA`. In VS Code, each individual setting has an unique _identifier_ which you can see by clicking on the cog wheel that appears to the left of each setting and clicking on 'Copy Setting ID'. This ID is what will be referred to while talking about a specific setting. You can also search for this ID in the search bar under _Settings_.
## Linting and Formatting Support (Optional)
Linters make it easier to find errors and check the quality of your code. On the other hand, code formatters help keep the source code of your application compliant with PEP (Python Enhancement Proposal) standards, which make it easier for other developers to read your code and collaborate with you.
For VS Code to provide linting support for your projects, you must first install a preferred linter like `flake8` or `pylint`.
bash ```
pip install flake8

```

Then, go to _Settings_ in VS Code and toggle the relevant setting (e.g. `python.linting.flake8Enabled`) for the _Python_ extension depending on what you installed. You also need to make sure that `python.linting.enabled` is toggled on.
A similar process must be followed for code formatting. First, install something like `autopep8` or `black`.
bash ```
pip install autopep8

```

You then need to tell VS Code which formatter to use by modifying `python.formatting.provider` and toggle on `editor.formatOnSave` so that it works without manual intervention.
If `pip` warns that the installed modules aren't in your PATH, you may have to specify the path to their location in VS Code (under _Settings_). Follow the method described under _Working With Virtual Environments_ to do that.
Now, when you create a new Python file, VS Code automatically gives you a list of _Problems_ (`CTRL+SHIFT+M`) in your program and formats the code on saving the file.
![Identified problems in the source code.](https://www.pythonguis.com/static/tutorials/developer/vscode/problems.png) _Identified problems in the source code, along with a description and line/column numbers._
You can also find the location of identified problems from the source overview on the right hand, inside the scrollbar.
## Working With Virtual Environments
Virtual environments are a way of life for Python developers. Most Python projects require the installation of external packages and modules (via `pip`). Virtual environments allow you to separate one project's packages from your other projects, which may require a different version of those same packages. Hence, it allows all those projects to have the specific dependencies they require to work.
The Python extension makes it easier for you by automatically activating the desired virtual environment for the in-built terminal and _Run Python File_ command after you set the path to the Python interpreter. By default, the path is set to use the system's Python installation (without a virtual environment).
1:1 Coaching & Tutoring for your Python GUIs project
[![Martin Fitzpatrick Python GUIs Coaching & Training](https://www.pythonguis.com/static/theme/images/products/coaching.jpg)](https://calendly.com/martinfitzpatrick/60min-python-guis-coaching)
[60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/) [Book Now](https://www.pythonguis.com/live/)
1:1 Python GUIs Coaching & Training
**Comprehensive code review** • **Bugfixes** & improvements • **Maintainability** advice and **architecture** improvements • **Design and usability** assessment • Suggestions and tips to **expand your knowledge** • **Packaging and distribution** help for Windows, Mac & Linux • [Find out more.](https://www.pythonguis.com/live)
To use a virtual environment for your project/workspace, you need to first make a new one by opening a terminal (`View > Terminal`) and typing `python -m venv .venv`. Then, you can set the default interpreter for that project by opening the _Command Palette_ (`CTRL+SHIFT+P`) and selecting `> Python: Select Interpreter`.
You should now either close the terminal pane in VS Code and open a new one or type `source .venv/bin/activate` into the existing one to start using the virtual environment. Then, install the required packages for your project by typing `pip install <package_name>`.
VS Code, by default, looks for tools like linters and code formatters in the current Python environment. If you don't want to keep installing them over and over again for each new virtual environment you make (unless your project requires a specific version of that tool), you can specify the path to their location under _Settings_ in VS Code. - `flake8` - `python.linting.flake8Path` - `autopep8` - `python.formatting.autopep8Path`
To find the global location of these packages on macOS and Linux, type `which flake8` and `which autopep8` in a terminal. If you are on Windows, you can use `where <command_name>`. Both these commands assume that `flake8` and `autopep8` are in your PATH.
## Understanding Workspaces in VS Code
VS Code has a concept of _Workspaces_. Each 'project folder' (or the root/top folder) is treated as a separate workspace. This allows you to have project-specific settings and enable/disable certain extensions for that workspace. It is also what allows VS Code to quickly recover the UI state (e.g. files that were previously kept open) when you open that workspace again.
In VS Code, each workspace (or folder) has to be 'trusted' before certain features like linters, autocomplete suggestions and the in-built terminal are allowed to work.
In the context of Python projects, if you tend to keep your virtual environments outside the workspace (where VS Code is unable to detect it), you can use this feature to set the default path to the Python interpreter for that workspace. To do that, first _Open a Folder_ (`CTRL+K CTRL+O`) and then go to `File > Preferences > Settings > Workspace` to modify `python.defaultInterpreterPath`.
![Setting the default interpreter path for the workspace.](https://www.pythonguis.com/static/tutorials/developer/vscode/defaultinterpreterpath.png) _Setting the default interpreter path for the workspace._
In VS Code settings you can search for settings by name using the bar at the top.
You can also use this approach to do things like use a different linter for that workspace or disable the code formatter for it. The workspace-specific settings you change are saved in a `.vscode` folder inside that workspace, which you can share with others.
If your VS Code is not recognizing libraries you are using in your code, double check the correct interpreter is being used. You can find which Python version you're using on the command line by running `which python` or `which python3` on macOS/Linux, or `where python` or `where python3` on Windows.
## Working With Git in VS Code (Optional)
Using _Version Control_ is required for developing applications. VS Code does have in-built support for Git but it is pretty barebones, not allowing much more than tracking changes that you have currently made and committing/pushing those changes once you are done.
For the best experience, it is recommended to use the _GitLens_ extension. It lets you view your commit history, check who made the changes and much more. To set it up, you first need to have Git set up on your machine ([go here](https://git-scm.com/)) and then install _GitLens_ from the _Extensions_ tab in the sidebar on the left. You can now use those Git-related features by going to the _Git_ tab in the sidebar (`CTRL+SHIFT+G`).
There are more Git-related extensions you could try as well, like _Git History_ and _GitLab Workflow_. Give them a whirl too!
## Community-driven & open source alternatives
While VS Code is open source (MIT-licensed), the distributed versions include some Microsoft-specific proprietary modifications, such as telemetry (app tracking). If you would like to avoid this, there is also a community-driven distribution of Visual Studio Code called [VSCodium](https://vscodium.com/) that provides freely-licensed binaries without telemetry.
Due to legal restrictions, VSCodium is unable to use the official Visual Studio Marketplace for extensions. Instead, it uses a separate vendor neutral, open source marketplace called [Open VSX Registry](https://open-vsx.org/). It doesn't have every extension, especially proprietary ones, and some are not kept up-to-date but both the _Python_ and _GitLens_ extensions are available on it.
You can also use the open source _Jedi_ language server for the Python extension, rather than the bundled _Pylance_ language server/extension, by configuring the `python.languageServer` setting. You can then completely disable Pylance by going to the _Extensions_ tab. Note that, if you are on VSCodium, Jedi is used by default (as Pylance is not available on Open VSX Registry) when you install the Python extension.
## Conclusion
Having the right tools and making sure they're set up correctly will greatly simplify your development process. While Visual Studio starts as a simple tool, it is flexible and extendable with plugins to suit your own preferred workflow. In this tutorial we've covered the basics of setting up your environment, and you should now be ready to start [developing your own applications with Python](https://www.pythonguis.com/topics/pyqt6-foundation/)!
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Lalin Paranawithana](https://www.pythonguis.com/static/theme/images/authors/lalin-paranawithana.jpg)](https://www.pythonguis.com/authors/lalin-paranawithana/)
**Getting started with VS Code for Python** was written by [Lalin Paranawithana](https://www.pythonguis.com/authors/lalin-paranawithana/) . 
Lalin is a technology enthusiast with a focus on Linux and digital privacy. Lalin is currently trying to learn Python so he can build paid, open source applications and libraries with Linux as a first-class citizen. 
**Getting started with VS Code for Python** was published in [tutorials](https://www.pythonguis.com/tutorials/) on September 21, 2022 (updated April 08, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[vscode](https://www.pythonguis.com/topics/vscode/) [python](https://www.pythonguis.com/topics/python/) [developer](https://www.pythonguis.com/topics/developer/) [development-environment](https://www.pythonguis.com/topics/development-environment/) [ide](https://www.pythonguis.com/topics/ide/) [ getting-started](https://www.pythonguis.com/topics/getting-started/)
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
