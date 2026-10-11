import unittest
from unittest.mock import Mock

from photo_set_builder.src.data.photo_set_definition import PhotoSetDefinition
from photo_set_builder.src.photo_set_synchroniser import PhotoSetSynchroniser
from photo_set_builder.src.viewer_config_manager import ViewerConfigManager

class PhotoSetsSynchroniserTests(unittest.TestCase):
    def test_photo_sets_are_processed_with_their_config_folder_data(self):
        self.out.synchronise_photo_sets(self.photo_sets)

        self.photo_set_synchroniser.synchronise_photo_set.assert_called_once_with(
            self.photo_sets[0],
            self.photo_configs[2]
        )
        self.photo_set_synchroniser.synchronise_photo_set.assert_called_once_with(
            self.photo_sets[1],
            self.photo_configs[1]
        )
        self.photo_set_synchroniser.synchronise_photo_set.assert_called_once_with(
            self.photo_sets[2],
            self.photo_configs[0]
        )

    def setUp(self):
        self.photo_set_synchroniser = Mock(spec=PhotoSetSynchroniser)
        self.photo_sets = [
            PhotoSetDefinition('Photo set 1', 'path 1', None),
            PhotoSetDefinition('Photo set 2', 'path 2', None),
            PhotoSetDefinition('Photo set 3', 'path 3', None),
        ]
        self.viewer_config_manager = Mock(spec=ViewerConfigManager)
        self.out = PhotoSetSynchroniser(
            self.photo_set_synchroniser,
            self.viewer_config_manager
            )
