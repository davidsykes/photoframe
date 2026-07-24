from enum import Enum, auto

class DownloadResult(Enum):
    REMOTE_VERSION_MISSING = auto()
    VERSION_APPLICATION_ENDED = auto()
    CHECK_FOR_UPDATES = auto()

class VersionRepeater:
    def __init__(
            self,
            version_has_been_downloaded_checker,
            version_downloader,
            version_runner):
        self._version_has_been_downloaded_checker = version_has_been_downloaded_checker
        self._version_downloader = version_downloader
        self._version_runner = version_runner

    def run_version(self, version, repeat_count) -> DownloadResult:
        version_name = version[0]
        if self._version_has_been_downloaded_checker.check_if_version_has_been_downloaded(version_name) is False:
            if self._version_downloader.download_version(version) is False:
                return DownloadResult.REMOTE_VERSION_MISSING

        self._version_runner.run_version(version_name)
        return DownloadResult.VERSION_APPLICATION_ENDED