import streamlit as st

def show_contact():
    with st.form("Contact Me"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("your message")
        submit_bnt = st.form_submit_button("Submit")


        if  submit_bnt:
            if not name:
                st.error("Please provide your name")
                st.stop()
        
            if not email:
                st.error("Please provide a valid Email")
                st.stop()

            if not message:
                st.error("Please provide a message")
                st.stop()

            st.success("Information successfully!")

    
        
show_contact()