import pygame, time
from classes.bullet import Bullet
from classes.game_sprite import GameSprite

class Ship(GameSprite):
    bullet_power = 10
    def __init__(self, window, speed, width, height, 
                filename, delay, health, x=0, y=0):
        super().__init__(window, speed, width, height, x, y)
        self.health = health
        self.filename = filename
        self.image = pygame.transform.scale(
            pygame.image.load(filename[0]), (width, height)
        )
        self.delay = delay
        self.last_shoot = 0
        self.bullets_group = pygame.sprite.Group()
        self.START_HEALTH = self.health
    def do_delay(self, func):
        if time.time() - self.last_shoot >= self.delay:
            self.last_shoot = time.time()
            func()

    def shoot(self, bullet_speed, bullet_padding_x=0):
        bullet = Bullet(self.window, 2, 25, self.rect.centerx+bullet_padding_x,
                            self.rect.centery, 
                            bullet_speed, self.filename[1])
        self.bullets_group.add(bullet)

    def move_bullets(self, *enemies):
        self.bullets_group.draw(self.window)
        self.bullets_group.update()
        if pygame.sprite.groupcollide(self.bullets_group, enemies, False, False):
            for x in enemies:
                if pygame.sprite.spritecollide(x, self.bullets_group, True):
                    x.health -= Ship.bullet_power
    def reset_health(self):
        self.health = self.START_HEALTH