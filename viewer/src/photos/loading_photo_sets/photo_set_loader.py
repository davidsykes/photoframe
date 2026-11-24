from datetime import date
from pathlib import Path

from common.src.system_operations import SystemOperations
from viewer.src.data.photo_set import PhotoSet
from viewer.src.photos.loading_photo_sets.random_weighter import RandomWeighter
from viewer.src.status.application_status import ApplicationStatus


class PhotoSetLoader:
    def __init__(self,
                 system_operations:SystemOperations,
                 random_weighter:RandomWeighter,
                 status_updater:ApplicationStatus,
                 excluded_extensions:set[str]):
        self._system_operations = system_operations
        self._random_weighter = random_weighter
        self._status_updater = status_updater
        self._excluded_extensions = excluded_extensions

    def load_photo_set(self,
                       photo_set_path : Path,
                       photo_set_date:date):
        name = photo_set_path.name
        images = self._system_operations.list_files_recursive(
            photo_set_path,
            self._excluded_extensions)
        weight = self._random_weighter.weigh(photo_set_date)
        photo_set = PhotoSet(name, images, weight)
        self._status_updater.update_status(
            f'Photo set {name}', f'{len(images)} photos')
        return photo_set