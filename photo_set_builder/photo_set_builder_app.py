from pathlib import Path
from common.src.config_file_loader import ConfigFileLoader
from common.src.system_operations import SystemOperations
from photo_set_builder.src.photo_set_builder_config import PhotosetBuilderConfig
from photo_set_builder.src.photo_set_processing.photo_scanner import PhotoScanner
from photo_set_builder.src.photo_set_processing.photo_set_processor import PhotoSetProcessor
from photo_set_builder.src.photo_set_processing.photos_synchroniser import PhotosSynchroniser
from photo_set_builder.src.photo_sets_lister import PhotoSetsLister
from photo_set_builder.src.photo_set_processing.photo_sets_processor import PhotoSetsProcessor
from photo_set_builder.src.photo_sets_synchroniser import PhotoSetsSynchroniser
from photo_set_builder.src.viewer_config_manager import ViewerConfigManager


APP_ROOT = Path(__file__).resolve().parent

def main() -> int:
    system_operations = SystemOperations()
    system_operations.set_logger('photo_set_builder', '')
    system_operations.log(f"Starting Photo Set Builder from {APP_ROOT}")

    config_file_path = APP_ROOT / 'photo_set_builder_config.json'
    config_file_loader = ConfigFileLoader(system_operations)
    config_data = PhotosetBuilderConfig(config_file_loader,
                                        config_file_path)
    photo_sets_lister = PhotoSetsLister(system_operations)
    photo_sets_definitions = photo_sets_lister.list_photo_sets(
        config_data.photo_sets_path)
    photo_scanner = PhotoScanner(system_operations,
                                 config_data.compressed_folder_name)
    photos_synchroniser = PhotosSynchroniser()
    photo_set_processor = PhotoSetProcessor(system_operations,
                                            photo_scanner,
                                            photos_synchroniser,
                                            config_data.compressed_folder_name)
    photo_sets_processor = PhotoSetsProcessor(photo_set_processor)
    photo_sets_processor.process_photo_sets(photo_sets_definitions)
    viewer_config_manager = ViewerConfigManager(config_data.viewer_config_path)
    photo_set_synchroniser = PhotoSetsSynchroniser(system_operations)
    photo_set_synchroniser.synchronise_photo_sets(photo_sets_definitions, viewer_config_manager.photo_folders)
    viewer_config_manager.save_viewer_config()

if __name__ == '__main__':
    raise SystemExit(main())