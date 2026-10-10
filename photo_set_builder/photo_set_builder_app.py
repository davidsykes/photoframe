from pathlib import Path
from common.src.config_file_loader import ConfigFileLoader
from common.src.system_operations import SystemOperations
from photo_set_builder.src.logic.list_to_dict_converter import ListToDictConverter
from photo_set_builder.src.logic.photo_compressor import PhotoCompressor
from photo_set_builder.src.logic.photo_set_builder_exception import PhotoSetBuilderException
from photo_set_builder.src.logic.photo_set_config_loader import PhotoSetConfigLoader
from photo_set_builder.src.logic.photo_zipper import PhotoZipper
from photo_set_builder.src.photo_set_builder_config import PhotosetBuilderConfig
from photo_set_builder.src.photo_set_processing.compressed_photos_remover import CompressedPhotosRemover
from photo_set_builder.src.photo_set_processing.photo_set_zipper import PhotoSetZipper
from photo_set_builder.src.photo_set_processing.photos_compressor import PhotosCompressor
from photo_set_builder.src.photo_set_processing.photo_scanner import PhotoScanner
from photo_set_builder.src.photo_set_processing.photo_set_processor import PhotoSetProcessor
from photo_set_builder.src.photo_set_processing.photos_synchroniser import PhotosSynchroniser
from photo_set_builder.src.photo_set_processing.photo_sets_lister import PhotoSetsLister
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
    photo_set_config_loader = PhotoSetConfigLoader(config_file_loader)
    photo_sets_lister = PhotoSetsLister(system_operations,
                                        photo_set_config_loader)
    photo_sets_definitions = photo_sets_lister.list_photo_sets(
        config_data.photo_sets_path)
    photo_scanner = PhotoScanner(system_operations,
                                 config_data.compressed_folder_name)
    list_to_dict_converter = ListToDictConverter()
    photo_zipper = PhotoZipper()
    photo_compressor = PhotoCompressor(photo_zipper)
    photos_compressor = PhotosCompressor(photo_compressor)
    compressed_photos_remover = CompressedPhotosRemover(system_operations)
    photos_synchroniser = PhotosSynchroniser(
        list_to_dict_converter,
        photos_compressor,
        compressed_photos_remover)
    photo_set_zipper = PhotoSetZipper()
    photo_set_processor = PhotoSetProcessor(system_operations,
                                            photo_scanner,
                                            photos_synchroniser,
                                            photo_set_zipper,
                                            config_data.compressed_folder_name)
    photo_sets_processor = PhotoSetsProcessor(photo_set_processor)
    photo_sets_processor.process_photo_sets(photo_sets_definitions)
    viewer_config_manager = ViewerConfigManager(
        config_file_loader,
        config_data.viewer_config_path)
    photo_set_synchroniser = PhotoSetsSynchroniser(
        system_operations,
        viewer_config_manager)
    photo_set_synchroniser.synchronise_photo_sets(
        photo_sets_definitions)
    viewer_config_manager.save_viewer_config()

def main2():
    try:
        return main()
    except PhotoSetBuilderException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    raise SystemExit(main2())