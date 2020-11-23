from random import sample
base = 3


def valid_board(bo):
    for i in range(len(bo)):
        # check if rows are valid
        tmp_row = [i for i in bo[i] if i != 0]
        if len(tmp_row) != len(set(tmp_row)):
            return False

        # check if cols are valid
        tmp_col = [bo[j][i] for j in range(len(bo[0])) if bo[j][i] != 0]
        if len(tmp_col) != len(set(tmp_col)):
            return False

    # check internal boxes are valid
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp_box = [bo[i + x][j + y] for x in range(3) for y in range(3) if bo[i + x][j + y] != 0]
            if len(tmp_box) != len(set(tmp_box)):
                return False

    return True


# from https://stackoverflow.com/questions/45471152
def make_board():
    rows = [g*base + r for g in jumble(range(base)) for r in jumble(range(base))]
    cols = [g*base + c for g in jumble(range(base)) for c in jumble(range(base))]
    nums = jumble(range(1, base*base+1))
    # make board
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]
    if valid_board(board):
        return board
    else:
        make_board()


# function to make pattern for a baseline valid solution
def pattern(r, c):
    return (base*(r % base) + r//base+c) % (base**2)


# function to shuffle not in place
def jumble(iterable):
    return sample(iterable, len(iterable))


def make_puzzle():
    board = make_board()
    size = base ** 2
    blanks = size ** 2 * 1 // 2
    cells = [(r, c) for r in range(size) for c in range(size)]
    for (r, c) in sample(cells, blanks):
        assert isinstance(r, int)
        assert isinstance(c, int)
        board[r][c] = 0
    return board
