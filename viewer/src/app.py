from viewer.src.imagepathloader import ImagePathLoader
from viewer.src.randomiser import Randomiser
from viewer.src.imagedisplay import ImageDisplay
from common.src.config_file_loader import ConfigFileLoader
from common.src.system_operations import SystemOperations

class PhotoFrameApp:
    def __init__(self, display):
        self.display = display

    def run(self):
        ini_file_name = "config.ini"
        system_operations = SystemOperations()
        config_file = ConfigFileLoader(system_operations, ini_file_name)
        image_path_loader = ImagePathLoader(config_file.get("image_directory"))
        image_paths = image_path_loader.load_image_paths()
        randomiser = Randomiser()
        randomised_image_paths = randomiser.randomise(image_paths)
        image_display = ImageDisplay(self.display)
        image_display.display_images(randomised_image_paths)