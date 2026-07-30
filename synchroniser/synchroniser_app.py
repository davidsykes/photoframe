import os
from pathlib import Path

from common.src.config_file_loader import ConfigFileLoader
from common.src.config_file_updater import ConfigFileUpdater
from common.src.remote_files_retriever import RemoteFilesRetriever
from common.src.system_operations import SystemOperations

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
    config_file_updater = ConfigFileUpdater(remote_files_retriever, config_file_loader, system_operations)

    project_config = config_file_loader.load_config_file('project_config.json')
    remote_config_url = project_config.get('remote_config_url')
    sync_remote_config_local_path = WORING_FOLDER / 'global_viewer_versions_config.json'
    config_file_updater.update_config_file(
        remote_config_url,
        sync_remote_config_local_path
    )
    sync_remote_config = config_file_loader.load_config_file(sync_remote_config_local_path)
    photo_folders = sync_remote_config.get('photo_folders')
    photo_folder_synchroniser.sync(photo_folders)
    return result


if __name__ == '__main__':
    raise SystemExit(main())