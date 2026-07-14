from imagepathloader import ImagePathLoader
from randomiser import Randomiser
from imagedisplay import ImageDisplay
from ini_file_loader import IniFileLoader

class PhotoFrameApp:
    def __init__(self, display):
        self.display = display

    def run(self):
        print("Run the application")
        ini_file_name = "config.ini"
        ini_file = IniFileLoader(ini_file_name)
        image_path_loader = ImagePathLoader(ini_file.get("image_directory"))
        image_paths = image_path_loader.load_image_paths()
        randomiser = Randomiser()
        randomised_image_paths = randomiser.randomise(image_paths)
        image_display = ImageDisplay(self.display)
        image_display.display_images(randomised_image_paths)