from pathlib import Path
import unittest
from unittest.mock import Mock

from common.src.config_file import ConfigFile
from common.src.config_file_loader import ConfigFileLoader
from photo_set_builder.src.photo_set_builder_config import PhotosetBuilderConfig

class PhotosetBuilderConfigTests(unittest.TestCase):
    def test_photo_sets_location(self):
        self.assertEqual(
            self.out.photo_sets_path,
            Path('images folder')
        )

    def test_viewer_config_path(self):
        self.assertEqual(
            self.out.viewer_config_path,
            Path('viewer config file path')
        )

    def test_compressed_folder_name(self):
        self.assertEqual(
            self.out.compressed_folder_name,
            'compressed'
        )

    def test_dropbox_path(self):
        self.assertEqual(
            self.out.dropbox_path,
            Path('dropbox_path')
        )

    def setUp(self):
        self.config_file_loader = Mock(spec=ConfigFileLoader)
        self.config = ConfigFile(
            {
                'photo_sets_path': 'images folder',
                'viewer_config_path': 'viewer config file path',
                'compressed_folder_name': 'compressed',
                'dropbox_path': 'dropbox_path'
            },
            'config file path'
        )
        self.config_file_loader.load_config_file = self.load_config_file
        self.out = PhotosetBuilderConfig(
            self.config_file_loader,
            'config file path'
            )

    def load_config_file(self, config_file_path):
        self.assertEqual(config_file_path, 'config file path')
        return self.config