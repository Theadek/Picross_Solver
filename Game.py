import pygame as pg


class Game:

    red = (255, 0, 0)
    background_color = (50, 50, 50)

    default_size_x = 5
    default_size_y = 5

    default_x_numbers = (2, 4, (3, 1), (1, 1), 1)
    default_y_numbers = (4, 3, 2, 1, 3)

    def __init__(self):
        pg.init()
        screen_width = 600
        game_display = pg.display.set_mode((screen_width, screen_width))
        clock = pg.time.Clock()

        font = pg.font.SysFont("Arial", 18)
        text = font.render("Test", True, self.red)
        pg.display.set_caption("PICROSS SOLVER")
        game_display.fill(self.background_color)
        game_display.blit(text, (screen_width//2 - text.get_width()//2, screen_width//2 - text.get_height()//2))


        done = False

        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                # print(event)
            pg.display.update()
            clock.tick(60)
