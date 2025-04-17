# Content from: https://www.riverbankcomputing.com/static/Docs/PyQt6/introduction.html

### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Introduction](https://www.riverbankcomputing.com/static/Docs/PyQt6/introduction.html)


# Introduction[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/introduction.html#introduction "Link to this heading")
This is the reference guide for PyQt6 v6.9. PyQt6 is a set of [Python](https://www.python.org) bindings for v6 of the Qt application framework from [The Qt Company](https://www.qt.io).
Qt is a set of C++ libraries and development tools that includes platform independent abstractions for graphical user interfaces, networking, threads, regular expressions, SQL databases, SVG, OpenGL, XML, user and application settings, positioning and location services, short range communications (NFC and Bluetooth), web browsing, 3D animation, charts, 3D data visualisation and interfacing with app stores.
PyQt6 comprises PyQt6 itself and a number of add-ons that correspond to Qt’s additional libraries. At the moment these are PyQt6-3D and PyQt6-NetworkAuth. Each is provided as a source distribution (_sdist_) and binary wheels for Windows, Linux and macOS.
PyQt6 supports the Windows, Linux and macOS platforms and requires Python v3.8 or later.
The homepage for PyQt6 is <https://www.riverbankcomputing.com/software/pyqt/>. Here you will always find the latest stable version and current development snapshots.
## License[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/introduction.html#license "Link to this heading")
PyQt6 is dual licensed on all platforms under the Riverbank Commercial License and the GPL v3. Your PyQt6 license must be compatible with your Qt license. If you use the GPL version then your own code must also use a compatible license.
PyQt6, unlike most of Qt, is not available under the LGPL.
You can find the answers to questions about licensing [here](https://www.riverbankcomputing.com/commercial/license-faq).
You can purchase a commercial PyQt6 license [here](https://www.riverbankcomputing.com/commercial/buy).
## PyQt6 Components[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/introduction.html#pyqt6-components "Link to this heading")
PyQt6 comprises a number of different components. First of all there are a number of Python extension modules. These are all installed in the `PyQt6` Python package and are described in the [list of modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html#ref-module-index).
Each extension module has a corresponding [PEP 484](https://www.python.org/dev/peps/pep-0484) defined stub file containing type hints for the module’s API. This can be used by static type checkers such as [mypy](http://www.mypy-lang.org).
PyQt6 contains plugins that enable Qt Designer and **qmlscene** to be extended using Python code. See [Writing Qt Designer Plugins](https://www.riverbankcomputing.com/static/Docs/PyQt6/designer.html#ref-designer-plugins) and [Integrating Python and QML](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#ref-integrating-qml) respectively for the details.
PyQt6 also contains a couple of utility programs.
  * **pyuic6** corresponds to the Qt **uic** utility. It converts [QtWidgets](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtwidgets/qtwidgets-module.html) based GUIs created using Qt Designer to Python code.
  * **pylupdate6** corresponds to the Qt **lupdate** utility. It extracts all of the translatable strings from Python code and creates or updates `.ts` translation files. These are then used by Qt Linguist to manage the translation of those strings.


The [DBus](http://www.freedesktop.org/wiki/Software/DBusBindings) support module is installed as dbus.mainloop.pyqt6. This module provides support for the Qt event loop in the same way that the dbus.mainloop.glib included with the standard `dbus-python` bindings package provides support for the GLib event loop. The API is described in [DBus Support](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html#ref-dbus). It is only available if the `dbus-python` v0.80 (or later) bindings package is installed. The [QtDBus](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtdbus/qtdbus-module.html) module provides a more Qt-like interface to DBus.
PyQt6 includes a large number of examples. These are ports to Python of many of the C++ examples provided with Qt. They can be found in the `examples` directory of the sdist.
Finally, PyQt6 contains the specification files that allow bindings for other Qt based class libraries that further extend PyQt6 to be developed and installed.
### [Table of Contents](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html)
  * [Introduction](https://www.riverbankcomputing.com/static/Docs/PyQt6/introduction.html)
    * [License](https://www.riverbankcomputing.com/static/Docs/PyQt6/introduction.html#license)
    * [PyQt6 Components](https://www.riverbankcomputing.com/static/Docs/PyQt6/introduction.html#pyqt6-components)


#### Previous topic
[Reference Guide](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html "previous chapter")
#### Next topic
[Contributing to this Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/contributing.html "next chapter")
### Quick search
### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Introduction](https://www.riverbankcomputing.com/static/Docs/PyQt6/introduction.html)


© Copyright 2025, Riverbank Computing Limited, The Qt Company. Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3. 
