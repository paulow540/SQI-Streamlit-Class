import streamlit as st


# FORMATTED TEXT

# badge
st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)

# caption
st.caption("This is a string that explains something above.")
st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")

# code
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")


# divider
st.divider()

st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule



# echo

with st.echo():
    st.write('This code will be printed')


# latex

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')


# text

st.text("This is text\n[and more text](that's not a Markdown link).")


# help
st.help(pandas.DataFrame)


# html

st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)