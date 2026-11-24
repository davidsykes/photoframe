
from common.src.whole_project_configuration import WholeProjectConfiguration
from synchroniser.src.photo_collections.photo_collections import PhotoCollections
from synchroniser.src.photo_folders_remover import PhotoFoldersRemover
from synchroniser.src.photo_folders_synchroniser import PhotoFoldersSynchroniser
from synchroniser.src.remote_config_loader import RemoteConfigLoader


class SynchroniserApp:
    def __init__(self,
                 whole_project_config:WholeProjectConfiguration,
                 remote_config_loader:RemoteConfigLoader,
                 photo_collections:PhotoCollections,
                 photo_folders_synchroniser:PhotoFoldersSynchroniser,
                 photo_folders_remover:PhotoFoldersRemover,
                 photo_folders_filter:str):
        self._whole_project_config = whole_project_config
        self._remote_config_loader = remote_config_loader
        self._photo_collections = photo_collections
        self._photo_folders_synchroniser = photo_folders_synchroniser
        self._photo_folders_remover = photo_folders_remover
        self._photo_folders_filter = photo_folders_filter

    def sync(self):
        remote_config_url = self._whole_project_config.remote_config_url
        remote_config = self._remote_config_loader.load_config(
            remote_config_url
        )
        unfiltered_photo_folders_raw = remote_config.get('photo_folders')
        self._photo_collections.initialise(unfiltered_photo_folders_raw)
        self._photo_collections.list('Unfiltered photo folders')
        self._photo_collections.filter_photo_sets(self._photo_folders_filter)
        self._photo_collections.list('Filtered photo folders')
        self._photo_folders_synchroniser.sync_folders(self._photo_collections)
        self._photo_folders_remover.remove_unreferenced_folders(
            self._photo_collections
        )