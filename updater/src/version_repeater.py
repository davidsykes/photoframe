

class VersionRepeater:
    def __init__(
            self,
            version_has_been_downloaded_checker,
            version_downloader,
            version_runner):
        self._version_has_been_downloaded_checker = version_has_been_downloaded_checker
        self._version_downloader = version_downloader
        self._version_runner = version_runner

    def run_version(self, version_name, repeat_count):
        if self._version_has_been_downloaded_checker.check_if_version_has_been_downloaded(version_name) is False:
            self._version_downloader.download_version(version_name)

        self._version_runner.run_version(version_name)