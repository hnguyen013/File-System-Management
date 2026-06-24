from models.file_node import FileNode
from models.folder_node import FolderNode


class FileSystemTree:
    def __init__(self):
        self.root = FolderNode("/")
        self.current_working_dir = self.root

    def mkdir(self, name):
        for child in self.current_working_dir.children:
            if child.name == name:
                raise ValueError("Folder already exists")

        folder = FolderNode(name)
        self.current_working_dir.add_child(folder)

    def create_file(self, name, size):
        if any(child.name == name for child in self.current_working_dir.children):
            raise ValueError("File already exists")

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

    def delete(self, name):
        node = self.search(name)

        if node is None:
            return False

        if node == self.root:
            return False

        parent = node.parent
        parent.remove_child(node)
        return True

    def change_directory(self, name):
        if name == "/":
            self.current_working_dir = self.root
            return True

        if name == "..":
            if self.current_working_dir.parent is not None:
                self.current_working_dir = self.current_working_dir.parent
            return True

        for child in self.current_working_dir.children:
            if child.name == name and isinstance(child, FolderNode):
                self.current_working_dir = child
                return True

        return False

    def get_path(self):
        if self.current_working_dir == self.root:
            return "/"

        path = []
        current = self.current_working_dir

        while current != self.root:
            path.append(current.name)
            current = current.parent

        path.reverse()
        return "/" + "/".join(path)

    def pwd(self):
        return self.get_path()
