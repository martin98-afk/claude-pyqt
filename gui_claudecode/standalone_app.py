# -*- coding: utf-8 -*-
from pathlib import Path

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from app.components.base import CustomVariable
from main_widget import OpenAIChatToolWindow
from widgets.context_selector import ContextRegistry


class GlobalVariables:
    def __init__(self):
        self.custom = {}


class StandaloneHomepage(QObject):
    global_variables_changed = pyqtSignal()

    def __init__(self, workspace: str = None):
        super().__init__()
        self.workflow_name = "standalone"
        self.workspace = str(Path(workspace or Path.cwd()).resolve())
        self.global_variables = GlobalVariables()
        self.context_register = ContextRegistry()
        self._register_default_contexts()

    def _register_default_contexts(self):
        def workspace_provider():
            path = self.workspace
            return ("当前工作目录", {"path": path, "text": path}, None)

        def noop_executor(_data, _tag=None):
            return None

        self.context_register.register("@workspace", workspace_provider, noop_executor)

    def _on_global_variables_changed(self, _scope: str, _name: str, _action: str):
        self.global_variables_changed.emit()

    def on_context_action(self, _action: str, _payload: str):
        return None

    def execute_skill(self, _method: str, _params: dict) -> dict:
        return {"error": "独立版暂未接入宿主技能执行器"}

    def add_custom_model_config(self, name: str, config: dict):
        self.global_variables.custom[name] = CustomVariable(value=config)
        self.global_variables_changed.emit()


class StandaloneMainWindow(QMainWindow):
    def __init__(self, workspace: str = None):
        super().__init__()
        self.homepage = StandaloneHomepage(workspace=workspace)
        self.chat_widget = OpenAIChatToolWindow(self.homepage, button=None)
        self.setWindowTitle("GUI ClaudeCode")
        self.setCentralWidget(self.chat_widget)
        self.resize(1280, 900)

