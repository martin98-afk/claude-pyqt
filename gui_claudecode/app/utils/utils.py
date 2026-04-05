# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Any

from PyQt5.QtGui import QFont, QIcon


_THEME_ICON_MAP = {
    "大模型": "applications-development",
    "长期记忆": "document-properties",
    "shell": "utilities-terminal",
    "回形针": "mail-attachment",
    "更新": "view-refresh",
}


def resource_path(path: str = "") -> str:
    base_dir = Path(__file__).resolve().parents[2]
    return str((base_dir / path).resolve())


def get_icon(name: str) -> QIcon:
    theme_name = _THEME_ICON_MAP.get(name, "")
    icon = QIcon.fromTheme(theme_name) if theme_name else QIcon()
    if not icon.isNull():
        return icon
    return QIcon()


def get_unified_font(size: int = 10, bold: bool = False) -> QFont:
    font = QFont("Segoe UI", size)
    font.setBold(bold)
    return font


def serialize_for_json(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(k): serialize_for_json(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [serialize_for_json(v) for v in value]
    if isinstance(value, Path):
        return str(value)
    if hasattr(value, "__dict__"):
        return serialize_for_json(vars(value))
    return value


def deserialize_from_json(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: deserialize_from_json(v) for k, v in value.items()}
    if isinstance(value, list):
        return [deserialize_from_json(v) for v in value]
    return value

