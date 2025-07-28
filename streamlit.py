import streamlit as st

st.title("Streamlit App")

user_input = st.text_input("Enter some text")

if st.button("Show Input"):
    st.write("You entered:", user_input)