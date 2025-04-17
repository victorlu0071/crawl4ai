# Content from: https://www.pythonguis.com/examples/python-rich-text-editor/

[](https://www.pythonguis.com/examples/python-rich-text-editor/#menu)
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
# Megasolid Idiom, a Rich Text Editor
Simple WYSIWYG editor in Python
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Mar 10 PyQt5 [ Example applications ](https://www.pythonguis.com/examples/)
[ Megasolid Idiom Source Code ](https://www.pythonguis.com/d/wordprocessor.zip)
Megasolid Idiom is a _rich text_ word processor implemented in Python and Qt. You can use it to open, edit and save HTML-formatted files, with a WYSIWYG (what you see is what you get) format view. Only basic formatting, headings, lists and images are supported.
Megasolid Idiom is based on the same code used for the No2Pads notepad app, so take a look at that if you want an even simpler example.
## Editor component
Megasolid Idiom uses the Qt built-in `QTextEdit` component for our rich text editor, which means that Qt handles a lot of the complicated faff of text editing. Support for rich text (rather than plain text) is enabled by default, or by setting `.setAcceptRichText(True)` on the editor.
## Editor subclass
To support drag-drop insert of images into the active document, we subclass `QTextEdit` to add custom Qt mime handlers.
python ```
class TextEdit(QTextEdit):
  def canInsertFromMimeData(self, source):
    if source.hasImage():
      return True
    else:
      return super().canInsertFromMimeData(source)
  def insertFromMimeData(self, source):
    cursor = self.textCursor()
    document = self.document()
    if source.hasUrls():
      for u in source.urls():
        file_ext = splitext(str(u.toLocalFile()))
        if u.isLocalFile() and file_ext in IMAGE_EXTENSIONS:
          image = QImage(u.toLocalFile())
          document.addResource(QTextDocument.ImageResource, u, image)
          cursor.insertImage(u.toLocalFile())
        else:
          # If we hit a non-image or non-local URL break the loop and fall out
          # to the super call & let Qt handle it
          break
      else:
        # If all were valid images, finish here.
        return

    elif source.hasImage():
      image = source.imageData()
      uuid = hexuuid()
      document.addResource(QTextDocument.ImageResource, uuid, image)
      cursor.insertImage(uuid)
      return
    super(TextEdit, self).insertFromMimeData(source)

```

The two handlers `canInsertFromMimeData` and `insertFromMimeData` are Qt's methods for accepting mime data (e.g. images, or other objects) dropped onto your editor. The both receive a signal parameter `source` which receives a [QMimeData](http://doc.qt.io/qt-5/qmimedata.html) object. Similar mechanisms are used for other widget types.
  * `canInsertFromMimeData` is a _check_ which confirms whether a particular _type_ can be accepted by the widget. This method should return `True` if you can accept the data being provided. If this method returns `True` the window manager will usually show an accept-drop indicator, e.g. an icon with a plus-sign or a drop animation. If you return `False` a cannot-drop indicator will be shown.
  * `insertFromMimeData` handles the actual adding of the mime content to the document. Here we handle two cases, one where we are adding from an image directly (try dragging an image from a browser window) and one where drop an URL/file (try dragging a file into the window).


You can use these methods to support other types, e.g. drag-dropping text into your window. You need to add the new type to both the `canInsertFromMimeData` and `insertFromMimeData` handlers.
## Editor config
The `QTextEdit` component (which we've subclassed as `TextEdit`) has some additional setup requirements. We switch on rich text mode for the editor component and enable auto-formatting (currently only bullet lists from `*`). The default font is set to _Times New Roman_ 12pt. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
python ```
class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    layout = QVBoxLayout()
    self.editor = TextEdit()
    # Setup the QTextEdit editor configuration
    self.editor.setAutoFormatting(QTextEdit.AutoAll)
    self.editor.selectionChanged.connect(self.update_format)
    # Initialize default font size.
    font = QFont('Times', 12)
    self.editor.setFont(font)
    # We need to repeat the size to init the current format.
    self.editor.setFontPointSize(12)

```

We need our toolbar to update automatically when clicking/selecting text within the editor. By connecting our custom slot (`update_format`) to the `.selectionChanged` signal from the editor, we receive a signal every time the current selection changes.
## Editor toolbars and actions
The editor toolbar is setup using a `QToolBar` to which we add a number of widgets.
### Fonts
The font dropdown is set up using `QFontComboBox` a Qt builtin which shows the fonts available on the host system, with each font listed by name with a demo of the font.
The `.currentFontChanged` signal is emitted by the combobox whenever the font is changed, passing the selected font as a parameter. By connecting this to the `.setCurrentFont` slot on our editor, we can use the dropdown to update the editors' font.
Font size is handled with a standard `QCombobox` which we pre-fill with a default list from the constant `FONT_SIZES`. The `.currentIndexChanged[str]` signal emits the current value of the combobox when it is updated. This is passed to the editor `.setFontPointSize` [using a lambda to wrap the call](https://www.pythonguis.com/tutorials/qt-transmit-extra-data-with-signals) so we can convert it to a `float` first.
### Styles
Style handling uses checkable (toggleable) `QAction` widgets. We add a key sequence for each widget to provide standard keyboard shortcuts (e.g. `QKeySequence.Bold`). Each `.toggled` signal is connected to an editor slot to trigger updates.
There is no `.setFontBold` handler, instead we must use `.setFontWeight` to set the weight specifically. Qt provides a set of default weights in the `Qt` namespace. The `Bold` handler wraps the call to `.setFontWeight`, setting it to `QFont.Bold` if enabled, or `QFont.Normal` if not.
python ```
self.bold_action = QAction(QIcon(os.path.join('images', 'edit-bold.png')), "Bold", self)
    self.bold_action.setStatusTip("Bold")
    self.bold_action.setShortcut(QKeySequence.Bold)
    self.bold_action.setCheckable(True)
    self.bold_action.toggled.connect(lambda x: self.editor.setFontWeight(QFont.Bold if x else QFont.Normal))
    format_toolbar.addAction(self.bold_action)
    format_menu.addAction(self.bold_action)
    self.italic_action = QAction(QIcon(os.path.join('images', 'edit-italic.png')), "Italic", self)
    self.italic_action.setStatusTip("Italic")
    self.italic_action.setShortcut(QKeySequence.Italic)
    self.italic_action.setCheckable(True)
    self.italic_action.toggled.connect(self.editor.setFontItalic)
    format_toolbar.addAction(self.italic_action)
    format_menu.addAction(self.italic_action)
    self.underline_action = QAction(QIcon(os.path.join('images', 'edit-underline.png')), "Underline", self)
    self.underline_action.setStatusTip("Underline")
    self.underline_action.setShortcut(QKeySequence.Underline)
    self.underline_action.setCheckable(True)
    self.underline_action.toggled.connect(self.editor.setFontUnderline)
    format_toolbar.addAction(self.underline_action)
    format_menu.addAction(self.underline_action)

```

The actions are added both to the toolbar at the menus. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
### Alignment
We finally add the handlers for alignment formatting. These are set up as a `QActionGroup` because they are mutually exclusive: action groups function like radio buttons. Each action's `.triggered` signal is connected to set a specific alignment on the current paragraph via the editor `.setAlignment`. We again use a `lambda` to, allowing us to pass the specific alignment type to the target method.
## Handling editor updates
We've defined a series of actions which, given user interaction to toggle them, will switch formatting in the editor. When a user selects text we also want to update the toolbar to match — turning the icon to bold, when a user selects some bold text for example. The niggle here is that if we update the actions in the toolbar they themselves will trigger an event which can undo the same action. To avoid this we store a `list` of actions to be blocked when updating the format.
python ```
# A list of all format-related widgets/actions, so we can disable/enable signals when updating.
    self._format_actions = [
      self.fonts,
      self.fontsize,
      self.bold_action,
      self.italic_action,
      self.underline_action,
      # We don't need to disable signals for alignment, as they are paragraph-wide.
    ]

```

The format update function then first blocks these signals, updates the toolbar widgets to represent the format of the currently selected text, and then re-enables the format afterwards.
python ```
def block_signals(self, objects, b):
    for o in objects:
      o.blockSignals(b)
  def update_format(self):
    """
    Update the font format toolbar/actions when a new text selection is made. This is necessary to keep
    toolbars/etc. in sync with the current edit state.
    :return:
    """
    # Disable signals for all format widgets, so changing values here does not trigger further formatting.
    self.block_signals(self._format_actions, True)
    self.fonts.setCurrentFont(self.editor.currentFont())
    # Nasty, but we get the font-size as a float but want it was an int
    self.fontsize.setCurrentText(str(int(self.editor.fontPointSize())))
    self.italic_action.setChecked(self.editor.fontItalic())
    self.underline_action.setChecked(self.editor.fontUnderline())
    self.bold_action.setChecked(self.editor.fontWeight() == QFont.Bold)
    self.alignl_action.setChecked(self.editor.alignment() == Qt.AlignLeft)
    self.alignc_action.setChecked(self.editor.alignment() == Qt.AlignCenter)
    self.alignr_action.setChecked(self.editor.alignment() == Qt.AlignRight)
    self.alignj_action.setChecked(self.editor.alignment() == Qt.AlignJustify)
    self.block_signals(self._format_actions, False)

```

Note the different approaches needed to toggle the status icons. _Italic_ and _underline_ are both available as `bool` values from the editor, while we need to compare the current weight for _bold_. For alignments, we can compare the current alignment to the Qt namespace values `Qt.AlignLeft`.
The font size change is a bit unpleasant: we get the point size from the editor, convert it to an integer (to round down) and then to a string, to apply as the current text for the box. This is necessary since users are free to enter any size value, even one not currently in the list.
## Opening & Saving files
The file open and save handlers are almost identical to those used in No2Pads with the slight tweak that we load and save as HTML for rich text. This is the only format natively supported by the Qt rich text widget for loading and saving — to support other formats you would need to write a converter between these. Plain text loading and saving is also supported.
python ```
def file_open(self):
    path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "HTML documents (*.html);Text documents (*.txt);All files (*.*)")
    try:
      with open(path, 'rU') as f:
        text = f.read()
    except Exception as e:
      self.dialog_critical(str(e))
    else:
      self.path = path
      # Qt will automatically try and guess the format as txt/html
      self.editor.setText(text)
      self.update_title()
  def file_save(self):
    if self.path is None:
      # If we do not have a path, we need to use Save As.
      return self.file_saveas()
    text = self.editor.toHtml() if splitext(self.path) in HTML_EXTENSIONS else self.editor.toPlainText()
    try:
      with open(self.path, 'w') as f:
        f.write(text)
    except Exception as e:
      self.dialog_critical(str(e))
  def file_saveas(self):
    path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "HTML documents (*.html);Text documents (*.txt);All files (*.*)")
    if not path:
      # If dialog is cancelled, will return ''
      return
    text = self.editor.toHtml() if splitext(path) in HTML_EXTENSIONS else self.editor.toPlainText()
    try:
      with open(path, 'w') as f:
        f.write(text)
    except Exception as e:
      self.dialog_critical(str(e))
    else:
      self.path = path
      self.update_title()

```

## Future ideas
You could extend the Megasolid Idiom to support —
  1. Text colour formatting. The support is there in `QTextEdit` for both foreground and background colours. Take a look at [this QColor color-selector widget](https://www.pythonguis.com/tutorials/qcolorbutton-a-color-selector-tool-for-pyqt/).
  2. Add support for both import/export formats, converting via HTML.


Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Megasolid Idiom, a Rich Text Editor** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/examples/python-rich-text-editor/Python books) on the subject. 
**Megasolid Idiom, a Rich Text Editor** was published in [examples](https://www.pythonguis.com/examples/) on March 07, 2019 (updated March 10, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [qt5](https://www.pythonguis.com/topics/qt5/) [app](https://www.pythonguis.com/topics/app/) [word-processor](https://www.pythonguis.com/topics/word-processor/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/)
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
