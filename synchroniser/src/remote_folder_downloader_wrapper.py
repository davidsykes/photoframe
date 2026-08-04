from tempfile import TemporaryDirectory

class RemoteFolderDownloaderWrapper:
    def __init__(self,
                 system_operations,
                 remote_folder_downloader,
                 tmp_folder_location):
        self._system_operations = system_operations
        self._remote_folder_downloader = remote_folder_downloader
        self._tmp_folder_location = tmp_folder_location

    def download_folder(self, url, destination_path):
        with TemporaryDirectory(dir=self._tmp_folder_location) as test_folder:
            self._system_operations.progress(
                f"Download folder {destination_path} from {url} using temporary folder {test_folder}")
            return self._remote_folder_downloader.download_folder(
                url,
                test_folder,
                destination_path
            )