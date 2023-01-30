from random import randrange

human = True

# use variables: board, userMove, winningSpaces - for reference ONLY

# display the board in the CLI
def cli_display_board(board): 
    print("+-------" * 3 + "+", sep="")

    for row in range(3): 
        print("|       " * 3, "|", sep="") 
        for col in range(3): 
            print("|   " + str(board[row][col]) + "   ", end="") 
        print("|")
        print("|       " * 3, "|", sep="") 
        print("+-------" * 3, "+", sep="") 

    return board

# initialise the board
def initialise_state():
    board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
    board[1][1] = 'X'
    return board

def make_list_of_free_fields(board):
    free = [] # create the free spaces array
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free.append((row,col))
    return free

# take user input in the CLI
def cli_enter_move(board):
    cli_input = input("Enter your move (1 - 9):")

    if len(cli_input) == 1 and cli_input >= '1' and cli_input <= '9':
        player_move(cli_input, board)
    else:
        raise Exception("Move out of bounds.")

# check user input against current free spaces 
def player_move(input, board):
    input = int(input) - 1
    
    row = input // 3
    col = input % 3

    sign = board[row][col]

    if sign == 'O' or sign == 'X':
        raise Exception("Cell occupied, choose another (sign =" + sign + ")")
    else:
        board[row][col] = 'O'
        
    return board

# check if same sign is used in winning combo
def winner_checker(board, sign):
    if sign == 'X':
        winner = 'computer'
    elif sign == 'O':
        winner = 'player'

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

# let computer have a 'turn'
def comp_turn(board, turns, free):
    valid = False

    while not valid:
        if turns > 0:
            comp_move = randrange(1, 9)
            print ("comp_move = ", comp_move)

            valid = comp_move >= 1 and comp_move <= 9
            if not valid:
                continue

            row = comp_move // 3
            col = comp_move % 3

            print ("row = ", row)
            print ("col = ", col)

            valid = board[row][col] in ['O', 'X']
        
            if valid:
                continue
            else:
                board[row][col] = 'X'

            winner = winner_checker(board, 'X')
            turns -=1

            return winner

def human_turn(board):
    cli_enter_move(board)
    winner = winner_checker(board, 'O')

    return winner

def game_over(winner, board, turns):
    if winner == None and turns == 0:
        cli_display_board(board)
        print("There are no spaces left, the game ends in a tie :(")
        exit()
    elif winner != None:
        cli_display_board(board)
        print(winner, "has won!")
        exit()

if __name__ == "__main__":
    board = initialise_state()
    free = make_list_of_free_fields(board)

    turns = 4

    while len(free):

        cli_display_board(board)

        if human:
            winner = human_turn(board)
            game_over(winner, board, turns)
        else:
            winner = comp_turn(board, turns, free)
            game_over(winner, board, turns)

        human = not human
        free = make_list_of_free_fields(board)

        

