from viewer.src.imagepathloader import ImagePathLoader
from viewer.src.randomiser import Randomiser
from viewer.src.imagedisplay import ImageDisplay
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
        image_paths = image_path_loader.load_image_paths()
        randomiser = Randomiser()
        randomised_image_paths = randomiser.randomise(image_paths)
        self.display.initialise()
        image_display = ImageDisplay(self.display)
        image_display.display_images(randomised_image_paths)