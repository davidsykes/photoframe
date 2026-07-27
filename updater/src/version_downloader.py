class VersionDownloader:
    def __init__(self,
                 system_operations,
                 sandbox,
                 remote_files_retriever,
                 unzipper):
        self._system_operations = system_operations
        self._sandbox = sandbox
        self._remote_files_retriever = remote_files_retriever
        self._unzipper = unzipper

    def download_version(self, version):
        version_name = version[0]
        version_url = version[1]
        self._system_operations.progress(f"Download version {version_name}")
        zip_path = self._sandbox.get_version_zip_path(version_name)
        unzip_folder = self._sandbox.get_unzip_folder(version_name)
        if self.download_remote_file(version_name, version_url, zip_path) and \
            self.unzip(version_name, zip_path, unzip_folder) and \
                self.move_folder(version_name, unzip_folder):
            return True
        return False

    def download_remote_file(self, version_name, version_url, zip_path):
        if self._remote_files_retriever.download_file(
            version_url, zip_path):
            return True
        self._system_operations.log(
            f'Download version {version_name} to {zip_path} failed'
            )
        return False

    def unzip(self, name, zip_path, unzip_folder):
        if (self._unzipper.unzip(zip_path, unzip_folder)):
            self._system_operations.delete_file(zip_path)
            return True
        self._system_operations.log(
            f'Unzip folder {zip_path} failed'
            )
        return False

    def move_folder(self, version_name, unzip_folder):
        version_folder = self._sandbox.get_version_folder(version_name)
        if self._system_operations.rename(unzip_folder, version_folder):
            return True
        self._system_operations.log(
            f'Move folder {unzip_folder} failed'
            )
        return False
        