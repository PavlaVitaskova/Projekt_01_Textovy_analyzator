# 1. intro
"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Pavla Vitásková
email: pavlavitaskova.pv@gmail.com
discord: pavlavitaskova_29682
"""
ODDELOVAC = "-" * 40

# 1.1 import variable from task_template.py:
from task_template import TEXTS

# 2. import PrettyTable and create users dictionary
from prettytable import PrettyTable

registrated_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

table = PrettyTable()
table.field_names = ["user", "password"]

# 2.1 rows in table
for user, password in registrated_users.items():
    table.add_row([user, password])

#print(table)

# 3. login
user_name = input("username: ")
user_password = input("password: ")

# 4. verify user data
if registrated_users.get(user_name) == user_password:
    print(ODDELOVAC)
    print(f"""Welcome to the app, {user_name}.
We have 3 texts to be analysed."""
    )
    print(ODDELOVAC)
    select_number = input("Enter a number btw. 1 and 3 to select: ")
    print(ODDELOVAC)
else:
    print("Unregistered user, terminating the program.")

# 5. user selects the text
selected_text = TEXTS[(int(select_number)) - 1]


# 6. perform statistics on selected text

# 6.1 count the words
text_without_whitespaces = selected_text.strip()
text_words = text_without_whitespaces.split()
words_count = len(text_words)

print(f"There are {words_count} words in the selected text.")

# 6.2 count the title words
title_words = 0

for word in text_words:
    if word.istitle():
        title_words += 1

print(f"There are {title_words} titlecase words.")

# 6.3 count the upper words
upper_words = 0

for word in text_words:
    if word.isupper() and word.isalpha():
        upper_words += 1

print(f"There are {upper_words} uppercase words.")

# 6.4 count the lower words
lower_words = 0

for word in text_words:
    if word.islower():
        lower_words += 1

print(f"There are {lower_words} lowercase words.")

# 6.5 count the numbers
numbers = 0

for word in text_words:
    if word.isdigit():
        numbers += 1

print(f"There are {numbers} numeric strings.")

# 6.6 sum the numbers
number_strings = list()

for word in text_words:
    if word.isdigit():
        number_strings.append(word)

# 6.6.1 convert each string to int:
numbers_int = list()

for num in number_strings:
    numbers_int.append(int(num))

# 6.6.2 sum the integers:
total_sum = sum(numbers_int)

# 6.6.3 result
print(f"The sum of all the numbers {total_sum}")
print(ODDELOVAC)

# 7. Bar graph (frequency of different word lengths in the text):
occurences = list()

for word in text_words:
    occurences.append(len(word))


