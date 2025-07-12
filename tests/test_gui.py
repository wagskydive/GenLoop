import os
import sys
from genloop_gui import MainWindow
from PySide6.QtWidgets import QApplication


def test_main_window_tabs(monkeypatch):
    monkeypatch.setenv("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    win = MainWindow()
    tabs = [win.tabs.tabText(i) for i in range(win.tabs.count())]
    expected = [
        "Characters",
        "Items",
        "Environments",
        "Brainstorm",
        "Style Sheet",
        "Results",
    ]
    assert tabs == expected
    win.close()
    app.quit()
