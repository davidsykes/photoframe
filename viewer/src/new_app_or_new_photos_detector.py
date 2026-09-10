from viewer.src.viewer_exit_exception import ViewerExitException

class NewAppOrNewPhotosDetector:
    def __init__(self,
                 remote_config_version_loader,
                 system_operations,
                 initial_remote_config_version):
        self._version_retriever = remote_config_version_loader
        self._system_operations = system_operations
        self._last_version = initial_remote_config_version

    def poll(self) -> None:
        config_data = self._version_retriever.get_config_data()
        current_version = config_data.version
        self._system_operations.log(f"Remote configuration version: {current_version}. Local version: {self._last_version}")
        if self._last_version != current_version:
            raise ViewerExitException(
                100,
                f"Version changed from {self._last_version} to {current_version}.")