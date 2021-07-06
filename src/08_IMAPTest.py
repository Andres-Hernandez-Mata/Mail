"""
Uso: IMAP4_SSL
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 06 Julio 2021
"""


import imaplib
import getpass

mail = imaplib.IMAP4_SSL('imap.gmail.com')
user = 'test.pc.fcfm@gmail.com'
password = getpass.getpass()
mail.login(user, password) 
folders = (mail.list()[1])
for x in folders:
    print(x.decode())



