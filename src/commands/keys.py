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
    SCHEMA_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", ''), 'tests')
    DATABASE_PATH = os.path.join(str(os.getcwd()).replace("commands", '').replace("src", '').replace("tests", '').replace("/SimpleFSDB", '').replace("\\SimpleFSDB", ''), 'SimpleFSDB', 'tests')
