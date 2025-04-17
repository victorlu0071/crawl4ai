# Content from: https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_interfaces.html

### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Support for Qt Interfaces](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_interfaces.html)


# Support for Qt Interfaces[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_interfaces.html#support-for-qt-interfaces "Link to this heading")
PyQt6 does not, generally, support defining a class that inherits from more than one Qt class. The exception is when inheriting from classes that Qt defines as _interfaces_ , for example [QTextObjectInterface](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtgui/qtextobjectinterface.html).
A Qt interface is an abstract class contains only pure virtual methods and is used as a mixin with (normally) a [QObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html) sub-class. It is often used to define the interface that a plugin must implement.
Note that PyQt6 does not need an equivalent of Qt’s `Q_INTERFACES` macro in order to use an interface class.
The `textobject.py` example included with PyQt6 demonstrates the use of an interface.
#### Previous topic
[Other Support for Dynamic Meta-objects](https://www.riverbankcomputing.com/static/Docs/PyQt6/metaobjects.html "previous chapter")
#### Next topic
[Support for QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/pyqt_qvariant.html "next chapter")
### Quick search
### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Support for Qt Interfaces](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_interfaces.html)


© Copyright 2025, Riverbank Computing Limited, The Qt Company. Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3. 
