from abc import abstractmethod


class AbstractCommand:
    @abstractmethod
    def execute(self):
        pass

    @staticmethod
    def validate(self):
        pass
