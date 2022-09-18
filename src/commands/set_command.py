from commands.abstract_command import *
from model.database import *


class SetCommand(AbstractCommand):
    def __init__(self, database, table, value, overwrite = False):
        SetCommand.validate(str(database), str(table), value, overwrite)
        self.table = Database(Database.get_schema_data(str(database))).get_table(str(table))
        self.value = eval(str(value))
        SetCommand.validate_value(self.table, self.value, overwrite)
        self.overwrite = overwrite

    def execute(self):
        self.table.set(self.value, self.overwrite)

    @staticmethod
    def validate(database, table, value, overwrite):
        if len(database) == 0 or database == "None":
            raise NoParameterError("database parameter not entered")
        if len(table) == 0 or table == "None":
            raise NoParameterError("table parameter not entered")
        if value == None :
            raise NoParameterError("value parameter not entered")
        if not isinstance(overwrite, bool):
            raise WrongParameterError("overwrite should be boolean value")
        if not isinstance(value, dict):
            raise WrongParameterError("value should be json")

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
