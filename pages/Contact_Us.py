import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("topics.csv")

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email address")
    option = st.selectbox("What topic do you want to discuss?",
                          df["topic"], key="topic")
    raw_message = st.text_area("Message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email} 
The Topic: {option}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your Email was sent successfully")

