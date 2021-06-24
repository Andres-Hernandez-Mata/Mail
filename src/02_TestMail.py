"""
Uso: SMTP
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 23 Junio 2021
"""

import smtplib
import ssl
import getpass

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "test.pc.fcfm@gmail.com"
password = getpass.getpass()
password = "fcfm.123"
message = "Hello world!"

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, "receiver_email", message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()


