import streamlit as st
import pandas as pd

#title
st.title("Streamlit Elements Demo")

#Dataframe Seciton
st.subheader("Dataframe")

df = pd.DataFrame({
    'Name':['Alice','Bob','Charlie','Devil'],
    'Age':[10,20,30,40],
    'Gender':['F','M','M','F'],
})

st.dataframe(df)

#Data Editoe section
st.subheader("Data Editor")
editable_df = st.data_editor(df)
print(editable_df)


#Static table
st.subheader("Static Table")
st.table(df)


#Metric Section
st.subheader("Metric")
st.metric(label="Total Rows",value=len(df))
st.metric(label="Average Age",value=round(df['Age'].mean(),1))

#JSON and Dict Section
st.subheader("JSON and Dict")

json_data = {
    "name": "Alice",
    "age": 10,
    "skills": ["Python","Data Science","Machine Learning"]
}

st.json(json_data)

#Also show it as dictionary
st.write("Dictionary view : ", json_data)