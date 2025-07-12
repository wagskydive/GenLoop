import os
import sys
from genloop_gui import MainWindow
from genloop_gui.main import ResultsWidget, CharacterTab
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


def test_results_widget_lists_pngs(tmp_path, monkeypatch):
    monkeypatch.setenv("QT_QPA_PLATFORM", "offscreen")
    (tmp_path / "a.png").write_bytes(b"1")
    (tmp_path / "b.png").write_bytes(b"2")
    app = QApplication.instance() or QApplication([])
    w = ResultsWidget(output_dir=tmp_path)
    items = [w.list.item(i).text() for i in range(w.list.count())]
    assert items == ["a.png", "b.png"]
    w.close()
    app.quit()


def test_character_tab_add_remove(monkeypatch):
    monkeypatch.setenv("QT_QPA_PLATFORM", "offscreen")
    app = QApplication.instance() or QApplication([])
    tab = CharacterTab()
    tab.add_slot()
    tab.add_slot()
    assert tab.list.count() == 2
    tab.list.setCurrentRow(0)
    tab.remove_slot()
    assert tab.list.count() == 1
    tab.close()
    app.quit()
