from pathlib import Path
import unittest
from unittest.mock import Mock
from common.src.config_file_loader import ConfigFileLoader
from common.src.config_file_updater import ConfigFileUpdater
from common.src.remote_files_retriever import RemoteFilesRetriever
from common.src.system_operations import SystemOperations


class TestConfigFileUpdater(unittest.TestCase):
    def test_update(self):
        self.out.update_config_file("remote_url", 'local_file_path')

        self.remote_files_retriever.download_file_or_return_false.assert_called_once_with(
            "remote_url", Path('local_file_path.new'))
        self.config_file_loader.load_config_file.assert_called_once_with(
            Path('local_file_path.new'))
        self.sys_operations.replace_file.assert_called_once_with(
            Path('local_file_path.new'), Path('local_file_path'))

    def test_if_retrieve_fails_the_file_is_not_updated(self):
        self.remote_files_retriever.download_file_or_return_false\
            .return_value = False

        self.out.update_config_file("remote_url", self.local_file_path)

        self.remote_files_retriever.download_file_or_return_false.assert_called_once_with(
            "remote_url", self.local_file_path_new)
        self.config_file_loader.load_config_file.assert_not_called()
        self.sys_operations.replace_file.assert_not_called()

    def test_if_downloaded_config_is_invalid_the_file_is_not_updated(self):
        self.config_file_loader.load_config_file.return_value = None

        self.out.update_config_file("remote_url", self.local_file_path)

        self.remote_files_retriever.download_file_or_return_false.assert_called_once_with(
            "remote_url", self.local_file_path_new)
        self.config_file_loader.load_config_file.assert_called_once_with(
            self.local_file_path_new)
        self.sys_operations.replace_file.assert_not_called()

    def test_if_downloaded_config_is_invalid_the_temp_file_is_deleted(self):
        self.config_file_loader.load_config_file.return_value = None

        self.out.update_config_file("remote_url", self.local_file_path)

        self.sys_operations.delete_file.assert_called_once_with(
            self.local_file_path_new
        )

    def setUp(self):
        self.local_file_path = Path('local_file_path')
        self.local_file_path_new = Path('local_file_path.new')
        self.remote_files_retriever = Mock(spec = RemoteFilesRetriever)
        self.remote_files_retriever.download_file_or_return_false.return_value = (
             True)
        self.config_file_loader = Mock(spec = ConfigFileLoader)
        self.config_file_loader.load_config_file.return_value = { "a": "b" }
        self.sys_operations = Mock(spec = SystemOperations)
        self.out = ConfigFileUpdater(
            self.remote_files_retriever,
            self.config_file_loader,
            self.sys_operations )
