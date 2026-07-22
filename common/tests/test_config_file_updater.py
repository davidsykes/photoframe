import unittest
from unittest.mock import Mock
from common.src.config_file_updater import ConfigFileUpdater


class TestConfigFileUpdater(unittest.TestCase):
    def test_update(self):
        self.out.update_config_file("remote_url", "local_file_path")

        self.remote_files_retriever.download_file.assert_called_once_with(
            "remote_url", "local_file_path.new")
        self.config_file_loader.load_config_file.assert_called_once_with(
            "local_file_path.new")
        self.sys_operations.replace_file.assert_called_once_with(
            "local_file_path.new", "local_file_path")

    def test_if_retrieve_fails_the_file_is_not_updated(self):
        self.remote_files_retriever.download_file.return_value\
             = False

        self.out.update_config_file("remote_url", "local_file_path")

        self.remote_files_retriever.download_file.assert_called_once_with(
            "remote_url", "local_file_path.new")
        self.config_file_loader.load_config_file.assert_not_called()
        self.sys_operations.replace_file.assert_not_called()

    def test_if_downloaded_config_is_invalid_the_file_is_not_updated(self):
        self.config_file_loader.load_config_file.return_value = None

        self.out.update_config_file("remote_url", "local_file_path")

        self.remote_files_retriever.download_file.assert_called_once_with(
            "remote_url", "local_file_path.new")
        self.config_file_loader.load_config_file.assert_called_once_with(
            "local_file_path.new")
        self.sys_operations.replace_file.assert_not_called()

    def test_if_downloaded_config_is_invalid_the_temp_file_is_deleted(self):
        self.config_file_loader.load_config_file.return_value = None

        self.out.update_config_file("remote_url", "local_file_path")
        
        self.sys_operations.delete_file.assert_called_once_with(
            "local_file_path.new"
        )

    @classmethod
    def setUp(self):
        self.remote_files_retriever = Mock()
        self.remote_files_retriever.download_file = Mock()
        self.remote_files_retriever.download_file.return_value =\
             True
        self.config_file_loader = Mock()
        self.config_file_loader.load_config_file = Mock()
        self.config_file_loader.load_config_file.return_value = { "a": "b" }
        self.sys_operations = Mock()
        self.out = ConfigFileUpdater(
            self.remote_files_retriever,
            self.config_file_loader,
            self.sys_operations )
