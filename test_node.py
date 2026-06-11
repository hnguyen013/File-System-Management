from models.file_node import FileNode
from models.folder_node import FolderNode


# Test tạo file
file1 = FileNode("a.txt", 100)
file2 = FileNode("b.txt", 200)

print("File 1:", file1.name, file1.get_type(), file1.get_size())
print("File 2:", file2.name, file2.get_type(), file2.get_size())


# Test tạo folder
folder = FolderNode("Documents")

folder.add_child(file1)
folder.add_child(file2)

print("\nFolder:", folder.name, folder.get_type())
print("Số lượng file trong folder:", len(folder.children))
print("Size folder:", folder.get_size())


# Test parent
print("\nParent của file1:", file1.parent.name)
print("Parent của file2:", file2.parent.name)


# Test remove child
folder.remove_child(file1)

print("\nSau khi xóa file1 khỏi folder:")
print("Số lượng file trong folder:", len(folder.children))
print("Size folder:", folder.get_size())
print("Parent của file1:", file1.parent)