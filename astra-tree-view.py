import os
import sys

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QTreeView, QFileSystemModel, QApplication, QWidget, QVBoxLayout, QMainWindow, QLineEdit


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sysmodel = QFileSystemModel()
        self.treeview = QTreeView()
        self.treeview.setModel(self.sysmodel)

        self.sysmodel.setRootPath(QDir.rootPath())
        self.treeview.setRootIndex(self.sysmodel.index("/home/" + os.getlogin()))
        self.sysmodel.setFilter(
            QDir.Dirs | QDir.Files | QDir.Hidden | QDir.NoDotAndDotDot)

        self.filterEdit = QLineEdit(self)
        self.filterEdit.textChanged.connect(self.eventFilter)

        main_window = QWidget()
        layout = QVBoxLayout(main_window)
        layout.addWidget(self.filterEdit)
        layout.addWidget(self.treeview)
        self.setCentralWidget(main_window)

    def eventFilter(self, filter_text):
        self.sysmodel.setNameFilters([f"*{filter_text}*"])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
