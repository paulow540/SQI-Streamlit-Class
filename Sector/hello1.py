import streamlit as st # type: ignore
import pandas as pd  # type: ignore

st.title("⭐Topic App")

st.info("welcome")


with st.expander("Hello world"):
    st.write("Us births")
    data = pd.read_csv("us_births.csv")
    data


with st.sidebar:
    st.header("Input features")

    gender = st.selectbox("What gender did you want to select",("M", "F"), placeholder="Your Gender" )

    # st.write(gender)
    month = st.slider("Month", min(data.month), max(data.month), 5)
    month
    with st.expander("Hello world"):
        st.write("Us births")
        data = pd.read_csv("us_births.csv")
        data

st.subheader("second")

# st.map()

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)





# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df

# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))