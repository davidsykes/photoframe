import unittest
from unittest.mock import Mock

from photo_set_builder.src.data.photo_set_configuration import PhotoSetConfiguration
from photo_set_builder.src.data.photo_set_definition import PhotoSetDefinition
from photo_set_builder.src.photo_set_processing.photo_set_processor import PhotoSetProcessor
from photo_set_builder.src.photo_set_processing.photo_sets_processor import PhotoSetsProcessor


class PhotoSetsProcessorTests(unittest.TestCase):
    def test_all_included_photo_sets_are_processed(self):
        self.out.process_photo_sets(self.photo_sets)

        self.assertEqual(self.photo_set_processor.process_photo_set.call_count,
                         2)
        self.photo_set_processor.process_photo_set.assert_any_call(
            self.photo_sets[0])
        self.photo_set_processor.process_photo_set.assert_any_call(
            self.photo_sets[2])

    def setUp(self):
        self.photo_sets = [
            self.create_photo_set(1, True),
            self.create_photo_set(2, False),
            self.create_photo_set(3, True),
        ]
        self.photo_set_processor = Mock(spec=PhotoSetProcessor)
        self.out = PhotoSetsProcessor(
            self.photo_set_processor
            )

    def create_photo_set(self, number, included):
        return PhotoSetDefinition(
            f'Photo set {number}',
            f'Path {number}',
            PhotoSetConfiguration(included, 'filter')
        )