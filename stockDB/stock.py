import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("../multiple_pages/us_births.csv")

month, gender, year = st.tabs(["Month by Births", "Gender by Births", "Year by births"])


with month: 
    month_births = df.groupby("month")["births"].sum()
    fig = px.bar(month_births,x=month_births.index,y="births")
    st.plotly_chart(fig)


with gender:
    gender_births = df.groupby("gender")["births"].sum()
    fig = px.pie(gender_births,names=gender_births.index, values="births")
    st.plotly_chart(fig)


with year:
    year_births = df.groupby("year")["births"].sum()
    fig = px.line(year_births,x=year_births.index,y="births")
    st.plotly_chart(fig)