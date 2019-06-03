import pygame as pg
import numpy as np


class Game:
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 128)
    background_color = (50, 50, 50)

    was_sth_corrected = False

    # TODO implement loading boards from file
    x_numbers = []
    y_numbers = []

    cell_size = 20

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

    def print_x_on_cell(self, x, y):
        start = (x * self.cell_size + self.cell_size // 4 + x, y * self.cell_size + self.cell_size // 4 + y)
        end = (x * self.cell_size + self.cell_size - self.cell_size // 4 + x,
               y * self.cell_size + self.cell_size - self.cell_size // 4 + y)
        pg.draw.line(self.game_display, self.blue, start, end, self.cell_size // 10)
        start = (
        x * self.cell_size + self.cell_size - self.cell_size // 4 + x, y * self.cell_size + self.cell_size // 4 + y)
        end = (
        x * self.cell_size + self.cell_size // 4 + x, y * self.cell_size + self.cell_size - self.cell_size // 4 + y)
        pg.draw.line(self.game_display, self.blue, start, end, self.cell_size // 10)

    def sum_of_y(self, y):
        result = 0
        numbers = self.y_numbers[y]
        for i in range(len(numbers)):
            result += numbers[i]
        return result

    def sum_of_y_set(self, y):
        result = 0
        for i in range(self.size_y):
            if self.y_set[i] == 1:
                result += 1
            elif self.board[y, i] == 1:
                result += 1
        return result

    def check_y(self, y, n=0, start_point=0):
        numbers = self.y_numbers[y]
        size = len(numbers) - n
        possibilities = self.size_y - start_point - (size - 1) + 1
        for o in range(size):
            possibilities -= numbers[size + n - o - 1]
        for p in range(possibilities):
            possible = True
            for b in range(numbers[n]):
                if self.board[y, start_point + b + p] == -1:
                    possible = False
                    break
            if possible:
                for b in range(numbers[n]):
                    self.y_set[b + start_point + p] = 1
                if size - 1 != 0:
                    self.check_y(y, (n + 1), start_point + p + numbers[n] + 1)
                elif self.sum_of_y(y) == self.sum_of_y_set(y):
                    self.y_series += self.y_set
                    self.number_of_y_series += 1
                for b in range(numbers[n]):
                    self.y_set[b + start_point + p] = 0

    def correct_y(self, y):
        for o in range(self.size_y):
            if self.y_series[o] == self.number_of_y_series and self.board[y, o] != 1:
                self.board[y, o] = 1
                self.print_cell(y, o)
                self.was_sth_corrected = True
            elif self.y_series[o] == 0 and self.board[y, o] != -1:
                self.board[y, o] = -1
                self.print_x_on_cell(y, o)
                self.was_sth_corrected = True

    def update_y(self, y):
        for o in range(self.size_y):
            if self.board[y, o] == 1:
                self.print_cell(y, o)
            elif self.board[y, o] == -1:
                self.print_x_on_cell(y, o)

    def sum_of_x(self, x):
        result = 0
        numbers = self.x_numbers[x]
        for i in range(len(numbers)):
            result += numbers[i]
        return result

    def sum_of_x_set(self, x):
        result = 0
        for i in range(self.size_x):
            if self.x_set[i] == 1:
                result += 1
            elif self.board[i, x] == 1:
                result += 1
        return result

    def check_x(self, x, n=0, start_point=0):
        numbers = self.x_numbers[x]
        size = len(numbers) - n
        possibilities = self.size_x - start_point - (size - 1) + 1
        for o in range(size):
            possibilities -= numbers[size + n - o - 1]
        for p in range(possibilities):
            possible = True
            for b in range(numbers[n]):
                if self.board[start_point + b + p, x] == -1:
                    possible = False
                    break
            if possible:
                for b in range(numbers[n]):
                    self.x_set[b + start_point + p] = 1
                if size - 1 != 0:
                    self.check_x(x, (n + 1), start_point + p + numbers[n] + 1)
                elif self.sum_of_x(x) == self.sum_of_x_set(x):
                    self.x_series += self.x_set
                    self.number_of_x_series += 1
                for b in range(numbers[n]):
                    self.x_set[b + start_point + p] = 0

    def correct_x(self, x):
        if self.number_of_x_series != 0:
            for o in range(self.size_x):
                if self.x_series[o] == self.number_of_x_series and self.board[o, x] != 1:
                    self.board[o, x] = 1
                    self.print_cell(o, x)
                    self.was_sth_corrected = True
                elif self.x_series[o] == 0 and self.board[o, x] != -1:
                    self.board[o, x] = -1
                    self.print_x_on_cell(o, x)
                    self.was_sth_corrected = True

    def read_from_file(self, file, tolist):
        line = file.readline()
        number = ""
        answer = []
        for c in line:
            if c == ' ':
                answer.append(int(number))
                number = ""
            elif c == "\n":
                continue
            else:
                number += c
        answer.append(int(number))
        tolist.append(answer)

    def __init__(self, path):
        pg.init()
        pg.display.set_caption("PICROSS SOLVER")

        file = open(path, "r")
        x = int(file.readline())
        y = int(file.readline())

        for i in range(x):
            self.read_from_file(file, self.x_numbers)

        for i in range(y):
            self.read_from_file(file, self.y_numbers)

        file.close()

        self.size_x = x
        self.size_y = y

        # 0 -> unknown, 1 -> full, -1 -> empty
        self.board = np.zeros((self.size_x, self.size_y), np.int8)

        self.y_set = np.zeros(self.size_y, np.int8)
        self.y_series = np.zeros(self.size_y, np.int8)
        self.number_of_y_series = 0

        self.x_set = np.zeros(self.size_x, np.int8)
        self.x_series = np.zeros(self.size_x, np.int8)
        self.number_of_x_series = 0

        self.screen_width = self.cell_size * self.size_x + self.size_x - 1
        self.screen_height = self.cell_size * self.size_y + self.size_y - 1
        self.game_display = pg.display.set_mode((self.screen_width, self.screen_height))
        # clock = pg.time.Clock()

        self.print_board()

        pg.display.update()
        done = False
        do_check = True

        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
            if do_check:
                self.was_sth_corrected = False
                for y in range(self.size_x):
                    self.y_set = np.zeros(self.size_y, np.int8)
                    self.y_series = np.zeros(self.size_y, np.int8)
                    self.number_of_y_series = 0
                    self.check_y(y)
                    self.correct_y(y)
                    pg.display.update()
                for x in range(self.size_y):
                    self.x_set = np.zeros(self.size_x, np.int8)
                    self.x_series = np.zeros(self.size_x, np.int8)
                    self.number_of_x_series = 0
                    self.check_x(x)
                    self.correct_x(x)
                    pg.display.update()
                if self.was_sth_corrected is False:
                    do_check = False
