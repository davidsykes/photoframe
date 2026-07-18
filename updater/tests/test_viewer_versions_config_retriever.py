from pathlib import Path
import unittest
from unittest.mock import Mock

from updater.src.viewer_versions_config_retriever import ViewerVersionsConfigRetriever

class TheRemoteConfigFileIsDownloaded(unittest.TestCase):
    def test_load(self):

        self.out.retrieve_viewer_versions_config("remote_url")

        self.remote_files_retriever.download_file.assert_called_once_with(
            "remote_url&dl=1", Path("viewer-versions-config-new.json"))

            
    @classmethod
    def setUp(self):
        self.sys_operations = Mock()
        self.remote_files_retriever = Mock()
        self.out = ViewerVersionsConfigRetriever(
            self.sys_operations, self.remote_files_retriever)

if __name__ == "__main__":
    unittest.main()