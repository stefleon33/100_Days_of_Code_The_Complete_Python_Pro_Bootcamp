# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is is like in {location}?")

#Positional Arguments
#greet_with("Jack Bauer", "London")

#Keyword Arguments
greet_with(location = "London", name = "Jack Bauer")

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    true_count = 0
    love_count = 0
    for char in combined_names:
        if char.lower() == 't':
            true_count += 1
        if char.lower() == 'r':
            true_count += 1
        if char.lower() == 'u':
            true_count += 1
        if char.lower() == 'e':
            true_count += 1
    for char in combined_names:
        if char.lower() == 'l':
            love_count += 1
        if char.lower() == 'o':
            love_count += 1
        if char.lower() == 'v':
            love_count += 1
        if char.lower() == 'e':
            love_count += 1
    print(str(true_count) + str(love_count))

calculate_love_score(name1="Kanye West", name2="Kim Kardashian")