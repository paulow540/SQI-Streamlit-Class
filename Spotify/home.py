import streamlit as st
import numpy as np
import pandas as pd
# import plotly.figure_factory as ff


with st.expander("Show dataset"):
    df = pd.read_csv("C:\\Users\\Administrator\\Downloads\\Spotify\\spotify_history.csv")
    df["ts"] = pd.to_datetime(df["ts"])
    df["year"] = df["ts"].dt.year
    df["month"] = df["ts"].dt.month
    df["day"] = df["ts"].dt.day
    df["reason_start"] = df["reason_start"].fillna("Blank")
    df["reason_end"] = df["reason_end"].fillna("Blank")
    st.write(df.head(4))
    


col1, col2 = st.columns(2)

with col1:
    artist_name = df["artist_name"].value_counts()[:11]
    # fig = ff.create_distplot(artist_name,)
    # st.plotly_chart(fig)
    st.write(artist_name)


    myear = df.groupby("year")["year"].count().sort_values(ascending=False)
    st.write(myear)
    # st.bar_chart(myear,x=str(myear.index), y="year")
        
    tab1, tab2 = st.tabs(["reason_start", "reason_end"])

    with tab1:
        reason_start = df["reason_start"].value_counts()
        st.write(reason_start)

    with tab2:
        reason_end = df["reason_end"].value_counts()
        st.write(reason_end)


        # day_reason_start = df.groupby(["reason_start","skipped"])["spotify_track_uri"].count().unstack().fillna(0)

        day_reason = pd.DataFrame({"Year":df["year"],"Day":df["day"],"Skipped":df["skipped"]})

        year = df.year.value_counts()

with col2:
    number = ["year","day","month", "skipped","reason_start","reason_end"]
    select_columns = st.sidebar.selectbox("show the columns",number)

    st.write(select_columns)

    count_columns = df[select_columns].value_counts()
    st.bar_chart(count_columns)

    st.line_chart(count_columns)

currecy = ["Naira","USD","Pound","Euro","Siwe","One"]
currecy2 = ["Naira","Pound","Euro","Siwe","One","USD"]


select = st.selectbox("Input currency", currecy)
select2 =st.selectbox("Output currency", currecy2)

input = st.number_input("Currency")

if st.button("Click to convert"):
    st.write(input)

