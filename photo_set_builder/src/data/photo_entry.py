from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PhotoEntry:
    source_path: Path
    photo_name: str