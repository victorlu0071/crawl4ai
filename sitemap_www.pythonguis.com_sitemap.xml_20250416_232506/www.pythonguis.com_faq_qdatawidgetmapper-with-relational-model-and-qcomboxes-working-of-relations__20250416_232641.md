# Content from: https://www.pythonguis.com/faq/qdatawidgetmapper-with-relational-model-and-qcomboxes-working-of-relations/

[](https://www.pythonguis.com/faq/qdatawidgetmapper-with-relational-model-and-qcomboxes-working-of-relations/#menu)
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
# QDataWidgetMapper with relational model and qcomboxes working of relations
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
mike2750 | 2021-06-07 00:33:26 UTC | #1
Has anyone gotten something like this to work? https://doc.qt.io/qtforpython/overviews/qtsql-sqlwidgetmapper-example.html#sql-widget-mapper-example
Tried but not having any luck and their examples are not in python just the same snippets from C++ which while is kinda helpful not actually useful as it does not have full working example can just translate and make work.
All of the fields work and show values except the qcomboboxes for "SSH Key Name", "SSH Config Name", and Group(SSH Group Name) .
python ```
self.ssh_key_name = QComboBox()
self.ssh_config_name = QComboBox()
self.ssh_group = QComboBox()

```

Screenshot: ![Screenshot from 2021-06-06 16-10-36|456x428](https://www.pythonguis.com/static/faq/forum/qdatawidgetmapper-with-relational-model-and-qcomboxes-working-of-relations/tciSyNbv2hC0HtkEMMCbkrbtf6E.png)
Code to test
python ```
import os
import sys
from pathlib import Path
from PyQt5 import QtGui, uic, QtCore, QtWidgets
from PyQt5.QtCore import QSize, Qt, QStandardPaths
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlRelation, QSqlRelationalDelegate, \
  QSqlQuery
from PyQt5.QtWidgets import (
  QApplication,
  QComboBox,
  QDataWidgetMapper,
  QDoubleSpinBox,
  QFormLayout,
  QHBoxLayout,
  QLabel,
  QLineEdit,
  QMainWindow,
  QPushButton,
  QSpinBox,
  QTableView,
  QVBoxLayout,
  QWidget, QTextEdit, QFileDialog,
)
from qtwidgets import PasswordEdit
# settings = QtCore.QSettings('WizardAssistant', 'WizardAssistantDesktop')
# config_data_dir = Path("WizardAssistant/WizardAssistantDesktop")
#
# # Define where sshconfig_db location is
# sshconfig_db = QStandardPaths.writableLocation(
#   QStandardPaths.AppConfigLocation) / config_data_dir / "wizardwebsshv2.db"
# Define App internal SSH config DB
sshdb = QSqlDatabase.addDatabase("QSQLITE", "SSHCONFIG")
# sshdb.setDatabaseName(os.fspath(sshconfig_db))
sshdb.setDatabaseName('wizardwebsshv2.db')
# ssh_target_db = str(sshconfig_db)
sshdb.open()
def create_sshconfig_db(database_name):
  #connection = create_db_connection(database_name)
  database_name.open()
  print(f'Trying to create SSH config tables in {str(database_name)}')
  query = QSqlQuery(db=database_name)
  query.exec(
    'CREATE TABLE IF NOT EXISTS sshgroup (id INTEGER PRIMARY KEY, ssh_group_name text(25) NOT NULL UNIQUE, ssh_group_description TEXT)')
  query.exec(
    'CREATE TABLE IF NOT EXISTS sshkeys (id INTEGER PRIMARY KEY, sshkey_name varchar(25) NOT NULL UNIQUE, sshkey_passphrase TEXT, sshkey_public blob, sshkey_private blob, sshkey_public_file TEXT, sshkey_private_file TEXT)')
  query.exec(
    'CREATE TABLE IF NOT EXISTS sshconfig (id INTEGER PRIMARY KEY, ssh_config_name text(25) NOT NULL UNIQUE, ssh_config_content TEXT)')
  query.exec(
    'CREATE TABLE IF NOT EXISTS sshconnections (id integer NOT NULL PRIMARY KEY, ssh_group_id INTEGER DEFAULT 1, ssh_connection_name varchar(100) NOT NULL UNIQUE, ssh_username varchar(100), ssh_password varchar(100), Host varchar(100), HostName varchar(100), Port integer, ProxyCommand TEXT, ssh_key_id INTEGER DEFAULT 1, ssh_config_id INTEGER DEFAULT 1, FOREIGN KEY(ssh_group_id) REFERENCES sshgroup(id), FOREIGN KEY(ssh_key_id) REFERENCES sshkeys(id), FOREIGN KEY(ssh_config_id) REFERENCES sshconfig(id))')
  print(f'Finished creating SSH config tables in {str(database_name)}')
  try:
    print(f'Trying to insert default sshconfig and sshgroup defaults in {str(database_name)}')
    query.exec("INSERT INTO sshkeys (sshkey_name,sshkey_passphrase,sshkey_public,sshkey_private,sshkey_public_file,sshkey_private_file) VALUES ('None', '', '', '', '', '')")
    query.exec("INSERT INTO sshconfig (ssh_config_name, ssh_config_content) VALUES ('default', '')")
    query.exec("INSERT INTO sshgroup (ssh_group_name, ssh_group_description) VALUES ('default', 'Default SSH Group')")
    query.exec("INSERT INTO sshconnections (ssh_group_id, ssh_connection_name, ssh_username, ssh_password, Host, HostName, Port, ProxyCommand, ssh_key_id, ssh_config_id) VALUES ('1', 'default_connection', 'username', 'password', 'test', 'test.example.com', '22', '', '1', '1')")
    # query.exec("")
  except:
    print('Error inserting default sshconfig and sshgroup defaults')
create_sshconfig_db(sshdb)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    layout = QVBoxLayout()
    form = QFormLayout()
    self.sshdb = sshdb
    self.sshdb.database('SSHCONFIG', open=True)
    # Set default home
    home_dir = str(Path.home())
    self.ssh_id = QSpinBox()
    self.ssh_id.setDisabled(True)
    self.ssh_group = QComboBox()
    # self.ssh_group.setDisabled(True)
    self.ssh_connection_name = QLineEdit()
    self.ssh_username = QLineEdit()
    self.ssh_password = PasswordEdit()
    self.ssh_key_passphrase = PasswordEdit()
    self.ssh_host = QLineEdit()
    self.ssh_hostname = QLineEdit()
    self.ssh_port = QSpinBox()
    self.ssh_port.setRange(1, 65535)
    self.ssh_port.setSingleStep(1)
    self.ssh_proxy_command = QLineEdit()
    self.ssh_key_name = QComboBox()
    self.ssh_config_name = QComboBox()
    # self.ssh_private_key_file = QLineEdit() # if bool(self.ssh_private_key_file): then QFileDialog.getOpenFileName(self, caption="Open Image", directory=home_dir, filter="SSh Private Key Files (id_*)")
    # self.ssh_public_key_file = QLineEdit() # QFileDialog.getOpenFileName(self, caption="Open Image", directory=home_dir, filter="SSh Public Key Files (id_*.pub)")
    form.addRow(QLabel("ID"), self.ssh_id)
    form.addRow(QLabel("Group"), self.ssh_group)
    form.addRow(QLabel("ConnectionName"), self.ssh_connection_name)
    form.addRow(QLabel("SSH Username"), self.ssh_username)
    form.addRow(QLabel("SSH Password"), self.ssh_password)
    form.addRow(QLabel("Host"), self.ssh_host)
    form.addRow(QLabel("HostName"), self.ssh_hostname)
    form.addRow(QLabel("Port"), self.ssh_port)
    form.addRow(QLabel("ProxyCommand"), self.ssh_proxy_command)
    form.addRow(QLabel("SSH Key Name"), self.ssh_key_name)
    form.addRow(QLabel("SSH Config Name"), self.ssh_config_name)
    self.model = QSqlRelationalTableModel(db=self.sshdb)
    self.ssh_group.setModel(self.model)
    ssh_group_index = self.model.fieldIndex("ssh_group_name")
    self.ssh_key_name.setModel(self.model)
    ssh_key_name_index = self.model.fieldIndex("sshkey_name")
    self.ssh_config_name.setModel(self.model)
    ssh_config_name_index = self.model.fieldIndex("ssh_config_name")
    self.model.setRelation(ssh_group_index, QSqlRelation("sshgroup", "id", "ssh_group_name"))
    self.model.setRelation(ssh_key_name_index, QSqlRelation("sshkeys", "id", "sshkey_name"))
    self.model.setRelation(ssh_config_name_index, QSqlRelation("sshconfig", "id", "ssh_config_name"))
    self.ssh_group.setModelColumn(self.model.fieldIndex("ssh_group_name"))
    self.ssh_key_name.setModelColumn(self.model.fieldIndex("sshkey_name"))
    self.ssh_config_name.setModelColumn(self.model.fieldIndex("ssh_config_name"))
    self.mapper = QDataWidgetMapper()
    self.mapper.setModel(self.model)
    self.mapper.addMapping(self.ssh_id, 0)
    self.mapper.addMapping(self.ssh_group, ssh_group_index)
    self.mapper.addMapping(self.ssh_connection_name, 2)
    self.mapper.addMapping(self.ssh_username, 3)
    self.mapper.addMapping(self.ssh_password, 4)
    self.mapper.addMapping(self.ssh_host, 5)
    self.mapper.addMapping(self.ssh_hostname, 6)
    self.mapper.addMapping(self.ssh_port, 7)
    self.mapper.addMapping(self.ssh_proxy_command, 8)
    self.mapper.addMapping(self.ssh_key_name, ssh_key_name_index)
    self.mapper.addMapping(self.ssh_config_name, ssh_config_name_index)
    # self.delegate = QSqlRelationalDelegate()
    self.mapper.setItemDelegate(QSqlRelationalDelegate(self))
    self.model.setTable("sshconnections")
    self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    self.model.select()
    self.mapper.toFirst()
    self.setMinimumSize(QSize(400, 400))
    controls = QHBoxLayout()
    # tag::controls[]
    prev_rec = QPushButton("Previous")
    prev_rec.clicked.connect(self.mapper.toPrevious)
    next_rec = QPushButton("Next")
    next_rec.clicked.connect(self.mapper.toNext)
    save_rec = QPushButton("Save Changes")
    save_rec.clicked.connect(self.mapper.submit)
    add_rec = QPushButton("Add")
    add_rec.clicked.connect(self.add_sshconnection)
    remove_rec = QPushButton("Remove")
    remove_rec.clicked.connect(self.mapper.submit)
    # end::controls[]
    controls.addWidget(prev_rec)
    controls.addWidget(next_rec)
    controls.addWidget(save_rec)
    controls.addWidget(add_rec)
    controls.addWidget(remove_rec)
    layout.addLayout(form)
    layout.addLayout(controls)
    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)
  def add_sshconnection(self):
    self.model.insertRows(self.model.rowCount(), 1)
    self.model.submit()
    self.mapper.toLast()

# row = self.mapper.currentIndex()
# self.mapper.submit()
# self.model.insertRow(row)
# self.mapper.setCurrentIndex(row)
def show_dialog(self):
  home_dir = str(Path.home())
  fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
  if fname[0]:
    f = open(fname[0], 'r')
    with f:
      data = f.read()
      self.textEdit.setText(data)

def select_file(self):
  if self.fname is not None and os.path.isfile(self.fname):
    eeg_cap_dir = os.path.dirname(self.fname)
  else:
    eeg_cap_dir = QtCore.QDir.currentPath()
  dialog = QtWidgets.QFileDialog(self)
  dialog.setWindowTitle('Open EEG Position file')
  dialog.setNameFilter('(*.csv)')
  dialog.setDirectory(eeg_cap_dir)
  dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
  filename = None
  if dialog.exec_() == QtWidgets.QDialog.Accepted:
    filename = dialog.selectedFiles()
  if filename:
    self.fname = str(filename[0])
    self.group_box.lineEdit.setText(self.fname)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

I also found this link but its kinda hard to follow as full code snippet is not readable. https://www.pythonstudio.us/pyqt-programming/using-database-form-views.html 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**QDataWidgetMapper with relational model and qcomboxes working of relations** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/qdatawidgetmapper-with-relational-model-and-qcomboxes-working-of-relations/Python books) on the subject. 
**QDataWidgetMapper with relational model and qcomboxes working of relations** was published in [faq](https://www.pythonguis.com/faq/) on June 06, 2021 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
