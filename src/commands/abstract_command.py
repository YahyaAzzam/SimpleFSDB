from abc import abstractmethod


class AbstractCommand:
    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def execute(self):
        pass
