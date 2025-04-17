# Content from: https://www.pythonguis.com/faq/editing-pyqt-tableview/

[](https://www.pythonguis.com/faq/editing-pyqt-tableview/#menu)
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
# Q&A: How can I enable editing on a QTableView?
Modifying your model to allow editing of your data source
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Jul 19 [ FAQ ](https://www.pythonguis.com/faq/)
In the model views course we covered [Displaying tabular data in Qt5 ModelViews](https://www.pythonguis.com/tutorials/qtableview-modelviews-numpy-pandas/). This takes a data source, for example a `list` of `list` objects, a `numpy` array or a Pandas `DataTable` and displays it in a Qt table view. But often, displaying is just the first step -- you also want your users to be able to add and edit the table, updating the underlying data object.
Reader Vic T asked:
> I have been trying for a few days to get edit mode to work with a QTableView using Pandas for the model via `QAbstractTableModel`. Having searched all over the internet although I found suggestions to implement the `flags()` method but it doesn’t seem to work.
This is correct -- you need to implement the `.flags()` method on your model to inform Qt that your model supports _editing_. To do this your method needs to return the `Qt.ItemIsEditable` flag, which you _or_ together (using the pipe `|` character) with the other flags. For example
python ```
  def flags(self, index):
    return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsEditable

```

But to get the editing working you also need to implement a `.setData` method. This is the model's interface between Qt and your data object and takes care of making the changes to the data.
Remember, Qt model views don't know anything about your data beyond what you tell them via the model. Likewise, they also don't know how to update your `list`, `array` or `DataFrame` objects with the new data that has been input. You need to handle that yourself!
Below are some example `.setData` methods for `list` of `list` data structures, `numpy` and `pandas`. The only difference is how we index into the data object. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
  * list
  * numpy
  * pandas


python ```
  def setData(self, index, value, role):
    if role == Qt.EditRole:
      self._data[index.row()][index.column()] = value
      return True

```

python ```
  def setData(self, index, value, role):
    if role == Qt.EditRole:
      self._data[index.row(), index.column()] = value
      return True

```

python ```
  def setData(self, index, value, role):
    if role == Qt.EditRole:
      self._data.iloc[index.row(),index.column()] = value
      return True

```

Notice that we first need to check the `role` is `Qt.EditRole` to determine if an edit is currently being made. After making the edit, we return `True` to confirm this.
If you try the above on your model, you should be able to edit the values. However, you'll notice that when editing it clears the current value of the cell -- you have to start from an empty cell. To display the current value when editing you need to modify the `.data` method to return the current value when the role is `Qt.EditRole` _as well as_ when it is `Qt.DisplayRole`. For example:
  * list
  * numpy
  * pandas


python ```
  def data(self, index, role=Qt.DisplayRole):
    if index.isValid():
      if role == Qt.DisplayRole or role == Qt.EditRole:
        value = self._data[index.row()][index.column()]
        return str(value)

```

python ```
  def data(self, index, role=Qt.DisplayRole):
    if index.isValid():
      if role == Qt.DisplayRole or role == Qt.EditRole:
        value = self._data[index.row(), index.column()]
        return str(value)

```

python ```
  def data(self, index, role=Qt.DisplayRole):
    if index.isValid():
      if role == Qt.DisplayRole or role == Qt.EditRole:
        value = self._data.iloc[index.row(), index.column()]
        return str(value)

```

That's it, you should now have a properly editable table view.
Below are some complete working examples for `list` data, `numpy` and `Pandas` tables, with PyQt5, PyQt6, PySide2 & PySide6
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
## list of list
The following examples use a nested list of lists as a data source.
  * PyQt5
  * PyQt6
  * PySide2
  * PySide6


python ```
import sys
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView

class PandasModel(QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
  def rowCount(self, index):
    # The length of the outer list.
    return len(self._data)
  def columnCount(self, index):
    # The following takes the first sub-list, and returns
    # the length (only works if all rows are an equal length)
    return len(self._data[0])
  def data(self, index, role=Qt.DisplayRole):
    if index.isValid():
      if role == Qt.DisplayRole or role == Qt.EditRole:
        value = self._data[index.row()][index.column()]
        return str(value)
  def setData(self, index, value, role):
    if role == Qt.EditRole:
      self._data[index.row()][index.column()] = value
      return True
    return False
  def flags(self, index):
    return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.table = QTableView()
    data = [
      [1, 9, 2],
      [1, 0, -1],
      [3, 5, 2],
      [3, 3, 2],
      [5, 8, 9],
    ]
    self.model = PandasModel(data)
    self.table.setModel(self.model)
    self.setCentralWidget(self.table)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

python ```
import sys
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView

class PandasModel(QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
  def rowCount(self, index):
    # The length of the outer list.
    return len(self._data)
  def columnCount(self, index):
    # The following takes the first sub-list, and returns
    # the length (only works if all rows are an equal length)
    return len(self._data[0])
  def data(self, index, role=Qt.DisplayRole):
    if index.isValid():
      if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
        value = self._data[index.row()][index.column()]
        return str(value)
  def setData(self, index, value, role):
    if role == Qt.ItemDataRole.EditRole:
      self._data[index.row()][index.column()] = value
      return True
    return False
  def flags(self, index):
    return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.table = QTableView()
    data = [
      [1, 9, 2],
      [1, 0, -1],
      [3, 5, 2],
      [3, 3, 2],
      [5, 8, 9],
    ]
    self.model = PandasModel(data)
    self.table.setModel(self.model)
    self.setCentralWidget(self.table)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

python ```
import sys
from PySide2.QtCore import QAbstractTableModel, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QTableView

class PandasModel(QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
  def rowCount(self, index):
    # The length of the outer list.
    return len(self._data)
  def columnCount(self, index):
    # The following takes the first sub-list, and returns
    # the length (only works if all rows are an equal length)
    return len(self._data[0])
  def data(self, index, role=Qt.DisplayRole):
    if index.isValid():
      if role == Qt.DisplayRole or role == Qt.EditRole:
        value = self._data[index.row()][index.column()]
        return str(value)
  def setData(self, index, value, role):
    if role == Qt.EditRole:
      self._data[index.row()][index.column()] = value
      return True
    return False
  def flags(self, index):
    return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.table = QTableView()
    data = [
      [1, 9, 2],
      [1, 0, -1],
      [3, 5, 2],
      [3, 3, 2],
      [5, 8, 9],
    ]
    self.model = PandasModel(data)
    self.table.setModel(self.model)
    self.setCentralWidget(self.table)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

python ```
import sys
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

class PandasModel(QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
  def rowCount(self, index):
    # The length of the outer list.
    return len(self._data)
  def columnCount(self, index):
    # The following takes the first sub-list, and returns
    # the length (only works if all rows are an equal length)
    return len(self._data[0])
  def data(self, index, role=Qt.DisplayRole):
    if index.isValid():
      if role == Qt.DisplayRole or role == Qt.EditRole:
        value = self._data[index.row()][index.column()]
        return str(value)
  def setData(self, index, value, role):
    if role == Qt.EditRole:
      self._data[index.row()][index.column()] = value
      return True
    return False
  def flags(self, index):
    return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.table = QTableView()
    data = [
      [1, 9, 2],
      [1, 0, -1],
      [3, 5, 2],
      [3, 3, 2],
      [5, 8, 9],
    ]
    self.model = PandasModel(data)
    self.table.setModel(self.model)
    self.setCentralWidget(self.table)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

## Pandas
The following examples use a Pandas DataFrame, adding column headings from the column names.
  * PyQt5
  * PyQt6
  * PySide2
  * PySide6


python ```
import sys
import pandas as pd
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView

class PandasModel(QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
  def rowCount(self, index):
    return self._data.shape[0]
  def columnCount(self, parnet=None):
    return self._data.shape[1]
  def data(self, index, role=Qt.DisplayRole):
    if index.isValid():
      if role == Qt.DisplayRole or role == Qt.EditRole:
        value = self._data.iloc[index.row(), index.column()]
        return str(value)
  def setData(self, index, value, role):
    if role == Qt.EditRole:
      self._data.iloc[index.row(), index.column()] = value
      return True
    return False
  def headerData(self, col, orientation, role):
    if orientation == Qt.Horizontal and role == Qt.DisplayRole:
      return self._data.columns[col]
  def flags(self, index):
    return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.table = QTableView()
    data = pd.DataFrame([[1, 9, 2], [1, 0, -1], [3, 5, 2], [3, 3, 2], [5, 8, 9],], columns=["A", "B", "C"])
    self.model = PandasModel(data)
    self.table.setModel(self.model)
    self.setCentralWidget(self.table)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

python ```

import sys
import pandas as pd
from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView

class PandasModel(QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
  def rowCount(self, index):
    return self._data.shape[0]
  def columnCount(self, parnet=None):
    return self._data.shape[1]
  def data(self, index, role=Qt.ItemDataRole.DisplayRole):
    if index.isValid():
      if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
        value = self._data.iloc[index.row(), index.column()]
        return str(value)
  def setData(self, index, value, role):
    if role == Qt.ItemDataRole.EditRole:
      self._data.iloc[index.row(), index.column()] = value
      return True
    return False
  def headerData(self, col, orientation, role):
    if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
      return self._data.columns[col]
  def flags(self, index):
    return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.table = QTableView()
    data = pd.DataFrame(
      [[1, 9, 2], [1, 0, -1], [3, 5, 2], [3, 3, 2], [5, 8, 9],], columns=["A", "B", "C"]
    )
    self.model = PandasModel(data)
    self.table.setModel(self.model)
    self.setCentralWidget(self.table)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

python ```

import sys
import pandas as pd
from PySide2.QtCore import QAbstractTableModel, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QTableView

class PandasModel(QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
  def rowCount(self, index):
    return self._data.shape[0]
  def columnCount(self, parnet=None):
    return self._data.shape[1]
  def data(self, index, role=Qt.DisplayRole):
    if index.isValid():
      if role == Qt.DisplayRole or role == Qt.EditRole:
        value = self._data.iloc[index.row(), index.column()]
        return str(value)
  def setData(self, index, value, role):
    if role == Qt.EditRole:
      self._data.iloc[index.row(), index.column()] = value
      return True
    return False
  def headerData(self, col, orientation, role):
    if orientation == Qt.Horizontal and role == Qt.DisplayRole:
      return self._data.columns[col]
  def flags(self, index):
    return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.table = QTableView()
    data = pd.DataFrame(
      [[1, 9, 2], [1, 0, -1], [3, 5, 2], [3, 3, 2], [5, 8, 9],], columns=["A", "B", "C"]
    )
    self.model = PandasModel(data)
    self.table.setModel(self.model)
    self.setCentralWidget(self.table)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

python ```

import sys
import pandas as pd
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

class PandasModel(QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
  def rowCount(self, index):
    return self._data.shape[0]
  def columnCount(self, parnet=None):
    return self._data.shape[1]
  def data(self, index, role=Qt.DisplayRole):
    if index.isValid():
      if role == Qt.DisplayRole or role == Qt.EditRole:
        value = self._data.iloc[index.row(), index.column()]
        return str(value)
  def setData(self, index, value, role):
    if role == Qt.EditRole:
      self._data.iloc[index.row(), index.column()] = value
      return True
    return False
  def headerData(self, col, orientation, role):
    if orientation == Qt.Horizontal and role == Qt.DisplayRole:
      return self._data.columns[col]
  def flags(self, index):
    return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.table = QTableView()
    data = pd.DataFrame(
      [[1, 9, 2], [1, 0, -1], [3, 5, 2], [3, 3, 2], [5, 8, 9],], columns=["A", "B", "C"]
    )
    self.model = PandasModel(data)
    self.table.setModel(self.model)
    self.setCentralWidget(self.table)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

## Numpy
The following examples use a `numpy` array for their data source. The array will only accept valid values (in this case integers) when setting, so we must first coerce the value to an integer before setting it on the error. If you enter something which isn't a valid integer (e.g. _jdskfjdskjfndsf_ ) the `int()` call will throw a `ValueError`, which we catch. By returning `False` when this exception is thrown we cancel the edit.
  * PyQt5
  * PyQt6
  * PySide2
  * PySide6


python ```

import sys
import numpy as np
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView

class PandasModel(QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
  def rowCount(self, index):
    return self._data.shape[0]
  def columnCount(self, index):
    return self._data.shape[1]
  def data(self, index, role=Qt.DisplayRole):
    if index.isValid():
      if role == Qt.DisplayRole or role == Qt.EditRole:
        value = self._data[index.row(), index.column()]
        return str(value)
  def setData(self, index, value, role):
    if role == Qt.EditRole:
      try:
        value = int(value)
      except ValueError:
        return False
      self._data[index.row(), index.column()] = value
      return True
    return False
  def flags(self, index):
    return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.table = QTableView()
    data = np.array([
     [1, 9, 2],
     [1, 0, -1],
     [3, 5, 2],
     [3, 3, 2],
     [5, 8, 9],
    ])
    self.model = PandasModel(data)
    self.table.setModel(self.model)
    self.setCentralWidget(self.table)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

python ```

import sys
import numpy as np
from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView

class PandasModel(QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
  def rowCount(self, index):
    return self._data.shape[0]
  def columnCount(self, index):
    return self._data.shape[1]
  def data(self, index, role=Qt.ItemDataRole.DisplayRole):
    if index.isValid():
      if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
        value = self._data[index.row(), index.column()]
        return str(value)
  def setData(self, index, value, role):
    if role == Qt.EditRole:
      try:
        value = int(value)
      except ValueError:
        return False
      self._data[index.row(), index.column()] = value
      return True
    return False
  def flags(self, index):
    return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.table = QTableView()
    data = np.array([
     [1, 9, 2],
     [1, 0, -1],
     [3, 5, 2],
     [3, 3, 2],
     [5, 8, 9],
    ])
    self.model = PandasModel(data)
    self.table.setModel(self.model)
    self.setCentralWidget(self.table)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

```

python ```

import sys
import numpy as np
from PySide2.QtCore import QAbstractTableModel, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QTableView

class PandasModel(QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
  def rowCount(self, index):
    return self._data.shape[0]
  def columnCount(self, index):
    return self._data.shape[1]
  def data(self, index, role=Qt.DisplayRole):
    if index.isValid():
      if role == Qt.DisplayRole or role == Qt.EditRole:
        value = self._data[index.row(), index.column()]
        return str(value)
  def setData(self, index, value, role):
    if role == Qt.EditRole:
      try:
        value = int(value)
      except ValueError:
        return False
      self._data[index.row(), index.column()] = value
      return True
    return False
  def flags(self, index):
    return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.table = QTableView()
    data = np.array([
     [1, 9, 2],
     [1, 0, -1],
     [3, 5, 2],
     [3, 3, 2],
     [5, 8, 9],
    ])
    self.model = PandasModel(data)
    self.table.setModel(self.model)
    self.setCentralWidget(self.table)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

python ```

import sys
import numpy as np
from PySide6.QtCore import QAbstractTableModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

class PandasModel(QAbstractTableModel):
  def __init__(self, data):
    super().__init__()
    self._data = data
  def rowCount(self, index):
    return self._data.shape[0]
  def columnCount(self, index):
    return self._data.shape[1]
  def data(self, index, role=Qt.DisplayRole):
    if index.isValid():
      if role == Qt.DisplayRole or role == Qt.EditRole:
        value = self._data[index.row(), index.column()]
        return str(value)
  def setData(self, index, value, role):
    if role == Qt.EditRole:
      try:
        value = int(value)
      except ValueError:
        return False
      self._data[index.row(), index.column()] = value
      return True
    return False
  def flags(self, index):
    return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.table = QTableView()
    data = np.array([
     [1, 9, 2],
     [1, 0, -1],
     [3, 5, 2],
     [3, 3, 2],
     [5, 8, 9],
    ])
    self.model = PandasModel(data)
    self.table.setModel(self.model)
    self.setCentralWidget(self.table)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

```

That's all for now! 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Q &A: How can I enable editing on a QTableView?** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/editing-pyqt-tableview/Python books) on the subject. 
**Q &A: How can I enable editing on a QTableView?** was published in [faq](https://www.pythonguis.com/faq/) on July 19, 2021 . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [qtableview](https://www.pythonguis.com/topics/qtableview/) [model-views](https://www.pythonguis.com/topics/model-views/) [editing](https://www.pythonguis.com/topics/editing/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/)
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
