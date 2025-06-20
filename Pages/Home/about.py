import streamlit as st
import numpy as np
import pandas as pd

st.title("PANDAS")


df = pd.read_csv("C:\\Users\\Administrator\\Documents\\Streamlit\\multiple_pages\\us_births.csv")

with st.expander("CLick to see the data"):
    
    st.write(df.head(2))


birth = df["births"].sum()
st.subheader(f"The total birth is {birth}", anchor=False)

tab1, tab2 = st.tabs(["Male Total Births", "Female Total Births"])

with tab1:
    birth_male = df[df["gender"] == "M"]["births"].sum()
    st.write("The Total number of birth is ", birth_male)

with tab2:
    birth_female = df[df["gender"] == "F"]["births"].sum()
    st.write("The Total number of birth is ",birth_female)


min_max = st.selectbox("Min and Max births",["", "Minimum", "Maximum"])

if min_max == str():
    st.write(" ")

elif min_max == "Minimum":
    min_birth = df["births"].min()
    st.write("The minimum births is ", min_birth)

else:
    max_birth = df["births"].max()
    st.write("The maximum births is ", max_birth)


name = 8


