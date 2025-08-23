import random

def custom_chance(percentage):
    chance = random.randint(1, 100)
    if chance <= 16:
        input("you rolled 1. click enter to exit.")
    elif chance <= 33:
        input("you rolled 2. click enter to exit.")
    elif chance <= 49:
        input("you rolled 3. click enter to exit.")
    elif chance <= 67:
        input("you rolled 4. click enter to exit.")
    elif chance <= 85:
        input("you rolled 5. click enter to exit.")
    
    else:
        input("you rolled 6. click enter to exit.")
custom_chance(16)
