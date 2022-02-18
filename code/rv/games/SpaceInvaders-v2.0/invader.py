import pygame as pg

class Invader(pg.sprite.Sprite):

    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load( './images/spaceInvaders.png' )
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.game = game

        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1

        if self.move_counter > 75:
            self.move_direction *= -1
            self.move_counter *= -1
