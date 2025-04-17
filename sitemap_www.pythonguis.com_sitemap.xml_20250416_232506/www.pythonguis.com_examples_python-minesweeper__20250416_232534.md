# Content from: https://www.pythonguis.com/examples/python-minesweeper/

[](https://www.pythonguis.com/examples/python-minesweeper/#menu)
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
# Moonsweeper
Explore the mysterious moon of Q'tee without getting too close to the alien natives!
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ Example applications ](https://www.pythonguis.com/examples/)
[ Source Code ](https://www.pythonguis.com/d/minesweeper.zip) [ Ubuntu Installer ](https://www.pythonguis.com/d/Moonsweeper.deb) [ Windows Installer ](https://www.pythonguis.com/d/MoonsweeperSetup.exe) [ Mac Disk Image ](https://www.pythonguis.com/d/Moonsweeper.dmg)
Moonsweeper is a single-player puzzle video game. The objective of the game is to explore the area around your landed space rocket, without coming too close to the deadly B'ug aliens. Your trusty tricounter will tell you the number of B'ugs in the vicinity.
This a simple single-player exploration game modelled on _Minesweeper_ where you must reveal all the tiles without hitting hidden mines. This implementation uses custom `QWidget` objects for the tiles, which individually hold their state as mines, status and the adjacent count of mines. In this version, the mines are replaced with alien bugs (B'ug) but they could just as easily be anything else.
Installers for Windows, Linux and Mac are available to download above, along with the complete source code.
## Running from source
Download the source archive, or check it out from Github [here](https://github.com/mfitzp/15-minute-apps/tree/master/minesweeper). Install requirements using:
python ```
pip3 install -r requirements.txt

```

You can then run _Moonsweeper_ with:
python ```
python3 minesweeper.py

```

Read on for a walkthrough of how the code works. The code is compatible with PyQt5 or PySide2 (Qt for Python), the only thing that changes is the imports and signal signature (see later).
  * PyQt5
  * PySide2


python ```
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

```

python ```
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

```

## Playing Field
The playing area for Moonsweeper is a NxN grid, containing a set number of mines. The dimensions and mine counts we'll used are taken from the default values for the Windows version of Minesweeper. The values used are shown in the table below: 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Level | Dimensions | Number of Mines  
---|---|---  
Easy | 8 x 8 | 10  
Medium | 16 x 16 | 40  
Hard | 24 x 24 | 99  
We store these values as a constant `LEVELS` defined at the top of the file. Since all the playing fields are square we only need to store the value once (8, 16 or 24).
python ```
LEVELS = [
  ("Easy", 8, 10),
  ("Medium", 16, 40),
  ("Hard", 24, 99)
]

```

The playing grid could be represented in a number of ways, including for example a 2D 'list of lists' representing the different states of the playing positions (mine, revealed, flagged).
However, this implementation uses an object-orientated approach. Individual squares on the map hold all relevant data about their current state and are also responsible for drawing themselves. In Qt we can do this simply by subclassing from `QWidget` and then implementing a custom paint function.
Since our tile objects are subclassing from `QWidget` we can lay them out like any other widget. We do this, by setting up a `QGridLayout`.
python ```
    self.grid = QGridLayout()
    self.grid.setSpacing(5)
    self.grid.setSizeConstraint(QLayout.SetFixedSize)

```

We can set up the playing around by creating our position tile widgets and adding them our grid. The initial setup for the level reads from `LEVELS` and assigns a number of variables to the window. The window title and mine counter are updated, and then the setup of the grid starts.
python ```
  def set_level(self, level):
    self.level_name, self.b_size, self.n_mines = LEVELS[level]
    self.setWindowTitle("Moonsweeper - %s" % (self.level_name))
    self.mines.setText("%03d" % self.n_mines)
    self.clear_map()
    self.init_map()
    self.reset_map()

```

The setup functions will be covered next.
The `Pos` class represents a tile, and holds all the relevant information for its relevant position in the map — including, for example, whether it is a mine, revealed, flagged and the number of mines in the immediate vicinity.
Each `Pos` object also has 3 custom signals _clicked_ , _revealed_ and _expandable_ which we connect to custom slosts. Finally, we call resize to adjust the size of the window to the new contents. This is actually only necessary when the window _shrinks_ — Qt will grow it automatically.
python ```
  def init_map(self):
    # Add positions to the map
    for x in range(0, self.b_size):
      for y in range(0, self.b_size):
        w = Pos(x,y)
        self.grid.addWidget(w, y, x)
        # Connect signal to handle expansion.
        w.clicked.connect(self.trigger_start)
        w.revealed.connect(self.on_reveal)
        w.expandable.connect(self.expand_reveal)
    # Place resize on the event queue, giving control back to Qt before.
    QTimer.singleShot(0, lambda: self.resize(1,1)) # <1>

```

  1. The `singleShot` timer is required to ensure the resize runs after we've returned to the event loop and Qt is aware of the new contents.


Now we have our grid of positional tile objects in place, we can begin creating the initial conditions of the playing board. This is broken down into a number of functions. We name them `_reset` (the leading underscore is a convention to indicate a private function, not intended for external use). The main function `reset_map` calls these functions in turn to set it up.
The process is as follows —
  1. Remove all mines (and reset data) from the field.
  2. Add new mines to the field.
  3. Calculate the number of mines adjacent to each position.
  4. Add a starting marker (the rocket) and trigger initial exploration.
  5. Reset the timer.


The code to do this:
python ```
  def reset_map(self):
    self._reset_position_data()
    self._reset_add_mines()
    self._reset_calculate_adjacency()
    self._reset_add_starting_marker()
    self.update_timer()

```

The separate steps from 1-5 are described in detail in turn below, with the code for each step.
The first step is to reset the data for each position on the map. We iterate through every position on the board, calling `.reset()` on the widget at each point. The code for the `.reset()` function is defined on our custom `Pos` class, we'll explore in detail later. For now it's enough to know it clears mines, flags and sets the position back to being unrevealed.
python ```
  def _reset_position_data(self):
    # Clear all mine positions
    for x in range(0, self.b_size):
      for y in range(0, self.b_size):
        w = self.grid.itemAtPosition(y, x).widget()
        w.reset()

```

Now all the positions are blank, we can begin the process of adding mines to the map. The maximum number of mines `n_mines` is defined by the level settings, described earlier.
python ```
  def _reset_add_mines(self):
    # Add mine positions
    positions = []
    while len(positions) < self.n_mines:
      x, y = random.randint(0, self.b_size-1), random.randint(0, self.b_size-1)
      if (x ,y) not in positions:
        w = self.grid.itemAtPosition(y,x).widget()
        w.is_mine = True
        positions.append((x, y))
    # Calculate end-game condition
    self.end_game_n = (self.b_size * self.b_size) - (self.n_mines + 1)
    return positions

```

With mines in position, we can now calculate the 'adjacency' number for each position — simply the number of mines in the immediate vicinity, using a 3x3 grid around the given point. The custom function `get_surrounding` simply returns those positions around a given `x` and `y` location. We count the number of these that is a mine `is_mine == True` and store.
Pre-calculating the adjacent counts here helps simplify the reveal logic later. But it means we can't allow the user to choose their initial move — we can explain this away as the "initial exploration around the rocket" and make it sound completely sensible.
Try and solve this yourself by postponing the calculation!
python ```
  def _reset_calculate_adjacency(self):
    def get_adjacency_n(x, y):
      positions = self.get_surrounding(x, y)
      return sum(1 for w in positions if w.is_mine)
    # Add adjacencies to the positions
    for x in range(0, self.b_size):
      for y in range(0, self.b_size):
        w = self.grid.itemAtPosition(y, x).widget()
        w.adjacent_n = get_adjacency_n(x, y)

```

A starting marker is used to ensure that the first move is _always_ valid. This is implemented as a _brute force_ search through the grid space, effectively trying random positions until we find a position which is not a mine. Since we don't know how many attempts this will take, we need to wrap it in an continuous loop.
Once that location is found, we mark it as the start location and then trigger the exploration of all surrounding positions. We break out of the loop, and reset the ready status.
python ```
  def _reset_add_starting_marker(self):
    # Place starting marker.
    # Set initial status (needed for .click to function)
    self.update_status(STATUS_READY)
    while True:
      x, y = random.randint(0, self.b_size - 1), random.randint(0, self.b_size - 1)
      w = self.grid.itemAtPosition(y, x).widget()
      # We don't want to start on a mine.
      if not w.is_mine:
        w.is_start = True
        w.is_revealed = True
        w.update()
        # Reveal all positions around this, if they are not mines either.
        for w in self.get_surrounding(x, y):
          if not w.is_mine:
            w.click()
        break
    # Reset status to ready following initial clicks.
    self.update_status(STATUS_READY)

```

![Initial starting state for Moonsweeper](https://www.pythonguis.com/static/examples/moonsweeper/minesweeper-start.png) _Initial starting state for Moonsweeper_
## Position Tiles
The game is structure game so that individual tile positions hold their own state information. This means that `Pos` tiles are able to handle their own game logic.
Since the `Pos` class is relatively complex, it is broken down here to a few parts, which are discussed in turn. The initial setup `__init__` block is simple, accepting an `x` and `y` position and storing it on the object. `Pos` positions never change once created.
To complete setup the `.reset()` function is called which resets all object attributes back to default, zero values. This flags the mine as _not the start position_ , _not a mine_ , _not revealed_ and _not flagged_. We also reset the adjacent count.
  * PyQt5
  * PySide2


python ```
class Pos(QWidget):
  expandable = pyqtSignal(int,int)
  revealed = pyqtSignal(object)
  clicked = pyqtSignal()
  def __init__(self, x, y, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setFixedSize(QSize(20, 20))
    self.x = x
    self.y = y
    self.reset()
  def reset(self):
    self.is_start = False
    self.is_mine = False
    self.adjacent_n = 0
    self.is_revealed = False
    self.is_flagged = False
    self.update()

```

python ```
class Pos(QWidget):
  expandable = pyqtSignal(int,int)
  revealed = pyqtSignal(object)
  clicked = pyqtSignal()
  def __init__(self, x, y, *args, **kwargs):
    super(Pos, self).__init__(*args, **kwargs)
    self.setFixedSize(QSize(20, 20))
    self.x = x
    self.y = y
    self.reset()
  def reset(self):
    self.is_start = False
    self.is_mine = False
    self.adjacent_n = 0
    self.is_revealed = False
    self.is_flagged = False
    self.update()

```

Gameplay is centered around mouse interactions with the tiles in the playfield, so detecting and reacting to mouse clicks is central. In Qt we catch mouse clicks by detecting the `mouseReleaseEvent`. To do this for our custom `Pos` widget we define a handler on the class. This receives `QMouseEvent` with the information containing what happened. In this case we are only interested in whether the mouse release occurred from the left or the right mouse button.
For a left mouse click we check whether the tile is flagged or already revealed. If it is either, we ignore the click — making flagged tiles 'safe', unable to be click by accident. If the tile is not flagged we simply initiation the `.click()` method (see later).
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt5](https://www.pythonguis.com/static/theme/images/products/pyqt5-book.png)](https://www.pythonguis.com/pyqt5-book/)
[Take a look ](https://www.pythonguis.com/pyqt5-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/create-simple-gui-applications/) and [Amazon Paperback](https://www.amazon.com/dp/B08RB2HRS1/)
For a right mouse click, on tiles which are _not_ revealed, we call our `.toggle_flag()` method to toggle a flag on and off.
python ```
  def mouseReleaseEvent(self, e):
    if (e.button() == Qt.RightButton and not self.is_revealed):
      self.toggle_flag()
    elif (e.button() == Qt.LeftButton):
      # Block clicking on flagged mines.
      if not self.is_flagged and not self.is_revealed:
        self.click()

```

The methods called by the `mouseReleaseEvent` handler are defined below.
The `.toggle_flag` handler simply sets `.is_flagged` to the inverse of itself (`True` becomes `False`, `False` becomes `True`) having the effect of toggling it on and off. Note that we have to call `.update()` to force a redraw having changed the state. We also emit our custom `.clicked` signal, which is used to start the timer — because placing a flag should also count as starting, not just revealing a square.
The `.click()` method handles a left mouse click, and in turn triggers the reveal of the square. If the number of adjacent mines to this `Pos` is zero, we trigger the `.expandable` signal to begin the process of auto-expanding the region explored (see later). Finally, we again emit `.clicked` to signal the start of the game.
Finally, the `.reveal()` method checks whether the tile is already revealed, and if not sets `.is_revealed` to `True`. Again we call `.update()` to trigger a repaint of the widget.
The optional emit of the `.revealed` signal is used only for the endgame full-map reveal. Because each reveal triggers a further lookup to find what tiles are also revealable, revealing the entire map would create a large number of redundant callbacks. By suppressing the signal here we avoid that.
python ```
  def toggle_flag(self):
    self.is_flagged = not self.is_flagged
    self.update()
    self.clicked.emit()
  def click(self):
    self.reveal()
    if self.adjacent_n == 0:
      self.expandable.emit(self.x, self.y)
    self.clicked.emit()
  def reveal(self, emit=True):
    if not self.is_revealed:
      self.is_revealed = True
      self.update()
      if emit:
        self.revealed.emit(self)

```

Finally, we define a custom `paintEvent` method for our `Pos` widget to handle the display of the current position state. To perform custom paint over a widget canvas we take a `QPainter` and the `event.rect()` which provides the boundaries in which we are to draw — in this case the outer border of the `Pos` widget.
Revealed tiles are drawn differently depending on whether the tile is a _start position_ , _bomb_ or _empty space_. The first two are represented by icons of a rocket and bomb respectively. These are drawn into the tile `QRect` using `.drawPixmap`. Note we need to convert the `QImage` constants to pixmaps, by passing through `QPixmap` by passing.
You might think "why not just store these as `QPixmap` objects since that's what we're using? Unfortunately you can't create `QPixmap` objects before your `QApplication` is up and running.
For empty positions (not rockets, not bombs) we optionally show the adjacency number if it is larger than zero. To draw text onto our `QPainter` we use `.drawText()` passing in the `QRect`, alignment flags and the number to draw as a string. We've defined a standard color for each number (stored in `NUM_COLORS`) for usability.
For tiles that are _not_ revealed we draw a tile, by filling a rectangle with light gray and draw a 1 pixel border of darker grey. If `.is_flagged` is set, we also draw a flag icon over the top of the tile using `drawPixmap` and the tile `QRect`.
python ```
  def paintEvent(self, event):
    p = QPainter(self)
    p.setRenderHint(QPainter.Antialiasing)
    r = event.rect()
    if self.is_revealed:
      if self.is_start:
        p.drawPixmap(r, QPixmap(IMG_START))
      elif self.is_mine:
        p.drawPixmap(r, QPixmap(IMG_BOMB))
      elif self.adjacent_n > 0:
        pen = QPen(NUM_COLORS[self.adjacent_n])
        p.setPen(pen)
        f = p.font()
        f.setBold(True)
        p.setFont(f)
        p.drawText(r, Qt.AlignHCenter | Qt.AlignVCenter, str(self.adjacent_n))
    else:
      p.fillRect(r, QBrush(Qt.lightGray))
      pen = QPen(Qt.gray)
      pen.setWidth(1)
      p.setPen(pen)
      p.drawRect(r)
      if self.is_flagged:
        p.drawPixmap(r, QPixmap(IMG_FLAG))

```

## Mechanics
We commonly need to get all tiles surrounding a given point, so we have a custom function for that purpose. It simple iterates across a 3x3 grid around the point, with a check to ensure we do not go out of bounds on the grid edges (`0 ≥ x ≤ self.b_size`). The returned list contains a `Pos` widget from each surrounding location.
python ```
  def get_surrounding(self, x, y):
    positions = []
    for xi in range(max(0, x - 1), min(x + 2, self.b_size)):
      for yi in range(max(0, y - 1), min(y + 2, self.b_size)):
        if not (xi == x and yi == y):
          positions.append( self.grid.itemAtPosition(yi, xi).widget() )
    return positions

```

The `expand_reveal` method is triggered in response to a click on a tile with zero adjacent mines. In this case we want to expand the area around the click to any spaces which also have zero adjacent mines, and also reveal any squares around the border of that expanded area (which aren't mines).
We start with a list `to_expand` containing the positions to check on the next iteration, a list `to_reveal` containing the tile widgets to reveal, and a flag `any_added` to determine when to exit the loop. The loop stops the first time no new widgets are added to `to_reveal`.
Inside the loop we reset `any_added` to `False`, and empty the `to_expand` list, keeping a temporary store in `l` for iterating over.
For each `x` and `y` location we get the 8 surrounding widgets. If any of these widgets is not a mine, and is not already in the `to_reveal` list we add it. This ensures that the edges of the expanded area are all revealed. If the position has no adjacent mines, we append the coordinates onto `to_expand` to be checked on the next iteration.
By adding any non-mine tiles to `to_reveal`, and only expanding tiles that are not already in `to_reveal`, we ensure that we won't visit a tile more than once.
python ```
  def expand_reveal(self, x, y):
    """
    Iterate outwards from the initial point, adding new locations to the
    queue. This allows us to expand all in a single go, rather than
    relying on multiple callbacks.
    """
    to_expand = [(x,y)]
    to_reveal = []
    any_added = True
    while any_added:
      any_added = False
      to_expand, l = [], to_expand
      for x, y in l:
        positions = self.get_surrounding(x, y)
        for w in positions:
          if not w.is_mine and w not in to_reveal:
            to_reveal.append(w)
            if w.adjacent_n == 0:
              to_expand.append((w.x,w.y))
              any_added = True
    # Iterate an reveal all the positions we have found.
    for w in to_reveal:
      w.reveal()

```

## Endgames
Endgame states are detected during the reveal process following a click on a title. There are two possible outcomes — 
  1. Tile is a mine, game over.
  2. Tile is not a mine, decrement the `self.end_game_n`.


This continues until `self.end_game_n` reaches zero, which triggers the win game process by calling either `game_over` or `game_won`. Success/failure is triggered by revealing the map and setting the relevant status, in both cases.
python ```
  def on_reveal(self, w):
    if w.is_mine:
      self.game_over()
    else:
      self.end_game_n -= 1 # decrement remaining empty spaces
      if self.end_game_n == 0:
        self.game_won()
  def game_over(self):
    self.reveal_map()
    self.update_status(STATUS_FAILED)
  def game_won(self):
    self.reveal_map()
    self.update_status(STATUS_SUCCESS)

```

![Oh no. Eaten by a B'ug.](https://www.pythonguis.com/static/examples/moonsweeper/minesweeper-lose.png) _Oh no. Eaten by a B'ug._
## Further ideas
If you want to have a go at expanding _Moonsweeper_ , here are a few ideas —
  1. Allow the player to take their own first turn. Try postponing the calculation of mine positions til after the user first clicks, and then generate positions until you get a miss.
  2. Add power-ups, e.g. a scanner to reveal a certain area of the board automatically.
  3. Let the hidden B'ugs move around between each turn. Keep a list of free-unrevealed positions, and allow the B'ugs to move into them. You'll need to recalculate the adjacencies after each click.


If you want a little more inspiration, [see this PR from Keith Hall](https://github.com/mfitzp/15-minute-apps/pull/11) which modifies startup to be selectable, among other things!
The full source is available for download below, along with installers for Windows, Mac and Linux.
For information on packaging and distributing PyQt5 applications [see this section](https://www.pythonguis.com/courses/packaging-and-distribution/).
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Moonsweeper** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/examples/python-minesweeper/Python books) on the subject. 
**Moonsweeper** was published in [examples](https://www.pythonguis.com/examples/) on July 08, 2019 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [minute-apps](https://www.pythonguis.com/topics/minute-apps/) [ games](https://www.pythonguis.com/topics/games/) [minesweeper](https://www.pythonguis.com/topics/minesweeper/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt5-games](https://www.pythonguis.com/topics/pyqt5-games/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
