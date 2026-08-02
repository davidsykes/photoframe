from pathlib import Path
import traceback
from common.src.config_file_updater import ConfigFileUpdater
from common.src.remote_files_retriever import RemoteFilesRetriever
from common.src.config_file_loader import ConfigFileLoader
from common.src.system_operations import SystemOperations
from updater.src.sandbox import Sandbox
from common.unzipper import UnZipper
from updater.src.version_downloader import VersionDownloader
from updater.src.version_has_been_downloaded_checker import VersionHasBeenDownloadedChecker
from updater.src.version_runner import VersionRunner
from updater.src.viewer_versions_config_loader import ViewerVersionsConfigLoader
from updater.src.version_repeater import DownloadResult, VersionRepeater

PROJECT_ROOT = Path(__file__).resolve().parent
WORKING_FOLDER = PROJECT_ROOT / "working"

sys_operations = SystemOperations()
sys_operations.set_logger('updater')

try:
    project_config_path = 'project_config.json'
    #updater_working_folder = Path(__file__).resolve().parent
    #print(f"Updater working folder: {updater_working_folder}")

    config_file_loader = ConfigFileLoader(sys_operations)
    updater_config_data = config_file_loader.load_config_file('updater/updater_config.json')
    viewer_app_working_folder = updater_config_data.get(
        'viewer_app_working_folder')
    viewer_sandbox = Sandbox(viewer_app_working_folder)
    
    project_config = config_file_loader.load_config_file(project_config_path)
    remote_config_url = project_config.get('remote_config_url')
    sys_operations.ensure_folder_exists(WORKING_FOLDER)
    viewer_versions_config_local_path = WORKING_FOLDER.joinpath(
        'viewer_versions_config.json')

    remote_files_retriever = RemoteFilesRetriever(sys_operations)
    config_file_updater = ConfigFileUpdater(
        remote_files_retriever,
        config_file_loader,
        sys_operations)
    viewer_versions_config_loader = ViewerVersionsConfigLoader(
        config_file_updater,
        config_file_loader,
        viewer_versions_config_local_path)
    version_has_been_downloaded_checker = VersionHasBeenDownloadedChecker(
        sys_operations,
        viewer_app_working_folder
    )
    unzipper = UnZipper()
    version_downloader = VersionDownloader(
        sys_operations,
        viewer_sandbox,
        remote_files_retriever,
        unzipper,
        project_config_path
    )
    parameters = project_config.get('viewer_parameters')
    version_runner = VersionRunner(viewer_sandbox, parameters)
    version_repeater = VersionRepeater(
        version_has_been_downloaded_checker,
        version_downloader,
        version_runner)

    check_for_updates = True
    while check_for_updates:
        check_for_updates = False

        viewer_versions_config = viewer_versions_config_loader.load_viewer_versions_config(
            remote_config_url)

        version_list = viewer_versions_config.get('version_list')

        next_version_to_try = len(version_list) - 1

        while check_for_updates is False and next_version_to_try >= 0:
            version = version_list[next_version_to_try]
            if (version_repeater.run_version(version, 3) == DownloadResult.CHECK_FOR_UPDATES):
                check_for_updates = True      
            next_version_to_try -= 1
except RuntimeError as ex:
    sys_operations.logger.error(str(ex))
    print("Run time error: " +str(ex))
except Exception as ex:
    sys_operations.logger.error(str(ex))
    print("Unhandled Exception: " +str(ex))
    traceback.print_exc()
