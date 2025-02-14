# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)

bids = {}

keep_bidding = True
while keep_bidding:
    bidder_name = input("What is your name? \n").capitalize()
    bid_amount = int(input("What is your bid? \n$"))
    bids[bidder_name] = bid_amount
    keep_bidding = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    highest_bid = max(bids.values())
    highest_bidder = max(bids, key=bids.get)

    if keep_bidding == "yes":
         print("\n" * 100)
    elif keep_bidding == "no":
        keep_bidding = False
        print(f"The winning bid is ${highest_bid} from {highest_bidder}.")
        print(bids)
    else:
        print("Invalid selection. Please try again.")
        continue