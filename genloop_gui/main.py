import os
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QWidget,
    QListWidget,
    QVBoxLayout,
    QPushButton,
    QListWidgetItem,
    QTextEdit,
)
from PySide6.QtCore import Qt
from .style_sheet import StyleSheetTab
import subprocess
import sys


class ResultsWidget(QWidget):
    """List files from the output directory."""

    def __init__(self, output_dir: str = "outputs") -> None:
        super().__init__()
        self.output_dir = output_dir
        self.list = QListWidget()
        self.refresh_btn = QPushButton("Refresh")
        self.refresh_btn.clicked.connect(self.refresh)
        layout = QVBoxLayout()
        layout.addWidget(self.list)
        layout.addWidget(self.refresh_btn)
        self.setLayout(layout)
        self.refresh()

    def refresh(self) -> None:
        self.list.clear()
        if os.path.isdir(self.output_dir):
            for name in sorted(os.listdir(self.output_dir)):
                if name.endswith(".png"):
                    self.list.addItem(name)


class CharacterTab(QWidget):
    """Manage character slots."""

    def __init__(self) -> None:
        super().__init__()
        self.list = QListWidget()
        self.add_btn = QPushButton("Add Slot")
        self.remove_btn = QPushButton("Remove Slot")
        self.generate_btn = QPushButton("Generate")
        self.output_view = QTextEdit()
        self.output_view.setReadOnly(True)
        self.add_btn.clicked.connect(self.add_slot)
        self.remove_btn.clicked.connect(self.remove_slot)
        self.generate_btn.clicked.connect(self.generate)
        layout = QVBoxLayout()
        layout.addWidget(self.list)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.remove_btn)
        layout.addWidget(self.generate_btn)
        layout.addWidget(self.output_view)
        self.setLayout(layout)

    def add_slot(self) -> None:
        num = self.list.count() + 1
        item = QListWidgetItem(f"Slot {num}")
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.list.addItem(item)

    def remove_slot(self) -> None:
        for item in self.list.selectedItems():
            self.list.takeItem(self.list.row(item))

    def generate(self) -> None:
        """Run the CLI character generation command."""
        cmd = [sys.executable, "-m", "genloop_cli", "generate", "characters"]
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        assert process.stdout is not None
        self.output_view.clear()
        for line in process.stdout:
            self.output_view.append(line.rstrip())
        process.wait()

class MainWindow(QMainWindow):
    """Main window with tab widget."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("GenLoop")
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        tab_defs = [
            ("Characters", CharacterTab()),
            ("Items", QWidget()),
            ("Environments", QWidget()),
            ("Brainstorm", QWidget()),
            ("Style Sheet", StyleSheetTab()),
            ("Results", ResultsWidget()),
        ]
        for name, widget in tab_defs:
            self.tabs.addTab(widget, name)

def main():
    app = QApplication.instance() or QApplication([])
    win = MainWindow()
    win.show()
    app.exec()

if __name__ == "__main__":
    main()
