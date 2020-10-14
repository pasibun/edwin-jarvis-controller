from enum import Enum


class ControlBoardTypes(Enum):
    def __str__(self):
        return str(self.value)

    HOME = "Home",
    LEFT = "Left",
    RIGHT = "Right",
    UP = "Up",
    DOWN = "Down",
    DEFAULT = "DEFAULT"
