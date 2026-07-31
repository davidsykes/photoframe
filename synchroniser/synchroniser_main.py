import os
from pathlib import Path

from common.src.config_file_loader import ConfigFileLoader
from common.src.config_file_updater import ConfigFileUpdater
from common.src.remote_files_retriever import RemoteFilesRetriever
from common.src.system_operations import SystemOperations
from synchroniser.src.photo_folder_synchroniser import PhotoFolderSynchroniser
from synchroniser.src.photo_folders_synchroniser import PhotoFoldersSynchroniser
from synchroniser.src.remote_config_loader import RemoteConfigLoader
from synchroniser.src.synchroniser_app import SynchroniserApp

PROJECT_ROOT = Path(__file__).resolve().parent
WORING_FOLDER = PROJECT_ROOT / "working"

def main() -> int:
    print(f'PROJECT_ROOT {PROJECT_ROOT}')
    print(f'WORING_FOLDER {WORING_FOLDER}')
    if not os.path.exists(WORING_FOLDER):
        os.makedirs(WORING_FOLDER)
    system_operations = SystemOperations()
    system_operations.set_logger('synchroniser')
    config_file_loader = ConfigFileLoader(system_operations)
    remote_files_retriever = RemoteFilesRetriever(system_operations)
    config_file_updater = ConfigFileUpdater(
        remote_files_retriever,
        config_file_loader,
        system_operations)
    project_config = config_file_loader.load_config_file('project_config.json')
    remote_config_loader = RemoteConfigLoader(
        WORING_FOLDER,
        'viewer_config',
        config_file_updater,
        config_file_loader)
    remote_folder_downloader = RemoteFolderDownloader()
    images_folder = project_config.get('images_folder')
    photo_folder_synchroniser = PhotoFolderSynchroniser(
        system_operations,
        remote_folder_downloader,
        images_folder
        )
    photo_folders_synchroniser = PhotoFoldersSynchroniser(photo_folder_synchroniser)

    app = SynchroniserApp(project_config,
                          remote_config_loader,
                          photo_folders_synchroniser)
    app.sync()

    return 123


if __name__ == '__main__':
    raise SystemExit(main())