from models.node import Node


class FolderNode(Node):
    def __init__(self, name):
        super().__init__(name, is_folder=True, size=0)
        self.children = []

    def add_child(self, node):
        node.parent = self
        self.children.append(node)

    def remove_child(self, node):
        self.children.remove(node)
        node.parent = None

    def get_size(self):
        total = 0
        for child in self.children:
            total += child.get_size()
        return total

    def get_type(self):
        return "Folder"
