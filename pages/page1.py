import streamlit as st
import numpy as np
import pandas as pd

st.title("page 1")

df = pd.DataFrame(np.random.randint(0, 100, (20, 5)),
                  columns=("Japanese", "Math", "Science", "Sociology", "English"))
st.write(df)

# Bar chart
st.title("Japanese grades")
st.bar_chart(df["Japanese"])

st.title("Japanese grades")
st.line_chart(df["Japanese"])

# scatter plot
df["Total Score"] = df["Japanese"] + df["Math"] + df["Science"] + df["English"]
st.title("Relation between Math and Science")
st.scatter_chart(df, x="Science", y="Math", size="Total Score")

# Scatter plot in Map
st.title("Scatter plot near Tokyo")
map_df = pd.DataFrame(
    np.random.rand(50, 2)/[50, 50] + [35.68, 139.76],
    columns=['latitude', 'longitude']
)
st.write(map_df)

st.map(map_df)



