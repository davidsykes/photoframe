import unittest
from unittest.mock import Mock

from photo_set_builder.src.photo_set_processing.photo_set_processor import PhotoSetProcessor
from photo_set_builder.src.photo_set_processing.photo_sets_processor import PhotoSetsProcessor


class PhotoSetsProcessorTests(unittest.TestCase):
    def test_all_photo_sets_are_processed(self):
        self.out.process_photo_sets(self.photo_sets)

        self.assertEqual(
            self.photo_set_processor.process_photo_set.call_count,
            len(self.photo_sets)
        )
        self.photo_set_processor.process_photo_set.assert_any_call(
            self.photo_sets[0])
        self.photo_set_processor.process_photo_set.assert_any_call(
            self.photo_sets[1])
        self.photo_set_processor.process_photo_set.assert_any_call(
            self.photo_sets[2])

    def setUp(self):
        self.photo_sets = [
            Mock(name='PhotoSet1'),
            Mock(name='PhotoSet2'),
            Mock(name='PhotoSet3')
        ]
        self.photo_set_processor = Mock(spec=PhotoSetProcessor)
        self.out = PhotoSetsProcessor(
            self.photo_set_processor
            )

    def load_config_file(self, config_file_path):
        self.assertEqual(config_file_path, 'config file path')
        return self.config