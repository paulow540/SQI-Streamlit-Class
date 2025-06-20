import streamlit as st 
import datetime
import pandas as pd
import numpy 

st.title("welcome to Streamlit class", anchor=False)

with st.expander("click me to see a table"):
    df = pd.read_csv("C:\\Users\\Administrator\\Documents\\Data sci kit\\Datasets\\us_births.csv")
    df

# name = st.text_input("Enter your full name", max_chars=100)
# age = st.number_input("Enter your age here")
# file = st.file_uploader("Upload a file here")
# audio = st.audio_input("Send me an audio text")
# # image = st.camera_input("Snap me")
# date = st.date_input("enter your date here", value=None)
# time = st.time_input("Set an alarm for", value=None)
# # char = st.chat_input("send me a message")

# rad =  st.radio(
#      "What's your favorite movie genre",
#      [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],

#  )
# button = st.button("Click me to see the values")

# if button:   
#     st.write(rad)

# check = st.checkbox("check me")
# if check:
#     st.write(rad)

# st.slider("select a range of value",1,20,4)











# if name and age:
#     st.write(f"My name is {name} and i am {age} years old")