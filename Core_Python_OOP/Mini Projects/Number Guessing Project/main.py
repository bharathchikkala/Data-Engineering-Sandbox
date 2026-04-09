logo = """
                             _   _                                  _               
  __ _ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / _` | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| (_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
 \__, |\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
 |___/                                                                              

"""
print(logo)
import random
print("Welcome to the number Guessing Game!")
print("Iam thinking of a number between 1 to 100")
mode = input("Choose difficulty: easy, hard\n")
org_num = random.randint(1,100)
if mode == "easy":
    print("You choosen easy so,You have 10 attempts to guess the number")
    attempts = 10
    condition = True
    while condition:
        guess_number = int(input("Guess the number: "))
        if attempts == 0:
            print(f"Attempts are over = {attempts},TRY AGAIN!")
            condition = False
        elif guess_number > org_num:
            attempts -= 1
            print(f"Too high!, make another guess\n Remaining attempts: {attempts}")
        elif guess_number < org_num:
            attempts -= 1
            print(f"Too low!, make another guess\n Remaining attempts: {attempts}")
        elif guess_number == org_num:
            attempts -= 1
            print("Yes, you guessed the number")
            condition = False

else:
    print("You choosen hard so,You have 5 attempts to guess the number")
    attempts = 5
    condition = True
    while condition:
        guess_number = int(input("Guess the number: "))
        if attempts == 0:
            print(f"Attempts are over = {attempts},TRY AGAIN!")
            condition = False
        elif guess_number > org_num:
            attempts -= 1
            print(f"Too high!, make another guess\n Remaining attempts: {attempts}")
        elif guess_number < org_num:
            attempts -= 1
            print(f"Too low!, make another guess\n Remaining attempts: {attempts}")
        elif guess_number == org_num:
            attempts -= 1
            print("Yes, you guessed the number")
            condition = False
