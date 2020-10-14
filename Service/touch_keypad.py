from ctypes import *
import time
import os.path

from Domain.control_board_types_enum import ControlBoardTypes


class ControlBoard(object):
    file_dir =os.path.dirname(__file__)
    filename = os.path.join(file_dir, '../resources/TTP229.so')
    tp = CDLL(os.path.abspath(os.path.realpath(filename)))

    def keypad_input(self):
        val = self.tp.TTP229_GetVal()
        time.sleep(0.5)
        if val & 1:
            return"O"
        elif val & 2:
            return"X"
        elif val & 4:
            return "E"
        elif val & 8:
            return "R"
        elif val & 16:
            return ControlBoardTypes.HOME
        elif val & 32:
            return "+"
        elif val & 64:
            return "-"
        elif val & 128:
            return "L"
        elif val & 256:
            return ControlBoardTypes.DOWN
        elif val & 512:
            return ControlBoardTypes.RIGHT
        elif val & 1024:
            return ControlBoardTypes.UP
        elif val & 2048:
            return ControlBoardTypes.LEFT
        elif val & 4096:
            return "Power"
        elif val & 8192:
            return "RP"
        elif val & 16384:
            return "WS"
        elif val & 32768:
            return "Y"
