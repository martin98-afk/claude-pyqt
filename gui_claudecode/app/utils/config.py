# -*- coding: utf-8 -*-
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict


@dataclass
class _SettingField:
    owner: "Settings"
    key: str
    default: Any

    @property
    def value(self) -> Any:
        return self.owner._data.get(self.key, self.default)


class Settings:
    _instance = None

    def __init__(self):
        self._config_dir = Path.home() / ".gui_claudecode"
        self._config_file = self._config_dir / "settings.json"
        self._defaults: Dict[str, Any] = {
            "llm_selected_model": "系统默认配置",
            "llm_model": "gpt-4o-mini",
            "llm_api_key": "",
            "llm_api_base": "https://api.openai.com/v1",
            "llm_max_tokens": 4096,
            "llm_temperature": 0.7,
            "llm_enable_thinking": False,
            "llm_saved_providers": {},
            "SERPAPI_KEY": "",
            "canvas_font_selected": "Segoe UI",
        }
        self._data = self._load()

        self.llm_selected_model = _SettingField(
            self, "llm_selected_model", self._defaults["llm_selected_model"]
        )
        self.llm_model = _SettingField(self, "llm_model", self._defaults["llm_model"])
        self.llm_api_key = _SettingField(
            self, "llm_api_key", self._defaults["llm_api_key"]
        )
        self.llm_api_base = _SettingField(
            self, "llm_api_base", self._defaults["llm_api_base"]
        )
        self.llm_max_tokens = _SettingField(
            self, "llm_max_tokens", self._defaults["llm_max_tokens"]
        )
        self.llm_temperature = _SettingField(
            self, "llm_temperature", self._defaults["llm_temperature"]
        )
        self.llm_enable_thinking = _SettingField(
            self, "llm_enable_thinking", self._defaults["llm_enable_thinking"]
        )
        self.llm_saved_providers = _SettingField(
            self, "llm_saved_providers", self._defaults["llm_saved_providers"]
        )
        self.SERPAPI_KEY = _SettingField(
            self, "SERPAPI_KEY", self._defaults["SERPAPI_KEY"]
        )
        self.canvas_font_selected = _SettingField(
            self, "canvas_font_selected", self._defaults["canvas_font_selected"]
        )

    def _load(self) -> Dict[str, Any]:
        if not self._config_file.exists():
            return dict(self._defaults)
        try:
            with open(self._config_file, "r", encoding="utf-8") as f:
                loaded = json.load(f)
            data = dict(self._defaults)
            if isinstance(loaded, dict):
                data.update(loaded)
            return data
        except Exception:
            return dict(self._defaults)

    def set(self, field_or_key, value: Any, save: bool = False):
        key = field_or_key.key if isinstance(field_or_key, _SettingField) else str(field_or_key)
        self._data[key] = value
        if save:
            self.save_config()

    def save_config(self):
        self._config_dir.mkdir(parents=True, exist_ok=True)
        with open(self._config_file, "w", encoding="utf-8") as f:
            json.dump(self._data, f, ensure_ascii=False, indent=2)

    @classmethod
    def get_instance(cls) -> "Settings":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

