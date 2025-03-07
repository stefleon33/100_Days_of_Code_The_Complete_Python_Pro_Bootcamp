import random
from art import logo, vs
from game_data import data

print(logo)
score = 0
game_should_continue = True
option_b = random.choice(data)

while game_should_continue is True:
    # TODO: Call Choices and have Choice A set to Choice B and Choice B chosen again
    option_a = option_b
    option_b = random.choice(data)
    if option_a == option_b:
        option_b = random.choice(data)

    # TODO: Call number of followers from data import
    follower_count_a = option_a['follower_count']
    follower_count_b = option_b['follower_count']

# TODO: Call Choices: Display name, description and location

print(f"Compare A: {data[0]['name']},")

print(vs)
print(f"Against B: {data[1]['name']},")

# TODO: Ask player to select who has more followers
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

# TODO: Compare number of followers using data
follower_count_a = option_a['follower_count']
follower_count_b = option_b['follower_count']
print(follower_count_a)
print(follower_count_b)

# TODO: User correct, tell them their current score, move Choice B to Choice A and restart

# TODO: User incorrect, end game and tell them their score.
# TODO: User correct, tell them their current score, move Choice B to Choice A and restart
def game():
    while True:
        ask_question = input("Who has more followers? Type 'A' or 'B': ").upper()
        score = 0

        if follower_count_a > follower_count_b and ask_question == 'A':
            score += 1
            print(f"You're right! Current Score: {score}")

        elif follower_count_a < follower_count_b and ask_question == 'B':
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            print(f"You're incorrect. Final Score: {score}")
            return False

game()
