# Import the Necessary Modules. 
import datetime
import io

# Function to save game results to a text file.
def save_game_results(player_name, human_moves, human_black_hole_hits, human_player, computer_moves, computer_black_hole_hits, computer_player):
    # Create file name with current date and time.
    time_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")
    played_date_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
    file_name = time_name + ".txt"
    # Write game results to file.
    with io.open(file_name, 'w', encoding='utf-8') as file:
        file.write("\t\t\t\t\t\t◈━◈━◈━◈━◈━◈━◈\n")
        file.write("\t\t\t\t\t\t    Dice Game\n")
        file.write("\t\t\t\t\t\t◈━◈━◈━◈━◈━◈━◈\n")
        file.write("\n")
        file.write("   Played on : " + played_date_time + "\n")
        file.write("\n")
        file.write("Game Results :\n")
        file.write("\t\t    Played By       : " + player_name + "\n")
        file.write("\t\t    Total Moves     : " + str(human_moves) + "\n")
        file.write("\t\t    Black Hole Hits : " + str(human_black_hole_hits) + "\n")
        if human_player >= 20:
            file.write("\t\t    Status          : Won the Game\n\n")
        else:
            file.write("\t\t    Status          : Lost the Game\n\n")
        file.write("\t\t    Played By       : Computer\n")
        file.write("\t\t    Total Moves     : " + str(computer_moves) + "\n")
        file.write("\t\t    Black Hole Hits : " + str(computer_black_hole_hits) + "\n")
        if computer_player >= 20:
            file.write("\t\t    Status          : Won the Game\n")
        else:
            file.write("\t\t    Status          : Lost the Game\n")

    return file_name