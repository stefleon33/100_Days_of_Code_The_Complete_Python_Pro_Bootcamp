import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
options = [rock, paper, scissors]
computer_choice = random.choice(options)

if player_choice == 0:
    print(f"{player_choice}" + rock)
elif player_choice == 1:
    print(f"{player_choice}" + paper)
elif player_choice == 2:
    print(f"{player_choice}" + scissors)
else:
    print("You didn't pick any known options.")

print("Computer choose: " + computer_choice)

if computer_choice == rock and player_choice == 0:
    print("It's a draw.")
elif computer_choice == paper and player_choice == 1:
    print("It's a draw.")
elif computer_choice == scissors and player_choice == 2:
    print("It's a draw.")
elif computer_choice == rock and player_choice == 2:
    print("You lose : (")
elif computer_choice == scissors and player_choice == 0:
    print("You win!")
elif computer_choice == paper and player_choice == 0:
    print("You lose : (")
elif computer_choice == rock and player_choice == 1:
    print("You win!")
elif computer_choice == scissors and player_choice == 1:
    print("You lose : (")
elif computer_choice == paper and player_choice == 2:
    print("You win!")
else:
    print("You typed an invalid number. You lose!")

#solution given
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
    
computer_choice = random.randint(0, 2)
print("Computer choose:")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice < computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!)
elif computer_choice == user_choice: 
    print("It's a draw!)
'''