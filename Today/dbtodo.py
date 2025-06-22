import streamlit as st
import sqlalchemy as sa
from sqlalchemy import Boolean,Column,Date,Integer,MetaData,String,Table
from streamlit.connections import SQLConnection

import datetime as date


TABLE_NAME = "todo_table"
conn = st.connection("todo_db")



@st.cache_resource
def connect_table():
    metadata_obj = MetaData()
    todo_table = Table(
        TABLE_NAME,
        metadata_obj,
        Column("id",Integer, primary_key=True),
        Column("title", String),
        Column("description", String),
        Column("created_at", Date),
        Column("due_at", Date),
        Column("done", Boolean) 
    )

    return metadata_obj, todo_table

def create_todo_callback(connection:SQLConnection, table:Table):
    title =st.session_state.new_todo_form_title
    description = st.session_state.new_todo_form_description
    due_date = st.session_state.new_todo_form_due_date

    new_todo = {
        "title":title,
        "description" :description,
        "created_at":date.date.today(),
        "due_at":due_date,
        "done":False,
    }
    stmt = table.insert().values(**new_todo)

    with connection.session as session:
        session.execute(stmt)
        session.commit()


# APP VIEW

st.title("Todo App")

metadata_obj, todo_table = connect_table()

with st.form("form"):
    st.subheader(":material/add_circle: Create todo")
    st.text_input("Todo Title", key="new_todo_form_title")
    st.text_area("Todo Description", key="new_todo_form_description")
    st.date_input("Due Date", key="new_todo_form_due_date")

    st.form_submit_button("Create Todo",
                           type="primary",
                           on_click= create_todo_callback,
                           args=(conn,todo_table)
                           )