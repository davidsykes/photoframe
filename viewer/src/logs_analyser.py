import subprocess
from sys import stdout


class LogsAnalyser:
    def __init__(self, system_operations, project_root, status_updater, working_folder):
        self._system_operations = system_operations
        self._project_root = project_root
        self._status_updater = status_updater
        self._working_folder = working_folder

    def analyse_logs(self):
        pass
        # try:
        #     proc = subprocess.run(['wlr-randr'], encoding='utf-8', stdout=subprocess.PIPE, check=False)
        #     self._status_updater.update_status('wlr-randr output', proc.stdout)
        # except Exception as e:
        #     self._status_updater.update_status('wlr-randr output', str(e))
