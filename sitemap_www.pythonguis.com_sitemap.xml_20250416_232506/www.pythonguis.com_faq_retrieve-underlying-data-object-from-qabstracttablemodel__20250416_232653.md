# Content from: https://www.pythonguis.com/faq/retrieve-underlying-data-object-from-qabstracttablemodel/

[](https://www.pythonguis.com/faq/retrieve-underlying-data-object-from-qabstracttablemodel/#menu)
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
# Retrieve underlying data object from QAbstractTableModel
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ FAQ ](https://www.pythonguis.com/faq/)
Paul_B_Hermans | 2020-11-12 03:09:01 UTC | #1
I am struggling with pyqt5 and hoping someone can guide me a bit. I have a class called Student. I want to display a few QTableView (read only) with only 3 columns that shows first_name, last_name and section.
Then, when the user selects 1 or more rows in the tableview and presses a button, I want to get the Student object that was used to create that row, and then use some of its other properties to do stuff.
My problem is that I can't figure out how to get back to the actual Student object that was used to build the table. Here is some snippets of code I have.....hoping someone can clue me in.
python ```
class Student:
  def __init__(self, section, last_name, first_name, email, sn_folder):
    self.section = section
    self.last_name = last_name
    self.first_name = first_name
    self.email = email
    self.SN_Folder = sn_folder
  def __str__(self):
    return self.full_name()
  def __repr__(self):
    return self.__str__()
  def full_name(self):
    return self.last_name + ", " + self.first_name

class StudentTableModel(QtCore.QAbstractTableModel):
  # students is a list of Student objects.
  def __init__(self, students=None, parent=None):
    super().__init__(parent)
    if students is None:
      self.students = []
    else:
      self.students = students
  def rowCount(self, index=QtCore.QModelIndex()):
    """ Returns the number of rows the model holds. """
    return len(self.students)
  def columnCount(self, index=QtCore.QModelIndex()):
    """ Returns the number of columns the model holds. """
    return 5
  def data(self, index, role=QtCore.Qt.DisplayRole):
    """ Depending on the index and role given, return data. If not
      returning data, return None (PySide equivalent of QT's
      "invalid QVariant").
    """
    if not index.isValid():
      return None
    if not 0 <= index.row() < len(self.students):
      return None
    if role == QtCore.Qt.DisplayRole:
      last_name = self.students[index.row()].last_name
      first_name = self.students[index.row()].first_name
      section = self.students[index.row()].section
      email = self.students[index.row()].email
      sn_folder = self.students[index.row()].SN_Folder
      if index.column() == 0:
        return last_name
      elif index.column() == 1:
        return first_name
      elif index.column() == 2:
        return section
      elif index.column() == 3:
        return email
      elif index.column() == 4:
        return sn_folder
    return None

```

then in my mainwindow I have a method for the button being clicked:
python ```
  def go_clicked(self):
    # Get a list of Student Objects ( was used to build the table)
    students = self.selected_course().students
    # Get selected row indices from the tableview
    row_indexes=[]
    for row in self.tblStudents2.selectionModel().selectedRows():
      row_indexes.append(row.row())
    # Attempt to retrieve the actual Student Object that corresponds to the row in the table
    # - this is wrong but it illustrates the idea. It works if I don't allow table to be sorted.
    for index in row_indexes:
      student = students[index]
      print(student)

```

Thanks in advance for any help you can provide!
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Retrieve underlying data object from QAbstractTableModel** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/retrieve-underlying-data-object-from-qabstracttablemodel/Python books) on the subject. 
**Retrieve underlying data object from QAbstractTableModel** was published in [faq](https://www.pythonguis.com/faq/) on November 11, 2020 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [pyside](https://www.pythonguis.com/topics/pyside/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
