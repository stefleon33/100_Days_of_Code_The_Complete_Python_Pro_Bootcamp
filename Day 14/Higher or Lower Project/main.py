import random
from art import logo, vs
from game_data import data

"""Display art"""
print(logo)
score = 0
game_should_continue = True

"""Generate a random account from the game data"""
option_b = random.choice(data)

while game_should_continue is True:
    # TODO: Call Choices and have Choice A set to Choice B and Choice B chosen again
    """Set option A to be option B and if the options are the same, call a new option B"""
    option_a = option_b
    option_b = random.choice(data)
    if option_a == option_b:
        option_b = random.choice(data)

    # TODO: Call number of followers from data import
    follower_count_a = option_a['follower_count']
    follower_count_b = option_b['follower_count']

    # TODO: Call Choices: Display name, description and location
    """Format the account data into printable format"""
    print(f"Compare A: {option_a['name']}, a(n) {option_a['description']}, from {option_a['country']}.")
    print(vs)
    print(f"Against B: {option_b['name']}, a(n) {option_b['description']}, from {option_b['country']}.")

    """Follower counts printed during testing"""
    #print(follower_count_a)
    #print(follower_count_b)

    # TODO: Ask player to select who has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # TODO: User correct, tell them their current score, move Choice B to Choice A and restart
    """If the user is right, the game should continue with their score increasing and Option A becoming Option B."""
    # TODO: User incorrect, end game and tell them their score.
    """If the user is wrong, the game should end and their final score should be displayed."""
    if follower_count_a > follower_count_b and guess == 'A':
        score += 1
        print("\n"*20)
        print(logo)
        print(f"You're right! Current Score: {score}")
        option_a = option_b
    elif follower_count_a < follower_count_b and guess == 'B':
        score += 1
        print("\n" * 20)
        print(logo)
        print(f"You're right! Current Score: {score}")
        option_a = option_b
    else:
        print("\n" * 20)
        print(logo)
        print(f"Sorry, you're wrong. Final Score: {score}")
        game_should_continue = False
