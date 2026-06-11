from models.file_system_tree import FileSystemTree


fs = FileSystemTree()

fs.mkdir("Documents")
fs.mkdir("Pictures")
fs.create_file("readme.txt", 10)

print("Path hiện tại:", fs.get_path())

print("\nDanh sách thư mục gốc:")
for item in fs.ls():
    print(item.name, "-", item.get_type(), "-", item.get_size())

fs.change_directory("Documents")
print("\nSau khi vào Documents:")
print("Path hiện tại:", fs.get_path())

fs.create_file("doc1.txt", 100)
fs.create_file("doc2.txt", 200)

print("\nDanh sách trong Documents:")
for item in fs.ls():
    print(item.name, "-", item.get_type(), "-", item.get_size())

result = fs.search("doc1.txt")
if result:
    print("\nTìm thấy:", result.name, "-", result.get_type())
else:
    print("\nKhông tìm thấy")

fs.change_directory("..")
print("\nSau khi quay lại thư mục cha:")
print("Path hiện tại:", fs.get_path())

deleted = fs.delete("readme.txt")
print("\nXóa readme.txt:", deleted)

print("\nDanh sách thư mục gốc sau khi xóa:")
for item in fs.ls():
    print(item.name, "-", item.get_type(), "-", item.get_size())

fs.change_directory("/")
print("\nVề thư mục gốc:")
print("Path hiện tại:", fs.get_path())

fs.create_file("a.txt", 100)
fs.mkdir("Folder1")
fs.create_file("Folder1", 100)
