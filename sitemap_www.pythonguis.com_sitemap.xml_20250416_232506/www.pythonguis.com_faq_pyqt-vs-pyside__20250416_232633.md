# Content from: https://www.pythonguis.com/faq/pyqt-vs-pyside/

[](https://www.pythonguis.com/faq/pyqt-vs-pyside/#menu)
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
# PyQt vs PySide Licensing
Everything you need to know about LGPL and GPL for your PySide/PyQt applications
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 01 [ FAQ ](https://www.pythonguis.com/faq/)
If you start building Python application with Qt5 you'll soon discover that there are in fact two packages which you can use to do this — PyQt and PySide. PyQt was developed by Phil Thompson of [Riverbank Computing Ltd.](https://www.riverbankcomputing.com/software/pyqt/intro) supporting versions of Qt going back to 2.x under a GPL license. Back in 2009 the developers of Qt wanted to have Python bindings for Qt available under the LGPL license (like Qt itself) and so started developing PySide.
Both packages are wrapping the same library — Qt — and so share 99.9% of their API. But there is one major difference: licensing.
PyQt | PySide  
---|---  
Current stable version (2019-06-23) | 6.1.1 | 6.1.2  
First stable release | Apr 2016 | Jul 2018  
Developed by | Riverbank Computing Ltd. | Qt  
License | GPL or commercial | LGPL  
Licensing is a confusing topic, so it's not surprising that it makes up the vast majority of questions I get about PySide vs. PyQt. In this short article I'll run through the most common questions and misconceptions about LGPL vs. GPL licensing and what it means for your applications.
Python itself is [licensed under the PSF License](https://docs.python.org/3/license.html#bsd0) (and a Zero-clause BSD license from 3.8.6 onwards). Neither license requires you to distribute your source code when distributing software created with Python, and the PSF only requires attribution when creating derivatives of Python itself.
## What is the GPL?
The GNU General Public License (GPL) is a free software license that guarantees end users the freedom to run, study, share, and modify their software. The key mechanism by which it does this is by ensuring that end users have access to the source code of applications they receive (as binaries).
If you are planning to release your software itself under the GPL, or you are developing software which will not be _distributed_ , the GPL requirement of PyQt5 is unlikely to be an issue. However, if you plan to distribute your software without distributing the source you will either need to purchase a commercial license from Riverbank for PyQt5 or use PySide2.
## What is the LGPL
The GNU Lesser General Public License (LGPL) is another free-software license published by the Free Software Foundation (FSF). This license is modeled on the GPL but allows developers to use software components released under the LGPL in their own software, without being required to release their source code. 
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
The LGPL license _does not_ require you to share the source code of your own applications, even if they are bundled with PySide2.
The LGPL does require you to distribute any changes you make to the PySide source code itself, but unless you're doing something very weird, you won't do this when making Python GUIs.
## Can I use PyQt for commercial applications?
Yes. There is a common misunderstanding that you _cannot_ use GPL licensed software in commercial applications. This isn't the case. The GPL does not prevent you from selling your software package, it merely requires you to share your source code with people who buy it.
If you use PyQt and _don't_ want to release your source code to customers, you will need the _Riverbank Commercial license_.
## Can I use PySide for commercial applications?
Yes, and you _don't_ need to release your source code to customers. The LGPL only requires you to release any changes you make to PySide itself.
## Why would someone buy my PyQt software if I'm giving away the source code?
Convenience. If you provide packaged installers for sale, the vast majority of people will want to use them rather than handle running/packaging the software from source themselves. That holds true even if your target audience is programmers: seriously, most people have better things to be doing with their time.
Again, note that the GPL _only_ requires that you make the source code available to those people who receive the binary version. If you are selling your software this means you are only required to give the source to people who have bought the application. Many companies providing GPL software provide the source to everyone, but this is not a requirement of the GPL. It's just easier.
## But my application contains super secret code!!! What then?
Then licensing is not the problem. While making the source code available of course makes it easier to read your _super secrets_ , whether you provide the source or not you must assume your code is readable. Python bytecode is easier to reverse to readable source than compiled languages -- although that is still no real impediment to motivated hackers.
For security you have to assume that any code you provide to end users is accessible, readable and modifiable. Licensing is irrelevant: it's as effective a security measure as saying "please don't!"
Remember, you only need to give your source code to people who have bought the software. If they share your software with someone else, the distribution requirement is on them.
If your application relies on code that absolutely must not be accessible to your users, keep it on a server you control and provide an API to be used by your application. The GPL used by PyQt places no restrictions on doing this. Doing this also allows you to control licensing/access to your application's features, for subscription-type services if you wish.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
Be aware though that this can be incredibly annoying for users, who might want to use your software offline or just have bad internet. Think really hard about whether your code is valuable enough to protect in this way. It probably isn't. Focus your time on building software people _want_ to pay for.
## Are there any other reasons to get a license?
Both Riverbank and Qt offer support to developers who buy their licenses.
## I started using the wrong library? What now!?
You can very easily migrate from PyQt to PySide and _vice versa_. Take a look at my [comparison and migration guide](https://www.pythonguis.com/faq/pyqt5-vs-pyside2/) for PyQt and PySide.
## Which should I use?
It's really up to you. The two key questions for more projects are --
  * How much of an issue is it to distribute the application source code?
  * Do you want to buy a license (or get paid support)?
  * For the application you're building, can you find good tutorials/examples in the library you're using?


The latter _usually_ favours starting with PyQt5: there are far more examples and tutorials available online because it's been around the longest. But my advice would be to get familiar -- as soon as possible -- with the differences so you can convert any code you find.
## One more time for the people at the back
The key points again --
  * PyQt5 is GPL licensed, PySide2 is LGPL licensed.
  * Both licenses have no effect on whether you can sell your software commercially. You can _sell_ GPL licensed software and LGPL licensed software.
  * Both licenses _may_ require you to share source code in specific circumstances, but LGPL is very unlikely to apply to a Python project.


For applications built with PyQt5 (GPL) if you distribute the software you must also make the source code of your software available to users (this doesn't mean making it publicly available, you can send it on request).
For applications build with PySide2 (LGPL) if you distribute the software you don't need to share the source of your application to your users. The one situation where you _do_ need to share source when you modify the source of the LGPL library (PySide) itself. You normally won't be doing this while building Python apps.
Any questions? Get in touch.
Interested in an in-depth guide? My [PySide6 book](https://www.pythonguis.com/pyside6-book) and [the PyQt6 book](https://www.pythonguis.com/pyqt6-book/) are available now!
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyside6-book/) _by Martin Fitzpatrick_ — (PySide6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyside6-book/) [Get the book](https://secure.pythonguis.com/01hf77d6fwm397veg5k5s46xcf/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**PyQt vs PySide Licensing** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/pyqt-vs-pyside/Python books) on the subject. 
**PyQt vs PySide Licensing** was published in [faq](https://www.pythonguis.com/faq/) on June 21, 2020 (updated April 01, 2025) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyside](https://www.pythonguis.com/topics/pyside/) [ pyqt6](https://www.pythonguis.com/topics/pyqt6/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ pyside2](https://www.pythonguis.com/topics/pyside2/) [qt](https://www.pythonguis.com/topics/qt/) [python](https://www.pythonguis.com/topics/python/) [qt5](https://www.pythonguis.com/topics/qt5/) [qt6](https://www.pythonguis.com/topics/qt6/)
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
