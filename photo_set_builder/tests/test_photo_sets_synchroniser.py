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

    def test_if_any_sets_have_been_changed_the_viewer_config_is_marked_as_changed(self):
        self.out.synchronise_photo_sets(self.photo_sets)

        self.viewer_config_manager.mark_as_changed.assert_called()

    def test_if_no_sets_have_been_changed_the_viewer_config_is_not_marked_as_changed(self):
        for pset in self.photo_sets:
            pset.photo_set_has_changed = False

        self.out.synchronise_photo_sets(self.photo_sets)

        self.viewer_config_manager.mark_as_changed.assert_not_called()

    def setUp(self):
        self.photo_set_synchroniser = Mock(spec=PhotoSetSynchroniser)
        self.viewer_config_manager = Mock(spec=ViewerConfigManager)
        self.photo_sets = [
            PhotoSetDefinition('Photo set 1', 'path 1', None, None, True),
            PhotoSetDefinition('Photo set 2', 'path 2', None, None, False),
            PhotoSetDefinition('Photo set 3', 'path 3', None, None, True),
        ]
        self.out = PhotoSetsSynchroniser(
            self.photo_set_synchroniser,
            self.viewer_config_manager
            )