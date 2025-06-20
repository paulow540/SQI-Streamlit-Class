import streamlit as st 

st.title("COUNTER APP⭐")

if "counter" not in st.session_state:
    st.session_state["counter"] =  0

def increment():
    st.session_state["counter"] +=1   

def decrement():
    st.session_state["counter"] -=1

st.button("Increase counter",  key= "inc", on_click=increment)
    
st.button("Decrease counter", key= "dec", on_click=decrement) 

st.write("increase counter", st.session_state["counter"])

st.write(st.session_state)