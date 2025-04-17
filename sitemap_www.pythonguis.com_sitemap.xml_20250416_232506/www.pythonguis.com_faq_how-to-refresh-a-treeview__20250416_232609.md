# Content from: https://www.pythonguis.com/faq/how-to-refresh-a-treeview/

[](https://www.pythonguis.com/faq/how-to-refresh-a-treeview/#menu)
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
# How to refresh a treeview?
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
Cody_Jackson | 2021-06-08 14:01:48 UTC | #1
I have a File Explorer panel (based on a tutorial) that uses a QTreeView and QFileSystemModel to show the contents of a directory. I want to update the view of the directory contents if the user changes the directory.
In other words, the current window looks at a default location. Users are able to change a config file to change the directory the window shows. However, they have to close the GUI and reopen to see the contents of the new directory.
I have spent about a day and a half looking at the documentation, Stack Overflow, and other locations to find some means to refresh the window, but I haven't found anything. It seems like this would be a built-in behaviour for QTreeView but I can't find it; maybe I'm looking for the wrong term. 
My code is below:
python ```
class ProjectExplorerTree(QTreeView):
  """Handles all functionality for the Project Explorer panel.
  Creates context menu for Build, Clean, Register, and Delete OpenCPI assets.
  Provides access to selected assets for use in other methods, such as Set/UnSet
  """
  def __init__(self, main_window, tree: QTreeView, console, rcc, hdl) -> None:
    """Creates the ListView/FileSystemModel for viewing"""
    super().__init__()
    self.treeView = tree
    self.default_dir = main_window.ocpi_path
    self.proj_path = main_window.user_proj_path
    self.console: OutputConsole = console
    self.rcc_target: RccTargets = rcc
    self.hdl_target: HdlTargets = hdl
    self.fileSystemModel = QFileSystemModel(self.treeView)
    self.fileSystemModel.setReadOnly(False)
    root: Optional[QModelIndex] = self.fileSystemModel.setRootPath(f"{self.proj_path}")
    self.treeView.setModel(self.fileSystemModel)
    self.treeView.hideColumn(1)
    self.treeView.hideColumn(2)
    self.treeView.hideColumn(3)
    self.treeView.setRootIndex(root)
    self.treeView.setSelectionMode(self.treeView.ExtendedSelection)
    self.treeView.setRootIsDecorated(True)
    self.treeView.setAlternatingRowColors(True)
    self.treeView.setDragEnabled(True) # Allow items to be dragged from this panel
    self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
    self.treeView.customContextMenuRequested.connect(self.context_menu)

```

I have tried using QFileSystemModel.rootPathChanged(), which didn't seem to work. I also tried using QFileSystemWatcher, which didn't do what I wanted (and it seems to already be incorporated into QFileSystemModel). I even tried using QDir.refresh(), which did nothing.
What am I missing to simply refresh the window when the config file is updated?
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
Cody_Jackson | 2021-06-08 16:59:37 UTC | #2
I don't know if this is the most correct way, but I was able to do it (manually, at least) by creating a Refresh context menu that implemented the following code:
python ```
def refresh_view(self):
  new_path = self.fileSystemModel.setRootPath(str(window.user_proj_path))
  self.treeView.setRootIndex(new_path)

```

Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**How to refresh a treeview?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/how-to-refresh-a-treeview/Python books) on the subject. 
**How to refresh a treeview?** was published in [faq](https://www.pythonguis.com/faq/) on June 08, 2021 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
