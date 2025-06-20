import streamlit as st
from forms.contact import show_contact

st.title("About Page", anchor=False)


@st. dialog("Contact Me")
def show_contact_form():
    show_contact()


col1, col2= st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./static/loss.png", width=200)

with col2:
    st.title("Opakunbi Paul", anchor=False)

    st.write(""" Data Analyst and data scienctist, assisting enterprises
             by supporting data-driven decision-making
    """)

    if st.button("Ⓜ️ Contact Me"):
        show_contact_form()



st.write("\n")
st.subheader("Experience & Quanl", anchor=False)

st.write(
    """
    - 1
    - 3
    - 5
    """
)

st.write("\n")
st.subheader("Hard skills", anchor=False)

st.write(
    """
    - Excel
    - Power bi
    - Spss
    """
)