from art import logo, vs
from game_data import data

print(logo)

option_a = ''
option_b = ''

# TODO: Call Choices: Display name, description and location

print(f"Compare A: {data[0]['name']},")

print(vs)
print(f"Against B: {data[1]['name']},")

# TODO: Ask player to select who has more followers
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

# TODO: Compare number of followers using data

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
