from pathlib import Path

from common.src.config_file_loader import ConfigFileLoader
from common.src.config_file_updater import ConfigFileUpdater
from common.src.remote_files_retriever import RemoteFilesRetriever
from common.src.system_operations import SystemOperations
from common.src.whole_project_configuration import WholeProjectConfiguration
from common.unzipper import UnZipper
from synchroniser.src.photo_folder_synchroniser import PhotoFolderSynchroniser
from synchroniser.src.photo_folders_filterer import PhotoFoldersFilterer
from synchroniser.src.photo_folders_remover import PhotoFoldersRemover
from synchroniser.src.photo_folders_synchroniser import PhotoFoldersSynchroniser
from synchroniser.src.remote_config_loader import RemoteConfigLoader
from synchroniser.src.remote_folder_downloader import RemoteFolderDownloader
from synchroniser.src.remote_folder_downloader_wrapper import RemoteFolderDownloaderWrapper
from synchroniser.src.synchroniser_app import SynchroniserApp

SYNCHRONISER_PROJECT_ROOT = Path(__file__).resolve().parent
PHOTOFRAME_PROJECT_ROOT = SYNCHRONISER_PROJECT_ROOT.parent
WORKING_FOLDER = SYNCHRONISER_PROJECT_ROOT / "working"

def main() -> int:
    system_operations = SystemOperations()
    system_operations.set_logger('synchroniser', '--')
    system_operations.ensure_folder_exists(WORKING_FOLDER)
    temp_folder_location = PHOTOFRAME_PROJECT_ROOT / "temp"
    system_operations.ensure_folder_exists(temp_folder_location)
    config_file_loader = ConfigFileLoader(system_operations)
    remote_files_retriever = RemoteFilesRetriever(system_operations)
    config_file_updater = ConfigFileUpdater(
        remote_files_retriever,
        config_file_loader,
        system_operations)
    #project_config = config_file_loader.load_config_file('project_config.json')
    project_config = WholeProjectConfiguration(config_file_loader)
    remote_config_loader = RemoteConfigLoader(
        WORKING_FOLDER,
        'remote_viewer_config',
        config_file_updater,
        config_file_loader)
    unzipper = UnZipper()
    remote_folder_downloader = RemoteFolderDownloader(
        system_operations,
        remote_files_retriever,
        unzipper
    )
    remote_folder_downloader_wrapper = RemoteFolderDownloaderWrapper(
        system_operations,
        remote_folder_downloader,
        temp_folder_location
    )
    images_folder = project_config.images_folder
    system_operations.log(f"Images folder: {images_folder}")
    system_operations.ensure_folder_exists(images_folder)
    photo_folder_synchroniser = PhotoFolderSynchroniser(
        system_operations,
        remote_folder_downloader_wrapper,
        images_folder
        )
    filter_string = project_config.photo_set_filter
    system_operations.log(f'Photo filter: \'{filter_string}\'')
    photo_folders_filterer = PhotoFoldersFilterer(system_operations, filter_string)
    photo_folders_synchroniser = PhotoFoldersSynchroniser(
        photo_folder_synchroniser)
    photo_folders_remover = PhotoFoldersRemover(
        system_operations,
        images_folder)

    app = SynchroniserApp(project_config,
                          remote_config_loader,
                          photo_folders_filterer,
                          photo_folders_synchroniser,
                          photo_folders_remover)
    app.sync()

    return 123


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("Exiting due to keyboard interrupt")
        raise SystemExit(1)