import pygame
from classes.locals import Player, GameBoss, Menu
from game_tools import *
from theme import *
from variables import * 

pygame.init()

#creating main window, clock
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


#create game sprites
player = Player(window, 8, PLAYER_WIDTH, PLAYER_HEIGHT, sprite_images['player'], 0.4, 100)
boss_sprite = GameBoss(window, 2, BOSS_WIDTH, BOSS_HEIGHT, sprite_images['boss'], 0.8, 100, WIDTH//2, -200)
enemies = pygame.sprite.Group()

#create fonts
basic_font = pygame.font.SysFont('verdana', 40)
events_font = pygame.font.SysFont('verdana', 60, True)
menu_font = pygame.font.SysFont('Arial', 80, True)

#add event to dictionary as key, add event function as value
events = {
    'win': lambda: win(events_font.render(f"YOU WIN {input_name.get_value()}!", True, GREEN, BLACK), window=window, position=(10, 250)), 
    'lose': lambda: lose(events_font.render(f"YOU LOSE {input_name.get_value()}!", True, RED, BLACK), window=window, position=(10, 250)),
}

hard_levels = {1: 'easy', 2: 'medium', 3:'hard', 4:'boss'}
location_levels = {1: 'space', 2: 'forest', 3: 'sea', 4: 'volcano'}
finishing_type = ''
finishing_variants = ['win', 'lose']
enemies_length = 3
level, max_level = 1, 4 #Start level: 1, max_level with boss: 4


#create main and set menu
main_menu = Menu(window, menu_font)
main_menu.add_button('START', (55, 219, 154), lambda: game())
main_menu.add_button("SETTINGS", (209, 8, 45), lambda: settings())
main_menu.add_button('EXIT', (219, 53, 150), exit)

#create settings menu
set_menu = pygame_menu.Menu("Settings", WIDTH, HEIGHT, theme=my_theme)
change_img_btn = set_menu.add.button('Change avatar', lambda: change_image(avatar_img))
change_img_btn.set_padding((5, 50))

input_name = set_menu.add.text_input('Name: ', default="username", maxchar=12)
input_name.set_padding((10, 15))

back_btn = set_menu.add.button("<-BACK")
back_btn.set_padding((10, 50))

avatar_img = set_menu.add.image(avatar_path)

avatar_img.resize(avatar_width, avatar_height)
avatar_img.translate(WIDTH//2-avatar_img.get_width()//2-20, -HEIGHT//2)

def menu(): 
    '''Show main menu with options'''
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
    '''function with game process'''
    global level, max_level, enemies_length, finishing_type
    background = pygame.transform.scale(
        pygame.image.load(location_themes['background'].get(location_levels.get(level))), 
        (WIDTH, HEIGHT))
    
    pygame.display.set_caption("Space Shooter")
    game, finish, is_boss = [True, False, False] # game = True; finish = False; boss = False
    [create_enemy(window, enemies, sprite_images[random.choice(['red_enemy', 'blue_enemy', 'green_enemy'])])
                    for i in range(enemies_length)]
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
                background = pygame.transform.scale(
                    pygame.image.load(location_themes['background'].get(location_levels.get(level))), 
                    (WIDTH, HEIGHT))
                if level < max_level:
                    enemies_length += 3
                    [create_enemy(window, enemies, sprite_images[random.choice(['red_enemy', 'blue_enemy', 'green_enemy'])])
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
            health_text = basic_font.render(f"Health: {player.health}", True, *location_themes['health_text'][location_levels[level]])
            level_text = basic_font.render(f"Level: {hard_levels[level]}", True, *location_themes['score_text'][location_levels[level]])
            level_text_pos = (WIDTH-level_text.get_width(), 0)
            draw_text(health_text, level_text, window=window, health_pos=(0, 0), level_pos=level_text_pos)
        elif finish:
            player.reset_health()
            boss_sprite.reset_health()
            boss_sprite.rect.x, boss_sprite.rect.y = WIDTH // 2, -100
            boss_sprite.randx = random.choice(boss_sprite.rand_x_positions)
            level, enemies_length = 1, 3
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
    '''Show and check events setting menu'''
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

            set_menu.draw(window)
            set_menu.update(events)
            back_btn.set_onreturn(quit_settings)
        pygame.display.update()
        clock.tick(FPS)

menu()