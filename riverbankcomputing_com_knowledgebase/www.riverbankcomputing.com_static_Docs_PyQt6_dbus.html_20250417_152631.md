# Content from: https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html

### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [DBus Support](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html)


# DBus Support[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html#dbus-support "Link to this heading")
PyQt6 provides two different modules that implement support for DBus. The [QtDBus](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtdbus/qtdbus-module.html) module provides wrappers for the standard Qt DBus classes. The dbus.mainloop.pyqt6 module adds support for the Qt event loop to the standard `dbus-python` Python module.
## [QtDBus](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtdbus/qtdbus-module.html)[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html#qtdbus "Link to this heading")
The [QtDBus](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtdbus/qtdbus-module.html) module is used in a similar way to the C++ library it wraps. The main difference is in the way it supports the demarshalling of DBus structures. C++ relies on the template-based registration of types using `qDBusRegisterMetaType()` which isn’t possible from Python. Instead a slot that accepts a DBus structure in an argument should specify a slot with a single [QDBusMessage](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtdbus/qdbusmessage.html) argument. The implementation of the slot should then extract the arguments from the message using its `arguments()` method.
For example, say we have a DBus method called `setColors()` that has a single argument that is an array of structures of three integers (red, green and blue). The DBus signature of the argument would then be `a(iii)`. In C++ you would typically define a class to hold the red, green and blue values and so your code would include the following (incomplete) fragments:
```
struct Color
{
  int red;
  int green;
  int blue;
};
Q_DECLARE_METATYPE(Color)
qDBusRegisterMetaType<Color>();
classServerAdaptor : public QDBusAbstractAdaptor
{
  Q_OBJECT
public slots:
  void setColors(QList<const Color &> colors);
};

```

The Python version is, of course, much simpler:
```
classServerAdaptor(QDBusAbstractAdaptor):
  @pyqtSlot(QDBusMessage)
  defsetColors(self, message):
    # Get the single argument.
    colors = message.arguments()[0]
    # The argument will be a list of 3-tuples of ints.
    for red, green, blue in colors:
      print("RGB:", red, green, blue)

```

Note that this technique can be used for arguments of any type, it is only require if DBus structures are involved.
## dbus.mainloop.pyqt6[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html#dbus-mainloop-pyqt6 "Link to this heading")
The dbus.mainloop.pyqt6 module provides support for the Qt event loop to `dbus-python`. The module’s API is almost identical to that of the dbus.mainloop.glib modules that provides support for the GLib event loop.
The dbus.mainloop.pyqt6 module contains the following function. 

DBusQtMainLoop(_set_as_default =False_)[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html#DBusQtMainLoop "Link to this definition")
    
Create a `dbus.mainloop.NativeMainLoop` object that uses the the Qt event loop. 

Parameters:
    
**set_as_default** – is optionally set to make the main loop instance the default for all new Connection and Bus instances. It may only be specified as a keyword argument, and not as a positional argument.
The following code fragment is all that is normally needed to set up the standard `dbus-python` language bindings package to be used with PyQt6:
```
fromdbus.mainloop.pyqt6import DBusQtMainLoop
DBusQtMainLoop(set_as_default=True)

```

### [Table of Contents](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html)
  * [DBus Support](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html)
    * [QtDBus](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html#qtdbus)
    * [dbus.mainloop.pyqt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html#dbus-mainloop-pyqt6)
      * [`DBusQtMainLoop()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html#DBusQtMainLoop)


#### Previous topic
[Internationalisation of PyQt6 Applications](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html "previous chapter")
#### Next topic
[The PyQt6 Extension API](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html "next chapter")
### Quick search
### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [DBus Support](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html)


© Copyright 2025, Riverbank Computing Limited, The Qt Company. Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3. 
