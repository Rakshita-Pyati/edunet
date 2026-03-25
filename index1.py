import streamlit as st
import google.generativeai as genai

st.title("welcome to the streamlit app")
user_input = st.text_input("enter the question")

genai.configure(api_key="AIzaSyAqav6j93DfGNiqv8yC_cec415EJeLxTVQ")

model = genai.GenerativeModel("models/gemini-2.5-flash")

if user_input:
    response = model.generate_content(user_input)
    st.write("this response is from generai")
    st.write(response.text)