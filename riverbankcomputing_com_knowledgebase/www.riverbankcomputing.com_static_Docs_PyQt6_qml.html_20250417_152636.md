# Content from: https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html

### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Integrating Python and QML](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html)


# Integrating Python and QML[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#integrating-python-and-qml "Link to this heading")
Qt includes QML as a means of declaratively describing a user interface and using JavaScript as a scripting language within it. It is possible to write complete standalone QML applications, or to combine them with C++. PyQt6 allows QML to be integrated with Python in exactly the same way. In particular:
  * Python types that are sub-classed from [QObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html) can be registered with QML.
  * Instances of registered Python types can be created and made available to QML scripts.
  * Instances of registered Python types can be created by QML scripts.
  * Singleton instances of registered Python types can be created automatically by a QML engine and made available to QML scripts.
  * QML scripts interact with Python objects through their properties, signals and slots.
  * Python properties, signals and slots can be given revision numbers that only those implemented by a specific version are made available to QML.


Note
The PyQt support for QML requires knowledge of the internals of the C++ code that implements QML. This can (and does) change between Qt versions and may mean that some features only work with specific Qt versions and may not work at all with some future version of Qt.
It is recommended that, in an MVC architecture, QML should only be used to implement the view. The model and controller should be implemented in Python.
## Registering Python Types[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#registering-python-types "Link to this heading")
Registering Python types with QML is done in the same way is it is done with C++ classes, i.e. using the [qmlRegisterType()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qtqml-module.html#qmlRegisterType), [qmlRegisterSingletonType()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qtqml-module.html#qmlRegisterSingletonType), [qmlRegisterUncreatableType()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qtqml-module.html#qmlRegisterUncreatableType) and [qmlRegisterRevision()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qtqml-module.html#qmlRegisterRevision) functions.
In C++ these are template based functions that take the C++ class, and sometimes a revision, as template arguments. In the Python implementation these are simply passed as the first arguments to the respective functions.
## A Simple Example[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#a-simple-example "Link to this heading")
The following simple example demonstates the implementation of a Python class that is registered with QML. The class defines two properties. A QML script is executed which creates an instance of the class and sets the values of the properties. That instance is then returned to Python which then prints the values of those properties.
Hopefully the comments are self explanatory:
```
importsys
fromPyQt6.QtCoreimport pyqtProperty, QCoreApplication, QObject, QUrl
fromPyQt6.QtQmlimport qmlRegisterType, QQmlComponent, QQmlEngine

# This is the type that will be registered with QML. It must be a
# sub-class of QObject.
classPerson(QObject):
  def__init__(self, parent=None):
    super().__init__(parent)
    # Initialise the value of the properties.
    self._name = ''
    self._shoeSize = 0
  # Define the getter of the 'name' property. The C++ type of the
  # property is QString which Python will convert to and from a string.
  @pyqtProperty('QString')
  defname(self):
    return self._name
  # Define the setter of the 'name' property.
  @name.setter
  defname(self, name):
    self._name = name
  # Define the getter of the 'shoeSize' property. The C++ type and
  # Python type of the property is int.
  @pyqtProperty(int)
  defshoeSize(self):
    return self._shoeSize
  # Define the setter of the 'shoeSize' property.
  @shoeSize.setter
  defshoeSize(self, shoeSize):
    self._shoeSize = shoeSize

# Create the application instance.
app = QCoreApplication(sys.argv)
# Register the Python type. Its URI is 'People', it's v1.0 and the type
# will be called 'Person' in QML.
qmlRegisterType(Person, 'People', 1, 0, 'Person')
# Create a QML engine.
engine = QQmlEngine()
# Create a component factory and load the QML script.
component = QQmlComponent(engine)
component.loadUrl(QUrl.fromLocalFile('example.qml'))
# Create an instance of the component.
person = component.create()
if person is not None:
  # Print the value of the properties.
  print("The person's name is %s." % person.name)
  print("They wear a size %d shoe." % person.shoeSize)
else:
  # Print all errors that occurred.
  for error in component.errors():
    print(error.toString())

```

The following is the `example.qml` QML script that is executed:
```
importPeople 1.0
Person {
  name: "Bob Jones"
  shoeSize: 12
}

```

## Using QQmlListProperty[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#using-qqmllistproperty "Link to this heading")
Defining list-based properties in Python that can be updated from QML is done using the QQmlListProperty class. However the way it is used in Python is slightly different to the way it is used in C++.
In the simple case QQmlListProperty wraps a Python list that is usually an instance sttribute, for example:
```
classBirthdayParty(QObject):
  def__init__(self, parent=None):
    super().__init__(parent)
    # The list which will be accessible from QML.
    self._guests = []
  @pyqtProperty(QQmlListProperty)
  defguests(self):
    return QQmlListProperty(Person, self, self._guests)

```

QML can now manipulate the Python list of `Person` instances. QQmlListProperty also acts as a proxy for the Python list so that the following can be written:
```
for guest in party.guests:
  print("Guest:", guest.name)

```

QQmlListProperty can also be used to wrap a _virtual_ list. The following code fragment is taken from the `chapter5-listproperties.py` example included with PyQt6:
```
classPieChart(QQuickItem):
  @pyqtProperty(QQmlListProperty)
  defslices(self):
    return QQmlListProperty(PieSlice, self,
        append=lambda pie_ch, pie_sl: pie_sl.setParentItem(pie_ch))

```

`PieChart` and `PieSlice` are Quick items that are registered using [qmlRegisterType()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qtqml-module.html#qmlRegisterType). Instances of both can be created from QML. `slices` is a property of `PieChart` that, as far as QML is concerned, is a list of `PieSlice` instances.
The pyqtProperty decorator specifies that the property is a QQmlListProperty, that its name is `slices` and that the `slices()` function is its getter.
The getter returns an instance of QQmlListProperty. This specifies that elements of the list should be of type `PieSlice`, that the `PieChart` instance (i.e. `self`) has the property, and defines the callable that will be invoked in order to append a new element to the list.
The `append` callable is passed two arguments: the object whose property is to be updated (i.e. the `PyChart` instance), and the element to be appended (i.e. a `PieSlice` instance). Here we simply set the chart as the slice’s parent item. Note that there isn’t actually a list anywhere - this is because, in this particular example, one isn’t needed.
The signature of the `append` callable is slightly different to that of the corresponding C++ function. In C++ the first argument is the QQmlListProperty instance rather than the `PyChart` instance. The signatures of the `at`, `clear` and `count` callables are different in the same way.
## Using Attached Properties[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#using-attached-properties "Link to this heading")
In order to use attached properties in C++, three steps need to be taken.
  * A type that has attached properties must implement a static function called `qmlAttachedProperties`. This is a factory that creates an instance of the properties object to attach.
  * A type that has attached properties needs to be defined as such using the `QML_ATTACHED` macro.
  * The instance of an attached properties object is retrieved using the `qmlAttachedPropertiesObject()` template function. The template type is the type that has the attached properties.


PyQt6 uses similar, but slightly simpler steps to achieve the same thing.
  * When calling [qmlRegisterType()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qtqml-module.html#qmlRegisterType) to register a type that has attached properties the type of the properties object is passed as the `attachedProperties` argument. This type will be used as the factory for creating an instance of the properties object.
  * The instance of an attached properties object is retrieved using the [qmlAttachedPropertiesObject()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qtqml-module.html#qmlAttachedPropertiesObject) function in the same way that you would from C++. Just like [qmlRegisterType()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qtqml-module.html#qmlRegisterType), [qmlAttachedPropertiesObject()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qtqml-module.html#qmlAttachedPropertiesObject) takes an additional first argument that is the type that, in C++, would be the template argument.


See the `attach.py` example included with PyQt6 for a complete example showing the use of attached properties.
## Using Property Value Sources[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#using-property-value-sources "Link to this heading")
Property values sources are implemented in PyQt6 in the same way as they are implemented in C++. Simply sub-class from both [QObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html) and [QQmlPropertyValueSource](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qqmlpropertyvaluesource.html) and provide an implementation of the [setTarget()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qqmlpropertyvaluesource.html#setTarget) method.
## Using [QQmlParserStatus](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qqmlparserstatus.html)[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#using-qqmlparserstatus "Link to this heading")
Monitoring the QML parser status is implemented in PyQt6 in the same way as it is implemented in C++. Simply sub-class from both [QObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html) and [QQmlParserStatus](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qqmlparserstatus.html) and provide implementations of the [classBegin()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qqmlparserstatus.html#classBegin) and [componentComplete()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qqmlparserstatus.html#componentComplete) methods.
## Writing Python Plugins for **qmlscene**[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#writing-python-plugins-for-qmlscene "Link to this heading")
Qt allows plugins that implement QML modules to be written that can be dynamically loaded by a C++ application (e.g. **qmlscene**). These plugins are sub-classes of [QQmlExtensionPlugin](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qqmlextensionplugin.html). PyQt6 supports exactly the same thing and allows those plugin to be written in Python. In other words it is possible to provide QML extensions written in Python to a C++ application, and to provide QML extensions written in C++ to a Python application.
PyQt6 provides a QML plugin called `pyqt6qmlplugin`. This acts as a wrapper around the Python code that implements the plugin. It handles the loading of the Python interpreter, locating and importing the Python module that contains the implementation of [QQmlExtensionPlugin](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qqmlextensionplugin.html), creating an instance of that class, and calling the instance’s [registerTypes()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtqml/qqmlextensionplugin.html#registerTypes) method. By default the `pyqt6qmlplugin` is installed in the `PyQt6` sub-directory of your Qt installation’s `plugin` directory.
Note
`pyqt6qmlplugin` is the name of the plugin as seen by QML. Its actual filename will be different and operating system dependent.
A QML extension module is a directory containing a file called `qmldir`. The file contains the name of the module and the name of the plugin that implements the module. It may also specify the directory containing the plugin. Usually this isn’t needed because the plugin is installed in the same directory.
Therefore, for a QML extension module called `Charts`, the contents of the `qmldir` file might be:
```
module Charts
plugin pyqt6qmlplugin /path/to/qt/plugins/PyQt6

```

The `pyqt6qmlplugin` expects to find a Python module in the same directory with a filename ending with `plugin.py` or `plugin.pyw`. In this case the name `chartsplugin.py` would be a sensible choice. Before importing this module `pyqt6qmlplugin` first places the name of the directory at the start of `sys.path`.
Note
`pyqt6qmlplugin` has to locate the directory containing the `qmldir` file itself. It does this using the same algorithm used by QML, i.e. it searches some standard locations and locations specified by the `QML2_IMPORT_PATH` environment variable. When using **qmlscene** , `pyqt6qmlplugin` will not know about any additional locations specified by its `-I` option. Therefore, `QML2_IMPORT_PATH` should always be used to specify additional locations to search.
Due to a limitation in QML it is not possible for multiple QML modules to use the same C++ plugin. In C++ this is not a problem as there is a one-to-one relationship between a module and the plugin. However, when using Python, `pyqt6qmlplugin` is used by every module. There are two solutions to this:
  * on operating systems that support it, place a symbolic link in the directory containing the `qmldir` file that points to the actual `pyqt6qmlplugin`
  * make a copy of `pyqt6qmlplugin` in the directory containing the `qmldir` file.


In both cases the contents of the `qmldir` file can be simplifed to:
```
module Charts
plugin pyqt6qmlplugin

```

PyQt6 provides an example that can be run as follows:
```
cd /path/to/examples/quick/tutorials/extending/chapter6-plugins
QML2_IMPORT_PATH=. /path/to/qmlscene app.qml

```

On Linux you may also need to set a value for the `LD_LIBRARY_PATH` environment variable.
### [Table of Contents](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html)
  * [Integrating Python and QML](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html)
    * [Registering Python Types](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#registering-python-types)
    * [A Simple Example](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#a-simple-example)
    * [Using QQmlListProperty](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#using-qqmllistproperty)
    * [Using Attached Properties](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#using-attached-properties)
    * [Using Property Value Sources](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#using-property-value-sources)
    * [Using QQmlParserStatus](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#using-qqmlparserstatus)
    * [Writing Python Plugins for **qmlscene**](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html#writing-python-plugins-for-qmlscene)


#### Previous topic
[Support for QSettings](https://www.riverbankcomputing.com/static/Docs/PyQt6/pyqt_qsettings.html "previous chapter")
#### Next topic
[Support for Cooperative Multi-inheritance](https://www.riverbankcomputing.com/static/Docs/PyQt6/multiinheritance.html "next chapter")
### Quick search
### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Integrating Python and QML](https://www.riverbankcomputing.com/static/Docs/PyQt6/qml.html)


© Copyright 2025, Riverbank Computing Limited, The Qt Company. Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3. 
