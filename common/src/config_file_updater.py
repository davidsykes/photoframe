class ConfigFileUpdater:
    def __init__(self,
                 remote_files_retriever,
                 config_file_loader,
                 sys_operations):
        self._remote_files_retriever = remote_files_retriever
        self._config_file_loader = config_file_loader
        self._sys_operations = sys_operations

    def update_config_file(self, remote_url, local_file_path):
        if self._remote_files_retriever.download_file(
            remote_url, local_file_path + ".new") is True:
            if (self._config_file_loader.load_config_file(local_file_path + ".new") is not None):
                self._sys_operations.move_file(
                    local_file_path + ".new", local_file_path)
