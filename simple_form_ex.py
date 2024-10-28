import streamlit as st
from datetime import datetime

st.title("User Information Form")

form_values = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None
} 
min_date  = datetime(1990,1,1)
max_date = datetime.now()

with st.form(key="user_info_fo rm"):
    form_values["name"] = st.text_input("Enter your name: ")
    form_values["height"] = st.number_input("Enter your height (cm): ")
    form_values["gender"] = st.radio("Select your gender: ", ("Male", "Female", "Other"))
    form_values["dob"] = st.date_input("Select your date of birth: ",max_value=max_date,min_value=min_date)

    submit_btn = st.form_submit_button(label="Submit")
    print("after submit")
    if submit_btn:
  
        if not all(form_values.values()):
            st.warning("Please fill in all the fields.")
        else:
            st.balloons()
            st.write("### INFO")
            for (key,value) in form_values.items():
                st.write(f"{key}:{value}")