from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget

class MainWindow(QMainWindow):
    """Main window with tab widget."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("GenLoop")
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        for name in [
            "Characters",
            "Items",
            "Environments",
            "Brainstorm",
            "Style Sheet",
            "Results",
        ]:
            self.tabs.addTab(QWidget(), name)

def main():
    app = QApplication.instance() or QApplication([])
    win = MainWindow()
    win.show()
    app.exec()

if __name__ == "__main__":
    main()
