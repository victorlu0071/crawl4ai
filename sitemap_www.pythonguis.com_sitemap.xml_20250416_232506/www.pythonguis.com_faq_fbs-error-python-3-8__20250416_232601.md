# Content from: https://www.pythonguis.com/faq/fbs-error-python-3-8/

[](https://www.pythonguis.com/faq/fbs-error-python-3-8/#menu)
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
# Fbs error Python 3.8
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Sep 17 PyQt5 [ FAQ ](https://www.pythonguis.com/faq/)
Kentin | 2020-05-11 10:38:09 UTC | #1
It seems that I can't do `fbs freeze` from a fresh new `fbs startproject` I tried on python 3.8, 3.7 and 3.6 on windows.
``` File "C:\Users\prato\AppData\Local\Programs\Python\Python38\lib\runpy.py", line 192, in _run_module_as_main return _run_code(code, main_globals, None, File "C:\Users\prato\AppData\Local\Programs\Python\Python38\lib\runpy.py", line 85, in _run_code exec(code, run_globals) File "C:\Users\prato\AppData\Local\Programs\Python\envs\Creameme\Scripts\pyinstaller.exe__main__.py", line 9, in  File "c:\users\prato\appdata\local\programs\python\envs\creameme\lib\site-packages\PyInstaller__main__.py", line 111, in run run_build(pyi_config, spec_file, **vars(args)) File "c:\users\prato\appdata\local\programs\python\envs\creameme\lib\site-packages\PyInstaller__main__.py", line 63, in run_build PyInstaller.building.build_main.main(pyi_config, spec_file,** kwargs) File "c:\users\prato\appdata\local\programs\python\envs\creameme\lib\site-packages\PyInstaller\building\build_main.py", line 844, in main build(specfile, kw.get('distpath'), kw.get('workpath'), kw.get('clean_build')) File "c:\users\prato\appdata\local\programs\python\envs\creameme\lib\site-packages\PyInstaller\building\build_main.py", line 791, in build exec(code, spec_namespace) File "C:\Users\prato\Documents\Courses\PersonalProjects\Creameme\creamemegui\target\PyInstaller\test.spec", line 18, in  pyz = PYZ(a.pure, a.zipped_data, File "c:\users\prato\appdata\local\programs\python\envs\creameme\lib\site-packages\PyInstaller\building\api.py", line 98, in **init** self.**postinit**() File "c:\users\prato\appdata\local\programs\python\envs\creameme\lib\site-packages\PyInstaller\building\datastruct.py", line 158, in **postinit** self.assemble() File "c:\users\prato\appdata\local\programs\python\envs\creameme\lib\site-packages\PyInstaller\building\api.py", line 128, in assemble self.code_dict = { File "c:\users\prato\appdata\local\programs\python\envs\creameme\lib\site-packages\PyInstaller\building\api.py", line 129, in  key: strip_paths_in_code(code) File "c:\users\prato\appdata\local\programs\python\envs\creameme\lib\site-packages\PyInstaller\building\utils.py", line 652, in strip_paths_in_code consts = tuple( File "c:\users\prato\appdata\local\programs\python\envs\creameme\lib\site-packages\PyInstaller\building\utils.py", line 653, in  strip_paths_in_code(const_co, new_filename) File "c:\users\prato\appdata\local\programs\python\envs\creameme\lib\site-packages\PyInstaller\building\utils.py", line 660, in strip_paths_in_code return code_func(co.co_argcount, co.co_kwonlyargcount, co.co_nlocals, co.co_stacksize, TypeError: an integer is required (got type bytes) Traceback (most recent call last): File "C:\Users\prato\AppData\Local\Programs\Python\envs\Creameme\Scripts\fbs-script.py", line 11, in  load_entry_point('fbs==0.8.4', 'console_scripts', 'fbs')() File "C:\Users\prato\AppData\Local\Programs\Python\envs\Creameme\lib\site-packages\fbs__main__.py", line 17, in _main fbs.cmdline.main() File "C:\Users\prato\AppData\Local\Programs\Python\envs\Creameme\lib\site-packages\fbs\cmdline.py", line 32, in main fn(*args) File "C:\Users\prato\AppData\Local\Programs\Python\envs\Creameme\lib\site-packages\fbs\builtin_commands__init__.py", line 120, in freeze freeze_windows(debug=debug) File "C:\Users\prato\AppData\Local\Programs\Python\envs\Creameme\lib\site-packages\fbs\freeze\windows.py", line 18, in freeze_windows run_pyinstaller(args, debug) File "C:\Users\prato\AppData\Local\Programs\Python\envs\Creameme\lib\site-packages\fbs\freeze__init__.py", line 47, in run_pyinstaller run(args, check=True) File "C:\Users\prato\AppData\Local\Programs\Python\Python38\lib\subprocess.py", line 512, in run raise CalledProcessError(retcode, process.args, subprocess.CalledProcessError: Command '['pyinstaller', '--name', 'test', '--noupx', '--log-level', 'ERROR', '--noconfirm', '--windowed', '--icon', 'C:\Users\prato\Documents\Courses\PersonalProjects\Cream eme\creamemegui\src\main\icons\Icon.ico', '--distpath', 'C:\Users\prato\Documents\Courses\PersonalProjects\Creameme\creamemegui\target', '--specpath', 'C:\Users\prato\Documents\Courses\Persona lProjects\Creameme\creamemegui\target\PyInstaller', '--workpath', 'C:\Users\prato\Documents\Courses\PersonalProjects\Creameme\creamemegui\target\PyInstaller', '--additional-hooks-dir', 'C:\Users\ prato\AppData\Local\Programs\Python\envs\Creameme\lib\site-packages\fbs\freeze\hooks', '--runtime-hook', 'C:\Users\prato\Documents\Courses\PersonalProjects\Creameme\creamemegui\target\PyInst aller\fbs_pyinstaller_hook.py', 'C:\Users\prato\Documents\Courses\PersonalProjects\Creameme\creamemegui\src\main\python\main.py']' returned non-zero exit status 1.
python ```

-------------------------
Kentin | 2020-05-11 10:38:32 UTC | #2
Sorry I only have this error on python 3.8.
On 3.6 and 3.7 I have a simple `FileNotFoundError: Could not find api-ms-win-crt-multibyte-l1-1-0.dll`
I don't really know why since i have installed windows sdk (with visual studio to be safe)
-------------------------
Kentin | 2020-05-12 15:28:30 UTC | #3
I fixed it !
I indeed needed to add the directory containing this file to PATH. I'm so stupid.
Sorry for the spam and thank you for the tutorial.
-------------------------
gkssjovi | 2020-05-12 21:51:08 UTC | #4
I have the same problem.
Can you give me more details on how you solved the problem?
What folder you added to the PATH?
-------------------------
martin | 2020-05-13 09:00:12 UTC | #5
Hey @gkssjovi which of the errors are you having? If it's the first --

```

TypeError: an integer is required (got type bytes)
python ```

-- then this is because fbs (and PyInstaller) isn't yet compatible with Python 3.8.
-------------------------
gkssjovi | 2020-05-13 10:24:43 UTC | #6
Hi,
Thank you for the reply.
I'm really new on Python Development, I want to create a small app for me.
I have created this project following your tutorial

  /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 -m venv fbsenv
  ls fbsenv/
  fbsenv/bin/python3 -V
  Python 3.6.8
  source fbsenv/bin/activate
  (fbsenv) PythonTestApp pip3 install fbs PyQt5 PyInstaller==3.4
Then I have created the project
`fbs startproject`
When I use fbs freeze I got this error.
  (fbsenv) PythonTestApp fbs freeze
  Traceback (most recent call last):
   File "/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/bin/pyinstaller", line 11, in <module>
    load_entry_point('PyInstaller==3.4', 'console_scripts', 'pyinstaller')()
   File "/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/lib/python3.6/site-packages/PyInstaller/__main__.py", line 111, in run
    run_build(pyi_config, spec_file, **vars(args))
   File "/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/lib/python3.6/site-packages/PyInstaller/__main__.py", line 63, in run_build
    PyInstaller.building.build_main.main(pyi_config, spec_file, **kwargs)
   File "/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/lib/python3.6/site-packages/PyInstaller/building/build_main.py", line 838, in main
    build(specfile, kw.get('distpath'), kw.get('workpath'), kw.get('clean_build'))
   File "/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/lib/python3.6/site-packages/PyInstaller/building/build_main.py", line 784, in build
    exec(text, spec_namespace)
   File "<string>", line 36, in <module>
   File "/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/lib/python3.6/site-packages/PyInstaller/building/api.py", line 676, in __init__
    self.__postinit__()
   File "/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/lib/python3.6/site-packages/PyInstaller/building/datastruct.py", line 158, in __postinit__
    self.assemble()
   File "/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/lib/python3.6/site-packages/PyInstaller/building/api.py", line 707, in assemble
    dist_nm=inm)
   File "/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/lib/python3.6/site-packages/PyInstaller/building/utils.py", line 276, in checkCache
    os.makedirs(os.path.dirname(cachedfile))
   File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/os.py", line 210, in makedirs
    makedirs(head, mode, exist_ok)
   File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/os.py", line 220, in makedirs
    mkdir(name, mode)
  PermissionError: [Errno 13] Permission denied: '/Users/gkssjovi/Library/Application Support/pyinstaller/bincache00_py36_64bit/_struct'
  Traceback (most recent call last):
   File "/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/bin/fbs", line 11, in <module>
    load_entry_point('fbs==0.8.6', 'console_scripts', 'fbs')()
   File "/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/lib/python3.6/site-packages/fbs/__main__.py", line 17, in _main
    fbs.cmdline.main()
   File "/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/lib/python3.6/site-packages/fbs/cmdline.py", line 32, in main
    fn(*args)
   File "/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/lib/python3.6/site-packages/fbs/builtin_commands/__init__.py", line 114, in freeze
    freeze_mac(debug=debug)
   File "/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/lib/python3.6/site-packages/fbs/freeze/mac.py", line 22, in freeze_mac
    run_pyinstaller(args, debug)
   File "/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/lib/python3.6/site-packages/fbs/freeze/__init__.py", line 47, in run_pyinstaller
    run(args, check=True)
   File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/subprocess.py", line 438, in run
    output=stdout, stderr=stderr)
  subprocess.CalledProcessError: Command '['pyinstaller', '--name', 'HelloWorld', '--noupx', '--log-level', 'ERROR', '--noconfirm', '--windowed', '--icon', '/Users/gkssjovi/Desktop/PythonTestApp/target/Icon.icns', '--osx-bundle-identifier', 'com.martin.helloworld', '--distpath', '/Users/gkssjovi/Desktop/PythonTestApp/target', '--specpath', '/Users/gkssjovi/Desktop/PythonTestApp/target/PyInstaller', '--workpath', '/Users/gkssjovi/Desktop/PythonTestApp/target/PyInstaller', '--additional-hooks-dir', '/Users/gkssjovi/Desktop/PythonTestApp/fbsenv/lib/python3.6/site-packages/fbs/freeze/hooks', '--runtime-hook', '/Users/gkssjovi/Desktop/PythonTestApp/target/PyInstaller/fbs_pyinstaller_hook.py', '/Users/gkssjovi/Desktop/PythonTestApp/src/main/python/main.py']' returned non-zero exit status 1.
-------------------------
gkssjovi | 2020-05-13 10:31:57 UTC | #7
Sorry, I saw is working now if I use sudo command.
Probably when I have tried before it was a problem with the python version.
I have another problem now. I use dark them on my mac os, and it seems it not recognised when I run the app.
Can you point me to the wright direction since I'm very new on this.
-------------------------
wrzhu5551 | 2020-07-22 21:47:13 UTC | #8
Hi, I will also appreciate the detail of the fix: which directory you added to PATH to fix this issue. I am having the same issue. I have tried to add the directories of virtualenv and fbs project in PATH but still see the same error.
-------------------------
mike2750 | 2020-07-23 03:27:22 UTC | #9
@gkssjovi You will need to use PyQt 5.12.2 or higher as advised in martins article below.
https://www.pythonguis.com/blog/macos-mojave-dark-mode-support-pyqt5122/
I think by default the fbs tutorials use like 5.9.2. So you may need to uninstall and then install this version

```

pip3 install pyqt5==5.12.2
python ```

Then

```

fbs clean fbs freeze ```
mike2750 | 2020-07-23 03:39:59 UTC | #10 
[PyQt/PySide 1:1 Coaching with Martin Fitzpatrick](https://cal.com/mfitzp/60min-python-guis-coaching/) — Get one on one help with your Python GUI projects. Working together with you I'll identify issues and suggest fixes, from bugs and usability to architecture and maintainability. 
[Book Now](https://www.pythonguis.com/live/) [60 mins ($195)](https://cal.com/mfitzp/60min-python-guis-coaching/)
[quote="Kentin, post:2, topic:180"] api-ms-win-crt-multibyte-l1-1-0.dll [/quote] @ [gkssjovi](https://forum.learnpyqt.com/u/gkssjovi)
You will need to add the directory for where the sdk was installed to path like how i advised in this commit. If you haven't installed NSIS you should and also add its path
https://github.com/mherrmann/fbs-tutorial/pull/47/files
Over **10,000 developers** have bought Create GUI Applications with Python & Qt!
[![Create GUI Applications with Python & Qt6](https://www.pythonguis.com/static/theme/images/products/pyqt6-book.png)](https://www.pythonguis.com/pyqt6-book/)
[Take a look ](https://www.pythonguis.com/pyqt6-book/)
Downloadable ebook (PDF, ePub) & Complete Source code
Also available from [Leanpub](https://www.leanpub.com/pyqt6-book/) and [Amazon Paperback](https://www.amazon.com/dp/B0B1CK5ZZ1/)
screenshots ![Selection_999\(1281\)|261x500](https://www.pythonguis.com/static/faq/forum/fbs-error-python-3-8/7xLLjky5Bw0AJdnxV4O7a9GeZOS.png) ![Selection_999\(1282\)|413x467](https://www.pythonguis.com/static/faq/forum/fbs-error-python-3-8/kzA4E4HznSoYRle33xDxOpwR2iA.png) ![Selection_999\(1283\)|528x500](https://www.pythonguis.com/static/faq/forum/fbs-error-python-3-8/Dpqh4tWgiqoYkDum2Q6RsvAIBt.png) ![Selection_999\(1285\)|524x500](https://www.pythonguis.com/static/faq/forum/fbs-error-python-3-8/v5Qb3NTOFPPh5ZlwWAmaOdKKWpe.png)
@martin this information would also be super helpful to have in your video tutorials. It's been awhile since i watched them but if its not in there I'm sure it would make a good addition to show how to install the lightweght SDK, NSIS, and signtool and add their paths to system Path. I spent a few hours one day trying to sort it out cause im not really a windows guy and all the guides make it seem like it should be super simple and gloss over the how. It is easy after you have done it once but starting out the last you want to do i spend an hour digging about the internet for the best proper way to do this.
[Create GUI Applications with Python & Qt5](https://www.pythonguis.com/pyqt5-book/) _by Martin Fitzpatrick_ — (PyQt5 Edition) The hands-on guide to making apps with Python — Over 10,000 copies sold! 
[More info ](https://www.pythonguis.com/pyqt5-book/) [Get the book](https://secure.pythonguis.com/01hafjvt3nhfgsr558v1fxrx8m/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Fbs error Python 3.8** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/faq/fbs-error-python-3-8/Python books) on the subject. 
**Fbs error Python 3.8** was published in [faq](https://www.pythonguis.com/faq/) on May 11, 2020 (updated September 17, 2024) . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ pyqt5](https://www.pythonguis.com/topics/pyqt5/) [pyqt](https://www.pythonguis.com/topics/pyqt/) [ packaging](https://www.pythonguis.com/topics/packaging/) [fbs](https://www.pythonguis.com/topics/fbs/) [ pyqt5-packaging](https://www.pythonguis.com/topics/pyqt5-packaging/) [python](https://www.pythonguis.com/topics/python/) [qt](https://www.pythonguis.com/topics/qt/) [qt5](https://www.pythonguis.com/topics/qt5/)
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
