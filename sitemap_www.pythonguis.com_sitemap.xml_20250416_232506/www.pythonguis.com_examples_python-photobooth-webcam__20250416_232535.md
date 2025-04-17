# Content from: https://www.pythonguis.com/examples/python-photobooth-webcam/

[](https://www.pythonguis.com/examples/python-photobooth-webcam/#menu)
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
# NSAViewer, desktop Photobooth
Take photos of yourself, with a terrible camera.
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Nov 04 [ Example applications ](https://www.pythonguis.com/examples/)
[ NSAViewer Source Code ](https://www.pythonguis.com/d/camera.zip)
This app isn't actually a direct line from your webcam to the NSA, it's a demo of using the webcam/camera support in Qt. The name is a nod to the paranoia (_or is it..._) of being watched through your webcam by government spooks.
With this app you can use your laptop's built-in camera to view yourself, and take photobooth-style snapshots. The app uses Qt's built in webcam methods to provide support for multiple cameras if you have them.
Originally the plan was to make the app (openly) uplod snapshots of all to a remote server to complete the idea, but this is the internet, and nobody wants to see that.
## Qt Camera Interface
Camera support in Qt5 is accessible via `QtMultimedia` with multimedia-specific widgets available via `QtMultimediaWidgets`. The first step to using cameras is to get a list of currently available cameras on the system, via `QCameraInfo.availableCameras()`. This returns a list of `QCameraInfo` objects, which provide various bits of information about each camera, including a unique ID.
If we have no cameras available we just quit out, ungracefully. If a camera is available we setup the `QCameraViewfinder` to provide a live updating viewfinder view from the active camera. We select the first camera in our list to use as a 'default' — on a laptop this is usually the built in camera.
python ```
class MainWindow(QMainWindow):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.available_cameras = QCameraInfo.availableCameras()
    if not self.available_cameras:
      pass #quit
    self.viewfinder = QCameraViewfinder()
    self.viewfinder.show()
    self.setCentralWidget(self.viewfinder)
    # Set the default camera.
    self.select_camera(0)

```

This is all that is required to stream the active camera live to the viewfinder widget.
## Camera Selection
The toolbar allows a user to select the active camera, take snapshot photos and to select the output folder for these photos. Each `QAction` is connected to a custom slot to handle the specific behaviour. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
The camera selection list is pre-filled with the user-friendly name of each camera, via `QCameraInfo.description()`. The index of the selected camera in the combobox matches its position in the list.
python ```
camera_toolbar = QToolBar("Camera")
camera_toolbar.setIconSize(QSize(14, 14))
self.addToolBar(camera_toolbar)
photo_action = QAction(QIcon(os.path.join('images', 'camera-black.png')), "Take photo...", self)
photo_action.setStatusTip("Take photo of current view")
photo_action.triggered.connect(self.take_photo)
camera_toolbar.addAction(photo_action)
change_folder_action = QAction(QIcon(os.path.join('images', 'blue-folder-horizontal-open.png')), "Change save location...", self)
change_folder_action.setStatusTip("Change folder where photos are saved.")
change_folder_action.triggered.connect(self.change_folder)
camera_toolbar.addAction(change_folder_action)
camera_selector = QComboBox()
camera_selector.addItems([c.description() for c in self.available_cameras])
camera_selector.currentIndexChanged.connect( self.select_camera )
camera_toolbar.addWidget(camera_selector)

```

The camera select method accepts a single parameter `i`, which is the index of a camera in our prefilled `self.available_cameras` list. This is a `QCameraInfo` object, which can be passed to `QCamera` to create a new camera object.
Once the camera object is created, we set it to use our existing viewfinder widget (central widget). The capture mode is set to `QCamera.CaptureStillImage` and then the camera must be started with `.start()`.
Capture of images from a camera is handled by `QCameraImageCapture`, which we setup by passing in our previously created camera object. The `.imageCaptured` signal is triggered every time (after) an image is captured, so we can connect to it to show a status update — the snapshotting is done seperately. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyside2-book/) _by Martin Fitzpatrick_ — (PySide2 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside2-book/) [Get the book](https://secure.pythonguis.com/01hf778jyaajk5vk1q6824sd44/)
def select_camera(self, i): self.camera = QCamera(self.available_cameras[i]) self.camera.setViewfinder(self.viewfinder) self.camera.setCaptureMode(QCamera.CaptureStillImage) self.camera.error.connect(lambda: self.alert(self.camera.errorString())) self.camera.start()
python ```
self.capture = QCameraImageCapture(self.camera)
self.capture.error.connect(lambda i, e, s: self.alert(s))
self.capture.imageCaptured.connect(lambda d, i: self.status.showMessage("Image %04d captured" % self.save_seq))
self.current_camera_name = self.available_cameras[i].description()
self.save_seq = 0

```

## Taking a photo
Taking a camera snapshot is handled in our custom `take_photo` slot using the `QCameraImageCapture` object created when initialising the camera. The `.capture()` method accepts a filename, which we create using our selected save path and a full-name timestamp. The file is stamped with a current time, plus the current camera and a sequence number to avoid conflicts. Snapshots are saved in JPEG format.
python ```
def take_photo(self):
  timestamp = time.strftime("%d-%b-%Y-%H_%M_%S")
  self.capture.capture(os.path.join(self.save_path, "%s-%04d-%s.jpg" % (
    self.current_camera_name,
    self.save_seq,
    timestamp
  )))
  self.save_seq += 1

```

The sequence number is incremented after the snapshot is taken.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**NSAViewer, desktop Photobooth** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/examples/python-photobooth-webcam/Python books) on the subject. 
**NSAViewer, desktop Photobooth** was published in [examples](https://www.pythonguis.com/examples/) on April 02, 2019 (updated November 04, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[qt5](https://www.pythonguis.com/topics/qt5/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [camera](https://www.pythonguis.com/topics/camera/) [webcam](https://www.pythonguis.com/topics/webcam/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/)
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
