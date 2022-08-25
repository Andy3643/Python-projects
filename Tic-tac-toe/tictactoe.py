#tic tac toe game 

#global variables
board = ['-','-','-',
        '-','-','-',
        '-','-','-']

game_still_going = True
winner = None
current_player = "X"

#function to display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#function to allow user to play game
def play_game():
    display_board() #display first board

    # loop through turns for players
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
#function to handle player turns
def handle_turn(player):
    position = input('Choose position between 1-9 :')
    position = int(position) - 1 # generate actual index

    board[position] ='X'
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    #check rows
    #check columns
    #check diagonals
    pass
def check_if_tie():
    pass
def flip_player():
    pass


play_game()