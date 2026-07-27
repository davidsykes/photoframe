from pathlib import Path


class Sandbox:
    def __init__(self, root: Path):
        self.root = Path(root)

    def get_version_zip_path(self, version_name):
        return self.root / f"{version_name}.zip"

    def get_unzip_folder(self, version_name):
        return self.root / f"{version_name}_unzip"

    def get_version_folder(self, version_name):
        return self.root / f"{version_name}"


###############################
    @property
    def manifest(self) -> Path:
        return self.root / "manifest.json"
