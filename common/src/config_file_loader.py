import json

from common.src.config_file import ConfigFile

class ConfigFileLoader:
    def __init__(self, system_operations):
        self._system_operations = system_operations

    def load_config_file(self, file_name):
        try:
            print(f"Loading config file: {file_name}")
            data = self._system_operations.load_file(file_name)
            if data:
                config = json.loads(data) if data else {}
                return ConfigFile(config, file_name)
            else:
                self._system_operations.log(
                    f"Unable to open config file: '{file_name}'"
                )
        except json.decoder.JSONDecodeError as ex:
                self._system_operations.log(
                f"Failed to parse JSON file '{file_name}': {str(ex)}"
                )
