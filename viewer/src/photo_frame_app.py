from enum import Enum, auto

from common.src.config_file_updater import ConfigFileUpdater
from common.src.remote_files_retriever import RemoteFilesRetriever
from common.src.config_file_loader import ConfigFileLoader
from common.src.whole_project_configuration import WholeProjectConfiguration
from viewer.src.cycle_stop_detector import CycleStopDetector
from viewer.src.images.image_loader import ImageLoader
from viewer.src.images.image_provider import ImageProvider
from viewer.src.main.main_loop import MainLoop
from viewer.src.menus.event_handler import EventHandler
from viewer.src.menus.events_handler import EventsHandler
from viewer.src.images.image_path_loader import ImagePathLoader
from viewer.src.menus.main_menu import MainMenu
from viewer.src.menus.menu_handler import MenuHandler
from viewer.src.new_app_or_new_photos_detector import NewAppOrNewPhotosDetector
from viewer.src.images.next_image_selector import NextImageSelector
from viewer.src.randomiser import Randomiser
from viewer.src.remote_config_version_loader import RemoteConfigVersionLoader
from viewer.src.sleep_decider import SleepDecider
from viewer.src.status.application_status import ApplicationStatus
from viewer.src.action_timer import ActionTimer
from viewer.src.status.version_loader import VersionLoader
from viewer.src.viewer_exit_exception import ViewerExitException

class DisplayType(Enum):
    PC_TEST_VERSION = auto()
    PI_DISPLAY_VERSION = auto()
    
class PhotoFrameApp:
    def __init__(self, display_type):
        self._display_type = display_type

    def run(self, system_operations, PROJECT_ROOT):
        config_file_loader = ConfigFileLoader(system_operations)
        whole_project_configuration = WholeProjectConfiguration(
            config_file_loader
        )
        viewer_config_file_name = "viewer/viewer_config.json"
        viewer_configuration = config_file_loader.load_config_file(viewer_config_file_name)
        if viewer_configuration is None:
            return 1
        images_folder = whole_project_configuration.images_folder
        image_path_loader = ImagePathLoader(images_folder)
        sleep_time_seconds = whole_project_configuration.sleep_time_seconds
        randomiser = Randomiser()
        next_image_selector = NextImageSelector(randomiser)
        remote_config_url = whole_project_configuration.remote_config_url
        remote_files_retriever = RemoteFilesRetriever(system_operations)
        config_file_updater = ConfigFileUpdater(
            remote_files_retriever,
            config_file_loader,
            system_operations)
        status_updater = ApplicationStatus()
        status_updater.update_status('Filter', whole_project_configuration.photo_set_filter)
        VersionLoader(system_operations, status_updater)\
            .load_version_details(PROJECT_ROOT / 'VERSION')
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
            'Remote update',
            system_operations,
            new_app_or_new_photos_detector.poll,
            time_between_version_checks_seconds)
        cycle_stop_detector = CycleStopDetector(
            [timed_new_app_or_new_photos_detector]
        )

        display = None
        if self._display_type == DisplayType.PC_TEST_VERSION:
            from viewer.src.display.pcdisplay import PCSystemDisplay
            from viewer.src.menus.events_emulator import EventsEmulator
            events = EventsEmulator(system_operations)
            display = PCSystemDisplay(events)
        elif self._display_type == DisplayType.PI_DISPLAY_VERSION:
            from viewer.src.display.pidisplay import PiSystemDisplay
            display = PiSystemDisplay(system_operations, status_updater, whole_project_configuration.hide_mouse)
        else:
            raise ValueError(f"Unknown display type: {self._display_type}")
        display.initialise_display()

        next_image_timer = ActionTimer(
            'Image change',
            system_operations,
            next_image_selector.select_next_image,
            sleep_time_seconds
        )
        sleep_decider = SleepDecider()
        main_menu = MainMenu(
            status_updater,
            next_image_timer,
            sleep_decider)
        menu_handler = MenuHandler(main_menu)
        event_handler = EventHandler(menu_handler)
        events_handler = EventsHandler(display, event_handler)
        image_paths = image_path_loader.load_image_paths(status_updater)
        next_image_selector.set_images(image_paths)
        image_loader = ImageLoader(display)
        image_provider = ImageProvider(
            next_image_timer,
            image_loader,
            sleep_decider)
        main_loop = MainLoop(
            cycle_stop_detector,
            next_image_timer,
            image_provider,
            display,
            events_handler,
            menu_handler)
        main_loop.loop()
        
