from pathlib import Path
import unittest
from unittest.mock import Mock, call

from synchroniser.src.photo_folder_synchroniser import PhotoFolderSynchroniser
from synchroniser.src.photo_folders_synchroniser import PhotoFoldersSynchroniser


class TestPhotoFoldersSynchroniser(unittest.TestCase):
    def test_all_folders_are_synchronised(self):
        self.out.sync_folders([['one'],['two']])

        self.photo_folder_synchroniser.sync_folder.assert_has_calls(
            [call(['one']),call(['two'])]
        )

    def setUp(self):
        self.photo_folder_synchroniser = Mock(spec=PhotoFolderSynchroniser)
        self.out = PhotoFoldersSynchroniser(
            self.photo_folder_synchroniser
        )
