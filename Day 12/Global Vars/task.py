# Modifying Global Scope

# enemies = 1
#
#
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")


"""Instead of modifying the global variable, this function will return enemy plus one.
Then, enemies can be set outside the function to the function value."""
enemies = 1

def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

