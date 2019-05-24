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
    board = np.zeros((size_x, size_y), np.int8)

    y_set = np.zeros(size_y, np.int8)
    y_series = np.zeros(size_y, np.int8)
    number_of_y_series = 0

    # TODO implement loading boards from file
    x_numbers = ((4, 3, 2, 1, 3))
    y_numbers = [[5], [4], [3], [2, 2], [3, 1]]
    # y_numbers = (2, 4, (3, 1), (1, 1), 1)

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
        pg.draw.rect(self.game_display, self.red,
                     pg.Rect(x * (self.cell_size + 1), y * (self.cell_size + 1), self.cell_size, self.cell_size))

    def sum_of_y(self, y):
        result = 0
        numbers = self.y_numbers[y]
        for i in range(len(numbers)):
            result += numbers[i]
        return result

    def sum_of_y_set(self):
        result = 0
        for i in range(self.size_y):
            result += self.y_set[i]
        return result

    def check_y(self, y, n=0, start_point=0):
        # TODO check where the bug is
        numbers = self.y_numbers[y]
        size = len(numbers) - n
        possibilities = self.size_y - start_point - (size - 1) + 1
        for o in range(size):
            possibilities -= numbers[size - o - 1]
        # end_point = start_point + numbers[n]
        possible = True
        for p in range(possibilities):
            for b in range(numbers[n]):
                if self.board[y, start_point + b + p] == -1:
                    possible = False
                    break
            if possible:
                for b in range(numbers[n]):
                    self.y_set[b + start_point] = 1
                if size - 1 != 0:
                    self.check_y(y, (n + 1), start_point + p + numbers[n] + 1)
                elif self.sum_of_y(y) == self.sum_of_y_set():
                    for b in range(self.size_y):
                        self.y_series[b] += self.y_set[b]
                    self.number_of_y_series += 1
                for b in range(numbers[n]):
                    self.y_set[b + start_point + p] = 0

    def correct_y(self, y):
        for o in range(self.size_y):
            if self.y_series[o] == self.number_of_y_series:
                self.board[y, o] = 1
            elif self.y_series[o] == 0:
                self.board[y, o] = -1

    def update_y(self, y):
        for o in range(self.size_y):
            if self.board[y, o] == 1:
                self.print_cell(y, o)

    def check_x(self, x, n=0, start_point=0):
        pass
        # TODO copy-paste from check_y (change y to x)

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
                # for y in range(5):
                self.y_set = np.zeros(self.size_y, np.int8)
                self.y_series = np.zeros(self.size_y, np.int8)
                self.number_of_y_series = 0
                self.check_y(y)
                self.correct_y(y)
                self.update_y(y)
                # TODO think of a way of printing only NEW cells
                pg.display.update()
