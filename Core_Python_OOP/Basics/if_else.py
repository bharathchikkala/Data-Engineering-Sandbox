# GAME-1, our main is to find the treasure and built this code by using if_else
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
person = input("press left or right").lower()
if person == "right":
    print("fall into a hole game over")
elif person == "left":
    choice1 = input("river came swim or wait for boat").lower()
    if choice1 == "swim":
            print("attacked by shark,gone")
    else:
        choice2 = input("choose one door either yellow or green").lower()
        if choice2 == "yellow":
         print("damn")
        if choice2 == "green":
              print("you won,treasure!")
else:
 print("plz choose only left or right")

# GAME-2, Rock Paper and scissors

choose = int(input("what do you choose? type 0 for rock,1 for paper,2 for scissors\n"))
game1 = ["rock", "paper", "scissors"]
print(game1[choose])
if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
elif choose == 2:
    print(scissors)
print("computer choice")
import random
choose2 = random.randint(0,2)
a = ["rock","paper","scissors"]
print(a[choose2])
if choose==0 and choose2 == 0:
    print("tie")
elif choose==0 and choose2==1:
    print("user wins")
elif choose==0 and choose2 ==2:
    print("user wins")
if choose==1 and choose2 ==0:
    print("computer wins")
if choose==1 and choose2 == 1:
    print("tie")
if choose==1 and choose2 == 2:
    print("computer wins")
if choose==2 and choose2 == 0:
    print("computer wins")
if choose ==2 and choose2 == 1:
    print("user wins")



