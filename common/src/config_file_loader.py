import json

from common.src.config_file import ConfigFile

class ConfigFileLoader:
    def __init__(self, file_loader):
        self.file_loader = file_loader

    def load_config_file(self, file_name):
        try:
            print(f"Loading config file: {file_name}")
            data = self.file_loader.load_file(file_name)
            config = json.loads(data) if data else {}
            return ConfigFile(config, file_name)
        except json.decoder.JSONDecodeError as ex:
            raise RuntimeError(
                f"Failed to parse JSON file '{file_name}': {ex}"
                ) from ex
