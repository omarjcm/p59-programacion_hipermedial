import pygame as pg
from invader import *
from player import *
from turtle import window_width, window_height

class Game:
    window_width
    window_height

    rows = 3
    cols = 10

    def __init__(self, width, height):
        pg.init()

        self.clock = pg.time.Clock()

        self.window_width = width
        self.window_height = height

        self.screen = pg.display.set_mode( (self.window_width, self.window_height) )
        pg.display.set_caption( 'Space Invaders' )

        self.background = pg.image.load('./images/background.jpg')

        self.invaders_group = pg.sprite.Group()
        self.create_invaders()

        self.players_group = pg.sprite.Group()
        self.player = Player(self, int(self.window_width/2), self.window_height - 100)
        self.players_group.add( self.player )

        self.player_bullets = pg.sprite.Group()

        self.game_over = True
        while self.game_over:
            self.screen.blit( self.background, (0,0) )

            self.invaders_group.update()
            self.players_group.update()

            self.player_bullets.update()

            self.invaders_group.draw( self.screen )
            self.players_group.draw( self.screen )

            self.player_bullets.draw( self.screen )

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_over = False

            pg.display.update()
            self.clock.tick(60)

        pg.quit()

    def create_invaders(self):
        for row in range(self.rows):
            for col in range(self.cols):
                invader = Invader(self, 100 + col * 65, 80 + row * 50)
                self.invaders_group.add( invader ) 


if __name__ == '__main__':
    game = Game(800, 600)