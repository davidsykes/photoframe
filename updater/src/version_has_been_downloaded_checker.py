from pathlib import Path

class VersionHasBeenDownloadedChecker:
    def __init__(self, system_operations, versions_path):
        self._system_operations = system_operations
        self._versions_path = versions_path

    def check_if_version_has_been_downloaded(self, version_name) -> bool:
        path = Path(self._versions_path, version_name)
        return self._system_operations.isdir(path)
