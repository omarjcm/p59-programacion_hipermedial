import pygame
from alien import Alien

'''
Basado en: https://github.com/janjilecek/pygame-invaders/blob/master/main.py
'''

class Game:
    screen = None 
    alliens = []

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode( (self.width, self.height) )
        self.clock = pygame.time.Clock()
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill( (0,0,0) )

            alien = Alien(self, 30, 30)
            alien.draw()


            

if __name__ == '__main__':
    game = Game(600, 400)