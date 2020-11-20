board = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-',
]

game_on = True

winner = None

current_player = "Presh"


def board_view():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


def player_turn():
    global current_player
    if current_player == "Presh":
        current_player = "Gideon"
    elif current_player == "Gideon":
        current_player = "Presh"


def game_control():
    print()
    print(current_player + "'s turn")

    valid = False
    while not valid:
        position = input('choose a number between 1-9: ')

        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('Not a valid item, Try again: ')

        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print('Try a different position.')

    board[position] = current_player
    board_view()


def check_if_game_end():
    check_winner()
    check_tie()


def check_winner():
    global winner
    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_row():
    global game_on
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_on = False

    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]


def check_column():
    global game_on

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_on = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]


def check_diagonal():
    global game_on
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"

    if diagonals_1 or diagonals_2:
        game_on = False

    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]


def check_tie():
    global game_on
    if "-" not in board:
        game_on = False


def play_game():
    global winner
    board_view()
    while game_on:
        game_control()

        check_if_game_end()

        player_turn()

    if winner == "Presh" or winner == "Gideon":
        print(winner + " won!!")
    elif winner == None:
        print("Tie!")


play_game()
