import json

from common.src.config_file import ConfigFile

class ConfigFileLoader:
    def __init__(self, system_operations):
        self._system_operations = system_operations

    def load_config_file(self, file_name) -> ConfigFile:
        try:
            data = self._system_operations.load_file(file_name)
            if data:
                config = json.loads(data) if data else {}
                return ConfigFile(config, file_name)
            else:
                self._system_operations.error(
                    f"Unable to open config file: '{file_name}'"
                )
        except FileNotFoundError as ex:
                self._system_operations.error(
                f"Unable to open config file '{file_name}': {str(ex)}"
                )
        except json.decoder.JSONDecodeError as ex:
                self._system_operations.error(
                f"Failed to parse JSON file '{file_name}': {str(ex)}"
                )
