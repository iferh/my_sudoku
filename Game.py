import pygame
from copy import deepcopy
from solver import solve_puzzle
from maker import make_puzzle

pygame.font.init()
solved = False
run = False


class Square:
    def __init__(self, real_value, row, col, width, height):
        self.real_value = real_value
        self.temp_value = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False
        self.x = 10 + (self.width * self.col) + (2 * self.col) + (4 * (self.col // 3))
        self.y = 10 + (self.height * self.row) + (2 * self.row) + (4 * (self.row // 3))

    def select(self, window):
        mouse = pygame.mouse.get_pos()
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            s = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            s.fill((0, 50, 225, 128))
            window.blit(s, (self.x, self.y))
        if self.selected:
            pygame.draw.rect(window, (0, 0, 245), (self.x, self.y, self.width, self.height), 3)


class Grid:
    def __init__(self, board):
        self.board = board
        self.height = 55
        self.width = 55
        self.squares = [Square(self.board[row][col], row, col, self.width, self.height) for col in range(9) for row in
                        range(9)]
        self.selected_square = None

    def select(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for square in self.squares:
            if square.x + square.width > mouse[0] > square.x and square.y + square.height > mouse[1] > square.y:
                if click[0] == 1:
                    self.selected_square = square
                    square.selected = True
            if square != self.selected_square:
                square.selected = False

    def draw(self, window):
        num_font = pygame.font.SysFont("comicsans", 40)
        draft_font = pygame.font.SysFont("comicsans", 20)
        for square in self.squares:
            # Draw squares
            pygame.draw.rect(window, (255, 255, 255), (square.x, square.y, square.width, square.height))
            # Draw numbers
            if square.real_value != 0:
                square_value = num_font.render(str(square.real_value), True, (0, 0, 0))
                text_center = (square.x + square.width / 2 - square_value.get_width() / 2,
                               square.y + square.height / 2 - square_value.get_height() / 2)
                window.blit(square_value, text_center)
            # Draw draft numbers
            if square.temp_value != 0:
                draft_value = draft_font.render(str(square.temp_value), True, (150, 150, 150))
                window.blit(draft_value, (square.x + 3, square.y + 3))
            # Draw selection animation
            square.select(window)


# Button function
def button(window, msg, x, y, width, height, icolor, acolor, action=None):
    button_font = pygame.font.SysFont("comicsans", 20)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(window, acolor, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(window, icolor, (x, y, width, height))
    button_label = button_font.render(msg, True, (0, 0, 0))
    text_center = (x + width / 2 - button_label.get_width() / 2, y + height / 2 - button_label.get_height() / 2)
    window.blit(button_label, text_center)


# Quit Game
def quit_game():
    pygame.quit()
    quit()


# Solve board
def do_solve():
    global solved
    solved = True


def new_puzzle():
    global run
    run = False
    main()


def main():
    global solved, run
    solved = False
    DISPLAY_WI, DISPLAY_HE = 680, 570
    FPS = 30
    WIN = pygame.display.set_mode((DISPLAY_WI, DISPLAY_HE))
    pygame.display.set_caption("My Sudoku")
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 30)
    # Variables
    mistakes = 0
    won = False
    board = make_puzzle()
    grid = Grid(board)
    solved_board = deepcopy(board)
    solve_puzzle(solved_board)
    run = True

    def redraw_window():
        WIN.fill((200, 200, 200))

        # Draw grid
        if not solved:
            grid.draw(WIN)
        else:
            solved_grid = Grid(solved_board)
            solved_grid.draw(WIN)

        # Draw text
        mistakes_label = main_font.render(f"Mistakes: {mistakes}", True, (255, 255, 255))
        WIN.blit(mistakes_label, (10, DISPLAY_HE - 30))

        # Draw buttons
        button(WIN, "New Puzzle", DISPLAY_WI - 135, 10, 120, 50, (255, 255, 255), (127, 152, 240), new_puzzle)
        button(WIN, "Solve Puzzle", DISPLAY_WI - 135, 70, 120, 50, (255, 255, 255), (127, 152, 240), do_solve)
        button(WIN, "Quit Game", DISPLAY_WI - 135, DISPLAY_HE - 90, 120, 50, (255, 255, 255), (127, 152, 240),
               quit_game)

        # Draw victory text
        if won:
            victory_label = main_font.render("Completed", True, (127, 152, 240))
            WIN.blit(victory_label, (DISPLAY_WI - victory_label.get_width() - 30, 130))

        # Update
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        # Activate select function in grid
        grid.select()

        # Key press
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and grid.selected_square.real_value == 0:
                if event.key == pygame.K_1:
                    grid.selected_square.temp_value = 1
                if event.key == pygame.K_2:
                    grid.selected_square.temp_value = 2
                if event.key == pygame.K_3:
                    grid.selected_square.temp_value = 3
                if event.key == pygame.K_4:
                    grid.selected_square.temp_value = 4
                if event.key == pygame.K_5:
                    grid.selected_square.temp_value = 5
                if event.key == pygame.K_6:
                    grid.selected_square.temp_value = 6
                if event.key == pygame.K_7:
                    grid.selected_square.temp_value = 7
                if event.key == pygame.K_8:
                    grid.selected_square.temp_value = 8
                if event.key == pygame.K_9:
                    grid.selected_square.temp_value = 9
                if event.key == pygame.K_DELETE:
                    grid.selected_square.temp_value = 0
                if event.key == pygame.K_BACKSPACE:
                    grid.selected_square.temp_value = 0
                if event.key == pygame.K_RETURN and grid.selected_square.temp_value != 0:
                    row = grid.selected_square.row
                    col = grid.selected_square.col
                    if grid.selected_square.temp_value == solved_board[row][col]:
                        grid.selected_square.real_value = grid.selected_square.temp_value
                        grid.selected_square.temp_value = 0
                        board[row][col] = solved_board[row][col]
                    else:
                        mistakes += 1
                        grid.selected_square.temp_value = 0

        if 0 not in [board[row][col] for col in range(9) for row in range(9)]:
            won = True


# Call main
main()
