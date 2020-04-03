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
    pass