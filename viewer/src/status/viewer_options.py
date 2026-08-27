from dataclasses import dataclass
from pathlib import Path


@dataclass
class ViewerOptions:
    #fullscreen: bool = True
    show_image_names: bool = False
    #image_duration: float = 20.0
    this_location: Path = Path('images')