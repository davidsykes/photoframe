from photo_set_builder.src.data.photo_entry import PhotoEntry


class PhotoScanner:
    INCLUDED_EXTENSIONS = {
        '.jpg',
        '.jpeg',
        '.png',
    }
    EXCLUDED_EXTENSIONS = {
        '.json',
        '.zip'
    }

    def __init__(self, system_operations, excluded_folder):
        self._system_operations = system_operations
        self._excluded_folder = excluded_folder

    def scan(self, photo_set_path):
        return list(self._scan(photo_set_path, ''))

    def _scan(self, photo_set_path, relative_path):
        for item in photo_set_path.iterdir():
            if item.is_dir():
                if item.name != self._excluded_folder:
                    child_relative_path = (
                        relative_path + item.name + '_'
                    )

                    yield from self._scan(
                        item,
                        child_relative_path,
                    )
            elif item.is_file():
                if item.suffix.lower() in self.INCLUDED_EXTENSIONS:
                    yield PhotoEntry(
                        item,
                        relative_path + item.name,
                    )
                elif item.suffix.lower() not in self.EXCLUDED_EXTENSIONS:
                    print(f'Exclude file from photo scan {item}')