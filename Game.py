import pygame as pg
import numpy as np

class Game:
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    background_color = (50, 50, 50)

    size_x = 5
    size_y = 5

    # 0 - null, 1 - full, 2 - X
    board = np.zeros(size_x, size_y)
    full_series_x = np.zeros(size_x)
    null_series_x = np.zeros(size_x)
    full_series_y = np.zeros(size_y)
    null_series_y = np.zeros(size_y)

    x_numbers = (4, 3, 2, 1, 3)
    y_numbers = (2, 4, (3, 1), (1, 1), 1)

    cell_size = 80

    def print_board(self):
        self.game_display.fill(self.background_color)
        for x in range(self.size_x - 1):
            start = (x * (self.cell_size + 1) + self.cell_size, 0)
            end = (x * (self.cell_size + 1) + self.cell_size, self.screen_height - 1)
            pg.draw.line(self.game_display, self.white, start, end, 1)
        for y in range(self.size_y - 1):
            start = (0, y * (self.cell_size + 1) + self.cell_size)
            end = (self.screen_width - 1, y * (self.cell_size + 1) + self.cell_size)
            pg.draw.line(self.game_display, self.white, start, end, 1)

    def print_cell(self, x, y):
        pg.draw.rect(self.game_display, self.black,
                     pg.Rect(x * (self.cell_size + 1), y * (self.cell_size + 1), self.cell_size, self.cell_size))

    def check_y(self, y, n=0, start_point=0):
        numbers = self.y_numbers[y]
        size = len(numbers)
        possibilites = self.size_y - start_point - (size - 1) + 1
        for o in range(size):
            possibilites -= numbers[0]
        # end_point = start_point + numbers[n]
        for p in range(possibilites):
            pass
            # TODO check if cells are free/full
            # TODO if n != size-1: self.check_y(y, n + 1, starting_point + p + numbers[n] + 1)

        # TODO check full_series_y to see which cells are full and which ones are null

        # TODO think about examples where there is NO correct arrangement

    # def check_y(self, y, n):
    #     numbers = self.y_numbers[y]
    #     size = len(numbers)
    #     for s in range(size):
    #         possibilities = self.size_y - (size - 1) + 1
    #         for o in range(size):
    #             possibilities -= numbers[o]
    #         start_pos = 0
    #         for o in range(s):
    #             start_pos += numbers[o] + 1
    #         end_pos = start_pos + numbers[s]
    #
    #         for i in range(possibilities):



    def __init__(self):
        pg.init()
        pg.display.set_caption("PICROSS SOLVER")

        self.screen_width = self.cell_size * self.size_x + self.size_x - 1
        self.screen_height = self.cell_size * self.size_y + self.size_y - 1
        self.game_display = pg.display.set_mode((self.screen_width, self.screen_height))
        # clock = pg.time.Clock()

        self.print_board()

        done = False

        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                # print(event)
            for y in range(self.size_y):
                self.check_y(y)
                pg.display.update()
