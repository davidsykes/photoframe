import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import hashlib
import json


BUILDER_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = BUILDER_ROOT.parent
OUTPUT_FOLDER = PROJECT_ROOT / "releases"

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
    source_folder: Path,
    archive_root: Path,
) -> None:
    for path in source_folder.rglob("*"):
        if not should_include(path):
            continue

        relative_path = path.relative_to(source_folder)
        archive_path = archive_root / relative_path

        archive.write(path, archive_path.as_posix())


def calculate_sha256(path: Path) -> str:
    digest = hashlib.sha256()

    with path.open("rb") as file:
        for block in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(block)

    return digest.hexdigest()


def build_release(version: str) -> Path:
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    zip_path = OUTPUT_FOLDER / f"photoframe-{version}.zip"

    release_metadata = {
        "manifest_version": 1,
        "photoframe_version": version,
    }

    with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as archive:
        add_folder(
            archive,
            PROJECT_ROOT / "updater",
            Path("updater"),
        )

        add_folder(
            archive,
            PROJECT_ROOT / "common",
            Path("common"),
        )

        add_folder(
            archive,
            PROJECT_ROOT / "release",
            Path("release"),
        )

        archive.writestr("VERSION", version + "\n")
        archive.writestr(
            "release.json",
            json.dumps(release_metadata, indent=2),
        )

    print(f"Created: {zip_path}")
    print(f"SHA-256: {calculate_sha256(zip_path)}")

    return zip_path


if __name__ == "__main__":
    if len(sys.argv) == 2:
        release = sys.argv[1]
        build_release(release)
    else:
        print("Release version missing")