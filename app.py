import streamlit as st
from summarize_text import summarize_text


st.title("AI Summarizer")
file = st.file_uploader("Upload a txt file to summarize", type=".txt")
if file is not None:
    data = file.getvalue().decode("utf-8")
    if st.button("Summarize"):
        content = summarize_text(data)
        st.write(content)
else:
    st.write("Upload a valid file")




