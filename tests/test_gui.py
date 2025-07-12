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


def test_character_tab_add_remove(monkeypatch, tmp_path):
    monkeypatch.setenv("QT_QPA_PLATFORM", "offscreen")
    import importlib
    gm = importlib.import_module("genloop_gui.main")
    from genloop_gui import slot_memory
    monkeypatch.setattr(gm, "SlotMemory", lambda: slot_memory.SlotMemory(path=str(tmp_path/"slots.json")))
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

def test_slot_memory_load_save(tmp_path):
    from genloop_gui.slot_memory import SlotMemory

    path = tmp_path / "slots.json"
    mem = SlotMemory(str(path))
    mem.lock_style("hero", "anime")
    mem.save()
    mem.slots = {}
    mem.load()
    assert mem.slots == {"hero": "anime"}


def test_character_tab_slot_memory(monkeypatch, tmp_path):
    monkeypatch.setenv("QT_QPA_PLATFORM", "offscreen")
    from genloop_gui import slot_memory
    import importlib
    gm = importlib.import_module("genloop_gui.main")
    def _factory():
        return slot_memory.SlotMemory(str(tmp_path / "slots.json"))
    monkeypatch.setattr(gm, "SlotMemory", lambda: _factory())
    monkeypatch.setattr(gm.QInputDialog, "getText", lambda *a, **kw: ("anime", True))
    app = QApplication.instance() or QApplication([])
    tab = CharacterTab()
    tab.add_slot()
    tab.list.setCurrentRow(0)
    tab.lock_style()
    tab.close()
    app.quit()
    mem = slot_memory.SlotMemory(str(tmp_path / "slots.json"))
    mem.load()
    assert mem.slots == {"Slot 1": "anime"}
