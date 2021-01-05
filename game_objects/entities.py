import pygame

from .main_classes import Game_object


class Player(Game_object):
    max_damage_delay = 0

    def __init__(self):
        self.max_hp = 20
        Game_object.__init__(self, 250, 250, 40, 40)
        self.speed = 6
        self.hp = 20
        self.damage_delay = 0
        self.font = pygame.font.SysFont('comicsans', 25)

    def move_left(self):
        self.x -= self.speed
        if self.x <= 0:
            self.x = 0

    def move_right(self, win):
        self.x += self.speed
        if self.x > win.get_width() - self.width:
            self.x = win.get_width() - self.width

    def move_up(self):
        self.y -= self.speed
        if self.y <= 0:
            self.y = 0

    def move_down(self, win):
        self.y += self.speed
        if self.y > win.get_height() - self.height:
            self.y = win.get_height() - self.height

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))
        hp_text = self.font.render(f"hp = {self.hp}", True, (255, 255, 255))
        win.blit(hp_text, (0, 0))
        speed_text = self.font.render(f"speed = {self.speed}", True, (255, 255, 255))
        win.blit(speed_text, (hp_text.get_width() + 10, 0))
