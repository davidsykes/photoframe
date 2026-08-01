import datetime
import os
from pathlib import Path

class SystemOperations:
    def load_file(self, file_name) -> str:
        with open(file_name, 'r') as file:
            data = file.read()
        return data
        
    def delete_file(self, file_name):
        os.remove(file_name)

    def replace_file(self, from_file, to_file):
        self.log(f'Move file {from_file} to {to_file}')
        os.replace(from_file, to_file)

    def isdir(self, path) -> bool:
        return os.path.isdir(path)

    def ensure_folder_exists(self, folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            self.log(f'Created folder {folder_path}')

    def rename(self, from_path, to_path):
        os.rename(from_path, to_path)
        return True
    
    def set_logger(self, log_file_name):
        import logging
        now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        logfile_path = Path('logs') / f'{log_file_name} {now}.log'
        logging.basicConfig(
            filename=logfile_path,
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s"
        )
        self.logger = logging.getLogger(__name__)

    def log(self, message):
        self.logger.info(message)
        print("--- " + message)

    def progress(self, message):
        self.logger.info(message)
        print("+++ " + message)
