from classes.game_sprite import GameSprite

class Bullet(GameSprite):
    def __init__(self, window, width, height, centerx, centery, speed, color):
        super().__init__(window, speed, width, height)
        self.image.fill(color)
        self.rect.centerx = centerx
        self.rect.centery = centery
    def update(self):
        self.rect.y += self.speed
        if self.off_screen():
            self.kill()