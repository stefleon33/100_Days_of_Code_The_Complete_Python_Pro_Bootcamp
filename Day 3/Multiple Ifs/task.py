print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Your ticket will be $5.")
    elif age <= 18:
        bill = 7
        print("Your ticket will be $7.")
    else:
        bill = 12
        print("Your ticket will be $12.")
    wants_photo = input("Do you want a photo of your ride? Type y for Yes or n for No. ")

    if wants_photo.lower() == "y":
        #Add $3 to the bill
        bill += 3

    print(f"Your final bill is ${bill}.")
else:
    print("Sorry you have to grow taller before you can ride.")
