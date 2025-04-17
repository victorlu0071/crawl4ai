# Content from: https://pyautogui.readthedocs.io/en/latest/msgbox.html

[ PyAutoGUI ](https://pyautogui.readthedocs.io/en/latest/index.html)
latest 
  * [Installation](https://pyautogui.readthedocs.io/en/latest/install.html)
  * [Cheat Sheet](https://pyautogui.readthedocs.io/en/latest/quickstart.html)
  * [Mouse Control Functions](https://pyautogui.readthedocs.io/en/latest/mouse.html)
  * [Keyboard Control Functions](https://pyautogui.readthedocs.io/en/latest/keyboard.html)
  * [Message Box Functions](https://pyautogui.readthedocs.io/en/latest/msgbox.html)
    * [The alert() Function](https://pyautogui.readthedocs.io/en/latest/msgbox.html#the-alert-function)
    * [The confirm() Function](https://pyautogui.readthedocs.io/en/latest/msgbox.html#the-confirm-function)
    * [The prompt() Function](https://pyautogui.readthedocs.io/en/latest/msgbox.html#the-prompt-function)
    * [The password() Function](https://pyautogui.readthedocs.io/en/latest/msgbox.html#the-password-function)
  * [Screenshot Functions](https://pyautogui.readthedocs.io/en/latest/screenshot.html)
  * [Testing](https://pyautogui.readthedocs.io/en/latest/tests.html)
  * [Roadmap](https://pyautogui.readthedocs.io/en/latest/roadmap.html)
  * [pyautogui](https://pyautogui.readthedocs.io/en/latest/source/modules.html)


[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/index.html)
  * [Docs](https://pyautogui.readthedocs.io/en/latest/index.html) »
  * Message Box Functions
  * [ Edit on GitHub](https://github.com/asweigart/pyautogui/blob/master/docs/msgbox.rst)


# Message Box Functions[¶](https://pyautogui.readthedocs.io/en/latest/msgbox.html#message-box-functions "Permalink to this headline")
PyAutoGUI makes use of the message box functions in PyMsgBox to provide a cross-platform, pure Python way to display JavaScript-style message boxes. There are four message box functions provided:
## The alert() Function[¶](https://pyautogui.readthedocs.io/en/latest/msgbox.html#the-alert-function "Permalink to this headline")
```
>>> alert(text='', title='', button='OK')

```

Displays a simple message box with text and a single OK button. Returns the text of the button clicked on.
## The confirm() Function[¶](https://pyautogui.readthedocs.io/en/latest/msgbox.html#the-confirm-function "Permalink to this headline")
```
>>> confirm(text='', title='', buttons=['OK', 'Cancel'])

```

Displays a message box with OK and Cancel buttons. Number and text of buttons can be customized. Returns the text of the button clicked on.
## The prompt() Function[¶](https://pyautogui.readthedocs.io/en/latest/msgbox.html#the-prompt-function "Permalink to this headline")
```
>>> prompt(text='', title='' , default='')

```

Displays a message box with text input, and OK & Cancel buttons. Returns the text entered, or None if Cancel was clicked.
## The password() Function[¶](https://pyautogui.readthedocs.io/en/latest/msgbox.html#the-password-function "Permalink to this headline")
```
>>> password(text='', title='', default='', mask='*')

```

Displays a message box with text input, and OK & Cancel buttons. Typed characters appear as `*`. Returns the text entered, or None if Cancel was clicked.
[Next ](https://pyautogui.readthedocs.io/en/latest/screenshot.html "Screenshot Functions") [ Previous](https://pyautogui.readthedocs.io/en/latest/keyboard.html "Keyboard Control Functions")
© Copyright 2019, Al Sweigart  Revision `24d638dc`. 
Built with [Sphinx](http://sphinx-doc.org/) using a [theme](https://github.com/rtfd/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org). 
