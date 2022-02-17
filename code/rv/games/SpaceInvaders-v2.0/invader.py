import pygame as pg

class Invader(pg.sprite.Sprite):
    
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load( './images/spaceInvaders.png' )
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.game = game
