MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 80,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 220,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def process_coins():
    fifty_notes = int(input("Insert some 50 notes into machine: "))
    hundred_notes = int(input("Insert some 100 notes into machine: "))
    five_hundred_notes = int(input("Insert some 500 notes into machine: "))
    fifty_notes_all = 50 * fifty_notes
    hundred_notes_all = 100 * hundred_notes
    five_hundred_notes_all = 500 * five_hundred_notes
    total_inserted = fifty_notes_all + hundred_notes_all + five_hundred_notes_all
    return total_inserted

def rating():
    rating = int(input(f"Rate the {need_item}🧋 for 1-5 before leaving: "))
    if rating < 4:
        print("will try our best to improve next time")
    elif rating <= 5:
        print("Glad you ENJOYED it")
    else:
        print("U enterted something else not 1-5\nok anyways have a good day")


def checking_to_give_what_they_want(total_inserted,need_item):
    giving_back_balance = total_inserted - MENU[need_item]['cost']
    if total_inserted >= MENU[need_item]['cost']:
        print(f"Looks like u inserted more money: {total_inserted},So here is your balance change: {giving_back_balance}")
        print(f"Here is your {need_item}🧋,Enjoy!")
        rating()
    elif total_inserted < MENU[need_item]['cost']:
        print(f"Actual cost of {need_item} is: {MENU[need_item]['cost']} but u inserted,{total_inserted} so try again")
        print(f"Collect Your inserted money,{total_inserted}")

def what_item():
    items = ['espresso', 'latte', 'cappuccino']
    for item in items:
        if need_item == item:
            print(f"The cost of {need_item} is: {MENU[need_item]['cost']}")
            print("Insert the money into machine to get item")


    # if need_item == "espresso":
    #     print(f"The cost of espresso is : {MENU['espresso']['cost']}")
    #     print("Insert the coins into machine to get item")
    # elif need_item == "latte":
    #     print(f"The cost of latte is : {MENU['latte']['cost']}")
    #     print("Insert the coins into machine to get item")
    # else:
    #     print(f"The cost of cappuccino is : {MENU['cappuccino']['cost']}")
    #     print("Insert the coins into machine to get item")


game_is_on = True
while game_is_on:
    need_item = input("What would u want? {espresso, latte, cappuccino}").lower()
    if need_item not in MENU:
        print(f"You entered item which is not in our MENU,So Try again")
        continue
    what_item()
    total_inserted = process_coins()
    checking_to_give_what_they_want(total_inserted,need_item)
    re_order = input("Want to order again? type yes or no").lower()
    if re_order == "yes":
        game_is_on = True
    else:
        game_is_on = False





