from enum import Enum


class ApplicationTypes(Enum):
    HEXAPOD = 0,
    ROBOTARM = 1,

    @classmethod
    def _missing_(cls, value):
        print("Not found! ", value)
        return ApplicationTypes.HEXAPOD
