from viewer.src.images.old.next_image_selector import NextImageSelectorOld
from viewer.src.images.old.randomiser import Randomiser


class ImageSelectionWrapper:
    def __init__(self,
                 is_new_version):
        is_new_version = False

        if (is_new_version):
            self._initialise_new_version()
        else:
            self._initialise_old_version()

    def _initialise_new_version(self):
        pass

    def _initialise_old_version(self):
        randomiser = Randomiser()
        self.next_image_selector = NextImageSelectorOld(randomiser)

    def select_next_image(self):
        return self.next_image_selector.select_next_image()

    def set_images(self, image_paths):
        self.next_image_selector.set_images(image_paths)