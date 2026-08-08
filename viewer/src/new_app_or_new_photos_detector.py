from viewer.src.viewer_exit_exception import ViewerExitException


class NewAppOrNewPhotosDetector:
    def __init__(self,
                 remote_version_loader):
        self._version_retriever = remote_version_loader

    def poll(self) -> None:
        current_version = self._version_retriever.get_version()
        if not hasattr(self, '_last_version'):
            self._last_version = current_version
        elif self._last_version != current_version:
            raise ViewerExitException(
                100,
                f"Version changed from {self._last_version} to {current_version}.")