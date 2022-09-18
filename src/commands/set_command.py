from commands.abstract_command import *
from model.database import *


class SetCommand(AbstractCommand):
    def __init__(self, database, table, value, overwrite = False):
        self.validate(database, table, value)
        self.table = Database(Database.get_schema_data(database)).get_table(table)
        self.value = eval(value)
        self.validate_value(self.table, self.value, overwrite)
        self.overwrite = overwrite

    def execute(self):
        self.table.set(self.value, self.overwrite)

    @staticmethod
    def validate(database, table, value):
        if database is None or len(database) == 0:
            raise NoParameterError("database parameter not entered")
        if table is None or len(table) == 0:
            raise NoParameterError("table parameter not entered")
        if value is None or len(value) == 0:
            raise NoParameterError("value parameter not entered")

    @staticmethod
    def validate_value(table, value, overwrite):
        table_meta_data = TableMetaData(table)
        primary_key = table_meta_data.primary_key
        if primary_key not in value:
             raise WrongParameterError("primary_key is missing")
        table_columns = table_meta_data.columns
        for input in value:
            if input not in table_columns:
                raise WrongParameterError("Wrong value")
        path = os.path.join(table.get_path(), "{}.json".format(value[primary_key]))
        if os.path.exists(path) and not overwrite:
                raise WrongParameterError("Can't set this file")
