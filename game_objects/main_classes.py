import pygame

pygame.init()


class Game_object:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def event(self):
        pass


class Item(Game_object):
    def __init__(self, x, y, width, height, color, name):
        Game_object.__init__(self, x, y, width, height)
        self.color = color
        self.text = pygame.font.SysFont('comicsans', 20).render(name, True, (255, 255, 255))

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        win.blit(self.text, (self.x - self.text.get_width() // 2, self.y - self.text.get_height()))

    def collision(self, obj):
        if self.x + self.width > obj.x and self.x < obj.x + obj.width:
            if self.y + self.height > obj.y and self.y < obj.y + obj.height:
                self.effect(obj)
                return True
            return False
        return False


class Wall(Game_object):
    def __init__(self, x, y, width, height, color):
        Game_object.__init__(self, x, y, width, height)
        self.color = color

    def collision_checker(self, obj):
        if self.x + self.width > obj.x and self.x < obj.x + obj.width:
            return self.y + self.height > obj.y and self.y < obj.y + obj.height

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))


class Room:
    def __init__(self, object_list=[], item_list=[], entity_list=[]):
        self.object_list = object_list
        self.item_list = item_list
        self.entity_list = entity_list
