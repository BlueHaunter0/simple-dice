import random

def custom_chance(percentage):
    chance = random.randint(1, 100)
    if chance <= 16:
        print("you rolled 1")
    elif chance <= 33:
        print("you rolled 2")
    elif chance <= 49:
        print("you rolled 3")
    elif chance <= 67:
        print("you rolled 4")
    elif chance <= 85:
        print("you rolled 5")
    
    else:
        print("you rolled 6")
custom_chance(16)


i did it like this