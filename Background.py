from os import name

from Const import WINDOW_WIDTH, ENTITY_SPEED
from Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)


    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WINDOW_WIDTH