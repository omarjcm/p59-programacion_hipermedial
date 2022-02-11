import pygame

class Ray:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect( self.game.screen, (254, 52, 110), pygame.Rect(self.x, self.y, 2, 4) )
        self.y -= 2