"""
module for working with puzzle game
git repo: https://github.com/fox-flex/puzzle
"""
N = 9

board0 = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 " 12  ****"
]


def check_unique(lst: list) -> bool:
    global N
    unique = True
    possible_val = set(map(str, range(1, N + 1)))
    line_val = set()
    for val in lst:
        if val in possible_val:
            if val not in line_val:
                line_val.add(val)
            else:
                unique = False
                break
    return unique


def check_horizontal(board: list) -> bool:
    # global N
    unique = True
    board_c = list(map(lambda x:x[1: -1], board[1:-1]))
    for line in board:
        if not check_unique(list(line)):
            unique = False
            break
    return unique


def check_vertical(board: list) -> bool:
    global N
    board_str = ''
    for line in board:
        board_str += line
    board_columns = []
    for i in range(N):
        board_columns.append(board_str[i::N])
    return check_horizontal(board_columns)


def check_color(board: list) -> bool:
    global N
    unique = True
    board_c = board[::-1]
    num = N//2 + 1
    for i in range(num):
        vals = []
        for j in range(num):
            vals.append(board_c[i+j][i])
            vals.append(board_c[i][i+j])
        if not check_unique(vals[1:]):
            unique = False
            break
    return unique


def validate_board(brd: list) -> bool:
    return check_horizontal(brd) and check_vertical(brd) and check_color(brd)


if __name__ == "__main__":
    print('Hello, World!')
