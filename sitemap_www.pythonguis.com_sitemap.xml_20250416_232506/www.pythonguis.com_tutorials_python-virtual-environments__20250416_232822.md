# Content from: https://www.pythonguis.com/tutorials/python-virtual-environments/

[](https://www.pythonguis.com/tutorials/python-virtual-environments/#menu)
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
# Working With Python Virtual Environments
Setting Your Python Working Environment, the Right Way
by [Lalin Paranawithana](https://www.pythonguis.com/authors/lalin-paranawithana/) Last updated Apr 08 [ Tutorials ](https://www.pythonguis.com/tutorials/)
As Python developers, we often need to add functionality to our applications which isn't provided by the standard library. Rather than implement everything ourselves, we can instead install 3rd party Python packages from the official Python package index at [PyPI](https://pypi.org/) using [`pip`](https://pip.pypa.io/en/stable/). The `pip` tool downloads and installs these 3rd party packages into our Python installation so we can immediately use them in our scripts and applications.
The [Python standard library](https://docs.python.org/3/library/index.html) is a set of Python packages that come bundled with Python installers. This library includes modules and packages like [`math`](https://docs.python.org/3/library/math.html#module-math) and usually [Tkinter](https://www.pythonguis.com/tkinter/).
There is a caveat here though: we can only install a single version of a package at any one time. While this isn't a problem when you create your first project, when you create the second any changes you make to the dependencies will also affect the first project. If any of your dependencies depend on other packages themselves (usually the case!) you may encounter conflicts where fixing the dependencies for one project breaks the dependencies for another.
This is known as _dependency hell_.
Thankfully, Python has a solution for this: **Python virtual environments**. Using virtual environments you can manage the packages for each project independently.
In this tutorial, we will learn how to create virtual environments and use them to manage our Python projects and their dependencies. We will also learn why virtual environments are an essential tool in any Python developer's arsenal.
Table of Contents
  * [Understand Why We Need Python Virtual Environments](https://www.pythonguis.com/tutorials/python-virtual-environments/#understand-why-we-need-python-virtual-environments)
  * [Explore How Python Virtual Environments Work](https://www.pythonguis.com/tutorials/python-virtual-environments/#explore-how-python-virtual-environments-work)
  * [Install Python On Your System](https://www.pythonguis.com/tutorials/python-virtual-environments/#install-python-on-your-system)
    * [Install Python on Windows or macOS](https://www.pythonguis.com/tutorials/python-virtual-environments/#install-python-on-windows-or-macos)
    * [Install Python on Linux](https://www.pythonguis.com/tutorials/python-virtual-environments/#install-python-on-linux)
  * [Create Python Virtual Environments](https://www.pythonguis.com/tutorials/python-virtual-environments/#create-python-virtual-environments)
  * [Use Python Virtual Environments](https://www.pythonguis.com/tutorials/python-virtual-environments/#use-python-virtual-environments)
    * [Activate the Virtual Environment](https://www.pythonguis.com/tutorials/python-virtual-environments/#activate-the-virtual-environment)
    * [Install Packages in the Virtual Environment](https://www.pythonguis.com/tutorials/python-virtual-environments/#install-packages-in-the-virtual-environment)
    * [Deactivate a Virtual Environment](https://www.pythonguis.com/tutorials/python-virtual-environments/#deactivate-a-virtual-environment)
    * [Manage the Location of Your Virtual Environments](https://www.pythonguis.com/tutorials/python-virtual-environments/#manage-the-location-of-your-virtual-environments)
    * [Delete a Python Virtual Environments](https://www.pythonguis.com/tutorials/python-virtual-environments/#delete-a-python-virtual-environments)
  * [Manage Your Project's Dependencies With pip](https://www.pythonguis.com/tutorials/python-virtual-environments/#manage-your-projects-dependencies-with-pip)
    * [Generate a Requirement File](https://www.pythonguis.com/tutorials/python-virtual-environments/#generate-a-requirement-file)
    * [Install Project Dependencies From a Requirement File](https://www.pythonguis.com/tutorials/python-virtual-environments/#install-project-dependencies-from-a-requirement-file)
    * [Tweak the Requirements File](https://www.pythonguis.com/tutorials/python-virtual-environments/#tweak-the-requirements-file)
    * [Create a Development Requirement File](https://www.pythonguis.com/tutorials/python-virtual-environments/#create-a-development-requirement-file)
  * [Conclusion](https://www.pythonguis.com/tutorials/python-virtual-environments/#conclusion)


## Understand Why We Need Python Virtual Environments
When working on a project, we often rely on specific external or third-party Python package versions. However, as packages get updated, their way of working may change.
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
If we update a package, the changes in that package may mean other projects stop functioning. To solve this issue, we have a few different options:
  * Continue using the **outdated version** of the package in all our projects.
  * Update _all_ our projects whenever a **new version** of the package comes out.
  * Use Python virtual environments to **isolate** the projects and their dependencies.


Not updating packages means that we won't be able to take advantage of new features or improvements. It can also affect the security of our project because we're not up-to-date with essential security updates and bug fixes for the Python packages our project relies on.
On the other hand, constantly updating our projects to keep them functional isn't much fun. While not always necessary, it quickly can become tedious and impractical, depending on the scale and the number of projects we have.
The last and best option is to use Python virtual environments. They allow us to manage the Python packages needed for each application separately. So we can choose when to update dependencies without affecting other projects that rely on those packages.
Using virtual environments gives us the benefit of being able to update packages without the risk of breaking all our projects at once. It gives us more time to make sure that each project works properly with the updated package version. It also avoids conflicts between package requirements and dependency requirements in our various projects.
Finally, using Python virtual environments is also recommended to avoid system conflicts because updating a package may break essential system tools or libraries that rely on a particular version of the package.
## Explore How Python Virtual Environments Work
A **virtual environment** is a folder containing a lightweight installation of Python. It creates a stripped-down and isolated copy of the base Python installation on our system without requiring us to install Python again.
Because a virtual environment is an isolated copy of our current system Python, we will find a copy of the `python` and `pip` executables inside each virtual environment folder. Once we activate a virtual environment, any `python` or `pip` commands will point to these executables instead of the ones in our system installation.
We can check where our system currently points Python commands to by running `python -c "import sys; print(sys.executable)"`. If we are not using a virtual environment, this command will show us where the system Python installation is located. Inside a virtual environment it will point to the environment's executable.
Using a virtual environment also means that `pip` will install external packages in the environment's `site` folder rather than in the system's. This way, we can keep different versions of a Python package installed in independent virtual environments. However, we still can only have one version of a given package per virtual environment.
## Install Python On Your System
In case you haven't done it yet, you need to install Python on your development machine before being able to use it.
### Install Python on Windows or macOS
You can install Python by going to its [download page](https://www.python.org/downloads/) and grabbing the specific installer for either Windows or macOS. Then, you have to run the installer and follow the on-screen instructions. Make sure you select the option to _Add Python to PATH_ during the installation process.
Python is also available for installation through [Microsoft Store](https://apps.microsoft.com/store/search/python) on Windows machines.
### Install Python on Linux
If you are on Linux, you can check if Python is installed on your machine by running the `python3 --version` command in a terminal. If this command issues an error, you can install Python from your Linux distribution repository.
You will find that the Python version available in most Linux repositories is relatively old. To work around this issue, you can use tools like [pyenv](https://github.com/pyenv/pyenv), which allows the installation of multiple Python versions.
For example, on Ubuntu and Debian, you can install Python by executing:
sh ```
$ sudo apt install python3

```

You may also need to install [`pip`](https://pip.pypa.io/en/stable/), the Python package installer, and [`venv`](https://docs.python.org/3/library/venv.html#module-venv), the module that allows you to create virtual environments. To do this, run the following command:
sh ```
$ sudo apt install python3-pip python3-venv

```

You only need to install `pip` and `venv` separately in some Linux distributions, including Ubuntu and Debian.
## Create Python Virtual Environments
The standard way to create virtual environments in Python is to use the `venv` module, which is a part of the standard library, so you shouldn't need to install anything additional on most systems.
A virtual environment is a stripped-down and isolated copy of an existing Python installation, so it doesn't require downloading anything.
You'll typically create a virtual environment per project. However, you can also have custom virtual environments with different purposes in your system.
To add a new virtual environment to a project, go to your project folder and run the following command in a terminal:
sh ```
$ python -m venv ./venv

```

If you check inside your project folder now, you'll see a new subfolder named `venv`. This folder contains the virtual environment you just made.
Using `venv`, `env`, or `.venv` as the virtual environment name is a common and accepted practice in the Python community.
## Use Python Virtual Environments
Now that you've successfully created your Python virtual environment, you can start using it to install whatever packages you need for your project. Note that every new virtual is like a fresh Python installation, with no third-party package available.
Unless you choose to pass the `--system-site-packages` switch to the `venv` command when you create the virtual environment, it will only contain the Python standard library and a couple of required packages. For any additional packages, we need to use `pip` to install them.
In the following sections, you'll learn how to activate your virtual environment for use, install packages, manage dependency, and more.
### Activate the Virtual Environment
To start using a virtual environment, you need to _activate_ it. The command to do this depends on your operating system and terminal shell.
On Unix systems, such as macOS and Linux, you can run the following command:
sh ```
$ source venv/bin/activate

```

This command activates your virtual environment, making it ready for use. You'll know that because your prompt will change from `$` to `(venv) $`. Go ahead and run the following command to check your current Python interpreter:
sh ```
(venv) $ python -c "import sys; print(sys.executable)"
/path/to/project/venv/bin/python

```

The output of this command will contain the path to the virtual environment interpreter. This interpreter is different from your system interpreter.
If you're on Windows and using PowerShell, then you can activate your virtual environment by running the following command:
sh ```
PS> venv\Scripts\activate

```

Again, you'll know the environment is active because your prompt will change from `PS>` to `(venv) PS>`.
Great! With these steps completed, we're now ready to start using our Python virtual environment.
### Install Packages in the Virtual Environment
Once the virtual environment is active, we can start using `pip` to install any packages our project requires. For example, say you want to install the [PyQt](https://www.pythonguis.com/pyqt6/) GUI framework to create desktop apps. In this case, you can run the following command:
sh ```
(venv) $ python -m pip install pyqt6

```

This command downloads and installs PyQt from the Python package index directly. Now you can start working on your GUI project.
Once you've activated a virtual environment, you can use `pip` directly without the `python -m` prefix. However, [best practices](https://snarky.ca/why-you-should-use-python-m-pip/) recommend using this command format.
You can also install multiple packages in one go:
sh ```
(venv) $ python -m pip install black flake8 mypy pytest

```

To install multiple packages with a single command, you only have to list the desired packages separated by spaces, as you did in the above command.
Finally, sometimes it's also useful to update a given package to its latest version:
sh ```
(venv) $ python -m pip install --upgrade pyqt6

```

The `--upgrade` flag tells `pip` to install the latest available version of an already installed package.
### Deactivate a Virtual Environment
Once you are done working on your GUI app, you need to _deactivate_ the virtual environment so you can switch back to your system shell or terminal. Remember that you'll have to reactivate this virtual environment next time you need to work on your project.
Here's how you can deactivate a Python virtual environment:
sh ```
(venv) $ deactivate

```

This command deactivates your virtual environment and gets you back into your system shell. You can run the `python -c "import sys; print(sys.executable)"` command to check that your current Python interpreter is your system Python.
### Manage the Location of Your Virtual Environments
Although you can place your virtual environments anywhere on your computer, there are a few standardized places for them to live. The most common one is inside the relevant project folder. As you already learned, the folder will usually be named `venv` or `.venv`.
If you use [Git for version control](https://www.pythonguis.com/tutorials/git-github-python/), make sure to ignore the virtual environment folder by adding it to `.gitignore`.
If you want to have all your virtual environments in a central location, then you can place them in your home folder. Directories like `~/.venvs` and `~/.virtualvenvs` are commonly used locations.
The Python extension for [Visual Studio Code](https://www.pythonguis.com/tutorials/getting-started-vs-code-python/) automatically [looks for any virtual environments](https://code.visualstudio.com/docs/python/environments#_where-the-extension-looks-for-environments) in a couple of places, including inside your current project folder and specific folders in your home folder (if they exist). If you want to specify additional external folders for it to look in, go to _Settings_ and configure `python.venvFolders` or `python.venvPath`. To avoid confusion, a good idea is to name each virtual environment in this folder after the relevant project name.
### Delete a Python Virtual Environments
If you are no longer working with a given virtual environment, you can get rid of it and all the related Python packages by simply deleting the virtual environment folder.
If you delete the virtual environment associated with a given project, to run the project again, you'll have to create a new virtual environment and install the required packages.
## Manage Your Project's Dependencies With `pip`
You've already learned how to create Python virtual environments to isolate the dependencies of your projects and avoid package versioning issues across different projects. You also learned how to install external dependencies with `pip`.
In the following sections, you'll learn how to efficiently manage a project's dependencies using `pip` and requirement files.
### Generate a Requirement File
An important advantage of using a dedicated virtual environment for each of our Python projects is that the environment will only contain the packages for that specific project. We can use the `pip freeze` command to get the list of currently installed packages in any active virtual environment:
sh ```
(venv) $ python -m pip freeze
PyQt6==6.5.0
PyQt6-Qt6==6.5.0
PyQt6-sip==13.5.1

```

This command allows us to create a text file containing the lists of the packages our project needs for running. To do this, go ahead and run the following command:
sh ```
(venv) $ python -m pip freeze > requirements.txt

```

After running the above command, you'll have a new file called `requirements.txt` in your project's directory.
By convention, the Python community uses the name `requirements.txt` for those files containing the list of dependencies of a given project. This file typically lives in the project's root directory.
Run the following command to check the content of this new file:
sh ```
$ cat requirements.txt
PyQt6==6.5.0
PyQt6-Qt6==6.5.0
PyQt6-sip==13.5.1

```

As you can see, your `requirements.txt` file lists those packages that you've installed in the active virtual environment. Once you have this file in place, anyone who needs to run your project from its source will know which packages they need to install. More importantly, they can use the file to install all the dependencies automatically, as you'll learn in the following section.
### Install Project Dependencies From a Requirement File
Besides of being able to see the list of Python packages our application needs, the requirements file also makes installing those packages in a new virtual environment just one command away:
sh ```
(new_venv) $ python -m pip install -r requirements.txt

```

The `-r` option of `pip install` allows you to provide a requirement file as an argument. Then, `pip` will read that file and install all the packages listed in it. If you run `pip freeze` again, you'll note that this new environment has the same packages installed.
### Tweak the Requirements File
Although using `pip freeze` is quite convenient, it often creates a lot of unnecessary clutter by populating the requirement file with Python packages that our application may not rely on directly. For example, packages that are dependencies of required packages and also packages that are only needed for development.
The generated file will also include the exact version of each package we have installed. While this may be useful, it is best to keep the requirement file clean. For example, dependencies of dependencies can often be ignored, since managing those is the responsibility of that package. That way, it'll be easy to know which packages are really required.
For example, in a GUI project, the `requirements.txt` file may only need to include PyQt6. In that case it would look like this:
sh ```
$ cat requirements.txt
PyQt6==6.5.0

```

Specifying the highest or lowest version of required packages may also be beneficial. To do this, we can replace the equality operator (`==`) with the less than (`<=`) or greater than (`>=`) operators, depending on your needs. If we completely omit the package version, `pip` will install the latest version available.
### Create a Development Requirement File
We should consider splitting our project requirement file into two separate files. For example, `requirements.txt` and `requirements_dev.txt`. This separation lets other developers know which packages are required for your project and which are solely relevant for development and testing purposes.
For example, you may use Black for formatting, `flake8` for linting, `mypy` for type checking, and `pytest` for testing your code. In this case, your `requirements_dev.txt` file should look something like this:
sh ```
$ cat requirements_dev.txt
black
flake8
mypy
pytest

```

With this file in place, developers who want to contribute to your project can install the required development dependencies easily.
## Conclusion
By now, you have a good understanding of how Python virtual environments work. They are straightforward to create and make it easy to manage the Python packages you need for developing your applications and projects.
Avoid installing Python packages outside of a virtual environment whenever possible. Creating a dedicated environment for a small Python script may not make sense. However, it's always a good idea to start any Python project that requires external packages by creating its own virtual environment.
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Lalin Paranawithana](https://www.pythonguis.com/static/theme/images/authors/lalin-paranawithana.jpg)](https://www.pythonguis.com/authors/lalin-paranawithana/)
**Working With Python Virtual Environments** was written by [Lalin Paranawithana](https://www.pythonguis.com/authors/lalin-paranawithana/) with contributions from [Leo Well](https://www.pythonguis.com/authors/leo-well/) and [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Lalin is a technology enthusiast with a focus on Linux and digital privacy. Lalin is currently trying to learn Python so he can build paid, open source applications and libraries with Linux as a first-class citizen. 
**Working With Python Virtual Environments** was published in [tutorials](https://www.pythonguis.com/tutorials/) on March 04, 2024 (updated April 08, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[python](https://www.pythonguis.com/topics/python/) [virtual environment](https://www.pythonguis.com/topics/virtual-environment/)
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
