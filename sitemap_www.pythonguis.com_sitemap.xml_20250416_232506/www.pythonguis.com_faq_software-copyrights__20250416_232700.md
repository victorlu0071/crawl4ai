# Content from: https://www.pythonguis.com/faq/software-copyrights/

[](https://www.pythonguis.com/faq/software-copyrights/#menu)
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
# The Basics of Software Copyrights
Why Do You Need to Bother With Licensing at All?
by [S.M. Oliva](https://www.pythonguis.com/authors/sm-oliva/) Last updated Mar 16 [ FAQ ](https://www.pythonguis.com/faq/)
When you're just starting out in software development, the last thing you want to do is worry about licensing. This is a subject fraught with legal and political battles that have been going on for decades. Some people think you should only use "free" or "copyleft" licenses like the GPL, while others feel the best route is to stick with "permissive" licenses like MIT or BSD.
Licensing is something you need to be aware of not only when developing your code--which inevitably requires you to use code developed and licensed by others--but also when deciding how to release your own software. Many developers treat licensing as an afterthought and that can get them into trouble if they select a license that is deemed "incompatible" with some other license.
While licensing is a very detailed and complex subject--far beyond the scope of a single article--here are a few basic principles to understand as you wander into this proverbial minefield.
## How Long Does Copyright Last?
Let's start with a basic question: Why do we need licensing at all? The simple answer is copyright. Any code that you write is protected by copyright in the United States, the United Kingdom, the European Union, and indeed most countries around the world. Copyright means that you, as the author of an original work, have the exclusive right to decide how others may use, copy, or distribute that work.
Historically, copyright was something that required an author to register their work with a government agency, such as the U.S. Copyright Office. This registration then guaranteed copyright protection for a fixed number of years and might need to be renewed at a later date. But today, copyright is generally considered "automatic" from the moment the work is created. In other words, if you just write some original code and save it to your computer--or push it to a remote repository like GitHub--it is now protected by copyright without you having to take any further action. While it is customary to affix a copyright notice, e.g. "Copyright 2022 Jane Smith," even that is not technically required anymore.
And unlike the old days, copyright today lasts a very long time. Most nations are parties to a treaty known as the [Berne Convention](https://www.wipo.int/treaties/en/ip/berne/), which sets certain minimum standards for copyright protection. Under the Convention, copyright for written works like software code must last _at least_ for the lifetime of the author plus another 50 years after their death. But this is just a minimum. The United States, the European Union, and many other Berne signatories have actually increased the term to 70 years after the author's death.
Now, those are the rules that apply to individual authors. A "work-for-hire," such as code written by a corporation's employees, are subject to different copyright terms. In the United States, such copyrights last 95 years from the date of first publication or 120 years after creation, whichever is shorter. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
In practice, these rules mean that code written for some of the first microcomputers in the early 1980s can remain under copyright well into the 22nd century! And given how even a simple program today may depend on dozens--if not hundreds--of previously written pieces of code, it would be impractical for you, as a developer, to seek out and get permission from each original author to reuse their work. This is where licensing comes into play.
## Setting Conditions for Using Your Code
A software license sets the conditions by which someone can use your code to create "derivative works," i.e., a new work that incorporates your copyrighted material. As a developer, you also rely on such licenses to create your own code using software developed by others. A license is effectively a contract between the copyright holder and the person who wishes to take advantage of the license.
Many developers--especially those who want to sell their software--offer different types of licenses for their code. For example, [Riverbank Computing, Ltd.](https://www.riverbankcomputing.com/commercial/license-faq), the company that publishes PyQt, does so under a "dual" license. One license is for use of PyQt in proprietary applications, i.e., software where the developer does not release their source code to the end user. The other license is the GNU General Public License v. 3.0 (GPLv3), which can be used with non-proprietary applications.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
Licenses like the GPLv3 are sometimes called [copyleft](https://www.gnu.org/licenses/copyleft.en.html) licenses. The word "copyleft" is a term of art that has no legal significance. Copyleft is basically a preferred outcome under copyright--i.e., preserving the ability of both the original author and any subsequent users to freely modify and redistribute source code. But this is all still rooted in the principles of copyright law. If you violate the terms of a software license, even a relatively permissive one, you are also violating the copyright of the developer who released their software under that license.
One way that you can violate copyright, perhaps without realizing it, is to release your own code under a license that is incompatible with the license of other code used in your project. Indeed, you may read that certain licenses are considered "open source" yet are not compatible with the GPLv3. Does this mean you must always use the same license? Not necessarily. For example, PySide is released under the Lesser GPL or LGPL license. The terms of this license differs from the GPLv3 but the two are still considered compatible in most cases. In the next article, we'll examine these differences in more detail.
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![S.M. Oliva](https://www.pythonguis.com/static/theme/images/authors/s.m.-oliva.jpg)](https://www.pythonguis.com/authors/sm-oliva/)
**The Basics of Software Copyrights** was written by [S.M. Oliva](https://www.pythonguis.com/authors/sm-oliva/) . 
S.M. Oliva is a freelance writer with over 25 years experience authoring original content for the web. He also spent over a decade working as a paralegal in probate, trusts, and estate planning. 
**The Basics of Software Copyrights** was published in [faq](https://www.pythonguis.com/faq/) on June 15, 2022 (updated March 16, 2023) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ licensing](https://www.pythonguis.com/topics/licensing/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [pyside](https://www.pythonguis.com/topics/pyside/) [gpl](https://www.pythonguis.com/topics/gpl/) [copyright](https://www.pythonguis.com/topics/copyright/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/)
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
