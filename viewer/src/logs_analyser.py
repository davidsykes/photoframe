class LogsAnalyser:
    def __init__(self, system_operations, project_root, status_updater, working_folder):
        self._system_operations = system_operations
        self._project_root = project_root
        self._status_updater = status_updater
        self._working_folder = working_folder