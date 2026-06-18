from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QListWidget,
    QMessageBox,
    QInputDialog,
)

from models.file_system_tree import FileSystemTree
from models.folder_node import FolderNode


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.fs = FileSystemTree()

        self.setWindowTitle("File System Management")
        self.setGeometry(200, 100, 800, 500)

        self.init_ui()
        self.refresh_view()

    def init_ui(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        self.path_label = QLabel()
        main_layout.addWidget(self.path_label)

        self.list_widget = QListWidget()
        main_layout.addWidget(self.list_widget)

        button_layout = QHBoxLayout()

        self.btn_new_folder = QPushButton("New Folder")
        self.btn_new_file = QPushButton("New File")
        self.btn_delete = QPushButton("Delete")
        self.btn_back = QPushButton("Back")
        self.btn_search = QPushButton("Search")
        self.btn_refresh = QPushButton("Refresh")

        button_layout.addWidget(self.btn_new_folder)
        button_layout.addWidget(self.btn_new_file)
        button_layout.addWidget(self.btn_delete)
        button_layout.addWidget(self.btn_back)
        button_layout.addWidget(self.btn_search)
        button_layout.addWidget(self.btn_refresh)

        main_layout.addLayout(button_layout)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.btn_new_folder.clicked.connect(self.add_folder)
        self.btn_new_file.clicked.connect(self.add_file)
        self.btn_delete.clicked.connect(self.delete_item)
        self.btn_back.clicked.connect(self.go_back)
        self.btn_search.clicked.connect(self.search_item)
        self.btn_refresh.clicked.connect(self.refresh_view)

    def refresh_view(self):
        self.path_label.setText("Current Path: " + self.fs.pwd())

        self.list_widget.clear()

        for child in self.fs.ls():
            item_type = child.get_type()
            size = child.get_size()
            self.list_widget.addItem(f"{child.name} - {item_type} - {size}")

    def add_folder(self):
        name, ok = QInputDialog.getText(self, "New Folder", "Folder name:")

        if ok and name:
            try:
                self.fs.mkdir(name)
                self.refresh_view()
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))

    def add_file(self):
        name, ok = QInputDialog.getText(self, "New File", "File name:")

        if ok and name:
            size, ok_size = QInputDialog.getInt(self, "File Size", "Size:", 0, 0)

            if ok_size:
                try:
                    self.fs.create_file(name, size)
                    self.refresh_view()
                except ValueError as e:
                    QMessageBox.warning(self, "Error", str(e))

    def delete_item(self):
        selected = self.list_widget.currentItem()

        if selected is None:
            QMessageBox.warning(self, "Error", "Please select an item")
            return

        name = selected.text().split(" - ")[0]

        result = self.fs.delete(name)

        if result:
            self.refresh_view()
        else:
            QMessageBox.warning(self, "Error", "Cannot delete item")

    def go_back(self):
        self.fs.change_directory("..")
        self.refresh_view()

    def search_item(self):
        name, ok = QInputDialog.getText(self, "Search", "Enter name:")

        if ok and name:
            result = self.fs.search(name)

            if result:
                QMessageBox.information(
                    self, "Found", f"Found: {result.name} - {result.get_type()}"
                )
            else:
                QMessageBox.warning(self, "Not Found", "Item not found")
