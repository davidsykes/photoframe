from enum import Enum, auto

from common.src.config_file_updater import ConfigFileUpdater
from common.src.remote_files_retriever import RemoteFilesRetriever
from common.src.config_file_loader import ConfigFileLoader
from common.src.whole_project_configuration import WholeProjectConfiguration
from viewer.src.awake_periods.awake_decider import AwakeDecider
from viewer.src.awake_periods.awake_schedule import AwakeSchedule
from viewer.src.cycle_stop_detector import CycleStopDetector
from viewer.src.display.display_controller import DisplayController
from viewer.src.display.subprocess_wrapper import SubprocessWrapper
from viewer.src.display.wlopm_commands import WlopmCommands
from viewer.src.display.wlr_randr_commands import WlrRandrCommands
from viewer.src.images.image_selection_wrapper import ImageSelectionWrapper
from viewer.src.images.old.image_loader import ImageLoader
from viewer.src.images.old.image_provider import ImageProvider
from viewer.src.main.main_loop import MainLoop
from viewer.src.menus.event_handler import EventHandler
from viewer.src.menus.events_handler import EventsHandler
from viewer.src.images.old.image_path_loader import ImagePathLoader
from viewer.src.menus.main_menu import MainMenu
from viewer.src.menus.menu_handler import MenuHandler
from viewer.src.new_app_or_new_photos_detector import NewAppOrNewPhotosDetector
from viewer.src.data.remote_config_data_loader import RemoteConfigDataLoader
from viewer.src.status.action_status_updater import ActionStatusUpdater
from viewer.src.status.application_status import ApplicationStatus
from viewer.src.action_timer import ActionTimer
from viewer.src.status.version_loader import VersionLoader

class DisplayType(Enum):
    PC_TEST_VERSION = auto()
    PI_DISPLAY_VERSION = auto()

class PhotoFrameApp:
    def __init__(self, command_line_options):
        self._command_line_options = command_line_options

    def run(self, system_operations, PROJECT_ROOT):
        print(f"Running PhotoFrameApp from: {PROJECT_ROOT}")
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
        image_display_seconds = whole_project_configuration.image_display_seconds
        remote_config_url = whole_project_configuration.remote_config_url
        remote_files_retriever = RemoteFilesRetriever(system_operations)
        status_updater = ApplicationStatus()
        action_status_updater = ActionStatusUpdater(
            'Download remote config', system_operations, status_updater)
        config_file_updater = ConfigFileUpdater(
            remote_files_retriever,
            config_file_loader,
            system_operations,
            action_status_updater)
        status_updater.update_status('Filter', whole_project_configuration.photo_set_filter)
        VersionLoader(system_operations, status_updater)\
            .load_version_details(PROJECT_ROOT / 'VERSION')
        remote_config_version_loader = RemoteConfigDataLoader(
            config_file_updater,
            config_file_loader,
            status_updater,
            remote_config_url,
            PROJECT_ROOT / 'remote_viewer_config.json',
            )
        initial_remote_config_data = remote_config_version_loader.get_config_data()
        new_app_or_new_photos_detector = NewAppOrNewPhotosDetector(
            remote_config_version_loader,
            system_operations,
            initial_remote_config_data.version
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
        from viewer.src.logs_analyser import LogsAnalyser
        LogsAnalyser(system_operations,
                     PROJECT_ROOT,
                     status_updater,
                     whole_project_configuration.viewer_app_working_folder).analyse_logs()

        display = None
        if self._command_line_options.display_type == DisplayType.PC_TEST_VERSION:
            from viewer.src.display.pcdisplay import PCSystemDisplay
            from viewer.src.menus.events_emulator import EventsEmulator
            events = EventsEmulator(system_operations)
            display = PCSystemDisplay(events)
        elif self._command_line_options.display_type == DisplayType.PI_DISPLAY_VERSION:
            from viewer.src.display.pidisplay import PiSystemDisplay
            display = PiSystemDisplay(system_operations, status_updater, whole_project_configuration.hide_mouse)
        else:
            raise ValueError(f"Unknown display type: {self._display_type}")
        display.initialise_display()


        image_selection_wrapper = ImageSelectionWrapper(
            self._command_line_options.run_new_code,
            initial_remote_config_data
        )



        next_image_timer = ActionTimer(
            'Image change',
            system_operations,
            image_selection_wrapper.select_next_image,
            image_display_seconds
        )
        awake_schedule = AwakeSchedule(
            system_operations,
            whole_project_configuration.wake_time,
            whole_project_configuration.sleep_time,
            self._command_line_options.always_awake
        )
        subprocess_wrapper = SubprocessWrapper()
        subprocess_command_generator = WlrRandrCommands()
        subprocess_command_generator = WlopmCommands()
        display_controller = DisplayController(
            subprocess_wrapper,
            subprocess_command_generator,
            status_updater,
            system_operations,
            whole_project_configuration.display_off_enabled)
        display_controller.initialise()
        awake_decider = AwakeDecider(awake_schedule, display_controller)
        main_menu = MainMenu(
            status_updater,
            next_image_timer,
            awake_decider,
            display_controller
            )
        menu_handler = MenuHandler(main_menu, display_controller, system_operations)
        event_handler = EventHandler(menu_handler)
        events_handler = EventsHandler(display, event_handler)
        image_paths = image_path_loader.load_image_paths(status_updater)
        image_selection_wrapper.set_images(image_paths)
        image_loader = ImageLoader(display)
        image_provider = ImageProvider(
            next_image_timer,
            image_loader,
            awake_decider)
        main_loop = MainLoop(
            cycle_stop_detector,
            next_image_timer,
            image_provider,
            display,
            events_handler,
            menu_handler)
        try:
            main_loop.loop()
        finally:
            display_controller.display_on()
