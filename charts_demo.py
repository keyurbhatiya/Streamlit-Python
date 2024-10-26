import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#title
st.title("Streamlit Charts Demo")

# Generate sample data

charts_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

#Area Chart Section
st.subheader("Area Chart")

st.area_chart(charts_data)

#Bar Chart Section
st.subheader("Bar Chart")

st.bar_chart(charts_data)

#Line Chart Section
st.subheader("Line Chart")

st.line_chart(charts_data)

#Scatter Chart Section
st.subheader("Scatter Chart")

scatter_data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})

st.scatter_chart(scatter_data)

#Map Section
st.subheader("Map")

map_data = pd.DataFrame(
    np.random.randn(100,2) / [50,50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

#Pyplot Section
st.subheader("Pyplot Chart")
fig, ax = plt.subplots()
ax.plot(charts_data['a'],label='A')
ax.plot(charts_data['b'],label='B')
ax.plot(charts_data['c'],label='C')
ax.set_title("Pyplot Line Charts")
ax.legend()
st.pyplot(fig)