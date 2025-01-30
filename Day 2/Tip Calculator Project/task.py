print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 18 20 22 "))
tip_as_percent = (tip/100) + 1
people = int(input("How many people to split the bill? "))
price_per_person = round((bill * tip_as_percent) / people, 2)
print(f"Each person should pay ${price_per_person}.")
