from sys import stdout


class LogsAnalyser:
    def __init__(self, system_operations, project_root, status_updater, working_folder):
        self._system_operations = system_operations
        self._project_root = project_root
        self._status_updater = status_updater
        self._working_folder = working_folder

    def analyse_logs(self):
        print(f'LogsAnalyser: project_root={self._project_root} working_folder={self._working_folder}')
        #self.find_log_files(self._project_root)
        #self.find_log_files(self._working_folder)
