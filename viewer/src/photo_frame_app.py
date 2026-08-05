from enum import Enum, auto

from viewer.src.cycle_stop_detector import CycleStopDetector
from viewer.src.imagepathloader import ImagePathLoader
from viewer.src.next_image_selector import NextImageSelector
from viewer.src.randomiser import Randomiser
from viewer.src.image_cycler import ImageCycler
from common.src.config_file_loader import ConfigFileLoader
from common.src.system_operations import SystemOperations


class DisplayType(Enum):
    PC_TEST_VERSION = auto()
    PI_DISPLAY_VERSION = auto()
    
class PhotoFrameApp:
    def __init__(self, display_type):
        self._display_type = display_type

    def run(self):
        ini_file_name = "project_config.json"
        system_operations = SystemOperations()
        system_operations.set_logger('viewer', '..')
        config_file_loader = ConfigFileLoader(system_operations)
        config_file = config_file_loader.load_config_file(ini_file_name)
        image_path_path = config_file.get("images_folder")
        image_path_loader = ImagePathLoader(image_path_path)
        sleep_time_seconds = config_file.get("sleep_time_seconds")
        randomiser = Randomiser()
        next_image_selector = NextImageSelector(randomiser)
        cycle_stop_detector = CycleStopDetector()

        display = None
        if self._display_type == DisplayType.PC_TEST_VERSION:
            from viewer.src.pcdisplay import PCSystemDisplay
            display = PCSystemDisplay()
        elif self._display_type == DisplayType.PI_DISPLAY_VERSION:
            from viewer.src.pidisplay import PiSystemDisplay
            display = PiSystemDisplay(system_operations)
        else:
            raise ValueError(f"Unknown display type: {self._display_type}")
        display.initialise()

        image_cycler = ImageCycler(
            next_image_selector,
            cycle_stop_detector,
            display,
            sleep_time_seconds)
        image_paths = image_path_loader.load_image_paths()
        next_image_selector.set_images(image_paths)
        image_cycler.cycle_images()
        
