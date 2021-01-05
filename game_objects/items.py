from .main_classes import Item


class Redbull(Item):
    def __init__(self, x, y):
        Item.__init__(self, x, y, 7, 20, (255, 0, 0), "red bull")

    def effect(self, obj):
        obj.speed += 1


class Healing_potion(Item):
    def __init__(self, x, y):
        Item.__init__(self, x, y, 7, 20, (161, 0, 185), "healing musk")

    def effect(self, obj):
        if not obj.max_hp < obj.hp + 3:
            obj.hp += 3
