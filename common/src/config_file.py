from pathlib import Path
from typing import Any


class ConfigFile:
    def __init__(self, data:Any, file_name:Path):
        self.config = data
        self.file_name = file_name

    def get(self, key:str) -> str:
        if key in self.config:
            return self.config[key]
        else:
            raise Exception(
                f"Key '{key}' not found in configuration file '{self.file_name}'.")

    def get_or_default(self, key, default) -> str:
        if key in self.config:
            return self.config[key]
        return default
