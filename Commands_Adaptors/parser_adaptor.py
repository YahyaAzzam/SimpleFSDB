class parsed_input:
    def __init__(self, args):
        self.command = args.command.lower()
        self.schema = args.schema
        self.database = args.database
        self.table = args.table
        self.primary_key = args.primary_key
        self.parameter = args.parameter
        self.value = args.value

    def parse(self):
        a = [self.command, self.schema, self.database, self.table, self.primary_key, self.parameter, self.value]
        return a
