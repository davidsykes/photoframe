from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import hashlib

# BUILDER_ROOT = Path(__file__).resolve().parent
# PROJECT_ROOT = BUILDER_ROOT.parent
# OUTPUT_FOLDER = PROJECT_ROOT.parent / "releases"

EXCLUDED_FOLDER_NAMES = {
    "__pycache__",
    "tests",
    ".git",
    ".idea",
    ".vscode"
}

EXCLUDED_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".zip"
}

def should_include(path: Path) -> bool:
    if any(part in EXCLUDED_FOLDER_NAMES for part in path.parts):
        return False

    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False

    return path.is_file()

def add_folder(
    archive: ZipFile,
    source_folder: Path
) -> int:
    file_count = 0
    for path in source_folder.rglob("*"):
        if not should_include(path):
            print(f'Excluding file: {path}')
            continue

        relative_path = path.relative_to(source_folder)
        archive_path = relative_path

        print(f'Adding file: {path} as {archive_path}')
        archive.write(path, archive_path.as_posix())
        file_count += 1

    return file_count

def calculate_sha256(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as file:
        for block in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(block)

    return digest.hexdigest()


def build_photo_set_zip(photo_set_name: str, set_path: Path) -> Path:
    zip_path = set_path / f"{photo_set_name}.zip"
    print(f'Building image zip: {zip_path}')

    with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as archive:
        file_count = add_folder(
            archive,
            set_path
        )

    print(f"Created: {zip_path}")
    print(f"File count: {file_count}")
    print(f"SHA-256: {calculate_sha256(zip_path)}")

    return zip_path


class ZipperImplementation:
    def zip(self, photo_set_name, zip_files_path):
        build_photo_set_zip(photo_set_name, zip_files_path)
