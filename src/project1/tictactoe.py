# the Tic Tac Toe Milestone Project game!
from random import random


def display_board(board):
    # clear output
    print('\n' * 100)
    print('|{}|{}|{}|'.format(board[0], board[1], board[2]))
    print('-------')
    print('|{}|{}|{}|'.format(board[3], board[4], board[5]))
    print('-------')
    print('|{}|{}|{}|'.format(board[6], board[7], board[8]))


# take in a player input and assign their marker as 'X' or 'O'.
def player_input():
    marker = ""
    while marker not in ['O', 'X']:
        marker = input("Player 1, Choose a marker (X or O): ")

    if marker is 'O':
        return 'O', 'X'
    else:
        return 'X', 'O'


# Takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    board[position - 1] = marker


# takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
    win_pos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win_moves in win_pos:
        if (mark * 3) == (board[win_moves[0]] + board[win_moves[1]] + board[win_moves[2]]):
            return True
    return False


# uses the random module to randomly decide which player goes first. You may want to lookup random.randint()
# Return a string of which player went first.
def choose_first():
    return random.randint(0, 1)


#  returns a boolean indicating whether a space on the board is freely available.
def space_check(board, position):
    return "#" == board[position - 1]


# Checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    return "#" not in board


# Asks for a player's next position (as a number 1-9) and check if it's a free position. If it is, then return the position
def player_choice(board):
    position = 0

    while position not in range(0, 10) or space_check(board, position):
        position = int(input("Enter a valid position(1-9): "))

    return position


def replay():
    return input("Do you want to play again? Y/N : ").lower() == 'y'


# check if game is over. Game over when
# 1. player 1 wins
# 2. player 2 wins
# 3. board is full
def game_over(board, player1, player2):
    return win_check(board, player1) or win_check(board, player2) or full_board_check(board)


print('Welcome to Tic Tac Toe!')
game_on = True
winner = None

while True:
    # Set the game up here
    tictactoe_board = ['#'] * 9
    print('Welcome to Tic Tac Toe!')
    player1, player2 = player_input()
    print("Player1 is {}\nPlayer2 is {}".format(player1, player2))
    game_on = True

    # print("starting game in 5 seconds")
    # sleep(5)

    while True:
        display_board(tictactoe_board)

        # Player 1 Turn
        print("Player 1's turn")
        position = player_choice(tictactoe_board)
        place_marker(tictactoe_board, player1, position)
        display_board(tictactoe_board)

        if game_over(tictactoe_board, player1, player2):
            print("Game Over")
            break

        # Player2's turn.
        print("Player 2's turn")
        position = player_choice(tictactoe_board)
        place_marker(tictactoe_board, player2, position)
        display_board(tictactoe_board)

        if game_over(tictactoe_board, player1, player2):
            print("Game Over")
            break

    if win_check(tictactoe_board, player1):
        print("Player 1 wins")
    elif win_check(tictactoe_board, player2):
        print("Player 2 wins")
    else:
        print("We have a draw")

    if not replay():
        break
