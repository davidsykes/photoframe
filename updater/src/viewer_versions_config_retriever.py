from pathlib import Path


class ViewerVersionsConfigRetriever:
    def __init__(self, sys_operations, remote_files_retriever):
        self._sys_operations = sys_operations
        self._remote_files_retriever = remote_files_retriever
        self.local_viewer_versions_config_path = "viewer-versions-config.json"
        self.remote_viewer_versions_config_path = "viewer-versions-config-new.json"

    def retrieve_viewer_versions_config(self, viewer_config_remote_url):
        self._remote_files_retriever.download_file(
            viewer_config_remote_url + "&dl=1" ,
            Path(self.remote_viewer_versions_config_path),
        )
        #new_config = self.load_and_check_config(self.remote_viewer_versions_config_path)
        #if new_config is not None:
        #    self._sys_operations.move_file(
        #        Path(self.remote_viewer_versions_config_path),
        #        Path(self.local_viewer_versions_config_path),
        #    )
        #    return self.load_and_check_config(self.local_viewer_versions_config_path)
