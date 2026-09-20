import unittest

from viewer.src.photos.photo_history import PhotoHistory

class PhotoHistoryTests(unittest.TestCase):
    def test_stored_photos_can_be_retrieved_in_reverse_order(self):
        self.out.new_photo('Photo 1')
        self.out.new_photo('Photo 2')
        self.out.new_photo('Photo 3')

        self.assertEqual('Photo 3', self.out[0])
        self.assertEqual('Photo 2', self.out[1])
        self.assertEqual('Photo 1', self.out[2])

    def test_only_n_photos_are_retained(self):
        self.assertEqual(0, len(self.out))

        self.out.new_photo('Photo 1')
        self.out.new_photo('Photo 2')
        self.out.new_photo('Photo 3')
        self.assertEqual(3, len(self.out))

        self.out.new_photo('Photo 4')
        self.out.new_photo('Photo 5')
        self.out.new_photo('Photo 6')
        self.assertEqual(5, len(self.out))

    def test_has_photo_been_shown_recently(self):
        self.out.new_photo('Photo 1')
        self.out.new_photo('Photo 2')
        self.out.new_photo('Photo 3')
        self.out.new_photo('Photo 4')
        self.out.new_photo('Photo 5')

        self.assertTrue(self.out.has_photo_been_shown_recently('Photo 1'))
        self.assertTrue(self.out.has_photo_been_shown_recently('Photo 5'))
        self.assertFalse(self.out.has_photo_been_shown_recently('Photo 6'))

    def test_has_photo_been_shown_recently_loops(self):
        self.out.new_photo('Photo 1')
        self.out.new_photo('Photo 2')
        self.out.new_photo('Photo 3')
        self.out.new_photo('Photo 4')
        self.out.new_photo('Photo 5')
        self.out.new_photo('Photo 6')

        self.assertFalse(self.out.has_photo_been_shown_recently('Photo 1'))
        self.assertTrue(self.out.has_photo_been_shown_recently('Photo 5'))
        self.assertTrue(self.out.has_photo_been_shown_recently('Photo 6'))

    def setUp(self):
        self.out = PhotoHistory(5)