programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

#print(programming_dictionary["Bug"])
#print(programming_dictionary)


for thing in programming_dictionary:
    print(thing)

colours = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow"
}

colours["grape"] = "purple"

print(colours)
for key in colours:
    print(key)
    print(colours[key])