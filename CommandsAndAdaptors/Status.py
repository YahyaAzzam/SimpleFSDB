import enum


class status(enum.Enum):
    Success = 0
    NoCommand = 1
    WrongCommand = 2
    NoSchema = 3
    WrongSchema = 4
    NoDatabase = 5
    WrongDatabase = 6
    NoTable = 7
    WrongTable = 8
    NoPrimaryKey = 9
    WrongPrimaryKey = 10
    NoParameter = 11
    WrongParameter = 12
    NoValue = 13
    WrongValue = 14
