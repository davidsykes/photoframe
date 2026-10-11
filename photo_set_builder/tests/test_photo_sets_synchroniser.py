import unittest
from unittest.mock import Mock, call

from photo_set_builder.src.data.photo_set_definition import PhotoSetDefinition
from photo_set_builder.src.photo_set_synchroniser import PhotoSetSynchroniser
from photo_set_builder.src.photo_sets_synchroniser import PhotoSetsSynchroniser
from photo_set_builder.src.viewer_config_manager import ViewerConfigManager

class PhotoSetsSynchroniserTests(unittest.TestCase):
    def test_photo_sets_are_processed_with_their_config_folder_data(self):
        self.out.synchronise_photo_sets(self.photo_sets)

        self.photo_set_synchroniser.synchronise_photo_set.assert_has_calls(
            [call(self.photo_sets[0], self.photo_configs[2]),
             call(self.photo_sets[1], self.photo_configs[1]),
             call(self.photo_sets[2], self.photo_configs[0])]
        )

    def setUp(self):
        self.photo_set_synchroniser = Mock(spec=PhotoSetSynchroniser)
        self.photo_sets = [
            PhotoSetDefinition('Photo set 1', 'path 1', None),
            PhotoSetDefinition('Photo set 2', 'path 2', None),
            PhotoSetDefinition('Photo set 3', 'path 3', None),
        ]
        self.photo_configs = [
            ['Photo set 3', 'Config 1'],
            ['Photo set 2', 'Config 2'],
            ['Photo set 1', 'Config 3']
        ]
        self.viewer_config_manager = Mock(spec=ViewerConfigManager)
        self.viewer_config_manager.find_photo_set_config = self.find_photo_set_config
        self.out = PhotoSetsSynchroniser(
            self.photo_set_synchroniser,
            self.viewer_config_manager
            )

    def find_photo_set_config(self, photo_set_name):
        for config in self.photo_configs:
            if config[0] == photo_set_name:
                return config