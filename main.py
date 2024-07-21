# 1. Intro
"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Pavla Vitásková
email: pavlavitaskova.pv@gmail.com
discord: pavlavitaskova_29682
"""

# 2. Imports and constants
ODDELOVAC = "-" * 40

# 2.1 Import variable from task_template.py
from task_template import TEXTS

# 2.2 Registrated users dictionary
registrated_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# 3. Login
user_name = input("username: ")
user_password = input("password: ")

# 4. Verify user data
if registrated_users.get(user_name) == user_password:
    print(ODDELOVAC)
    print(f"""Welcome to the app, {user_name}.
We have 3 texts to be analysed.
{ODDELOVAC}"""
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
# ale chci mít čistá slova pro další pokusy s programem,
# zároveň opravuji chybu minulé verze programu
# kdyby to vadilo, smažu to

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
There are {numbers} numeric strings.""")

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

# 7.1 Word lengths in selected text
list_of_occurences = list()

for word in cleaned_words:
    list_of_occurences.append(len(word))

# 7.2 How to get pairs (word lenght, number of occurrences)
dict_occurences = {}

for word_lenght in list_of_occurences:
    if word_lenght in dict_occurences:
        dict_occurences[word_lenght] += 1
    else:
        dict_occurences[word_lenght] = 1

sorted_dict_occurences = dict(sorted(dict_occurences.items()))

pairs = sorted_dict_occurences.items()

# 7.3 Print the header
print(f"{'LEN':<3} | {'OCCURRENCES':<17} | {'NR.':<3}")
print(ODDELOVAC)

# 7.4 Print each row
for length, occurances in pairs:
    stars = "*" * occurances
    print(f"{length:<3} | {stars:<17} | {occurances:<3}")
