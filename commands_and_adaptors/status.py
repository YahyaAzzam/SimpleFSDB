import enum


class Status(enum.Enum):
    Success = 0
    NoParameterError = 1
    WrongParameterError = 2
    NullPointerError = 3
