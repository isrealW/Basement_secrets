import pygame

from display_manager import Display_manager
from event_manager import Event_manager
from game_objects.entities import *
from game_objects.items import *
from game_objects.main_classes import Room
from game_objects.wall import *


def link_rooms(room1, room2, width, height):
    room1.object_list.append(Door(room2, 0, width, height))
    room2.object_list.append(Door(room1, 1, width, height))
    return room1


def link_rooms2(room1, room2, width, height):
    room1.object_list.append(Door(room2, 2, width, height))
    room2.object_list.append(Door(room1, 3, width, height))
    return room1


class Game_manager:
    def __init__(self):
        width, height = 800, 600
        self.win = pygame.display.set_mode((width, height))
        self.player = Player()
        self.clock = pygame.time.Clock()
        # map
        room1 = Room([Border(100, 100, 100, 30)], [Redbull(300, 400), Healing_potion(400, 400)], [self.player])
        room2 = Room([Border(100, 100, 200, 30), Border(100, 200, 200, 30), Spike(100, 300, 300, 30)])
        room3 = Room([Border(100, 200, 200, 30), Border(100, 300, 200, 30)])
        link_rooms(room1, room2, width, height)
        link_rooms2(room2, room3, width, height)

        self.current_room = room1
        self.event_manager = Event_manager(self, self.win)
        self.display_manager = Display_manager(self, self.win)

    def event(self):
        return self.event_manager.event()

    def display(self):
        self.display_manager.display_game()


if __name__ == "__main__":
    game_manager = Game_manager()
    run = True
    while run:
        game_manager.clock.tick(60)
        if game_manager.event() == pygame.QUIT:
            run = False
        game_manager.display()
