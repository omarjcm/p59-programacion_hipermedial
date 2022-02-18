import pygame as pg

class Player(pg.sprite.Sprite):

    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load( './images/user.png' )
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.game = game
    
    def update(self):
        self.speed = 3
        self.key = pg.key.get_pressed()

        if self.key[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        
        if self.key[pg.K_RIGHT] and self.rect.right < self.game.window_width:
            self.rect.x += self.speed
            
        if self.key[pg.K_SPACE]:
            bullet = Player_Bullet(self.rect.centerx, self.rect.top)
            self.game.player_bullets.add( bullet )



class Player_Bullet(pg.sprite.Sprite):

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load( './images/user_bullet.png' )
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

        self.sound = pg.mixer.Sound('./sounds/shoot.wav')
        self.sound.play()

    def update(self):
        self.rect.y -= 5
        