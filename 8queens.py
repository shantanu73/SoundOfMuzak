from copy import deepcopy
import time

row = []
board = []
NUM = 8

for index in range(NUM):
    row.append(0)

for index in range(NUM):
    f = deepcopy(row)
    board.append(f)


def print_board(c_board):
    row = NUM - 1
    while row >= 0:
        col = 0
        while col < NUM:
            print(c_board[row][col], end=" ")
            col += 1
        print()
        row -= 1


def place_queen(c_board, c_rank, c_file):
    initial_board = deepcopy(c_board)

    print("yo-1 :-")
    print_board(initial_board)

    c_board[c_rank][c_file] = 1

    # print("this row:-")
    # print(c_board[c_rank])
    time.sleep(1)

    # # Modify rank
    # i = 0
    # for x in c_board[c_rank]:
    #     if x == 0:
    #         c_board[c_rank][i] = 2
    #     i += 1
    #
    # # Modify file
    # j = 0
    # for y in c_board:
    #     if y[c_file] == 0:
    #         c_board[j][c_file] = 2
    #     j += 1


    diff = c_file - c_rank
    min_row = 0
    min_col = diff
    max_row = NUM - 1 - diff
    max_col = NUM - 1
    if diff < 0:
        diff = - diff
        min_row = diff
        min_col = 0
        max_row = NUM - 1
        max_col = NUM - 1 - diff


    # # Modify forward slash diagonal
    # i, j = min_row, min_col
    #
    # while i <= max_row and j <= max_col:
    #     if c_board[i][j] == 0:
    #         c_board[i][j] = 2
    #     i += 1
    #     j += 1


    # Modify backward slash diagonal
    a, b = max_row, min_col
    # a, b = max, max_col

    print("\na & b")
    print(a,b)

    while a >= min_row and b <= max_col:
        if c_board[a][b] == 0:
            c_board[a][b] = 2

        a -= 1
        b += 1

    # if a > b:
    #     while a < max_row and b > min_col:
    #         if c_board[a][b] == 0:
    #             c_board[a][b] = 2
    #         a += 1
    #         b -= 1
    # else:
    #     while a > min_row and b < max_col:
    #         if c_board[a][b] == 0:
    #             c_board[a][b] = 2
    #         a -= 1
    #         b += 1

    print("\nyo-2 :-")
    print_board(c_board)

    # del initial_board


place_queen(board, 3, 5)
# place_queen(board, 5, 3)
