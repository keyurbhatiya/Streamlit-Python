import streamlit as st
import pandas as pd


#title
st.title("Streamlit Form Demo")

#form
with st.form(key="sample_form"):

    #text input
    st.subheader("Text Inputs")

    name = st.text_input("Enter your name")

    feedback =st.text_area("Provide your feedback")

    #date and time Inputs
    st.subheader("Date and Time Inputs")
    dob = st.date_input("Select your date of birth")
    time = st.time_input("Choose a preferred time")

    #selector
    st.subheader("Selector")
    choice = st.radio("Choose an option",['Option 1','Option 2','Option 3'])
    gender = st.selectbox("Select your gendert",['Male','Female','Other'])
    slider_value = st.select_slider("Select a range", options=[1,2,3,4,5])

    #Toggles and checkboxes
    st.subheader("Toggles and Checkboxes")
    notification = st.checkbox("Receive notification?")
    toggle_value = st.checkbox("Enable dark mode?", value=False)


    #Submit Button for the form
    submit_btn = st.form_submit_button(label="Submit")

#outside of form
st.subheader("Buttons")