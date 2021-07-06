"""
Uso: BytesParser
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 06 Julio 2021
"""

from email import policy
from email.parser import BytesParser

eml_file = input("File name: ")
with open(eml_file, 'rb') as fp:
    msg = BytesParser(policy=policy.default).parse(fp)

print('To:', msg['to'])
print('From:', msg['from'])
print('Subject:', msg['subject'])
print('Received-SPF:', msg['Received-SPF'])
print('DKIM-Signature:', msg['DKIM-Signature'])

#for x in msg.keys():
    #print(x)


