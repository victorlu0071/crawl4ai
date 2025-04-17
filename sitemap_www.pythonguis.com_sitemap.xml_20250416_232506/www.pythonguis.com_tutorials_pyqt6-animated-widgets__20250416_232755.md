# Content from: https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/

[](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/#menu)
  * Python GUIs
  * [Home](https://www.pythonguis.com/)
  * [Latest Articles](https://www.pythonguis.com/latest/)
  * [FAQ](https://www.pythonguis.com/faq/)
  * [Forum ](https://forum.pythonguis.com/)
  * [PyQt6 ](https://www.pythonguis.com/pyqt6/)
  * [PyQt6 Tutorial ](https://www.pythonguis.com/pyqt6-tutorial/)
  * Basics
  * [Create a PyQt6 app](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/)
  * [PyQt6 Signals](https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/)
  * [PyQt6 Widgets](https://www.pythonguis.com/tutorials/pyqt6-widgets/)
  * [PyQt6 Layouts](https://www.pythonguis.com/tutorials/pyqt6-layouts/)
  * [PyQt6 Menus](https://www.pythonguis.com/tutorials/pyqt6-actions-toolbars-menus/)
  * [PyQt6 Dialogs](https://www.pythonguis.com/tutorials/pyqt6-dialogs/)
  * [Multi-window PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/)
  * Qt Designer
  * [First Qt Designer app](https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/)
  * [Qt Designer Layouts](https://www.pythonguis.com/tutorials/pyqt6-qt-designer-gui-layout/)
  * [Dialogs in Qt Designer](https://www.pythonguis.com/tutorials/pyqt6-creating-dialogs-qt-designer/)
  * Concurrency
  * [Long-running tasks](https://www.pythonguis.com/tutorials/multithreading-pyqt6-applications-qthreadpool/)
  * [External processes](https://www.pythonguis.com/tutorials/pyqt6-qprocess-external-programs/)
  * Model Views
  * [Model Views](https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/)
  * [Pandas & Numpy Views](https://www.pythonguis.com/tutorials/pyqt6-qtableview-modelviews-numpy-pandas/)
  * Plotting
  * [Plotting With PyQtGraph and PyQt6](https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/)
  * [Plotting With Matplotlib and PyQt6](https://www.pythonguis.com/tutorials/pyqt6-plotting-matplotlib/)
  * QGraphics
  * [Vector Graphics](https://www.pythonguis.com/tutorials/pyqt6-qgraphics-vector-graphics/)
  * Custom Widgets
  * [Bitmap Graphics](https://www.pythonguis.com/tutorials/pyqt6-bitmap-graphics/)
  * [Custom Widgets](https://www.pythonguis.com/tutorials/pyqt6-creating-your-own-custom-widgets/)
  * [Animating Widgets](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/)
  * [Custom Designer Widgets](https://www.pythonguis.com/tutorials/pyqt6-embed-pyqtgraph-custom-widgets-qt-app/)
  * Further
  * [Modifying Signals](https://www.pythonguis.com/tutorials/pyqt6-transmitting-extra-data-qt-signals/)
  * [Taskbar apps](https://www.pythonguis.com/tutorials/pyqt6-system-tray-mac-menu-bar-applications/)
  * Packaging
  * [Packaging for Windows](https://www.pythonguis.com/tutorials/packaging-pyqt6-applications-windows-pyinstaller/)
  * [Packaging for macOS](https://www.pythonguis.com/tutorials/packaging-pyqt6-applications-pyinstaller-macos-dmg/)
  * Resources
  * [Books](https://www.pythonguis.com/books/)
  * Services
  * [Consulting](https://www.pythonguis.com/hire/)
  * [1:1 Coaching](https://www.pythonguis.com/live/)
  * [Contact](https://www.pythonguis.com/contact/)
  * [About](https://www.pythonguis.com/about/)
  * Libraries
  * [PySide6](https://www.pythonguis.com/pyside6/)
  * [PyQt5](https://www.pythonguis.com/pyqt5/)
  * [Streamlit](https://www.pythonguis.com/streamlit/)
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Animating Custom Widgets With QPropertyAnimation in PyQt6
Add dynamic visual effects to your custom widgets
by [Salem Al Bream](https://www.pythonguis.com/authors/salem-al-bream/) Last updated Mar 15 PyQt6 [ PyQt6 Custom Widgets ](https://www.pythonguis.com/pyqt6-tutorial/#pyqt6-custom-widgets)
#### [ PyQt6 Tutorial ](https://www.pythonguis.com/pyqt6-tutorial/) — [PyQt6 Custom Widgets](https://www.pythonguis.com/pyqt6-tutorial/#pyqt6-custom-widgets)
  * [QPainter and Bitmap Graphics in PyQt6](https://www.pythonguis.com/tutorials/pyqt6-bitmap-graphics/)
  * [Creating custom GUI widgets in PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-your-own-custom-widgets/)
  * [Animating Custom Widgets With QPropertyAnimation in PyQt6](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/)


This tutorial is also available for [PySide2](https://www.pythonguis.com/tutorials/pyside-animated-widgets/) , [PySide6](https://www.pythonguis.com/tutorials/pyside6-animated-widgets/) and [PyQt5](https://www.pythonguis.com/tutorials/qpropertyanimation/)
In the previous tutorial we looked at how you can [build custom widgets with PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-your-own-custom-widgets/).
The widget we built used a combination of layouts, nested widgets and a simple `QPainter` canvas to create a customized widget you can drop into any application.
But that just scratched the surface of what is possible with custom widgets in PyQt6. In this tutorial we'll look at how you can use Qt's `QPropertyAnimation` to enhance your custom widgets with visual effects and animations.
![Window with two animated checkbox toggles](https://i.imgur.com/zYneY8h.gif) _The custom animated toggle checkbox in action._
[QPropertyAnimation](https://doc.qt.io/qt-5/qpropertyanimation.html) allows you to change the value of an attribute of an object from a _startValue_ to a _endValue_ over a certain amount of time, and optionally following a custom _easingCurve_.
To do this the attribute you want to change must be defined as a Qt property. Before moving forward with `QPropertyAnimation` let's take a look at the _property_ concept in Python & Qt.
Table of Contents
  * [Properties](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/#properties)
    * [Python properties](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/#python-properties)
    * [Qt Properties](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/#qt-properties)
  * [QPropertyAnimation](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/#qpropertyanimation)
    * [QEasingCurve](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/#qeasingcurve)
    * [Common curves](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/#common-curves)
    * [Combining Multiple QPropertyAnimation animations](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/#combining-multiple-qpropertyanimation-animations)
    * [Animated Toggle "Replacement for QCheckBox"](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/#animated-toggle-replacement-for-qcheckbox)


## Properties
Objects in Python have _attributes_ which you can set and get values from. These can be defined on the class itself (making them _class attributes_) or on the object instance (making them _object attributes_). Default values for object attributes are usually set in the `__init__` method of the class, by assigning to `self.<attribute name>`. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
python ```
class MyObject:
  def __init__(self):
    self.my_attribute = 1
    self.my_attribute2 = 2
obj = MyObject()
print(obj.my_attribute)
print(obj.my_attribute2)
obj.my_attribute = 'hello'
print(obj.my_attribute)

```

If you run this example, you'll see the following output.
python ```
1
2
hello

```

When we create an instance of the `MyObject` class, the `__init__` method sets the two attributes `my_attribute` and `my_attribute2`. We can read these by accessing from the instance with `obj.my_attribute`, or set them by assigning to the attribute with `obj.my_attribute = <value>`.
While simple attributes are great for most use-cases, sometimes it is useful to be able to perform additional steps when getting and setting a value. For example, perhaps you want to send notifications in response to a change, or perform some kind of calculation on values as they are set. In these cases, you can use _properties_.
### Python properties
Python _properties_ behave outwardly exactly like attributes -- you can set and get them just as you would a normal attribute. Internally however each _property_ uses _getter_ and (optionally) _setter_ methods to handle the get and set operations respectively.
The _getter_ and _setter_ methods are separate from one another. The _getter_ is mandatory. If you don't define a _setter_ , the property is read only.
You define properties using the [property built-in](https://docs.python.org/3/library/functions.html#property). You can use this to define a property in two ways --
  1. Using `property()` as a _function_.
  2. Using `@property` as a _decorator_[1](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/#fn:1)


The following example shows how to define custom properties on a simple class using both these approaches.
  * decorator
  * function


python ```
class MyCustomClass:
  def __init__(self):
    self._value = None
  @property
  def value(self):
    print("getting the value", self._value)
    return self._value
  @value.setter
  def value(self, value):
    print("setting the value", value)
    self._value = value

obj = MyCustomClass()
a = obj.value    # Access the value
print(a)      # Print the value
obj.value = 'hello' # Set the value
b = obj.value    # Access the value
print(b)      # Print the value

```

python ```
class MyCustomClass:
  def __init__(self):
    self._value = None
  def getValue(self):
    print("getting the value", self._value)
    return self._value
  def setValue(self, value):
    print("setting the value", value)
    self._value = value
  value = property(getValue, setValue)

obj = MyCustomClass()
a = obj.value    # Access the value
print(a)      # Print the value
obj.value = 'hello' # Set the value
b = obj.value    # Access the value
print(b)      # Print the value

```

I prefer the `@decorator` syntax, since it keeps the method names the same as the value that you are setting/getting through the property -- but which you choose is up to you. If you run either example, you'll see the same output.
python ```
getting the value None
None
setting the value hello
getting the value hello
hello

```

When we access the `obj.value` property the `@property` decorated `value` method is run, printing the "getting the value" message. The value is returned as for any other object attribute. When we set the value, the `@value.setter` decorated method is run, printing the "setting the value" message.
The actual value is stored internally in a _private_ attribute `self._value` which we provide with a default value in the object `__init__`.
### Qt Properties
[Qt properties](https://doc.qt.io/qt-5/properties.html) work in a similar way, allowing us to define attributes on Qt classes and implement _getter_ and _setter_ methods to perform other functions. However, defining Qt properties also allows us to integrate with other Qt components.
To define a property in PyQt6 we use `pyqtProperty`, importable from the _QtCore_ module. As with Python properties, both can be used either as a _function_ or as a _decorator_.
The only difference with the Python approach, is that for Qt we must also provide a _type_ for the property -- in the example below `int` -- so Qt knows what type of data it can receive from/send to this property.
  * PyQt6 @decorator
  * PyQt6 function


python ```
from PyQt6.QtCore import pyqtProperty
class CustomObject(QObject):
  def __init__(self):
    super().__init__()
    self._value = 0    # the default value
  @pyqtProperty(int)
  def value(self):
    return self._value
  @value.setter
  def value(self, value):
    self._value = value

```

python ```
from PyQt6.QtCore import pyqtProperty
class CustomObject(QObject):
  def __init__(self):
    super().__init__()
    self._value = 0    # the default value
  def getValue(self):
    return self._value
  def setValue(self, value):
    self._value = value
  value = pyqtProperty(int, getValue, setValue)

```

As before, if we create an instance of this class, we can now get and set its _value_ member as if it is a normal attribute, e.g. --
python ```
obj = CustomObject()
obj.value = 7
print(obj.value)

```

One simple use for getter/setter methods in PyQt6 application is to emit signals when certain attributes are changed. For example, in the below snippet we've added a custom `pyqtSignal` to the class, and emit the new value whenever the _value_ changed.
python ```
from PyQt6.QtCore import pyqtProperty, pyqtSignal
class CustomObject(QObject):
  valueChanged = pyqtSignal(int)
  def __init__(self):
    super().__init__()
    self._value = 0    # the default value
  # change the setter function to be as:
  @value.setter
  def value(self, value):
    # here, the check is very important..
    # to prevent unneeded signal being propagated.
    if value != self._value:
      self._value = value
      self.valueChanged.emit(value)

```

Now we're familiar with using properties in PyQt6 (and Python) we'll now look at how we can use `QPropertyAnimation` to _animate_ properties and use this to create custom widget animations.
## _QPropertyAnimation_
So far we've defined simple properties with _setter_ and _getter_ methods that behave like simple attributes. We also added a side-effect to a setter method to emit a signal notifying of a change.
`QPropertyAnimation` is an interface built upon properties which can be used to animate -- or _interpolate_ -- between _start_ and _end_ values for a given property. Using this we can trigger a change and have a series of timed values set automatically.
If altering this property triggers an refresh of the widget (or we use the animated value in a `paintEvent()`) the widget will appear to animate.
Below is an example using `QPropertyAnimation` to animate the position of a simple `QWidget` -- a red filled square -- in a window. The animation updates the _position_ of the widget via `.pos` which automatically triggers a repaint by Qt.
python ```
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QPropertyAnimation, QPoint
class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.resize(600, 600)
    self.child = QWidget(self)
    self.child.setStyleSheet("background-color:red;border-radius:15px;")
    self.child.resize(100, 100)
    self.anim = QPropertyAnimation(self.child, b"pos")
    self.anim.setEndValue(QPoint(400, 400))
    self.anim.setDuration(1500)
    self.anim.start()

```

This will produce the following animation. By default the animation is _linear_ , with the `QWidget` moving towards the end position at a constant rate.
![Linear](https://i.imgur.com/iboUFmL.gif) _Single linear animation of a widget._
To create an animation using `QPropertyAnimation` you need to provide the following --
  1. tell the `QPropertyAnimation` which _object_ we want to animate, here `self.child`
  2. Provide a _property name_ here `b"pos"` (must be specified as _bytes_ `b"value"`)
  3. _[Optional]_ the _start_ value.
  4. The _end_ value.
  5. _[Optional]_ the _duration_ of interpolation _[in ms]_ , by default it's 250 ms.


The property you're animating _must_ have a _setter_ -- default properties on built-in widgets have setters, but for custom widgets you need to implement this.
Rather than a simple _linear_ animation you often want to add acceleration and deacceleration to the animation. This can be useful for creating widgets that feel _realistic_ and _physical_ , or to add interesting eye-catching effects. To add acceleration and deacceleration to an animation you use _easing curves_ via `QEasingCurve`.
### QEasingCurve
`QEasingCurve` is a Qt object which describes the transition -- or interpolation -- between two points. We can apply this transition to our animated properties to change how they behave.
In physical objects changes rarely happen at constant speed, but rather have a _acceleration_ and _deaccelerate_ phase. For example the speed of a falling object will start slow and increase over time due to gravity. A kicked ball accelerate rapidly -- but not instantly -- to full speed, and then deaccelerate due to air resistance. If you move an object with your hand you will accelerate it gradually before deaccelerating as you reach the destination for accuracy.
Try it in real life! Just grab any thing nearby and watch how your hand moves.
When moving a GUI component it can look _unnatural_ if it has constant speed. To allow us to define more natural looking behaviors, Qt provides us with several _common_ predefined curves.
The graphs may seem a little strange if you are not familiar with transition curves, so we'll look at them in a little more detail.
Each curve represents a _value_ vs. _time_ relationship, i.e. they show how a value will change _over time_. If the line is rising, the value is increasing, if the line is falling the value is decreasing. The _slope_ or _gradient_ of the line at any given point represents the _rate_ of change (how quickly the value is changing) at that particular point. Steeper slopes indicate faster changes, while a _horizontal_ line indicates the value is not changing, or _constant_ , at that point.
### Common curves
The default "curve" is not a curve at all, but a line. This **Linear** easing curve interpolates between two values in regular, consistent steps.
![QEasingCurve.Type.Linear](https://i.imgur.com/XfQ9v63.png) _`QEasingCurve.Type.Linear`_
Over**10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Next is one of the most common transition curves used in UIs -- **_InOutCubic_**. This starts with a low slope, which increases until the mid-point, before decreasing again. The effect of this curve a gradual change, which accelerates to the mid-point, before de-accelerating to a stop at the end.
![QEasingCurve.Type.InOutCubic](https://i.imgur.com/SwItQRT.png) _`QEasingCurve.Type.InOutCubic`_
There are also variants that only apply this transition in one direction (in, or out).
![QEasingCurve.Type.InCubic](https://i.imgur.com/R3gykov.png) _`QEasingCurve.Type.InCubic`_
![QEasingCurve.Type.OutCubic](https://i.imgur.com/7LikOZj.png) _`QEasingCurve.Type.OutCubic`_
The **OutInCubic** is the reverse of _InOutCubic_ and accelerates rapidly at the beginning, slowing down at the midpoint, then accelerates towards the end. This may be useful for slideshows or infinitely moving and changing components, where you want elements to rush into view and then pause before exiting.
![QEasingCurve.Type.OutInCubic](https://i.imgur.com/DiLBZet.png) _`QEasingCurve.Type.OutInCubic`_
Last one **_OutBounce_** , show funny out of box animation, give a look on its animated demo below.
![QEasingCurve.Type.InBounce](https://i.imgur.com/F8mruOz.png) _`QEasingCurve.Type.InBounce`_
![QEasingCurve.Type.OutBounce](https://i.imgur.com/hqHlkSx.png) _`QEasingCurve.Type.OutBounce`_
It's easier to understand these transitions if you see them in action. Below are a series of complete examples which you can experiment with, and adapt to the other transitions.
  * InOutCubic
  * OutInCubic
  * OutBounce


python ```
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QPropertyAnimation, QPoint, QEasingCurve
class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.resize(600, 600)
    self.child = QWidget(self)
    self.child.setStyleSheet("background-color:red;border-radius:15px;")
    self.child.resize(100, 100)
    self.anim = QPropertyAnimation(self.child, b"pos")
    self.anim.setEasingCurve(QEasingCurve.Type.InOutCubic)
    self.anim.setEndValue(QPoint(400, 400))
    self.anim.setDuration(1500)
    self.anim.start()

```

python ```
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QPropertyAnimation, QPoint, QEasingCurve
class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.resize(600, 600)
    self.child = QWidget(self)
    self.child.setStyleSheet("background-color:red;border-radius:15px;")
    self.child.resize(100, 100)
    self.anim = QPropertyAnimation(self.child, b"pos")
    self.anim.setEasingCurve(QEasingCurve.Type.OutInCubic)
    self.anim.setEndValue(QPoint(400, 400))
    self.anim.setDuration(1500)
    self.anim.start()

```

python ```
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QPropertyAnimation, QPoint, QEasingCurve
class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.resize(600, 600)
    self.child = QWidget(self)
    self.child.setStyleSheet("background-color:red;border-radius:15px;")
    self.child.resize(100, 100)
    self.anim = QPropertyAnimation(self.child, b"pos")
    self.anim.setEasingCurve(QEasingCurve.Type.OutBounce)
    self.anim.setEndValue(QPoint(400, 400))
    self.anim.setDuration(1500)
    self.anim.start()

```

![InOutCubic](https://i.imgur.com/KLMRQWt.gif) _Single InOutCubic animation of a widget._
![OutInCubic](https://i.imgur.com/UPGi26w.gif) _Single OutInCubic animation of a widget._
![OutBounce](https://i.imgur.com/mSdM5we.gif) _Single OutBounce animation of a widget._
The timing of each of these animations is identical (1.5 seconds) the difference in the animations is due to recording. In a Qt app each animation will take exactly the same time.
We've only looked at the most common of the easing curves. For the complete list refer to the Qt [QEasingCurve](https://doc.qt.io/qt-5/qeasingcurve.html) documentation and experiment! You will find several charts in the documentation to visualize their behavior.
### Combining Multiple `QPropertyAnimation` animations
These single animation curves are useful on their own, but sometimes you may want to combine multiple animations together to build more complex behaviors. To support this, Qt provides _QAnimationGroup_ , with which we can combine several animations and control when they _start_ and _stop_. There are two classes of animation group, which group animations in specific ways --
  * `QParallelAnimationGroup` groups animations to run at the same time
  * `QSequentialAnimationGroup` groups animations to run sequentially in order


`QAnimationGroup` is an _abstract_ class, so can't be used directly.
Below is an example moving a widget with two _sequential_ animations. The first moves the block as before, the second expands the size of the block horizontally.
python ```
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import (
  QPropertyAnimation, QSequentialAnimationGroup, QPoint, QSize)

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.resize(600, 600)
    self.child = QWidget(self)
    self.child.setStyleSheet("background-color:red;border-radius:15px;")
    self.child.resize(100, 100)
    self.anim = QPropertyAnimation(self.child, b"pos")
    self.anim.setEndValue(QPoint(200, 200))
    self.anim.setDuration(1500)
    self.anim_2 = QPropertyAnimation(self.child, b"size")
    self.anim_2.setEndValue(QSize(250, 150))
    self.anim_2.setDuration(2000)
    self.anim_group = QSequentialAnimationGroup()
    self.anim_group.addAnimation(self.anim)
    self.anim_group.addAnimation(self.anim_2)
    self.anim_group.start()

```

![Two sequential animations](https://i.imgur.com/lh913wX.gif) _Chaining two sequential animations one after another._
Alternatively, you can run multiple animations concurrently. The following example applies two animations that run in parallel. The first moves the block as before, the second fades the block in.
python ```
from PyQt6.QtWidgets import QWidget, QGraphicsOpacityEffect
from PyQt6.QtCore import QPropertyAnimation, QParallelAnimationGroup, QPoint

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.resize(600, 600)
    self.child = QWidget(self)
    effect = QGraphicsOpacityEffect(self.child)
    self.child.setGraphicsEffect(effect)
    self.child.setStyleSheet("background-color:red;border-radius:15px;")
    self.child.resize(100, 100)
    self.anim = QPropertyAnimation(self.child, b"pos")
    self.anim.setEndValue(QPoint(200, 200))
    self.anim.setDuration(1500)
    self.anim_2 = QPropertyAnimation(effect, b"opacity")
    self.anim_2.setStartValue(0)
    self.anim_2.setEndValue(1)
    self.anim_2.setDuration(2500)
    self.anim_group = QParallelAnimationGroup()
    self.anim_group.addAnimation(self.anim)
    self.anim_group.addAnimation(self.anim_2)
    self.anim_group.start()

```

![Two parallel animations](https://i.imgur.com/puhS9Q9.gif) _Running two concurrent animations on a single widget._
### Animated Toggle "Replacement for QCheckBox"
With these simple building blocks we have everything we need to build complex UI behaviors into our custom widgets. In this next part we'll take what we've learnt and use it to construct a fully-functional custom "Toggle" widget with animated behaviors.
The widget we're building inherits from `QCheckBox` and provides a drop-in replacement for it, adding an animated toggle switch with animated slider and a little bit of eye candy to highlight state changes. By inheriting from `QCheckBox` we get all the built-in checkbox behaviors for free, so we just need to deal with the visual parts.
To implement our design, we --
  * Define our colors (`QPen` and `QBrush`) using arguments and store them as object attributes. _This is not required, but saves us constructing them on every frame._
  * Override the `paintEvent(self, e)` which receives a `QPaintEvent`.
  * Define `QPropertyAnimation` and `QAnimationGroup` objects, to control the properties we want to animate.
  * Select the correct signals on which to trigger the animation.


Below is the complete code for our custom animated toggle checkbox.
python ```
from PyQt6.QtCore import (
  Qt, QSize, QPoint, QPointF, QRectF,
  QEasingCurve, QPropertyAnimation, QSequentialAnimationGroup,
  pyqtSlot, pyqtProperty)
from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtGui import QColor, QBrush, QPaintEvent, QPen, QPainter

class AnimatedToggle(QCheckBox):
  _transparent_pen = QPen(Qt.GlobalColor.transparent)
  _light_grey_pen = QPen(Qt.GlobalColor.lightGray)
  def __init__(self,
    parent=None,
    bar_color=Qt.GlobalColor.gray,
    checked_color="#00B0FF",
    handle_color=Qt.GlobalColor.white,
    pulse_unchecked_color="#44999999",
    pulse_checked_color="#4400B0EE"
    ):
    super().__init__(parent)
    # Save our properties on the object via self, so we can access them later
    # in the paintEvent.
    self._bar_brush = QBrush(bar_color)
    self._bar_checked_brush = QBrush(QColor(checked_color).lighter())
    self._handle_brush = QBrush(handle_color)
    self._handle_checked_brush = QBrush(QColor(checked_color))
    self._pulse_unchecked_animation = QBrush(QColor(pulse_unchecked_color))
    self._pulse_checked_animation = QBrush(QColor(pulse_checked_color))
    # Setup the rest of the widget.
    self.setContentsMargins(8, 0, 8, 0)
    self._handle_position = 0
    self._pulse_radius = 0
    self.animation = QPropertyAnimation(self, b"handle_position", self)
    self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
    self.animation.setDuration(200) # time in ms
    self.pulse_anim = QPropertyAnimation(self, b"pulse_radius", self)
    self.pulse_anim.setDuration(350) # time in ms
    self.pulse_anim.setStartValue(10)
    self.pulse_anim.setEndValue(20)
    self.animations_group = QSequentialAnimationGroup()
    self.animations_group.addAnimation(self.animation)
    self.animations_group.addAnimation(self.pulse_anim)
    self.stateChanged.connect(self.setup_animation)
  def sizeHint(self):
    return QSize(58, 45)
  def hitButton(self, pos: QPoint):
    return self.contentsRect().contains(pos)
  @pyqtSlot(int)
  def setup_animation(self, value):
    self.animations_group.stop()
    if value:
      self.animation.setEndValue(1)
    else:
      self.animation.setEndValue(0)
    self.animations_group.start()
  def paintEvent(self, e: QPaintEvent):
    contRect = self.contentsRect()
    handleRadius = round(0.24 * contRect.height())
    p = QPainter(self)
    p.setRenderHint(QPainter.RenderHint.Antialiasing)
    p.setPen(self._transparent_pen)
    barRect = QRectF(
      0, 0,
      contRect.width() - handleRadius, 0.40 * contRect.height()
    )
    barRect.moveCenter(QPointF(contRect.center()))
    rounding = barRect.height() / 2
    # the handle will move along this line
    trailLength = contRect.width() - 2 * handleRadius
    xPos = contRect.x() + handleRadius + trailLength * self._handle_position
    if self.pulse_anim.state() == QPropertyAnimation.State.Running:
      p.setBrush(
        self._pulse_checked_animation if
        self.isChecked() else self._pulse_unchecked_animation)
      p.drawEllipse(QPointF(xPos, barRect.center().y()),
             self._pulse_radius, self._pulse_radius)
    if self.isChecked():
      p.setBrush(self._bar_checked_brush)
      p.drawRoundedRect(barRect, rounding, rounding)
      p.setBrush(self._handle_checked_brush)
    else:
      p.setBrush(self._bar_brush)
      p.drawRoundedRect(barRect, rounding, rounding)
      p.setPen(self._light_grey_pen)
      p.setBrush(self._handle_brush)
    p.drawEllipse(
      QPointF(xPos, barRect.center().y()),
      handleRadius, handleRadius)
    p.end()
  @pyqtProperty(float)
  def handle_position(self):
    return self._handle_position
  @handle_position.setter
  def handle_position(self, pos):
    """change the property
    we need to trigger QWidget.update() method, either by:
      1- calling it here [ what we doing ].
      2- connecting the QPropertyAnimation.valueChanged() signal to it.
    """
    self._handle_position = pos
    self.update()
  @pyqtProperty(float)
  def pulse_radius(self):
    return self._pulse_radius
  @pulse_radius.setter
  def pulse_radius(self, pos):
    self._pulse_radius = pos
    self.update()

```

The `AnimatedToggle` class is quite complex. There are a few key points to notice.
  1. Because we're inheriting from `QCheckBox` it is essential that we override `hitButton()`. This defines the clickable area of our widget, and by a `QCheckBox` is only clickable in the area of the checkable box. Here we expand the clickable region to the entire widget, using `self.contentsRect()` so a click anywhere on the widget will toggle the state.
  2. Similarly it's essential we override `sizeHint()` so when we add our widget to layouts, they know an acceptable default size to use.
  3. You must set `p.setRenderHint(QPainter.RenderHint.Antialiasing)` to smooth the edges of things you draw, otherwise the outline will be jagged.
  4. In this example we trigger the animation using the `self.stateChanged` signal, which is provided by `QCheckBox`. This fires whenever the state (_checked_ or _unchecked_) of the widget changes. It is important to choose the right trigger to start the animation in order for the widget to feel intuitive.
  5. Since we're using `stateChanged` to _start_ the animation, if you check the state of the toggle as soon as it's been clicked it will give the correct value -- even if the animation is not yet complete.


Don't try to change the logical state inside `paintEvent` or from a `QPropertyAnimation`.
Save the above code in a file named `animated_toggle.py` and in the same folder save the following simple skeleton application (e.g. as `app.py`) which imports the `AnimatedToggle` class and creates a little demo.
python ```
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from animated_toggle import AnimatedToggle
app = QApplication([])
window = QWidget()
mainToggle = AnimatedToggle()
secondaryToggle = AnimatedToggle(
    checked_color="#FFB000",
    pulse_checked_color="#44FFB000"
)
mainToggle.setFixedSize(mainToggle.sizeHint())
secondaryToggle.setFixedSize(mainToggle.sizeHint())
window.setLayout(QVBoxLayout())
window.layout().addWidget(QLabel("Main Toggle"))
window.layout().addWidget(mainToggle)
window.layout().addWidget(QLabel("Secondary Toggle"))
window.layout().addWidget(secondaryToggle)
mainToggle.stateChanged.connect(secondaryToggle.setChecked)
window.show()
app.exec()

```

Running the code you should see the following demo appear in a window.
![Window with two animated checkbox toggles](https://i.imgur.com/zYneY8h.gif) _The custom animated toggle checkbox in action._
Try experimenting with the `AnimatedToggle` class, using alternative easing curves and building different animation sequences. See what you can come up with!
  1. well, decorators are functions too. [↩](https://www.pythonguis.com/tutorials/pyqt6-animated-widgets/#fnref:1 "Jump back to footnote 1 in the text")
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)


Mark As Complete 
[![Salem Al Bream](https://www.pythonguis.com/static/theme/images/authors/salem-al-bream.jpg)](https://www.pythonguis.com/authors/salem-al-bream/)
**Animating Custom Widgets With QPropertyAnimation in PyQt6** was written by [Salem Al Bream](https://www.pythonguis.com/authors/salem-al-bream/) . 
**Animating Custom Widgets With QPropertyAnimation in PyQt6** was published in [tutorials](https://www.pythonguis.com/tutorials/) on December 23, 2021 (updated March 15, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[widgets](https://www.pythonguis.com/topics/widgets/) [animation](https://www.pythonguis.com/topics/animation/) [qpropertyanimation](https://www.pythonguis.com/topics/qpropertyanimation/) [properties](https://www.pythonguis.com/topics/properties/) [custom-widgets](https://www.pythonguis.com/topics/custom-widgets/) [qcheckbox](https://www.pythonguis.com/topics/qcheckbox/) [qt](https://www.pythonguis.com/topics/qt/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [ pyqt6-custom-widgets](https://www.pythonguis.com/topics/pyqt6-custom-widgets/) [python](https://www.pythonguis.com/topics/python/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
