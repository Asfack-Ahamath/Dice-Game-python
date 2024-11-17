# Import the Necessary Module. 
import time

# Function to show the game rules.
def show_game_rules(player_name):
    valid_input = False
    while not valid_input:
        print("\n=================================================================================\n")
        # Ask if player wants to see the rules.
        show_rules = input(str(player_name) + "! Do you want to know the rules of this game? (Yes-Y / No-N) : ").lower()
        if show_rules == 'y':
            # Display game rules.
            print("\n=================================================================================\n")
            print("Game Rules :")
            time.sleep(0.5)
            print("\n    ✽  The game is played between a human player and a computer player.")
            time.sleep(0.5)
            print("\n    ✽  The game begins only when the dice roll 6")
            time.sleep(0.5)
            print("\n    ✽  Move forward by half the dice roll value.")
            time.sleep(0.5)
            print("\n\t✽  Dice value 6 means move 3 blocks")
            print("\n\t✽  Dice value 4 means move 2 blocks") 
            print("\n\t✽  Dice value 5 means move 2 blocks (.5 is neglected)")
            print("\n\t✽  Dice value 1 means no moves at all")
            time.sleep(0.5)
            print("\n    ✽  There are two black holes on positions 7 and 14.")
            time.sleep(0.5)
            print("\n    ✽  If any player hits the black hole, they will be sent to location 1")
            time.sleep(0.5)
            print("\n    ✽  The first one to reach location 20 is the winner.")
            time.sleep(0.5)
            print("\n    ✽  The game tracks the number of moves and black hole hits for each player.")
            time.sleep(0.5)
            print("\n    ✽  The results of the game will be saved to a text file.\n")
            print("✽   ✽   ✽   ✽   ✽   ✽".center(80))
            print("\r")
            print("--------------------------".center(80))
            print("Good Luck.✌️  Let's Play!!".center(81))
            print("--------------------------".center(80))
            print("\n=================================================================================\n")
            time.sleep(0.5)
            print("Hi {} Welcome to Dice Game!".format(player_name).center(80))
            print("\n=================================================================================\n")
            valid_input = True
        elif show_rules == 'n':
            print("\n=================================================================================\n")
            time.sleep(0.5)
            print("Hi {} Welcome to Dice Game!".format(player_name).center(80))
            print("\n=================================================================================\n")
            valid_input = True
        else:
            print("\nInvalid Input. Enter Y or N.")