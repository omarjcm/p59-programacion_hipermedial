import pygame
from alien import Alien
from generator import Generator
from starship import Starship
from ray import Ray

'''
Basado en: https://github.com/janjilecek/pygame-invaders/blob/master/main.py
'''

class Game:
    screen = None 
    aliens = []
    rays = []
    lost = False

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode( (self.width, self.height) )
        self.clock = pygame.time.Clock()
        done = False

        starship = Starship(self, self.width/2, self.height-20)
        generator = Generator(self)

        while not done:
            if len(self.aliens) == 0:
                self.displayText( 'VICTORIA ALCANZADA' )

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_LEFT]:
                starship.x -= 2 if starship.x > 20 else 0
            elif pressed[pygame.K_RIGHT]:
                starship.x += 2 if starship.x < (self.width - 20) else 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.rays.append( Ray(self, starship.x, starship.y) )

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill( (0,0,0) )

            for alien in self.aliens:
                alien.draw()
                alien.checkCollision(self)

                if alien.y > self.height-20:
                    self.lost = True
                    self.displayText( 'PERDISTE!' )
            
            for ray in self.rays:
                ray.draw()
            
            if not self.lost:
                starship.draw()

    def displayText(self, texto):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 50)
        textSurface = font.render(texto, False, (44, 0, 63))
        self.screen.blit( textSurface, (110, 160) )

if __name__ == '__main__':
    game = Game(600, 400)