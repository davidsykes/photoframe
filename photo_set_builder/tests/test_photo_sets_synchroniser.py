import unittest
from unittest.mock import Mock, call

from photo_set_builder.src.data.photo_set_definition import PhotoSetDefinition
from photo_set_builder.src.photo_set_synchroniser import PhotoSetSynchroniser
from photo_set_builder.src.photo_sets_synchroniser import PhotoSetsSynchroniser
from photo_set_builder.src.viewer_config_manager import ViewerConfigManager

class PhotoSetsSynchroniserTests(unittest.TestCase):
    def test_changed_photo_sets_are_processed_with_their_config_folder_data(self):
        self.out.synchronise_photo_sets(self.photo_sets)

        self.assertEqual(2,
                         self.photo_set_synchroniser.synchronise_photo_set.call_count)
        self.photo_set_synchroniser.synchronise_photo_set.assert_has_calls(
            [call(self.photo_sets[0]),
             call(self.photo_sets[2])]
        )

    def setUp(self):
        self.photo_set_synchroniser = Mock(spec=PhotoSetSynchroniser)
        self.photo_sets = [
            PhotoSetDefinition('Photo set 1', 'path 1', None, None, True),
            PhotoSetDefinition('Photo set 2', 'path 2', None, None, False),
            PhotoSetDefinition('Photo set 3', 'path 3', None, None, True),
        ]
        self.out = PhotoSetsSynchroniser(
            self.photo_set_synchroniser
            )