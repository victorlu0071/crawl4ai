# Content from: https://www.pythonguis.com/faq/how-to-create-online-offline-database-together/

[](https://www.pythonguis.com/faq/how-to-create-online-offline-database-together/#menu)
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
# How to create online offline database together
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 [ FAQ ](https://www.pythonguis.com/faq/)
meshelleva4815 | 2020-08-20 02:39:49 UTC | #1
been a while here actually guys!
I actually need help on a project am working on. what I want to do is have my application use an sql database offline and also have an online database, something like Google mail, you know the contact backup in Google that works offline, you save a contact and it automatically updates it when you are connected to the internet. just something exactly like that. I don't know if am explanatory enough with this anyways but just something that works offline and can always migrate changes to the online database when connected.
I really don't know how or where to start from and I really hope to get my way around here. thanks in advance
martin | 2020-09-11 20:06:40 UTC | #2
Hey @meshelleva4815 thanks for your question, sorry for the delay -- I recently had a baby and I've been a little busy!
What you're describing is an online/offline sync. There are a lot of complications with doing this -- for example, can your app be run in multiple different places? If so, you need sync to work in two directions (from the server back to the client) rather than in one way. This also introduces the possibility of conflict.
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
Normally what you would do is --
  1. When starting the client should (try and..) sync the latest _complete_ state with the remote server. This can be done by retrieve the full db (if it is small), or by retrieving the sequence of operations since our last connect.
  2. Once synced, the client should record it's operations. For a database this can be a series of database operations (update/insert) etc. along with time (order) that they occurred.
  3. If connected, these can be sent to the server as they happen, _or_ batched. If disconnected, the client should keep a log of them, to send when the reconnection occurs.


If you have conflicts -- e.g. two separate clients have made conflicting changes, such as edited a field to different values -- you'll need some way to resolve this. Usually you would ask the user.
Hope that's enough to get started?
meshelleva4815 | 2020-09-27 13:59:30 UTC | #3
sorry am just replying to this. I replied back with a mail actually, didn't know it's not going to reflect here. thanks for the ideas you gave but my main problems now are: 1. understanding the working principles. that is how it works in the background. I guess I will definitely need two databases for it, but does it have to be same language(like sqlite, or mysql) for the two db, if same language is possible, do I just duplicate the one I have and paste in another folder for testing. 2. how do I create the log that helps keep track on the activities of the offline db since the last login...
now I have an idea and a rough picture of what I should do to start with your exposition but will be glade if you can help with this above 2concerns. thanks in advance boss. how is your baby...😁😁
martin | 2020-09-29 20:06:01 UTC | #4
Hey @meshelleva4815
It would definitely be easier for you if both databases were using the identical version/dialect. Firstly, for writing/debugging you can test both sides of the setup without needing to translate between them. Secondly, you know any operations you do one one can be done on the other -- different databases have different limitations, particularly around more complex field types, etc.
That said, using sqlite on your local database does have the advantage that it's very portable and doesn't require a separate database installation. It's a trade off, which will depend on what sort of data you're storing. For simple stuff, and sticking to standard SQL you should be OK with sqlite + mysql/postgresql.
As for how to log these changes... you have a lot of options. The simplest would be to simply log the SQL operations to file or and to submit these to the server (executing them) on reconnection. Another would be to define a custom "language" to describe the record mutations used to regenerate the SQL operation on the target system, but probably a bit redundant.
This only works if you have a single client though. Do you? If not, you're going to need to think of a way to handle and resolve conflicts -- e.g. if two clients edit the same record, and sync later, what do you do? As soon as one operation fails, any subsequent operation cannot be assumed to work (use transactions and you can roll back, but then?)
Mark As Complete 
For a complete guide to building GUI applications with Python, see our [PyQt6 tutorial](https://www.pythonguis.com/pyqt6-tutorial/). Using another library? We also have a [PyQt5 tutorial](https://www.pythonguis.com/pyqt5-tutorial/), [PySide6 tutorial](https://www.pythonguis.com/pyside6-tutorial/) and [PySide2 tutorial](https://www.pythonguis.com/pyside2-tutorial/).
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**How to create online offline database together** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/how-to-create-online-offline-database-together/Python books) on the subject. 
**How to create online offline database together** was published in [faq](https://www.pythonguis.com/faq/) on August 20, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
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
