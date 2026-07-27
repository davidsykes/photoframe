import os

class SystemOperations:
    def load_file(self, file_name) -> str:
        with open(file_name, 'r') as file:
            data = file.read()
        return data
        
    def delete_file(self, file_name):
        os.remove(file_name)

    def replace_file(self, from_file, to_file):
        os.replace(from_file, to_file)

    def isdir(self, path) -> bool:
        return os.path.isdir(path)

    def rename(self, from_path, to_path):
        os.rename(from_path, to_path)
        return True
    
    def set_logger(self, log_file_path):
        import logging
        logging.basicConfig(
            filename=log_file_path,
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(name)s %(message)s"
        )
        self.logger = logging.getLogger(__name__)

    def log(self, message):
        self.logger.info(message)
        print("--- " + message)

    def progress(self, message):
        print("+++ " + message)
