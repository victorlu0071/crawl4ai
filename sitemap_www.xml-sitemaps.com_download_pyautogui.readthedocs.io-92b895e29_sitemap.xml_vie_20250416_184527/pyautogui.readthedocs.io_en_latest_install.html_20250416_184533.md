# Content from: https://pyautogui.readthedocs.io/en/latest/install.html

[ PyAutoGUI ](https://pyautogui.readthedocs.io/en/latest/index.html)
latest 
  * [Installation](https://pyautogui.readthedocs.io/en/latest/install.html)
    * [Windows](https://pyautogui.readthedocs.io/en/latest/install.html#windows)
    * [macOS](https://pyautogui.readthedocs.io/en/latest/install.html#macos)
    * [Linux](https://pyautogui.readthedocs.io/en/latest/install.html#linux)
  * [Cheat Sheet](https://pyautogui.readthedocs.io/en/latest/quickstart.html)
  * [Mouse Control Functions](https://pyautogui.readthedocs.io/en/latest/mouse.html)
  * [Keyboard Control Functions](https://pyautogui.readthedocs.io/en/latest/keyboard.html)
  * [Message Box Functions](https://pyautogui.readthedocs.io/en/latest/msgbox.html)
  * [Screenshot Functions](https://pyautogui.readthedocs.io/en/latest/screenshot.html)
  * [Testing](https://pyautogui.readthedocs.io/en/latest/tests.html)
  * [Roadmap](https://pyautogui.readthedocs.io/en/latest/roadmap.html)
  * [pyautogui](https://pyautogui.readthedocs.io/en/latest/source/modules.html)


[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/index.html)
  * [Docs](https://pyautogui.readthedocs.io/en/latest/index.html) »
  * Installation
  * [ Edit on GitHub](https://github.com/asweigart/pyautogui/blob/master/docs/install.rst)


# Installation[¶](https://pyautogui.readthedocs.io/en/latest/install.html#installation "Permalink to this headline")
To install PyAutoGUI, install the `pyautogui` package from PyPI by running `pip install pyautogui` (on Windows) or `pip3 install pyautogui` (on macOS and Linux). (On macOS and Linux, `pip` refers to Python 2’s pip tool.)
OS-specific instructions are below.
## Windows[¶](https://pyautogui.readthedocs.io/en/latest/install.html#windows "Permalink to this headline")
On Windows, you can use the `py.exe` program to run the latest version of Python:
> `py -m pip install pyautogui`
If you have multiple versions of Python installed, you can select which one with a command line argument to `py`. For example, for Python 3.8, run:
> `py -3.8 -m pip install pyautogui`
(This is the same as running `pip install pyautogui`.)
## macOS[¶](https://pyautogui.readthedocs.io/en/latest/install.html#macos "Permalink to this headline")
On macOS and Linux, you need to run `python3`:
> `python3 -m pip install pyautogui`
If you are running El Capitan and have problems installing pyobjc try:
> `MACOSX_DEPLOYMENT_TARGET=10.11 pip install pyobjc`
## Linux[¶](https://pyautogui.readthedocs.io/en/latest/install.html#linux "Permalink to this headline")
On macOS and Linux, you need to run `python3`:
> `python3 -m pip install pyautogui`
On Linux, additionally you need to install the `scrot` application, as well as Tkinter:
> `sudo apt-get install scrot`
> `sudo apt-get install python3-tk`
> `sudo apt-get install python3-dev`
PyAutoGUI install the modules it depends on, including PyTweening, PyScreeze, PyGetWindow, PymsgBox, and MouseInfo.
[Next ](https://pyautogui.readthedocs.io/en/latest/quickstart.html "Cheat Sheet") [ Previous](https://pyautogui.readthedocs.io/en/latest/index.html "Welcome to PyAutoGUI’s documentation!")
© Copyright 2019, Al Sweigart  Revision `24d638dc`. 
Built with [Sphinx](http://sphinx-doc.org/) using a [theme](https://github.com/rtfd/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org). 
