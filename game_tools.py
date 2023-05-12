from random import choice
from classes.locals import Enemy
from music import *
from variables import ENEMY_WIDTH, ENEMY_HEIGHT

def create_enemy(window, enemies_group, enemy_color):
    random_pos_x = choice(list(range(0, window.get_width() - 100)))
    random_pos_y = choice(list(range(-1400, -100)))
    _enemy_ = Enemy(window, 3, ENEMY_WIDTH, ENEMY_HEIGHT, enemy_color,
                        0.4, Enemy.bullet_power, random_pos_x, random_pos_y)
    enemies_group.add(_enemy_)

def draw_text(*text_objects, window, **positions):
    for obj, pos in zip(text_objects, positions.values()):
        window.blit(obj, pos)

def win(win_text, window, position):
    draw_text(win_text, window=window, win_pos=position)
    play_music_for_event("game music/win_music.mp3")

def lose(lose_text, window, position):
    draw_text(lose_text, window=window, lose_pos=position)
    play_music_for_event("game music/game over music.mp3")
