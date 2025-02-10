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