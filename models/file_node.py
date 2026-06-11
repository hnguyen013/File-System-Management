from models.node import Node


class FileNode(Node):
    def __init__(self, name, size):
        super().__init__(name, is_folder=False, size=size)

    def get_size(self):
        return self.size

    def get_type(self):
        return "File"