from abc import ABC


class Keys(ABC):
    TABLES = "Tables"
    DATABASE = "database_name"
    NAME = "name"
    COLUMNS = "columns"
    PRIMARY_KEY = "primary_key"
    INDEX_KEYS = "index_keys"
    OVERWRITE = "overwrite"
    CONSISTENCY = "Consistency"
