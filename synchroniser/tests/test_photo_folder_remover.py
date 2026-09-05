from pathlib import Path
import unittest
from unittest.mock import Mock

from common.src.system_operations import SystemOperations
from synchroniser.src.photo_collections.photo_collections import PhotoCollections
from synchroniser.src.photo_folders_remover import PhotoFoldersRemover
from synchroniser.src.photo_collections.photo_collection import PhotoCollection

class TestPhotoFolderSynchroniser(unittest.TestCase):
    def test_unreferenced_folders_are_removed(self):
        collections = PhotoCollections()
        collections.initialise(
            [['folder 1','url 1'], ['folder 3','url 3']]
        )
        self.out.remove_unreferenced_folders(collections)

        self.system_operations.listdir.assert_called_once_with(
            Path('images folder')
        )
        self.system_operations.rmtree.assert_called_once_with(
            Path('images folder') / 'folder 2'
        )

    def setUp(self):
        self.system_operations = Mock(spec=SystemOperations)
        self.system_operations.listdir.return_value = [
            'folder 1', 'folder 2', 'folder 3'
        ]
        self.out = PhotoFoldersRemover(
            self.system_operations,
            'images folder')
