import streamlit as st
from send_email import send_email
st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email address")
    message = st.text_area("Message")
    message = message + "\n\n" + user_email
    button = st.form_submit_button("Submit")
    if button:
        st.write(f"Thank you for your message. We will get back to you at {user_email} shortly.")
        st.write(f"Your message was: {message}")
        send_email(message)

