# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QCompleter


class SearchableEditableComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.NoInsert)
        completer = QCompleter(self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setFilterMode(Qt.MatchContains)
        completer.setCompletionMode(QCompleter.PopupCompletion)
        self.setCompleter(completer)

    def addItems(self, texts):
        super().addItems(texts)
        if self.completer():
            self.completer().setModel(self.model())

    def text(self) -> str:
        return self.currentText()

    def setText(self, text: str):
        self.setEditText(text)

