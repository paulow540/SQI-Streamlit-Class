import streamlit as st
import pandas as pd
import numpy as np

about = st.Page("views/about.py", title="About Page", icon="🔥", default=True,)
sale =st.Page("views/sale_bd.py", title="SALE DASHBOARD", icon="⭐")


# Navigator menu

# pg = st.navigation(pages=[about,sale])


# Navigator with section

pg = st.navigation(
    {"Info":[about],
    "Business" : [sale]
    }
)


st.logo("static/profit.png")
st.sidebar.text("Made with ❤️ by Paul")

pg.run()

# st.sidebar.markdown("welcome ...")
# data1= pd.DataFrame({"AGE":[2,4,6,8,10], "Price":[10,14,16,18,20]})
# st.sidebar.scatter_chart(data=data1,x="AGE",y="Price")

check = st.sidebar.checkbox("check me")
if check:
    st.sidebar.write(f"welcome {check}")

st.sidebar.divider()
st.sidebar.file_uploader("Click to upload")
with st.sidebar.expander("it's well "):
    st.write("babe")

st.sidebar.color_picker("pick your color")

age = st.sidebar.slider("what is your age", min_value=1, max_value=20, value=4)
st.sidebar.write(age)



import pandas as pd
data= pd.read_csv("us_births.csv")
st.dataframe(data=data)

birth = sum(data["births"])



st.bar_chart(data=data, x="gender", y=birth)

st.line_chart()