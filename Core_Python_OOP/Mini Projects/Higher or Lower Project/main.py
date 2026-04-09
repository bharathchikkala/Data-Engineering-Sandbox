import random
from game_data import data
a = random.choice(data)
current_score = 0
game_starts = True
while game_starts:
    logo = r"""
        __  ___       __             
       / / / (_)___ _/ /_  ___  _____
      / /_/ / / __ `/ __ \/ _ \/ ___/
     / __  / / /_/ / / / /  __/ /    
    /_/ ///_/\__, /_/ /_/\___/_/     
       / /  /____/_      _____  _____
      / /   / __ \ | /| / / _ \/ ___/
     / /___/ /_/ / |/ |/ /  __/ /    
    /_____/\____/|__/|__/\___/_/     
    """
    print(logo)
    b = random.choice(data)
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
    vs = r"""
     _    __    
    | |  / /____
    | | / / ___/
    | |/ (__  ) 
    |___/____(_)
    """

    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}")
    print(f"Your current score is:{current_score}")
    Answer = input("Who has more followers? type 'A' or 'B': ").upper()
    A = a['follower_count']
    B = b['follower_count']
    if Answer == 'A' and A > B:
        current_score += 1
        print(f"U got it, Current score is:{current_score}")
        a = b
    elif Answer == 'A' and A < B:
        print("It was not! TRY AGAIN")
        game_starts = False
    elif Answer == 'B' and A < B:
        current_score += 1
        print(f"U got it, Current score is:{current_score}")
        a = b
    elif Answer == 'B' and A > B:
        print("It was not! TRY AGAIN")
        game_starts = False

print(f"Your FINAL SCORE is:{current_score}")


