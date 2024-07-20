# 1. I ntro
"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Pavla Vitásková
email: pavlavitaskova.pv@gmail.com
discord: pavlavitaskova_29682
"""

# 2. Imports and constants
ODDELOVAC = "-" * 40

# 2.1 Import variable from task_template.py:
from task_template import TEXTS


registrated_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}


# 2.3 Import Counter to create bar graph
from collections import Counter

# 3. Login
user_name = input("username: ")
user_password = input("password: ")

# 4. Verify user data
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

# 5. User selects the text
selected_text = TEXTS[(int(select_number)) - 1]

# 6. Perform statistics on selected text

# 6.1 Count all words
text_without_whitespaces = selected_text.strip()
text_words = text_without_whitespaces.split()
words_count = len(text_words)

print(f"There are {words_count} words in the selected text.")

# 6.2 Count all words in a string that start with a capital letter
title_words = 0

for word in text_words:
    if word.istitle():
        title_words += 1

print(f"There are {title_words} titlecase words.")

# 6.3 Count all words with uppercase letters
upper_words = 0

for word in text_words:
    if word.isupper() and word.isalpha():
        upper_words += 1

print(f"There are {upper_words} uppercase words.")

# 6.4 Count all words with lowercase letters
lower_words = 0

for word in text_words:
    if word.islower():
        lower_words += 1

print(f"There are {lower_words} lowercase words.")

# 6.5 Count all the numbers
numbers = 0

for word in text_words:
    if word.isdigit():
        numbers += 1

print(f"There are {numbers} numeric strings.")

# 6.6 Sum of numbers

# 6.6.1 Convert each string to int:

numbers_int = list()

for num in text_words:
    if num.isdigit():
        numbers_int.append(int(num))

# 6.6.2 Sum the integers:
total_sum = sum(numbers_int)

print(f"The sum of all the numbers {total_sum}")
print(ODDELOVAC)

# 7. Bar graph (frequency of different word lengths in the text):
list_of_occurences = list()

for word in text_words:
    list_of_occurences.append(len(word))

# 7.1 Count the occurrences of each number
occurrences = Counter(list_of_occurences)

# 7.2 Sort the items by number
sorted_occurrences = sorted(occurrences.items())

# 7.3 Print the header
print(f"{'LEN':<2} | {'OCCURRENCES':<16} | {'NR.':<3}")
print("-" * 40)

# 7.4 Print each row
for length, count in sorted_occurrences:
    stars = '*' * count
    print(f"{length:<2} | {stars:<16} | {count:<3}")
