import pygame


class Display_manager:
    def __init__(self, game_manger, win):
        self.win = win
        self.manager = game_manger

    def display_game(self):
        self.win.fill((0, 0, 0))
        for obj in self.manager.current_room.object_list:
            obj.draw(self.win)
        for obj in self.manager.current_room.item_list:
            obj.draw(self.win)
        for obj in self.manager.current_room.entity_list:
            obj.draw(self.win)
        pygame.display.update()
