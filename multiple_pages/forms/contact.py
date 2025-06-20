import streamlit as st
import numpy as np
import pandas as pd


# with st.expander("click me"):
#     code = '''def hello():
#         print("Hello, Streamlit!")'''
#     st.code(code, language="python")

# side = st.sidebar.color_picker("enter your color")
# st.sidebar.write("your color is ", side)

st.sidebar.audio_input("Enter your aud")

# st.sidebar.image("C:\\Users\\Administrator\\Music\\profit.png")

col1, col2= st.columns(2, gap="small", vertical_alignment="center")

with col1:

    st.subheader("first column", anchor=False)

with col2:
    st.subheader("second column", anchor=False)
    tab1, tab2 = st.tabs(["Tab1","Tab2"])

    with tab1:
        def show_contact():
            with st.form("Contact Me"):
                name = st.text_input("Name")
                email = st.text_input("Email")
                message = st.text_area("your message")
                submit_bnt = st.form_submit_button("Submit")


                if  submit_bnt:
                    if not name:
                        st.error("Please provife your name 😒")
                        st.stop()
                
                    if not email:
                        st.error("Please provide a valid Email")
                        st.stop()

                    if not message:
                        st.error("Please provide a message")
                        st.stop()

                    st.success("Information successfully!")

            
        show_contact()

    with tab2:
        df = pd.read_csv("C:\\Users\\Administrator\\Documents\\Streamlit\\multiple_pages\\us_births.csv")
        df







