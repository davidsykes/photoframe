from dataclasses import dataclass
from pathlib import Path

from common.src.config_file import ConfigFile


@dataclass()
class PhotoSetDefinition:
    name: str
    photo_set_path: Path
    configuration: ConfigFile
    photo_set_has_changed: bool = False
