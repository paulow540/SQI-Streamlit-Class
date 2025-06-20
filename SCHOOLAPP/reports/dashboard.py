import streamlit as st
import re

pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
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
        
            if email is re.match(pattern, email) is not None:              
                print("Valid email:")
                
            if not email:
                st.error("Enter your email")
                st.stop()


            if not message:
                st.error("Please provide a message")
                st.stop()

            st.success("Information successfully!")

            
show_contact()