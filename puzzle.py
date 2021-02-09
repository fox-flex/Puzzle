"""
module for working with puzzle game
git repo: https://github.com/fox-flex/puzzle
"""


def check_unique(lst: list, num=9) -> bool:
    """
    Function check if in list of N values aren't any repetition of elements.
    It there are function return False. True otherwise.
    >>> check_unique(['1', '2', '3', '4', '5', '6', '7', '*', '*'])
    True
    >>> check_unique(['1', '2', '3', '4', '4', '6', '7', '*', ' '])
    False
    """
    unique = True
    possible_val = set(map(str, range(1, num + 1)))
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
    """
    Function check if in each line are unique elements.
    It there are function return True. False otherwise.
    >>> check_horizontal(["**** ****",\
                          "***1 ****",\
                          "**  3****",\
                          "* 4 1****",\
                          "     9 5 ",\
                          " 6  83  *",\
                          "3   1  **",\
                          "  8  2***",\
                          " 12  ****"])
    True
    >>> check_horizontal(["**** ****",\
                          "***1 ****",\
                          "**  3****",\
                          "* 4 1****",\
                          "     9 5 ",\
                          " 6  83  *",\
                          "3   1  **",\
                          "  8  2***",\
                          "112  ****"])
    False
    """
    unique = True
    for line in board:
        if not check_unique(list(line)):
            unique = False
            break
    return unique


def check_vertical(board: list, num=9) -> bool:
    """
    Function check if in each column are unique elements.
    It there are function return True. False otherwise.
    >>> check_horizontal(["**** ****",\
"***1 ****",\
"**  3****",\
"* 4  ****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
" 12  ****"])
    True
    >>> check_horizontal(["**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"112  ****"])
    False
    """
    board_str = ''
    for line in board:
        board_str += line
    board_columns = []
    for i in range(num):
        board_columns.append(board_str[i::num])
    return check_horizontal(board_columns)


def check_color(board: list, num=9) -> bool:
    """
    Function check if in each color of board are unique elements.
    It there are function return True. False otherwise.
    >>> check_horizontal(["**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
" 12  ****"])
    True
    >>> check_horizontal(["**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"112  ****"])
    False
    """
    unique = True
    board_c = board[::-1]
    num = num // 2 + 1
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
    """
    Function check if board satisfies the condition of the game.
    It there are function return True. False otherwise.
    >>> check_horizontal(["**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3      **",\
"  8  2***",\
" 12  ****"])
    True
    >>> check_horizontal(["**** ****",\
"***1 ****",\
"**  3****",\
"* 4 1****",\
"     9 5 ",\
" 6  83  *",\
"3   1  **",\
"  8  2***",\
"112  ****"])
    False
    """
    return check_horizontal(brd) and check_vertical(brd) and check_color(brd)


if __name__ == "__main__":
    print('Hello, World!')
