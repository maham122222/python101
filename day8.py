# Generating password

import random
import string
letters=list(string.ascii_lowercase+string.ascii_uppercase)
numbers=list(string.digits)
symbols=list(string.punctuation)

print("Welcome to Password Generator :) ")
n_letters=int(input('How many letters you want in your passwords?\n'))
n_numbers=int(input('How many numbers you want in your passwords?\n'))
n_symbols=int(input('How many symbols you want in your passwords?\n'))
password=[]
for i in range(1,n_letters+1):
    l=random.choice(letters)
    password+=l

for i in range(1,n_numbers+1):
    l=random.choice(numbers)
    password+=l

for i in range(1,n_symbols+1):
    l=random.choice(symbols)
    password+=l

random.shuffle(password)
password_string=""
for i in password:
    password_string += i
print(password)

