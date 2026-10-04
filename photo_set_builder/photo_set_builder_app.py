from pathlib import Path
from common.src.system_operations import SystemOperations
from photo_set_builder.src.photo_set_builder_config import PhotosetBuilderConfig
from photo_set_builder.src.photo_sets_lister import PhotoSetsLister
from photo_set_builder.src.photo_sets_processor import PhotoSetsProcessor
from photo_set_builder.src.photo_sets_synchroniser import PhotoSetsSynchroniser
from photo_set_builder.src.viewer_config_manager import ViewerConfigManager


APP_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = APP_ROOT.parent

def main() -> int:
    system_operations = SystemOperations()
    system_operations.set_logger('photo_set_builder', '')
    system_operations.log(f"Starting Photo Set Builder from {APP_ROOT}")
    system_operations.log(f"Starting Photo Set Builder from {PROJECT_ROOT}")

    config_file_path = PROJECT_ROOT / 'photo_set_builder_config.json'
    config_data = PhotosetBuilderConfig(config_file_path)
    photo_sets_definitions = PhotoSetsLister(system_operations).list_photo_sets(config_data.photo_sets_path)
    photo_sets_processor = PhotoSetsProcessor(system_operations)
    photo_sets_processor.process_photo_sets(photo_sets_definitions)
    viewer_config_manager = ViewerConfigManager(config_data.viewer_config_path)
    photo_set_synchroniser = PhotoSetsSynchroniser(system_operations)
    photo_set_synchroniser.synchronise_photo_sets(photo_sets_definitions, viewer_config_manager.photo_folders)
    viewer_config_manager.save_viewer_config()

if __name__ == '__main__':
    raise SystemExit(main())