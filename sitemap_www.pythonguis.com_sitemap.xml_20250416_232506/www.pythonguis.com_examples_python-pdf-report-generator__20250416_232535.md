# Content from: https://www.pythonguis.com/examples/python-pdf-report-generator/

[](https://www.pythonguis.com/examples/python-pdf-report-generator/#menu)
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
# PDF Report generator
Generate custom PDF reports using reportlab & pdfrw
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 01 [ Example applications ](https://www.pythonguis.com/examples/)
If your job involves generating PDF reports, invoices, etc. you have probably thought about automating that with Python. Python has some great libraries for working with PDF files, allowing you to read and write PDFs from scripts. But you can also use these libraries as the basic of simple GUI tools, giving you an easy way to auto-fill or edit PDF reports on the desktop.
In this tutorial we'll be using two libraries to create a custom PDF report filler. The data will be collected using a Qt form: just edit the fields, press "Generate" to get the filled out form in the folder. The two libraries we'll be using here are --
  * [reportlab](https://www.reportlab.com/) which allows you to create PDFs using text and drawing primitives
  * [pdfrw](https://github.com/pmaupin/pdfrw) a library for reading and extracting pages from existing PDFs


While we _could_ use _reportlab_ to draw the entire PDF, it's easier to design a template using external tools and then simply overlay the dynamic content on this. We can use `pdfrw` to read our template PDF and then extract a page, onto which we can then draw using `reportlab`. That allows us to overlay custom information (from our app) directly onto an existing PDF template, which we save under a new name.
In this example we're entering the fields manually, but you can modify the application to read the data for the PDF from an external CSV file & generate multiple PDFs from it.
## Template PDF
For testing I've created [a custom _TPS report_ template](https://downloads.pythonguis.com/d/template.pdf) using Google Docs and downloaded the page as PDF. The page contains a number of fields which are to be filled. In this tutorial, we'll write a PyQt form which a user can fill in and then write that data out onto the PDF at the correct place.
![TPS Report](https://www.pythonguis.com/static/examples/pdf-generator/tpsreport.png)
The template is in A4 format. Save it in the same folder as your script. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
If you have another template you'd prefer to use, feel free to use that. Just remember that you'll need to adjust the positions of the form fields when writing it.
## Laying out the Form view
Qt includes a `QFormLayout` layout which simplifies the process of generating simple form layouts. It works similarly to a grid, but you can add rows of elements together and strings are converted automatically to `QLabel` objects. Our skeleton application, including the full layout matching the template form (more or less) is shown below.
  * PyQt5
  * PySide2
  * PyQt6
  * PySide6


python ```
from PyQt5.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QSpinBox
class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.name = QLineEdit()
    self.program_type = QLineEdit()
    self.product_code = QLineEdit()
    self.customer = QLineEdit()
    self.vendor = QLineEdit()
    self.n_errors = QSpinBox()
    self.n_errors.setRange(0, 1000)
    self.comments = QTextEdit()
    self.generate_btn = QPushButton("Generate PDF")
    layout = QFormLayout()
    layout.addRow("Name", self.name)
    layout.addRow("Program Type", self.program_type)
    layout.addRow("Product Code", self.product_code)
    layout.addRow("Customer", self.customer)
    layout.addRow("Vendor", self.vendor)
    layout.addRow("No. of Errors", self.n_errors)
    layout.addRow("Comments", self.comments)
    layout.addRow(self.generate_btn)
    self.setLayout(layout)

app = QApplication([])
w = Window()
w.show()
app.exec()

```

python ```
from PySide2.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QSpinBox

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.name = QLineEdit()
    self.program_type = QLineEdit()
    self.product_code = QLineEdit()
    self.customer = QLineEdit()
    self.vendor = QLineEdit()
    self.n_errors = QSpinBox()
    self.n_errors.setRange(0, 1000)
    self.comments = QTextEdit()
    self.generate_btn = QPushButton("Generate PDF")
    layout = QFormLayout()
    layout.addRow("Name", self.name)
    layout.addRow("Program Type", self.program_type)
    layout.addRow("Product Code", self.product_code)
    layout.addRow("Customer", self.customer)
    layout.addRow("Vendor", self.vendor)
    layout.addRow("No. of Errors", self.n_errors)
    layout.addRow("Comments", self.comments)
    layout.addRow(self.generate_btn)
    self.setLayout(layout)

app = QApplication([])
w = Window()
w.show()
app.exec_()

```

python ```
from PyQt6.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QSpinBox

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.name = QLineEdit()
    self.program_type = QLineEdit()
    self.product_code = QLineEdit()
    self.customer = QLineEdit()
    self.vendor = QLineEdit()
    self.n_errors = QSpinBox()
    self.n_errors.setRange(0, 1000)
    self.comments = QTextEdit()
    self.generate_btn = QPushButton("Generate PDF")
    layout = QFormLayout()
    layout.addRow("Name", self.name)
    layout.addRow("Program Type", self.program_type)
    layout.addRow("Product Code", self.product_code)
    layout.addRow("Customer", self.customer)
    layout.addRow("Vendor", self.vendor)
    layout.addRow("No. of Errors", self.n_errors)
    layout.addRow("Comments", self.comments)
    layout.addRow(self.generate_btn)
    self.setLayout(layout)

app = QApplication([])
w = Window()
w.show()
app.exec()

```

python ```
from PySide6.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QSpinBox

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.name = QLineEdit()
    self.program_type = QLineEdit()
    self.product_code = QLineEdit()
    self.customer = QLineEdit()
    self.vendor = QLineEdit()
    self.n_errors = QSpinBox()
    self.n_errors.setRange(0, 1000)
    self.comments = QTextEdit()
    self.generate_btn = QPushButton("Generate PDF")
    layout = QFormLayout()
    layout.addRow("Name", self.name)
    layout.addRow("Program Type", self.program_type)
    layout.addRow("Product Code", self.product_code)
    layout.addRow("Customer", self.customer)
    layout.addRow("Vendor", self.vendor)
    layout.addRow("No. of Errors", self.n_errors)
    layout.addRow("Comments", self.comments)
    layout.addRow(self.generate_btn)
    self.setLayout(layout)

app = QApplication([])
w = Window()
w.show()
app.exec_()

```

When writing tools to replace/automate paper forms, it's usually a good idea to try and mimic the layout of the paper form so it's familiar.
The above will give us the following layout in a window when run. You can already type things into the fields, but pressing the button won't do anything yet -- we haven't written the code to generate the PDF or hooked it up to the button.
![The form layout](https://www.pythonguis.com/static/examples/pdf-generator/form.png)
## Generating a PDF
For PDF generation using a base template, we'll be combining `reportlab` and `PdfReader`. The process is as follows --
  1. Read in the `template.pdf` file using `PdfReader`, and extract the first page only.
  2. Create a _reportlab_ `Canvas` object
  3. Use `pdfrw.toreportlab.makerl` to generate a canvas object then add it to the Canvas with `canvas.doForm()`
  4. Draw out custom bits on the Canvas
  5. Save the PDF to file


The code is shown below, this doesn't require Qt, you can save to a file and run as-is. When run the resulting PDF will be saved as `result.pdf` in the same folder.
python ```
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
outfile = "result.pdf"
template = PdfReader("template.pdf", decompress=False).pages[0]
template_obj = pagexobj(template)
canvas = Canvas(outfile)
xobj_name = makerl(canvas, template_obj)
canvas.doForm(xobj_name)
ystart = 443
# Prepared by
canvas.drawString(170, ystart, "My name here")
canvas.save()

```

Since the process of generating the PDF is doing IO, it may take some time (e.g. if we loading files off network drives). Because of this, it is better to handle this in a separate thread. We'll define this custom thread runner next.
## Running the generation in a separate thread
Since each generation is an isolated job, it makes sense to use Qt's `QRunner` framework to handle the process -- this also makes it simple later to for example add customizable templates per job. We're using the same approach seen in [the Multithreading tutorial](https://www.pythonguis.com/multithreading-pyqt-applications-qthreadpool/) where we use a subclass of `QRunner` to hold our custom run code, and implement runner-specific signals on a separate subclass of `QObject`.
  * PyQt5
  * PySide2
  * PyQt6
  * PySide6


python ```
from PyQt5.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QMessageBox, QSpinBox
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

class WorkerSignals(QObject):
  """
  Defines the signals available from a running worker thread.
  """
  error = pyqtSignal(str)
  file_saved_as = pyqtSignal(str)

class Generator(QRunnable):
  """
  Worker thread
  Inherits from QRunnable to handle worker thread setup, signals
  and wrap-up.
  :param data: The data to add to the PDF for generating.
  """
  def __init__(self, data):
    super().__init__()
    self.data = data
    self.signals = WorkerSignals()
  @pyqtSlot()
  def run(self):
    try:
      outfile = "result.pdf"
      template = PdfReader("template.pdf", decompress=False).pages[0]
      template_obj = pagexobj(template)
      canvas = Canvas(outfile)
      xobj_name = makerl(canvas, template_obj)
      canvas.doForm(xobj_name)
      ystart = 443
      # Prepared by
      canvas.drawString(170, ystart, self.data['name'])
      canvas.save()
    except Exception as e:
      self.signals.error.emit(str(e))
      return
    self.signals.file_saved_as.emit(outfile)

```

python ```
from PySide2.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QMessageBox, QSpinBox
from PySide2.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

class WorkerSignals(QObject):
  """
  Defines the signals available from a running worker thread.
  """
  error = Signal(str)
  file_saved_as = Signal(str)

class Generator(QRunnable):
  """
  Worker thread
  Inherits from QRunnable to handle worker thread setup, signals
  and wrap-up.
  :param data: The data to add to the PDF for generating.
  """
  def __init__(self, data):
    super().__init__()
    self.data = data
    self.signals = WorkerSignals()
  @Slot()
  def run(self):
    try:
      outfile = "result.pdf"
      template = PdfReader("template.pdf", decompress=False).pages[0]
      template_obj = pagexobj(template)
      canvas = Canvas(outfile)
      xobj_name = makerl(canvas, template_obj)
      canvas.doForm(xobj_name)
      ystart = 443
      # Prepared by
      canvas.drawString(170, ystart, self.data['name'])
      canvas.save()
    except Exception as e:
      self.signals.error.emit(str(e))
      return
    self.signals.file_saved_as.emit(outfile)

```

python ```
from PyQt6.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QMessageBox, QSpinBox
from PyQt6.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

class WorkerSignals(QObject):
  """
  Defines the signals available from a running worker thread.
  """
  error = pyqtSignal(str)
  file_saved_as = pyqtSignal(str)

class Generator(QRunnable):
  """
  Worker thread
  Inherits from QRunnable to handle worker thread setup, signals
  and wrap-up.
  :param data: The data to add to the PDF for generating.
  """
  def __init__(self, data):
    super().__init__()
    self.data = data
    self.signals = WorkerSignals()
  @pyqtSlot()
  def run(self):
    try:
      outfile = "result.pdf"
      template = PdfReader("template.pdf", decompress=False).pages[0]
      template_obj = pagexobj(template)
      canvas = Canvas(outfile)
      xobj_name = makerl(canvas, template_obj)
      canvas.doForm(xobj_name)
      ystart = 443
      # Prepared by
      canvas.drawString(170, ystart, self.data['name'])
      canvas.save()
    except Exception as e:
      self.signals.error.emit(str(e))
      return
    self.signals.file_saved_as.emit(outfile)

```

python ```
from PySide6.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QMessageBox, QSpinBox
from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot
from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

class WorkerSignals(QObject):
  """
  Defines the signals available from a running worker thread.
  """
  error = Signal(str)
  file_saved_as = Signal(str)

class Generator(QRunnable):
  """
  Worker thread
  Inherits from QRunnable to handle worker thread setup, signals
  and wrap-up.
  :param data: The data to add to the PDF for generating.
  """
  def __init__(self, data):
    super().__init__()
    self.data = data
    self.signals = WorkerSignals()
  @Slot()
  def run(self):
    try:
      outfile = "result.pdf"
      template = PdfReader("template.pdf", decompress=False).pages[0]
      template_obj = pagexobj(template)
      canvas = Canvas(outfile)
      xobj_name = makerl(canvas, template_obj)
      canvas.doForm(xobj_name)
      ystart = 443
      # Prepared by
      canvas.drawString(170, ystart, self.data['name'])
      canvas.save()
    except Exception as e:
      self.signals.error.emit(str(e))
      return
    self.signals.file_saved_as.emit(outfile)

```

We've defined two signals here:
  * `file_saved_as` which emits the filename of the saved PDF file (on success)
  * `error` which emits errors as a string for debugging


We need a `QThreadPool` to add run our custom runner on. We can add this onto our `MainWindow`in the `__init__` block.
python ```
class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.threadpool = QThreadPool()

```

Now we have the generator `QRunner` defined, we just need to implement the `generate` method to create the runner, pass it the data from our form fields and the start the generation running.
python ```
def generate(self):
  self.generate_btn.setDisabled(True)
  data = {
    'name': self.name.text(),
    'program_type': self.program_type.text(),
    'product_code': self.product_code.text(),
    'customer': self.customer.text(),
    'vendor': self.vendor.text(),
    'n_errors': str(self.n_errors.value()),
    'comments': self.comments.toPlainText()
  }
  g = Generator(data)
  g.signals.file_saved_as.connect(self.generated)
  g.signals.error.connect(print) # Print errors to console.
  self.threadpool.start(g)
def generated(self, outfile):
  pass28

```

In this code we first disable the `generate_btn` so the user can't press the button multiple times while the generation is taking place. We then construct a dictionary of data from our widgets, using the `.text()` method to get the text from `QLineEdit` widgets, `.value()` to get the value from the `QSpinBox` and `.toPlainText()` to get the plain text representation of the `QTextEdit`. We convert the numeric value to a string, since we are placing text.
To actually generate the PDF we create an instance of the `Generator` runner we just defined, passing in the dictionary of data. We connect the `file_saved_as` signal to our `generated` method (defined at the bottom, but not doing anything yet) and the `error` signal to the standard Python `print` function: this will automatically print any errors to the console.
Finally, we take our `Generator` instance and pass it to our threadpool's `.start()` method to queue it to run (it should start immediately). We can then hook this method up to our button in the `__init__` of our main window e.g.
python ```
  self.generate_btn.pressed.connect(self.generate)

```

If you run the app now, pressing the button will trigger the generation of the PDF and the result will be saved as `result.pdf` in the same folder as you started the app. So far we've only placed a single block of text on the page, so let's complete the generator to write all our fields in the correct place.
## Completing the generator
Next we need to finish the text placement on the template. The trick here is to work out what the per-line spacing is for your template (depends on the font size etc.) and then calculate positions relative to the first line. The y coordinates increase _up_ the page (so 0,0 is the bottom left) so in our code before, we define the `ystart` for the top line and then _subtract_ 28 for each line.
python ```

ystart = 443
# Prepared by
canvas.drawString(170, ystart, self.data['name'])
# Date: Todays date
today = datetime.today()
canvas.drawString(410, ystart, today.strftime('%F'))
# Device/Program Type
canvas.drawString(230, ystart-28, self.data['program_type'])
# Product code
canvas.drawString(175, ystart-(2*28), self.data['product_code'])
# Customer
canvas.drawString(315, ystart-(2*28), self.data['customer'])
# Vendor
canvas.drawString(145, ystart-(3*28), self.data['vendor'])
ystart = 250
# Program Language
canvas.drawString(210, ystart, "Python")
canvas.drawString(430, ystart, self.data['n_errors'])

```

### Wrapping
For most of our form fields we can just output the text as-is, since there are no line breaks. If the text entered is too long, then it will overflow -- but if we wanted we can limit this on the fields themselves by setting a max length in characters, e.g.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
python ```
field.setMaxLength(25)

```

For the comments field, things are a little more tricky. The field can be much longer, and lines need to be wrapped over multiple lines in the template. The field also accepts line breaks (by pressing Enter) which cause problems when written out to the PDF.
![Line breaks show up as black squares](https://www.pythonguis.com/static/examples/pdf-generator/linebreaks.png)
As you can see in the above screenshot, the line breaks appear as black squares in the text. The good news is that just removing the line breaks will make it easier to wrap: we can just wrap each line to a specified number of characters.
Since the characters are variable width this isn't perfect, but it shouldn't matter. If we wrap for a line-full of the widest characters (W) any real line will fit.
Python comes with the `textwrap` library built in, which we can use to wrap our text, once we've stripped the newlines.
python ```
import textwrap
comments = comments.replace('\n', ' ')
lines = textwrap.wrap(comments, width=80)

```

But we need to account for the first line being shorter, which we can do by wrapping first to the shorter length, re-joining the remainder, and re-wrapping it, e.g.
python ```
import textwrap
comments = comments.replace('\n', ' ')
lines = textwrap.wrap(comments, width=65) # 45
first_line = lines[0]
remainder = ' '.join(lines[1:])
lines = textwrap.wrap(remainder, 75) # 55
lines = lines[:4] # max lines, not including the first.

```

The comment markers on the wrap lines (45 & 55) show the wrap length needed to fit a line of Ws into the space. This is the _shortest possible_ line, but not realistic. The values used should work with most normal text.
To do this _properly_ we should calculate the actual size of each length of text in the document font and use that to inform the wrapper.
Once we have the lines prepared, we can print them onto the PDF by iterating through the list and decrementing the y position for each time. The spacing between the lines in our template document is 28.
python ```
comments = self.data['comments'].replace('\n', ' ')
if comments:
  lines = textwrap.wrap(comments, width=65) # 45
  first_line = lines[0]
  remainder = ' '.join(lines[1:])
  lines = textwrap.wrap(remainder, 75) # 55
  lines = lines[:4] # max lines, not including the first.
  canvas.drawString(155, 223, first_line)
  for n, l in enumerate(lines, 1):
    canvas.drawString(80, 223 - (n*28), l)

```

This gives the following result with some sample text.
![Wrapped text](https://www.pythonguis.com/static/examples/pdf-generator/loremwrapped.png)
## Automatically showing the result
When the file is created our runner returns the filename of the created file in a signal (currently it is always the same). It would be nice to present the resulting PDF to the user automatically, so they can check if everything looks good. On Windows we can use `os.startfile` to open a file with the _default launcher_ for that type -- in this case opening the PDF with the default PDF viewer.
Since this isn't available on other platforms, we catch the error and instead show a `QMessageBox`
python ```

  def generated(self, outfile):
    self.generate_btn.setDisabled(False)
    try:
      os.startfile(outfile)
    except Exception:
      # If startfile not available, show dialog.
      QMessageBox.information(self, "Finished", "PDF has been generated")

```

## Complete code
The complete code for PyQt5, PySide2, PyQt6 or PySide6 is shown below.
  * PyQt5
  * PySide2
  * PyQt6
  * PySide6


python ```
from PyQt5.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QMessageBox, QSpinBox
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot
from reportlab.pdfgen.canvas import Canvas
import os
import textwrap
from datetime import datetime
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

class WorkerSignals(QObject):
  """
  Defines the signals available from a running worker thread.
  """
  error = pyqtSignal(str)
  file_saved_as = pyqtSignal(str)

class Generator(QRunnable):
  """
  Worker thread
  Inherits from QRunnable to handle worker thread setup, signals
  and wrap-up.
  :param data: The data to add to the PDF for generating.
  """
  def __init__(self, data):
    super().__init__()
    self.data = data
    self.signals = WorkerSignals()
  @pyqtSlot()
  def run(self):
    try:
      outfile = "result.pdf"
      template = PdfReader("template.pdf", decompress=False).pages[0]
      template_obj = pagexobj(template)
      canvas = Canvas(outfile)
      xobj_name = makerl(canvas, template_obj)
      canvas.doForm(xobj_name)
      ystart = 443
      # Prepared by
      canvas.drawString(170, ystart, self.data['name'])
      # Date: Todays date
      today = datetime.today()
      canvas.drawString(410, ystart, today.strftime('%F'))
      # Device/Program Type
      canvas.drawString(230, ystart-28, self.data['program_type'])
      # Product code
      canvas.drawString(175, ystart-(2*28), self.data['product_code'])
      # Customer
      canvas.drawString(315, ystart-(2*28), self.data['customer'])
      # Vendor
      canvas.drawString(145, ystart-(3*28), self.data['vendor'])
      ystart = 250
      # Program Language
      canvas.drawString(210, ystart, "Python")
      canvas.drawString(430, ystart, self.data['n_errors'])
      comments = self.data['comments'].replace('\n', ' ')
      if comments:
        lines = textwrap.wrap(comments, width=65) # 45
        first_line = lines[0]
        remainder = ' '.join(lines[1:])
        lines = textwrap.wrap(remainder, 75) # 55
        lines = lines[:4] # max lines, not including the first.
        canvas.drawString(155, 223, first_line)
        for n, l in enumerate(lines, 1):
          canvas.drawString(80, 223 - (n*28), l)
      canvas.save()
    except Exception as e:
      self.signals.error.emit(str(e))
      return
    self.signals.file_saved_as.emit(outfile)

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.threadpool = QThreadPool()
    self.name = QLineEdit()
    self.program_type = QLineEdit()
    self.product_code = QLineEdit()
    self.customer = QLineEdit()
    self.vendor = QLineEdit()
    self.n_errors = QSpinBox()
    self.n_errors.setRange(0, 1000)
    self.comments = QTextEdit()
    self.generate_btn = QPushButton("Generate PDF")
    self.generate_btn.pressed.connect(self.generate)
    layout = QFormLayout()
    layout.addRow("Name", self.name)
    layout.addRow("Program Type", self.program_type)
    layout.addRow("Product Code", self.product_code)
    layout.addRow("Customer", self.customer)
    layout.addRow("Vendor", self.vendor)
    layout.addRow("No. of Errors", self.n_errors)
    layout.addRow("Comments", self.comments)
    layout.addRow(self.generate_btn)
    self.setLayout(layout)
  def generate(self):
    self.generate_btn.setDisabled(True)
    data = {
      'name': self.name.text(),
      'program_type': self.program_type.text(),
      'product_code': self.product_code.text(),
      'customer': self.customer.text(),
      'vendor': self.vendor.text(),
      'n_errors': str(self.n_errors.value()),
      'comments': self.comments.toPlainText()
    }
    g = Generator(data)
    g.signals.file_saved_as.connect(self.generated)
    g.signals.error.connect(print) # Print errors to console.
    self.threadpool.start(g)
  def generated(self, outfile):
    self.generate_btn.setDisabled(False)
    try:
      os.startfile(outfile)
    except Exception:
      # If startfile not available, show dialog.
      QMessageBox.information(self, "Finished", "PDF has been generated")

app = QApplication([])
w = Window()
w.show()
app.exec_()

```

python ```
from PySide2.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QMessageBox, QSpinBox
from PySide2.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot
from reportlab.pdfgen.canvas import Canvas
import os
import textwrap
from datetime import datetime
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

class WorkerSignals(QObject):
  """
  Defines the signals available from a running worker thread.
  """
  error = Signal(str)
  file_saved_as = Signal(str)

class Generator(QRunnable):
  """
  Worker thread
  Inherits from QRunnable to handle worker thread setup, signals
  and wrap-up.
  :param data: The data to add to the PDF for generating.
  """
  def __init__(self, data):
    super().__init__()
    self.data = data
    self.signals = WorkerSignals()
  @Slot()
  def run(self):
    try:
      outfile = "result.pdf"
      template = PdfReader("template.pdf", decompress=False).pages[0]
      template_obj = pagexobj(template)
      canvas = Canvas(outfile)
      xobj_name = makerl(canvas, template_obj)
      canvas.doForm(xobj_name)
      ystart = 443
      # Prepared by
      canvas.drawString(170, ystart, self.data['name'])
      # Date: Todays date
      today = datetime.today()
      canvas.drawString(410, ystart, today.strftime('%F'))
      # Device/Program Type
      canvas.drawString(230, ystart-28, self.data['program_type'])
      # Product code
      canvas.drawString(175, ystart-(2*28), self.data['product_code'])
      # Customer
      canvas.drawString(315, ystart-(2*28), self.data['customer'])
      # Vendor
      canvas.drawString(145, ystart-(3*28), self.data['vendor'])
      ystart = 250
      # Program Language
      canvas.drawString(210, ystart, "Python")
      canvas.drawString(430, ystart, self.data['n_errors'])
      comments = self.data['comments'].replace('\n', ' ')
      if comments:
        lines = textwrap.wrap(comments, width=65) # 45
        first_line = lines[0]
        remainder = ' '.join(lines[1:])
        lines = textwrap.wrap(remainder, 75) # 55
        lines = lines[:4] # max lines, not including the first.
        canvas.drawString(155, 223, first_line)
        for n, l in enumerate(lines, 1):
          canvas.drawString(80, 223 - (n*28), l)
      canvas.save()
    except Exception as e:
      self.signals.error.emit(str(e))
      return
    self.signals.file_saved_as.emit(outfile)

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.threadpool = QThreadPool()
    self.name = QLineEdit()
    self.program_type = QLineEdit()
    self.product_code = QLineEdit()
    self.customer = QLineEdit()
    self.vendor = QLineEdit()
    self.n_errors = QSpinBox()
    self.n_errors.setRange(0, 1000)
    self.comments = QTextEdit()
    self.generate_btn = QPushButton("Generate PDF")
    self.generate_btn.pressed.connect(self.generate)
    layout = QFormLayout()
    layout.addRow("Name", self.name)
    layout.addRow("Program Type", self.program_type)
    layout.addRow("Product Code", self.product_code)
    layout.addRow("Customer", self.customer)
    layout.addRow("Vendor", self.vendor)
    layout.addRow("No. of Errors", self.n_errors)
    layout.addRow("Comments", self.comments)
    layout.addRow(self.generate_btn)
    self.setLayout(layout)
  def generate(self):
    self.generate_btn.setDisabled(True)
    data = {
      'name': self.name.text(),
      'program_type': self.program_type.text(),
      'product_code': self.product_code.text(),
      'customer': self.customer.text(),
      'vendor': self.vendor.text(),
      'n_errors': str(self.n_errors.value()),
      'comments': self.comments.toPlainText()
    }
    g = Generator(data)
    g.signals.file_saved_as.connect(self.generated)
    g.signals.error.connect(print) # Print errors to console.
    self.threadpool.start(g)
  def generated(self, outfile):
    self.generate_btn.setDisabled(False)
    try:
      os.startfile(outfile)
    except Exception:
      # If startfile not available, show dialog.
      QMessageBox.information(self, "Finished", "PDF has been generated")

app = QApplication([])
w = Window()
w.show()
app.exec_()

```

python ```
from PyQt6.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QMessageBox, QSpinBox
from PyQt6.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot
from reportlab.pdfgen.canvas import Canvas
import os
import textwrap
from datetime import datetime
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

class WorkerSignals(QObject):
  """
  Defines the signals available from a running worker thread.
  """
  error = pyqtSignal(str)
  file_saved_as = pyqtSignal(str)

class Generator(QRunnable):
  """
  Worker thread
  Inherits from QRunnable to handle worker thread setup, signals
  and wrap-up.
  :param data:The data to add to the PDF for generating.
  """
  def __init__(self, data):
    super().__init__()
    self.data = data
    self.signals = WorkerSignals()
  @pyqtSlot()
  def run(self):
    try:
      outfile = "result.pdf"
      template = PdfReader("template.pdf", decompress=False).pages[0]
      template_obj = pagexobj(template)
      canvas = Canvas(outfile)
      xobj_name = makerl(canvas, template_obj)
      canvas.doForm(xobj_name)
      ystart = 443
      # Prepared by
      canvas.drawString(170, ystart, self.data['name'])
      # Date: Todays date
      today = datetime.today()
      canvas.drawString(410, ystart, today.strftime('%F'))
      # Device/Program Type
      canvas.drawString(230, ystart-28, self.data['program_type'])
      # Product code
      canvas.drawString(175, ystart-(2*28), self.data['product_code'])
      # Customer
      canvas.drawString(315, ystart-(2*28), self.data['customer'])
      # Vendor
      canvas.drawString(145, ystart-(3*28), self.data['vendor'])
      ystart = 250
      # Program Language
      canvas.drawString(210, ystart, "Python")
      canvas.drawString(430, ystart, self.data['n_errors'])
      comments = self.data['comments'].replace('\n', ' ')
      if comments:
        lines = textwrap.wrap(comments, width=65) # 45
        first_line = lines[0]
        remainder = ' '.join(lines[1:])
        lines = textwrap.wrap(remainder, 75) # 55
        lines = lines[:4] # max lines, not including the first.
        canvas.drawString(155, 223, first_line)
        for n, l in enumerate(lines, 1):
          canvas.drawString(80, 223 - (n*28), l)
      canvas.save()
    except Exception as e:
      self.signals.error.emit(str(e))
      return
    self.signals.file_saved_as.emit(outfile)

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.threadpool = QThreadPool()
    self.name = QLineEdit()
    self.program_type = QLineEdit()
    self.product_code = QLineEdit()
    self.customer = QLineEdit()
    self.vendor = QLineEdit()
    self.n_errors = QSpinBox()
    self.n_errors.setRange(0, 1000)
    self.comments = QTextEdit()
    self.generate_btn = QPushButton("Generate PDF")
    self.generate_btn.pressed.connect(self.generate)
    layout = QFormLayout()
    layout.addRow("Name", self.name)
    layout.addRow("Program Type", self.program_type)
    layout.addRow("Product Code", self.product_code)
    layout.addRow("Customer", self.customer)
    layout.addRow("Vendor", self.vendor)
    layout.addRow("No. of Errors", self.n_errors)
    layout.addRow("Comments", self.comments)
    layout.addRow(self.generate_btn)
    self.setLayout(layout)
  def generate(self):
    self.generate_btn.setDisabled(True)
    data = {
      'name': self.name.text(),
      'program_type': self.program_type.text(),
      'product_code': self.product_code.text(),
      'customer': self.customer.text(),
      'vendor': self.vendor.text(),
      'n_errors': str(self.n_errors.value()),
      'comments': self.comments.toPlainText()
    }
    g = Generator(data)
    g.signals.file_saved_as.connect(self.generated)
    g.signals.error.connect(print) # Print errors to console.
    self.threadpool.start(g)
  def generated(self, outfile):
    self.generate_btn.setDisabled(False)
    try:
      os.startfile(outfile)
    except Exception:
      # If startfile not available, show dialog.
      QMessageBox.information(self, "Finished", "PDF has been generated")

app = QApplication([])
w = Window()
w.show()
app.exec()

```

python ```
from PySide6.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QMessageBox, QSpinBox
from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot
from reportlab.pdfgen.canvas import Canvas
import os
import textwrap
from datetime import datetime
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

class WorkerSignals(QObject):
  """
  Defines the signals available from a running worker thread.
  """
  error = Signal(str)
  file_saved_as = Signal(str)

class Generator(QRunnable):
  """
  Worker thread
  Inherits from QRunnable to handle worker thread setup, signals
  and wrap-up.
  :param data:The data to add to the PDF for generating.
  """
  def __init__(self, data):
    super().__init__()
    self.data = data
    self.signals = WorkerSignals()
  @Slot()
  def run(self):
    try:
      outfile = "result.pdf"
      template = PdfReader("template.pdf", decompress=False).pages[0]
      template_obj = pagexobj(template)
      canvas = Canvas(outfile)
      xobj_name = makerl(canvas, template_obj)
      canvas.doForm(xobj_name)
      ystart = 443
      # Prepared by
      canvas.drawString(170, ystart, self.data['name'])
      # Date: Todays date
      today = datetime.today()
      canvas.drawString(410, ystart, today.strftime('%F'))
      # Device/Program Type
      canvas.drawString(230, ystart-28, self.data['program_type'])
      # Product code
      canvas.drawString(175, ystart-(2*28), self.data['product_code'])
      # Customer
      canvas.drawString(315, ystart-(2*28), self.data['customer'])
      # Vendor
      canvas.drawString(145, ystart-(3*28), self.data['vendor'])
      ystart = 250
      # Program Language
      canvas.drawString(210, ystart, "Python")
      canvas.drawString(430, ystart, self.data['n_errors'])
      comments = self.data['comments'].replace('\n', ' ')
      if comments:
        lines = textwrap.wrap(comments, width=65) # 45
        first_line = lines[0]
        remainder = ' '.join(lines[1:])
        lines = textwrap.wrap(remainder, 75) # 55
        lines = lines[:4] # max lines, not including the first.
        canvas.drawString(155, 223, first_line)
        for n, l in enumerate(lines, 1):
          canvas.drawString(80, 223 - (n*28), l)
      canvas.save()
    except Exception as e:
      self.signals.error.emit(str(e))
      return
    self.signals.file_saved_as.emit(outfile)

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.threadpool = QThreadPool()
    self.name = QLineEdit()
    self.program_type = QLineEdit()
    self.product_code = QLineEdit()
    self.customer = QLineEdit()
    self.vendor = QLineEdit()
    self.n_errors = QSpinBox()
    self.n_errors.setRange(0, 1000)
    self.comments = QTextEdit()
    self.generate_btn = QPushButton("Generate PDF")
    self.generate_btn.pressed.connect(self.generate)
    layout = QFormLayout()
    layout.addRow("Name", self.name)
    layout.addRow("Program Type", self.program_type)
    layout.addRow("Product Code", self.product_code)
    layout.addRow("Customer", self.customer)
    layout.addRow("Vendor", self.vendor)
    layout.addRow("No. of Errors", self.n_errors)
    layout.addRow("Comments", self.comments)
    layout.addRow(self.generate_btn)
    self.setLayout(layout)
  def generate(self):
    self.generate_btn.setDisabled(True)
    data = {
      'name': self.name.text(),
      'program_type': self.program_type.text(),
      'product_code': self.product_code.text(),
      'customer': self.customer.text(),
      'vendor': self.vendor.text(),
      'n_errors': str(self.n_errors.value()),
      'comments': self.comments.toPlainText()
    }
    g = Generator(data)
    g.signals.file_saved_as.connect(self.generated)
    g.signals.error.connect(print) # Print errors to console.
    self.threadpool.start(g)
  def generated(self, outfile):
    self.generate_btn.setDisabled(False)
    try:
      os.startfile(outfile)
    except Exception:
      # If startfile not available, show dialog.
      QMessageBox.information(self, "Finished", "PDF has been generated")

app = QApplication([])
w = Window()
w.show()
app.exec_()

```

## Generating from a CSV file
In the above example you need to type the data to fill in manually. This is fine if you don't have a lot of PDFs to generate, but not so much fun if you have an entire CSV file worth of data to generate reports for. In the example below, rather than present a list of form fields to the user we just ask for a source CSV file from which PDFs can be generated -- each row in the file generates a separate PDF file using the data in the file.
  * PyQt5
  * PySide2
  * PyQt6
  * PySide6


python ```
from PyQt5.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QMessageBox, QSpinBox, QFileDialog
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot
from reportlab.pdfgen.canvas import Canvas
import os, csv
import textwrap
from datetime import datetime
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

class WorkerSignals(QObject):
  """
  Defines the signals available from a running worker thread.
  """
  error = pyqtSignal(str)
  finished = pyqtSignal()

class Generator(QRunnable):
  """
  Worker thread
  Inherits from QRunnable to handle worker thread setup, signals
  and wrap-up.
  :param data: The data to add to the PDF for generating.
  """
  def __init__(self, data):
    super().__init__()
    self.data = data
    self.signals = WorkerSignals()
  @pyqtSlot()
  def run(self):
    try:
      filename, _ = os.path.splitext(self.data['sourcefile'])
      folder = os.path.dirname(self.data['sourcefile'])
      template = PdfReader("template.pdf", decompress=False).pages[0]
      template_obj = pagexobj(template)
      with open(self.data['sourcefile'], 'r', newline='') as f:
        reader = csv.DictReader(f)
        for n, row in enumerate(reader, 1):
          fn = f'{filename}-{n}.pdf'
          outfile = os.path.join(folder, fn)
          canvas = Canvas(outfile)
          xobj_name = makerl(canvas, template_obj)
          canvas.doForm(xobj_name)
          ystart = 443
          # Prepared by
          canvas.drawString(170, ystart, row.get('name', ''))
          # Date: Todays date
          today = datetime.today()
          canvas.drawString(410, ystart, today.strftime('%F'))
          # Device/Program Type
          canvas.drawString(230, ystart-28, row.get('program_type', ''))
          # Product code
          canvas.drawString(175, ystart-(2*28), row.get('product_code', ''))
          # Customer
          canvas.drawString(315, ystart-(2*28), row.get('customer', ''))
          # Vendor
          canvas.drawString(145, ystart-(3*28), row.get('vendor', ''))
          ystart = 250
          # Program Language
          canvas.drawString(210, ystart, "Python")
          canvas.drawString(430, ystart, row.get('n_errors', ''))
          comments = row.get('comments', '').replace('\n', ' ')
          if comments:
            lines = textwrap.wrap(comments, width=65) # 45
            first_line = lines[0]
            remainder = ' '.join(lines[1:])
            lines = textwrap.wrap(remainder, 75) # 55
            lines = lines[:4] # max lines, not including the first.
            canvas.drawString(155, 223, first_line)
            for n, l in enumerate(lines, 1):
              canvas.drawString(80, 223 - (n*28), l)
          canvas.save()
    except Exception as e:
      self.signals.error.emit(str(e))
      return
    self.signals.finished.emit()

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.threadpool = QThreadPool()
    self.sourcefile = QLineEdit()
    self.sourcefile.setDisabled(True) # must use the file finder to select a valid file.
    self.file_select = QPushButton("Select CSV...")
    self.file_select.pressed.connect(self.choose_csv_file)
    self.generate_btn = QPushButton("Generate PDF")
    self.generate_btn.pressed.connect(self.generate)
    layout = QFormLayout()
    layout.addRow(self.sourcefile, self.file_select)
    layout.addRow(self.generate_btn)
    self.setLayout(layout)
  def choose_csv_file(self):
    filename, _ = QFileDialog.getOpenFileName(self, "Select a file", filter="CSV files (*.csv)")
    if filename:
      self.sourcefile.setText(filename)
  def generate(self):
    if not self.sourcefile.text():
      return # If the field is empty, ignore.
    self.generate_btn.setDisabled(True)
    data = {
      'sourcefile': self.sourcefile.text(),
    }
    g = Generator(data)
    g.signals.finished.connect(self.generated)
    g.signals.error.connect(print) # Print errors to console.
    self.threadpool.start(g)
  def generated(self):
    self.generate_btn.setDisabled(False)
    QMessageBox.information(self, "Finished", "PDFs have been generated")

app = QApplication([])
w = Window()
w.show()
app.exec()

```

python ```
from PySide2.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QMessageBox, QSpinBox, QFileDialog
from PySide2.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot

from reportlab.pdfgen.canvas import Canvas
import os, csv
import textwrap
from datetime import datetime
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

class WorkerSignals(QObject):
  """
  Defines the signals available from a running worker thread.
  """
  error = Signal(str)
  finished = Signal()

class Generator(QRunnable):
  """
  Worker thread
  Inherits from QRunnable to handle worker thread setup, signals
  and wrap-up.
  :param data: The data to add to the PDF for generating.
  """
  def __init__(self, data):
    super().__init__()
    self.data = data
    self.signals = WorkerSignals()
  @Slot()
  def run(self):
    try:
      filename, _ = os.path.splitext(self.data['sourcefile'])
      folder = os.path.dirname(self.data['sourcefile'])
      template = PdfReader("template.pdf", decompress=False).pages[0]
      template_obj = pagexobj(template)
      with open(self.data['sourcefile'], 'r', newline='') as f:
        reader = csv.DictReader(f)
        for n, row in enumerate(reader, 1):
          fn = f'{filename}-{n}.pdf'
          outfile = os.path.join(folder, fn)
          canvas = Canvas(outfile)
          xobj_name = makerl(canvas, template_obj)
          canvas.doForm(xobj_name)
          ystart = 443
          # Prepared by
          canvas.drawString(170, ystart, row.get('name', ''))
          # Date: Todays date
          today = datetime.today()
          canvas.drawString(410, ystart, today.strftime('%F'))
          # Device/Program Type
          canvas.drawString(230, ystart-28, row.get('program_type', ''))
          # Product code
          canvas.drawString(175, ystart-(2*28), row.get('product_code', ''))
          # Customer
          canvas.drawString(315, ystart-(2*28), row.get('customer', ''))
          # Vendor
          canvas.drawString(145, ystart-(3*28), row.get('vendor', ''))
          ystart = 250
          # Program Language
          canvas.drawString(210, ystart, "Python")
          canvas.drawString(430, ystart, row.get('n_errors', ''))
          comments = row.get('comments', '').replace('\n', ' ')
          if comments:
            lines = textwrap.wrap(comments, width=65) # 45
            first_line = lines[0]
            remainder = ' '.join(lines[1:])
            lines = textwrap.wrap(remainder, 75) # 55
            lines = lines[:4] # max lines, not including the first.
            canvas.drawString(155, 223, first_line)
            for n, l in enumerate(lines, 1):
              canvas.drawString(80, 223 - (n*28), l)
          canvas.save()
    except Exception as e:
      self.signals.error.emit(str(e))
      return
    self.signals.finished.emit()

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.threadpool = QThreadPool()
    self.sourcefile = QLineEdit()
    self.sourcefile.setDisabled(True) # must use the file finder to select a valid file.
    self.file_select = QPushButton("Select CSV...")
    self.file_select.pressed.connect(self.choose_csv_file)
    self.generate_btn = QPushButton("Generate PDF")
    self.generate_btn.pressed.connect(self.generate)
    layout = QFormLayout()
    layout.addRow(self.sourcefile, self.file_select)
    layout.addRow(self.generate_btn)
    self.setLayout(layout)
  def choose_csv_file(self):
    filename, _ = QFileDialog.getOpenFileName(self, "Select a file", filter="CSV files (*.csv)")
    if filename:
      self.sourcefile.setText(filename)
  def generate(self):
    if not self.sourcefile.text():
      return # If the field is empty, ignore.
    self.generate_btn.setDisabled(True)
    data = {
      'sourcefile': self.sourcefile.text(),
    }
    g = Generator(data)
    g.signals.finished.connect(self.generated)
    g.signals.error.connect(print) # Print errors to console.
    self.threadpool.start(g)
  def generated(self):
    self.generate_btn.setDisabled(False)
    QMessageBox.information(self, "Finished", "PDFs have been generated")

app = QApplication([])
w = Window()
w.show()
app.exec_()

```

python ```
from PyQt6.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QMessageBox, QSpinBox, QFileDialog
from PyQt6.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot

from reportlab.pdfgen.canvas import Canvas
import os, csv
import textwrap
from datetime import datetime
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

class WorkerSignals(QObject):
  """
  Defines the signals available from a running worker thread.
  """
  error = pyqtSignal(str)
  finished = pyqtSignal()

class Generator(QRunnable):
  """
  Worker thread
  Inherits from QRunnable to handle worker thread setup, signals
  and wrap-up.
  :param data: The data to add to the PDF for generating.
  """
  def __init__(self, data):
    super().__init__()
    self.data = data
    self.signals = WorkerSignals()
  @pyqtSlot()
  def run(self):
    try:
      filename, _ = os.path.splitext(self.data['sourcefile'])
      folder = os.path.dirname(self.data['sourcefile'])
      template = PdfReader("template.pdf", decompress=False).pages[0]
      template_obj = pagexobj(template)
      with open(self.data['sourcefile'], 'r', newline='') as f:
        reader = csv.DictReader(f)
        for n, row in enumerate(reader, 1):
          fn = f'{filename}-{n}.pdf'
          outfile = os.path.join(folder, fn)
          canvas = Canvas(outfile)
          xobj_name = makerl(canvas, template_obj)
          canvas.doForm(xobj_name)
          ystart = 443
          # Prepared by
          canvas.drawString(170, ystart, row.get('name', ''))
          # Date: Todays date
          today = datetime.today()
          canvas.drawString(410, ystart, today.strftime('%F'))
          # Device/Program Type
          canvas.drawString(230, ystart-28, row.get('program_type', ''))
          # Product code
          canvas.drawString(175, ystart-(2*28), row.get('product_code', ''))
          # Customer
          canvas.drawString(315, ystart-(2*28), row.get('customer', ''))
          # Vendor
          canvas.drawString(145, ystart-(3*28), row.get('vendor', ''))
          ystart = 250
          # Program Language
          canvas.drawString(210, ystart, "Python")
          canvas.drawString(430, ystart, row.get('n_errors', ''))
          comments = row.get('comments', '').replace('\n', ' ')
          if comments:
            lines = textwrap.wrap(comments, width=65) # 45
            first_line = lines[0]
            remainder = ' '.join(lines[1:])
            lines = textwrap.wrap(remainder, 75) # 55
            lines = lines[:4] # max lines, not including the first.
            canvas.drawString(155, 223, first_line)
            for n, l in enumerate(lines, 1):
              canvas.drawString(80, 223 - (n*28), l)
          canvas.save()
    except Exception as e:
      self.signals.error.emit(str(e))
      return
    self.signals.finished.emit()

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.threadpool = QThreadPool()
    self.sourcefile = QLineEdit()
    self.sourcefile.setDisabled(True) # must use the file finder to select a valid file.
    self.file_select = QPushButton("Select CSV...")
    self.file_select.pressed.connect(self.choose_csv_file)
    self.generate_btn = QPushButton("Generate PDF")
    self.generate_btn.pressed.connect(self.generate)
    layout = QFormLayout()
    layout.addRow(self.sourcefile, self.file_select)
    layout.addRow(self.generate_btn)
    self.setLayout(layout)
  def choose_csv_file(self):
    filename, _ = QFileDialog.getOpenFileName(self, "Select a file", filter="CSV files (*.csv)")
    if filename:
      self.sourcefile.setText(filename)
  def generate(self):
    if not self.sourcefile.text():
      return # If the field is empty, ignore.
    self.generate_btn.setDisabled(True)
    data = {
      'sourcefile': self.sourcefile.text(),
    }
    g = Generator(data)
    g.signals.finished.connect(self.generated)
    g.signals.error.connect(print) # Print errors to console.
    self.threadpool.start(g)
  def generated(self):
    self.generate_btn.setDisabled(False)
    QMessageBox.information(self, "Finished", "PDFs have been generated")

app = QApplication([])
w = Window()
w.show()
app.exec()

```

python ```
from PySide6.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QMessageBox, QSpinBox, QFileDialog
from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal, Slot

from reportlab.pdfgen.canvas import Canvas
import os, csv
import textwrap
from datetime import datetime
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

class WorkerSignals(QObject):
  """
  Defines the signals available from a running worker thread.
  """
  error = Signal(str)
  finished = Signal()

class Generator(QRunnable):
  """
  Worker thread
  Inherits from QRunnable to handle worker thread setup, signals
  and wrap-up.
  :param data: The data to add to the PDF for generating.
  """
  def __init__(self, data):
    super().__init__()
    self.data = data
    self.signals = WorkerSignals()
  @Slot()
  def run(self):
    try:
      filename, _ = os.path.splitext(self.data['sourcefile'])
      folder = os.path.dirname(self.data['sourcefile'])
      template = PdfReader("template.pdf", decompress=False).pages[0]
      template_obj = pagexobj(template)
      with open(self.data['sourcefile'], 'r', newline='') as f:
        reader = csv.DictReader(f)
        for n, row in enumerate(reader, 1):
          fn = f'{filename}-{n}.pdf'
          outfile = os.path.join(folder, fn)
          canvas = Canvas(outfile)
          xobj_name = makerl(canvas, template_obj)
          canvas.doForm(xobj_name)
          ystart = 443
          # Prepared by
          canvas.drawString(170, ystart, row.get('name', ''))
          # Date: Todays date
          today = datetime.today()
          canvas.drawString(410, ystart, today.strftime('%F'))
          # Device/Program Type
          canvas.drawString(230, ystart-28, row.get('program_type', ''))
          # Product code
          canvas.drawString(175, ystart-(2*28), row.get('product_code', ''))
          # Customer
          canvas.drawString(315, ystart-(2*28), row.get('customer', ''))
          # Vendor
          canvas.drawString(145, ystart-(3*28), row.get('vendor', ''))
          ystart = 250
          # Program Language
          canvas.drawString(210, ystart, "Python")
          canvas.drawString(430, ystart, row.get('n_errors', ''))
          comments = row.get('comments', '').replace('\n', ' ')
          if comments:
            lines = textwrap.wrap(comments, width=65) # 45
            first_line = lines[0]
            remainder = ' '.join(lines[1:])
            lines = textwrap.wrap(remainder, 75) # 55
            lines = lines[:4] # max lines, not including the first.
            canvas.drawString(155, 223, first_line)
            for n, l in enumerate(lines, 1):
              canvas.drawString(80, 223 - (n*28), l)
          canvas.save()
    except Exception as e:
      self.signals.error.emit(str(e))
      return
    self.signals.finished.emit()

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.threadpool = QThreadPool()
    self.sourcefile = QLineEdit()
    self.sourcefile.setDisabled(True) # must use the file finder to select a valid file.
    self.file_select = QPushButton("Select CSV...")
    self.file_select.pressed.connect(self.choose_csv_file)
    self.generate_btn = QPushButton("Generate PDF")
    self.generate_btn.pressed.connect(self.generate)
    layout = QFormLayout()
    layout.addRow(self.sourcefile, self.file_select)
    layout.addRow(self.generate_btn)
    self.setLayout(layout)
  def choose_csv_file(self):
    filename, _ = QFileDialog.getOpenFileName(self, "Select a file", filter="CSV files (*.csv)")
    if filename:
      self.sourcefile.setText(filename)
  def generate(self):
    if not self.sourcefile.text():
      return # If the field is empty, ignore.
    self.generate_btn.setDisabled(True)
    data = {
      'sourcefile': self.sourcefile.text(),
    }
    g = Generator(data)
    g.signals.finished.connect(self.generated)
    g.signals.error.connect(print) # Print errors to console.
    self.threadpool.start(g)
  def generated(self):
    self.generate_btn.setDisabled(False)
    QMessageBox.information(self, "Finished", "PDFs have been generated")

app = QApplication([])
w = Window()
w.show()
app.exec_()

```

You can run this app using the `template.pdf` and [this example CSV file](https://downloads.pythonguis.com/d/tps.csv) to generate a few TPS reports.
Things to notice --
  * We now generate multiple files, so it doesn't make much sense to open them when they're finished. Instead, we always show the "complete" message, and only once. The signal `file_saved_as` has been renamed to `finished` and we've removed the filename `str` since it's no longer used.
  * The `QLineEdit` to get the filename is disabled so it's not possible to edit directly: the only way to set a source CSV file is to select the file directly, ensuring it's there.
  * We auto-generate the output filenames, based on the import filename and the current row number. The `filename` is taken from the input CSV: with a CSV named `tps.csv` files will be named `tps-1.pdf`, `tps-2.pdf` etc. Files are written out to the folder the source CSV is in.
  * Since some rows/files might miss required fields, we use `.get()` on the row dictionary with a default empty string.


## Possible improvements
If you feel like improving on this code, there are a few things you could try 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
  * Make the template and output file location configurable -- use a Qt file dialogs
  * Load the field positions from a file alongside the template (JSON) so you can use the same form with multiple templates
  * Make the fields configurable -- this gets quite tricky, but you particular types (`str`, `datetime`, `int`, etc.) can have specific widgets assigned to them


Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PDF Report generator** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/examples/python-pdf-report-generator/Python books) on the subject. 
**PDF Report generator** was published in [examples](https://www.pythonguis.com/examples/) on March 01, 2021 (updated April 01, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[pdf](https://www.pythonguis.com/topics/pdf/) [ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [ pyside6](https://www.pythonguis.com/topics/pyside6/) [reportlab](https://www.pythonguis.com/topics/reportlab/) [report](https://www.pythonguis.com/topics/report/) [generator](https://www.pythonguis.com/topics/generator/) [threads](https://www.pythonguis.com/topics/threads/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
