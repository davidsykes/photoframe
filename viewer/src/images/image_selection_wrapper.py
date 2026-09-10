from viewer.src.images.next_image_selector import NextImageSelector
from viewer.src.images.old.next_image_selector import NextImageSelectorOld
from viewer.src.images.old.randomiser import RandomiserOld
from viewer.src.images.photo_sets_loader import PhotoSetsLoader
from viewer.src.images.randomiser import Randomiser


class ImageSelectionWrapper:
    def __init__(self,
                 is_new_version,
                 remote_config_data,
                 path_to_photo_sets):
        #is_new_version = False

        self.is_new_version = is_new_version
        if (is_new_version):
            self._initialise_new_version(
                remote_config_data,
                path_to_photo_sets)
        else:
            self._initialise_old_version()

    def _initialise_new_version(self,
                                remote_config_data,
                                path_to_photo_sets):
        photo_sets_loader = PhotoSetsLoader()
        photo_sets = photo_sets_loader.load_photo_sets(
            remote_config_data,
            path_to_photo_sets)
        randomiser = Randomiser()
        self.next_image_selector = NextImageSelector(
            randomiser,
            photo_sets
        )

    def _initialise_old_version(self):
        randomiser = RandomiserOld()
        self.next_image_selector = NextImageSelectorOld(randomiser)

    def select_next_image(self):
        return self.next_image_selector.select_next_image()

    def set_images(self, image_paths):
        if not self.is_new_version:
            self.next_image_selector.set_images(image_paths)