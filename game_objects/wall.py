from .main_classes import Wall


class Border(Wall):
    def __init__(self, x, y, width, height, color=(0, 0, 255)):
        Wall.__init__(self, x, y, width, height, color)

    def collision_left(self, obj):
        if self.collision_checker(obj):
            obj.x = self.x + self.width

    def collision_right(self, obj):
        if self.collision_checker(obj):
            obj.x = self.x - obj.width

    def collision_up(self, obj):
        if self.collision_checker(obj):
            obj.y = self.y + self.height

    def collision_down(self, obj):
        if self.collision_checker(obj):
            obj.y = self.y - obj.height

    def collision(self, direction, obj, manager):
        if direction == 0:
            self.collision_left(obj)
        elif direction == 1:
            self.collision_right(obj)
        elif direction == 2:
            self.collision_up(obj)
        elif direction == 3:
            self.collision_down(obj)


class Door(Wall):
    def __init__(self, room, direction, win_width, win_height):
        self.direction = direction
        self.room = room
        self.win_width = win_width
        self.win_height = win_height
        if direction == 0:
            width = 20
            height = 60
            x = 0
            y = win_height // 2 - height // 2
        elif direction == 1:
            width = 20
            height = 60
            x = win_width - width
            y = win_height // 2 - height // 2
        elif direction == 2:
            width = 60
            height = 20
            x = win_width // 2 - width // 2
            y = 0
        elif direction == 3:
            width = 60
            height = 20
            x = win_width // 2 - width // 2
            y = win_height - height
        Wall.__init__(self, x, y, width, height, (0, 255, 0))

    def collision(self, direction, obj, manager):
        if self.collision_checker(obj):
            manager.current_room.entity_list.remove(obj)
            self.room.entity_list.append(obj)
            manager.current_room = self.room
            if self.direction == 0:
                obj.x = self.win_width - self.width - obj.width
                obj.y = self.win_height // 2
            if self.direction == 1:
                obj.x = self.width
                obj.y = self.win_height // 2
            if self.direction == 2:
                obj.y = self.win_height - self.height - obj.height
                obj.x = self.win_width // 2
            if self.direction == 3:
                obj.y = self.height
                obj.x = self.win_width // 2


class Spike(Wall):
    def __init__(self, x, y, width, height):
        Wall.__init__(self, x, y, width, height, (161, 0, 0))
        self.collision_list = []

    def collision(self, direction, obj, manager):
        if self.collision_checker(obj):
            if not obj in self.collision_list:
                self.collision_list.append(obj)
        else:
            if obj in self.collision_list:
                self.collision_list.remove(obj)

    def event(self):
        for obj in self.collision_list:
            if obj.damage_delay == 0:
                obj.hp -= 0.5
                obj.damage_delay += 10
