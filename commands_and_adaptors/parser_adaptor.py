from iadaptor import IInputAdaptor


class ParsedInput(IInputAdaptor):
    def __init__(self, parser):
        self.command = str(parser.command).lower()
        self.schema = parser.schema
        self.database = parser.database
        self.table = parser.table
        self.primary_key = parser.primary_key
        self.parameter = parser.parameter
        self.value = parser.value
