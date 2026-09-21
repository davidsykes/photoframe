from viewer.src.logic.random_monitor import RandomMonitor
from viewer.src.photos.loading_photo_sets.photo_set_date_retriever import PhotoSetDateRetriever
from viewer.src.photos.loading_photo_sets.photo_set_loader import PhotoSetLoader
from viewer.src.photos.loading_photo_sets.photo_sets_loader import PhotoSetsLoader
from viewer.src.photos.loading_photo_sets.random_weighter import RandomWeighter
from viewer.src.photos.random_photo_selection_old.photo_from_photo_set_selector import PhotoFromPhotoSetSelector
from viewer.src.photos.random_photo_selection_old.photo_from_photo_set_selector_non_repeating import PhotoFromPhotoSetSelectorNonRepeating
from viewer.src.photos.random_photo_selection_old.photo_set_selector import PhotoSetSelector
from viewer.src.photos.random_photo_selection_old.photo_set_selector_non_repeating import PhotoSetSelectorNonRepeating
from viewer.src.photos.random_photo_selection_old.random_photo_selector import RandomPhotoSelector

class PhotoSelectionWrapper:
    def __init__(self,
                 remote_config_data,
                 path_to_photo_sets,
                 system_operations,
                 randomiser):
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
        self.random_monitor = RandomMonitor(photo_sets)
        photo_set_selector = PhotoSetSelector(randomiser, photo_sets, self.random_monitor)
        photo_set_selector_non_repeating = PhotoSetSelectorNonRepeating(photo_set_selector, 3, 50)
        photo_from_photo_set_selector = PhotoFromPhotoSetSelector(randomiser, self.random_monitor)
        photo_from_photo_set_selector_non_repeating = PhotoFromPhotoSetSelectorNonRepeating(photo_from_photo_set_selector, 50, 100)
        self.next_photo_selector = RandomPhotoSelector(
            photo_set_selector_non_repeating,
            photo_from_photo_set_selector_non_repeating,
            self.random_monitor
        )

    def select_random_photo(self):
        return self.next_photo_selector.select_random_photo()