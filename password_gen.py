import random


password_length = int(input("How many characters should the password be?"))
lowercase = "abcdefglmnopqrstuvwxyz"
uppercase = "ABCDEFGLMNOPQRSTUVMXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_-+=[]{};:,./<>?"

all_characters = lowercase + uppercase + digits + symbols
password = ""
for i in range(password_length):
    password += random.choice(lowercase)


print(password)

