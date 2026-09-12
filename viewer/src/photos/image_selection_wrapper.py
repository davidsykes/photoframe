

from viewer.src.photos.old.next_image_selector import NextImageSelectorOld
from viewer.src.photos.old.randomiser import RandomiserOld
from viewer.src.photos.photo_selection.next_image_selector import NextImageSelector
from viewer.src.photos.photo_set_date_retriever import PhotoSetDateRetriever
from viewer.src.photos.photo_set_loader import PhotoSetLoader
from viewer.src.photos.photo_sets_loader import PhotoSetsLoader
from viewer.src.photos.random_weighter import RandomWeighter
from viewer.src.photos.randomiser import Randomiser


class ImageSelectionWrapper:
    def __init__(self,
                 is_new_version,
                 remote_config_data,
                 path_to_photo_sets,
                 system_operations):
        #is_new_version = False

        self.is_new_version = is_new_version
        if (is_new_version):
            self._initialise_new_version(
                remote_config_data,
                path_to_photo_sets,
                system_operations)
        else:
            self._initialise_old_version()

    def _initialise_new_version(self,
                                remote_config_data,
                                path_to_photo_sets,
                                system_operations):
        random_weighter = RandomWeighter()
        photo_set_loader = PhotoSetLoader(system_operations,
                                          random_weighter,
                                          {'.json', '.txt'})
        photo_set_date_retriever = PhotoSetDateRetriever()
        photo_sets_loader = PhotoSetsLoader(
            system_operations,
            photo_set_loader,
            photo_set_date_retriever
        )
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