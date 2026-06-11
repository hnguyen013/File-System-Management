from models.file_node import FileNode
from models.folder_node import FolderNode


class FileSystemTree:
    def __init__(self):
        self.root = FolderNode("/")
        self.current_working_dir = self.root

    def mkdir(self, name):
        folder = FolderNode(name)
        self.current_working_dir.add_child(folder)

    def create_file(self, name, size):
        file = FileNode(name, size)
        self.current_working_dir.add_child(file)

    def ls(self):
        return self.current_working_dir.children

    def search(self, name, node=None):
        if node is None:
            node = self.root

        if node.name == name:
            return node

        if isinstance(node, FolderNode):
            for child in node.children:
                result = self.search(name, child)
                if result:
                    return result

        return None