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

    while True:
        answer = input("Enter a number btw. 1 and 3 to select: ")

        if answer.isnumeric() and int(answer) in range(1, 4):
            break
        else:
            print(
            "The value you entered doesn't match the requirements. Try again."
            )
    
else:
    print("Unregistered user, terminating the program.")
    exit()    

print(ODDELOVAC)

# 5. User selects the text
selected_text = TEXTS[(int(answer)) - 1]

# 6. Perform statistics on selected text

# 6.1 Count all words
just_words = selected_text.split()
cleaned_words = []                  
# vím, že .strip je to pro účel programu zbytečný krok,
# ale chci mít čistá slova pro další pokusy s programem

for word in just_words:
    word = word.strip('.,')

    cleaned_words.append(word)

words_count = len(cleaned_words)

print(f"There are {words_count} words in the selected text.")

# 6.2   Count:
#       words that start with a capital letter, 
#       words written in uppercase,
#       words written in lowercase,
#       numbers:

title_words = 0
uppercase_words = 0
lowercase_words = 0
numbers = 0

for word in cleaned_words:
    if word.istitle():
        title_words += 1
    elif word.isupper() and word.isalpha():
        uppercase_words += 1
    elif word.islower():
        lowercase_words += 1
    elif word.isdigit():
        numbers += 1
print(f"""There are {title_words} titlecase words.
There are {uppercase_words} uppercase words.
There are {lowercase_words} lowercase words.
"There are {numbers} numeric strings.""")

# 6.3 Sum of numbers

# 6.3.1 Convert each number in string format to integer format:
numbers_int = list()

for num in cleaned_words:
    if num.isdigit():
        numbers_int.append(int(num))

# 6.3.2 Sum the integers:
total_sum = sum(numbers_int)

print(f"The sum of all the numbers {total_sum}")
print(ODDELOVAC)

# 7. Bar graph (frequency of different word lengths in the text):
list_of_occurences = list()

for word in cleaned_words:
    list_of_occurences.append(len(word))

dict_occurences = {}

# Cyklus přes seznam a počítání výskytů
for number_letters in list_of_occurences:
    if number_letters in dict_occurences:
        dict_occurences[number_letters] += 1
    else:
        dict_occurences[number_letters] = 1

sorted_dict_occurences = dict(sorted(dict_occurences.items()))

pairs = sorted_dict_occurences.items()

# 7.3 Print the header
print(f"{'LEN':<2} | {'OCCURRENCES':<16} | {'NR.':<3}")
print("-" * 40)

# 7.4 Print each row
for length, count in pairs:
    stars = '*' * count
    print(f"{length:<2} | {stars:<16} | {count:<3}")
