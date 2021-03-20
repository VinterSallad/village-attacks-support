from playsound import playsound
import random
import PySimpleGUI as sg


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


# #
# def game_partition(string):
#     play_notification_sound()
#     print_big(string)
#     input()
#
#
# #
# def monster_phase():
#     game_partition("Coin to first player")
#
#     game_partition("First player go, don't forget Reserve!")
#     game_partition("Second player go, don't forget Reserve!")
#     game_partition("Third player go, don't forget Reserve!")
#
#
# #
# def villager_phase():
#     game_partition("Villager event")
#
#     game_partition("Villager attacks & moves")
#
#
# #
# def cleanup_phase():
#     game_partition("Traps are activated")
#     game_partition("New villagers are summoned")
#     game_partition("Draw new trap")
#     game_partition("Cleanup")


# MAIN
# GAME LOOP

# i = 1
#
# while True:
#
#     user = input("Round " + str(i) + " starts")
#
#     if user == "stop":
#         break
#     else:
#         monster_phase()
#         villager_phase()
#         cleanup_phase()
#
#     input("Round " + str(i) + " ends")
#
#     i += 1

startLayout = [[]]

layout = [[sg.Button('Proceed'), sg.Button('Flip Coin'), sg.Button('Get Type'), sg.Button('Troll'), sg.Button('Reset')],
          [sg.Input('', key='-STATUS-', readonly=True)],
          [sg.Input('', key='-COIN-', readonly=True)],
          [sg.Input('', key='-TYPE-', readonly=True)],
          [sg.Input('', key='-TROLL-', readonly=True)],
          [sg.OptionMenu(['Day', 'Night'], default_value='Select Starting Time', size=(17, 5))]]

# Starting Theme
sg.theme('BlueMono')
# Day Theme
#sg.theme('Reddit')
# Night Theme
#sg.theme('DarkBlue')
window = sg.Window('Village Attacks Tool', layout)

stage = 0
day = True

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    # STATUS
    if event == 'Proceed':
        stage += 1
        if stage == 1:
            window.Element('-STATUS-').Update('Draw Trap')
        elif stage == 2:
            window.Element('-STATUS-').Update('Assign Coin')
        elif stage == 3:
            window.Element('-STATUS-').Update('Players play, do not forget reserve')
        elif stage == 4:
            window.Element('-STATUS-').Update('Town Event')
        elif stage == 5:
            window.Element('-STATUS-').Update('Villagers attack and move')
        elif stage == 6:
            window.Element('-STATUS-').Update('Traps activate')
        elif stage == 7:
            window.Element('-STATUS-').Update('New villagers spawn')
        elif stage == 8:
            window.Element('-STATUS-').Update('Cleanup')
            stage = 0
    # COIN
    elif event == 'Flip Coin':
        if random.randint(1, 2) == 1:
            window.Element('-COIN-').Update('Heads')
        else:
            window.Element('-COIN-').Update('Tails')
    # TYPE
    elif event == 'Get Type':
        unit = random.randint(1, 6)
        if unit == 1:
            window.Element('-TYPE-').Update('Red Type')
        elif unit == 2:
            window.Element('-TYPE-').Update('Blue Type')
        elif unit == 3:
            window.Element('-TYPE-').Update('Green Type')
        elif unit == 4:
            window.Element('-TYPE-').Update('Purple Type')
        elif unit == 5:
            window.Element('-TYPE-').Update('Yellow Type')
        elif unit == 6:
            window.Element('-TYPE-').Update('Rainbow Type')
    # TROLL
    elif event == 'Troll':
        unit = random.randint(1, 3)
        if unit == 1:
            window.Element('-TROLL-').Update("Troll rampages")
        elif unit == 2:
            window.Element('-TROLL-').Update("Troll attacks monsters")
        elif unit == 3:
            window.Element('-TROLL-').Update("Troll attacks villagers")

window.close()
