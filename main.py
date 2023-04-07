import pygame
from classes.locals import Player, GameBoss, Menu
from game_tools import *
from theme import *

pygame.init()

#creating main window, clock and setting FPS
WIDTH, HEIGHT = 600, 650
window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60

sprite_images = {
    'player': ['images/ship_images/spaceship_player.png', YELLOW],
    'red_enemy': ['images/ship_images/red_spaceship.png', RED],
    'blue_enemy': ['images/ship_images/blue_spaceship.png', BLUE],
    'green_enemy': ['images/ship_images/green_spaceship.png', GREEN],
    'boss': ['images/ship_images/boss_spaceship.png', PURPLE]
}

player = Player(window, 8, 120, 120, sprite_images['player'], 0.4, 100)

boss_sprite = GameBoss(window, 1, 180, 180, sprite_images['boss'], 0.8, 100, WIDTH//2, -200)
enemies = pygame.sprite.Group()

#creating fonts and texts for game
basic_font = pygame.font.SysFont('verdana', 30)
events_font = pygame.font.SysFont('kodchiangupc', 90)
menu_font = pygame.font.SysFont('leelawadeeuisemilight', 80, True)

#add event to dictionary as key, add event function as value
events = {
    'win': lambda: win(events_font.render(f"YOU WIN {input_name.get_value()}!", True, GREEN), window=window, position=(10, 250)), 
    'lose': lambda: lose(events_font.render(f"YOU LOSE {input_name.get_value()}!", True, RED), window=window, position=(10, 250)),
}
hard_levels = {1: 'easy', 2: 'medium', 3:'hard', 4:'boss'}
finishing_type = ''
finishing_variants = ['win', 'lose']
enemies_length = 0
level, max_level = 0, 4 #Level by default: 0, max_level with boss: 2


#create menu
main_menu = Menu(window, menu_font)
main_menu.add_button('START', (55, 219, 154), lambda: game())
main_menu.add_button("SETTINGS", (209, 8, 45), lambda: settings())
main_menu.add_button('EXIT', (219, 53, 150), exit)

set_menu = pygame_menu.Menu("Settings", WIDTH, HEIGHT, theme=my_theme)
input_name = set_menu.add.text_input('Name: ', default="username", maxchar=8)
input_name.set_padding((10, 15))

back_btn = set_menu.add.button("<-BACK")
back_btn.set_padding((10, 50))

def menu():
    menu = True
    menu_background = pygame.transform.scale(pygame.image.load('images/backgrounds/laser_bg.jpg'), (WIDTH, HEIGHT))
    pygame.display.set_caption("Main menu")
    while menu:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                menu = False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_UP:
                    main_menu.select(-1)
                elif ev.key == pygame.K_DOWN:
                    main_menu.select(1)
                elif ev.key == pygame.K_RETURN:
                    main_menu.do_func()       
                    menu = False
        window.fill((0, 0, 0))
        window.blit(menu_background, (0, 0))
        main_menu.draw_menu(150)
        pygame.display.update()
        clock.tick(FPS)
def game():
    global level, max_level, enemies_length, finishing_type
    background = pygame.transform.scale(
    pygame.image.load('images/backgrounds/space.jpg'), (WIDTH, HEIGHT)
    )
    pygame.display.set_caption("Space Shooter")
    game, finish, is_boss = [True, False, False] # game = True; finish = False; boss = False
    while game:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                finish = True
        window.fill((0, 0, 0))
        window.blit(background, (0, 0))
        
        if not finish:
            player.move_bullets(*enemies) if not is_boss else player.move_bullets(boss_sprite)
            player.update()
            player.draw()

            if player.health <= 0:
                finishing_type = finishing_variants[1]
                finish = True
            if len(enemies) == 0 and not is_boss:
                level += 1
                if level < max_level:
                    enemies_length += 3
                    [create_enemy(window, enemies, sprite_images[choice(['red_enemy', 'blue_enemy', 'green_enemy'])])
                    for i in range(enemies_length)]
            if level == max_level:
                is_boss = True
            if is_boss:
                boss_sprite.update(player)
                boss_sprite.draw()
                if boss_sprite.health <= 0:
                    is_boss = False
                    finish = True
                    finishing_type = finishing_variants[0]
            enemies.update(player)
            enemies.draw(window)

            health_text = basic_font.render(f"Health: {player.health}", True, RED, WHITE)
            level_text = basic_font.render(f"Level: {hard_levels[level]}", True, WHITE, YELLOW)
            level_text_pos = (WIDTH-level_text.get_width(), 0)
            draw_text(health_text, level_text, window=window, health_pos=(0, 0), level_pos=level_text_pos)
        elif finish:
            player.reset_health()
            boss_sprite.reset_health()
            boss_sprite.rect.x, boss_sprite.rect.y = WIDTH // 2, -100
            boss_sprite.randx = choice(boss_sprite.rand_x_positions)
            level, enemies_length = 0, 0
            is_boss = False
            for i in [player.bullets_group, boss_sprite.bullets_group, enemies]:
                i.empty()
            if finishing_type != '': 
                pygame.time.delay(100)
                events[finishing_type]()
                pygame.display.update()
                pygame.time.delay(3000)
                finishing_type = ''
            game = False 
            menu()

        pygame.display.update()
        clock.tick(FPS)

def settings():
    pygame.display.set_caption("Settings")
    st_process = True
    def quit_settings():
        nonlocal st_process
        st_process = False
        menu()
        
    while st_process:
        window.fill((0, 0, 0))
        
        events = pygame.event.get()
        for ev in events:
            if ev.type ==  pygame.QUIT:
                quit_settings()
        if set_menu.is_enabled():
            back_btn.set_onreturn(quit_settings)
            set_menu.draw(window)
            set_menu.update(events)
        pygame.display.update()
        clock.tick(FPS)

menu()