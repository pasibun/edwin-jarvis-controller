from enum import Enum


class ControlBoardTypes(Enum):
    HOME = 0,
    LEFT = 1,
    RIGHT = 2,
    UP = 3,
    DOWN = 4,
    DEFAULT = 5,
    DONE = 9,
    HEXAPOD = 7,
    ROBOTARM = 8

    @classmethod
    def _missing_(cls, value):
        print("Not found! ", value)
        return ControlBoardTypes.DEFAULT
