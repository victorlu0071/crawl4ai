# Content from: https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html

### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Installing PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html)


# Installing PyQt6[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#installing-pyqt6 "Link to this heading")
Both the GPL and commercial versions of PyQt6 can be built from sdists or installed from binary wheels. Although this section concentrates on PyQt6 itself it applies equally to the add-on projects (e.g. PyQt6-3D, PyQt6-NetworkAuth etc.).
## Understanding the Correct Version to Install[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#understanding-the-correct-version-to-install "Link to this heading")
People sometimes mistakenly believe that support for a particular version of Qt requires a matching version of PyQt.
Qt uses [semantic versioning](https://semver.org/spec/v2.0.0.html) when deciding on the version number of a release. In summary the major version is increased when a release includes incompatible changes, the minor version is increased when a release includes compatible changes, and the patch version is increased when a release includes no user-visible changes.
With PyQt6 the version number of PyQt6 is tied, to a certain extent, to the version of Qt v6 so that:
  * The major version will always be **6**.
  * For a particular minor version _n_ it will build against any version of Qt v6, but will not support any new features introduced in Qt v6._n+1_ or later.
  * It will support all the features of supported modules of Qt v6._n_ or earlier.
  * Support for new modules may be added to PyQt6 at any time. This would result in a change of patch version only.
  * The major and minor versions of the latest release of PyQt6 will be the same as the latest release of Qt v6.
  * The patch versions of PyQt6 and Qt v6 are entirely unrelated to each other.


So, for example, PyQt6 v6.1 will build against Qt v6.2 but will not support any new features introduced in Qt v6.2. PyQt6 v6.1 will support all the features of supported modules of Qt v6.0 and those new features introduced in Qt v6.1.
In summary, you should always try and use the latest version of PyQt6 no matter what version of Qt v6 you are using.
## Installing from Wheels[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#installing-from-wheels "Link to this heading")
Wheels are the standard Python packaging format for pure Python or binary extension modules such as PyQt6. Wheels are provide for 64-bit Windows, 64-bit macOS (Intel and ARM) and 64-bit Linux. These correspond to the platforms for which The Qt Company provide binary installers.
Wheels are installed using Python’s **pip** program.
### Installing the GPL Version[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#installing-the-gpl-version "Link to this heading")
To install the wheel for the GPL version of PyQt6, run:
```
pip install PyQt6

```

This will attempt to install the wheel for your platform and your version of Python (assuming both are supported). The wheel will be automatically downloaded from [PyPI](https://pypi.org/project/PyQt6/).
You may find that **pip** doesn’t download a wheel but instead downloads the sdist and tries to build PyQt6 from source. If it does then the build will probably fail with a cryptic error message. There are a number of reasons for this:
  * there is no wheel available for your platform and version of Python
  * your version of Python is unsupported (e.g. v3.7)
  * your version of **pip** is too old and doesn’t support the current standards for naming wheels
  * in order for **pip** to build from source additional options must be specified.


When using **pip** to build from source then a command line similar to the following should be used:
```
pip -v install --config-settings --confirm-license= --config-settings --qmake=/path/to/qmake PyQt6

```

The `-v` option is not required but is recommended. The **qmake** location does not need to specified if it is on `PATH`.
**pip** will also automatically install any dependencies that are required. In the case of PyQt6 itself this will be the PyQt6-Qt6 and PyQt6-sip projects. The PyQt6-Qt6 project contains the parts of a standard LGPL Qt installation required by PyQt6. The PyQt6-sip project contains the [sip](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/sip/sip-module.html) module.
Note
If you want PyQt6 to use a copy of Qt that you already have installed then you need to build it from source.
To uninstall the GPL version, run:
```
pip uninstall PyQt6

```

Note
The Qt libraries in the Linux wheel of the PyQt6-Qt6 project require OpenSSL v1.1 however some Linux distributions (specifically Ubuntu 22.04 at the time of writing) include the incompatible OpenSSL v3.
The required version of OpenSSL can be downloaded from the Ubuntu 20.04 repository by clicking [here](http://security.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.16_amd64.deb).
The downloaded `.deb` file can then be installed by running:
```
sudo apt install /path/to/libssl1.1_1.1.1f-1ubuntu2.16_amd64.deb

```

### Installing the Commercial Version[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#installing-the-commercial-version "Link to this heading")
Wheels are also provided for the commercial version of PyQt6 but they must be downloaded from your account on the Riverbank Computing website. Before you install the downloaded wheel using **pip** you must ensure you have an appropriate Qt license and have decided how you want to distribute your PyQt6 wheels to your developers.
By default, installing the commercial PyQt6 wheel will do the same as installing the GPL wheel, i.e. it will automatically download and install the required parts of a standard LGPL Qt installation from PyPI. There are a number of reasons why you might not want to do this:
  * you have a commercial Qt license and need to make sure that is used with PyQt6
  * you don’t allow your developers access to PyPI
  * you want to minimise the number of wheels you need to distribute to your developers.


Note
Some Qt libraries are licensed under the GPL rather than the LGPL. If your own application license is compatibile with the LGPL but is incompatible with the GPL then you must make sure you do not use the corresponding PyQt modules (even though you have a commercial PyQt license).
The solution to all these issues is to use the **pyqt-bundle** program to bundle a copy of your own Qt installation with your commercial PyQt6. This will produce a new wheel that you can distribute easily to your developers.
**pyqt-bundle** is part of [PyQt-builder](https://pypi.org/project/PyQt-builder/). To install it, run:
```
pip install PyQt-builder

```

The documentation can be found [here](https://pyqt-builder.readthedocs.io/en/stable/pyqtbundle.html).
To uninstall the commercial version, run:
```
pip uninstall PyQt6-commercial

```

## Building and Installing from Source[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#building-and-installing-from-source "Link to this heading")
As described above **pip** can be used to download, build and install the GPL source packages from the [PyQt6](https://pypi.org/project/PyQt6/) project at PyPI. However doing so is not recommended as it is not easy to configure the installation or diagnose any problems.
PyQt6 is built using [PyQt-builder](https://pypi.org/project/PyQt-builder/). To install it, run:
```
pip install PyQt-builder

```

PyQt-builder is an extension to the [SIP](https://pypi.org/project/sip/) bindings generator which will be installed automatically.
The rest of these instructions assume that you have downloaded the PyQt6 sdist from [PyPI](https://pypi.org/project/PyQt6/) and will used SIP’s **sip-install** command line tool to do the build and installation.
If you are using the commercial version of PyQt6 then you should use the download instructions which were sent to you when you made your purchase. You must also download your `pyqt-commercial.sip` license file.
PyQt-builder extends SIP’s build system by adding [options](https://pyqt-builder.readthedocs.io/en/stable/command_line_tools.html) to SIP’s [command line tools](https://python-sip.readthedocs.io/en/stable/command_line_tools.html).
PyQt6 further extends the build system by adding the following options to SIP’s command line tools. 

--confirm-license[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#cmdoption-confirm-license "Link to this definition")
    
Using this confirms that you accept the terms of the PyQt license. If it is omitted then you will be asked for confirmation during configuration. 

--dbus DIR[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#cmdoption-dbus "Link to this definition")
    
The directory containing the `dbus/dbus-python.h` header file of the dbus-python package can be found in the directory `DIR`. 

--license-dir DIR[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#cmdoption-license-dir "Link to this definition")
    
The `pyqt-commercial,sip` license file needed by the commercial version of PyQt6 can be found in the directory `DIR`. By default it is assumed that you have copied it to the `sip` sub-directory of the unpacked sdist. 

--no-dbus-python[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#cmdoption-no-dbus-python "Link to this definition")
    
The Qt support for the dbus-python package will not be built. 

--no-designer-plugin[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#cmdoption-no-designer-plugin "Link to this definition")
    
The Qt Designer plugin will not be built. 

--no-qml-plugin[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#cmdoption-no-qml-plugin "Link to this definition")
    
The **qmlscene** plugin will not be built. 

--no-tools[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#cmdoption-no-tools "Link to this definition")
    
The **pyuic6** and **pylupdate6** tools will not be built. 

--qt-shared[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#cmdoption-qt-shared "Link to this definition")
    
Normally Qt is checked to see if it has been built as shared libraries. Some Linux distributions configure their Qt builds to make this check unreliable. This option ignores the result of the check and assumes that Qt has been built as shared libraries.
### Building the [sip](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/sip/sip-module.html) Module[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#building-the-sip-module "Link to this heading")
It is not necessary to install the [PyQt6.sip](https://www.riverbankcomputing.com/static/Docs/PyQt6/api/sip/sip-module.html) module before building PyQt6 but it must be installed before PyQt6 can be used.
The module is built using `setuptools` and is available from the [PyQt6-sip](https://pypi.org/project/PyQt6-sip/) project at PyPI. It uses `setuptools` as its build system and can be installed by **pip** or you can also unpack the sdist and install it by running its **setup.py** script.
### Building PyQt6[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#building-pyqt6 "Link to this heading")
Once you have downloaded the sdist from PyPI, unpack it and change directory to its top level directory (i.e. the one containing the `pyproject.toml` file.
If you are building the commercial version of PyQt6 then copy the `pyqt-commercial.sip` license file to the `sip` sub-directory.
To build and install PyQt6, run:
```
sip-install

```

In order to see all the available command line options, run:
```
sip-install -h

```

If you want to run **make** seperately then instead run:
```
sip-build --no-make
make
make install

```

### Building PyQt6 Add-on Projects[¶](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#building-pyqt6-add-on-projects "Link to this heading")
The add-on PyQt6 projects are built and installed in exactly the same way as PyQt6 itself. PyQt6 must be built and installed first.
### [Table of Contents](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html)
  * [Installing PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html)
    * [Understanding the Correct Version to Install](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#understanding-the-correct-version-to-install)
    * [Installing from Wheels](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#installing-from-wheels)
      * [Installing the GPL Version](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#installing-the-gpl-version)
      * [Installing the Commercial Version](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#installing-the-commercial-version)
    * [Building and Installing from Source](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#building-and-installing-from-source)
      * [Building the sip Module](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#building-the-sip-module)
      * [Building PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#building-pyqt6)
      * [Building PyQt6 Add-on Projects](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html#building-pyqt6-add-on-projects)


#### Previous topic
[Support for Old Versions of Python](https://www.riverbankcomputing.com/static/Docs/PyQt6/eol_policy.html "previous chapter")
#### Next topic
[Differences Between PyQt6 and PyQt5](https://www.riverbankcomputing.com/static/Docs/PyQt6/pyqt5_differences.html "next chapter")
### Quick search
### Navigation
  * [Index](https://www.riverbankcomputing.com/static/Docs/PyQt6/genindex.html "General index")
  * [Classes](https://www.riverbankcomputing.com/static/Docs/PyQt6/sip-classes.html "Index of all classes") |
  * [Modules](https://www.riverbankcomputing.com/static/Docs/PyQt6/module_index.html "Index of all modules") |
  * [PyQt Documentation v6.9.0](https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html) »
  * [Installing PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/installation.html)


© Copyright 2025, Riverbank Computing Limited, The Qt Company. Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3. 
