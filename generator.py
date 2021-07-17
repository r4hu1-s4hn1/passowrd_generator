import random
from string import *
import os

# setting up charsets
lower=ascii_lowercase
upper=ascii_uppercase
numbers=digits
special_characters=punctuation
charset=[lower,upper,numbers,special_characters]

#users interaction
print("l -> for lowercase\nu -> for uppercase\nn -> for numbers\ns -> for special characters\nEnter to select the set( seperated by spaces ):")
charsets=[]
for i in input().split():
    if i=='l':
        charsets.append(lower)
    if i=='u':
        charsets.append(upper)
    if i=='n':
        charsets.append(numbers)
    if i=='s':
        charsets.append(special_characters)
        
print(charsets)

for j in range(5):
    password=""
    for i in range(12):
        c=random.choice(charsets)
        password += random.choice(c)

    print(password)


