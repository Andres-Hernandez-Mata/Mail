"""
Uso: IMAP4_SSL 2
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 08 Julio 2021
"""

import imaplib
import getpass

mail = imaplib.IMAP4_SSL('imap.gmail.com')
user = 'test.pc.fcfm@gmail.com'
password = getpass.getpass()
#password = 'fcfm.123'
mail.login(user, password) 
folders = (mail.list()[1])
mail.select('Inbox')

tmp, data = mail.search(None, 'ALL')
for num in data[0].split():
	tmp, data = mail.fetch(num, '(RFC822)')
	print('Message: {0}\n'.format(num))
	print(data[0][1].decode())
	break
mail.close()
