import sys

# constants used for displaying the board
EMPTY_SPACE = '.'   # a period is easier to count than the space
PLAYER_X = 'X'
PLAYER_O = 'O'
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLOUM_LABLES = ('1', '2', '3', '4', '5', '6', '7')
assert len(COLOUM_LABLES) == BOARD_WIDTH


def main():
    print("""four in a row by saikiran reddy
             Two players take turns dropping tiles into one of seven columns, trying
              to make four in a row horizontally, vertically, or diagonally.""")
    # set up a new game
    game_board = get_new_board()
    player_Turn = PLAYER_X

    while True:  # run a player's turn
        # dispaly the board and get player's moves
        display_Board(game_board)
        player_move = ask_for_player_move(player_Turn, game_board)
        game_board[player_move] = player_Turn

        # check for win or tie:
        if is_winner(player_Turn, game_board):
            display_Board(game_board)    # display the board one last time
            print('player' + player_Turn + 'has won!!!!!!!!!!!!!!!')
            sys.exit()
        elif is_full(game_board):
            display_Board(game_board)     # display the board one last time
            print('there is a tie!!!!!!!!!')
            sys.exit()

        # switch turns to other players:
        if player_Turn == PLAYER_X:
            player_Turn = PLAYER_O

        elif player_Turn == PLAYER_O:
            player_Turn = PLAYER_X


def get_new_board():
    """Returns a dictionary that represents a Four in a Row board.
     The keys are (columnIndex, rowIndex) tuples of two integers, and the
     values are one of the 'X', 'O' or '.' (empty space) strings."""
    board = {}
    for column_Index in range(BOARD_WIDTH):
        for row_index in range(BOARD_HEIGHT):
            board[(column_Index, row_index)] = EMPTY_SPACE

    return board


def display_Board(board):
    """display the board and title son the screen"""
    '''Prepare a list to pass to the format() string method for the
       board template. The list holds all of the board's tiles (and empty
       spaces) going left to right, top to bottom:'''

    title_chars = []

    for row_index in range(BOARD_HEIGHT):
        for column_Index in range(BOARD_WIDTH):
            title_chars.append(board[(column_Index, row_index)])

    # display the board
    print("""
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+""".format(*title_chars))


def ask_for_player_move(player_tile, board):
    """Let a player select a column on the board to drop a tile into.
       Returns a tuple of the (column, row) that the tile falls into."""
    while True:
        print('player {}, enter a coloum or Quit:'.format(player_tile))
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('thanks for playing')
            sys.exit()

        if response not in COLOUM_LABLES:
            print('enter a number in 1 to {}'.format(BOARD_WIDTH))
            continue    # ask player again for their move

        coulmn_index = int(response) - 1

        # if the colulm is full ask for a move again
        if board[(coulmn_index, 0)] != EMPTY_SPACE:
            print('the coulm is full, select another one')
            continue   # ask player again for thier move

        # starting from the bottom find the 1st empty space
        for row_index in range(BOARD_HEIGHT -1, -1, -1):
            if board[(coulmn_index, row_index)] == EMPTY_SPACE:
                return coulmn_index, row_index


def is_full(board):
    """returns true if the board has no empty spaces"""
    for row_index in range(BOARD_HEIGHT):
        for coulmn_index in range(BOARD_WIDTH):
            if board[(coulmn_index, row_index)] == EMPTY_SPACE:
                return False

    return True   # all spaces are full


def is_winner(player_tile, board):
    """returns true if player tile has four tiles in a row on board """

    # go through entire board checking four in a row
    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT):
            # check for horizontal four in a row:
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index + 1, row_index)]
            tile3 = board[(column_index + 2, row_index)]
            tile4 = board[(column_index + 3, row_index)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

    for column_index in range(BOARD_WIDTH):
        for row_index in range(BOARD_HEIGHT - 3):
            # check for vertical four in a row
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index, row_index + 1)]
            tile3 = board[(column_index, row_index + 2)]
            tile4 = board[(column_index, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT - 3):
            # check for four in a row , right dow diagonal
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index + 1, row_index + 1)]
            tile3 = board[(column_index + 2, row_index + 2)]
            tile4 = board[(column_index + 3, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

            tile1 = board[(column_index + 3, row_index)]
            tile2 = board[(column_index + 2, row_index + 1)]
            tile3 = board[(column_index + 1, row_index + 2)]
            tile4 = board[(column_index, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

    return False


if __name__ == '__main__':
    main()

