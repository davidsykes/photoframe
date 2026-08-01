from pathlib import Path
from tempfile import TemporaryDirectory

class RemoteFolderDownloaderWrapper:
    def __init__(self,
                 system_operations,
                 remote_folder_downloader):
        self._system_operations = system_operations
        self._remote_folder_downloader = remote_folder_downloader

    def download_folder(self, url, destination_path):
        with TemporaryDirectory() as test_folder:
            self._system_operations.progress(
                f"Download folder {url} to {destination_path} using temporary folder {test_folder}")
            return self._remote_folder_downloader.download_folder(
                url,
                test_folder,
                destination_path
            )