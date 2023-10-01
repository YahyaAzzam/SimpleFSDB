# Import necessary modules
import uuid
import os
import json
import pathlib


# Define a Row class
class Row:
    def __init__(self, table, data):
        # Store the table and data associated with the row
        self.__table__ = table
        self.__data__ = data

        # Generate or retrieve the primary key for the row
        self.__data__[table.get_primary_key()] = self.__get_primary_key__()

        # Define the lock path for the row data
        self.__lock_path__ = os.path.join(self.__table__.get_lock_path(), "{}.json".format(self.get_primary_key()))

    # Get the data associated with the row
    def get_data(self):
        return self.__data__

    # Generate or retrieve the primary key for the row
    def __get_primary_key__(self):
        primary_key = self.__data__.get(self.__table__.get_primary_key()) if self.__data__.get(
            self.__table__.get_primary_key()) else str(uuid.uuid4().hex)
        return primary_key

    # Get the primary key of the row
    def get_primary_key(self):
        return self.__data__[self.__table__.get_primary_key()]

    # Get the path to the row data file
    def get_row_path(self):
        return os.path.join(self.__table__.get_data_path(), "{}.json".format(self.get_primary_key()))

    # Check if the row data file exists
    def row_exists(self):
        return os.path.exists(self.get_row_path())

    # Serialize the row by writing its data to a file
    def serialize(self):
        self.__lock__()
        with open(self.get_row_path(), 'w') as file:
            json.dump(self.__data__, file)
        self.__add_to_index__()
        self.__unlock__()

    # Add the row's data to associated indices
    def __add_to_index__(self):
        indices = self.__table__.get_indices()
        for index in indices:
            if index != self.__table__.get_primary_key() and index in self.__data__:
                indices[index].add_value(self.__data__[index], self.get_primary_key())

    # Delete the row's data from associated indices
    def __delete_index__(self):
        indices = self.__table__.get_indices()
        for index in indices:
            if index != self.__table__.get_primary_key() and index in self.__data__:
                indices[index].remove_value(self.__data__[index], self.get_primary_key())

    # Delete the row, including its data and associated index entries
    def delete(self):
        self.__check_lock__()
        self.__delete_index__()

    # Load a row by its primary key from the table
    @staticmethod
    def load_by_primary_key(table, primary_key):
        path = os.path.join(table.get_data_path(), "{}.json".format(primary_key))
        if not (path and os.path.isfile(path)):
            return None
        with open(path, 'r') as file:
            data = json.load(file)
        return Row(table, data)

    # Check if the row has a specified attribute
    def has_attribute(self, query):
        for attribute in query.items():
            if not self.__data__ or attribute[1] != self.__data__[attribute[0]]:
                return False
        return True

    # Lock the row to prevent concurrent access
    def __lock__(self):
        try:
            with open(self.__lock_path__, 'x'):
                pass
        except:
            self.__lock__()

    # Check if the row is locked; wait until it is unlocked
    def __check_lock__(self):
        while os.path.exists(self.__lock_path__):
            pass

    # Unlock the row
    def __unlock__(self):
        pathlib.Path(self.__lock_path__).unlink()
