
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Alice Kocirova  
email: a.kocirova@gmail.com
discord: alicekocirova
"""


user = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]

texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# program si vyžádá přihlašovací jméno a heslo
username = input("Enter a user")
password = input("Enter password")

# zjisti, jestli zadané údaje odpovídají někomu z registrovaných uživatelů, jinak program ukonči

if username in user:
    index = user.index(username)
    if password[index] == passwords:
        print("-" * 40)
        print(f"Welcome to the app, {username}")
        print("We have 3 text to be analyzed")
        print("-" * 40)
    
    else:
        print("Unregistered user, terminating the program.")
        exit()

# program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS

selection = input("Enter a number between 1 and 3 to select: ")

if selection.isdigit():
    selection = int(selection)
    if 1 <= selection <= len(texts):
        selected_text = texts[selection -1]
        print(f"You selected text number {selection}.")

    else:
        print("Invalid selection, terminating the program.")
        exit()

else:
    print("Invalid input, terminating the program.")
    exit()

# statistiky pro vybraný text

text = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. '''
]

words = selected_text.split()

word_count = 0
titlecase_count = 0
uppercase_count = 0
lowercase_count = 0
numeric_count = 0
numeric_sum = 0



for word in words:
    clean_word = word.strip(".,!?")
    word_count += 1

    if clean_word.istitle():
        titlecase_count += 1

    elif clean_word.isupper():
        uppercase_count += 1

    elif clean_word.islower():
        lowercase_count += 1

    elif clean_word.isdigit():
        numeric_count += 1
        numeric_sum += int(clean_word)

print("There are", word_count, "words in the selected text.")
print("There are", titlecase_count, "titlecase words.")
print("There are", uppercase_count, "uppercase words.")
print("There are", lowercase_count, "lowercase words.")
print("There are", numeric_count, "numeric strings.")
print("The sum of all the numbers", numeric_sum)

# délky slov a sloupcový graf

word_lengths = {} 

for word in words:
    clean_word = word.strip(",.!?%")
    length = len(clean_word)
    if length in word_lengths:
        word_lengths[length] = word_lengths[length] + 1
    else:
        word_lengths[length] = 1

print("-" * 40)
print("LEN |  OCCURENCES  |NR.")
print("-" * 40)


for length in range(1, 12):
    if length in word_lengths:
        count = word_lengths[length]
    else:
        count = 0

   
    print(str(length).rjust(2), "|", end=' ')

   
    for i in range(count):
        print("*", end='')

    
    for i in range(12 - count):
        print(" ", end='')

    
    print("|", count)






 

 




