# Content from: https://www.pythonguis.com/examples/python-notepad-clone/

[](https://www.pythonguis.com/examples/python-notepad-clone/#menu)
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
# No2Pads, a simple Notepad clone
The QTextEdit widget does 90% of the work
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ Example applications ](https://www.pythonguis.com/examples/)
[ No2Pads Source Code ](https://www.pythonguis.com/d/notepad.zip)
Notepad doesn't need much introduction. It's a plaintext editor that's been part of Windows since the beginning, and similar applications exist in every GUI desktop ever created.
Here we reimplement Notepad in Python using PyQt, a task that is made particularly easy by Qt providing a text editor widget. A few signal-hookups is all that is needed to implement a fully working app.
## The Editor
The full source code for _No2Pads_ is available in the [15 minute apps](https://github.com/mfitzp/15-minute-apps/tree/master/notepad) repository. You can download/clone to get a working copy, then install requirements using:
python ```
pip3 install -r requirements.txt

```

You can then run _No2Pads_ with:
python ```
python3 notepad.py

```

Read on for a walkthrough of how the code works.
## Editor
Qt provides a complete plain text editor component widget in the form of `QPlainTextEdit`. This widget displays an editing area in which you can type, click around and select text.
To add the widget to our window, we just create it as normal and then set it in the central widget position for the window. We don't need a layout, since we won't be adding any other widgets.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
We also setup the editor to use the system fixed width font `QFontDatabase.FixedFont` at pointsize 12.
python ```
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import os
import sys

class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.editor = QPlainTextEdit() # Could also use a QTextEdit and set self.editor.setAcceptRichText(False)
    self.setCentralWidget(self.editor)
    # Setup the QTextEdit editor configuration
    fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
    fixedfont.setPointSize(12)
    self.editor.setFont(fixedfont)
    # self.path holds the path of the currently open file.
    # If none, we haven't got a file open yet (or creating new).
    self.path = None

```

## Edit commands
To be useful an editor needs to be able to perform a lot of standard operations — copy, paste, cut, insert, clear. Implementing all these operations on the text buffer directly would take some work. However, the `QPlainTextEdit` widget actually provides support for all of this through Qt slots.
Triggering any of these operations is simply a case of calling one the slot at the appropriate time. Below we add a set of toolbar buttons for editing, each defined as a `QAction`. Connecting the `.triggered` signal from the `QAction` to the relevant slot enables the behaviour.
python ```
cut_action = QAction(QIcon(os.path.join('images', 'scissors.png')), "Cut", self)
    cut_action.setStatusTip("Cut selected text")
    cut_action.triggered.connect(self.editor.cut)
    edit_toolbar.addAction(cut_action)
    edit_menu.addAction(cut_action)
    copy_action = QAction(QIcon(os.path.join('images', 'document-copy.png')), "Copy", self)
    copy_action.setStatusTip("Copy selected text")
    copy_action.triggered.connect(self.editor.copy)
    edit_toolbar.addAction(copy_action)
    edit_menu.addAction(copy_action)
    paste_action = QAction(QIcon(os.path.join('images', 'clipboard-paste-document-text.png')), "Paste", self)
    paste_action.setStatusTip("Paste from clipboard")
    paste_action.triggered.connect(self.editor.paste)
    edit_toolbar.addAction(paste_action)
    edit_menu.addAction(paste_action)
    select_action = QAction(QIcon(os.path.join('images', 'selection-input.png')), "Select all", self)
    select_action.setStatusTip("Select all text")
    select_action.triggered.connect(self.editor.selectAll)
    edit_menu.addAction(select_action)

```

The complete list of slots available on a `QPlainTextEdit` are —
Slot | Operation  
---|---  
`.clear()` | Clear selected text  
`.cut()` | Cut selected text to clipboard  
`.copy()` | Copy selected text to clipboard  
`.paste()` | Paste clipboard at cursor  
`.undo()` | Undo last action  
`.redo()` | Redo last undo'd action  
`.insertPlainText(text)` | Insert plain text at cursor  
`.selectAll()` | Select all text in document  
There are also a set of signals available, such as `.copyAvailable` to update the UI when these operations are possible. You can use these to enable and disable buttons when they can't be used.
## File operations
To complete a working text editor we need to be able to open and save files we're working on. There are no built-in handlers for doing this, but we can construct a simple slots ourselves, and trigger then using menubar actions as before.
First we define `file_open` method, which when run uses `QFileDialog.getOpenFileName` to display a platform file open dialog. The selected path is then used to open the file (using Python file context).
If that completes without throwing any errors, we set the contents to the text editor widget. Finally, we store the file path (so Save writes to the correct place) and update the window title. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
python ```
def file_open(self):
    path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")
    if path:
      try:
        with open(path, 'rU') as f:
          text = f.read()
      except Exception as e:
        self.dialog_critical(str(e))
      else:
        self.path = path
        self.editor.setPlainText(text)
        self.update_title()

```

There are two blocks for saving files — `save` and `save_as` — the former for saving an open file, which already has a filename, the latter for saving a new file.
The `save` block checks whether we have a known path, stored in `self.path`. If not, it calls `save_as` itself to show a dialog to get a path. Opting to "Save As" will follow this same path.
In either case, the save itself is handled by `_save_to_path()` which accepts a target path. It gets the current plain text content of the editor, and then opening a file, writes it to disk.
Errors are displayed using a dialog box callback. If we saved successfully we store the path for future _Save_ calls and update the window title.
python ```
def file_save(self):
    if self.path is None:
      # If we do not have a path, we need to use Save As.
      return self.file_saveas()
    self._save_to_path(self.path)
  def file_saveas(self):
    path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt);All files (*.*)")
    if not path:
      # If dialog is cancelled, will return ''
      return
    self._save_to_path(self.path)
  def _save_to_path(self, path):
    text = self.editor.toPlainText()
    try:
      with open(path, 'w') as f:
        f.write(text)
    except Exception as e:
      self.dialog_critical(str(e))
    else:
      self.path = path
      self.update_title()

```

Printing is fairly straightforward to set up for the `QPlainTextEdit` class. First we show a dialog box to allow the user to select the printer and options. If they click OK on this dialog, it exits with a `True` state and the selected printer is available via `dlg.printer()`. Pass this to the editor's `print_()` method to trigger the print.
python ```
def file_print(self):
    dlg = QPrintDialog()
    if dlg.exec_():
      self.editor.print_(dlg.printer())

```

The final step is to hook these all up to `QAction.triggered` signals in our menubar.
python ```
file_toolbar = QToolBar("File")
    file_toolbar.setIconSize(QSize(14, 14))
    self.addToolBar(file_toolbar)
    file_menu = self.menuBar().addMenu("&File")
    open_file_action = QAction(QIcon(os.path.join('images', 'blue-folder-open-document.png')), "Open file...", self)
    open_file_action.setStatusTip("Open file")
    open_file_action.triggered.connect(self.file_open)
    file_menu.addAction(open_file_action)
    file_toolbar.addAction(open_file_action)
    save_file_action = QAction(QIcon(os.path.join('images', 'disk.png')), "Save", self)
    save_file_action.setStatusTip("Save current page")
    save_file_action.triggered.connect(self.file_save)
    file_menu.addAction(save_file_action)
    file_toolbar.addAction(save_file_action)
    saveas_file_action = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Save As...", self)
    saveas_file_action.setStatusTip("Save current page to specified file")
    saveas_file_action.triggered.connect(self.file_saveas)
    file_menu.addAction(saveas_file_action)
    file_toolbar.addAction(saveas_file_action)
    print_action = QAction(QIcon(os.path.join('images', 'printer.png')), "Print...", self)
    print_action.setStatusTip("Print current page")
    print_action.triggered.connect(self.file_print)
    file_menu.addAction(print_action)
    file_toolbar.addAction(print_action)

```

## Future ideas
That's a basic functional text editor implemented. You could extend the No2Pads to support —
  1. Implement _clear_ and _clear all_ from the edit slots
  2. Add support for configurable display colours, styles, etc. Take a look at the Qt styles framework.
  3. Add support for syntax or Markdown formatting.


For an example of a Rich Text Editor, check out Megasolid Idiom, a Rich Text Editor
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**No2Pads, a simple Notepad clone** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/examples/python-notepad-clone/Python books) on the subject. 
**No2Pads, a simple Notepad clone** was published in [examples](https://www.pythonguis.com/examples/) on April 15, 2017 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [qt5](https://www.pythonguis.com/topics/qt5/) [text](https://www.pythonguis.com/topics/text/) [textedit](https://www.pythonguis.com/topics/textedit/) [notepad](https://www.pythonguis.com/topics/notepad/) [editor](https://www.pythonguis.com/topics/editor/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/)
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
