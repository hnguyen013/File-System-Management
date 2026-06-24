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

from services.file_system_service import FileSystemService


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.file_service = FileSystemService()

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
        self.btn_open = QPushButton("Open Folder")
        self.btn_root = QPushButton("Go Root")

        button_layout.addWidget(self.btn_new_folder)
        button_layout.addWidget(self.btn_new_file)
        button_layout.addWidget(self.btn_delete)
        button_layout.addWidget(self.btn_back)
        button_layout.addWidget(self.btn_search)
        button_layout.addWidget(self.btn_refresh)
        button_layout.addWidget(self.btn_open)
        button_layout.addWidget(self.btn_root)

        main_layout.addLayout(button_layout)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.btn_new_folder.clicked.connect(self.add_folder)
        self.btn_new_file.clicked.connect(self.add_file)
        self.btn_delete.clicked.connect(self.delete_item)
        self.btn_back.clicked.connect(self.go_back)
        self.btn_search.clicked.connect(self.search_item)
        self.btn_refresh.clicked.connect(self.refresh_view)
        self.btn_open.clicked.connect(self.open_folder)
        self.btn_root.clicked.connect(self.go_root)
        self.list_widget.itemDoubleClicked.connect(self.open_folder)

    def refresh_view(self):
        self.path_label.setText("Current Path: " + self.file_service.get_current_path())

        self.list_widget.clear()

        for child in self.file_service.list_items():
            item_type = child.get_type()
            size = child.get_size()
            self.list_widget.addItem(f"{child.name} - {item_type} - {size}")

    def add_folder(self):
        name, ok = QInputDialog.getText(self, "New Folder", "Folder name:")

        if ok and name:
            try:
                self.file_service.create_folder(name)
                self.refresh_view()
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))

    def add_file(self):
        name, ok = QInputDialog.getText(self, "New File", "File name:")

        if ok and name:
            size, ok_size = QInputDialog.getInt(self, "File Size", "Size:", 0, 0)

            if ok_size:
                try:
                    self.file_service.create_file(name, size)
                    self.refresh_view()
                except ValueError as e:
                    QMessageBox.warning(self, "Error", str(e))

    def delete_item(self):
        selected = self.list_widget.currentItem()

        if selected is None:
            QMessageBox.warning(self, "Error", "Please select an item")
            return

        name = selected.text().split(" - ")[0]

        result = self.file_service.delete_item(name)

        if result:
            self.refresh_view()
        else:
            QMessageBox.warning(self, "Error", "Cannot delete item")

    def go_back(self):
        self.file_service.go_back()
        self.refresh_view()

    def search_item(self):
        name, ok = QInputDialog.getText(self, "Search", "Enter name:")

        if ok and name:
            result = self.file_service.search_item(name)

            if result:
                QMessageBox.information(
                    self, "Found", f"Found: {result.name} - {result.get_type()} - {result.get_size()}"
                )
            else:
                QMessageBox.warning(self, "Not Found", "Item not found")
    def open_folder(self):
        selected = self.list_widget.currentItem()

        if selected is None:
            QMessageBox.warning(self, "Error", "Please select a folder")
            return

        text = selected.text()
        name = text.split(" - ")[0]
        item_type = text.split(" - ")[1]

        if item_type != "Folder":
            QMessageBox.warning(self, "Error", "Please select a folder, not a file")
            return

        result = self.file_service.change_directory(name)

        if result:
            self.refresh_view()
        else:
            QMessageBox.warning(self, "Error", "Cannot open folder")
    def go_root(self):
        self.file_service.go_root()
        self.refresh_view()
