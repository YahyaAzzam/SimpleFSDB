import os
from abc import ABC


class Keys(ABC):
    TABLES = "Tables"
    DATABASE = "database_name"
    NAME = "name"
    COLUMNS = "columns"
    PRIMARY_KEY = "primary_key"
    INDEX_KEYS = "Index_keys"
    CONSISTENCY = "consistency"
    SCHEMA_PATH = str(os.getcwd()).replace("\\CommandsAndAdaptors", '')
