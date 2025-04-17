# Content from: https://www.pythonguis.com/faq/my-pyqt5-application-freezes-when-i-dont-use-partial-function/

[](https://www.pythonguis.com/faq/my-pyqt5-application-freezes-when-i-dont-use-partial-function/#menu)
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
# My pyqt5 application freezes when I don't use partial function
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
jonstakvik10545 | 2021-05-06 11:57:09 UTC | #1
This is my first question asked in this forum
My goal is to create a proof-of-concept code to run a simple dynamic simulator in a Python pyqt5 HMI. I've created a very simple simulator with some setters and getters and I'm using a model-view-controller design pattern. The HMI is fairly simple with a just a few inputs. I'm also using pyqtgraph to plot the simulated results in real-time.
My issue is that my HMI freezes at start up unless I add at least one partial function when I connect my signals to the slots:
python ```
def _connectSignals(self):
  self._view.buttons['u'].clicked.connect(self._on_u_update)
  self._view.buttons['k'].clicked.connect(self._on_k_update)
  self._view.buttons['dt'].clicked.connect(partial(self._on_dt_update, 'dummy')) # Program freeze without at least one partial function. No idea why.
def _on_k_update(self):
  self._model.set_k(float(self._view.lineEdits['k'].text()))
def _on_dt_update(self, dt): # Need to have an input here to avoid program freezing. See connect of dt above
  dt_ = float(self._view.lineEdits['dt'].text())
  dt_ = float(dt_)
  self._model.set_dt(dt_ / 1000.0)
  self.u_line.set_n_samples(seconds=60, dt=dt_ / 1000.0)
  self.x_line.set_n_samples(seconds=60, dt=dt_ / 1000.0)
  self.dt = int(dt_)
  self.timer.setInterval(self.dt)
def _on_u_update(self):
  self._model.set_u(float(self._view.lineEdits['u'].text()))

```

This even happen when I avoid calling my `_connectSignals` function. I suspect that it might have something to do with me using QTimer to control the stepping of the simulator.
There are no error messages, and I'm not able to pause/debug the application. I would greatly appreciate any help on solving this. The entire code is located below:
python ```
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore
from functools import partial
from scipy.integrate import odeint
import pyqtgraph as pg
class POC_Simulator():
  def __init__(self):
    self.u = 0.0
    self.k = 1.0
    self.x = 0.0
    self.dt = 0.050
    self.t = 0.0
  def set_k(self, k):
    self.k = float(k)
  def get_k(self):
    return self.k
  def set_u(self, u):
    self.u = float(u)
  def get_u(self):
    return self.u
  def set_dt(self, dt):
    self.dt = float(dt)
  def get_dt(self):
    return self.dt
  def get_x(self):
    return self.x
  def get_t(self):
    return self.t
  def model(self, x, t):
    dxdt = 1/self.k*(-x + self.u)
    return dxdt
  def step(self):
    t_span = [0, self.dt]
    x = odeint(self.model, self.x, t_span)
    self.x = float(x[1])
    self.t += self.dt
    return self.x, self.t
class GraphLine():
  def __init__(self, graph: pg.PlotWidget, n_samples=100):
    self.graph = graph
    self.x = []
    self.y = []
    self.n_samples = n_samples

  def createPlot(self, color, linetype, name, width):
    if linetype == '-':
      style = QtCore.Qt.SolidLine
    elif linetype == ':':
      style = QtCore.Qt.DotLine
    elif linetype == '--':
      style = QtCore.Qt.DashLine
    else:
      style = QtCore.Qt.SolidLine
    pen = pg.mkPen(color=color)
    self.plt = self.graph.plot(self.x, self.y, pen=pen, style=style, name=name, width=width)
  def updatePlot(self, x, y):
    if len(self.x) >= self.n_samples:
      self.x = self.x[1:]
    self.x.append(x)
    if len(self.y) >= self.n_samples:
      self.y = self.y[1:]
    self.y.append(y)
    self.plt.setData(self.x, self.y)
  def set_n_samples(self, seconds, dt):
    self.n_samples = seconds / dt
class SimulatorUI(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle('POC Simulator UI')
    self.setFixedSize(800, 500)
    self.generalLayout = QHBoxLayout()
    self._centralWidget = QWidget()
    self.setCentralWidget(self._centralWidget)
    self._centralWidget.setLayout(self.generalLayout)
    self._createInputs()
    self._createPlot()
    self.n_samples = 100
  def _createInputs(self):
    layout = QVBoxLayout()
    lines = ('u', 'k', 'dt')
    self.lineEdits = {}
    self.labelValues = {}
    self.buttons = {}
    for name in lines:
      lineLayout = QHBoxLayout()
      lineEdit = QLineEdit('')
      lineLayout.addWidget(QLabel(name))
      lineLayout.addWidget(lineEdit)
      self.lineEdits[name] = lineEdit
      btn = QPushButton(f'Update {name}')
      lineLayout.addWidget(btn)
      self.buttons[name] = btn
      value = QLabel('')
      lineLayout.addWidget(value)
      self.labelValues[name] = value
      layout.addLayout(lineLayout)
    self.generalLayout.addLayout(layout)
  def _createPlot(self):
    self.graphWidget = pg.PlotWidget()
    self.graphWidget.setBackground('w')
    self.graphWidget.addLegend()
    self.graphWidget.showGrid(x=True, y=True)
    self.generalLayout.addWidget(self.graphWidget)
  def addPlot(self, color, name, width=2, linetype='-'):
    line = GraphLine(self.graphWidget)
    line.createPlot(color=color, linetype=linetype, width=width, name=name)
    return line
class POC_Ctrl():
  def __init__(self, model: POC_Simulator, view: SimulatorUI):
    self._model = model
    self._view = view
    self._connectSignals()
    self.timer = QtCore.QTimer()
    self.u_line = self._view.addPlot(color='k', linetype=':', name='u')
    self.x_line = self._view.addPlot(color='r', name='x')
    u_0 = self._model.get_u()
    k_0 = self._model.get_k()
    dt_0 = self._model.get_dt()
    self.dt = int(dt_0 * 1000)
    self.timer.setInterval(self.dt)
    self.timer.timeout.connect(self._onTimerTimeout)
    self._view.labelValues['u'].setText(f'u value: {u_0}')
    self._view.labelValues['k'].setText(f'k value: {k_0}')
    self._view.labelValues['dt'].setText(f'dt value: {self.dt}')
    self._view.lineEdits['u'].setText(f'{u_0}')
    self._view.lineEdits['k'].setText(f'{k_0}')
    self._view.lineEdits['dt'].setText(f'{self.dt}')
    self.timer.start()
  def _connectSignals(self):
    self._view.buttons['u'].clicked.connect(self._on_u_update)
    self._view.buttons['k'].clicked.connect(self._on_k_update)
    self._view.buttons['dt'].clicked.connect(partial(self._on_dt_update, 'dummy')) # Program freeze without at least one partial function. No idea why.
  def _on_k_update(self):
    self._model.set_k(float(self._view.lineEdits['k'].text()))
  def _on_dt_update(self, dt): # Need to have an input here to avoid program freezing. See connect of dt above
    dt_ = float(self._view.lineEdits['dt'].text())
    dt_ = float(dt_)
    self._model.set_dt(dt_ / 1000.0)
    self.u_line.set_n_samples(seconds=60, dt=dt_ / 1000.0)
    self.x_line.set_n_samples(seconds=60, dt=dt_ / 1000.0)
    self.dt = int(dt_)
    self.timer.setInterval(self.dt)
  def _on_u_update(self):
    self._model.set_u(float(self._view.lineEdits['u'].text()))

  def _onTimerTimeout(self):
    self._model.step()
    self._view.labelValues['u'].setText(f'u value: {self._model.get_u()}')
    self._view.labelValues['k'].setText(f'k value: {self._model.get_k()}')
    self._view.labelValues['dt'].setText(f'dt value: {int(self._model.get_dt()*1000.0)}')
    self.u_line.updatePlot(self._model.get_t(), self._model.get_u())
    self.x_line.updatePlot(self._model.get_t(), self._model.get_x())
    self.timer.start()

def main():
  app = QApplication(sys.argv)
  view = SimulatorUI()
  view.show()
  model = POC_Simulator()
  POC_Ctrl(model=model, view=view)
  sys.exit(app.exec())
if __name__ == '__main__':
  main()

```

martin | 2021-04-02 19:31:49 UTC | #2
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Hi @jonstakvik10545 welcome to the forum. This was a tricky one to work out, but I think I have a solution for you.
The issue is caused by where you create the controller object at the bottom of your application. You create the `POC_Ctrl(model=model, view=view)` object, but don't keep a reference to it (by assigning to a variable). The fix is shown below.
python ```

def main():
  app = QApplication(sys.argv)
  view = SimulatorUI()
  view.show()
  model = POC_Simulator()
  ctrl = POC_Ctrl(model=model, view=view)
  sys.exit(app.exec())

```

When I make that change the plot updates as expected. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
In Python objects without references are automatically cleared up. So what's happening is that when your application is running the controller is being created and immediately destroyed, and as a result the timer is being destroyed along with it.
As to why the `partial` function stops it happening? The partial function holds a reference to the object `self` through its reference to `self._on_dt_update` -- and that reference is preventing the object from being deleted. Pretty weird eh.
python ```
self._view.buttons['dt'].clicked.connect(partial(self._on_dt_update, 'dummy'))
                       # ^ self here prevents it being deleted, as there will always be a reference to it.

```

Let me know if anything isn't clear. 
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**My pyqt5 application freezes when I don't use partial function** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/my-pyqt5-application-freezes-when-i-dont-use-partial-function/Python books) on the subject. 
**My pyqt5 application freezes when I don't use partial function** was published in [faq](https://www.pythonguis.com/faq/) on March 29, 2021 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyqtgraph](https://www.pythonguis.com/topics/pyqtgraph/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [ data-science](https://www.pythonguis.com/topics/data-science/)
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
