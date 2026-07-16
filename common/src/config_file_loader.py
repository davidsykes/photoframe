import json

class ConfigFileLoader:
    def __init__(self, file_loader, file_name):
        self.file_name = file_name
        self.data = file_loader.load_file(file_name)
        try:
            self.config = json.loads(self.data) if self.data else {}
        except json.decoder.JSONDecodeError as ex:
            raise RuntimeError(
                f"Failed to parse JSON file '{file_name}': {ex}"
                ) from ex

    def get(self, key):
        if key in self.config:
            return self.config[key]
        else:
            raise Exception(f"Key '{key}' not found in configuration file '{self.file_name}'.")