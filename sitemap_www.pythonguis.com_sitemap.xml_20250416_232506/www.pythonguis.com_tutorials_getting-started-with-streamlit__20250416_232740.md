# Content from: https://www.pythonguis.com/tutorials/getting-started-with-streamlit/

[](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/#menu)
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
  * [Tkinter](https://www.pythonguis.com/tkinter/)
  * [PySide2](https://www.pythonguis.com/pyside2/)


  * Search Python GUIs


[](https://www.pythonguis.com "Python GUIs")
Search Python GUIs
# Getting Started with Streamlit
Build your first Streamlit app and explore some basic features
by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) Last updated Apr 02 Streamlit [ Tutorials ](https://www.pythonguis.com/tutorials/)
Streamlit is an open-source Python library that makes it easy to create and share custom web apps for machine learning and data science. In this tutorial we'll take a first look at Streamlit, installing it, getting it set up and building a simple app.
Table of Contents
  * [Installing Streamlit](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/#installing-streamlit)
  * [Add title, headings, and paragraphs](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/#add-title-headings-and-paragraphs)
    * [Adding Titles](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/#adding-titles)
    * [Adding Headings](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/#adding-headings)
    * [Adding Paragraphs](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/#adding-paragraphs)
  * [Adding different kinds of buttons to the Streamlit app](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/#adding-different-kinds-of-buttons-to-the-streamlit-app)
    * [Basic Button](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/#basic-button)
    * [Download Button](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/#download-button)
    * [Radio Buttons for Options](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/#radio-buttons-for-options)
  * [Adding slider](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/#adding-slider)
  * [Adding the dropdown menu in the app](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/#adding-the-dropdown-menu-in-the-app)
  * [Adding a Sidebar in Streamlit](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/#adding-a-sidebar-in-streamlit)
  * [Creating a simple web app using Streamlit](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/#creating-a-simple-web-app-using-streamlit)


## Installing Streamlit
Because Streamlit is a third-party library, we need to install it on our system before using it. Streamlit can be easily installed using pip. Open your terminal (Mac/Linux) or Command Prompt (Windows) and type the following command:
bash ```
pip install streamlit

```

This command will download and install Streamlit and its dependencies. Once the installation is complete, we can create a simple Streamlit app.
Open your editor and create a file named `app.py`. This file will be our main Python file to write and edit the Streamlit app. In order to make sure that Streamlit is running on our system, let us import it and run the app.
python ```
import streamlit as st

```

To run the app, open the terminal in the same directory and enter the following commands
bash ```
streamlit run app.py

```

This command will open a new tab in your default browser. It will be empty right now, but this is where we'll be building the interface of our app.
## Add title, headings, and paragraphs
Streamlit allows you to create clean and structured web apps with ease, making it perfect for data visualization and interactive dashboards. One of the key features that make Streamlit user-friendly is its ability to format text with titles, headings, and paragraphs. This tutorial will guide you through how to add these elements to your Streamlit app. 
#### Never miss an update
Enjoyed this? Subscribe to get new updates straight in your Inbox.
Subscribe 
You can unsubscribe anytime. Just ham, no spam.
### Adding Titles
Titles in Streamlit are added using the `st.title()` function. This function displays the text in a large, bold font, ideal for the heading of your app.
python ```
import streamlit as st
st.title("This is the title of our app")

```

Save the changes and refresh the browser tab to see the changes. This will create a large, centered title at the top of your app.
![The streamlit application open in your browser](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/first-app.png) _The streamlit application open in your browser_
### Adding Headings
Streamlit provides several levels of headings to structure your content, similar to HTML's `<h1>` to `<h6>` tags. You can use `st.header()` and `st.subheader()` for the primary and secondary sections, respectively.
python ```
import streamlit as st
st.title("This is the title of our app")
st.header("This is a Header")
st.subheader("This is a Subheader")

```

In this code, we use `st.header()` to create the prominent heading, ideal for section titles. Then we call `st.subheader()` to create a slightly smaller heading, suitable for subsections under a header.
Save the changes and refresh the browser. It will create the following changes to our app.
![Subheaders added through Streamlit](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/subheaders.png) _Subheaders added through Streamlit_
### Adding Paragraphs
To add regular text or paragraphs, use the `st.write()` function. This function can handle text, Markdown, and even complex objects like data frames.
python ```
import streamlit as st
st.title("This is the title of our app")
st.header("This is a Header")
st.subheader("This is a Subheader")
st.write("You can write text here and it will appear as a paragraph.")

```

Save the change and refresh the browser tab.
![Paragraph text added through Streamlit](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/paragraph-text.png) _Paragraph text added through Streamlit_
## Adding different kinds of buttons to the Streamlit app
Buttons are fundamental interactive elements in any web application. Streamlit provides simple yet versatile options for adding buttons to your app, enabling users to trigger actions, navigate between sections, or submit data. This tutorial will guide you through adding different kinds of buttons to your Streamlit app and how to handle user interactions.
### Basic Button
The simplest button in Streamlit is created using the `st.button()` function. It generates a clickable button that can trigger specific actions.
python ```
import streamlit as st
st.title("This is the title of our app")
st.button("Click Me")

```

![A button in your Streamlit UI](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/button.png) _A button in your Streamlit UI_
Notice that a small button is shown in our app. Right now, it is a static button which mean nothing will happen when we click the button. To make it interactive, we have to use conditional statements. When the button is clicked in Streamlit app, it returns a True value. So, we can use this in our conditional statement.
python ```
import streamlit as st
st.title("This is the title of our app")
button = st.button("Click Me")
if button: # button is True if clicked
  st.write("You clicked the button")

```

We create the button by calling `st.button()` passing in the label as a string "Click Me". If the button is clicked in the browser, the value of `button` will be `True` and the `if` branch will be executed: outputting the message to the UI.
![A button with clickable behavior](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/clickable-button.png) _A button with clickable behavior_
### Download Button
You can create a download button using `st.download_button()`, which allows users to download files directly from your app.
python ```
import streamlit as st
st.title("This is the title of our app")
text_file_content = "This is a sample text file. This content will be downloaded as a text file."
st.download_button(
  label="Download Text File",
  data=text_file_content,
  file_name="sample.txt",
  mime="text/plain"
)

```

In this code we use `st.download_button()` to creates a button that, when clicked, lets users download a file. The parameters of the download button are:
  * `label`: The text on the button.
  * `data`: The content to be downloaded.
  * `file_name`: The name of the file.
  * `mime`: The MIME type of the file (e.g., `text/plain`).


This gives the following update UI:
![A download button](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/download-button.png) _A download button_
### Radio Buttons for Options
Radio buttons allow users to select one option from a set of choices. Streamlit provides this functionality using `st.radio()`.
python ```
import streamlit as st
st.title("This is the title of our app")
choice = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
if choice == "Option 1":
  st.write("You selected Option 1")
elif choice == "Option 2":
  st.write("You selected Option 2")
else:
  st.write("You selected Option 3")

```

In this case we used `st.radio()` to create a set of radio buttons. The selected option is stored in the variable `choice`, which you can use to control the app's behavior.
This will give the following result:
![Radio buttons in your Streamlit UI](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/radio-buttons.png) _Radio buttons in your Streamlit UI_
## Adding slider
A slider in Streamlit is a UI element that allows users to select a value by moving a handle along a track. This is particularly useful for adjusting parameters in data visualizations, setting thresholds, or selecting ranges for filtering data.
Streamlit provides `st.slider()` which you can use to add sliders to your app. This function supports both single-value and range sliders.
A single value slider allows users to select a single value within a specified range. Here’s how to add a simple slider to your Streamlit app:
python ```
import streamlit as st
st.title("This is the title of our app")
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is: {age}")

```

Here we've used `st.slider()` to add a slider to your app. The first argument is the label for the slider. The next two arguments define the minimum and maximum values, while the the last argument is the default value the slider starts at.
![A simple slider in your Streamlit UI](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/slider.png) _A simple slider in your Streamlit UI_
[Packaging Python Applications with PyInstaller](https://www.pythonguis.com/packaging-book/) _by Martin Fitzpatrick_ — This step-by-step guide walks you through packaging your own Python applications from simple examples to complete installers and signed executables. 
[More info ](https://www.pythonguis.com/packaging-book/) [Get the book](https://secure.pythonguis.com/01hf77hrbf5v8z5kjtwbhmbwjz/)
Streamlit also allows you to create a range slider, where users can select an upper and lower bound of a range. This is useful for filtering where you want to select some data within the given range. You can add a range slider to your application as follows:
python ```
import streamlit as st
st.title("This is the title of our app")
start, end = st.slider("Select a range of values:", 0, 100, (20, 80))
st.write(f"Selected range: {start} to {end}")

```

![A range slider in your Streamlit UI](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/range-slider.png) _A range slider in your Streamlit UI_
Here, `st.slider()` is used to create a range slider by passing a tuple `(20, 80)` as the default value. The tuple represents the initial _start_ and _end_ values of the slider range.
When you run this app, the slider will allow users to select a range between 0 and 100, starting with a default range from 20 to 80. The selected range is then displayed on the app. The initial and returned tuple represent the selected range in the slider.
Don't confuse this with a Python `range`! Unlike a Python range, they are inclusive: that is, if you select 80 as the upper bound, then 80 will be returned (not 79).
## Adding the dropdown menu in the app
Dropdown menus are a powerful and versatile UI component that allows users to select an option from a predefined list. Streamlit makes it easy to add dropdown menus to your web app, providing an intuitive way for users to interact with your data or application.
Streamlit provides a straightforward way to add dropdown menus through the `st.selectbox()` function. This function not only adds a dropdown to your app but also allows you to capture the selected value for further processing. Let’s start with a simple example where users can choose their favorite fruit from a list:
python ```
import streamlit as st
st.title("This is the title of our app")
fruit = st.selectbox("Select your favorite fruit:", ["Apple", "Banana", "Orange", "Grapes", "Mango"])
st.write(f"You selected: {fruit}")

```

![A dropdown box in your Streamlit UI](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/dropdown.png) _A dropdown box in your Streamlit UI_
In the above code we used `st.selectbox()` to creates a dropdown menu. The first argument is the label for the dropdown and the second argument is the list of options users can choose from.
## Adding a Sidebar in Streamlit
A sidebar is an additional panel that appears on the left side of the app. It can be used to house interactive widgets like sliders, buttons, and dropdowns, or to display information that should be easily accessible throughout the app.
This allows the main part of the app to focus on displaying results, visualizations, or other content, while the sidebar handles user inputs and navigation.
Streamlit makes it easy to add a sidebar using the `st.sidebar attribute`, which you can use to place any widget or content into the sidebar.
To add a sidebar to your Streamlit app, you can use the `st.sidebar` attribute followed by the widget you want to add. Here’s a basic example of adding a sidebar with a simple slider.
python ```
import streamlit as st
st.title("This is the title of our app")
age = st.sidebar.slider("Select your age:", 0, 100, 25)
st.write(f"Your age is: {age}")

```

This will produce the following output:
![Adding a sidebar to your Streamlit UI](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/sidebar.png) _Adding a sidebar to your Streamlit UI_
`st.sidebar.slider()` is a function that adds a slider widget to the sidebar instead of the main page. The rest of the code works just like a regular slider.
You can add multiple widgets to the sidebar, allowing users to control various aspects of your app from one convenient location. Here’s an example with a dropdown menu, a slider, and a button.
python ```
import streamlit as st
st.title("This is the title of our app")
color = st.sidebar.selectbox("Select a color:", ["Red", "Green", "Blue"])
# Add a slider to the sidebar
level = st.sidebar.slider("Select the intensity level:", 0, 100, 50)
# Add a button to the sidebar
if st.sidebar.button("Apply Settings"):
  st.write(f"Settings applied: Color={color}, Level={level}")

```

The updated UI is shown below:
![Multiple widgets in the sidebar of your Streamlit UI](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/sidebar-multiple.png) _Multiple widgets in the sidebar of your Streamlit UI_
In this code we used `st.sidebar.selectbox()` to add a dropdown menu to the sidebar, `st.sidebar.slider()` to add a slider to the sidebar and finally `st.sidebar.button()` to add a button to the sidebar. The the action associated with the button click is displayed on the main page.
## Creating a simple web app using Streamlit
Now, we will combine all the basic concepts that we have learned about Streamlit and put them together to create a simple streamlit web app.
In this example we'll being using the Iris dataset. This data is widely available, for example [from this repository](https://github.com/mwaskom/seaborn-data). Download [the csv file](https://github.com/mwaskom/seaborn-data/raw/refs/heads/master/iris.csv) into the same folder as your Streamlit app and then we can load it using pandas.
Using this dataset we're going to build a data exploration dashboard with the following features.
  * **Dataset Display** showing the full Iris dataset.
  * **Sidebar Controls** ** to allow users to select a feature and filter the data based on that feature using sliders.
  * **Filtered Data Display** to show the filtered dataset based on the user's input.
  * **Basic Statistics** like mean, median, standard deviation, calculated live based on the selected feature in the filtered dataset.


The UI is simple, but shows some of the neat features of Streamlit.
python ```
import streamlit as st
import pandas as pd
# Load the Iris dataset
df = pd.read_csv('iris.csv')
# Set the title of the app
st.title("Iris Dataset Explorer")
# Display the entire dataframe
st.write("### Full Iris Dataset")
st.dataframe(df)
# Sidebar configuration
st.sidebar.header("Filter Options")
# Feature selection
feature = st.sidebar.selectbox("Select a feature to filter by:", df.columns[:-1])
# Range selection based on the selected feature
min_value = float(df[feature].min())
max_value = float(df[feature].max())
range_slider = st.sidebar.slider(f"Select range of {feature}:", min_value, max_value, (min_value, max_value))
# Filter the dataframe based on the selected range
filtered_df = df[(df[feature] >= range_slider[0]) & (df[feature] <= range_slider[1])]
# Display the filtered dataset
st.write(f"### Filtered Iris Dataset by {feature} between {range_slider[0]} and {range_slider[1]}")
st.dataframe(filtered_df)
# Display basic statistics for the filtered data
st.write(f"### Statistics for {feature}")
st.write(filtered_df[feature].describe())

```

The `iris.csv` path is relative, so will only work if you run the script from the same folder. If you want to run it from elsewhere (a parent folder) you will need to modify the path.
Below is the final UI, showing the sidebar on the left and the full & filtered Iris dataset in the middle panel. Change the feature and adjust the parameter to filter the data.
![Data filtering demo using Pandas & Streamlit](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/streamlit-data-demo.png) _Data filtering demo using Pandas & Streamlit_
This simple Streamlit app provides an easy way to explore the Iris dataset. It demonstrates how you can use sidebars, dropdown menus, and sliders to create an interactive and user-friendly data exploration tool.
You can take this simple app and adapt it for other data sets or expand it with additional features, such as advanced filtering or data manipulation options.
The complete guide to packaging Python GUI applications with PyInstaller.
[![Packaging Python Applications with PyInstaller](https://www.pythonguis.com/static/theme/images/products/packaging-book.png)](https://www.pythonguis.com/packaging-book/)
[Take a look ](https://www.pythonguis.com/packaging-book/)
Mark As Complete 
[![Martin Fitzpatrick](https://www.pythonguis.com/static/theme/images/authors/martin-fitzpatrick.jpg)](https://www.pythonguis.com/authors/martin-fitzpatrick/)
**Getting Started with Streamlit** was written by [Martin Fitzpatrick](https://www.pythonguis.com/authors/martin-fitzpatrick/) . 
Martin Fitzpatrick has been developing Python/Qt apps for 8 years. Building desktop applications to make data-analysis tools more user-friendly, Python was the obvious choice. Starting with Tk, later moving to wxWidgets and finally adopting PyQt. Martin founded PythonGUIs to provide easy to follow GUI programming tutorials to the Python community. He has written a number of popular [https://www.martinfitzpatrick.com/browse/books/](https://www.pythonguis.com/tutorials/getting-started-with-streamlit/Python books) on the subject. 
**Getting Started with Streamlit** was published in [tutorials](https://www.pythonguis.com/tutorials/) on April 02, 2025 . Feedback & Corrections [can be submitted here](https://tally.so/r/wbvxNE). 
[ streamlit](https://www.pythonguis.com/topics/streamlit/) [ foundation](https://www.pythonguis.com/topics/foundation/)
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
