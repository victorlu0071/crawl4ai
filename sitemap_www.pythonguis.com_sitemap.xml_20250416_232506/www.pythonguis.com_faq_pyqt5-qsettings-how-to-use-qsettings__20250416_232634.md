# Content from: https://www.pythonguis.com/faq/pyqt5-qsettings-how-to-use-qsettings/

[](https://www.pythonguis.com/faq/pyqt5-qsettings-how-to-use-qsettings/#menu)
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
# Pyqt5 QSettings. how to use QSettings
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
meshelleva4815 | 2021-05-07 20:58:01 UTC | #1
Hi Martin's, please can you help on a tutorial on how to use QSettings. am currently having issues in using the module or library 😀😀 in my current project, I have so many options that I need the settings to enable or disable, I tried the documentation but it's really not helping. I just need an in-depth or even if it's a demo on how to use the settings. I count much on your respond soon boss. how is your baby..? good morning
mike2750 | 2021-05-07 20:58:10 UTC | #2
yeah this is a very confusing thing once i learned paid off nicely. I'm dumping some examples of stuff to give you an idea of how i used it with related helpful links.
Here's a test script to set and view settings.
python ```
import sys
import os
from PyQt5 import QtCore

settings = QtCore.QSettings('WizardAssistant', 'WizardAssistantDesktop')
print(settings.fileName())
settings.setValue('wizardwebsshport', 8889)
#settings.setValue('theme_selection', 'Dark')
#settings.setValue('license', 'XXXXX-XXXX-XXXXX-XXXX')
#settings.remove('license')
keys = settings.allKeys()
print(keys)

```

Here's how you can define and load settings from Qsettings in app
python ```
settings = QtCore.QSettings('WizardAssistant', 'WizardAssistantDesktop')
config_data_dir = Path("WizardAssistant/WizardAssistantDesktop")
license_file = QStandardPaths.writableLocation(
  QStandardPaths.AppConfigLocation) / config_data_dir / 'wizardassistant_license.skm'


# Restore settings if exist or set a default
if settings.contains("theme_selection"):
  # there is the key in QSettings
  print('Checking for theme preference in config')
  theme_selection = settings.value('theme_selection')
  print('Found theme_selection in config:' + theme_selection)
else:
  print('theme_selection not found in config. Using default Darkmode')
  settings.setValue('theme_selection', 'Dark')
  pass
if settings.contains("panel_name"):
  # there is the key in QSettings
  print('Checking for default panel_name in config')
  panel_name = settings.value('panel_name')
  print('Found panel_name in config:' + str(panel_name))
else:
  print('panel_name not found in config. Using default: Cyberpanel')
  settings.setValue('panel_name', 'cyberpanel')
  panel_name = str(settings.value('panel_name'))
  pass

class AppContext(ApplicationContext):
  def run(self):
    global version, current_version, current_release_notes_url, license_type, trial_license, lite_license, premium_license, professional_license, corporate_license, license_expiration, license_key_is_valid, license_key, license_string, current_release_url
    version = self.build_settings['version']
    QApplication.setApplicationName("WizardAssistantDesktop")
    QApplication.setOrganizationName("WizardAssistant")
    QApplication.setOrganizationDomain("wizardassistant.com")
    # Splash startup screen initialization
    self.splash = QSplashScreen(
      QPixmap(os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), 'images', 'chevron_logo.png')))
    self.splash.show()
    self.settings = QSettings()
    print(self.settings.fileName())
    def load_license_from_config():
      global license_string
      if self.settings.contains("license"):
        # there is the key in QSettings
        print('Checking for license in config')
        license_string = self.settings.value('license')
        print('Found license in config:' + license_string)
      else:
        print('License not found in config')
        pass

```

Resource links I found helpful when learning and saved. https://doc.qt.io/qtforpython/PySide2/QtCore/QSettings.html#basic-usage https://doc.qt.io/qtforpython/overviews/qtwidgets-mainwindows-application-example.html#application-example https://doc.qt.io/qtforpython/PySide2/QtCore/QSettings.html#PySide2.QtCore.PySide2.QtCore.QSettings.setPath https://doc.qt.io/qtforpython/PySide2/QtCore/QSettings.html#PySide2.QtCore.PySide2.QtCore.QSettings.isWritable https://www.riverbankcomputing.com/static/Docs/PyQt4/qsettings.html https://www.riverbankcomputing.com/static/Docs/PyQt5/pyqt_qsettings.html https://medium.com/manash-en-blog/quick-qt-1-saving-settings-of-qt-applications-using-qsettings-a4ef4f0033e3 https://stackoverflow.com/questions/53108577/check-if-qsettings-is-using-the-default-value https://doc.qt.io/qtforpython/PySide2/QtCore/QSettings.html#PySide2.QtCore.PySide2.QtCore.QSettings.allKeys https://stackoverflow.com/questions/58904533/restoring-qcheckbox-with-qsettings
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
On that same path you will probably want to know where these Qsettings are stored and control that possibly so ill leave this related information here to hopefully save you and others time.
Qstandardpaths test file shows you paths of where things would go on that OS when run.
python ```
from PyQt5 import QtCore
from PyQt5.QtCore import QStandardPaths
# https://doc.qt.io/qtforpython/PySide2/QtCore/QStandardPaths.html#more
print(str(QStandardPaths.writableLocation(QStandardPaths.AppConfigLocation)))
print(str(QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)))
print(str(QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)))
print(str(QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)))
std_paths_list_names = ['QStandardPaths.DesktopLocation', 'QStandardPaths.DocumentsLocation',
            'QStandardPaths.FontsLocation', 'QStandardPaths.ApplicationsLocation',
            'QStandardPaths.MusicLocation', 'QStandardPaths.MoviesLocation',
            'QStandardPaths.PicturesLocation', 'QStandardPaths.TempLocation', 'QStandardPaths.HomeLocation',
            'QStandardPaths.DataLocation', 'QStandardPaths.CacheLocation',
            'QStandardPaths.GenericCacheLocation', 'QStandardPaths.GenericDataLocation',
            'QStandardPaths.RuntimeLocation', 'QStandardPaths.ConfigLocation',
            'QStandardPaths.DownloadLocation', 'QStandardPaths.GenericConfigLocation',
            'QStandardPaths.AppDataLocation', 'QStandardPaths.AppLocalDataLocation',
            'QStandardPaths.AppConfigLocation']
std_paths_list = [QStandardPaths.DesktopLocation, QStandardPaths.DocumentsLocation, QStandardPaths.FontsLocation,
         QStandardPaths.ApplicationsLocation, QStandardPaths.MusicLocation, QStandardPaths.MoviesLocation,
         QStandardPaths.PicturesLocation, QStandardPaths.TempLocation, QStandardPaths.HomeLocation,
         QStandardPaths.DataLocation, QStandardPaths.CacheLocation, QStandardPaths.GenericCacheLocation,
         QStandardPaths.GenericDataLocation, QStandardPaths.RuntimeLocation, QStandardPaths.ConfigLocation,
         QStandardPaths.DownloadLocation, QStandardPaths.GenericConfigLocation, QStandardPaths.AppDataLocation,
         QStandardPaths.AppLocalDataLocation, QStandardPaths.AppConfigLocation]
for path in std_paths_list:
  print(str(path))
  print(str(QStandardPaths.writableLocation(path)))
print(str(QStandardPaths.writableLocation(QStandardPaths.AppConfigLocation)))

```

Related resources: https://doc.qt.io/qtforpython/PySide2/QtCore/QStandardPaths.html#more https://www.ics.com/blog/whats-new-qt-5-qstandardpaths https://community.kde.org/Frameworks/Porting_Notes/KStandardDirs https://contingencycoder.wordpress.com/2013/07/07/quick-tip-qt-5-standard-paths/
meshelleva4815 | 2020-10-10 07:23:53 UTC | #3
😱😱I can't thank you enough Mike. this far more than I was expecting. I really appreciate. good days ahead I hope and pray...thank you
mike2750 | 2020-10-10 09:20:46 UTC | #4
My pleasure. Always happy to help. some of this stuff is a real pita due to limited examples of real usage so involves a lot of trial and error.
I love to share and save others from the same frustration I experienced. :)
I definitely think both of these topics would make for nice tutorial ideas. 
The Qsettings thing had i learned about it sooner would have saved me a ton of time. I was having trouble sharing what port a service was listening on between two different processes in the app one being a service/daemon and had i know i could have used Qsettings to share the current port atomicly without dealing with temporary files reading/writing that would have saved me a week of my time off being frustrated with why i was not able to read/write to installation path from frozen/installed app lol. 
There is so many cool ways to use that and my examples are pretty basic. I don't know fully what all settings I'm going to have but i will probably build them into a dictionary or list and loop through loading/restoring them vs the one by one approach ive been doing as i add new ones.
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Pyqt5 QSettings. how to use QSettings** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyqt5-qsettings-how-to-use-qsettings/Python books) on the subject. 
**Pyqt5 QSettings. how to use QSettings** was published in [faq](https://www.pythonguis.com/faq/) on October 09, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
