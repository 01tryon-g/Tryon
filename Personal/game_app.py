board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-",
]

winner = None

game_still_going = True

current_player = 'p'

def display():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])



def switch_player():
    global current_player
    if current_player == 'p':
        current_player = 'd'
    elif current_player == 'd':
        current_player = 'p'



def handle_turn():
    print()
    print(current_player + "'s turn")

    valid = False
    while not valid:
        location = input('Type a number between 1-9: ')

        while location not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            location = input('Not a valid input, Try again? ')

        location = int(location) - 1
        # board[location] = current_player

        if board[location] == '-':
            valid = True
        else:
            print('Try a different position')

    board[location] = current_player
    display()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner
    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]



def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]



def check_diagonals():
    global game_still_going
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"

    if diagonals_1 or diagonals_2:
        game_still_going = False

    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]



def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False




def play_game():
    global winner
    display()
    while game_still_going:

        handle_turn()

        check_if_game_over()

        switch_player()

    if winner == 'p' or winner == 'd':
        print(winner + " won. ")
    elif winner == None:
        print("Tie. ")


play_game()


