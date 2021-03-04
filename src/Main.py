from playsound import playsound
import random


# Plays sound to players to notify action
def play_notification_sound():
    playsound('../sound/notification.wav')


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
def game_partition(string):
    play_notification_sound()
    print_big(string)
    input()


#
def monster_phase():
    game_partition("Coin to first player")

    game_partition("First player go, don't forget Reserve!")
    game_partition("Second player go, don't forget Reserve!")
    game_partition("Third player go, don't forget Reserve!")


#
def villager_phase():
    game_partition("Villager event")

    game_partition("Villager attacks & moves")


#
def cleanup_phase():
    game_partition("Traps are activated")
    game_partition("New villagers are summoned")
    game_partition("Draw new trap")
    game_partition("Cleanup")


# MAIN
# GAME LOOP

i = 1

while True:

    user = input("Round " + str(i) + " starts")

    if user == "stop":
        break
    else:
        monster_phase()
        villager_phase()
        cleanup_phase()

    input("Round " + str(i) + " ends")

    i += 1
