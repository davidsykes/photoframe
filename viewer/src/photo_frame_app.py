from enum import Enum, auto
from pathlib import Path
from common.src.config_file_updater import ConfigFileUpdater
from common.src.remote_files_retriever import RemoteFilesRetriever
from common.src.config_file_loader import ConfigFileLoader
from common.src.whole_project_configuration import WholeProjectConfiguration
from viewer.src.awake_periods.awake_decider import AwakeDecider
from viewer.src.awake_periods.awake_schedule import AwakeSchedule
from viewer.src.cycle_stop_detector import CycleStopDetector
from viewer.src.display.display_on_off_controller import DisplayOnOffController
from viewer.src.display.image_provider import ImageProvider
from viewer.src.display.subprocess_wrapper import SubprocessWrapper
from viewer.src.display.wlopm_commands import WlopmCommands
from viewer.src.display.wlr_randr_commands import WlrRandrCommands
from viewer.src.logic.random_monitor import RandomMonitor
from viewer.src.main.main_loop import MainLoop
from viewer.src.menus.framework.event_handler import EventHandler
from viewer.src.menus.framework.events_handler import EventsHandler
from viewer.src.menus.definitions.first_menu import FirstMenu
from viewer.src.menus.definitions.debug_menu import DebugMenu
from viewer.src.menus.framework.menu_handler import MenuHandler
from viewer.src.new_app_or_new_photos_detector import NewAppOrNewPhotosDetector
from viewer.src.data.remote_config_data_loader import RemoteConfigDataLoader
from viewer.src.photos.historic_photo_chooser import HistoricPhotoChooser
from viewer.src.photos.loading_photo_sets.photo_set_date_retriever import PhotoSetDateRetriever
from viewer.src.photos.loading_photo_sets.photo_set_loader import PhotoSetLoader
from viewer.src.photos.loading_photo_sets.photo_sets_loader import PhotoSetsLoader
from viewer.src.photos.loading_photo_sets.random_weighter import RandomWeighter
from viewer.src.photos.photo_history import PhotoHistory
from viewer.src.photos.sequential_photos_new.next_photo_to_show_cache import NextPhotoToShowCache
from viewer.src.photos.sequential_photos_new.next_photo_to_show_generator import NextPhotoToShowGenerator
from viewer.src.photos.sequential_photos_new.photo_from_photo_set_selector import PhotoFromPhotoSetSelectorNew
from viewer.src.photos.sequential_photos_new.random_photo_selector_new import RandomPhotoSelectorNew
from viewer.src.photos.loading_photo_sets.image_from_file_loader import ImageFromFileLoader
from viewer.src.photos.photo_to_display_chooser import PhotoToDisplayChooser
from viewer.src.photos.sequential_photos_new.random_photo_set_selector import RandomPhotoSetSelector
from viewer.src.photos.sequential_photos_old.photo_selection_wrapper import PhotoSelectionWrapper
from viewer.src.photos.sequential_photos_old.sequential_photo_chooser import SequentialPhotoChooser
from viewer.src.status.action_status_updater import ActionStatusUpdater
from viewer.src.status.application_status import ApplicationStatus
from viewer.src.action_timer import ActionTimer
from viewer.src.status.version_loader import VersionLoader
from viewer.src.logic.randomiser import Randomiser

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
        images_folder = Path(whole_project_configuration.images_folder)
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
            from viewer.src.menus.framework.events_emulator import EventsEmulator
            events = EventsEmulator(system_operations)
            display = PCSystemDisplay(events)
        elif self._command_line_options.display_type == DisplayType.PI_DISPLAY_VERSION:
            from viewer.src.display.pidisplay import PiSystemDisplay
            display = PiSystemDisplay(system_operations, status_updater, whole_project_configuration.hide_mouse)
        else:
            raise ValueError(f"Unknown display type: {self._display_type}")
        display.initialise_display()

        photo_history = PhotoHistory(50)
        randomiser = Randomiser()

        ##########################

        run_new_code = not self._command_line_options.run_new_code

        status_updater.update_status('Running new photo selector', run_new_code)
        if run_new_code:
            photo_selection_wrapper = None
            next_image_timer = None
            sequential_photo_chooser = None



            photo_sets = self.load_photo_sets(system_operations,
                                              initial_remote_config_data,
                                              images_folder)

            random_monitor = RandomMonitor(photo_sets)

            sequential_photo_chooser = self.build_random_photo_selector_module(
                system_operations,
                image_display_seconds,
                randomiser,
                photo_sets,
                photo_history
            )
        else:
            photo_selection_wrapper = PhotoSelectionWrapper(
                initial_remote_config_data,
                images_folder,
                system_operations,
                randomiser
            )
            next_image_timer = ActionTimer(
                'Image change',
                system_operations,
                photo_selection_wrapper.select_random_photo,
                image_display_seconds
            )
            random_monitor = photo_selection_wrapper.random_monitor
            sequential_photo_chooser = SequentialPhotoChooser(
                next_image_timer,
                photo_history)


        ##############################


        awake_schedule = AwakeSchedule(
            system_operations,
            whole_project_configuration.wake_time,
            whole_project_configuration.sleep_time,
            self._command_line_options.always_awake
        )
        subprocess_wrapper = SubprocessWrapper()
        subprocess_command_generator = WlrRandrCommands()
        subprocess_command_generator = WlopmCommands()
        display_on_off_controller = DisplayOnOffController(
            subprocess_wrapper,
            subprocess_command_generator,
            status_updater,
            system_operations)
        display_on_off_controller.initialise()
        awake_decider = AwakeDecider(awake_schedule, display_on_off_controller)

        debug_menu = DebugMenu(
            status_updater,
            next_image_timer,
            awake_decider,
            display_on_off_controller,
            random_monitor
            )
        menu_handler = MenuHandler(display_on_off_controller, system_operations)
        historic_photo_chooser = HistoricPhotoChooser(photo_history)
        first_menu = FirstMenu(menu_handler, debug_menu, historic_photo_chooser)
        menu_handler.set_main_menu(first_menu)
        event_handler = EventHandler(menu_handler)
        events_handler = EventsHandler(display, event_handler)

        image_from_file_loader = ImageFromFileLoader(display)
        photo_path_provider = PhotoToDisplayChooser(
            awake_decider,
            historic_photo_chooser,
            sequential_photo_chooser
            )
        image_provider = ImageProvider(
            photo_path_provider,
            image_from_file_loader)
        main_loop = MainLoop(
            cycle_stop_detector,
            image_provider,
            display,
            events_handler,
            menu_handler)
        try:
            main_loop.loop()
        finally:
            display_on_off_controller.display_on()

    def load_photo_sets(self,
                        system_operations,
                        remote_config_data,
                        path_to_photo_sets):
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
        return photo_sets

    def build_random_photo_selector_module(self,
                                           system_operations,
                                           image_display_seconds,
                                           randomiser,
                                           photo_sets,
                                           photo_history):
        random_photo_set_selector = RandomPhotoSetSelector(
            randomiser,
            photo_sets)
        photo_from_photo_set_selecter = PhotoFromPhotoSetSelectorNew(
            randomiser
        )
        random_photo_selector = RandomPhotoSelectorNew(
            random_photo_set_selector,
            photo_from_photo_set_selecter)
        next_photo_to_show_generator = NextPhotoToShowGenerator(
            random_photo_selector,
            photo_history,
            50
        )
        next_photo_to_show_timer = ActionTimer(
                'Image change new',
                system_operations,
                next_photo_to_show_generator.generate_next_photo,
                image_display_seconds
            )

        return NextPhotoToShowCache(next_photo_to_show_timer,
                                    photo_history)