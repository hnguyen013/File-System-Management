from abc import ABC, abstractmethod


class Node(ABC):
    def __init__(self, name, is_folder, size=0):
        self.name = name
        self.is_folder = is_folder
        self.size = size
        self.parent = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self.__name = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("Size cannot be negative")
        self.__size = value

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def get_type(self):
        pass