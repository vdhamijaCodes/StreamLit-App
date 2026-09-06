import streamlit as st
from summarize_text import summarize_text, count_words

st.title("Summarize Text")

uploaded_file = st.file_uploader("Upload the file you would like to summarize", type = "txt")

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")

    if st.button("Summarize"):
        summary = summarize_text(text)
        st.write(summary)

    