from art import logo
import random
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

"""Function to adjust an 11 to a 1 to prevent the hand from going over."""
def adjust_for_ace(hand):
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1

def play_blackjack():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play == "y":
        player_cards = []
        computer_cards = []
        player_score = ""
        computer_score = ""

        """Initial Deal"""
        player_cards = random.sample(cards, 2)
        computer_cards = random.sample(cards, 1)

        adjust_for_ace(player_cards)

        player_score = sum(player_cards)
        computer_score = sum(computer_cards)

        print(f"\tYour cards: {player_cards}, current score: {player_score}")
        print(f"\tComputer's cards: {computer_cards}, ?")

        if player_score == 21:
            print("You win! You got 21!")
            return

        """Player's Turn"""
        while True:
            hit_or_stay = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if hit_or_stay == "y":
                player_cards += random.sample(cards, 1)
                adjust_for_ace(player_cards)
                player_score = sum(player_cards)

                print(f"\tYour cards: {player_cards}, current score: {player_score}")
                print(f"\tComputer's cards: {computer_cards}, ?")

                if player_score > 21:
                    print(f"\tYour final hand: {player_cards}, final score: {player_score}")
                    print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
                    print("You went over. You lose.")
                    play_blackjack()
                elif player_score == 21:
                    print("You win! You got 21!")
                    return

            elif hit_or_stay == "n":
                break
            else:
                break

        """Computer's Turn"""
        while computer_score < 17:
            computer_cards.append(random.choice(cards))
            adjust_for_ace(computer_cards)
            computer_score = sum(computer_cards)

        print(f"\tYour final hand: {player_cards}, final score: {player_score}")
        print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
        if player_score > 21:
            print("You went over. You lose.")
        elif computer_score == 21 and player_score != 21:
            print("You lose! The dealer scored 21.")
        elif computer_score > 21 or player_score > computer_score:
            print("You win!")
        elif player_score < computer_score:
            print("You lose.")
        elif player_score == computer_score:
            print("It's a draw!")
        else:
            return
        play_blackjack()
    else:
        print("Goodbye!")

play_blackjack()
