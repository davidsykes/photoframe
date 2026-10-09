from dataclasses import dataclass
from pathlib import Path
from photo_set_builder.src.data.photo_set_configuration import PhotoSetConfiguration


@dataclass()
class PhotoSetDefinition:
    name: str
    photo_set_path: Path
    config: PhotoSetConfiguration
    photo_set_has_changed: bool = False
