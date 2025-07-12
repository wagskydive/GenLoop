"""Manage style tags saved in a JSON file."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import List
from PySide6.QtWidgets import QWidget, QListWidget, QPushButton, QVBoxLayout, QListWidgetItem
from PySide6.QtCore import Qt


@dataclass
class StyleSheet:
    path: str = "styles.json"
    styles: List[str] = field(default_factory=list)

    def load(self) -> List[str]:
        """Load styles from ``path`` if it exists."""
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                self.styles = json.load(f)
        except FileNotFoundError:
            self.styles = []
        return self.styles

    def save(self) -> None:
        """Save styles to ``path``."""
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.styles, f, indent=2)

    def add(self, style: str) -> None:
        if style not in self.styles:
            self.styles.append(style)

    def remove(self, style: str) -> None:
        if style in self.styles:
            self.styles.remove(style)


class StyleSheetTab(QWidget):
    """Simple editor for a :class:`StyleSheet`."""

    def __init__(self, sheet: StyleSheet | None = None) -> None:
        super().__init__()
        self.sheet = sheet or StyleSheet()
        self.sheet.load()
        self.list = QListWidget()
        self.add_btn = QPushButton("Add Style")
        self.remove_btn = QPushButton("Remove Style")
        self.add_btn.clicked.connect(self.add_style)
        self.remove_btn.clicked.connect(self.remove_style)
        layout = QVBoxLayout()
        layout.addWidget(self.list)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.remove_btn)
        self.setLayout(layout)
        self.refresh()

    def refresh(self) -> None:
        self.list.clear()
        for s in self.sheet.styles:
            item = QListWidgetItem(s)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.list.addItem(item)

    def add_style(self) -> None:
        item = QListWidgetItem("New Style")
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.list.addItem(item)
        self.sheet.add("New Style")

    def remove_style(self) -> None:
        for item in self.list.selectedItems():
            self.sheet.remove(item.text())
            self.list.takeItem(self.list.row(item))

    def closeEvent(self, event) -> None:  # type: ignore[override]
        self.sheet.styles = [self.list.item(i).text() for i in range(self.list.count())]
        self.sheet.save()
        super().closeEvent(event)

