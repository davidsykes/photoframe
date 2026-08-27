class VersionLoader:
    def __init__(self, system_operations, status):
        self._system_operations = system_operations
        self._status = status

    def load_version_details(self, version_path):
        data = self._system_operations.load_file(version_path)
        if data is None:
            self.set_status(f"File '{version_path}' not found")
        else:
            self.set_status(data.replace("\r\n", " ").replace("\n", " "))

    def set_status(self, status):
        self._status.update_status('Version', status)