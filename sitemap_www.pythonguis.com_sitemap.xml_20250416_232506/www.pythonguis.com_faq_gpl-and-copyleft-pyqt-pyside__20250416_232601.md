# Content from: https://www.pythonguis.com/faq/gpl-and-copyleft-pyqt-pyside/

[](https://www.pythonguis.com/faq/gpl-and-copyleft-pyqt-pyside/#menu)
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
# Understanding the GPL and "Copyleft"
When Are Two Open Source Software Licenses Incompatible?
by [S.M. Oliva](https://www.pythonguis.com/authors/sm-oliva/) Last updated Mar 16 [ FAQ ](https://www.pythonguis.com/faq/)
In the last article I discussed the basic principles of copyright and how they related to software licenses such as the GPL and the LGPL. This time, let's examine the interaction _between_ "open source" and "free software" licenses. Specifically, how can the potential incompatibility between different licenses affect your own development work?
## License or Contract?
The GNU General Public License (GPL) is probably the most well-known of the "free software" licenses. There are two versions of the GPL still in use today: GPLv2 and GPLv3. (There is also the "Lesser" GPL or LGPLv2 and LGPLv3, which are commonly used for libraries and slightly modify the terms of their corresponding GPL versions.) The goal of these licenses is to promote "copyleft"--i.e., the idea that source code must be made freely available to anyone who wishes to use, modify, or redistribute a piece of GPL-licensed software.
Although styled as a "license," several courts in the United States have said the copyleft objectives of the GPL make it a "contract" that imposes obligations beyond the scope of a normal copyright license. For example, [a federal judge in California recently held](https://storage.courtlistener.com/recap/gov.uscourts.cacd.837808/gov.uscourts.cacd.837808.30.0.pdf) that U.S. copyright law did not prevent a third-party beneficiary under the GPL from asserting a breach of contract claim in state court. This case, _Software Freedom Conservancy v. Vizio, Inc._ , involves allegations that the manufacturer of a "smart TV" used software licensed under the GPLv2 and LGPLv2 but did not release the full source code to the third party upon request, as required by the licenses.
The manufacturer argued the case should have been dismissed because only the copyright holder--i.e., the original developers of the software--can sue for infringement under United States law. But the judge rejected that view, noting the GPLv3 and LGPLv3 expressly created a right for third parties to "receive source code," which actually goes against the traditional function of copyright, i.e., "to limit who may reproduce" a protected work.
## What You Need to Know Before "Mixing" Software Licenses
Looking at the GPL and LGPL as contracts also helps to illustrate the concept of license incompatibility. A contract imposes certain obligations on the parties to that agreement. If either party subsequently acts in a manner that violates these obligations, they may be found in breach of the contract.
The GPL itself is quite a lengthy document--more than 5,600 words--and most software developers are not trained to read or understand legal "code." But the basic idea is simple enough: If you receive any code licensed under the GPL and choose to modify and redistribute it in any way, you must also release the source code for your modifications.
The GPL is meant to prevent the use of licensed code in "proprietary" applications, i.e., software where the developer only makes an executable binary or "object code" available to users without the accompanying source code. And if you ask many "free software" advocates, they would likely tell you they want to create a world where all software is _exclusively_ licensed under GPL terms in this manner. 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
Of course, that isn't the world we live in. Many developers choose to license their software under terms that do not impose any significant reciprocal obligations on subsequent users. Such "permissive" licenses like MIT and Apache typically require little more than including a notice confirming the original developer's copyright in their code. Otherwise, the recipient is free to do whatever they wish with the licensed code--including using it in a proprietary application.
So what happens when you mix GPL and non-GPL code? According to the terms of the GPL, you still have to follow all of the rules applicable to its license. Otherwise the other license may be considered "incompatible." Likewise, if the other license includes its own additional restrictions, that too could make it incompatible with the GPL.
Keep in mind, license incompatibility may be claimed by the Free Software Foundation--the authors of the GPL--but that doesn't mean these issues have been heard or decided by a court. Still, as a developer you probably want to act in good faith and not combine GPL-licensed code with another license where incompatibility has been alleged. You also need to consider that if you adopt a license that potentially conflicts with the GPL, that will discourage others from using or incorporating any changes you have made to GPL-licensed code. 
[Create GUI Applications with Python & Qt6](https://www.pythonguis.com/pyqt6-book/) _by Martin Fitzpatrick_ — (PyQt6 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt6-book/) [Get the book](https://secure.pythonguis.com/01hf77bjcgxgghzq88pwh1nqe2/)
But what actually creates incompatibility? In many cases it may be seemingly trivial language. For example, older versions of Python--we're talking 1.6 through 2.1--had a license that stated its terms were governed by the laws of the State of Virginia. The FSF considered that incompatible with the GPL, which does not contain any such provision. (Modern Python is released under the Python Software Foundation license, which is considered GPL-compatible by the FSF.)
Other grounds that the [FSF has identified](https://www.gnu.org/licenses/license-list.en.html#NonFreeSoftwareLicenses) as creating GPL incompatibility include:
  * requiring users to obtain separate permission from the original authors before redistributing software;
  * prohibiting users from selling copies of software (or limiting the price they can charge for such copies);
  * limiting the use of software to certain types of organizations or purposes; and
  * the terms of the license are so vague that GPL compatibility cannot be readily ascertained.


You'll note in this list the item that says the GPL does not limit your ability to charge for copies of software developed using GPL-licensed code. Indeed, contrary to what many people believe, a "free software" license does not require you to give away your work. Nor does it prohibit you from developing commercial applications based on your work. In the next article, I'll explain this subject in greater detail, including why some software--like PyQt and Qt itself--are distributed under "dual" licensing schemes.
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyside6-book.png)](https://www.pythonguis.com/pyside6-book/)
[Take a look ](https://www.pythonguis.com/pyside6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyside6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1JL1CH9/)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![S.M. Oliva](https://www.pythonguis.com/static/theme/images/authors/s.m.-oliva.jpg)](https://www.pythonguis.com/authors/sm-oliva/)
**Understanding the GPL and "Copyleft"** was written by [S.M. Oliva](https://www.pythonguis.com/authors/sm-oliva/) . 
S.M. Oliva is a freelance writer with over 25 years experience authoring original content for the web. He also spent over a decade working as a paralegal in probate, trusts, and estate planning. 
**Understanding the GPL and "Copyleft"** was published in [faq](https://www.pythonguis.com/faq/) on June 17, 2022 (updated March 16, 2023) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
