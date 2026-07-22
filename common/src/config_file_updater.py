class ConfigFileUpdater:
    def __init__(self,
                 remote_files_retriever,
                 config_file_loader,
                 sys_operations):
        self._remote_files_retriever = remote_files_retriever
        self._config_file_loader = config_file_loader
        self._sys_operations = sys_operations

    def update_config_file(self, remote_url, local_file_path):
        print(f"Updating config file from {remote_url} to {local_file_path}")
        temp_local_file_path = local_file_path + ".new"
        print(f"Temporary local file path: {temp_local_file_path}")
        if self._remote_files_retriever.download_file(
            remote_url, temp_local_file_path) is True:
            print(f"Downloaded file to {temp_local_file_path}")
            if (self._config_file_loader.load_config_file(
                temp_local_file_path) is not None):
                self._sys_operations.replace_file(
                    temp_local_file_path, local_file_path)
            else:
                self._sys_operations.delete_file(temp_local_file_path)
