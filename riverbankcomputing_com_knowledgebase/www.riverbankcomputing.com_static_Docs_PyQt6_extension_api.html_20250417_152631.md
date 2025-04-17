# Content from: https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html

### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [The PyQt6 Extension API](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html)


# The PyQt6 Extension API[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#the-pyqt6-extension-api "Link to this heading")
An important feature of PyQt6 (and SIP generated modules in general) is the ability for other extension modules to build on top of it. [QScintilla](https://www.riverbankcomputing.com/software/qscintilla/) is such an example.
PyQt6 provides a C++ extension API that can be used by other modules. This has the advantage of sharing code and also enforcing consistent behaviour.
## C++ API[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#c-api "Link to this heading")
The C++ API is a set of functions. The addresses of each function is obtained by calling SIP’s `sipImportSymbol()` function with the name of the function required.
The functions exported by PyQt6 are as follows: 

voidpyqt6_cleanup_qobjects()[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv422pyqt6_cleanup_qobjectsv "Link to this definition")
    
Call the C++ destructor of any [QObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html) instance that is owned by Python (with the exception of any [QCoreApplication](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qcoreapplication.html) instance). 

voidpyqt6_err_print()[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv415pyqt6_err_printv "Link to this definition")
    
A replacement for [`PyErr_Print()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Print "\(in Python v3.13\)") that passes the text of the exception and traceback to `qFatal()`. 

char**pyqt6_from_argv_list(PyObject*argv_list, int&argc)[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv420pyqt6_from_argv_listP8PyObjectRi "Link to this definition")
    
Convert a Python list to a standard C array of command line arguments and an argument count. 

Parameters:
    
  * **argv_list** – is the Python list of arguments.
  * **argc** – is updated with the number of arguments in the list.



Returns:
    
an array of pointers to the arguments on the heap. 

PyObject*pyqt6_from_qvariant_by_type(QVariant&value, PyObject*type)[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv427pyqt6_from_qvariant_by_typeR8QVariantP8PyObject "Link to this definition")
    
Convert a [QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html) to a Python object according to an optional Python type. 

Parameters:
    
  * **value** – is the value to convert.
  * **type** – is the Python type.



Returns:
    
the converted value. If it is `0` then a Python exception will have been raised. 

sipErrorStatepyqt6_get_connection_parts(PyObject*slot, QObject*transmitter, constchar*signal_signature, boolsingle_shot, QObject**receiver, QByteArray&slot_signature)[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv426pyqt6_get_connection_partsP8PyObjectP7QObjectPKcbPP7QObjectR10QByteArray "Link to this definition")
    
Get the receiver object and slot signature to allow a signal to be connected to an optional transmitter. 

Parameters:
    
  * **slot** – is the slot and should be a callable or a bound signal.
  * **transmitter** – is the optional [QObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html) transmitter.
  * **signal_signature** – is the signature of the signal to be connected.
  * **single_shot** – is `true` if the signal will only ever be emitted once.
  * **receiver** – is updated with the [QObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html) receiver. This may be a proxy if the slot requires it.
  * **slot_signature** – is updated with the signature of the slot.



Returns:
    
the error state. If this is `sipErrorFail` then a Python exception will have been raised. 

constQMetaObject*pyqt6_get_qmetaobject(PyTypeObject*type)[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv421pyqt6_get_qmetaobjectP12PyTypeObject "Link to this definition")
    
Get the QMetaObject instance for a Python type. The Python type must be a sub-type of [QObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html)’s Python type. 

Parameters:
    
**type** – is the Python type object. 

Returns:
    
the [QMetaObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qmetaobject.html). 

sipErrorStatepyqt6_get_pyqtsignal_parts(PyObject*signal, QObject**transmitter, QByteArray&signal_signature)[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv426pyqt6_get_pyqtsignal_partsP8PyObjectPP7QObjectR10QByteArray "Link to this definition")
    
Get the transmitter object and signal signature from a bound signal. 

Parameters:
    
  * **signal** – is the bound signal.
  * **transmitter** – is updated with the [QObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html) transmitter.
  * **signal_signature** – is updated with the signature of the signal.



Returns:
    
the error state. If this is `sipErrorFail` then a Python exception will have been raised. 

sipErrorStatepyqt6_get_pyqtslot_parts(PyObject*slot, QObject**receiver, QByteArray&slot_signature)[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv424pyqt6_get_pyqtslot_partsP8PyObjectPP7QObjectR10QByteArray "Link to this definition")
    
Get the receiver object and slot signature from a callable decorated with [pyqtSlot()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qtcore-module.html#pyqtSlot). 

Parameters:
    
  * **slot** – is the callable slot.
  * **receiver** – is updated with the [QObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html) receiver.
  * **slot_signature** – is updated with the signature of the slot.



Returns:
    
the error state. If this is `sipErrorFail` then a Python exception will have been raised. 

sipErrorStatepyqt6_get_signal_signature(PyObject*signal, constQObject*transmitter, QByteArray&signal_signature)[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv426pyqt6_get_signal_signatureP8PyObjectPK7QObjectR10QByteArray "Link to this definition")
    
Get the signature string for a bound or unbound signal. If the signal is bound, and the given transmitter is specified, then it must be bound to the transmitter. 

Parameters:
    
  * **signal** – is the signal.
  * **transmitter** – is the optional [QObject](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html) transmitter.
  * **signal_signature** – is updated with the signature of the signal.



Returns:
    
the error state. If this is `sipErrorFail` then a Python exception will have been raised. 

voidpyqt6_register_from_qvariant_convertor(bool(*convertor)(constQVariant&,PyObject**))[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv438pyqt6_register_from_qvariant_convertorPFbRK8QVariantPP8PyObjectE "Link to this definition")
    
Register a convertor function that converts a [QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html) value to a Python object. 

Parameters:
    
**convertor** – is the convertor function. This takes two arguments. The first argument is the [QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html) value to be converted. The second argument is updated with a reference to the result of the conversion and it will be `0`, and a Python exception raised, if there was an error. The convertor will return `true` if the value was handled so that no other convertor will be tried. 

voidpyqt6_register_to_qvariant_convertor(bool(*convertor)(PyObject*,QVariant&,bool*))[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv436pyqt6_register_to_qvariant_convertorPFbP8PyObjectR8QVariantPbE "Link to this definition")
    
Register a convertor function that converts a Python object to a [QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html) value. 

Parameters:
    
**convertor** – is the convertor function. This takes three arguments. The first argument is the Python object to be converted. The second argument is a pointer to [QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html) value that is updated with the result of the conversion. The third argument is updated with an error flag which will be `false`, and a Python exception raised, if there was an error. The convertor will return `true` if the value was handled so that no other convertor will be tried. 

voidpyqt6_register_to_qvariant_data_convertor(bool(*convertor)(PyObject*,void*,int,bool*))[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv441pyqt6_register_to_qvariant_data_convertorPFbP8PyObjectPviPbE "Link to this definition")
    
Register a convertor function that converts a Python object to the pre-allocated data of a [QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html) value. 

Parameters:
    
**convertor** – is the convertor function. This takes four arguments. The first argument is the Python object to be converted. The second argument is a pointer to the pre-allocated data of a [QVariant](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qvariant.html) value that is updated with the result of the conversion. The third argument is the meta-type of the value. The fourth argument is updated with an error flag which will be `false`, and a Python exception raised, if there was an error. The convertor will return `true` if the value was handled so that no other convertor will be tried. 

voidpyqt6_update_argv_list(PyObject*argv_list, intargc, char**argv)[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv422pyqt6_update_argv_listP8PyObjectiPPc "Link to this definition")
    
Update a Python list from a standard C array of command line arguments and an argument count. This is used in conjunction with [`pyqt6_from_argv_list()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv420pyqt6_from_argv_listP8PyObjectRi "pyqt6_from_argv_list") to handle the updating of argument lists after calling constructors of classes such as [QCoreApplication](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qcoreapplication.html). 

Parameters:
    
  * **argv_list** – is the Python list of arguments that will be updated.
  * **argc** – is the number of command line arguments.
  * **argv** – is the array of pointers to the arguments on the heap.


### [Table of Contents](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html)
  * [The PyQt6 Extension API](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html)
    * [C++ API](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#c-api)
      * [`pyqt6_cleanup_qobjects()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv422pyqt6_cleanup_qobjectsv)
      * [`pyqt6_err_print()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv415pyqt6_err_printv)
      * [`pyqt6_from_argv_list()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv420pyqt6_from_argv_listP8PyObjectRi)
      * [`pyqt6_from_qvariant_by_type()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv427pyqt6_from_qvariant_by_typeR8QVariantP8PyObject)
      * [`pyqt6_get_connection_parts()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv426pyqt6_get_connection_partsP8PyObjectP7QObjectPKcbPP7QObjectR10QByteArray)
      * [`pyqt6_get_qmetaobject()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv421pyqt6_get_qmetaobjectP12PyTypeObject)
      * [`pyqt6_get_pyqtsignal_parts()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv426pyqt6_get_pyqtsignal_partsP8PyObjectPP7QObjectR10QByteArray)
      * [`pyqt6_get_pyqtslot_parts()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv424pyqt6_get_pyqtslot_partsP8PyObjectPP7QObjectR10QByteArray)
      * [`pyqt6_get_signal_signature()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv426pyqt6_get_signal_signatureP8PyObjectPK7QObjectR10QByteArray)
      * [`pyqt6_register_from_qvariant_convertor()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv438pyqt6_register_from_qvariant_convertorPFbRK8QVariantPP8PyObjectE)
      * [`pyqt6_register_to_qvariant_convertor()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv436pyqt6_register_to_qvariant_convertorPFbP8PyObjectR8QVariantPbE)
      * [`pyqt6_register_to_qvariant_data_convertor()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv441pyqt6_register_to_qvariant_data_convertorPFbP8PyObjectPviPbE)
      * [`pyqt6_update_argv_list()`](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html#_CPPv422pyqt6_update_argv_listP8PyObjectiPPc)


#### Previous topic
[DBus Support](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html "previous chapter")
### Quick search
### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [The PyQt6 Extension API](https://www.riverbankcomputing.com/static/Docs/PyQt6/extension_api.html)


© Copyright 2025, Riverbank Computing Limited, The Qt Company. Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3. 
