import streamlit as st
import pandas as pd

st.write("Hello World")
st.write("Hello :blue[World]")
st.title("Hello :blue[World]")

"""
https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
"""
st.title("Hello :sunglasses:")
st.title("Hello :kimono:")

st.write(
    pd.DataFrame({
        "first column": [1,2,3,4],
        "second column": [10, 20, 30, 40]
    })
)

st.link_button("click here", "https://docs.streamlit.io/develop/api-reference")

st.header("Hello World", divider="rainbow")

code = """print("Hello")"""
st.code(code, language="python")

agree = st.checkbox("I agree")
if agree:
    st.write("Okay!")

options = st.multiselect(
    "What is your favorite color ?",
    ['red', 'yellow', 'blue', 'green', 'black']
)

st.write("your selected colors: ", options)


option = st.radio(
    "What is your favorite color ?",
    ['red', 'yellow', 'blue', 'green', 'black']
)

st.write("your selected colors: ", option)


df = pd.DataFrame(
    [
        {"colors": 'red', "rating": 4, "mark": True},
        {"colors": 'green', "rating": 5, "mark": True},
        {"colors": 'blue', "rating": 3, "mark": True}
    ]
)

edited_df = st.data_editor(df)
# st.write(edited_df["rating"].idxmax())
st.write(edited_df.loc[edited_df["rating"].idxmax()]["colors"])
st.write(edited_df.loc[edited_df["mark"] == True])


# download button
csv = edited_df.to_csv().encode("utf-8")

st.download_button(
    label="download csv",
    data=csv,
    file_name="sample_df.csv",
    mime="text/csv"
)


# progress bar
df2 = pd.DataFrame(
    {
        "sales": [20, 55, 100, 80],
        "progress_sales": [20, 40, 100, 80]
    }
)

st.data_editor(
    df2,
    column_config={
        "progress_sales": st.column_config.ProgressColumn(
            min_value=0,
            max_value=100
        )
    }
)

# display time series bar
df3 = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 30, 60, 80, 100],
            [3, 50, 0, 80, 40, 30, 100]
        ]
    }
)

st.data_editor(df3)

st.data_editor(
    df3,
    column_config={
        "sales": st.column_config.BarChartColumn(
            y_min=0,
            y_max=100
        )
    }
)

# time series line chart
st.data_editor(
    df3,
    column_config={
        "sales": st.column_config.LineChartColumn(
            y_min=0,
            y_max=100
        )
    }
)

# slider
age = st.slider("how old are you ? :", 0, 130, 40)
st.write("I'm ", age, ' old.')

# import date selection
import datetime
date = st.date_input("When is your birthday ?", datetime.date(2000, 1, 1))
st.write("I was born at ", date)

# free text
text = st.text_input("please enter something :", "xxxxxxxx")
st.write(text)

# separate column
col1, col2 = st.columns(2)
with col1:
    st.title("column1")
    st.write("this is column1")
with col2:
    st.title("column2")
    st.write("this is column2")

# separate tab
tab1, tab2 = st.tabs(["tab1", "tab2"])
with tab1:
    st.title("column1")
    st.write("this is column1")
with tab2:
    st.title("column2")
    st.write("this is column2")


with st.expander("see more detail"):
    st.write("xxxxxx")


with st.popover("see more detail"):
    st.write("XxxxxxX")


with st.sidebar:
    st.write("side menu")
    st.write("side menu 2")


# notification
agree2 = st.checkbox("I agree.")
if agree2:
    st.toast("Thank you", icon="🚨")

birthday = st.checkbox("Today is your birthday ?")
if birthday:
    st.balloons()

# multiple pages
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/page1.py", label="page1")
st.page_link("pages/page2.py", label="page2")
st.page_link("https://docs.streamlit.io/", label="Streamlit Docs")