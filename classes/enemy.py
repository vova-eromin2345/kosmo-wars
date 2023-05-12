import pygame
from classes.ship import Ship
from random import choice, randint
from variables import FPS


class Enemy(Ship):
    def update(self, player):
        self.move_bullets(player)
        self.rect.y += self.speed
        if len(self.groups()[0].sprites()) == randint(0, FPS*2) and self.rect.y >= -150:
           self.do_delay(lambda: self.shoot(8))
        if pygame.sprite.collide_rect(player, self) or self.off_screen():
            player.health -= self.health
            self.kill()
        if self.health <= 0:
            self.kill()
class GameBoss(Enemy):
    rand_x_positions = [-4, -3, -2, 2, 3, 4]
    randx = choice(rand_x_positions)
    def update(self, player):
        self.rect.y += self.speed
        self.rect.x += self.randx
        if self.rect.x > (self.window_rect.width-self.rect.width-5) or self.rect.x < 5:
            self.randx *= -1
        self.do_delay(lambda: self.shoot( abs(self.randx) * 2))
        self.move_bullets(player)
        if pygame.sprite.collide_rect(self, player) or self.off_screen():
            player.health -= self.health
    def shoot(self, bullet_speed):
        super().shoot(bullet_speed, 10)
        super().shoot(bullet_speed, -10)