import unittest

from synchroniser.src.photo_collections.photo_collection import PhotoCollection


class TestPhotoCollection(unittest.TestCase):
    def test_name_is_the_first_item(self):
        collection = PhotoCollection(['name', 'url'])
        self.assertEqual(collection.name, 'name')

    def test_url_is_the_second_item(self):
        collection = PhotoCollection(['name', 'url'])
        self.assertEqual(collection.url, 'url')

    def test_filter_tags_is_the_name_if_only_two_values_are_provided(self):
        collection = PhotoCollection(['name', 'url'])
        self.assertEqual(collection.filter_tags, 'name')

    def test_filter_tags_is_the_third_item_if_three_values_are_provided(self):
        collection = PhotoCollection(['name', 'url', 'filter_tags'])
        self.assertEqual(collection.filter_tags, 'filter_tags')