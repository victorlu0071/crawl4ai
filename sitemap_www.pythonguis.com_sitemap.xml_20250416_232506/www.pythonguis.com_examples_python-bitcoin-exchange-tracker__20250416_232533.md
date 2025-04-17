# Content from: https://www.pythonguis.com/examples/python-bitcoin-exchange-tracker/

[](https://www.pythonguis.com/examples/python-bitcoin-exchange-tracker/#menu)
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
# Goodforbitcoin, a Cryptocurrency market tracker
Track cryptocurrency market values and trade volumes
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 PyQt5 [ Example applications ](https://www.pythonguis.com/examples/)
[ Source Code ](https://www.pythonguis.com/d/crypto.zip) [ Mac Disk Image ](https://www.pythonguis.com/d/Goodforbitcoin.dmg) [ Windows Application ](https://www.pythonguis.com/d/Goodforbitcoin.zip)
_Goodforbitcoin_ is a simple cryptocurrency market-tracker. It displays daily market rates, including _high_ , _low_ and _close_ valuations, alongside market trade volume for a range of popular cryptocurrencies. It comes with built-in support for `BTC`, `ETH`, `LTC`, `EOS`, `XRP` and `BCH` currencies, with `EUR`, `USD` and `GBP` as base currencies for valuations.
The only Bitcoin I own I was given by some random chap on the internet. I am by no means knowledgeable about cryptocurrencies, this app is just for fun.
Read on for an overview of how the application is put together, including _interacting with APIs from PyQt5_ , plotting data with _PyQtGraph_ and packaging apps with _PyInstaller_.
The app is powered by the [CryptoCompare.com](https://www.cryptocompare.com/) API from which we retrieve per-day _high_ , _low_ , _open_ and _close_ values, alongside market trading volume amounts. The resulting exchange rates are plotted using _PyQtGraph_ along with a currency exchange list-view which is updated as you move your mouse through the plotted timeline. The bundled app is available for Windows and Mac.
## Working with the API
The first thing we need is a data source. Here we're using [CryptoCompare.com](https://www.cryptocompare.com/) which offers [free developer API access](https://min-api.cryptocompare.com/) for non-commercial purposes, including historic data.
### The API calls
We're using two separate API calls to plot our graphs — 
  1. The daily historic exchange values for all supported cryptocurrencies (`BTC`, `ETH`, `LTC`, `EOS`, `XRP` and `BCH`) against a set of base-currencies (`EUR`, `USD` and `GBP`).
  2. The daily market _volume_ data, giving the amount of trades occurring.


The two API calls we are doing are... 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
python ```
https://min-api.cryptocompare.com/data/histoday?fsym={fsym}&tsym={tsym}&limit={limit}
https://min-api.cryptocompare.com/data/exchange/histoday?tsym={tsym}&limit={limit}

```

In the URLs `fsym` is the _from symbol_ the currency converting from, `tsym` is _to symbol_ the currency we're converting to, and `limit` which is the number of results to return on the request — since we're calling `/histoday` this is the number of days data to return.
The requests are performed with `requests`, passing a per-application key in an authentication `Apikey` header, e.g.
python ```
auth_header = {
  'Apikey': CRYPTOCOMPARE_API_KEY
}
url = 'https://min-api.cryptocompare.com/data/exchange/histoday?tsym={tsym}&limit={limit}'
r = requests.get(
  url.format(**{
    'tsym': self.base_currency,
    'limit': NUMBER_OF_TIMEPOINTS-1,
    'extraParams': 'www.mfitzp.com',
    'format': 'json',
  }),
  headers=auth_header,
)

```

### Performing API requests in threads
Requests to APIs take time to complete. If we make the request directly in the GUI thread it will block the rest of the application executing — including responding to user input. The application would become _unresponsive_ (spinning wheel of death, faded window).
We can avoid this problem quite easily by performing the API requests in a separate thread.
For a complete overview this `QWorker` approach see the [PyQt5 threads tutorial](https://www.pythonguis.com/multithreading-pyqt-applications-qthreadpool/).
First we define a signals `QObject` which contains the signals we want to emit from our worker thread. This includes signals to emit _finished_ , _error_ , _progress_ (how much is complete) and _data_ (the returned data).
python ```
class WorkerSignals(QObject):
  """
  Defines the signals available from a running worker thread.
  """
  finished = pyqtSignal()
  error = pyqtSignal(tuple)
  progress = pyqtSignal(int)
  data = pyqtSignal(dict, list)
  cancel = pyqtSignal()

```

We also add a _cancel_ signal which allows the parent app to signal to an active worker thread when a new request has been queued before the first one completes. This signal sets a flag `is_interrupted` on the worker, which is checked before each currency's data is downloaded. If `True` it will return without emitting the _finished_ signal.
python ```
class UpdateWorker(QRunnable):
  """
  Worker thread for updating currency.
  """
  signals = WorkerSignals()
  def __init__(self, base_currency):
    super().__init__()
    self.is_interrupted = False
    self.base_currency = base_currency
    self.signals.cancel.connect(self.cancel)
  @pyqtSlot()
  def run(self):
    auth_header = {
      'Apikey': CRYPTOCOMPARE_API_KEY
    }
    try:
      rates = {}
      for n, crypto in enumerate(AVAILABLE_CRYPTO_CURRENCIES, 1):
        url = 'https://min-api.cryptocompare.com/data/histoday?fsym={fsym}&tsym={tsym}&limit={limit}'
        r = requests.get(
          url.format(**{
            'fsym': crypto,
            'tsym': self.base_currency,
            'limit': NUMBER_OF_TIMEPOINTS-1,
            'extraParams': 'www.mfitzp.com',
            'format': 'json',
          }),
          headers=auth_header,
        )
        r.raise_for_status()
        rates[crypto] = r.json().get('Data')
        self.signals.progress.emit(int(100 * n / len(AVAILABLE_CRYPTO_CURRENCIES)))
        if self.is_interrupted:
          # Stop without emitting finish signals.
          return
      url = 'https://min-api.cryptocompare.com/data/exchange/histoday?tsym={tsym}&limit={limit}'
      r = requests.get(
        url.format(**{
          'tsym': self.base_currency,
          'limit': NUMBER_OF_TIMEPOINTS-1,
          'extraParams': 'www.mfitzp.com',
          'format': 'json',
        }),
        headers=auth_header,
      )
      r.raise_for_status()
      volume = [d['volume'] for d in r.json().get('Data')]
    except Exception as e:
      self.signals.error.emit((e, traceback.format_exc()))
      return
    self.signals.data.emit(rates, volume)
    self.signals.finished.emit()
  def cancel(self):
    self.is_interrupted = True

```

A separate API reqeust is performed for each cryptocurrency, updating the progress bar (emitting `(int(100 * n / len(AVAILABLE_CRYPTO_CURRENCIES)))` on each iteration) and then a final request is made to retrieve the volume information. Once all requests are finished the resulting data is emitted using the earlier defined signals.
### Caching
The free API comes with a generous limit of 100,000 calls/month, which you're unlikely to hit. However, it's still polite not to waste other people's bandwidth if you can avoid it. Since we're retrieving daily rates, there isn't any reason to download >1 time per day.
As we're performing the API calls using the `requests` library we can use `requests_cache` to automatically cache all our API requests transparently. This uses a simple SQLite file database to store the results of previous requests.
python ```
import requests_cache
requests_cache.install_cache(os.path.expanduser('~/.goodforbitcoin'))

```

With the cache enabled API responses will be cached and subsequent requests to the same URL will fetch from the cache (until it expires, set to 1 day by the API).
You can put the cache wherever you want on disk, the only requirement is that it is user-writeable (so it continues to work after the app is packaged).
## Plotting the data
The API calls return _high_ , _low_ , _open_ and _close_ values for each day and for each cryptocurrency in addition to a separate market _volume_ value. These are plotted as a series of lines, with each cryptocurrency _close_ value plotted in a different colour, with _high_ and _low_ values drawed as dotted lines either side. The _open_ value is not plotted.
![PyQtGraph plot with multiple currencies and volume data](https://www.pythonguis.com/static/examples/bitcoin-exchange-tracker/Screenshot_2019-07-27_at_15.03.51.png) _PyQtGraph plot with multiple currencies and volume data_
### The currency axis
The currency values are all plotted on the same scale, using the same axis. We only plot the currency lines only once we have the data back from the API (in case any currencies are not activated) so the initial setup is just of the axis and grid. We also set the axis names, and add an _infinite_ vertical line, which is just to track through the plot to get per-day currency conversion rates.
python ```
self.ax = pg.PlotWidget()
self.ax.showGrid(True, True)
self.line = pg.InfiniteLine(
  pos=-20,
  pen=pg.mkPen('k', width=3),
  movable=False # We have our own code to handle dragless moving.
)
self.ax.addItem(self.line)
self.ax.setLabel('left', text='Rate')
self.p1 = self.ax.getPlotItem()
self.p1.scene().sigMouseMoved.connect(self.mouse_move_handler)

```

The axis' mouse move signal is connected to the custom `mouse_move_handler` slot, which moves the infinite line and updates the current rates shown in the rates table (see later).
### The volume axis
The volume axis is plotted on a separate scale, as a dotted black line. This can be zoomed vertically independently of the currencies. This is a bit tricky to achieve in _PyQtGraph_ , requiring you to manually create a `ViewBox` object and connect it up to the main axis.
python ```
# Add the right-hand axis for the market activity.
self.p2 = pg.ViewBox()
self.p2.enableAutoRange(axis=pg.ViewBox.XYAxes, enable=True)
self.p1.showAxis('right')
self.p1.scene().addItem(self.p2)
self.p2.setXLink(self.p1)
self.ax2 = self.p1.getAxis('right')
self.ax2.linkToView(self.p2)
self.ax2.setGrid(False)
self.ax2.setLabel(text='Volume')

```

Unlike for the currencies we do add the curve here, since we know it will always be present. The initial state is a diagonal line (for no reason).
python ```
self._market_activity = pg.PlotCurveItem(
  np.arange(NUMBER_OF_TIMEPOINTS), np.arange(NUMBER_OF_TIMEPOINTS),
  pen=pg.mkPen('k', style=Qt.DashLine, width=1)
)
self.p2.addItem(self._market_activity)
# Automatically rescale our twinned Y axis.
self.p1.vb.sigResized.connect(self.update_plot_scale)

```

We need connect the _resized_ signal from the primary axis to our custom `update_plot_scale` slot, to automatically update the secondary axis dimensions.
python ```
def update_plot_scale(self):
  self.p2.setGeometry(self.p1.vb.sceneBoundingRect())

```

Now the two axes are defined, we can draw our plot lines.
### Updating the plot
The plot is updated in response to the data being returned by the API request worker. This triggers the `.redraw()` method, which uses the data (available on `self.data`) to either add, or update lines to the plot.
python ```
  def redraw(self):
    y_min, y_max = sys.maxsize, 0
    x = np.arange(NUMBER_OF_TIMEPOINTS)
    # Pre-process data into lists of x, y values.
    for currency, data in self.data.items():
      if data:
        _, close, high, low = zip(*[
          (v['time'], v['close'], v['high'], v['low'])
          for v in data
        ])
        if currency in self._data_visible:
          # This line should be visible, if it's not drawn draw it.
          if currency not in self._data_lines:
            self._data_lines[currency] = {}
            self._data_lines[currency]['high'] = self.ax.plot(
              x, high, # Unpack a list of tuples into two lists, passed as individual args.
              pen=pg.mkPen(self.get_currency_color(currency), width=2, style=Qt.DotLine)
            )
          else:
            self._data_lines[currency]['high'].setData(x, high)
          y_min, y_max = min(y_min, *low), max(y_max, *high)
        else:
          # This line should not be visible, if it is delete it.
          if currency in self._data_lines:
            self._data_lines[currency]['high'].clear()
  ...

```

References to plotted lines are kept in a dictionary `self._data_lines` keyed by the cryptocurrency identifier. This allows us to check on each update whether we already have a line defined, and update it rather than recreating it. We can also remove lines for currencies that we no longer want to draw (if they've been deselected in the currency list).
The market activity (volume) plot however is always there, so we can just perform a simple update to the existing line.
python ```
self._market_activity.setData(x, self.volume)

```

In addition to the plotted lines, we also show a list with the currency conversion rates for all cryptocurrencies at the currently position in the graph. As you move your pointer back and forward these rates update automatically.
## Rates table
The rates table is a `QTableView` widget, using the Qt5 ModelView architecture.
1:1 Coaching & Tutoring for your Python GUIs project
[![Martin Fitzpatrick Python GUIs Coaching & Training](https://www.pythonguis.com/static/theme/images/products/coaching.jpg)](https://calendly.com/martinfitzpatrick/60min-python-guis-coaching)
[60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/) [Book Now](https://www.pythonguis.com/live/)
1:1 Python GUIs Coaching & Training
**Comprehensive code review** • **Bugfixes** & improvements • **Maintainability** advice and **architecture** improvements • **Design and usability** assessment • Suggestions and tips to **expand your knowledge** • **Packaging and distribution** help for Windows, Mac & Linux • [Find out more.](https://www.pythonguis.com/live)
![Goodforbitcoin rates table](https://www.pythonguis.com/static/examples/bitcoin-exchange-tracker/Screenshot_2019-07-27_at_21.35.05.png) _Goodforbitcoin rates table_
We define a `QStandardItemModel` model which we can use to update the data in the table, and set the headers for the colums. Finally, the `.itemChanged` signal is connect to our custom slot method `check_check_state`.
python ```
self.listView = QTableView()
self.model = QStandardItemModel()
self.model.setHorizontalHeaderLabels(["Currency", "Rate"])
self.model.itemChanged.connect(self.check_check_state)

```

If the item is checked, and the currency is not currently displayed (the currency identifier is _not_ in our `._data_visible` map) we add the currency to it and trigger a redraw. Likewise, if the item is unchecked but the currency is displayed, we remove it and trigger a redraw.
python ```
def check_check_state(self, i):
  if not i.isCheckable(): # Skip data columns.
    return
  currency = i.text()
  checked = i.checkState() == Qt.Checked
  if currency in self._data_visible:
    if not checked:
      self._data_visible.remove(currency)
      self.redraw()
  else:
    if checked:
      self._data_visible.append(currency)
      self.redraw()

```

We always download data for all currencies, even if they are not currently displayed, so we can update the plot immediately. You might want to have a go at changing this behaviour.
To automatically update the values on the rates table we have already connected our `mouse_move_handler` slot to mouse moves on the main axis. This slot receives a `pos` value which is a `QPoint` position relative to the axis. We first use the `.x()` value to set the position of the vertical line, and then hand off the _int_ of the value to our `update_data_viewer` method.
python ```
def mouse_move_handler(self, pos):
  pos = self.ax.getViewBox().mapSceneToView(pos)
  self.line.setPos(pos.x())
  self.update_data_viewer(int(pos.x()))

```

This next method checks if the position `i` is within the range of our data (the number of days of data we have). Then for each currency it gets the corresponding value (the _close_ value) and then sets this onto the second `QStandardItems` — the column with the currency exchange rates — as a 4dp number.
python ```
def update_data_viewer(self, i):
  if i not in range(NUMBER_OF_TIMEPOINTS):
    return
  for currency, data in self.data.items():
    self.update_data_row(currency, data[i])
def update_data_row(self, currency, data):
  citem, vitem = self.get_or_create_data_row(currency)
  vitem.setText("%.4f" % data['close'])

```

The `get_or_create_data_row` looks to see if a data row exists in the model for the corresponding currency. If it does it returns the existing row, if not it creates a new row by calling `add_data_row`. This means we don't need to define the rows explicitly, they are created automatically based on the data returned by the API.
python ```
def get_or_create_data_row(self, currency):
  if currency not in self._data_items:
    self._data_items[currency] = self.add_data_row(currency)
  return self._data_items[currency]
def add_data_row(self, currency):
  citem = QStandardItem()
  citem.setText(currency)
  citem.setForeground(QBrush(QColor(
    self.get_currency_color(currency)
  )))
  citem.setColumnCount(2)
  citem.setCheckable(True)
  if currency in DEFAULT_DISPLAY_CURRENCIES:
    citem.setCheckState(Qt.Checked)
  vitem = QStandardItem()
  vitem.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
  self.model.setColumnCount(2)
  self.model.appendRow([citem, vitem])
  self.model.sort(0)
  return citem, vitem

```

## Packaging
Now we have the working app, the last step is to bundle it up for distribution. Installers for Windows and Mac are available at the top of this article. To do this we're using _PyInstaller_ the current standard for bundling Python applications.
Because this app has no external data files building an installer for it is pretty straightforward. Install _PyInstaller_ with `pip3 install pyinstaller` then run —
bash ```
pyinstaller crypto.py

```

This produces a _spec_ file which contains the information needed by _PyInstaller_ to build the distribution installers. This file is cross-platform and should be included in your source control so any improvements are persisted.
The automatically generated file is enough to package this application as-is, but we need a few tweaks to make it complete.
### MacOS Retina Support
By default MacOS applications don't support retina (high resolution) screens. To enable this support you need to set the `NSHighResolutionCapable` flag in the application `.plist` bundled inside the `.app`. This is simple enough to do in _PyInstaller_.
Edit the `.spec` file to add the `info_plist` block shown below, with `NSHighResolutionCapable`
python ```
app = BUNDLE(coll,
      ...
       info_plist={
         'NSHighResolutionCapable': 'True'
       },

```

Now, whenever you bundle your application, this flag will be added to the MacOS bundle `.plist` automatically.
### Icons
To make the application show a custom icon while running we need to generate Windows `.ico` and MacOS `.icns` files and add these to the `.spec` definition.
A MacOSX icon bundle `icon.icns` contains multiple alternative icon sizes, which are laborious to generate by hand. The following script will take a single `.png` file input and automatically generate an `.icns` bundle containing the different sizes.
bash ```
#!/bin/bash
mkdir $1.iconset
sips -z 16 16   $1 --out $1.iconset/icon_16x16.png
sips -z 32 32   $1 --out $1.iconset/icon_16x16@2x.png
sips -z 32 32   $1 --out $1.iconset/icon_32x32.png
sips -z 64 64   $1 --out $1.iconset/icon_32x32@2x.png
sips -z 128 128  $1 --out $1.iconset/icon_128x128.png
sips -z 256 256  $1 --out $1.iconset/icon_128x128@2x.png
sips -z 256 256  $1 --out $1.iconset/icon_256x256.png
sips -z 512 512  $1 --out $1.iconset/icon_256x256@2x.png
sips -z 512 512  $1 --out $1.iconset/icon_512x512.png
cp $1 $1.iconset/icon_512x512@2x.png
iconutil -c icns $1.iconset
rm -R $1.iconset

```

This file saved as `makeicns.sh` and `chmod +x makeicns.sh` can then be used to generate an `.icns` bundle from a single large PNG, as follows.
bash ```
./makeicns.sh bitcoin-icon.png

```

You may want to check the resized icons and edit the lower resolution ones to simplify them to improve clarity. Just remove the `rm -R $1.iconset` step from the script.
For Windows we can generate an `.ico` file by loading a PNG into Gimp and resize down to 64x64, 32x32 and 16x16 on separate layers. Unlike for MacOS you can provide a single square image if you are happy to let it be resized automatically, just ensure it is saved as `.ico`.
### The completed spec file
To complete the spec file we can manually set the name of the application (to _Goodforbitcoin_) and update the filenames for the bundled applications to match. In addition the _PyInstaller_ script will have added a `pathex` variable with a static path.
python ```
pathex=['/Users/martin/repos/minute-apps/crypto'],

```

The `pathex` will be different if you generate this file yourself.
This can be removed if the `.spec` file is in the same folder are your applications base Python file to make the file portable. The last step is to add a number of hidden imports (modules which are not correctly detected by PyInstaller). These are only necessary for the Windows builds.
The completed spec file used to bundle the downloads is shown below.
python ```
# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(['crypto.py'],
       binaries=[],
       datas=[],
       hiddenimports=[
       'numpy.random.common',
       'numpy.random.bounded_integers',
       'numpy.random.entropy',
       ],
       hookspath=[],
       runtime_hooks=[],
       excludes=[],
       win_no_prefer_redirects=False,
       win_private_assemblies=False,
       cipher=block_cipher,
       noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
       cipher=block_cipher)
exe = EXE(pyz,
     a.scripts,
     [],
     exclude_binaries=True,
     name='Goodforbitcoin',
     debug=False,
     bootloader_ignore_signals=False,
     strip=False,
     upx=True,
     console=False,
     icon='resources/icon.ico'
     )
coll = COLLECT(exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='Goodforbitcoin')
app = BUNDLE(coll,
       name='Goodforbitcoin.app',
       icon='resources/icon.icns',
       bundle_identifier='com.learnpyqt.Goodforbitcoin',
       info_plist={
         'NSHighResolutionCapable': 'True'
       },
)

```

The packaged Goodforbitcoin apps, along with the source code, can be downloaded using the links below.
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Goodforbitcoin, a Cryptocurrency market tracker** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/examples/python-bitcoin-exchange-tracker/Python books) on the subject. 
**Goodforbitcoin, a Cryptocurrency market tracker** was published in [examples](https://www.pythonguis.com/examples/) on July 28, 2019 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [app](https://www.pythonguis.com/topics/app/) [bitcoin](https://www.pythonguis.com/topics/bitcoin/) [exchange](https://www.pythonguis.com/topics/exchange/) [market](https://www.pythonguis.com/topics/market/) [currency](https://www.pythonguis.com/topics/currency/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
