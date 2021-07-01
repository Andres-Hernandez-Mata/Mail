"""
Uso: MIMEText
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 01 Julio 2021
"""

import smtplib
from email.mime.text import MIMEText
import getpass


def sendMail(user,pwd,to,subject,text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    try:
        smtpServer = smtplib.SMTP('smtp.gmail.com', 587)
        print("[+] Connecting To Mail Server.")
        smtpServer.ehlo()
        print("[+] Starting Encrypted Session.")
        smtpServer.starttls()
        smtpServer.ehlo()
        print("[+] Logging Into Mail Server.")
        smtpServer.login(user, pwd)
        print("[+] Sending Mail.")
        smtpServer.sendmail(user, to, msg.as_string())
        smtpServer.close()
        print("[+] Mail Sent Successfully.")
    except:
        print("[-] Sending Mail Failed.")

user = 'test.pc.fcfm@gmail.com'
pwd = getpass.getpass()
sendMail(user, pwd, 'perla.vieragn@uanl.edu.mx',
         'Re: Important', 'Test Message')



