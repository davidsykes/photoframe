import datetime
import os
import shutil
from pathlib import Path
import time

class SystemOperations:
    def load_file(self, file_name) -> str:
        try:
            with open(file_name, 'r') as file:
                data = file.read()
            return data
        except FileNotFoundError:
            return None

    def delete_file(self, file_name):
        os.remove(file_name)

    def replace_file(self, from_file, to_file):
        os.replace(from_file, to_file)

    def shutil_copy(self, from_file, to_file):
        self.log(f'Copy file {from_file} to {to_file}')
        shutil.copy(from_file, to_file)

    def listdir(self, path) -> list[str]:
        return os.listdir(path)

    def isdir(self, path) -> bool:
        return os.path.isdir(path)

    def ensure_folder_exists(self, folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            self.log(f'Created folder {folder_path}')

    def rmtree(self, path):
        print(f'Remove folder {path}')
        shutil.rmtree(path)

    def rename(self, from_path, to_path):
        shutil.move(str(from_path), str(to_path))
        return True

    def set_logger(self, log_file_name, log_indent):
        log_folder = Path('logs')
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)
        import logging
        now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        logfile_path = log_folder / f'{log_file_name}-{now}.log'
        logging.basicConfig(
            filename=logfile_path,
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s"
        )
        self.logger = logging.getLogger(__name__)
        self.log_indent = log_indent

    def log(self, message):
        self.logger.info(message)
        print(f'{self.log_indent}--- {message}')

    def error(self, message):
        self.logger.error(message)
        print(f'{self.log_indent}!!! {message}')

    def progress(self, message):
        self.logger.info(message)
        print(f'{self.log_indent}+++ {message}')

    def get_time_seconds(self):
        return time.time()