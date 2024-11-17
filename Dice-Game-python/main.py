# Import statements for dice game.
from module.human_player import ask_player_name
from module.game_rules import show_game_rules
from module.game_logic import human_dice_value, computer_dice_value, wait_for_enter, black_hole, game_table, start_game
from module.game_results import save_game_results

# Main function to run the game.
def main():
    play_game = start_game()
    # Ask player if they want to play the game.
    if play_game == "n":
        print("\n══════════════════════════════════════════════════════════\n")
        print("         At Least Play The Dice Game Next Time!\n")
        print("\t         👋 👋 Bye! Bye! 👋 👋")
        print("\n══════════════════════════════════════════════════════════\n")
        return

    while play_game == "y":
        # Ask player for their name and show game rules.
        player_name = ask_player_name()
        show_game_rules(player_name)
        # Play the game until it ends.
        game_ended = False

        while not game_ended:
            # Initializing and declaring Variables.
            human_player, computer_player = 0, 0
            show_human_player, show_computer_player = 0, 0
            game_started = True 
            human_moves = 0
            computer_moves = 0
            human_black_hole_hits = 0
            computer_black_hole_hits = 0

            while not game_ended:
                # Roll the dice for human player and computer player.
                wait_for_enter()
                dice_value_human = human_dice_value()
                dice_value_computer = computer_dice_value()
                print(player_name + "'s dice roll is : " + str(dice_value_human))

                # For Human Player.
                if human_player == 0 and dice_value_human == 6:
                    human_player = 1
                elif human_player != 0:
                    show_human_player = human_player
                    human_player = black_hole(human_player, dice_value_human)
                    if human_player == 1 and show_human_player != 1:
                        human_black_hole_hits += 1
                    if human_player != show_human_player:
                        human_moves += 1

                # For Computer Player.
                if computer_player == 0 and dice_value_computer == 6:
                    computer_player = 1
                elif computer_player != 0:
                    show_computer_player = computer_player
                    computer_player = black_hole(computer_player, dice_value_computer)
                    if computer_player == 1 and show_computer_player != 1:
                        computer_black_hole_hits += 1
                    if computer_player != show_computer_player:
                        computer_moves += 1

                # Display game table.
                game_table(human_player, computer_player)
                print()
                # Display information about the dice roll and new position for human player.
                if human_player == 0:
                    print(player_name + " dice roll is " + str(dice_value_human) + " and cannot start the game")
                elif human_player == 1 and show_human_player != 1:
                    if dice_value_human == 6:
                        print(player_name + " dice roll is " + str(dice_value_human) + " and the game started")
                    else:
                        print(player_name + " dice roll is " + str(dice_value_human) + " and hit a black hole")
                else:
                    if human_player >= 20:
                        print(player_name + " dice roll is " + str(dice_value_human) + " and current location is " + str(human_player) + " (Winner)")
                    else:
                        print(player_name + " dice roll is " + str(dice_value_human) + " and current location is " + str(human_player))

                # Display information about the dice roll and new position for computer player.
                if computer_player == 0:
                    print("Computer dice roll is " + str(dice_value_computer) + " and cannot start the game")
                elif computer_player == 1 and show_computer_player != 1:
                    if dice_value_computer == 6:
                        print("Computer dice roll is " + str(dice_value_computer) + " and the game started")
                    else:
                        print("Computer dice roll is " + str(dice_value_computer) + " and hit a black hole")
                else:
                    if computer_player >= 20:
                        print("Computer dice roll is " + str(dice_value_computer) + " and current location is " + str(computer_player) + " (Winner)")
                    else:
                        print("Computer dice roll is " + str(dice_value_computer) + " and current location is " + str(computer_player))
                print("\n---------------------------------------------------------------------------------\n")

                #Check if the game has ended.
                if human_player >= 20 and computer_player < 20:
                    print("🎉 Congratulations!! "+ player_name +" You Won The Game!!! 🎉")
                    print("\n---------------------------------------------------------------------------------\n")
                    game_ended = True
                elif computer_player >= 20 and human_player < 20:
                    print("Computer Won The Game!!!")
                    print("Sorry!! "+ player_name +" 😢 Better Luck Next Time!!!")
                    print("\n---------------------------------------------------------------------------------\n")
                    game_ended = True

            # Save game results to file.
            file_name = save_game_results(player_name, human_moves, human_black_hole_hits, human_player, computer_moves, computer_black_hole_hits, computer_player)
            print("\t      Game Results have been saved to " + file_name)
            print("\n---------------------------------------------------------------------------------")
            print("▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼△▼".rjust(55))
            print("═════════════════════════════════════════════════════════════════════════════════\n")
        # Ask player if they want to play again.
        while True:
            play_again = input("\t\t    Do you want to play again? (Yes-Y /No-N): ").lower()
            if play_again in ["y", "n"]:
                break
            else:
                print("\n\t\t          Invalid Input. Enter Y or N.")
            print("\n═════════════════════════════════════════════════════════════════════════════════\n")

        if play_again == "n":
            play_game = "n"
            print("\n═════════════════════════════════════════════════════════════════════════════════\n")
            print("Thank you for playing Dice Game!\n".rjust(58))
            print("👋 👋 Bye! Bye! 👋 👋".rjust(47))
            print("\n═════════════════════════════════════════════════════════════════════════════════\n")

        elif play_again == "y":
            print("\n═════════════════════════════════════════════════════════════════════════════════\n")
            print ("So, Let's play again...".center(80))
            print("\n=================================================================================")

# Call the main function to start the game.
main()
