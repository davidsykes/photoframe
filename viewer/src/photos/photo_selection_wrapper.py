from viewer.src.logic.random_monitor import RandomMonitor
from viewer.src.photos.old.next_image_selector import NextImageSelectorOld
from viewer.src.photos.old.randomiser import RandomiserOld
from viewer.src.photos.photo_selection.next_photo_selector import NextPhotoSelector
from viewer.src.photos.photo_selection.photo_from_photo_set_selector import PhotoFromPhotoSetSelector
from viewer.src.photos.photo_selection.photo_from_photo_set_selector_non_repeating import PhotoFromPhotoSetSelectorNonRepeating
from viewer.src.photos.photo_selection.photo_set_selector import PhotoSetSelector
from viewer.src.photos.photo_selection.photo_set_selector_non_repeating import PhotoSetSelectorNonRepeating
from viewer.src.photos.photo_selection.randomiser import Randomiser
from viewer.src.photos.photo_set_date_retriever import PhotoSetDateRetriever
from viewer.src.photos.photo_set_loader import PhotoSetLoader
from viewer.src.photos.photo_sets_loader import PhotoSetsLoader
from viewer.src.photos.random_weighter import RandomWeighter


class PhotoSelectionWrapper:
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
        random_monitor = RandomMonitor()
        photo_set_selector = PhotoSetSelector(randomiser, photo_sets, random_monitor)
        photo_set_selector_non_repeating = PhotoSetSelectorNonRepeating(photo_set_selector, 3, 50)
        photo_from_photo_set_selector = PhotoFromPhotoSetSelector(randomiser, random_monitor)
        photo_from_photo_set_selector_non_repeating = PhotoFromPhotoSetSelectorNonRepeating(photo_from_photo_set_selector, 50, 100)
        self.next_photo_selector = NextPhotoSelector(
            photo_set_selector_non_repeating,
            photo_from_photo_set_selector_non_repeating
        )

    def _initialise_old_version(self):
        randomiser = RandomiserOld()
        self.next_image_selector = NextImageSelectorOld(randomiser)

    def select_next_photo(self):
        return self.next_photo_selector.select_next_photo()

    def set_images(self, image_paths):
        if not self.is_new_version:
            self.next_image_selector.set_images(image_paths)