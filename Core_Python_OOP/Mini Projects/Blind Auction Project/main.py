# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art
print(art.logo)
bids = { }
highest_bid = 0
highest_bidder = ""
condition = True
while condition == True:
    name = input("what is your name?")
    price = int(input("what is your bid?"))
    bids[name] = price

    asking = input("Any other there, if yes type 'yes' or 'no': ")
    if asking == "yes":
        print("\n" * 20)

    else:
        condition = False
        for bidder in bids:
            bid_amount = bids[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                highest_bidder = bidder
        print(f"winner is {highest_bidder} with a bid of ${highest_bid}")

