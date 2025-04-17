# Content from: https://www.pythonguis.com/write/style-guide/

[](https://www.pythonguis.com/write/style-guide/#menu)
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
# Python GUI's Style Guide Contribute your expertise
If you've come to this page, you may be interested in writing for Python GUIs. Here, you'll find the general style requirements that you must follow when writing for us. Please, read them carefully and consistently apply them in your writing.
Thanks!
## Write in Markdown
Always write tutorials in Markdown:
[Typora](https://www.typora.io/) is a good cross-platform editor, that has a semi-wysiwyg interface.
  * Use `-` for unordered lists in markdown (this helps minimize conflicts/unnecessary changes on PRs). In Typora, this is configurable in Preferences -> Markdown.
  * Include the code blocks as `.py` files in this repo, along with resources (e.g. images, ui files) so we can regenerate any videos/etc. in future.
  * When there are screencasts make sure you explain all the steps (assume the reader can't see the screencast)
  * Try and re-use existing code blocks for consistency across the site (there should be one way to do it).


## Writing Style
When you write articles for Python GUIs, follow the following guidelines:
  * Focus your writing on the reader.
  * Use American spelling in both, your code and your article's text. Check the [Merriam Webster](https://www.merriam-webster.com/) dictionary when in doubt.
  * Focus your writing on "We." In the end, "We are doing this together." However, sometimes you can directly refer to the reader as "You."
  * Avoid the following words and other similar ones because they can make our readers feel thumb if they don't get it:
    * Easy
    * Simple
  * Don't assume knowledge from the reader's side. So, avoid phrases like the following:
    * As you know...
    * As you might already know...
  * Use backtick to embed code objects, such as variables and function names, in your normal writing. Use them to embed file names too.
  * Use parentheses to denote functions and callable objects. For example, `app.exec()` instead of just `app.exec`.
  * Use font formats, such as **bold** and _italic_ sparingly. Use bold font for terms that you're defining yourself. Use italics to emphasize something. Don't use quotes "" for this purpose.
  * Avoid enclosing sentences in parentheses. Instead, extract your sentence and provide appropriate punctuation and capitalization. Use parentheses for one or two explanatory terms only.
  * Avoid walls of text by introducing **visual aids** like:
    * Code examples
    * Images and screenshots
    * Videos, animation, and screencasts
    * Diagrams
    * Vertical lists
    * Tables
  * Avoid long paragraphs and long sentences. Your paragraphs should have 3 to 5 sentences only.
  * Open your paragraphs with a topic sentence and add a few sentences to explain the topic in more detail.
  * Introduce every visual aid by telling the reader what they'll see. Use a colon to finish the intro sentence or paragraph.
  * Recap every vidual aid by telling the reader what they just saw. Of course, use other words and phrasing. This approach may sound repetitive but it's a great teaching technique that helps people remember the content.
  * Use the Oxford comma or [serial comma](https://en.wikipedia.org/wiki/Serial_comma) in a series of three or more terms.
  * Use title case for sections and subsections. Follow these rules:
    * Capitalize major words, such as nouns, pronouns, verbs, adjectives, adverbs, and some conjunctions.
    * Lowercase the conjunctions _and_ , _but_ , _for_ , _or_ , and _nor_.
    * Lowercase the articles _the_ , _a_ , and _an_.
    * Lowercase prepositions, regardless of length, except when they are stressed, are used adverbially or adjectivally, or are used as conjunctions.
    * Lowercase the words _to_ and _as_.
    * Lowercase the second word after a hyphenated prefix (e.g., Mid-, Anti-, Super-, etc.) in compound modifiers (e.g., Mid-year, Anti-hero, etc.).
    * Always capitalize the first of titles and subtitles.
  * Always write your vertical lists in parallel structure. List items should be equivalent. If you start with a noun, then all your items should start with a noun. If you start with a verb in whatever form, then all the items should start with verbs in the same form.
  * Don't add the final period to your vertical list items if they're sentence fragments. Add a final period to all your vertical list items only if they're complete sentences (with subject and predicate).
  * Write your Table of Content in parallel structure as well.
  * Use H2 and H3 headings for your sections. Avoid using H4 headings.


## Use Custom Tags
To support all the features required, we extend Markdown with a few simple tags:
  * Start a line with `INFO:`, `WARNING:`, `TIP:` to create an admonition boxout. It must be a single line only, but Markdown is fully supported.
  * `@ [video URL]` to embed a video
  * `@ [imgur id]` to embed an imgur image
  * `@ [gfycat id]` to embed an gfycat image


## Use Multicode-blocks
Multicode-blocks are tabbed blocks containing multiple code blocks. These are used, for example, to provide both PyQt5 and PySide2 code examples.
These can be added to a tutorial by running two code blocks immediately after one another without a space between them.
The label on the tab is taken from the text immediately following the language name, after a colon, e.g. `python:PyQt5` will set the language to `python` and add "PyQt5" as the label on the tab. You can do the same for other languages, e.g. `bash:PyQt5` when different libraries use different command line tools.
## Format Code Examples
All the code examples on the site must meet the following requirements:
  * Make all your code examples PEP8 compliant.
  * Format your code examples using [Black](https://pypi.org/project/black/).
  * Use Python 3 syntax.
  * Remove any unused imports.
  * Sort your imports with [`isort`](https://pypi.org/project/isort/)
  * Provide working example source files for any code blocks & images.
  * Use descriptive and realistic names for variables, functions, classes, and so on. Avoid names like `my_button`, `my_variable`, and others that use the `my` prefix.
  * Use a uniform naming style in individual code files. If you're working on a GUI app using Qt's camel case style, then make your variables and object in the containing file use the same convention. If you're working on a pure Python file, then use Python's naming style (snake case with underscores).


## Format Images, Videos, and Animations
All our images, videos, and animations should be properly formatted:
  * Images should be stored in the same folder as the markdown file.
  * Animations (gif, video) is not currently supported so these must use an external service (e.g. [imgur.com](https://imgur.com/)).


If you have any questions about the style guide or writing process, you can contact the editor.
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
