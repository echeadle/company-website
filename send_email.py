import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "echeadle@gmail.com"
    password = os.getenv("GMAIL_PASSWORD")
    recipient = "edward.cheadle8@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, recipient, message)


if __name__ == "__main__":
  send_email()

