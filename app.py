import streamlit as st
from vaantamil import மெய்ம்மயக்கம்_சோதனை

st.set_page_config(
    page_title="வான் தமிழ்",
    layout="centered"
)

st.title("தொல்காப்பிய செய்திகள்")
st.caption("தமிழ் இலக்கண ஆய்வி")

word = st.text_input("தமிழ் சொல்லை உள்ளிடுங்கள்")

if word:
    result = மெய்ம்மயக்கம்_சோதனை(word)
    if result:
        st.subheader("முடிவுகள்")
        st.code(result, language="text")
