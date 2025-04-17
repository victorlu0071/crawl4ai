# Content from: https://www.pythonguis.com/faq/how-to-drag-drop-svg-elements/

[](https://www.pythonguis.com/faq/how-to-drag-drop-svg-elements/#menu)
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
# How to drag&drop SVG elements?
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
PedanticHacker | 2021-03-29 10:33:50 UTC | #1
Hello, I'm back with a new question. 🙂
How can I implement drag&drop operation if the operation is going to be done on an SVG canvas? It's an SVG chessboard and I want to implement drag&drop for chess piece elements. How can I implement the drag&drop operation using PyQt6? 🤔
martin | 2021-04-07 15:18:00 UTC | #2
Always interesting questions :smiley:
When you say a SVG canvas what do you mean? My default approach for something like this would be using `QGraphicsScene` to display the SVG objects and handle the drag/drop behavior there. Or are you displaying it already in some other way?
PedanticHacker | 2021-04-08 10:39:57 UTC | #3 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
Yes, I am already displaying the chessboard (my SVG canvas) with the `load()` method of the `QSvgWidget` class. Is this something that can be done, or is `QGraphicsScene` inevitable to be implemented for the drag&drop functionality?
PedanticHacker | 2021-05-14 13:30:19 UTC | #4
Should I use [this](https://doc.qt.io/qt-6/qgraphicsscene.html#addWidget) class?
martin | 2021-05-14 15:53:14 UTC | #5
Sorry this dropped completely off my radar. Yes, I think graphics scene is the way to go -- I'm sure you _could_ work something out using `QSvgWidget` layering multiple items over one another, but I think it would be hard to work with.
Using graphics scene you can load SVG objects in using `item = QGraphicsSvgItem("example.svg")` -- once you have the item, just add it to the scene.
Here's a working example -- just replace `example.svg` with any SVG file.
python ```
import sys
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QApplication, QGraphicsItem, QMainWindow
from PyQt5.QtSvg import QGraphicsSvgItem

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    item = QGraphicsSvgItem('example.svg')
    item.setFlag(QGraphicsItem.ItemIsMovable)
    self.scene = QGraphicsScene()
    self.scene.addItem(item)
    self.view = QGraphicsView()
    self.view.setScene(self.scene)
    self.setCentralWidget(self.view)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

```

https://imgur.com/eBjI4s0
PedanticHacker | 2021-05-14 19:01:54 UTC | #6
Thanks, @martin!
I've fixed the code to work on PyQt6 v6.1. Here you go:
python ```
import sys
from PyQt6.QtWidgets import (
  QApplication, QGraphicsItem, QGraphicsScene, QGraphicsView, QMainWindow)
from PyQt6.QtSvgWidgets import QGraphicsSvgItem

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    item = QGraphicsSvgItem("test.svg")
    item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
    self.scene = QGraphicsScene()
    self.scene.addItem(item)
    self.view = QGraphicsView()
    self.view.setScene(self.scene)
    self.setCentralWidget(self.view)

if __name__ == "__main__":
  app_instance = QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  app_instance.exec()

```

Now I just need to know how can I move SVG pieces on an SVG chessboard. So the chessboard needs to be stationary, but the pieces must be drag&droppable. Please expand on your code to achieve that kind of behavior.
martin | 2021-05-14 20:31:54 UTC | #7
If you don't set the `QGraphicsItem.GraphicsItemFlag.ItemIsMovable` the object will be fixed in the scene -- undraggable. So you can just _not_ set that on your board.
It's been a while since I worked with the graphics scene bits but here's a simple turn-taking chess board, with white and black pieces. I had to keep with PyQt5 -- using PyQt6 I was seeing some weird visual distortion when moving the pieces (clipping errors).
python ```

import sys
from PyQt5.QtWidgets import (
  QApplication, QGraphicsItem, QGraphicsScene, QGraphicsView, QMainWindow)
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtCore import pyqtSignal, QSize, QPointF
class ChessPiece(QGraphicsSvgItem):
  moved = pyqtSignal() # emit piece color/value
  def __init__(self):
    super().__init__(self.svg)
  def check_turn(self, color):
    self.setFlag(QGraphicsItem.ItemIsMovable, color == self.color)
  def mouseReleaseEvent(self, e):
    super().mouseReleaseEvent(e)
    # add check if moved.
    print("moved!")
    self.moved.emit()

class WhiteChessPiece(ChessPiece):
  color = 'w'
  svg = 'white.svg'
class BlackChessPiece(ChessPiece):
  color = 'b'
  svg = 'black.svg'

class MainWindow(QMainWindow):
  turn = pyqtSignal(str)
  def __init__(self):
    super().__init__()
    self.scene = QGraphicsScene()
    board = QGraphicsSvgItem("chessboard.svg")
    self.scene.addItem(board)
    pieces = []
    for cls, y in [(WhiteChessPiece, 0), (BlackChessPiece, 1)]:
      for x in range(8):
        cp = cls()
        cp.setScale(2)
        cp.setPos(QPointF(30+x*63, 10+y*450))
        cp.setFlag(QGraphicsItem.ItemIsMovable, True)
        cp.setFlag(QGraphicsItem.ItemClipsToShape, True)
        self.turn.connect(cp.check_turn)
        cp.moved.connect(self.toggle_turn)
        pieces.append(cp)
        self.scene.addItem(cp)
    self.view = QGraphicsView()
    self.view.setScene(self.scene)
    self.setCentralWidget(self.view)
    # Initial state.
    self.current_turn = 'w'
    self.turn.emit(self.current_turn)

  def toggle_turn(self):
    print("Current turn", self.current_turn)
    self.current_turn = 'w' if self.current_turn == 'b' else 'b'
    print("Change turn to", self.current_turn)
    self.turn.emit(self.current_turn)

if __name__ == "__main__":
  app_instance = QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  app_instance.exec()

```

This is what it looks like in action. Moving a piece toggles the current turn, you can't drag a white piece when it's black's turn and vice versa.
https://imgur.com/Cf2zVe8
I used the SVG chess pieces from Wikipedia, with [this board](https://freesvg.org/wooden-chessboard).
PedanticHacker | 2021-05-14 23:37:07 UTC | #8
Wow, this is very interesting! Thank you.
I've noticed that when a piece is dropped (after being dragged), it doesn't clip to a square. How can I achieve that?
EDIT: I am reading about `QGraphicsProxyWidget`. I guess I can pass my SVG chessboard (with pieces) to `QGraphicsProxyWidget` and see what that'll do. My SVG chessboard (as a `QSvgWidget` subclass) inherits `QWidget`, so that should work. `QGraphicsProxyWidget` needs a `QWidget` descendant to work.
martin | 2021-05-15 08:33:56 UTC | #9
If I remember rightly you can handle that using `itemChange` on your subclass. This receives notifications when something changes on the item, if you catch `QGraphicsItem.GraphicsItemChange.ItemPositionChange` you can than modify the position to the grid. That method is where you will implement most of the custom behaviours for your pieces -- probably should have used it for the "move detection" in my example.
If you want to detect which square a piece is in, you have two options --
  1. Use the (snapped) position and calculate the grid position from this. Remember that by default the position is the top left, you might want to change it to the middle-bottom of the piece, or just calculate it using the size.
  2. Overlay some (invisible) blocks into the board squares, giving each a name (in chess nomenclature) which matches the grid position and emit that directly.


If you want to do the second, you can make things easier on yourself by positioning the hit box towards the top of the board square. That way you avoid dealing with multiple hits, and the piece will register "in" whichever square its base is over.
![image|114x114](https://www.pythonguis.com/static/faq/forum/how-to-drag-drop-svg-elements/uT7cRct7m59pK1PXzL3hlBDjRLC.png)
You might still have problems on the horizontal with differently sized/shaped pieces, so (1) could be easier overall.
PedanticHacker | 2021-05-15 10:36:38 UTC | #10
What about the `QGraphicsProxyWidget`?
I already have a fully-working SVG chessboard widget (in which chess pieces obey the rules of chess and also snap into squares), but the widget only provides click-click functionality for piece movement. I am hoping that this `QGraphicsProxyWidget` will provide the drag&drop functionality.
Am I leaning towards the right path?
EDIT: Maybe I should focus my attention on using QtQuick to implement what I want?
martin | 2021-05-15 16:12:19 UTC | #11
Not sure, but I don't think so. `QGraphicsProxyWidget` wraps _widgets_ to make them work inside `QGraphicsScene`. It's basically a translation layer between the graphics scene API and the widget API.
What you're asking for is something to allow you to manipulate objects inside an SVG object. `QGraphicsSvgItem` doesn't support SVG manipulation (as far as I can tell) and neither does `QSvgWidget` -- adding a proxy widget on top of it won't change that.
The problem would be the same in QML too -- you'd need methods to allow you to change items inside your SVG. You could re-implement a chess board in QML but it wouldn't be much different to doing it in graphics scene.
I'd really just bite the bullet and implement your own chess board view in graphics scene. It's not particularly complex to do and it'll give you complete control over how things behave/look in your app.
If you're still using the `python-chess` library for the engine, take a look at [the SVG module](https://github.com/niklasf/python-chess/blob/master/chess/svg.py) -- that's how the SVG is drawn, which you can convert step-by-step to graphics scene objects.
PedanticHacker | 2021-05-16 00:02:40 UTC | #12
[quote="martin, post:11, topic:831"] If you’re still using the `python-chess` library for the engine, take a look at [the SVG module](https://github.com/niklasf/python-chess/blob/master/chess/svg.py) – that’s how the SVG is drawn, which you can convert step-by-step to graphics scene objects. [/quote]
Yes, I am using exactly that! Please give me a hint on how to convert the python-chess SVG to graphics scene objects.
PedanticHacker | 2021-05-16 00:02:06 UTC | #13
So far, I have managed to produce this code:
python ```
import sys
from PyQt5.QtWidgets import (
  QApplication, QGraphicsItem, QGraphicsScene, QGraphicsView, QMainWindow)
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtSvg import QGraphicsSvgItem

class ChessPiece(QGraphicsSvgItem):
  moved = pyqtSignal()
  def __init__(self):
    super().__init__(self.svg)
  def mouseReleaseEvent(self, event):
    super().mouseReleaseEvent(event)
    self.moved.emit()
  @pyqtSlot(bool)
  def check_turn(self, turn):
    white_or_black = (turn == self._turn)
    self.setFlag(
      QGraphicsItem.GraphicsItemFlag.ItemIsMovable,
      enabled=white_or_black)

class WhitePawn(ChessPiece):
  _turn = True
  svg = "svg/pieces/white_pawn.svg"

class WhiteRook(ChessPiece):
  _turn = True
  svg = "svg/pieces/white_rook.svg"

class WhiteKnight(ChessPiece):
  _turn = True
  svg = "svg/pieces/white_knight.svg"

class WhiteBishop(ChessPiece):
  _turn = True
  svg = "svg/pieces/white_bishop.svg"

class WhiteQueen(ChessPiece):
  _turn = True
  svg = "svg/pieces/white_queen.svg"

class WhiteKing(ChessPiece):
  _turn = True
  svg = "svg/pieces/white_king.svg"

class BlackPawn(ChessPiece):
  _turn = False
  svg = "svg/pieces/black_pawn.svg"

class BlackRook(ChessPiece):
  _turn = False
  svg = "svg/pieces/black_rook.svg"

class BlackKnight(ChessPiece):
  _turn = False
  svg = "svg/pieces/black_knight.svg"

class BlackBishop(ChessPiece):
  _turn = False
  svg = "svg/pieces/black_bishop.svg"

class BlackQueen(ChessPiece):
  _turn = False
  svg = "svg/pieces/black_queen.svg"

class BlackKing(ChessPiece):
  _turn = False
  svg = "svg/pieces/black_king.svg"

class MainWindow(QMainWindow):
  turn = pyqtSignal(bool)
  def __init__(self):
    super().__init__()
    self._current_turn = True
    self.scene = QGraphicsScene()
    board = QGraphicsSvgItem("svg/board.svg")
    self.scene.addItem(board)
    for pawn, rank in [(WhitePawn, 6), (BlackPawn, 1)]:
      for piece in range(8):
        _piece = pawn()
        _piece.setScale(1.1)
        _piece.setPos(12.5 + 45*piece, 12.5 + 45*rank)
        _piece.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        _piece.setFlag(QGraphicsItem.GraphicsItemFlag.ItemClipsToShape)
        self.turn.connect(_piece.check_turn)
        _piece.moved.connect(self.toggle_turn)
        self.scene.addItem(_piece)
    for rook, rank in [(WhiteRook, 7), (BlackRook, 0)]:
      for piece in range(2):
        _piece = rook()
        _piece.setScale(1.1)
        _piece.setPos(12.5 + 316.25*piece, 12.5 + 45*rank)
        _piece.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        _piece.setFlag(QGraphicsItem.GraphicsItemFlag.ItemClipsToShape)
        self.turn.connect(_piece.check_turn)
        _piece.moved.connect(self.toggle_turn)
        self.scene.addItem(_piece)
    for knight, rank in [(WhiteKnight, 7), (BlackKnight, 0)]:
      for piece in range(2):
        _piece = knight()
        _piece.setScale(1.1)
        _piece.setPos(57.5 + 225*piece, 12.5 + 45*rank)
        _piece.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        _piece.setFlag(QGraphicsItem.GraphicsItemFlag.ItemClipsToShape)
        self.turn.connect(_piece.check_turn)
        _piece.moved.connect(self.toggle_turn)
        self.scene.addItem(_piece)
    for bishop, rank in [(WhiteBishop, 7), (BlackBishop, 0)]:
      for piece in range(2):
        _piece = bishop()
        _piece.setScale(1.1)
        _piece.setPos(103 + 135*piece, 12.5 + 45*rank)
        _piece.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        _piece.setFlag(QGraphicsItem.GraphicsItemFlag.ItemClipsToShape)
        self.turn.connect(_piece.check_turn)
        _piece.moved.connect(self.toggle_turn)
        self.scene.addItem(_piece)
    for queen, rank in [(WhiteQueen, 7), (BlackQueen, 0)]:
      for piece in range(1):
        _piece = queen()
        _piece.setScale(1.1)
        _piece.setPos(148 + 135*piece, 12.5 + 45*rank)
        _piece.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        _piece.setFlag(QGraphicsItem.GraphicsItemFlag.ItemClipsToShape)
        self.turn.connect(_piece.check_turn)
        _piece.moved.connect(self.toggle_turn)
        self.scene.addItem(_piece)
    for king, rank in [(WhiteKing, 7), (BlackKing, 0)]:
      for piece in range(1):
        _piece = king()
        _piece.setScale(1.1)
        _piece.setPos(193 + 135*piece, 12.5 + 45*rank)
        _piece.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        _piece.setFlag(QGraphicsItem.GraphicsItemFlag.ItemClipsToShape)
        self.turn.connect(_piece.check_turn)
        _piece.moved.connect(self.toggle_turn)
        self.scene.addItem(_piece)
    self.view = QGraphicsView()
    self.view.setScene(self.scene)
    self.setCentralWidget(self.view)
  @pyqtSlot()
  def toggle_turn(self):
    self._current_turn = not self._current_turn
    self.turn.emit(self._current_turn)

if __name__ == "__main__":
  app_instance = QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  app_instance.exec()

```

This code plus all the needed SVG files were uploaded [HERE](https://ufile.io/ah1sxltj). It's a ZIP file.
I, however, still want to know how to convert the python-chess SVG to graphics scene objects. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
martin | 2021-05-16 06:46:06 UTC | #14
In the python-chess SVG module it constructs a SVG document, and then creates the pieces and adds them to it. If you replace that base document with a QGraphicsScene, and then instead of adding the SVG pieces to the document, you wrap them in `QGraphicsSvgItem` and add them to the scene (individually).
Most of the code _should_ stay the same, since it's just defining SVG objects which you can wrap. Later you could, for example, replace arrows etc. with `QGraphicsScene` native equivalents, or translate the pieces to native paths, but you don't have to.
Remember, you can clear & re-assemble the board on each move (like the SVG version does).
I'm going to be out of office for the next couple of weeks, but if I find myself with some time to kill I'll have a go ;)
PedanticHacker | 2021-05-19 12:57:45 UTC | #15
I'm having a hard time to understand what exactly you mean by saying `wrap SVG objects`. Please elaborate, if you find the time.
martin | 2021-05-20 17:02:53 UTC | #16
Here you go, little working demo.
![Screenshot 2021-05-20 at 19.02.07|565x500](https://www.pythonguis.com/static/faq/forum/how-to-drag-drop-svg-elements/i1sdoNhEEy1OkuA1yDJ1r3IMm8K.jpeg)
What I meant was take the SVG g-path definitions from the the python-chess SVG module and then use them to create `QGraphicsSvgItem` objects. When I tried it turns out you can't create a svg object from a string, so in the example below I write them out to files.
python ```
import math
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import QRectF, QTimer, QPointF
from PyQt5.QtGui import QBrush, QColor, QPen
from PyQt5.QtSvg import QGraphicsSvgItem
import chess
from typing import Dict, Iterable, Optional, Tuple, Union
from io import StringIO
board = chess.Board()

SQUARE_SIZE = 45
MARGIN = 20
PIECES_G = {
  "b": """<g id="black-bishop" class="black bishop" fill="none" fill-rule="evenodd" stroke="#000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 36c3.39-.97 10.11.43 13.5-2 3.39 2.43 10.11 1.03 13.5 2 0 0 1.65.54 3 2-.68.97-1.65.99-3 .5-3.39-.97-10.11.46-13.5-1-3.39 1.46-10.11.03-13.5 1-1.354.49-2.323.47-3-.5 1.354-1.94 3-2 3-2zm6-4c2.5 2.5 12.5 2.5 15 0 .5-1.5 0-2 0-2 0-2.5-2.5-4-2.5-4 5.5-1.5 6-11.5-5-15.5-11 4-10.5 14-5 15.5 0 0-2.5 1.5-2.5 4 0 0-.5.5 0 2zM25 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 1 1 5 0z" fill="#000" stroke-linecap="butt"/><path d="M17.5 26h10M15 30h15m-7.5-14.5v5M20 18h5" stroke="#fff" stroke-linejoin="miter"/></g>""", # noqa: E501
  "k": """<g id="black-king" class="black king" fill="none" fill-rule="evenodd" stroke="#000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22.5 11.63V6" stroke-linejoin="miter"/><path d="M22.5 25s4.5-7.5 3-10.5c0 0-1-2.5-3-2.5s-3 2.5-3 2.5c-1.5 3 3 10.5 3 10.5" fill="#000" stroke-linecap="butt" stroke-linejoin="miter"/><path d="M11.5 37c5.5 3.5 15.5 3.5 21 0v-7s9-4.5 6-10.5c-4-6.5-13.5-3.5-16 4V27v-3.5c-3.5-7.5-13-10.5-16-4-3 6 5 10 5 10V37z" fill="#000"/><path d="M20 8h5" stroke-linejoin="miter"/><path d="M32 29.5s8.5-4 6.03-9.65C34.15 14 25 18 22.5 24.5l.01 2.1-.01-2.1C20 18 9.906 14 6.997 19.85c-2.497 5.65 4.853 9 4.853 9M11.5 30c5.5-3 15.5-3 21 0m-21 3.5c5.5-3 15.5-3 21 0m-21 3.5c5.5-3 15.5-3 21 0" stroke="#fff"/></g>""", # noqa: E501
  "n": """<g id="black-knight" class="black knight" fill="none" fill-rule="evenodd" stroke="#000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M 22,10 C 32.5,11 38.5,18 38,39 L 15,39 C 15,30 25,32.5 23,18" style="fill:#000000; stroke:#000000;"/><path d="M 24,18 C 24.38,20.91 18.45,25.37 16,27 C 13,29 13.18,31.34 11,31 C 9.958,30.06 12.41,27.96 11,28 C 10,28 11.19,29.23 10,30 C 9,30 5.997,31 6,26 C 6,24 12,14 12,14 C 12,14 13.89,12.1 14,10.5 C 13.27,9.506 13.5,8.5 13.5,7.5 C 14.5,6.5 16.5,10 16.5,10 L 18.5,10 C 18.5,10 19.28,8.008 21,7 C 22,7 22,10 22,10" style="fill:#000000; stroke:#000000;"/><path d="M 9.5 25.5 A 0.5 0.5 0 1 1 8.5,25.5 A 0.5 0.5 0 1 1 9.5 25.5 z" style="fill:#ececec; stroke:#ececec;"/><path d="M 15 15.5 A 0.5 1.5 0 1 1 14,15.5 A 0.5 1.5 0 1 1 15 15.5 z" transform="matrix(0.866,0.5,-0.5,0.866,9.693,-5.173)" style="fill:#ececec; stroke:#ececec;"/><path d="M 24.55,10.4 L 24.1,11.85 L 24.6,12 C 27.75,13 30.25,14.49 32.5,18.75 C 34.75,23.01 35.75,29.06 35.25,39 L 35.2,39.5 L 37.45,39.5 L 37.5,39 C 38,28.94 36.62,22.15 34.25,17.66 C 31.88,13.17 28.46,11.02 25.06,10.5 L 24.55,10.4 z " style="fill:#ececec; stroke:none;"/></g>""", # noqa: E501
  "p": """<g id="black-pawn" class="black pawn"><path d="M22 9c-2.21 0-4 1.79-4 4 0 .89.29 1.71.78 2.38-1.95 1.12-3.28 3.21-3.28 5.62 0 2.03.94 3.84 2.41 5.03-3 1.06-7.41 5.55-7.41 13.47h23c0-7.92-4.41-12.41-7.41-13.47 1.47-1.19 2.41-3 2.41-5.03 0-2.41-1.33-4.5-3.28-5.62.49-.67.78-1.49.78-2.38 0-2.21-1.79-4-4-4z" stroke="#000" stroke-width="1.5" stroke-linecap="round"/></g>""", # noqa: E501
  "q": """<g id="black-queen" class="black queen" fill="#000" fill-rule="evenodd" stroke="#000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><g fill="#000" stroke="none"><circle cx="6" cy="12" r="2.75"/><circle cx="14" cy="9" r="2.75"/><circle cx="22.5" cy="8" r="2.75"/><circle cx="31" cy="9" r="2.75"/><circle cx="39" cy="12" r="2.75"/></g><path d="M9 26c8.5-1.5 21-1.5 27 0l2.5-12.5L31 25l-.3-14.1-5.2 13.6-3-14.5-3 14.5-5.2-13.6L14 25 6.5 13.5 9 26zM9 26c0 2 1.5 2 2.5 4 1 1.5 1 1 .5 3.5-1.5 1-1.5 2.5-1.5 2.5-1.5 1.5.5 2.5.5 2.5 6.5 1 16.5 1 23 0 0 0 1.5-1 0-2.5 0 0 .5-1.5-1-2.5-.5-2.5-.5-2 .5-3.5 1-2 2.5-2 2.5-4-8.5-1.5-18.5-1.5-27 0z" stroke-linecap="butt"/><path d="M11 38.5a35 35 1 0 0 23 0" fill="none" stroke-linecap="butt"/><path d="M11 29a35 35 1 0 1 23 0M12.5 31.5h20M11.5 34.5a35 35 1 0 0 22 0M10.5 37.5a35 35 1 0 0 24 0" fill="none" stroke="#fff"/></g>""", # noqa: E501
  "r": """<g id="black-rook" class="black rook" fill="#000" fill-rule="evenodd" stroke="#000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 39h27v-3H9v3zM12.5 32l1.5-2.5h17l1.5 2.5h-20zM12 36v-4h21v4H12z" stroke-linecap="butt"/><path d="M14 29.5v-13h17v13H14z" stroke-linecap="butt" stroke-linejoin="miter"/><path d="M14 16.5L11 14h23l-3 2.5H14zM11 14V9h4v2h5V9h5v2h5V9h4v5H11z" stroke-linecap="butt"/><path d="M12 35.5h21M13 31.5h19M14 29.5h17M14 16.5h17M11 14h23" fill="none" stroke="#fff" stroke-width="1" stroke-linejoin="miter"/></g>""", # noqa: E501
  "B": """<g id="white-bishop" class="white bishop" fill="none" fill-rule="evenodd" stroke="#000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><g fill="#fff" stroke-linecap="butt"><path d="M9 36c3.39-.97 10.11.43 13.5-2 3.39 2.43 10.11 1.03 13.5 2 0 0 1.65.54 3 2-.68.97-1.65.99-3 .5-3.39-.97-10.11.46-13.5-1-3.39 1.46-10.11.03-13.5 1-1.354.49-2.323.47-3-.5 1.354-1.94 3-2 3-2zM15 32c2.5 2.5 12.5 2.5 15 0 .5-1.5 0-2 0-2 0-2.5-2.5-4-2.5-4 5.5-1.5 6-11.5-5-15.5-11 4-10.5 14-5 15.5 0 0-2.5 1.5-2.5 4 0 0-.5.5 0 2zM25 8a2.5 2.5 0 1 1-5 0 2.5 2.5 0 1 1 5 0z"/></g><path d="M17.5 26h10M15 30h15m-7.5-14.5v5M20 18h5" stroke-linejoin="miter"/></g>""", # noqa: E501
  "K": """<g id="white-king" class="white king" fill="none" fill-rule="evenodd" stroke="#000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22.5 11.63V6M20 8h5" stroke-linejoin="miter"/><path d="M22.5 25s4.5-7.5 3-10.5c0 0-1-2.5-3-2.5s-3 2.5-3 2.5c-1.5 3 3 10.5 3 10.5" fill="#fff" stroke-linecap="butt" stroke-linejoin="miter"/><path d="M11.5 37c5.5 3.5 15.5 3.5 21 0v-7s9-4.5 6-10.5c-4-6.5-13.5-3.5-16 4V27v-3.5c-3.5-7.5-13-10.5-16-4-3 6 5 10 5 10V37z" fill="#fff"/><path d="M11.5 30c5.5-3 15.5-3 21 0m-21 3.5c5.5-3 15.5-3 21 0m-21 3.5c5.5-3 15.5-3 21 0"/></g>""", # noqa: E501
  "N": """<g id="white-knight" class="white knight" fill="none" fill-rule="evenodd" stroke="#000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M 22,10 C 32.5,11 38.5,18 38,39 L 15,39 C 15,30 25,32.5 23,18" style="fill:#ffffff; stroke:#000000;"/><path d="M 24,18 C 24.38,20.91 18.45,25.37 16,27 C 13,29 13.18,31.34 11,31 C 9.958,30.06 12.41,27.96 11,28 C 10,28 11.19,29.23 10,30 C 9,30 5.997,31 6,26 C 6,24 12,14 12,14 C 12,14 13.89,12.1 14,10.5 C 13.27,9.506 13.5,8.5 13.5,7.5 C 14.5,6.5 16.5,10 16.5,10 L 18.5,10 C 18.5,10 19.28,8.008 21,7 C 22,7 22,10 22,10" style="fill:#ffffff; stroke:#000000;"/><path d="M 9.5 25.5 A 0.5 0.5 0 1 1 8.5,25.5 A 0.5 0.5 0 1 1 9.5 25.5 z" style="fill:#000000; stroke:#000000;"/><path d="M 15 15.5 A 0.5 1.5 0 1 1 14,15.5 A 0.5 1.5 0 1 1 15 15.5 z" transform="matrix(0.866,0.5,-0.5,0.866,9.693,-5.173)" style="fill:#000000; stroke:#000000;"/></g>""", # noqa: E501
  "P": """<g id="white-pawn" class="white pawn"><path d="M22 9c-2.21 0-4 1.79-4 4 0 .89.29 1.71.78 2.38-1.95 1.12-3.28 3.21-3.28 5.62 0 2.03.94 3.84 2.41 5.03-3 1.06-7.41 5.55-7.41 13.47h23c0-7.92-4.41-12.41-7.41-13.47 1.47-1.19 2.41-3 2.41-5.03 0-2.41-1.33-4.5-3.28-5.62.49-.67.78-1.49.78-2.38 0-2.21-1.79-4-4-4z" fill="#fff" stroke="#000" stroke-width="1.5" stroke-linecap="round"/></g>""", # noqa: E501
  "Q": """<g id="white-queen" class="white queen" fill="#fff" fill-rule="evenodd" stroke="#000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M8 12a2 2 0 1 1-4 0 2 2 0 1 1 4 0zM24.5 7.5a2 2 0 1 1-4 0 2 2 0 1 1 4 0zM41 12a2 2 0 1 1-4 0 2 2 0 1 1 4 0zM16 8.5a2 2 0 1 1-4 0 2 2 0 1 1 4 0zM33 9a2 2 0 1 1-4 0 2 2 0 1 1 4 0z"/><path d="M9 26c8.5-1.5 21-1.5 27 0l2-12-7 11V11l-5.5 13.5-3-15-3 15-5.5-14V25L7 14l2 12zM9 26c0 2 1.5 2 2.5 4 1 1.5 1 1 .5 3.5-1.5 1-1.5 2.5-1.5 2.5-1.5 1.5.5 2.5.5 2.5 6.5 1 16.5 1 23 0 0 0 1.5-1 0-2.5 0 0 .5-1.5-1-2.5-.5-2.5-.5-2 .5-3.5 1-2 2.5-2 2.5-4-8.5-1.5-18.5-1.5-27 0z" stroke-linecap="butt"/><path d="M11.5 30c3.5-1 18.5-1 22 0M12 33.5c6-1 15-1 21 0" fill="none"/></g>""", # noqa: E501
  "R": """<g id="white-rook" class="white rook" fill="#fff" fill-rule="evenodd" stroke="#000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 39h27v-3H9v3zM12 36v-4h21v4H12zM11 14V9h4v2h5V9h5v2h5V9h4v5" stroke-linecap="butt"/><path d="M34 14l-3 3H14l-3-3"/><path d="M31 17v12.5H14V17" stroke-linecap="butt" stroke-linejoin="miter"/><path d="M31 29.5l1.5 2.5h-20l1.5-2.5"/><path d="M11 14h23" fill="none" stroke-linejoin="miter"/></g>""", # noqa: E501
}
for symbol, v in PIECES_G.items():
  if symbol.isupper():
    symbol += 'w' # case insensitive filesystems hm.
  else:
    symbol += 'b'
  with open(f'{symbol}.svg', 'w') as f:
    f.write(f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">{v}</svg>')

class ChessBoardScene(QGraphicsScene):

  def render(self, board: Optional[chess.BaseBoard] = None):
    self.clear()
    orientation = True
    margin = 5

    # Render board.
    for square, bb in enumerate(chess.BB_SQUARES):
      file_index = chess.square_file(square)
      rank_index = chess.square_rank(square)
      x = (file_index if orientation else 7 - file_index) * SQUARE_SIZE + margin
      y = (7 - rank_index if orientation else rank_index) * SQUARE_SIZE + margin
      color = "#eeeeee" if chess.BB_LIGHT_SQUARES & bb else "#333333"
      self.addRect(
        QRectF(x, y, SQUARE_SIZE, SQUARE_SIZE),
        brush=QBrush(QColor(color))
      )
    # Render pieces
    for square, bb in enumerate(chess.BB_SQUARES):
      file_index = chess.square_file(square)
      rank_index = chess.square_rank(square)
      x = (file_index if orientation else 7 - file_index) * SQUARE_SIZE + margin
      y = (7 - rank_index if orientation else rank_index) * SQUARE_SIZE + margin
      piece = board.piece_at(square)
      if piece:
        p = chess.Piece(piece.piece_type, piece.color)
        symbol = p.symbol()
        if symbol.isupper():
          symbol += 'w' # case insensitive filesystems hm.
        else:
          symbol += 'b'
        svgo = QGraphicsSvgItem(f'{symbol}.svg')
        self.addItem(svgo)
        svgo.setPos(QPointF(x, y))


class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.moves = ['e4', 'e5', 'Qh5', 'Nc6', 'Bc4', 'Nf6', 'Qxf7']
    self.board = chess.Board()
    self.scene = ChessBoardScene()
    self.viewer = QGraphicsView()
    self.setCentralWidget(self.viewer)
    self.viewer.setScene(self.scene)
    self.timer = QTimer()
    self.timer.timeout.connect(self.next_move)
    self.timer.setInterval(1000)
    self.timer.start()
  def next_move(self):
    if self.moves:
      move = self.moves.pop(0)
      print(move)
      self.board.push_san(move)
      self.scene.render(self.board)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

```

This only includes the squares and the moves ( not the arrows, etc.) but should be clear-ish.
martin | 2021-05-20 19:07:23 UTC | #18
By clipping do you mean the selection isn't correctly getting the right item? It's the item view box on the SVG items, should be reduced to the size of the square e.g.
python ```
file.write(f"""<svg viewBox="0 0 {SQUARE_SIZE} {SQUARE_SIZE}" xmlns="http://www.w3.org/2000/svg">{v}</svg>""")

```

Edit: ah I see you mean the drop-centering to the square, will take a look.
PedanticHacker | 2021-05-20 19:17:07 UTC | #19
[quote="martin, post:18, topic:831"] Edit: ah I see you mean the drop-centering to the square, will take a look. [/quote]
Yes, I ment exactly that. :slight_smile:
martin | 2021-05-20 21:13:11 UTC | #20
You can do this on a subclass of `QGraphicsSvgItem` by overriding the `mouseReleaseEvent` e.g.
python ```

class ChessPiece(QGraphicsSvgItem):
  def mouseReleaseEvent(self, e):
    super().mouseReleaseEvent(e) # let default drop occur before snapping.
    half_sq = SQUARE_SIZE // 2 # offset half a square, to snap the center point
    x = self.x() + half_sq
    y = self.y() + half_sq
    x = (x // SQUARE_SIZE) * SQUARE_SIZE
    y = (y // SQUARE_SIZE) * SQUARE_SIZE
    self.prepareGeometryChange()
    self.setPos(QPointF(x, y))

```

...you can _also_ do snapping on `itemChange` but then it will snap as you drag it, which is not very nice for moving pieces on a chess board.
PedanticHacker | 2021-05-21 13:46:23 UTC | #22
Now after implementing your wonderful solution for piece-to-center-square snapping, the final code is...
python ```
import sys
import chess
import chess.svg
from PyQt5.QtGui import QBrush
from PyQt5.QtSvg import QGraphicsSvgItem
from PyQt5.QtCore import QPointF, QRectF, Qt
from PyQt5.QtWidgets import (
  QApplication, QGraphicsScene, QGraphicsView, QMainWindow)

MARGIN = 0
SQUARE_SIZE = 45
HALF_SQUARE_SIZE = SQUARE_SIZE // 2

class Piece(QGraphicsSvgItem):
  def mouseReleaseEvent(self, event):
    super().mouseReleaseEvent(event)
    x_offset = self.x() + HALF_SQUARE_SIZE
    y_offset = self.y() + HALF_SQUARE_SIZE
    x = (x_offset // SQUARE_SIZE) * SQUARE_SIZE
    y = (y_offset // SQUARE_SIZE) * SQUARE_SIZE
    new_position = QPointF(x, y)
    self.setPos(new_position)

class Chessboard(QGraphicsScene):
  def render(self, board):
    orientation = True
    # Render squares.
    for square, bitboard in enumerate(chess.BB_SQUARES):
      file = chess.square_file(square)
      rank = chess.square_rank(square)
      x = (file if orientation else 7 - file) * SQUARE_SIZE + MARGIN
      y = (7 - rank if orientation else rank) * SQUARE_SIZE + MARGIN
      square_color = (
        Qt.GlobalColor.yellow if chess.BB_LIGHT_SQUARES & bitboard
        else Qt.GlobalColor.blue)
      self.addRect(
        QRectF(x, y, SQUARE_SIZE, SQUARE_SIZE),
        brush=QBrush(square_color))
    # Render pieces on squares.
    for square in chess.SQUARES:
      file = chess.square_file(square)
      rank = chess.square_rank(square)
      x = (file if orientation else 7 - file) * SQUARE_SIZE + MARGIN
      y = (7 - rank if orientation else rank) * SQUARE_SIZE + MARGIN
      piece = board.piece_at(square)
      if piece is not None:
        piece_symbol = piece.symbol()
        filename = (
          piece_symbol + "-white.svg" if piece_symbol.isupper()
          else piece_symbol + "-black.svg")
        item = Piece(f"{filename}")
        item.setFlag(QGraphicsSvgItem.GraphicsItemFlag.ItemIsMovable)
        item.setPos(QPointF(x, y))
        self.addItem(item)

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.board = chess.Board()
    self.scene = Chessboard()
    self.viewer = QGraphicsView()
    self.setCentralWidget(self.viewer)
    self.viewer.setScene(self.scene)
    self.scene.render(self.board)

if __name__ == "__main__":
  app_instance = QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  app_instance.exec()

```

I named my Python file (containing this code) as `test.py` and put all those SVG files (`p-black.svg`, `N-white.svg`, etc.) in the same directory/folder as `test.py`. It works beautifully!
EDIT: I think that the method `prepareGeometryChange()` (called in the `mouseReleaseEvent` reimplementation) is not needed to be called, since we don't change the **size** of an item's `boundingRect`, we just change its **position**. Hence, I removed that `prepareGeometryChange()` method call. It still works correctly without it.
PedanticHacker | 2021-05-23 00:59:28 UTC | #24
[quote="martin, post:7, topic:831"] I had to keep with PyQt5 – using PyQt6 I was seeing some weird visual distortion when moving the pieces (clipping errors). [/quote]
I solved this problem! :slight_smile:
All you need to do is to put `self.changed.connect(self.update)` in the `__init__` of a `QGraphicsScene` subclass. The rendering is then done with no visual artifacts. I've discovered this on my own, completely by sheer luck.
PedanticHacker | 2021-05-27 14:14:43 UTC | #25
@martin, I now only have one nasty issue to fix. If I mouse-drag a chess piece outside the scene's bounding rect, the view scrolls the viewport. I don't want that.
How can I have a mouse-drag to be constrained within the scene's bounding rect (so that the view doesn't scroll the viewport)?
I also wasn't able to somehow disable the view from ever scrolling the viewport. Can't be done. Please help!
martin | 2021-05-28 09:25:03 UTC | #26
You can set the size of the scene using `.setSceneRect` I think that should constrain it and prevent it scrolling.
PedanticHacker | 2021-05-28 10:33:49 UTC | #27
I tried constraining the `QGraphicsView`'s viewport from scrolling by calling `self.setSceneRect(self.sceneRect())` in the `__init__()` of my `QGraphicsScene()` subclass. This didn't do the trick. Scrolling the `QGraphicsView`'s viewport is apparently so tightly embedded into `Qt`'s `Graphics View Framework` that I'm really starting to think it can't be done. I tried all sorts of tricks from forums like this, but none of those "tricks" worked, or my application crashed when doing something crazy.
My main problem is that the user of my application is able to, currently, drop a chess piece outside the scene's bounding rect, and hence the application crashes immediately, because chessboard coordinates are, of course, not defined outside of it.
martin | 2021-06-23 07:37:16 UTC | #28
Somehow I managed it in my Solitaire app [source here](https://github.com/learnpyqt/15-minute-apps/blob/master/solitaire/solitaire.py). I thought it was just the sceneRect, but I also fix the window size (seems weird that would be related).
Aside from that you can also constrain the positions when snapping in the squares (min/max for the board dimensions), that'll avoid the crash at least.
PedanticHacker | 2021-06-23 07:37:11 UTC | #29
@martin, you, my friend, are absolutely amazing! Yes, your approach in the Solitaire source code solved my problem. :+1:
Now the view doesn't scroll its viewport even if a chess piece is dragged outside the scene (the dragged chess piece is obscured). And if a chess piece is dropped outside the scene, I catch the appropriate exception (that is raised by the python-chess library) and ignore it, and redraw the chessboard, which basically puts the dragged chess piece back as it was before entering the drag operation. All is good.
To refine the user experience, I am wondering whether dragging a chess piece can be constrained to inside the scene's rect only, because now a chess piece (when leaving the scene's rect) is obscured. Is that something that can be done, i.e., to lock the movement of the mouse-drag operation within the bounds of the scene's rect?
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**How to drag &drop SVG elements?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/how-to-drag-drop-svg-elements/Python books) on the subject. 
**How to drag &drop SVG elements?** was published in [faq](https://www.pythonguis.com/faq/) on March 29, 2021 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
