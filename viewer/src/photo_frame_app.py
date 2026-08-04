from viewer.src.cycle_stop_detector import CycleStopDetector
from viewer.src.imagepathloader import ImagePathLoader
from viewer.src.next_image_selector import NextImageSelector
from viewer.src.randomiser import Randomiser
from viewer.src.image_cycler import ImageCycler
from common.src.config_file_loader import ConfigFileLoader
from common.src.system_operations import SystemOperations

class PhotoFrameApp:
    def __init__(self, display):
        self.display = display

    def run(self):
        ini_file_name = "project_config.json"
        system_operations = SystemOperations()
        system_operations.set_logger('viewer', '..')
        config_file_loader = ConfigFileLoader(system_operations)
        config_file = config_file_loader.load_config_file(ini_file_name)
        image_path_loader = ImagePathLoader(config_file.get("images_folder"))
        randomiser = Randomiser()
        next_image_selector = NextImageSelector(randomiser)
        cycle_stop_detector = CycleStopDetector()
        image_cycler = ImageCycler(
            system_operations,
            next_image_selector,
            cycle_stop_detector,
            self.display)
        self.display.initialise()
        image_paths = image_path_loader.load_image_paths()
        next_image_selector.set_images(image_paths)
        image_cycler.cycle_images()
        
