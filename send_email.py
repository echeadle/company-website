import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "echeadle@gmail.com"
password = "xlwgibgzuirjqjmp"

recipient = "edward.cheadle8@gmail.com"

context = ssl.create_default_context()

message = """\
Subject: Hello from Edward Cheadle
This is a test message from Edward Cheadle.
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, recipient, message)

