# streamlit_crud_app.py

# streamlit_create_db.py

import streamlit as st
import sqlite3, pandas as pd

# Title
st.title("📂 Create SQLite Database and Users Table")

# Connect to (or create) SQLite DB
conn = sqlite3.connect("mydata.db")
cursor = conn.cursor()

# Create table if not exists
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
);
"""

# Execute
cursor.execute(create_table_query)
conn.commit()

st.success("✅ Database and `users` table created successfully!")

# Optional: show the structure of the table
if st.checkbox("Show table structure"):
    cursor.execute("PRAGMA table_info(users)")
    table_info = cursor.fetchall()
    st.write(pd.DataFrame(table_info, columns=["CID", "Name", "Type", "NotNull", "Default", "PK"]))

# Close connection
conn.close()





import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# CREATE TABLE users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     email TEXT
# );


# DB Connection
engine = create_engine("sqlite:///mydata.db")  # change for other DBs

# App title
st.title("🛠️ Simple CRUD App with Streamlit")

# Choose operation
operation = st.sidebar.selectbox("Choose Operation", ["View", "Insert", "Update", "Delete"])

# Load current data
def get_users():
    with engine.connect() as conn:
        return pd.read_sql("SELECT * FROM users", conn)

# View Data
if operation == "View":
    st.subheader("👀 All Users")
    df = get_users()
    st.dataframe(df)

# Insert Data
elif operation == "Insert":
    st.subheader("➕ Insert New User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    if st.button("Insert"):
        with engine.begin() as conn:
            conn.execute(text("INSERT INTO users (name, email) VALUES (:name, :email)"),
                         {"name": name, "email": email})
        st.success("User inserted successfully!")

# Update Data
elif operation == "Update":
    st.subheader("✏️ Update Existing User")
    users = get_users()
    user_to_edit = st.selectbox("Select User", users["id"])
    new_name = st.text_input("New Name")
    new_email = st.text_input("New Email")
    if st.button("Update"):
        with engine.begin() as conn:
            conn.execute(text("UPDATE users SET name = :name, email = :email WHERE id = :id"),
                         {"name": new_name, "email": new_email, "id": user_to_edit})
        st.success("User updated!")

# Delete Data
elif operation == "Delete":
    st.subheader("🗑️ Delete a User")
    users = get_users()
    user_to_delete = st.selectbox("Select User", users["id"])
    if st.button("Delete"):
        with engine.begin() as conn:
            conn.execute(text("DELETE FROM users WHERE id = :id"), {"id": user_to_delete})
        st.success("User deleted.")



username = st.text_input("Username")
password = st.text_input("Password", type="password")

if username == "admin" and password == "pass123":
    st.success("Access granted.")
    # show app content
else:
    st.warning("Enter valid credentials.")
    st.stop()
