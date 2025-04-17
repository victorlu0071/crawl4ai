# Content from: https://www.riverbankcomputing.com/static/Docs/PyQt6/python_shell.html

### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Using PyQt6 from the Python Shell](https://www.riverbankcomputing.com/static/Docs/PyQt6/python_shell.html)


# Using PyQt6 from the Python Shell[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/python_shell.html#using-pyqt6-from-the-python-shell "Link to this heading")
PyQt6 installs an input hook (using `PyOS_InputHook()`) that processes events when an interactive interpreter is waiting for user input. This means that you can, for example, create widgets from the Python shell prompt, interact with them, and still being able to enter other Python commands.
For example, if you enter the following in the Python shell:
```
>>> fromPyQt6.QtWidgetsimport QApplication, QWidget
>>> a = QApplication([])
>>> w = QWidget()
>>> w.show()
>>> w.hide()
>>>

```

The widget would be displayed when `w.show()` was entered and hidden as soon as `w.hide()` was entered.
The installation of an input hook can cause problems for certain applications (particularly those that implement a similar feature using different means). The [QtCore](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qtcore-module.html) module contains the [pyqtRemoveInputHook()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qtcore-module.html#pyqtRemoveInputHook) and [pyqtRestoreInputHook()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qtcore-module.html#pyqtRestoreInputHook) functions that remove and restore the input hook respectively.
#### Previous topic
[Support for Pickling](https://www.riverbankcomputing.com/static/Docs/PyQt6/pickle.html "previous chapter")
#### Next topic
[Internationalisation of PyQt6 Applications](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html "next chapter")
### Quick search
### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Using PyQt6 from the Python Shell](https://www.riverbankcomputing.com/static/Docs/PyQt6/python_shell.html)


© Copyright 2025, Riverbank Computing Limited, The Qt Company. Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3. 
