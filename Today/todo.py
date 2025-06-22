import streamlit as st

st.title("ADD Todo")



def _create_todo(name, description,due_date):
    return f"{name} -- {description} -- {due_date}"

def add_todo(num):
    name = st.session_state[f"name{num}"]
    description = st.session_state[f"description{num}"]
    due_date = st.session_state[f"date{num}"]
    st.session_state[f"todo{num}"] = _create_todo(name, description,due_date)



def todo_edit_form(num):
    with st.container(border=True):
        if f"todo{num}" not in st.session_state:
            st.session_state[f"todo{num}"] = ""

        with st.form(key=f"form{num}",enter_to_submit=False, border=False):
            st.text_input("Name", key=f"name{num}")
            st.text_area("description", key=f"description{num}")
            st.date_input("Due date", key=f"date{num}")

            st.form_submit_button("Add todo", 
                                on_click=add_todo, 
                                args=(num,)
                                
                                )

        st.write(st.session_state[f"todo{num}"])



todo_edit_form("One")
todo_edit_form("two")
st.json(st.session_state)