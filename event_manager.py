import pygame

pygame.init()


class Event_manager:
    def __init__(self, game_manager, win):
        self.manager = game_manager
        self.win = win

    def check_collision(self, direction, obj):
        for o in self.manager.current_room.object_list:
            o.collision(direction, obj, self.manager)
        for i in self.manager.current_room.item_list:
            if i.collision(obj):
                self.manager.current_room.item_list.remove(i)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.QUIT

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.manager.player.move_left()
            self.check_collision(0, self.manager.player)
        if keys[pygame.K_RIGHT]:
            self.manager.player.move_right(self.win)
            self.check_collision(1, self.manager.player)
        if keys[pygame.K_UP]:
            self.manager.player.move_up()
            self.check_collision(2, self.manager.player)
        if keys[pygame.K_DOWN]:
            self.manager.player.move_down(self.win)
            self.check_collision(3, self.manager.player)

        if self.manager.player.hp <= 0:
            return pygame.QUIT
        if self.manager.player.damage_delay > 0:
            self.manager.player.damage_delay -= 1

        # go over all the objects and event them
        for e in self.manager.current_room.entity_list:
            e.event()
        for o in self.manager.current_room.object_list:
            o.event()
        for i in self.manager.current_room.item_list:
            i.event()
