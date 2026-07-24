class VersionDownloader:
    def __init__(self,
                 system_operations,
                 remote_files_retriever):
        self._system_operations = system_operations
        self._remote_files_retriever = remote_files_retriever

    def download_version(self, version):
        version_name = version[0]
        version_url = version[1]
        version_destination = version_name + ".zip"
        self._system_operations.progress(f"Download version {version_name}")
        if self._remote_files_retriever.download_file(
            version_url, version_destination) is False:
            self._system_operations.log(
                f'Download version {version_name} to {version_url} failed'
            )
            return False
        return True