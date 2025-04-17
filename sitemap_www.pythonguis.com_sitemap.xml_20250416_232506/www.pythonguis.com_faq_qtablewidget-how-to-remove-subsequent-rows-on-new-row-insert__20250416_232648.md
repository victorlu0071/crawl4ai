# Content from: https://www.pythonguis.com/faq/qtablewidget-how-to-remove-subsequent-rows-on-new-row-insert/

[](https://www.pythonguis.com/faq/qtablewidget-how-to-remove-subsequent-rows-on-new-row-insert/#menu)
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
# QTableWidget: How to remove subsequent rows on new row insert?
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
PedanticHacker | 2020-07-23 21:39:34 UTC | #1
Hello, @martin! :slight_smile: 
So I have an interesting problem to solve. I am coding a chess GUI application. I have a QTableWidget table for the chess moves to be displayed in two columns, column 0 for the White player and column 1 for the Black player. When I click on a cell and that cell becomes selected, the chessboard position changes accordingly.
Now I want to code that if the user adds a new chess move in that particular position, while rows are inserted below that currently selected row, to remove all those subsequent rows. So, if the chess move added is for the White player, insert a new row and add that chess move to column 0 and remove subsequent rows; but if the chess move added is for the Black player, overwrite the item in column 1 and also remove subsequent rows.
My slot method looks like this:
python ```
@pyqtSlot(chess.Move)
def on_new_move_made(self, move):
  """Inserts a new move into the table of chess moves in SAN
  (Standard Algebraic Notation) format.
  """
  if settings.board.turn == chess.WHITE:
    self.row = self.moves_widget.rowCount()
    self.column = 0
    self.moves_widget.insertRow(self.row)
  elif settings.board.turn == chess.BLACK:
    self.column = 1
  san_move = settings.board.san(move)
  self.new_move = QTableWidgetItem(san_move)
  self.moves_widget.setItem(self.row, self.column, self.new_move)
  self.moves_widget.setCurrentItem(self.new_move)
  self.moves_widget.scrollToBottom()

```

I'm frustrated. Please help me out. Thank you!
martin | 2020-07-29 14:37:25 UTC | #2 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Hey @PedanticHacker thanks for the post and welcome to the forum. Sorry for the delay in replying -- this wasn't so simple to figure out (more the logic than Qt specific stuff).
If I understand your problem correctly, you want the user to basically "overwrite" previous moves in the list at any time, by selecting a row and then adding the move? If a row is selected and there are subsequent rows then you want to delete the following.
The tricky part really is how to handle the current white/black state. I've gone for the following -- 
  1. if a row is selected all subsequent rows are deleted.
  2. if the next move is a white move, it will _always_ add a new row after the selected row
  3. if the next move is a black move, it will _always_ replace the black move on the selected row


The following is a fully-working example. I've defined a simply `Move` class and a move generator, which toggles between white/black turns and returns positions that follow chess rules (I think, I don't really know).
python ```
from PyQt5.QtWidgets import QTableWidget, QVBoxLayout, QWidget, QPushButton, QTableWidgetItem, QMainWindow, QApplication
from random import choice
WHITE = 0
BLACK = 1
class Move:
  def __init__(self, turn, move):
    self.turn = turn
    self.move = move
  def __str__(self):
    return "{} {}".format(self.turn, self.move)
def chess_moves():
  """
  Generator producing chess moves.
  """
  turn = WHITE
  while True:
    move_str = choice('KQRBN ') + choice('abcdefgh') + choice('12345678')
    yield Move(turn, move_str)
    # Cycle the white/black turns.
    if turn == WHITE:
      turn = BLACK
    else:
      turn = WHITE

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.moves = chess_moves()
    self.moves_widget = QTableWidget()
    self.moves_widget.setColumnCount(2)
    self.moves_widget.setHorizontalHeaderLabels(['White','Black'])
    self.btn = QPushButton("Move")
    self.btn.pressed.connect(self.add_chess_move)
    layout = QVBoxLayout()
    layout.addWidget(self.moves_widget)
    layout.addWidget(self.btn)
    w = QWidget()
    w.setLayout(layout)
    self.setCentralWidget(w)

  def add_chess_move(self):
    move = next(self.moves)
    selected = self.moves_widget.selectedIndexes()
    if selected:
      row = selected[0].row() # Get row of first selected item.
      # Row is selected, delete all after.
      while self.moves_widget.rowCount() > row + 1:
        self.moves_widget.removeRow(row + 1)
      # Clear selection so we don't re-delete next time.
      self.moves_widget.clearSelection()
    row = self.moves_widget.rowCount()-1
    # White always adds a new row.
    if move.turn == WHITE:
      row += 1
      self.moves_widget.setRowCount(row+1)
    item = QTableWidgetItem(move.move)
    column = move.turn
    self.moves_widget.setItem(row, move.turn, item)
    self.moves_widget.scrollToBottom()

app = QApplication([])
w = MainWindow()
w.show()
app.exec_()

```

As shown, for deleting rows the simplest option is to delete the row after the current one _repeatedly_ , until the table is empty. Since the subsequent moves will "scroll up" by doing this you empty the list after that point.
Saying all this, I wonder if you've come across the [model views](https://www.pythonguis.com/courses/model-views/qtableview-modelviews-numpy-pandas/)? Using these you could represent your list of moves as a simple Python list and avoid all this manipulation in the table itself -- you could just chop off the end of a list and be done.
Hope this helps!
PedanticHacker | 2020-07-29 18:54:15 UTC | #3
Thanks for your answer, @martin!
Is it also possible I use a combination of QTableWidget's currentRow() and/or currentColumn() methods with setRowCount()? So, if the currently selected row is, for example, 5 and the table has, like, 10 rows and a new chess move was inserted, I'd just set a new row count and be done with this. But I wasn't able to make this work. Am I even thinking in the right direction?
martin | 2020-07-29 19:40:12 UTC | #4
You're quite right! The block can be replaced with ...
python ```
    if selected:
      row = selected[0].row() # Get row of first selected item.
      # Row is selected, delete all after.
      self.moves_widget.setRowCount(row + 1)
      # Clear selection so we don't re-delete next time.
      self.moves_widget.clearSelection()

```

You need to set the row count to the selected row number _plus one_ because the row numbers are zero indexed. So if you select the first (0th) row, you're selecting row 0 and want 1 rows total.
For the `currentColumn` are you wanting to replace the white move and clear the black move if it's the white's turn and you select a row (rather than start a new one always)?
PedanticHacker | 2020-07-29 22:50:35 UTC | #5 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
We're getting close to the solution! :slight_smile:
I think it would be simpler to replace the White's move and use the takeItem() method of QTableWidget to remove the Black's move (if it is White's turn), and remove subsequent rows. If the turn is Black's, then the item is automatically replaced, so here we should only remove subsequent rows.
I've tested your code and it removes rows after the currently selected row on new move insertion. However, we're not quite there yet, because only subsequent rows are removed, but the new move is not displayed.
Here's my updated slot code...
python ```
@pyqtSlot(chess.Move)
def on_new_move_made(self, move):
  """Inserts a new move into the table of chess moves in SAN
  (Standard Algebraic Notation) format.
  """
  move_selected = self.moves_widget.selectedIndexes()
  if move_selected:
    # Get the row number of the currently selected chess move
    # for the white player.
    white_player = 0
    row = move_selected[white_player].row()
    # A new chess move is made, so delete all move entries
    # after it.
    self.moves_widget.setRowCount(row + 1)
    # Clear the chess move selection so that the entry of the
    # move is not re-deleted on new move insertion.
    self.moves_widget.clearSelection()
  elif not move_selected:
    if settings.board.turn == chess.WHITE:
      self.row = self.moves_widget.rowCount()
      self.column = 0
      self.moves_widget.insertRow(self.row)
    elif settings.board.turn == chess.BLACK:
      self.column = 1
    san_move = settings.board.san(move)
    self.new_move = QTableWidgetItem(san_move)
    self.moves_widget.setItem(self.row, self.column, self.new_move)
    self.moves_widget.scrollToBottom()

```

martin | 2020-08-04 17:35:06 UTC | #6
I think this does what you're looking for ---
python ```
from PyQt5.QtWidgets import QTableWidget, QVBoxLayout, QWidget, QPushButton, QTableWidgetItem, QMainWindow, QApplication
from random import choice
WHITE = 0
BLACK = 1
class Move:
  def __init__(self, turn, move):
    self.turn = turn
    self.move = move
  def __str__(self):
    return "{} {}".format(self.turn, self.move)
def chess_moves():
  """
  Generator producing chess moves.
  """
  turn = WHITE
  while True:
    move_str = choice('KQRBN ') + choice('abcdefgh') + choice('12345678')
    yield Move(turn, move_str)
    # Cycle the white/black turns.
    if turn == WHITE:
      turn = BLACK
    else:
      turn = WHITE

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.moves = chess_moves()
    self.moves_widget = QTableWidget()
    self.moves_widget.setColumnCount(2)
    self.moves_widget.setHorizontalHeaderLabels(['White','Black'])
    self.btn = QPushButton("Move")
    self.btn.pressed.connect(self.add_chess_move)
    layout = QVBoxLayout()
    layout.addWidget(self.moves_widget)
    layout.addWidget(self.btn)
    w = QWidget()
    w.setLayout(layout)
    self.setCentralWidget(w)

  def add_chess_move(self):
    move = next(self.moves)
    item = QTableWidgetItem(move.move)
    selected = self.moves_widget.selectedIndexes()
    if selected:
      # We have a selected row.
      row = selected[0].row() # Get row of first selected item.
      # Row is selected, delete all after.
      self.moves_widget.setRowCount(row + 1)
      # Clear selection so we don't re-delete next time.
      self.moves_widget.clearSelection()
      # Replace move in column 1, clear column 2.
      self.moves_widget.setItem(row, move.turn, item)
      if move.turn == WHITE:
        # Clear column 2 (black)
        self.moves_widget.takeItem(row, BLACK)
    else:
      # Nothing is selected
      row = self.moves_widget.rowCount() - 1
      if move.turn == WHITE:
        # Append a row.
        row += 1
        self.moves_widget.setRowCount(row + 1)
      column = move.turn
      self.moves_widget.setItem(row, move.turn, item)

    self.moves_widget.scrollToBottom()

app = QApplication([])
w = MainWindow()
w.show()
app.exec_()

```

I split out the two states "adding with selected" and "adding with no selection" to separate branches to keep things simple. 
If you select a row when it's black's turn, then the black move will be replaced on the selected row. If you select a row when it's white's turn, then the white move will be replaced, and the black move cleared.
PedanticHacker | 2020-08-12 19:18:06 UTC | #7
Based on your example, I can now declare my problem solved. Thank you, @martin! :slight_smile:
My slot now looks like this...
> python ```
@pyqtSlot(chess.Move)
def on_new_move_made(self, move):
  """Inserts a new move into the table of chess moves in SAN
  (Standard Algebraic Notation) format.
  """
  row = self.moves_widget.rowCount()
  column = 0 if settings.board.turn == chess.WHITE else 1
  san_move = settings.board.san(move)
  new_move = QTableWidgetItem(san_move)
  selected_move = self.moves_widget.selectedIndexes()
  if not selected_move:
    if settings.board.turn == chess.WHITE:
      self.moves_widget.setRowCount(row + 1)
    elif settings.board.turn == chess.BLACK:
      row -= 1
  elif selected_move:
    index = 0
    row = selected_move[index].row()
    if settings.board.turn == chess.WHITE:
      self.moves_widget.setRowCount(row + 1)
      self.moves_widget.insertRow(row + 1)
      row += 1
    elif settings.board.turn == chess.BLACK:
      self.moves_widget.setRowCount(row + 1)
  self.moves_widget.setItem(row, column, new_move)
  self.moves_widget.clearSelection()
  self.moves_widget.scrollToBottom()

```

If you have any optimization suggestions, please let me know. Thanks again!
PedanticHacker | 2020-08-12 19:18:06 UTC | #8
I've updated my code a bit. I'm posting this for my personal future reference and for anyone that might encounter a similar problem. Below is the refactored code.
python ```
@pyqtSlot(chess.Move)
def add_new_move(self, move):
  """Inserts a new move into the table of chess moves in SAN
  (Standard Algebraic Notation) format.
  """
  row = self.moves_widget.rowCount()
  column = 0 if settings.board.turn == chess.WHITE else 1
  number_of_columns = self.moves_widget.columnCount()
  move_index = (row * number_of_columns) + column
  settings.board.move_stack[move_index:-1]
  san_move = settings.board.san(move)
  new_move = QTableWidgetItem(san_move)
  if settings.board.turn == chess.WHITE:
    self.moves_widget.setRowCount(row + 1)
  elif settings.board.turn == chess.BLACK:
    row -= 1
  self.moves_widget.setItem(row, column, new_move)
  self.moves_widget.scrollToBottom()
  self.svg_widget.move_sound_played.emit()

```

The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**QTableWidget: How to remove subsequent rows on new row insert?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/qtablewidget-how-to-remove-subsequent-rows-on-new-row-insert/Python books) on the subject. 
**QTableWidget: How to remove subsequent rows on new row insert?** was published in [faq](https://www.pythonguis.com/faq/) on July 23, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
