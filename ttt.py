"""
Joel's majestic Tictactoe game.
Logic and commandline implementation.
Flask code will import the logic...
"""
import random
import sys

PLAYER_X = 'X'
PLAYER_O = 'O'
PLAYERS = (PLAYER_X, PLAYER_O)
GAME_TIE = 'T'


def cli_display_board(board):
    """Display the board in the CLI"""
    print("+-------" * 3 + "+", sep="")

    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

    return board


def board_to_str(board) -> str:
    """Convert the board to a 9 character string"""
    # steps
    # create a new list to contain the stringified board cells
    # (Peek at cli_display_board for hints...)
    # Loop through the rows
    #      Loop through the columns
    #           take the current cell contents to add the str() equivalent to the new list
    # return a "".join() of the new list
    str_board = []

    for row in range(3):
        for col in range(3):
            str_board.append(str(board[row][col]))
    return "".join(str_board)


def str_to_board(str_board) -> list:
    """Convert the string to a board"""
    # Create a new blank board that will be undated with moves
    board = initialise_state()
    # Loop through the characters in str_board
    #   (Get the current character from str_board)
    #   Is the character a valid move?
    #       If not, skip to the next step in the loop i.e. continue
    #       Add the valid move to the board you're going to return set_move()
    # DONE :-)

    # for ch in len(str_board[slice(0, 9)]):
    last_cell = min(len(str_board), 9)
    for x in range(0, last_cell):
        cur_value = str_board[x]
        if cur_value not in PLAYERS:
            continue
        board = set_move(board, x+1, cur_value)

    return board


def calc_cell_from_move(move):
    """Board is a list of lists
    move is an integer/string in the range 1-9
    """
    input = int(move) - 1
    row = input // 3
    col = input % 3

    return row, col


def get_move(board, move):
    """Board is a list of lists
    move is an integer/string in the range 1-9
    """
    row, col = calc_cell_from_move(move)

    return board[row][col]


def set_move(board, move, value):
    row, col = calc_cell_from_move(move)

    board[row][col] = value
    return board


def initialise_state(cur_board=None):
    """Initialise the board"""
    if cur_board is None:
        board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
    else:
        board = str_to_board(cur_board)
    return board


def make_list_of_free_fields(board):
    """Makes the free fields for the computer to reference turns against"""
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in PLAYERS:
                free.append((row, col))
    return free


def cli_enter_move(board):
    """Take the user CLI"""
    cli_input = input("Enter your move (1 - 9):")

    if len(cli_input) == 1 and cli_input >= '1' and cli_input <= '9':
        return player_move(cli_input, board)
    else:
        raise Exception("Move out of bounds.")


def player_move(input, board):
    """check user input against current free spaces"""

    # row, col = calc_cell_from_move(input)
    # sign = board[row][col]
    sign = get_move(board, input)

    if sign in PLAYERS:  # if sign == 'O' or sign == 'X':
        raise Exception("Cell occupied, choose another (sign =" + sign + ")")
    else:
        # board[row][col] = PLAYER_O
        board = set_move(board, input, PLAYER_O)
    return board


def winner_checker(board, sign):
    """Check if either player has 3 in a row"""
    winner = sign

    diag1 = diag2 = True

    for cell in range(3):
        if board[cell][0] == sign and board[cell][1] == sign and board[cell][2] == sign:
            return winner
        if board[0][cell] == sign and board[1][cell] == sign and board[2][cell] == sign:
            return winner
        if board[cell][cell] != sign:
            diag1 = False
        if board[2 - cell][cell] != sign:
            diag2 = False
    if diag1 or diag2:
        return winner
    return None


def check_result(board):
    """Check if someone has won.
    Check if it's a tie"""
    free = make_list_of_free_fields(board)
    if not free:
        # Return Tie state
        return GAME_TIE
    if winner_checker(board, PLAYER_X):
        return PLAYER_X
    if winner_checker(board, PLAYER_O):
        return PLAYER_O
    return None


def comp_turn(board):
    """
        Let the computer have a 'turn' -
        Based on the current state of the board
        Calculate the remaining moves available.
        IF there's more than one remaining field, calculate randrange based on len(free)
        Return the board - just like the player_move()
    """

    free = make_list_of_free_fields(board)

    if len(free) != 0:
        comp_move = random.choice(free)

        board[comp_move[0]][comp_move[1]] = PLAYER_X

        # winner = winner_checker(board, PLAYER_X)

        # return winner
    return board


def cli_human_turn(board):
    """Begin the human's turn"""
    return cli_enter_move(board)
    # winner = winner_checker(board, PLAYER_O)
# 
    # return winner


def main():
    human = False
    board = initialise_state()
    free = make_list_of_free_fields(board)

    cli_display_board(board)

    while len(free):

        if human:
            # winner = cli_human_turn(board, free)
            board = cli_human_turn(board)
            cli_display_board(board)
        else:
            # winner = comp_turn(board)
            board = comp_turn(board)
            cli_display_board(board)
        result = check_result(board)

        # if winner is None and len(free) == 1:
        if result == GAME_TIE:
            print("There are no spaces left, the game ends in a tie :(")
            sys.exit()
        # elif winner is not None:
        elif result is not None:
            print(result, "has won!")
            sys.exit()

        human = not human
        free = make_list_of_free_fields(board)


if __name__ == "__main__":
    main()
