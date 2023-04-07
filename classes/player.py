import pygame
from classes.ship import Ship
from music import play_music_for_event


class Player(Ship):
    def __init__(self, window, speed, width, height, filename, health, delay):
        super().__init__(window, speed, width, height, filename, health, delay)
        self.rect.centerx = self.window_rect.width // 2
        self.rect.bottom = self.window_rect.bottom
        self.bullet_speed = -self.speed
    def shoot(self, bullet_speed):
        super().shoot(bullet_speed)
        play_music_for_event('game music/shoot.mp3')
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.rect.x < self.window_rect.width - self.rect.width - 5:
            self.rect.x += self.speed
        elif keys[pygame.K_SPACE]:
            self.do_delay(lambda: self.shoot(self.bullet_speed))