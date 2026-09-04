import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import hashlib

from process_image import prepare_photo


BUILDER_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = BUILDER_ROOT.parent
OUTPUT_FOLDER = PROJECT_ROOT.parent / "releases"

EXCLUDED_FOLDER_NAMES = {
    "__pycache__",
    "tests",
    ".git",
    ".idea",
    ".vscode",
    "resized"
}

EXCLUDED_SUFFIXES = {
    ".pyc",
    ".pyo",
}


def should_include(path: Path) -> bool:
    if any(part in EXCLUDED_FOLDER_NAMES for part in path.parts):
        return False

    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False

    return path.is_file()

def resize_photo(path: Path) -> Path:
    photos_folder = path.parent
    resized_folder = photos_folder / "resized"
    resized_folder.mkdir(exist_ok=True)

    resized_path = resized_folder / path.name
    if not resized_path.exists():
        print(f'Compressing path from {path} to {resized_path}')
        prepare_photo(path, resized_path)
    return resized_path

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

        resized_path = resize_photo(path)

        #photos_folder = path.parent
        #resized_path = photos_folder / "resized" / path.name
        #prepare_photo(path, resized_path)
        print(f'Adding file: {resized_path} as {archive_path}')
        archive.write(resized_path, archive_path.as_posix())
        file_count += 1

    return file_count

def calculate_sha256(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as file:
        for block in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(block)

    return digest.hexdigest()


def build_release(version: str, set_path: Path) -> Path:
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    zip_path = OUTPUT_FOLDER / f"images-{version}.zip"
    print(f'Building release: {zip_path}')

    with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as archive:
        file_count = add_folder(
            archive,
            set_path
        )

    print(f"Created: {zip_path}")
    print(f"File count: {file_count}")
    print(f"SHA-256: {calculate_sha256(zip_path)}")

    return zip_path


if __name__ == "__main__":
    if len(sys.argv) == 3:
        set_name = sys.argv[1]
        set_path = Path(sys.argv[2])
        build_release(set_name, set_path)
    else:
        print("Useage: python build_image_set.py <set name> <set_path>")