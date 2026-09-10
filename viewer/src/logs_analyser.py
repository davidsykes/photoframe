import os
from pathlib import Path
from sys import stdout
import time


class LogsAnalyser:
    def __init__(self, system_operations, project_root, status_updater, working_folder):
        self._system_operations = system_operations
        self._project_root = project_root
        self._status_updater = status_updater
        self._working_folder = working_folder
        self._log_count = 0
        self._now = time.time()
        self._folders = {}

    def analyse_logs(self):
        print(f'LogsAnalyser: project_root={self._project_root} working_folder={self._working_folder}')
        self._status_updater.update_status('project_root', self._project_root)
        self._status_updater.update_status('working_folder', self._working_folder)
        self.find_log_files(self._project_root, )
        self.find_log_files(self._working_folder)
        self._status_updater.update_status('Log file count', self._log_count)
        for f in self._folders:
            print(f'Logs {f} => {self._folders[f]}')
            self._status_updater.update_status(f'Logs in {f}', self._folders[f])

    def find_log_files(self, path):
        source_folder = Path(path)
        for path in source_folder.rglob("*"):
            parent = path.parent
            parent_name = parent.name
            parent2 = parent.parent
            parent2_name = parent2.name
            if parent_name == 'logs' and parent2_name[0] != '.':
                self._log_count = self._log_count + 1
                mtime = os.path.getmtime(path)
                age_seconds = self._now - mtime
                age_days = age_seconds / 60 / 60 / 24
                #print(f'path {name} {age_days} {path}')
                self.add_log_count(parent2)

    def add_log_count(self, name):
        if name in self._folders:
            self._folders[name] = self._folders[name] + 1
        else:
            self._folders[name] = 1