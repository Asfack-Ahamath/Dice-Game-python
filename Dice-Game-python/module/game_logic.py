# Import the Necessary Module. 
import random

# Function to generate a random dice value for the human player.
def human_dice_value():
    return random.randint(1, 6)

# Function to generate a random dice value for the computer player.
def computer_dice_value():
    return random.randint(1, 6)

# Function to wait for the player to press Enter.
def wait_for_enter():
    input("Press Enter to Dice...")

# Function to handle black hole locations.
def black_hole(location, dice_value):
    new_location = location + (dice_value // 2)
    # If player hit a black hole, reset location to 1
    if new_location == 7 or new_location == 14:
        return 1
    return new_location

# Function to display the game table.
def game_table(human_player, computer_player):
    # Display game table
    print("\n  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20")
    print("─────────────────────────────────────────────────────────────────────────────────")

    for i in range(1, 21):
        if i == human_player:
            print("│ X", end=" ")
        elif i == 7 or i == 14:
            print("│ O", end=" ")
        else:
            print("│  ", end=" ")
    print("│")
    print("─────────────────────────────────────────────────────────────────────────────────")

    for i in range(1, 21):
        if i == computer_player:
            print("│ X", end=" ")
        elif i == 7 or i == 14:
            print("│ O", end=" ")
        else:
            print("│  ", end=" ")
    print("│")
    print("─────────────────────────────────────────────────────────────────────────────────")

# Function to start the game.
def start_game():
    while True:
        print("\r")
        # Ask if player wants to play the game.
        play_game = input("Would you like to play this Dice Game? (Yes-Y / No-N) : ").lower()
        if play_game in ["y", "n"]:
            return play_game
        else:
            print("\n\t\t\t   Invalid Input. Enter Y or N.")