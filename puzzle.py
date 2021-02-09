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
 "  2  ****"
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


def check_vertical(board: list, num=N) -> bool:
    board_str = ''
    for line in board:
        board_str += line
    board_columns = []
    num = 9
    for i in range(num):
        board_columns.append(board_str[i::num])
    return check_horizontal(board_columns)


def check_color(board: list, num=N) -> bool:
    pass


def validate_board(board: list, num=N) -> bool:
    is_correct = True

    return is_correct


if __name__ == "__main__":
    # print('Hello, World!')
    pass
