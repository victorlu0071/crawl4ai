# Content from: https://www.riverbankcomputing.com/static/Docs/PyQt6/

### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/) »
  * [Reference Guide](https://www.riverbankcomputing.com/static/Docs/PyQt6/)


# Reference Guide[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/#reference-guide "Link to this heading")
  * [Introduction](https://www.riverbankcomputing.com/static/Docs/PyQt6/introduction.html)
    * [License](https://www.riverbankcomputing.com/static/Docs/PyQt6/introduction.html#license)
    * [PyQt6 Components](https://www.riverbankcomputing.com/static/Docs/PyQt6/introduction.html#pyqt6-components)
  * [Contributing to this Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/contributing.html)
    * [Repository Structure](https://www.riverbankcomputing.com/static/Docs/PyQt6/contributing.html#repository-structure)
    * [Description Files](https://www.riverbankcomputing.com/static/Docs/PyQt6/contributing.html#description-files)
    * [Contributing Patches](https://www.riverbankcomputing.com/static/Docs/PyQt6/contributing.html#contributing-patches)
  * [Support for Old Versions of Python](https://www.riverbankcomputing.com/static/Docs/PyQt6/eol_policy.html)
  * [Installing PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html)
    * [Understanding the Correct Version to Install](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#understanding-the-correct-version-to-install)
    * [Installing from Wheels](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#installing-from-wheels)
    * [Building and Installing from Source](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#building-and-installing-from-source)
  * [Differences Between PyQt6 and PyQt5](https://www.riverbankcomputing.com/static/Docs/PyQt6/pyqt5_differences.html)
  * [Support for Signals and Slots](https://www.riverbankcomputing.com/static/Docs/PyQt6/signals_slots.html)
    * [Unbound and Bound Signals](https://www.riverbankcomputing.com/static/Docs/PyQt6/signals_slots.html#unbound-and-bound-signals)
    * [Defining New Signals with pyqtSignal](https://www.riverbankcomputing.com/static/Docs/PyQt6/signals_slots.html#defining-new-signals-with-pyqtsignal)
    * [Connecting, Disconnecting and Emitting Signals](https://www.riverbankcomputing.com/static/Docs/PyQt6/signals_slots.html#connecting-disconnecting-and-emitting-signals)
    * [Connecting Signals Using Keyword Arguments](https://www.riverbankcomputing.com/static/Docs/PyQt6/signals_slots.html#connecting-signals-using-keyword-arguments)
    * [The pyqtSlot Decorator](https://www.riverbankcomputing.com/static/Docs/PyQt6/signals_slots.html#the-pyqtslot-decorator)
    * [The `PyQt_PyObject` Signal Argument Type](https://www.riverbankcomputing.com/static/Docs/PyQt6/signals_slots.html#the-pyqt-pyobject-signal-argument-type)
    * [Connecting Slots By Name](https://www.riverbankcomputing.com/static/Docs/PyQt6/signals_slots.html#connecting-slots-by-name)
  * [Support for Qt Properties](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_properties.html)
    * [Defining New Qt Properties](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_properties.html#defining-new-qt-properties)
  * [Other Support for Dynamic Meta-objects](https://www.riverbankcomputing.com/static/Docs/PyQt6/metaobjects.html)
    * [pyqtEnum](https://www.riverbankcomputing.com/static/Docs/PyQt6/metaobjects.html#pyqtenum)
    * [pyqtClassInfo](https://www.riverbankcomputing.com/static/Docs/PyQt6/metaobjects.html#pyqtclassinfo)
  * [Support for Qt Interfaces](https://www.riverbankcomputing.com/static/Docs/PyQt6/qt_interfaces.html)
  * [Support for QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/pyqt_qvariant.html)
  * [Support for QSettings](https://www.riverbankcomputing.com/static/Docs/PyQt6/pyqt_qsettings.html)
  * [Integrating Python and QML](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html)
    * [Registering Python Types](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#registering-python-types)
    * [A Simple Example](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#a-simple-example)
    * [Using QQmlListProperty](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#using-qqmllistproperty)
    * [Using Attached Properties](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#using-attached-properties)
    * [Using Property Value Sources](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#using-property-value-sources)
    * [Using QQmlParserStatus](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#using-qqmlparserstatus)
    * [Writing Python Plugins for **qmlscene**](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#writing-python-plugins-for-qmlscene)
  * [Support for Cooperative Multi-inheritance](https://www.riverbankcomputing.com/static/Docs/PyQt6/multiinheritance.html)
  * [Things to be Aware Of](https://www.riverbankcomputing.com/static/Docs/PyQt6/gotchas.html)
    * [TLS Support](https://www.riverbankcomputing.com/static/Docs/PyQt6/gotchas.html#tls-support)
    * [Crashes On Exit](https://www.riverbankcomputing.com/static/Docs/PyQt6/gotchas.html#crashes-on-exit)
    * [Keyword Arguments](https://www.riverbankcomputing.com/static/Docs/PyQt6/gotchas.html#keyword-arguments)
    * [Garbage Collection](https://www.riverbankcomputing.com/static/Docs/PyQt6/gotchas.html#garbage-collection)
    * [Multiple Inheritance](https://www.riverbankcomputing.com/static/Docs/PyQt6/gotchas.html#multiple-inheritance)
    * [Access to Protected Member Functions](https://www.riverbankcomputing.com/static/Docs/PyQt6/gotchas.html#access-to-protected-member-functions)
    * [`None` and `NULL`](https://www.riverbankcomputing.com/static/Docs/PyQt6/gotchas.html#none-and-null)
    * [Support for `void *`](https://www.riverbankcomputing.com/static/Docs/PyQt6/gotchas.html#support-for-void)
  * [Using Qt Designer](https://www.riverbankcomputing.com/static/Docs/PyQt6/designer.html)
    * [Using the Generated Code](https://www.riverbankcomputing.com/static/Docs/PyQt6/designer.html#using-the-generated-code)
    * [**pyuic6**](https://www.riverbankcomputing.com/static/Docs/PyQt6/designer.html#pyuic6)
    * [Writing Qt Designer Plugins](https://www.riverbankcomputing.com/static/Docs/PyQt6/designer.html#writing-qt-designer-plugins)
  * [Support for Pickling](https://www.riverbankcomputing.com/static/Docs/PyQt6/pickle.html)
  * [Using PyQt6 from the Python Shell](https://www.riverbankcomputing.com/static/Docs/PyQt6/python_shell.html)
  * [Internationalisation of PyQt6 Applications](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html)
    * [**pylupdate6**](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#pylupdate6)
    * [Differences Between PyQt6 and Qt](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#differences-between-pyqt6-and-qt)
    * [Support for Translator Comments](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#support-for-translator-comments)
  * [DBus Support](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html)
    * [QtDBus](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html#qtdbus)
    * [dbus.mainloop.pyqt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html#dbus-mainloop-pyqt6)
  * [The PyQt6 Extension API](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html)
    * [C++ API](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#c-api)


#### Next topic
[Introduction](https://www.riverbankcomputing.com/static/Docs/PyQt6/introduction.html "next chapter")
### Quick search
### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/) »
  * [Reference Guide](https://www.riverbankcomputing.com/static/Docs/PyQt6/)


© Copyright 2025, Riverbank Computing Limited, The Qt Company. Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3. 
