from models.file_system_tree import FileSystemTree


class FileSystemService:
    def __init__(self):
        self.fs = FileSystemTree()

    def get_current_path(self):
        return self.fs.pwd()

    def list_items(self):
        return self.fs.ls()

    def create_folder(self, name):
        self.fs.mkdir(name)

    def create_file(self, name, size):
        self.fs.create_file(name, size)

    def delete_item(self, name):
        return self.fs.delete(name)

    def search_item(self, name):
        return self.fs.search(name)

    def change_directory(self, name):
        return self.fs.change_directory(name)

    def go_back(self):
        return self.fs.change_directory("..")

    def go_root(self):
        return self.fs.change_directory("/")