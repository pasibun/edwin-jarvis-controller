import os
from ctypes import CDLL

from Domain.control_board_types import ControlBoardTypes


class TouchKeypadService(object):
    file_dir = os.path.dirname(__file__)
    filename = os.path.join(file_dir, '../resources/TTP229.so')
    tp = CDLL(os.path.abspath(os.path.realpath(filename)))

    def get_key_press(self):
        val = self.tp.TTP229_GetVal()
        if val & 1:
            print("O")
            return ControlBoardTypes.DEFAULT
        elif val & 2:
            print("X")
            return ControlBoardTypes.DEFAULT
        elif val & 4:
            print("E")
            return ControlBoardTypes.DEFAULT
        elif val & 8:
            print("R")
            return ControlBoardTypes.DEFAULT
        elif val & 16:
            return ControlBoardTypes.HOME
        elif val & 32:
            print("+")
            return ControlBoardTypes.HEXAPOD
        elif val & 64:
            print("-")
            return ControlBoardTypes.ROBOTARM
        elif val & 128:
            print("L")
            return ControlBoardTypes.DEFAULT
        elif val & 256:
            return ControlBoardTypes.DOWN
        elif val & 512:
            return ControlBoardTypes.RIGHT
        elif val & 1024:
            return ControlBoardTypes.UP
        elif val & 2048:
            return ControlBoardTypes.LEFT
        elif val & 4096:
            print("Power")
            return ControlBoardTypes.DEFAULT
        elif val & 8192:
            print("RP")
            return ControlBoardTypes.DEFAULT
        elif val & 16384:
            print("WS")
            return ControlBoardTypes.DEFAULT
        elif val & 32768:
            print("Y")
            return ControlBoardTypes.DEFAULT
        else:
            return None
