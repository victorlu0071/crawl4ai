# Content from: https://www.riverbankcomputing.com/static/Docs/PyQt6/metaobjects.html

### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Other Support for Dynamic Meta-objects](https://www.riverbankcomputing.com/static/Docs/PyQt6/metaobjects.html)


# Other Support for Dynamic Meta-objects[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/metaobjects.html#other-support-for-dynamic-meta-objects "Link to this heading")
PyQt6 creates a [QMetaObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qmetaobject.html) instance for any Python sub-class of [QObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html) without the need for the equivalent of Qt’s `Q_OBJECT` macro. Most of a [QMetaObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qmetaobject.html) is populated automatically by defining signals, slots and properties as described in previous sections. In this section we cover the ways in which the remaining parts of a [QMetaObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qmetaobject.html) are populated.
## [pyqtEnum()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qtcore-module.html#pyqtEnum)[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/metaobjects.html#pyqtenum "Link to this heading")
The [pyqtEnum()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qtcore-module.html#pyqtEnum) class decorator is used to decorate sub-classes of the Python [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "\(in Python v3.13\)") class so that they are published in the [QMetaObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qmetaobject.html). The typical use in PyQt6 is to declare symbolic constants that can be used by QML, and as the type of properties that can be set in Qt Designer. For example:
```
fromenumimport Enum, Flag
fromPyQt6.QtCoreimport pyqtEnum, QObject

classInstruction(QObject):
  @pyqtEnum
  classDirection(Enum):
    Up, Down, Left, Right = range(4)
  @pyqtEnum
  classStatus(Flag):
    Null = 0x00
    Urgent = 0x01
    Acknowledged = 0x02
    Completed = 0x04

```

## [pyqtClassInfo()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qtcore-module.html#pyqtClassInfo)[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/metaobjects.html#pyqtclassinfo "Link to this heading")
The [pyqtClassInfo()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qtcore-module.html#pyqtClassInfo) class decorator is used to specify a a name/value pair that is placed in the class’s [QMetaObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qmetaobject.html). It is the equivalent of Qt’s `Q_CLASSINFO` macro.
For example it is used by QML to define the default property of a class:
```
fromPyQt6.QtCoreimport pyqtClassInfo, QObject

@pyqtClassInfo('DefaultProperty', 'guests')
classBirthdayParty(QObject):
  pass

```

The decorator may be chained to define multiple name/value pairs.
### [Table of Contents](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html)
  * [Other Support for Dynamic Meta-objects](https://www.riverbankcomputing.com/static/Docs/PyQt6/metaobjects.html)
    * [pyqtEnum](https://www.riverbankcomputing.com/static/Docs/PyQt6/metaobjects.html#pyqtenum)
    * [pyqtClassInfo](https://www.riverbankcomputing.com/static/Docs/PyQt6/metaobjects.html#pyqtclassinfo)


#### Previous topic
[Support for Qt Properties](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_properties.html "previous chapter")
#### Next topic
[Support for Qt Interfaces](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_interfaces.html "next chapter")
### Quick search
### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Other Support for Dynamic Meta-objects](https://www.riverbankcomputing.com/static/Docs/PyQt6/metaobjects.html)


© Copyright 2025, Riverbank Computing Limited, The Qt Company. Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3. 
