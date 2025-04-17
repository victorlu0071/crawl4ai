# Content from: https://www.riverbankcomputing.com/static/Docs/PyQt6/pyqt_qvariant.html

### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Support for QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/pyqt_qvariant.html)


# Support for [QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html)[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/pyqt_qvariant.html#support-for-qvariant "Link to this heading")
PyQt6 can convert any Python object to a [QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html) and back again. Normally this is done automatically and transparently so you don’t even need to know of the existence of [QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html).
An invalid [QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html) is automatically converted to `None` and vice versa.
However there are some situations where you might need to exert more control. For example you might want to distinguish between a [QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html) containing a C++ float value and one containing a C++ double value.
However it is possible to temporarily suppress the automatic conversion of a C++ [QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html) to a Python object and to return a wrapped Python [QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html) instead by calling the [`enableautoconversion()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/sip/sip-module.html#PyQt6.sip.enableautoconversion "PyQt6.sip.enableautoconversion") function.
The actual value of a wrapped Python [QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html) is obtained by calling its [value()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html#value) method.
#### Previous topic
[Support for Qt Interfaces](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_interfaces.html "previous chapter")
#### Next topic
[Support for QSettings](https://www.riverbankcomputing.com/static/Docs/PyQt6/pyqt_qsettings.html "next chapter")
### Quick search
### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Support for QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/pyqt_qvariant.html)


© Copyright 2025, Riverbank Computing Limited, The Qt Company. Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3. 
