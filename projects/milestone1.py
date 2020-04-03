from IPython.display import clear_output

def display_board(board):

    clear_output()
    print(board[7]+ ' | ' + board[8] + ' | ' + board[9])
    print('--|---|--')
    print(board[4]+ ' | ' + board[5] + ' | ' + board[6])
    print('--|---|--')
    print(board[1]+ ' | ' + board[2] + ' | ' + board[3])

# Test board to make sure display is working
# test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# display_board(test_board)

def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Choose X or O: ').upper()

    if marker == 'X':

        return ('X', 'O')
    else:
        return ('Y', 'X')

def place_marker(board, marker, position):
    board[position] = marker

# Test to make sure that marker placement is working
# place_marker(test_board, 'M', 8)
# print(display_board(test_board))

def win_check(board, mark):
    # check for horizontal wins
    return ((board[7] == board[8] == board[9] == mark) or 
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    # check for diagonal wins
    (board[7] == board[5] == board[3] == mark) or 
    (board[9] == board[5] == board[1] == mark) or
    # check for vertical wins
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark))

import random

def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else: 
        return 'Player 2'
        
def space_check(board, position):

    return board[position] == ''

def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False

    return True


def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position (1-9) '))
    
    return position

def replay():

    choice = input('Play again" Enter Yes or No ')

    return choice == 'Yes'

# While loop to keep running the game
print("Welcome to Tic Tac Toe!")

while True: 

    ## Set everything up (Board, Who's First, Choose Markers)
    the_board = ['']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or no ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    ## Game Play
    while game_on:

        if turn == 'Player 1':
            # Show the board
            display_board(the_board)
            # Choose position
            position = player_choice(the_board)

            # Place marker
            place_marker(the_board, player1_marker, position)

            # Check for win
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 HAS WON!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game!')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            # Show board
            display_board(the_board)
            # Choose position
            position = player_choice(the_board)

            # Place marker
            place_marker(the_board, player2_marker, position)

            # Check for win
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 HAS WON!')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break

            