# Content from: https://www.pythonguis.com/faq/postgres-pyqt5-windows-driver-not-loaded/

[](https://www.pythonguis.com/faq/postgres-pyqt5-windows-driver-not-loaded/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
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
  * [PyQt5](https://www.pythonguis.com/pyqt5/)
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Using Postgres with Qt & Python on Windows, fixing QPSQL driver not loaded
Setting PATH to use the Postgres library
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Mar 30 [ FAQ ](https://www.pythonguis.com/faq/)
If you're trying to use Postgres with PyQt5/6 or PySide2/PySide6 you may have come across an issue with loading the driver. Qt (correctly) lists the driver as available in Qt, but when trying to load it the load will fail. This is because the Qt library depends on Postgres' own library, which must be available in the path to load.
The following script will let you test if the Postgres library is loading correctly.
  * PyQt5
  * PyQt6
  * PySide2
  * PySide6


python ```
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication
app = QApplication([])
db = QSqlDatabase("QPSQL")
print("Available drivers", db.drivers())
if not db.open():
  print("Unable to connect.")
  print('Last error', db.lastError().text())
else:
  print("Connection to the database successful")

```

python ```
from PyQt6.QtSql import QSqlDatabase
from PyQt6.QtWidgets import QApplication
app = QApplication([])
db = QSqlDatabase("QPSQL")
print("Available drivers", db.drivers())
if not db.open():
  print("Unable to connect.")
  print('Last error', db.lastError().text())
else:
  print("Connection to the database successful")

```

python ```
from PySide2.QtSql import QSqlDatabase
from PySide2.QtWidgets import QApplication
app = QApplication([])
db = QSqlDatabase("QPSQL")
print("Available drivers", db.drivers())
if not db.open():
  print("Unable to connect.")
  print('Last error', db.lastError().text())
else:
  print("Connection to the database successful")

```

python ```
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QApplication
app = QApplication([])
db = QSqlDatabase("QPSQL")
print("Available drivers", db.drivers())
if not db.open():
  print("Unable to connect.")
  print('Last error', db.lastError().text())
else:
  print("Connection to the database successful")

```

Executing the above script in a new command prompt will give the following output (if Postgres is not accessible).
command ```
>python test.py
QSqlDatabase: QPSQL driver not loaded
QSqlDatabase: available drivers: QSQLITE QODBC QODBC3 QPSQL QPSQL7
Available drivers ['QSQLITE', 'QODBC', 'QODBC3', 'QPSQL', 'QPSQL7']
Unable to connect.
Last error Driver not loaded Driver not loaded

```

The list of "available drivers" shows the _Qt drivers_ which are available in your PyQt5 (or PyQt6, or PySide2, or PySide6) installation. For example, in my installation the driver files are under `site-packages\PyQt5\Qt5\plugins\sqldrivers`
command ```
C:\Users\Martin\AppData\Local\Programs\Python\Python37\Lib\site-packages\PyQt5\Qt5\plugins\sqldrivers> dir
 Volume in drive C has no label.
 Volume Serial Number is 0A6A-65ED
 Directory of C:\Users\Martin\AppData\Local\Programs\Python\Python37\Lib\site-packages\PyQt5\Qt5\plugins\sqldrivers
02/12/2021 14:35  <DIR>     .
02/12/2021 14:35  <DIR>     ..
02/12/2021 14:35     1,412,080 qsqlite.dll
02/12/2021 14:35      98,288 qsqlodbc.dll
02/12/2021 14:35      79,856 qsqlpsql.dll
        3 File(s)   1,590,224 bytes
        2 Dir(s) 174,429,970,432 bytes free

```

The _Driver not loaded_ error is occurring because the Qt Postgres driver cannot find the Postgres libraries. The Qt Postgres driver is a wrapper around these libraries, rather than a complete implementation of Postgres itself.
To get this working you need to ensure the required Postgres library files are available in your path. You can do this by adding your Postgres installation `bin` folder to your path. For example, on my computer Postgres is installed under `C:\Program Files\PostgreSQL\14\` (I'm using version 14). We need to add to the Postgres `bin` folder to the `PATH` as this contains `libpq.dll` (Postgres Access Library) which Qt needs.
command ```
SET PATH=%PATH%;C:\Program Files\PostgreSQL\14\bin

```

With that in place, running the script again will show that that driver has loaded successfully. The connection still isn't working, since it needs the username and password set. But if you get _this_ far you know the driver is working properly.
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
command ```
U:\home\martin\www\pythonguis\content\faq\qt-postgres-driver>python test.py
Available drivers ['QSQLITE', 'QODBC', 'QODBC3', 'QPSQL', 'QPSQL7']
Unable to connect.
Last error connection to server at "localhost" (::1), port 5432 failed: fe_sendauth: no password supplied
QPSQL: Unable to connect

```

We can modify the test script to add your username and password to complete the connection. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
  * PyQt5
  * PyQt6
  * PySide2
  * PySide6


python ```
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication
app = QApplication([])
db = QSqlDatabase("QPSQL")
db.setUserName("postgres") # postgres is the default root username
db.setPassword("")  # add your password here
print("Available drivers", db.drivers())
if not db.open():
  print("Unable to connect.")
  print('Last error', db.lastError().text())
else:
  print("Connection to the database successful")

```

python ```
from PyQt6.QtSql import QSqlDatabase
from PyQt6.QtWidgets import QApplication
app = QApplication([])
db = QSqlDatabase("QPSQL")
db.setUserName("postgres") # postgres is the default root username
db.setPassword("")  # add your password here
print("Available drivers", db.drivers())
if not db.open():
  print("Unable to connect.")
  print('Last error', db.lastError().text())
else:
  print("Connection to the database successful")

```

python ```
from PySide2.QtSql import QSqlDatabase
from PySide2.QtWidgets import QApplication
app = QApplication([])
db = QSqlDatabase("QPSQL")
db.setUserName("postgres") # postgres is the default root username
db.setPassword("")  # add your password here
print("Available drivers", db.drivers())
if not db.open():
  print("Unable to connect.")
  print('Last error', db.lastError().text())
else:
  print("Connection to the database successful")

```

python ```
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import QApplication
app = QApplication([])
db = QSqlDatabase("QPSQL")
db.setUserName("postgres") # postgres is the default root username
db.setPassword("")  # add your password here
print("Available drivers", db.drivers())
if not db.open():
  print("Unable to connect.")
  print('Last error', db.lastError().text())
else:
  print("Connection to the database successful")

```

...and then the connection will complete as expected. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
command ```
>python test-userpass.py
Available drivers ['QSQLITE', 'QODBC', 'QODBC3', 'QPSQL', 'QPSQL7']
Connection to the database successful

```

Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Using Postgres with Qt & Python on Windows, fixing QPSQL driver not loaded** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/postgres-pyqt5-windows-driver-not-loaded/Python books) on the subject. 
**Using Postgres with Qt & Python on Windows, fixing QPSQL driver not loaded** was published in [faq](https://www.pythonguis.com/faq/) on January 29, 2022 (updated March 30, 2022) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[postgres](https://www.pythonguis.com/topics/postgres/) [sql](https://www.pythonguis.com/topics/sql/) [database](https://www.pythonguis.com/topics/database/) [qsqldatabase](https://www.pythonguis.com/topics/qsqldatabase/) [qtsql](https://www.pythonguis.com/topics/qtsql/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [ databases](https://www.pythonguis.com/topics/databases/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
