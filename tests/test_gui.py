import os
import sys
import subprocess
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


def test_character_tab_generate_runs_cli(monkeypatch):
    monkeypatch.setenv("QT_QPA_PLATFORM", "offscreen")
    calls = {}

    class DummyProcess:
        def __init__(self, *args, **kwargs):
            calls["cmd"] = args[0]
            self.stdout = ["ok"]
            self.returncode = 0

        def wait(self):
            pass

    monkeypatch.setattr(
        subprocess,
        "Popen",
        lambda *a, **kw: DummyProcess(*a, **kw),
    )

    app = QApplication.instance() or QApplication([])
    tab = CharacterTab()
    tab.generate_btn.click()
    assert "genloop_cli" in " ".join(calls["cmd"])
    tab.close()
    app.quit()


def test_style_sheet_load_save(tmp_path):
    from genloop_gui.style_sheet import StyleSheet

    path = tmp_path / "styles.json"
    sheet = StyleSheet(str(path))
    sheet.add("anime")
    sheet.save()
    sheet.styles = []
    sheet.load()
    assert sheet.styles == ["anime"]
