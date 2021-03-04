from playsound import playsound
import random


# Plays sound to players to notify action
def play_notification_sound():
    playsound('notification.wav')


# Prints a string in a formatted format
def print_big(string):
    print("____________________")
    print()
    print(string)
    print()
    print("____________________")


# Flips the coin
def flip_coin():
    if random.randint(1, 2) == 1:
        print("Heads")
    else:
        print("Tails")


# Throws 6 dices
def throw_dices():
    i = 0
    while i < 6:
        rand = random.randint(1, 6)
        if rand == 1:
            print("Villager Move")
        elif rand == 2:
            print("Melee")
        elif rand == 3:
            print("Ranged")
        elif rand == 4:
            print("Shield")
        elif rand == 5:
            print("Counter")
        elif rand == 6:
            print("Magic")

        i += 1


#
def monster_phase():
    play_notification_sound()
    print_big("Coin to starting player")


#
def villager_phase():
    play_notification_sound()


#
def cleanup_phase():
    play_notification_sound()


# MAIN
# GAME LOOP
while True:
    user = input()

    if user == "stop":
        break
    else:
        monster_phase()
        villager_phase()
        cleanup_phase()
