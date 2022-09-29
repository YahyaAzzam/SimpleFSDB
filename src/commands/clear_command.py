import sys
import os
sys.path.append(os.path.dirname(__file__).replace("commands", ''))
from commands.abstract_command import *
from model.database import *


class ClearCommand(AbstractCommand):
    def __init__(self, database_name):
        ClearCommand.validate(database_name)
        self.database_name = database_name

    def execute(self):
        database = Database(database_name = self.database_name)
        database.clear()

    @staticmethod
    def validate(database_name):
        if database_name == None or len(database_name) == 0:
            raise NoParameterError("database_name parameter not entered")
