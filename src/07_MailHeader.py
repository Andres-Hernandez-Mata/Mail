"""
Uso: Mailparser
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 06 Julio 2021
"""

import mailparser

eml_file = input("File name: ")
mail = mailparser.parse_from_file(eml_file)
print(mail.date)
print(mail.from_)
print(mail.delivered_to)
print(mail.messae_id)
print(mail.subject)
print(mail.to)


