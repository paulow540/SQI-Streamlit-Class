# streamlit_app.py

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, inspect

# ---------------------
# Connect to Database
# ---------------------
DATABASE_URL = "mysql+pymysql://root:paulow540@localhost/sakila"  # change this if using PostgreSQL, MySQL, etc.
engine = create_engine(DATABASE_URL)

# ---------------------
# UI: Title
# ---------------------
st.title("📊 Database Viewer App")

# ---------------------
# UI: Choose Table
# ---------------------
inspector = inspect(engine)
tables = inspector.get_table_names()
selected_table = st.selectbox("Choose a table to view:", tables)


# ---------------------
# Fetch Data from Selected Table
# ---------------------
@st.cache_data
def load_table_data(table_name):
    query = f"SELECT * FROM {table_name}"
    return pd.read_sql(query, engine)

data = load_table_data(selected_table)
st.write(f"Showing data from `{selected_table}`:")
st.dataframe(data)

# ---------------------
# Optional: Filter by Column
# ---------------------
columns = data.columns.tolist()
selected_column = st.selectbox("Select column to filter by (optional):", ["None"] + columns)

if selected_column != "None":
    unique_values = data[selected_column].dropna().unique()
    filter_value = st.selectbox(f"Select value from `{selected_column}`:", unique_values)
    filtered_data = data[data[selected_column] == filter_value]
    st.write(f"Filtered data where `{selected_column}` = `{filter_value}`:")
    st.dataframe(filtered_data)
