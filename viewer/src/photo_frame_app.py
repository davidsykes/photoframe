from enum import Enum, auto

from common.src.config_file_updater import ConfigFileUpdater
from common.src.remote_files_retriever import RemoteFilesRetriever
from common.src.config_file_loader import ConfigFileLoader
from viewer.src.cycle_stop_detector import CycleStopDetector
from viewer.src.events.event_handler import EventHandler
from viewer.src.events.events_handler import EventsHandler
from viewer.src.imagepathloader import ImagePathLoader
from viewer.src.new_app_or_new_photos_detector import NewAppOrNewPhotosDetector
from viewer.src.next_image_selector import NextImageSelector
from viewer.src.randomiser import Randomiser
from viewer.src.image_cycler import ImageCycler
from viewer.src.remote_config_version_loader import RemoteConfigVersionLoader
from viewer.src.sleeper import Sleeper
from viewer.src.status_updater import StatusUpdater
from viewer.src.action_timer import ActionTimer

class DisplayType(Enum):
    PC_TEST_VERSION = auto()
    PI_DISPLAY_VERSION = auto()
    
class PhotoFrameApp:
    def __init__(self, display_type):
        self._display_type = display_type

    def run(self, system_operations, PROJECT_ROOT):
        config_file_loader = ConfigFileLoader(system_operations)
        whole_project_config_file_name = "project_config.json"
        whole_project_configuration = config_file_loader.load_config_file(whole_project_config_file_name)
        viewer_config_file_name = "viewer/viewer_config.json"
        viewer_configuration = config_file_loader.load_config_file(viewer_config_file_name)
        if viewer_configuration is None:
            return 1
        image_path_path = whole_project_configuration.get("images_folder")
        image_path_loader = ImagePathLoader(image_path_path)
        sleep_time_seconds = whole_project_configuration.get("sleep_time_seconds")
        randomiser = Randomiser()
        next_image_selector = NextImageSelector(randomiser)
        remote_config_url = whole_project_configuration.get("remote_config_url")
        remote_files_retriever = RemoteFilesRetriever(system_operations)
        config_file_updater = ConfigFileUpdater(
            remote_files_retriever,
            config_file_loader,
            system_operations)
        status_updater = StatusUpdater()
        remote_config_version_loader = RemoteConfigVersionLoader(
            config_file_updater,
            config_file_loader,
            status_updater,
            remote_config_url,
            PROJECT_ROOT / 'remote_viewer_config.json',
            )
        new_app_or_new_photos_detector = NewAppOrNewPhotosDetector(
            remote_config_version_loader
        )
        time_between_version_checks_seconds = viewer_configuration.get(
            "time_between_version_checks_seconds")
        timed_new_app_or_new_photos_detector = ActionTimer(
            system_operations,
            new_app_or_new_photos_detector.poll,
            time_between_version_checks_seconds)
        cycle_stop_detector = CycleStopDetector(
            [timed_new_app_or_new_photos_detector]
        )

        display = None
        if self._display_type == DisplayType.PC_TEST_VERSION:
            from viewer.src.display.pcdisplay import PCSystemDisplay
            display = PCSystemDisplay()
        elif self._display_type == DisplayType.PI_DISPLAY_VERSION:
            from viewer.src.display.pidisplay import PiSystemDisplay
            display = PiSystemDisplay(system_operations)
        else:
            raise ValueError(f"Unknown display type: {self._display_type}")
        display.initialise()

        event_handler = EventHandler()
        events_handler = EventsHandler(event_handler)
        sleeper = Sleeper(
            system_operations,
            display,
            events_handler,
            sleep_time_seconds)
        image_cycler = ImageCycler(
            next_image_selector,
            cycle_stop_detector,
            display,
            sleeper)
        image_paths = image_path_loader.load_image_paths()
        next_image_selector.set_images(image_paths)
        image_cycler.cycle_images()
        
