import pygame

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, window, speed, width, height, x=0,y=0):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = x, y
        self.speed = speed
        self.window = window
        self.window_rect = self.window.get_rect()
    def draw(self):
        self.window.blit(self.image, self.rect)
    
    def off_screen(self):
        return self.rect.bottom >= self.window_rect.height if self.speed > 0 \
            else self.rect.top < 0