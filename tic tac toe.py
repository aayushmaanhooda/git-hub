"""lets make tic tak toe now """
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]
#if gmae is still going
game_is_still_going =True
#who won
winner =None
#whos turn it is
current_player ='X'


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    display_board()
    while game_is_still_going:
        # handle a single turn of a player
        handle_turn(current_player)

        #check if game has ended
        check_if_game_over()

        #filp to the other player
        flip_player()

    if winner =="X" or winner=="O":
        print(winner , "won.")
    elif winner == None:
        print("Tie.")

#hanf=dle single turn of a player function
def handle_turn(player):
    print( player + "'s turn")
    position = input("choose a position from 1-9")
    valid = False
    while not valid:

        while position not in ['1', '2', '3' , '4' , '5' ,'6' ,'7' ,'8' ,'9']:
            position = input(" Invalid input!! choose a position from 1-9")
        position = int(position) - 1
        if board[position] =="_":
            valid=True

        else:
            print("you cant go there...try again")


    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner
    #check rows
    row_winner = check_rows()

    #check column
    column_winner = check_columns()

    #check diagonals
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
        """there is a win"""
    elif column_winner:
        winner  =column_winner
        """there is win"""
    elif diagonals_winner:
        winner  =diagonals_winner
        """there was a win"""
    else:
        winner =None
        """no win"""

    return

def check_rows():
    #set up global variable
    global game_is_still_going
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"

    if row_1 or row_2 or row_3:
        game_is_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_is_still_going
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"

    if column_1 or column_2 or column_3:
        game_is_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
def check_diagonals():
    global game_is_still_going
    d_1 = board[0] == board[4] == board[8] != "_"
    d_2 = board[6] == board[4] == board[2] != "_"

    if d_1 or d_2:
        game_is_still_going = False
    if d_1:
        return board[0]
    elif d_2:
        return board[6]
    return
def check_if_tie():
    global game_is_still_going
    if "_" not in board:
        game_is_still_going=False
    return
def flip_player():
    global current_player

    if current_player=="X":
        current_player ="O"
    elif current_player =="O":
        current_player ="X"
    return


play_game()

