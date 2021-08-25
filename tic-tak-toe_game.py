#========Code written by Vijendra (github username == vijendrasaini1922)
#================defining functions

#===============printing graphic of tic-tac-toe

def print_game(values):
    print("\n")
    print("\t       |       |")
    print("\t   {}   |   {}   |   {}".format(values[0], values[1], values[2]))
    print("\t_______|_______|_____")

    print("\t       |       |")
    print("\t   {}   |   {}   |   {}".format(values[3], values[4], values[5]))
    print("\t_______|_______|_____")
    
    print("\t       |       |")
    print("\t   {}   |   {}   |   {}".format(values[6], values[7], values[8]))
    print("\t_______|_______|_____")


# Function to print the score-board
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t           SCOREBOARD         ")
    print("\t--------------------------------")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t--------------------------------\n")

#==========Function to check winner
def check_win(player_position, current_player):
#=======Possible winning combination
    win_output = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                  [1, 4, 7], [2, 5, 8], [3, 6, 9],
                  [1, 5, 9], [3, 5, 7]]
    
#======Check weather a player wins or not till now
    for x in win_output:
        if all(y in player_position[current_player] for y in x):
#=======Return True if winning condition satisfied
            return True
    return False

#=========Check weather match is draw or not
def check_draw(player_position):
    if len(player_position['X']) + len(player_position['O']) == 9:
        return True
    return False

#=========Store information of game
#=========check status of the each move
#=========Each players's moves

# For single game 
def single_game(current_player):
    #======Draw tic-tac-toe graphics
    values = [' ' for x in range(9)]
    #======Storing past and present of two players
    player_position = {'X': [], 'O':[]}

#==========Now loop this single time game
    while True:
        print_game(values)

#======use try and except block for extra errors
#======currently leave it

#=======Taken input for input number from user
        print("Player ", current_player, " turn ! Which box ?")
        move = int(input())

#======Entered value must form 1-9
        if move < 1 or move > 9:
            print("Wront Input!!! Try Again")
            continue

#======Check if entered position is occupied of empty
        if values[move-1] != ' ':
            print("Place is already filled!!! Try Again.")
            continue

#======After one round we update game information:

#=======update the current Player
        values[move - 1] = current_player

#=======update the player position
        player_position[current_player].append(move)

#=======Function call for checking win
        if check_win(player_position, current_player):
            print_game(values)
            print("Congratulation !! Player : ", current_player, " has won the game!!\n")
            return current_player

#======Function call for checking draw the match
        if check_draw(player_position):
            print_game(values)
            print("Game is Drawn!!!\n")
            return 'D'

#======If no one wins then switch the turn:
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X' 
#==============================while loop completes

#========Game inputs Starting
if __name__ == "__main__":
    print("Player 1: ")
    player1 = input("Enter the name: ")

    print("Player 2: ")
    player2 = input("Enter the name: ")
    print("\n")

    current_player = player1

#=========Stores the choice of players
    player_choice = {'X': "", 'O': ""}

#=========options
    options = ['X', 'O']

#==========Stores the Scoreboard and initialize
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)

#=========The loop runs until win or quit

    while True:
#========Player choice exlorer
        print("Turn to choose for: ",current_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 for quit")

#=======Input for choice
        choice = int(input())

        if choice == 1:
            player_choice['X'] = current_player
            if current_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            player_choice['O'] = current_player
            if current_player == player1:
                player_choice['X'] = player1
            else:
                player_choice['X'] = player2

        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break

        else:
            print("Wront Choice!! Please select the correct choice from given choices.")

#=======Stores the winner of single game of tic-tac-toe
        winner = single_game(options[choice - 1])

#=======Editing scoreboards according to winner if game is not draw
        if winner != "D":
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)

#=======switching players
        if current_player == player1:
            current_player = player2
        else: 
            current_player = player1


#================================End of code==========================