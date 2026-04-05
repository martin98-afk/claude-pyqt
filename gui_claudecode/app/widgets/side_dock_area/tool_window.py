# -*- coding: utf-8 -*-
from enum import Enum

from PyQt5.QtWidgets import QWidget


class DockPosition(Enum):
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"


class ToolWindow(QWidget):
    def __init__(self, homepage=None, button=None):
        super().__init__(parent=None)
        self.homepage = homepage
        self.button = button
        if hasattr(self, "setup_ui"):
            self.setup_ui()
