# def greet():
#     print("Hello, ")
#     print("How is your day today? ")
#     print("What are you doing today? ")
#
# greet()

#Function that allows for inputs
def greet_with_name(name):
    print(f"Hello, {name}")
    print(f"How is your day today {name}? ")
    print(f"What are you doing today {name}? ")

greet_with_name("Stef")

def life_in_weeks(current_age):
    ninety_years_in_weeks = 4680
    current_age_in_weeks = current_age * 52
    time_left = ninety_years_in_weeks - current_age_in_weeks
    print(f"You have {time_left} weeks left.")

life_in_weeks(56)