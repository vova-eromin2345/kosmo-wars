import pygame_menu

my_theme = pygame_menu.themes.THEME_ORANGE.copy()

my_theme.background_color = (10, 10, 10)

my_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE_TITLE
my_theme.cursor_color = (100, 0, 0)

my_theme.title_font = pygame_menu.font.FONT_MUNRO
my_theme.title_font_size = 70
my_theme.title_font_color = (199, 14, 39)

my_theme.widget_font_color = (200, 0, 0)
my_theme.widget_background_color = (10, 10, 10)
my_theme.widget_border_width = 5
my_theme.widget_border_color = (200, 0, 0)
my_theme.widget_margin = (10, 20)
my_theme.widget_font_size = 30
