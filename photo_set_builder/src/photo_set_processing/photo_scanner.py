from pathlib import Path
from photo_set_builder.src.data.photo_entry import PhotoEntry


class PhotoScanner:
    def __init__(self, system_operations, excluded_folder):
        self._system_operations = system_operations
        self._excluded_folder = excluded_folder

    def scan(self, photo_set_path):
        return [photo for photo in self._scan(photo_set_path, '')]

    def _scan(self, photo_set_path, relative_path):
        for item in photo_set_path.iterdir():
            if item.is_dir():
                if item.name != self._excluded_folder:
                    relative_path += item.name + '_'
                    yield from self._scan(item, relative_path)
            elif item.is_file():
                yield PhotoEntry(item, relative_path, relative_path + item.name)