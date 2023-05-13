WIDTH, HEIGHT = 800, 850

FPS = 60

PLAYER_WIDTH, PLAYER_HEIGHT = 150, 150
BOSS_WIDTH, BOSS_HEIGHT = 200, 200
ENEMY_WIDTH, ENEMY_HEIGHT = 120, 120

bullet_power = 10

WHITE = (255, 255, 255)
RED = (242, 27, 27)
BLUE = (27, 102, 242)
PURPLE = (172, 5, 250)
YELLOW = (179, 176, 30)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)


sprite_images = {
    'player': ['images/ship_images/spaceship_player.png', PURPLE],
    'red_enemy': ['images/ship_images/red_spaceship.png', RED],
    'blue_enemy': ['images/ship_images/blue_spaceship.png', BLUE],
    'green_enemy': ['images/ship_images/green_spaceship.png', GREEN],
    'boss': ['images/ship_images/boss_spaceship.png', YELLOW]
}
bg_path = 'images/backgrounds'

location_themes = {
    'background': {'space': f'{bg_path}/space.jpg', 'forest': f'{bg_path}/forest.jpg', 'sea': f'{bg_path}/sea.jpg', 'volcano': f'{bg_path}/volcano.jpg'},
    'score_text': {'space': (WHITE, YELLOW), 'forest': (WHITE, (53, 199, 48)), 'sea': (WHITE, BLUE), 'volcano': (WHITE, PURPLE)},
    'health_text': {'space': (RED, WHITE), 'forest': ((9, 110, 5), WHITE), 'sea': (BLUE, WHITE), 'volcano': ((126, 15, 163), WHITE)}
}