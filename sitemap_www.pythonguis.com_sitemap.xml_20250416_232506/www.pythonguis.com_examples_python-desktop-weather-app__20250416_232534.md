# Content from: https://www.pythonguis.com/examples/python-desktop-weather-app/

[](https://www.pythonguis.com/examples/python-desktop-weather-app/#menu)
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
# Raindar, desktop Weather App
Pulling data from a remote API
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ Example applications ](https://www.pythonguis.com/examples/)
[ Raindar Source Code ](https://www.pythonguis.com/d/weather.zip)
Get up-to-date weather direct to your desktop, including meterological data and week-ahead predictions.
## The OpenWeatherMap API
Requests to the API can take a few moments to complete. If we perform these in the main application loop this will cause our app to hang while waiting for data. To avoid this we perform all requests in seperate worker threads,
This worker collects both the current weather and a forecast, and returns this to the main thread to update the UI.
First we define a number of custom signals which the worker can emit. These include _finished_ a generic signal for the worker completing, _error_ which emits an `Exception` message should an error occur and _result_ which returns the result of the API call. The data is returned as two separate `dict` objects, one representing the current weather and one for the forecast.
python ```
:::python
class WorkerSignals(QObject):
  '''
  Defines the signals available from a running worker thread.
  '''
  finished = pyqtSignal()
  error = pyqtSignal(str)
  result = pyqtSignal(dict, dict)

```

The `WeatherWorker` runnable handles the actual requests to the API. It is initialized with a single parameter `location` which gives the location that the worker will retrieve the weather data for. Each worker performs two requests, one for the weather, and one for the forecast, receiving a JSON strings from the OpenWeatherMap.org. These are then unpacked into `dict` objects and emitted using the `.result` signal.
python ```
:::python
class WeatherWorker(QRunnable):
  '''
  Worker thread for weather updates.
  '''
  signals = WorkerSignals()
  is_interrupted = False
  def __init__(self, location):
    super().__init__()
    self.location = location
  @pyqtSlot()
  def run(self):
    try:
      params = dict(
        q=self.location,
        appid=OPENWEATHERMAP_API_KEY
      )
      url = 'http://api.openweathermap.org/data/2.5/weather?%s&units=metric' % urlencode(params)
      r = requests.get(url)
      weather = json.loads(r.text)
      # Check if we had a failure (the forecast will fail in the same way).
      if weather['cod'] != 200:
        raise Exception(weather['message'])
      url = 'http://api.openweathermap.org/data/2.5/forecast?%s&units=metric' % urlencode(params)
      r = requests.get(url)
      forecast = json.loads(r.text)
      self.signals.result.emit(weather, forecast)
    except Exception as e:
      self.signals.error.emit(str(e))
    self.signals.finished.emit()

```

## The User Interface
The Raindar UI was created using Qt Designer, and saved as `.ui` file, which is [available for download](https://raw.githubusercontent.com/mfitzp/15-minute-apps/master/weather/mainwindow.ui). This was converted to an importable Python file using `pyuic5`.
With the main window layout defined in Qt Designer. To create the mainwindow we simply create a subclass of `Ui_MainWindow` (and `QMainWindow`) and call `self.setupUi(self)` as normal.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt5](https://www.pythonguis.com/static/theme/images/products/pyside2-book.png)](https://www.pythonguis.com/pyside2-book/)
[Take a look ](https://www.pythonguis.com/pyside2-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/create-gui-applications-pyside/) and [Amazon Paperback](https://www.amazon.com/dp/B08R92BW7R/)
To trigger the request for weather data using the push button we connect it's _pressed_ signal to our custom `update_weather` slot.
Finally we create our thread pool class, to handle running our workers and show the main window.
python ```
:::python
class MainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.setupUi(self)
    self.pushButton.pressed.connect(self.update_weather)
    self.threadpool = QThreadPool()
    self.show()

```

## Requesting and Refreshing data
Pressing the button triggers the `update_weather` slot method. This creates a new `WeatherWorker` instance, passing in the currently set location from the `lineEdit` box. The _result_ and _error_ signals of the worker are connected up to the `weather_result` handler, and to our custom `alert` handler respectively.
The `alert` handler uses `QMessageBox` to display a message box window, containing the error from the worker.
python ```
:::python
  def update_weather(self):
    worker = WeatherWorker(self.lineEdit.text())
    worker.signals.result.connect(self.weather_result)
    worker.signals.error.connect(self.alert)
    self.threadpool.start(worker)
  def alert(self, message):
    alert = QMessageBox.warning(self, "Warning", message)

```

## Handling the result
The _weather_ and _forecast_ `dict` objects returned by the workers are emitted through the _result_ signal. This signal is connected to our custom slot `weather_result`, which receives the two `dict` objects. This method is responsible for updating the UI with the result returned, showing both the numeric data and updating the weather icons.
The _weather_ results are updated to the UI by `setText` on the defined `QLabels`, formatted to decimal places where appropriate. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
python ```
:::python
  def weather_result(self, weather, forecasts):
    self.latitudeLabel.setText("%.2f °" % weather['coord']['lat'])
    self.longitudeLabel.setText("%.2f °" % weather['coord']['lon'])
    self.windLabel.setText("%.2f m/s" % weather['wind']['speed'])
    self.temperatureLabel.setText("%.1f °C" % weather['main']['temp'])
    self.pressureLabel.setText("%d" % weather['main']['pressure'])
    self.humidityLabel.setText("%d" % weather['main']['humidity'])
    self.weatherLabel.setText("%s (%s)" % (
      weather['weather'][0]['main'],
      weather['weather'][0]['description']
    )

```

The timestamps are processed using a custom `from_ts_to_time_of_day` function to return a user-friendlier time of day in am/pm format with no leading zero.
python ```
:::python
    def from_ts_to_time_of_day(ts):
      dt = datetime.fromtimestamp(ts)
      return dt.strftime("%I%p").lstrip("0")
    self.sunriseLabel.setText(from_ts_to_time_of_day(weather['sys']['sunrise']))

```

The OpenWeatherMap.org has a custom mapping for icons, with each weather state indicated by a specific number — [the full mapping is available here](https://www.pythonguis.com/examples/python-desktop-weather-app/). We're using the free fugue icon set, which has a pretty complete set of weather-related icons. To simplify the mapping between the OpenWeatherMap.org and the icon set, the icons have been renamed to their respective OpenWeatherMap.org numeric code.
python ```
:::python
    def set_weather_icon(self, label, weather):
      label.setPixmap(
        QPixmap(
          os.path.join('images', "%s.png" % weather[0]['icon'])
            )
      )

```

First we set the current weather icon, from the `weather` dict, then iterate over the first 5 of the provided forecasts. The forecast icons, times and temperature labels were defined in Qt Designer with the names `forecastIcon<n>`, `forecastTime<n>` and `forecastTemp<n>`, making it simple to iterate over them in turn and retrieve them using `getattr` with the current iteration index.
python ```
:::python
    self.set_weather_icon(self.weatherIcon, weather['weather'])
    for n, forecast in enumerate(forecasts['list'][:5], 1):
      getattr(self, 'forecastTime%d' % n).setText(from_ts_to_time_of_day(forecast['dt']))
      self.set_weather_icon(getattr(self, 'forecastIcon%d' % n), forecast['weather'])
      getattr(self, 'forecastTemp%d' % n).setText("%.1f °C" % forecast['main']['temp'])

```

The full source is [available on Github](https://github.com/mfitzp/15-minute-apps/tree/master/weather).
## Challenges
A few simple ways you could extend this application —
  1. Eliminate repeated requests for the data, by using `request_cache`. This will persist the request data between runs.
  2. Support for multiple locations.
  3. Configurable forecast length.
  4. Make the current weather available on a toolbar icon while running.


[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Raindar, desktop Weather App** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/examples/python-desktop-weather-app/Python books) on the subject. 
**Raindar, desktop Weather App** was published in [examples](https://www.pythonguis.com/examples/) on April 01, 2019 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qt5](https://www.pythonguis.com/topics/qt5/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/)
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
