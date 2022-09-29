import sys
import os
sys.path.append(os.path.dirname(__file__).replace("model", ''))
from model.index import *


class PrimaryKeyIndex(Index):
    def __init__(self, primary_key_name, table_metadata):
        super().__init__(primary_key_name, table_metadata)

    def serialize(self):
        pass

    def add_value(self):
        pass

    def __update_value__(self, value_name, primary_keys):
        pass

    def remove_value(self):
        pass
