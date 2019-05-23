import pygame as pg


class Game:
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    background_color = (50, 50, 50)

    size_x = 5
    size_y = 5

    default_x_numbers = (2, 4, (3, 1), (1, 1), 1)
    default_y_numbers = (4, 3, 2, 1, 3)

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

    def __init__(self):
        pg.init()

        self.screen_width = self.cell_size * self.size_x + self.size_x - 1
        self.screen_height = self.cell_size * self.size_y + self.size_y - 1
        self.game_display = pg.display.set_mode((self.screen_width, self.screen_height))
        clock = pg.time.Clock()

        self.print_board()
        self.print_cell(2, 1)

        font = pg.font.SysFont("Arial", 18)
        text = font.render("Test", True, self.red)
        pg.display.set_caption("PICROSS SOLVER")

        # Debug print
        # self.game_display.blit(text, (self.screen_width // 2 - text.get_width() // 2, self.screen_width // 2 - text.get_height() // 2))

        done = False

        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                # print(event)
            pg.display.update()
            clock.tick(60)
