from pathlib import Path

class RemoteFolderDownloader:
    def __init__(self,
                 system_operations,
                 remote_files_retriever,
                 unzipper):
        self._system_operations = system_operations
        self._remote_files_retriever = remote_files_retriever
        self._unzipper = unzipper

    def download_folder(self, url, working_folder, destination_path):
        self._system_operations.progress(f"Download folder {url}")
        working_folder = Path(working_folder)
        zip_path = working_folder / 'zip.zip'
        unzip_folder = working_folder / 'contents'
        if self.download_remote_file(url, zip_path) and \
            self.unzip(zip_path, unzip_folder) and \
                self.move_folder(unzip_folder, destination_path):
            return True
        return False

    def download_remote_file(self, version_url, zip_path):
        if self._remote_files_retriever.download_file(
            version_url, zip_path):
            return True
        self._system_operations.log(
            f'Download version {version_url} to {zip_path} failed'
            )
        return False

    def unzip(self, zip_path, unzip_folder):
        if (self._unzipper.unzip(zip_path, unzip_folder)):
            self._system_operations.delete_file(zip_path)
            return True
        self._system_operations.log(
            f'Unzip folder {zip_path} failed'
            )
        return False

    def move_folder(self, source, destination):
        if self._system_operations.rename(source, destination):
            return True
        self._system_operations.log(
            f'Move folder {source} to {destination} failed'
            )
        return False
        