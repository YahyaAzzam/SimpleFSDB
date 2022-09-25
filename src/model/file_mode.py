import enum


class FileMode(enum.Enum):
    x = "CantOverwrite"
    w = "CanOverwrite"
