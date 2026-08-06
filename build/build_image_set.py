import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import hashlib
import json


PROJECT_ROOT = Path(__file__).resolve().parent
OUTPUT_FOLDER = PROJECT_ROOT / "images"

EXCLUDED_FOLDER_NAMES = {
    "__pycache__",
    "tests",
    ".git",
    ".idea",
    ".vscode",
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


def add_folder(
    archive: ZipFile,
    source_folder: Path
) -> int:
    file_count = 0
    for path in source_folder.rglob("*"):
        if not should_include(path):
            continue

        relative_path = path.relative_to(source_folder)
        archive_path = relative_path

        archive.write(path, archive_path.as_posix())
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

    release_metadata = {
        "manifest_version": 1,
        "viewer_version": version,
    }

    with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as archive:
        file_count = add_folder(
            archive,
            set_path
        )

        #archive.writestr("VERSION", version + "\n")
        #archive.writestr(
        #    "release.json",
        #    json.dumps(release_metadata, indent=2),
        #)

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