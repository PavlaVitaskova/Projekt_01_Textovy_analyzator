# 1. Úvod
"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Pavla Vitásková
email: pavlavitaskova.pv@gmail.com
discord: pavlavitaskova_29682
"""

# 2. Importování PrettyTable a vytvoření slovníku s uživateli
from prettytable import PrettyTable

registrated_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

table = PrettyTable()
table.field_names = ["user", "password"]

# Vyplnění řad v tabulce
for user, password in registrated_users.items():
    table.add_row([user, password])


print(table)

# 3. Přihlášení uživatele
user_name = input("Zadej své jméno: ")
user_password = input("Zadej své jméno: ")
