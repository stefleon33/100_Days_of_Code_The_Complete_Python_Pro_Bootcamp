import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy level, my work
result = random.choices(letters, k=nr_letters) + random.choices(symbols, k=nr_symbols) + random.choices(numbers, k=nr_numbers)
string_result = "".join(result)

print(string_result)

#Hard level, my work
random.shuffle(result)
shuffled_result = "".join(result)
print(shuffled_result)

#Easy level, given solution
'''
password = ""
for char in range(0, nr_letters):
    password += random.choice(letters)
for num in range(0, nr_numbers):
    password += random.choice(numbers)
for sym in range(0, nr_symbols):
    password += random.choice(symbols)
print(password)
'''

#Hard level, given solution
'''
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for num in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
for sym in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ''
for char in password_list:
    password += char
print(f"Your password is: {password}")
'''