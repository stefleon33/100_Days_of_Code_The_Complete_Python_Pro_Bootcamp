print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size.upper() == "S":
    bill += 15
elif size.upper() == "M":
    bill += 20
elif size.upper() == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")
if pepperoni.upper() == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese.upper() ==  "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")