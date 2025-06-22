import streamlit as st 
import time 

st.title("COUNTER APP⭐")


# with st.form(key="form"):
#     name = st.text_input("Name")
#     email = st.text_input("Email")
#     date = st.date_input("Date")

#     if st.form_submit_button("Submit"):
#         if name and email and date:        
#             st.success("valid")
#         else:
#             st.error("not valid")


@st.fragment      
def todo(num):
    
    def add_action():
            name =st.session_state[f"Name{num}"]
            email = st.session_state[f"Email{num}"]
            date = st.session_state[f"Date{num}"]
        
            

    st.text_input("Name", key=f"Name{num}")
    st.text_input("Email", key=f"Email{num}")
    st.date_input("Date", key=f"Date{num}", value=None)

    st.button("submit", on_click=add_action, key=f"{num}")

    st.session_state

todo("One")
todo("Two")













# @st.fragment
# def con(con_):
#     time.sleep(2)
#     st.subheader(f"Counter {con_}")
#     key_word = f"counter{con_}"
#     if  key_word not in st.session_state:
#         st.session_state[key_word] =  0

#     def increment(name):
#         st.session_state[key_word] +=1   

#     def decrement(name):
#         st.session_state[key_word] -=1

#     name = st.text_input("what is your name", key=f"{con_}")
#     st.session_state["name"] = name

#     st.button("Increase counter", type="primary", key= f"inc{con_}", on_click=increment, args=(name,))
        
#     st.button("Decrease counter",type="tertiary", key= f"dec{con_}", on_click=decrement, args=(name,)) 

#     st.write("increase counter", st.session_state[key_word], name)

#     st.write(st.session_state)

# con("one")
# con("two")
