from pathlib import Path
import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from synchroniser.src.photo_folders_filterer import PhotoFoldersFilterer


class TestPhotoFolderFilterer(unittest.TestCase):
    def test_non_matching_folders_are_removed(self):

        filtered = self.out.filter_photo_sets(
            [['Match 1','url 1'],
             ['Set 2','url 2'],
             ['Match 3','url 3']])

        self.assertEqual(
            filtered,
            [['Match 1','url 1'],
             ['Match 3','url 3']]
        )

    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.system_operations.listdir.return_value = [
            'folder 1', 'folder 2', 'folder 3'
        ]
        self.out = PhotoFoldersFilterer(
            self.system_operations,
            'Match')
