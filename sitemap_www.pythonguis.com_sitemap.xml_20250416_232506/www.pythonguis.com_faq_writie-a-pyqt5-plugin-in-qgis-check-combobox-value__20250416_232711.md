# Content from: https://www.pythonguis.com/faq/writie-a-pyqt5-plugin-in-qgis-check-combobox-value/

[](https://www.pythonguis.com/faq/writie-a-pyqt5-plugin-in-qgis-check-combobox-value/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PyQt5 ](https://www.pythonguis.com/pyqt5/)
  * [PyQt5 Tutorial ](https://www.pythonguis.com/pyqt5-tutorial/)
  * Basics
  * [Create a PyQt5 app](https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/)
  * [PyQt5 Signals](https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/)
  * [PyQt5 Widgets](https://www.pythonguis.com/tutorials/pyqt-basic-widgets/)
  * [PyQt5 Layouts](https://www.pythonguis.com/tutorials/pyqt-layouts/)
  * [PyQt5 Menus](https://www.pythonguis.com/tutorials/pyqt-actions-toolbars-menus/)
  * [PyQt5 Dialogs](https://www.pythonguis.com/tutorials/pyqt-dialogs/)
  * [Multi-window PyQt5](https://www.pythonguis.com/tutorials/creating-multiple-windows/)
  * Qt Designer
  * [First Qt Designer app](https://www.pythonguis.com/tutorials/first-steps-qt-creator/)
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/creating-dialogs-qt-designer/)
  * [The QResource System in PyQt5](https://www.pythonguis.com/tutorials/qresource-system/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyqt-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/)
  * Plotting
  * [Plotting With PyQtGraph and PyQt5](https://www.pythonguis.com/tutorials/plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PyQt5](https://www.pythonguis.com/tutorials/plotting-matplotlib/)
  * QGraphics
  * [Vector Graphics](https://www.pythonguis.com/tutorials/pyqt-qgraphics-vector-graphics/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/qpropertyanimation/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/system-tray-mac-menu-bar-applications-pyqt/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-pyinstaller-macos-dmg/)
  * [Packaging for Linux](https://www.pythonguis.com/tutorials/packaging-pyqt5-applications-linux-pyinstaller/)
  * [Packaging QResources](https://www.pythonguis.com/tutorials/packaging-data-files-pyqt5-with-qresource-system/)
  * [Packaging with fbs](https://www.pythonguis.com/tutorials/packaging-pyqt5-apps-fbs/)
  * Resources
  * [Books](https://www.pythonguis.com/books/)
  * Services
  * [Consulting](https://www.pythonguis.com/hire/)
  * [1:1 Coaching](https://www.pythonguis.com/live/)
  * [Contact](https://www.pythonguis.com/contact/)
  * [About](https://www.pythonguis.com/about/)
  * Libraries
  * [PyQt6](https://www.pythonguis.com/pyqt6/)
  * [PySide6](https://www.pythonguis.com/pyside6/)
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Writie a PyQT5 Plugin in QGIS (Check ComboBox Value)
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
yuriyrogalski11143 | 2021-05-11 11:45:54 UTC | #1
Hello dear Python Community,
its my first expecience to write a QGIS Plugin with PyQT5. With Plugin Builder i allready Set up the Development Folder and here i have those 3 Files (posted with the Code below) which i can open and execute with Atom and run in QGIS
SPBIM.py (as I understand the main File for writing my App) SPBIM_dialog.py (this File it tells me loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer SPBIM_dialog_base.py (File which was converted converted in cmd line with **pyuic5 -x Plugin_dialog_base.ui -o Plugin_dialog_base.py** - If i hadn't used the Qt Designer i could have Set up the Interface in here, but not sure the purpose of this File - if i have to add sth here
I have only a ComboBox and a Button Box Object: comboBox Class: QComboBox Object: button_box Class: QDialogButtonBox
The purpose of this Plugin (which is allready implemented in QGIS) is to Check the Values (5 Values set up in QtDesigner) the User activated/ picked in the Combobox !!!
Depending on the Value chosen - a bunch of more Python Code (5 different/ other Python Files) should be implemented/ executed/ run) - from File / in a Function?! 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
i can activate self.comboBox in Plugin_dialog_base.py File (but not in SPBIM.py File)
Thank you for advise / hints help. Really trying to get this work done!
From other Forums i found the hint (but don't know how to implement this idea in the SPBIM_dialog.py File) Your "check boxes" don't work because you're putting your lines in the wrong place (**run** method). However, you need first to declare objects in ****init**** method for connecting them to a 'change_status' function (preferably one for each check box). I'm going to exemplify this only for "Interpretation" Check Box.
QGIS environment tells me in SPBIM.py it can't find my both Elemenets (combo_box, button_box) !!! 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
File: SPBIM.py
python ```
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .SPBIM_dialog import SPBIMDialog
import os.path

class SPBIM:
  """QGIS Plugin Implementation."""

def __init__(self, iface):
  """Constructor.
  :param iface: An interface instance that will be passed to this class
    which provides the hook by which you can manipulate the QGIS
    application at run time.
  :type iface: QgsInterface
  """
  # Save reference to the QGIS interface
  self.iface = iface
  # initialize plugin directory
  self.plugin_dir = os.path.dirname(__file__)
  # initialize locale
  locale = QSettings().value('locale/userLocale')[0:2]
  locale_path = os.path.join(
    self.plugin_dir,
    'i18n',
    'SPBIM_{}.qm'.format(locale))
  if os.path.exists(locale_path):
    self.translator = QTranslator()
    self.translator.load(locale_path)
    QCoreApplication.installTranslator(self.translator)
  # Declare instance attributes
  self.actions = []
  self.menu = self.tr(u'&SPBIM')
  # Check if plugin was started the first time in current QGIS session
  # Must be set in initGui() to survive plugin reloads
  self.first_start = None
# noinspection PyMethodMayBeStatic
def tr(self, message):
  """Get the translation for a string using Qt translation API.
  We implement this ourselves since we do not inherit QObject.
  :param message: String for translation.
  :type message: str, QString
  :returns: Translated version of message.
  :rtype: QString
  """
  # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
  return QCoreApplication.translate('SPBIM', message)

def add_action(
  self,
  icon_path,
  text,
  callback,
  enabled_flag=True,
  add_to_menu=True,
  add_to_toolbar=True,
  status_tip=None,
  whats_this=None,
  parent=None):
  """Add a toolbar icon to the toolbar.
  :param icon_path: Path to the icon for this action. Can be a resource
    path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
  :type icon_path: str
  :param text: Text that should be shown in menu items for this action.
  :type text: str
  :param callback: Function to be called when the action is triggered.
  :type callback: function
  :param enabled_flag: A flag indicating if the action should be enabled
    by default. Defaults to True.
  :type enabled_flag: bool
  :param add_to_menu: Flag indicating whether the action should also
    be added to the menu. Defaults to True.
  :type add_to_menu: bool
  :param add_to_toolbar: Flag indicating whether the action should also
    be added to the toolbar. Defaults to True.
  :type add_to_toolbar: bool
  :param status_tip: Optional text to show in a popup when mouse pointer
    hovers over the action.
  :type status_tip: str
  :param parent: Parent widget for the new action. Defaults None.
  :type parent: QWidget
  :param whats_this: Optional text to show in the status bar when the
    mouse pointer hovers over the action.
  :returns: The action that was created. Note that the action is also
    added to self.actions list.
  :rtype: QAction
  """
  icon = QIcon(icon_path)
  action = QAction(icon, text, parent)
  action.triggered.connect(callback)
  action.setEnabled(enabled_flag)
  if status_tip is not None:
    action.setStatusTip(status_tip)
  if whats_this is not None:
    action.setWhatsThis(whats_this)
  if add_to_toolbar:
    # Adds plugin icon to Plugins toolbar
    self.iface.addToolBarIcon(action)
  if add_to_menu:
    self.iface.addPluginToMenu(
      self.menu,
      action)
  self.actions.append(action)
  return action
def initGui(self):
  """Create the menu entries and toolbar icons inside the QGIS GUI."""
  icon_path = ':/plugins/SPBIM/icon.png'
  self.add_action(
    icon_path,
    text=self.tr(u'SPBIM'),
    callback=self.run,
    parent=self.iface.mainWindow())
  # will be set False in run()
  self.first_start = True


def unload(self):
  """Removes the plugin menu item and icon from QGIS GUI."""
  print("UNLOADING Plugin")

  for action in self.actions:
    self.iface.removePluginMenu(
      self.tr(u'&SPBIM'),
      action)
    self.iface.removeToolBarIcon(action)



def run(self):
  """Run method that performs all the real work"""
  print("STARTING Plugin")

  # Create the dialog with elements (after translation) and keep reference
  # Only create GUI ONCE in callback, so that it will only load when the plugin is started
  if self.first_start == True:
    self.first_start = False
    self.dlg = SPBIMDialog()
  # show the dialog
  self.dlg.show()
  # Run the dialog event loop
  result = self.dlg.exec_()
  # See if OK was pressed
  if result:
    # Do something useful here - delete the line containing pass and
    # substitute with your code.
    #
    #
    pass

  print("STARTING Plugin")

```

File: SPBIM_dialog.py
python ```
import os
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
  os.path.dirname(__file__), 'SPBIM_dialog_base.ui'))

class SPBIMDialog(QtWidgets.QDialog, FORM_CLASS):
  def __init__(self, parent=None):
    """Constructor."""
    super().__init__(parent)
    # Set up the user interface from Designer through FORM_CLASS.
    # After self.setupUi() you can access any designer object by doing
    # self.<objectname>, and you can use autoconnect slots - see
    # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
    # #widgets-and-dialogs-with-auto-connect
    self.setupUi(self)

```

File: SPBIM_dialog_base.py
python ```
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SPBIMDialogBase(object):
  def setupUi(self, SPBIMDialogBase):
    SPBIMDialogBase.setObjectName("SPBIMDialogBase")
    SPBIMDialogBase.resize(613, 184)
    self.gridLayout = QtWidgets.QGridLayout(SPBIMDialogBase)
    self.gridLayout.setObjectName("gridLayout")
    spacerItem = QtWidgets.QSpacerItem(20, 72, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
    self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
    self.button_box = QtWidgets.QDialogButtonBox(SPBIMDialogBase)
    self.button_box.setOrientation(QtCore.Qt.Horizontal)
    self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
    self.button_box.setObjectName("button_box")
    self.gridLayout.addWidget(self.button_box, 3, 3, 1, 1)
    self.label = QtWidgets.QLabel(SPBIMDialogBase)
    self.label.setObjectName("label")
    self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
    self.comboBox = QtWidgets.QComboBox(SPBIMDialogBase)
    self.comboBox.setObjectName("comboBox")
    self.comboBox.addItem("")
    self.comboBox.addItem("")
    self.comboBox.addItem("")
    self.comboBox.addItem("")
    self.comboBox.addItem("")
    self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
    spacerItem1 = QtWidgets.QSpacerItem(225, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
    spacerItem2 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
    self.retranslateUi(SPBIMDialogBase)
    self.button_box.accepted.connect(SPBIMDialogBase.accept)
    self.button_box.rejected.connect(SPBIMDialogBase.reject)
    QtCore.QMetaObject.connectSlotsByName(SPBIMDialogBase)
  def retranslateUi(self, SPBIMDialogBase):
    _translate = QtCore.QCoreApplication.translate
    SPBIMDialogBase.setWindowTitle(_translate("SPBIMDialogBase", "SPBIM"))
    self.label.setText(_translate("SPBIMDialogBase", "XXX:"))
    self.comboBox.setItemText(0, _translate("SPBIMDialogBase", "1. XXX"))
    self.comboBox.setItemText(1, _translate("SPBIMDialogBase", "2. XXX"))
    self.comboBox.setItemText(2, _translate("SPBIMDialogBase", "3. XXX"))
    self.comboBox.setItemText(3, _translate("SPBIMDialogBase", "4. XXX"))
    self.comboBox.setItemText(4, _translate("SPBIMDialogBase", "5. XXX"))

if __name__ == "__main__":
  import sys
  app = QtWidgets.QApplication(sys.argv)
  SPBIMDialogBase = QtWidgets.QDialog()
  ui = Ui_SPBIMDialogBase()
  ui.setupUi(SPBIMDialogBase)
  SPBIMDialogBase.show()
  sys.exit(app.exec_())

```

1:1 Coaching & Tutoring for your Python GUIs project
[![Martin Fitzpatrick Python GUIs Coaching & Training](https://www.pythonguis.com/static/theme/images/products/coaching.jpg)](https://calendly.com/martinfitzpatrick/60min-python-guis-coaching)
[60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/) [Book Now](https://www.pythonguis.com/live/)
1:1 Python GUIs Coaching & Training
**Comprehensive code review** • **Bugfixes** & improvements • **Maintainability** advice and **architecture** improvements • **Design and usability** assessment • Suggestions and tips to **expand your knowledge** • **Packaging and distribution** help for Windows, Mac & Linux • [Find out more.](https://www.pythonguis.com/live)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Writie a PyQT5 Plugin in QGIS (Check ComboBox Value)** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/writie-a-pyqt5-plugin-in-qgis-check-combobox-value/Python books) on the subject. 
**Writie a PyQT5 Plugin in QGIS (Check ComboBox Value)** was published in [faq](https://www.pythonguis.com/faq/) on May 10, 2021 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
  * [](https://www.pythonguis.com/ "Python GUIs")
  * [Databases & SQL](https://www.pythonguis.com/topics/databases/)
  * [Learn the fundamentals](https://www.pythonguis.com/topics/foundation/)
  * [Where do I begin?](https://www.pythonguis.com/topics/getting-started/)
  * [Data Science](https://www.pythonguis.com/topics/data-science/)
  * [Packaging & Distribution](https://www.pythonguis.com/topics/packaging/)
  * [QML/QtQuick](https://www.pythonguis.com/topics/qml/)
  * [Raspberry Pi](https://www.pythonguis.com/topics/raspberry-pi/)
  * [Games](https://www.pythonguis.com/topics/games/)
  * [Intermediate Tutorials](https://www.pythonguis.com/topics/intermediate/)


  * **Sections**
  * [Installation](https://www.pythonguis.com/installation/)
  * [First steps with PySide6](https://www.pythonguis.com/tutorials/pyside6-creating-your-first-window/)
  * [First steps with PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/)
  * [Example Python Apps](https://www.pythonguis.com/examples/)
  * [Widget Library](https://www.pythonguis.com/widgets/)
  * [Simple PyQt6 & PySide6 documentation](https://www.pythonguis.com/docs/)
  * [Reusable code & snippets](https://www.pythonguis.com/code/)
  * [Frequently Asked Questions](https://www.pythonguis.com/faq/)


  * **Tutorials**
  * [Which Python GUI library?](https://www.pythonguis.com/faq/which-python-gui-library/)
  * [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/)
  * [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/)
  * [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/)
  * [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/)
  * [Tkinter tutorial](https://www.pythonguis.com/tkinter-tutorial/)
  * [Latest articles](https://www.pythonguis.com/blog/)


  * **Books & Downloads**
  * [ Your Downloads](https://www.martinfitzpatrick.com/library/)
  * [PyQt5 Book](https://www.pythonguis.com/pyqt5-book/) / [PySide2 Book](https://www.pythonguis.com/pyside2-book/)
  * [PyQt6 Book](https://www.pythonguis.com/pyqt6-book/) / [PySide6 Book](https://www.pythonguis.com/pyside6-book/)
  * [Python Packaging Book](https://www.pythonguis.com/packaging-book/)
  * [ Book Source Code](https://www.pythonguis.com/books/downloads/)
  * [ PyQt6 Video Course](https://www.martinfitzpatrick.com/pyqt6-crash-course/)


  * **Community & Consulting**
  * [ Python GUIS Forum ](https://forum.pythonguis.com/)
  * [ Feedback & Corrections](https://tally.so/r/wbvxNE)
  * [Consulting](https://www.pythonguis.com/hire/)
  * [Mentoring](https://www.pythonguis.com/live/)
  * [Contact me](https://www.martinfitzpatrick.com/contact)
  * [Licensing, Privacy & Legal](https://www.martinfitzpatrick.com/legal)


[](https://twitter.com/pythonguis) [](https://github.com/pythonguis) [](https://www.facebook.com/pythonguis) [](https://www.youtube.com/channel/UCMW4KwSlygaDef0tgqPjbRQ) [](https://www.linkedin.com/company/pythonguis/)
[Python GUIs](https://www.pythonguis.com/) Copyright ©2014-2025 [ Martin Fitzpatrick](https://www.martinfitzpatrick.com)
Tutorials CC-BY-NC-SA [Sitemap](https://www.pythonguis.com/sitemap/) [Changelog](https://www.pythonguis.com/changelog/) Public code [BSD](https://opensource.org/licenses/BSD-2-Clause) & [MIT](https://opensource.org/licenses/MIT)
