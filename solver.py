# solver.py

def solve_puzzle(grid):
    empty = pick_empty(grid)
    if not empty:
        return True
    else:
        y, x = empty
    for num in range(1, 10):
        if check_valid(grid, num, (y, x)):
            grid[y][x] = num
            if solve_puzzle(grid):
                return True
            grid[y][x] = 0
    return False


def check_valid(grid, num, pos):
    y, x = pos
    # check if num is valid within row
    for i in range(9):
        if num == grid[y][i] and x != i:
            return False
    # check if num is valid within col
    for i in range(len(grid)):
        if num == grid[i][x] and y != i:
            return False
    # check if num is valid within 3x3 box
    a = [y // 3 * 3 + i for i in range(3)]
    b = [x // 3 * 3 + i for i in range(3)]
    for r, c in [(r, c) for r in a for c in b]:
        if num == grid[r][c] and r != y and c != x:
            return False
    # return true if all tests are false
    return True


def pick_empty(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                return y, x  # returning tuple row, column
    return False


def print_board(grid):
    for y in range(9):
        if y % 3 == 0 and y != 0:  # print line under every 3 rows
            print('— ' * 17)
        for x in range(9):
            if x % 3 == 0 and x != 0:  # print separator under every 3 cols
                print(' | ', end="")
            if x == 8:
                print(f' {grid[y][x]} ')
            else:
                print(f' {grid[y][x]} ', end="")
