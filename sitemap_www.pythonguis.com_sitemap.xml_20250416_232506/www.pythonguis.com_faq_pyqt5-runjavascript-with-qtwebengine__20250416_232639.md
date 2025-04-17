# Content from: https://www.pythonguis.com/faq/pyqt5-runjavascript-with-qtwebengine/

[](https://www.pythonguis.com/faq/pyqt5-runjavascript-with-qtwebengine/#menu)
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
# PyQt5 runjavascript with QtWebEngine
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
mike2750 | 2020-09-19 20:19:25 UTC | #1
Figured I'd share this here as there are very few practicable examples online other then the one i stumbled on the other day which enlightened me to how it works.
I now am able to some super badass stuff with my app and send commands to the ssh session programmatically from Python through the run javscript :slight_smile:
![run_command_from_button|636x500](https://www.pythonguis.com/static/faq/forum/pyqt5-runjavascript-with-qtwebengine/mtN63B3Z1UvMz7S8a7pnAYtjxaP.gif)
full example code for reference.
python ```
#!/usr/bin/env python3
# encoding: utf-8
import os
import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui, QtWebEngineWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QMessageBox, QDialog, QSplashScreen, \
  QDateTimeEdit, QActionGroup, QAbstractItemView, QDockWidget, QPlainTextEdit, QTableWidgetItem
from PyQt5 import QtSql
from PyQt5.QtCore import (QCoreApplication, QRect, QSize, Qt, QUrl, QDateTime, QThread, pyqtSignal as Signal, QEvent,
             QFile, QMetaObject, QRegExp, QSortFilterProxyModel, QSettings, QTimer, QTextStream,
             QStandardPaths, QObject)
# from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel, QSqlQuery
from PyQt5.QtGui import QPixmap, QPalette, QColor, QClipboard, QGuiApplication
from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import QTabWidget, QApplication, QInputDialog, QFileDialog, QPushButton
free_port = '8889'
settings = QtCore.QSettings('WizardAssistant', 'WizardAssistantDesktop')
if settings.contains("wizardwebsshport"):
  # there is the key in QSettings
  # print('Checking for wizardwebsshport in config')
  wizardwebsshport = settings.value('wizardwebsshport')
  # print('Found wizardwebsshport port in config:' + wizardwebsshport)
  free_port = wizardwebsshport
else:
  print('wizardwebsshport not found in config')
  pass
try:
  ssh_terminal_url = 'http://localhost:' + str(free_port)
  print(ssh_terminal_url)
except:
  pass
ssh_username = 'example2'
ssh_password = 'somerandompass'
ssh_key_passphrase = ''
ssh_public_key = ''
ssh_private_key = ''
ssh_host = ''
ssh_hostname = 'dev.example.com'
ssh_port = '22'
ssh_proxy_command = ''
ssh_public_key_file = ''
ssh_private_key_file = ''
totp = ''
cmd = """for phpver in $(ls -1 /opt/cpanel/ |grep ea-php | sed 's/ea-php//g') ; do echo "PHP $phpver" ; /opt/cpanel/ea-php$phpver/root/usr/bin/php -i |grep -Ei 'memory_limit|post_max_size|upload_max_filesize|max_execution_time|session.save_path' && echo "" ; done"""

class TabbedTerminal(QTabWidget):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setDocumentMode(True)
    self.setTabPosition(QTabWidget.South)
    self._new_button = QPushButton(self)
    self._new_button.setText("New SSH Session")
    self._new_button.clicked.connect(self.add_new_tab)
    self.setCornerWidget(self._new_button)
    self.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
    self.currentChanged.connect(self.current_tab_changed)
    self.setTabsClosable(True)
    self.setMovable(True)
    self.tabCloseRequested.connect(self.close_current_tab)
    # Uncomment to disable native menubar on Mac
    # self.menuBar().setNativeMenuBar(False)
    self.add_new_tab(QUrl(ssh_terminal_url), 'Homepage')
    # self.show()
    self.setWindowTitle("Wizard Assistant SSH")
    self.setWindowIcon(QIcon(os.path.join('images', 'ma-icon-64.png')))
  def add_new_tab(self, qurl=ssh_terminal_url, label="Blank"):
    # if qurl is None:
    # qurl = QUrl('http://localhost:8888/')
    qurl = QUrl(ssh_terminal_url)
    browser = QWebEngineView()
    # self.webSettings = browser.settings()
    # self.webSettings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
    # self.webSettings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
    # self.webSettings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
    # self.webSettings.setAttribute(QWebEngineSettings.JavascriptCanAccessClipboard, True)
    # self.webSettings.setAttribute(QWebEngineSettings.JavascriptCanPaste, True)
    # self.webSettings.setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
    # self.webSettings.setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
    # self.webSettings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
    # self.webSettings.setAttribute(QWebEngineSettings.AllowWindowActivationFromJavaScript, True)
    browser.setUrl(qurl)
    i = self.addTab(browser, label)
    self.setCurrentIndex(i)
    # More difficult! We only want to update the url when it's from the
    # correct tab
    # browser.urlChanged.connect(lambda qurl, browser=browser:
    #              self.update_urlbar(qurl, browser))
    browser.loadFinished.connect(lambda _, i=i, browser=browser:
                   self.setTabText(i, browser.page().title()))
    browser.titleChanged.connect(lambda _, i=i, browser=browser:
                   self.setTabText(i, browser.page().title()))
    browser.titleChanged.connect(lambda _, i=i, browser=browser:
                   self.setTabToolTip(i, browser.page().title()))
  def tab_open_doubleclick(self, i):
    if i == -1: # No tab under the click
      self.add_new_tab()
  def current_tab_changed(self, i):
    qurl = self.currentWidget().url()
    self.update_title(self.currentWidget())
  def close_current_tab(self, i):
    if self.count() < 2:
      return
    self.removeTab(i)
  def update_title(self, browser):
    if browser != self.currentWidget():
      # If this signal is not from the current tab, ignore
      return
    title = self.currentWidget().page().title()
    self.setWindowTitle("%s - Wizard Assistant SSH" % title)
  def navigate_webssh(self):
    self.currentWidget().setUrl(QUrl(ssh_terminal_url))
  def navigate_home(self):
    self.currentWidget().setUrl(QUrl(ssh_terminal_url))
  def navigate_to_url(self): # Does not receive the Url
    q = QUrl(self.urlbar.text())
    if q.scheme() == "":
      q.setScheme("http")
    self.currentWidget().setUrl(q)
  def open_file(self):
    filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                         "SSH Private Key (id_*);;"
                         "All files (*.*)")
    if filename:
      with open(filename, 'rb') as f:
        sshkeyprivate = f.read()
    f.close()
  @QtCore.pyqtSlot(bool)
  def on_load_finished(self, ok):
    if ok:
      script = """
      // pass an object to wssh.connect
      var opts = {
       hostname: '%s',
       port: '%s',
       username: '%s',
       password: '%s',
       privatekey: '%s',
       passphrase: '%s',
       totp: '%s'
      };
      wssh.connect(opts);
      """ % (ssh_hostname, ssh_port, ssh_username, ssh_password, ssh_private_key, ssh_key_passphrase, totp)
      self.currentWidget().page().runJavaScript(script)
  @QtCore.pyqtSlot(bool)
  def run_command_via_js(self):
    script = """
    // var cmd = (function() {/**/}).toString().match(/[^]*\/\*([^]*)\*\/\}$/)[1];
      wssh.send(`%s`);
    """ % cmd
    self.currentWidget().page().runJavaScript(script)

qtCreatorFile = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "ui",
               "sshterminal.ui") # Type your file path
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class build(Ui_MainWindow, QtWidgets.QMainWindow):
  def __init__(self, parent=None):
    QtWidgets.QMainWindow.__init__(self)
    Ui_MainWindow.__init__(self)
    self.setupUi(self)
    for name, obj in dict(self.__dict__).items():
      # print(str(name) + str(obj))
      obj_type = str(obj).strip("<PyQt5").rsplit(" ")[0].replace(".", '', 1)
      # obj_type = str(obj).strip("<").rsplit(" ")[0]
      # print(obj_type)
      # obj_type = obj_str.strip("<PyQt5").rsplit(" ")[0].replace(".", '', 1)
      label_name = "self." + str(name)
      try:
        label_name = self.findChild(eval(obj_type), name)
        print(str(label_name) + ' created')
      except:
        pass
      if not isinstance(obj_type, QObject):
        continue
    try:
      print('Trying to embed SSH Terminal Widget')
      self.sshterminal = TabbedTerminal(self.ssh_placeholder_widget)
      self.sshterminal.setObjectName(u"sshterminal")
      self.verticalLayout_2.addWidget(self.sshterminal)
      self.sshterminal.setStyleSheet("QTabBar::tab { height: 25px; width: 125px; }")
      print('Embedded SSH Terminal Widget completed')
    except:
      print('Unable to embed SSH Terminal Widget')
      pass
    self.new_session_pushButton.setText('Run command')
    self.new_session_pushButton.clicked.connect(self.sshterminal.run_command_via_js)

def start():
  app = QtWidgets.QApplication(sys.argv)
  QApplication.setStyle("Fusion")
  #
  # # Now use a palette to switch to dark colors:
  palette = QPalette()
  palette.setColor(QPalette.Window, QColor(53, 53, 53))
  palette.setColor(QPalette.WindowText, Qt.white)
  palette.setColor(QPalette.Base, QColor(25, 25, 25))
  palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
  palette.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
  palette.setColor(QPalette.ToolTipText, Qt.white)
  palette.setColor(QPalette.Text, Qt.white)
  palette.setColor(QPalette.Button, QColor(53, 53, 53))
  palette.setColor(QPalette.ButtonText, Qt.white)
  palette.setColor(QPalette.BrightText, Qt.red)
  palette.setColor(QPalette.Link, QColor(42, 130, 218))
  palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
  palette.setColor(QPalette.HighlightedText, Qt.black)
  QApplication.setPalette(palette)
  bld = build()
  bld.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  start()

```

Now with this I can do some really slick stuff now not possible in any other way in most terminals :slight_smile:
![double_click_execution|690x402](https://www.pythonguis.com/static/faq/forum/pyqt5-runjavascript-with-qtwebengine/rM2d6mZIB87K6XwRIhwS4G3BTmb.gif)
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
Hopefully this will help someone else out if theyre looking for how to do this with QtWebengine
Resources: https://stackoverflow.com/questions/55947552/pyqt5-retrieve-form-values-using-runjavascript https://doc.qt.io/qtforpython/PySide2/QtWebEngineWidgets/QWebEnginePage.html#id5 http://www.366service.com/jp/qa/be447fc5bf361b1c7ab234de61497a0d http://python.6.x6.nabble.com/inject-code-to-webpage-using-QWebEnginePage-runJavaScript-td5255473.html
martin | 2020-09-19 20:19:04 UTC | #2
This is really nice @mike2750 thanks for sharing! I can see what you were getting at now -- being able to trigger more complex commands from a simple menu (effectively macros I guess?) ...will it be possible for users to add custom ones too?
How does this bit work (...i.e. where is the `cmd` var set)?
python ```
  @QtCore.pyqtSlot(bool)
  def run_command_via_js(self):
    script = """
    // var cmd = (function() {/**/}).toString().match(/[^]*\/\*([^]*)\*\/\}$/)[1];
      wssh.send(`%s`);
    """ % cmd
    self.currentWidget().page().runJavaScript(script)

```

mike2750 | 2020-09-20 03:17:07 UTC | #3
Thanks. Yeah it does kinda work like a macro in a way. Its like pasting it in but being executed via the runjavascript and the wssh.send in [wizardwebssh](https://gitlab.com/mikeramsey/wizardwebssh).
I do play to add command editing but I'm working on finishing up the SSH config editor which i did im using the data widget mapper for. ![image|337x500, 75%](https://www.pythonguis.com/static/faq/forum/pyqt5-runjavascript-with-qtwebengine/wHkKrVRLspNWqNJLwugJCqwuVmT.png)
I plan to use the same approach with the command editor but the main hurdle is i want user added commands to be merged seamlessly with the auto updating main commands db. It looks like i will have to use QT SQL Query approach to search across multiple sqlite databases or use a [QConcatenateTablesProxyModel](https://doc.qt.io/qt-5/qconcatenatetablesproxymodel.html) so that results from the built in or company level commands db which self updates doesn't overwrite the user level commands db which will be in
For windows:
python ```
%LocalAppData%\WizardAssistant\WizardAssistantDesktop

```

Which with pyqt settings i load like this
python ```
settings = QtCore.QSettings('WizardAssistant', 'WizardAssistantDesktop')
config_data_dir = Path("WizardAssistant/WizardAssistantDesktop")
if settings.contains("sshconfig_db"):
  # there is the key in QSettings
  print('Checking for ssh_db location preference in config')
  sshconfig_db = settings.value('sshconfig_db')
  print('Found sshconfig_db in config:' + sshconfig_db)
else:
  print('sshconfig_db not found in config. Using default')
  sshconfig_db = QStandardPaths.writableLocation(
    QStandardPaths.AppConfigLocation) / config_data_dir / "wizardwebssh.db"
  settings.setValue('sshconfig_db', str(sshconfig_db))
  pass

```

In regards to the command its dynamically generated depending on form input if there is variable information then substitutions occur on the placeholder variable names. I'll be submitting my app for review and code advise eventually here once it feel its almost done with the major stuff.
python ```
  def listclicked(self, index):
    print('============BEGIN listclicked==================')
    global cmd_replaced
    row = index.row()
    cmd = self.proxy_model.data(self.proxy_model.index(row, 3))
    cmd_requires = self.proxy_model.data(self.proxy_model.index(row, 4))
    cmd_description = self.proxy_model.data(self.proxy_model.index(row, 5))
    print(cmd_description)
    self.command_description.setText(cmd_description)
    self.command_requires_label.setText('Requires: ' + cmd_requires.upper())
    global ticketid, domain, url, email, email2, username, clientip, date_time_input, apache_dom_date, apache_error_date, litespeed_error_date, dcpumon_date, linuxlog_date, atop_date, time_24hr_format, time_12hr_format, apache_dom_datetime, apache_error_datetime, litespeed_error_datetime, linuxlog_datetime, panel_main_error_log, panel_login_log, session_log, access_log, http_error_log, http_error_logs_dir, modsec_log, domlog_path, ssh_log, ftp_log, cron_log, firewall_log, bruteforce_log, email_mainlog, email_authlog, kernel_general_log, mysql_log, suspension_log, malware_scanner, malware_scanner_q, support_email, company_script_domain, fix_perms
    self.form_variable_setup()
    self.controlpanel_logs_substitutions()
    def get_random_alphanumeric_string(length):
      letters_and_digits = string.ascii_letters + string.digits
      result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
      print("Random alphanumeric String is:", result_str)
      return result_str
    random_pass = get_random_alphanumeric_string(8)
    substitutions = {
      "TicketIDInputField": ticketid,
      "DomainInputField": domain,
      "Email1InputField": email,
      "Email2InputField": email2,
      "CPUsernameInputField": username,
      "DatabaseNameInputField": databasename,
      "ClientIPInputField": clientip,
      "ApacheErrorDateInputField": apache_error_date,
      "LitespeedErrorDateInputField": litespeed_error_date,
      "DcpumonDateInputField": dcpumon_date,
      "LinuxDateInputField": linuxlog_date,
      "LinuxDayNumberInputField": linuxlog_day_number,
      "AtopDateInputField": atop_date,
      "TimeInputField_time_24hr_format": time_24hr_format,
      "TimeInputField_time_12hr_format": time_12hr_format,
      "ApacheDomDateInputField": apache_dom_date,
      "ApacheDomDateTimeInputField": apache_dom_datetime,
      "ApacheErrorDateTimeInputField": apache_error_datetime,
      "LitespeedErrorDateTimeInputField": litespeed_error_datetime,
      "LinuxDateTimeInputField": linuxlog_datetime,
      "PanelMainErrorLog": panel_main_error_log,
      "PanelLoginLog": panel_login_log,
      "PanelSessionLog": session_log,
      "PanelAccessLog": access_log,
      "HTTPErrorLog": http_error_log,
      "HTTPErrorLogsDir": http_error_logs_dir,
      "ModsecLog": modsec_log,
      "DomLogPath": domlog_path,
      "SSHLog": ssh_log,
      "FTPLog": ftp_log,
      "CronLog": cron_log,
      "FirewallLog": firewall_log,
      "BruteforceLog": bruteforce_log,
      "EmailMainLog": email_mainlog,
      "EmailAuthLog": email_authlog,
      "KernelGeneralLog": kernel_general_log,
      "MySQLLog": mysql_log,
      "SuspensionLog": suspension_log,
      "MalwareScanner": malware_scanner,
      "MalwareScannerQuarantine": malware_scanner_q,
      "SupportEmail": support_email,
      "CompanyScriptDomain": company_script_domain,
      "RandomPass": random_pass,
      "FixPerms": fix_perms, }
    cmd_replaced = replace(cmd, substitutions)
    # print(row)
    # print(cmd)
    print()
    # print("id = %s" % projectModel.record(row).field(0).value().toString())
    print("command = %s" % self.proxy_model.data(self.proxy_model.index(row, 3)))
    print("adjusted command = %s" % cmd_replaced)
    command_alias_selected = self.proxy_model.data(self.proxy_model.index(row, 2))
    # dialog_notification('Command Copied to Clipboard' + str(command_alias_selected))
    # setup clipboard and copy command to clipboard when selected
    clipboard = QGuiApplication.clipboard()
    original_text = clipboard.text()
    clipboard.setText(cmd_replaced)
    if is_linux():
      clipboard.setText(cmd_replaced, QClipboard.Selection)
    self.sshterminal.setFocusPolicy(Qt.StrongFocus)
    # self.sshterminal.setText(clipboard.text())
    print('============END listclicked==================')

```

Also been trying to figure out how to define the tooltip for tableview from existing qsqltable model seen nothing conclusive how to do that but it might be easier to do if i switch to QT SQL Query or proxy model i suppose.
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PyQt5 runjavascript with QtWebEngine** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyqt5-runjavascript-with-qtwebengine/Python books) on the subject. 
**PyQt5 runjavascript with QtWebEngine** was published in [faq](https://www.pythonguis.com/faq/) on September 15, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
