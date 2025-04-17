# Content from: https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html

### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Internationalisation of PyQt6 Applications](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html)


# Internationalisation of PyQt6 Applications[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#internationalisation-of-pyqt6-applications "Link to this heading")
PyQt6 and Qt include a comprehensive set of tools for translating applications into local languages. For a full description, see the Qt Linguist Manual in the Qt documentation.
The process of internationalising an application comprises the following steps.
  * The programmer uses **pylupdate6** to create or update a `.ts` translation file for each human language that the application is to be translated into. A `.ts` file is an XML file that contains the messages to be translated and the corresponding translations that have already been made. **pylupdate6** can be run any number of times during development to update the `.ts` files with the latest messages for translation.
  * The translator uses Qt Linguist to update the `.ts` files with translations of the messages.
  * The release manager then uses Qt’s **lrelease** utility to convert the `.ts` files to `.qm` files which are compact binary equivalents used by the application. If an application cannot find an appropriate `.qm` file, or a particular message hasn’t been translated, then the messages used in the original source code are used instead.


## **pylupdate6**[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#pylupdate6 "Link to this heading")
The **pylupdate6** utility is a command line interface to the [lupdate](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/lupdate/lupdate-module.html) module. The command has the following syntax:
```
pylupdate6 [options] --ts .ts-file [--ts .ts-file ...] file [file ...]

```

The full set of command line options is: 

-h, --help[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#cmdoption-pylupdate6-h "Link to this definition")
    
A help message is written to `stdout`. 

-V, --version[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#cmdoption-pylupdate6-V "Link to this definition")
    
The version number is written to `stdout`. 

--exclude PATTERN[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#cmdoption-pylupdate6-exclude "Link to this definition")
    
a UNIX shell-style pattern that is matched against the source files found when recursively searching a directory. If a source file matches then it is excluded. This option may be specified any number of times. 

--no-obsolete[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#cmdoption-pylupdate6-no-obsolete "Link to this definition")
    
All obsolete messages from the translation files will be discarded. An obsolete message is one that was found by a previous invocation of **pylupdate6** but has not been found by this invocation. By default obsolete messages are retained and marked as such in the translation file. 

--no-summary[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#cmdoption-pylupdate6-no-summary "Link to this definition")
    
A summary of updates to the translation files will not be displayed on `stdout`. 

--ts FILE[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#cmdoption-pylupdate6-ts "Link to this definition")
    
The name of a translation file that is created or updated with the translatable messages extracted from the source files. This option may be specified any number of times. 

--verbose[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#cmdoption-pylupdate6-verbose "Link to this definition")
    
Progress messages will be displayed to `stdout`.
The rest of the command line are the names of the `.py` Python source files and `.ui` Designer files from which **pylupdate6** extracts messages from.
Note
Each time you invoke **pylupdate6** you should be careful to specify all the `.py` and `.ui` files that make up your application and not just the ones that have changed. Otherwise any messages that appear in files that you don’t specify will be marked as obsolete.
## Differences Between PyQt6 and Qt[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#differences-between-pyqt6-and-qt "Link to this heading")
Qt implements internationalisation support through the [QTranslator](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qtranslator.html) class, and the [QT_TRANSLATE_NOOP()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qtcore-module.html#QT_TRANSLATE_NOOP), [translate()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qcoreapplication.html#translate), [QT_TR_NOOP()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qtcore-module.html#QT_TR_NOOP) and [tr()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html#tr) methods. Usually [tr()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html#tr) is used to obtain the correct translation of a message. The translation process uses a message context to allow the same message to be translated differently. In Qt [tr()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html#tr) is actually generated by **moc** and uses the hardcoded class name as the context. On the other hand, translate allows the context to be specified explicitly.
Unfortunately, because of the way Qt implements [tr()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html#tr) it is not possible for PyQt6 to exactly reproduce its behaviour. The PyQt6 implementation of [tr()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html#tr) uses the class name of the instance as the context. The key difference, and the source of potential problems, is that the context is determined dynamically in PyQt6, but is hardcoded in Qt. In other words, the context of a translation may change depending on an instance’s class hierarchy. For example:
```
classA(QObject):
  defhello(self):
    return self.tr("Hello")
classB(A):
  pass
a = A()
a.hello()
b = B()
b.hello()

```

In the above the message is translated by `a.hello()` using a context of `A`, and by `b.hello()` using a context of `B`. In the equivalent C++ version the context would be `A` in both cases.
The PyQt6 behaviour is unsatisfactory and may be changed in the future. It is recommended that [translate()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qcoreapplication.html#translate) be used in preference to [tr()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qobject.html#tr). This is guaranteed to work with current and future versions of PyQt6 and makes it much easier to share message files between Python and C++ code. Below is the alternative implementation of `A` that uses [translate()](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/qtcore/qcoreapplication.html#translate):
```
classA(QObject):
  defhello(self):
    return QCoreApplication.translate('A', "Hello")

```

## Support for Translator Comments[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#support-for-translator-comments "Link to this heading")
In the same way that Qt’s **lupdate** can extract C++ comments aimed at the translator, **pylupdate6** can extract similarly formatted Python comments. Specifically:
> **#:** introduces a general comment for the translator
> **#=** introduces a unique identifier attached to the message
> **#~** introduces a field name and field contents attached to the message.
### [Table of Contents](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html)
  * [Internationalisation of PyQt6 Applications](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html)
    * [**pylupdate6**](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#pylupdate6)
    * [Differences Between PyQt6 and Qt](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#differences-between-pyqt6-and-qt)
    * [Support for Translator Comments](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html#support-for-translator-comments)


#### Previous topic
[Using PyQt6 from the Python Shell](https://www.riverbankcomputing.com/static/Docs/PyQt6/python_shell.html "previous chapter")
#### Next topic
[DBus Support](https://www.riverbankcomputing.com/static/Docs/PyQt6/dbus.html "next chapter")
### Quick search
### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Internationalisation of PyQt6 Applications](https://www.riverbankcomputing.com/static/Docs/PyQt6/i18n.html)


© Copyright 2025, Riverbank Computing Limited, The Qt Company. Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3. 
