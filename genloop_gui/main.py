import os
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget,
    QWidget,
    QListWidget,
    QVBoxLayout,
    QPushButton,
)


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

class MainWindow(QMainWindow):
    """Main window with tab widget."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("GenLoop")
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        tab_defs = [
            ("Characters", QWidget()),
            ("Items", QWidget()),
            ("Environments", QWidget()),
            ("Brainstorm", QWidget()),
            ("Style Sheet", QWidget()),
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
