"""
Uso: SMTP 2
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 01 Julio 2021
"""

import smtplib
import ssl
import getpass

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "test.pc.fcfm@gmail.com"
receiver_email = "perla.vieragn@uanl.edu.mx"
password = getpass.getpass()
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)




