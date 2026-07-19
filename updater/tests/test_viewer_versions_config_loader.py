from pathlib import Path
import unittest
from unittest.mock import Mock

from updater.src.viewer_versions_config_loader import ViewerVersionsConfigLoader

class ViewerVersionsConfigLoaderTests(unittest.TestCase):
    def test_the_remote_config_file_is_updated_and_loaded(self):

        config = self.out.load_viewer_versions_config("remote_url")

        self.config_file_updater.update_config_file.assert_called_once_with(
            "remote_url", "viewer config path")
        self.config_file_loader.load_config_file.assert_called_once_with(
            "viewer config path")
        self.assertEqual(config, {"viewer": "config"})

    @classmethod
    def setUp(self):
        self.config_file_updater = Mock()
        self.config_file_loader = Mock()
        self.config_file_loader.load_config_file = Mock()
        self.config_file_loader.load_config_file.return_value = {"viewer": "config"}
        self.out = ViewerVersionsConfigLoader(
            self.config_file_updater,
            self.config_file_loader,
            "remote_url",
            "viewer config path"
        )
