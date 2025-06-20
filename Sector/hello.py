import streamlit as st




st.title("STREAMLIT CLASS ⭐⭐")
st.subheader("welocme to class")

st.markdown("*Streamlit* is **really** ***cool***.")

st.badge("New")
st.badge("Success", icon=":material/check:", color="green")


st.caption("*okay*")


code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")


name = st.text_input("What is your name ")
if name:
    st.write(f"welcome to class {name} ")

with st.expander("Hello world"):
    info = ["Ayo","Ola","Mike"]
    for i in info:
        st.button(i)
    
    


name = st.chat_input("What is your name ")
if name:
    st.write(f" {name} ")
