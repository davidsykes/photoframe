import json

class IniFileLoader:
    def __init__(self, file_loader, file_name):
        self.data = file_loader.load(file_name)
        self.config = json.loads(self.data) if self.data else {}

    def get(self, key):
        if key in self.config:
            return self.config[key]
        else:
            raise Exception(f"Key '{key}' not found in configuration.")