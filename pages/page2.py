import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

st.title("page 2")


iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name="species")

st.write(X)
st.write(y)

# learning data and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# learning model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# predict test data
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.write(f"accuracy is {accuracy}.")



