import pygame

class Menu:
    def __init__(self, window, font):
        self.functions = []
        self.buttons = []
        self.select_btn_index = 0
        self.window = window
        self.window_rect = self.window.get_rect()
        self.font = font
    
    def add_button(self, text, btn_color, func):
        self.buttons.append(self.font.render(text, True, btn_color))
        self.functions.append(func)
    def draw_menu(self, padding_y):
        for index, btn in enumerate(self.buttons):
            rect = pygame.Rect(self.window_rect.width//2-btn.get_width()//2, padding_y*(index+1), *btn.get_size())
            if index == self.select_btn_index:
                pygame.draw.rect(self.window, (173, 7, 32), pygame.Rect(rect.x-20, rect.y, rect.width+40, rect.height), 10, 10)
            self.window.blit(btn, rect)
    def select(self, direction):
        if self.select_btn_index == len(self.buttons)-1 and direction == 1:
            self.select_btn_index = 0
        elif self.select_btn_index == 0 and direction == -1:
            self.select_btn_index = len(self.buttons)-1
        else:
            self.select_btn_index += direction
    
    def do_func(self):
        self.functions[self.select_btn_index]()
        