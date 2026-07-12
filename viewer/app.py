from imagepathloader import ImagePathLoader
from randomiser import Randomiser
from imagedisplay import ImageDisplay

class PhotoFrameApp:
    def __init__(self, display):
        self.display = display

    def run(self):
        print("Run the application")
        image_path_loader = ImagePathLoader()
        image_paths = image_path_loader.load_image_paths()
        randomiser = Randomiser()
        randomised_image_paths = randomiser.randomise(image_paths)
        image_display = ImageDisplay(self.display)
        image_display.display_images(randomised_image_paths)