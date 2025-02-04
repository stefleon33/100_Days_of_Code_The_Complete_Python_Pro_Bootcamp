import random

#My solution
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_pick = random.randint(0,4)
print(random_pick)
if random_pick == 0:
    print(friends[0])
elif random_pick == 1:
    print(friends[1])
elif random_pick == 2:
    print(friends[2])
elif random_pick == 3:
    print(friends[3])
else:
    print(friends[4])

#Given solution 1
print(random.choice(friends))

#Given solution 2
print(friends[random_pick])