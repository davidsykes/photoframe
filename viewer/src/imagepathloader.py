from pathlib import Path

class ImagePathLoader:
    def __init__(self, image_directory):
        self.image_directory = image_directory
        self.excluded_extensions = {'.json', '.txt'}

    def load_image_paths(self):
        print(f"Loading image paths from directory: {self.image_directory}")
        image_paths = self._list_files_recursive(self.image_directory)
        print(f"Found {len(image_paths)} image paths.")
        print(f"Image paths: {image_paths}")
        return image_paths

    def _list_files_recursive(self, path):
        return [
            str(path)
            for path in Path(self.image_directory).rglob("*")
            if path.is_file()
            and path.suffix.lower() not in self.excluded_extensions
        ]
