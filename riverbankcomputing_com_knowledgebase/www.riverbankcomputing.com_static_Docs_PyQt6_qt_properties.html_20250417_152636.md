# Content from: https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_properties.html

### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Support for Qt Properties](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_properties.html)


# Support for Qt Properties[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_properties.html#support-for-qt-properties "Link to this heading")
PyQt6 does not support the setting and getting of Qt properties as if they were normal instance attributes. This is because the name of a property often conflicts with the name of the property’s getter method.
However, PyQt6 does support the initial setting of properties using keyword arguments passed when an instance is created. For example:
```
act = QAction("&Save", self, shortcut=QKeySequence.StandardKey.Save,
    statusTip="Save the document to disk", triggered=self.save)

```

The example also demonstrates the use of a keyword argument to connect a signal to a slot.
PyQt6 also supports setting the values of properties (and connecting a signal to a slot) using the `pyqtConfigure()` method. For example, the following gives the same results as above:
```
act = QAction("&Save", self)
act.pyqtConfigure(shortcut=QKeySequence.StandardKey.Save,
    statusTip="Save the document to disk", triggered=self.save)

```

## Defining New Qt Properties[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_properties.html#defining-new-qt-properties "Link to this heading")
A new Qt property may be defined using the pyqtProperty function. It is used in the same way as the standard Python `property()` function. In fact, Qt properties defined in this way also behave as Python properties. 

PyQt6.QtCore.pyqtProperty(_type_[, _fget=None_[, _fset=None_[, _freset=None_[, _fdel=None_[, _doc=None_[, _designable=True_[, _scriptable=True_[, _stored=True_[, _user=False_[, _constant=False_[, _final=False_[, _notify=None_[, _revision=0_]]]]]]]]]]]]])[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_properties.html#PyQt6.QtCore.pyqtProperty "Link to this definition")
    
Create a property that behaves as both a Python property and a Qt property. 

Parameters:
    
  * **type** – the type of the property. It is either a Python type object or a string that is the name of a C++ type.
  * **fget** – the optional callable used to get the value of the property.
  * **fset** – the optional callable used to set the value of the property.
  * **freset** – the optional callable used to reset the value of the property to its default value.
  * **fdel** – the optional callable used to delete the property.
  * **doc** – the optional docstring of the property.
  * **designable** – optionally sets the Qt `DESIGNABLE` flag.
  * **scriptable** – optionally sets the Qt `SCRIPTABLE` flag.
  * **stored** – optionally sets the Qt `STORED` flag.
  * **user** – optionally sets the Qt `USER` flag.
  * **constant** – optionally sets the Qt `CONSTANT` flag.
  * **final** – optionally sets the Qt `FINAL` flag.
  * **notify** – the optional unbound notify signal.
  * **revision** – the revision exported to QML.



Return type:
    
the property object.
It is also possible to use pyqtProperty as a decorator in the same way as the standard Python `property()` function. The following example shows how to define an `int` property with a getter and setter:
```
fromPyQt6.QtCoreimport QObject, pyqtProperty
classFoo(QObject):
  def__init__(self):
    QObject.__init__(self)
    self._total = 0
  @pyqtProperty(int)
  deftotal(self):
    return self._total
  @total.setter
  deftotal(self, value):
    self._total = value

```

If you prefer the Qt terminology you may also use `write` instead of `setter` (and `read` instead of `getter`).
### [Table of Contents](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html)
  * [Support for Qt Properties](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_properties.html)
    * [Defining New Qt Properties](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_properties.html#defining-new-qt-properties)
      * [`PyQt6.QtCore.pyqtProperty()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_properties.html#PyQt6.QtCore.pyqtProperty)


#### Previous topic
[Support for Signals and Slots](https://www.riverbankcomputing.com/static/Docs/PyQt6/signals_slots.html "previous chapter")
#### Next topic
[Other Support for Dynamic Meta-objects](https://www.riverbankcomputing.com/static/Docs/PyQt6/metaobjects.html "next chapter")
### Quick search
### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Support for Qt Properties](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_properties.html)


© Copyright 2025, Riverbank Computing Limited, The Qt Company. Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3. 
