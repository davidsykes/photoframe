from pathlib import Path
import traceback
from common.src.config_file_updater import ConfigFileUpdater
from common.src.remote_files_retriever import RemoteFilesRetriever
from common.src.config_file_loader import ConfigFileLoader
from common.src.system_operations import SystemOperations
from updater.src.viewer_versions_config_loader import ViewerVersionsConfigLoader

sys_operations = SystemOperations()
sys_operations.set_logger("C:\\TestData\\PhotoFrame\\Logs\\updater.log")

try:
    config_file_loader = ConfigFileLoader(sys_operations)
    updater_config_data = config_file_loader.load_config_file('updater/config.json')
    remote_files_local_storage_path = updater_config_data.get('remote_files_local_storage_path')
    remote_files_retriever = RemoteFilesRetriever(sys_operations, remote_files_local_storage_path)
    viewer_config_remote_url = updater_config_data.get('viewer_config_remote_url')
    viewer_config_local_path = updater_config_data.get('viewer_config_local_path')
    config_file_updater = ConfigFileUpdater()
    viewer_versions_config_loader = ViewerVersionsConfigLoader(
        config_file_updater,
        config_file_loader,
        viewer_config_remote_url,
        viewer_config_local_path)

    check_for_updates = True
    while check_for_updates:
        check_for_updates = False

        viewer_versions_config = viewer_versions_config_loader.load_viewer_versions_config(viewer_config_remote_url)

        version_list = viewer_versions_config.get('version_list')

        next_version_to_try = len(version_list) - 1

        while check_for_updates is False and next_version_to_try >= 0:
            version = version_list[next_version_to_try]
            if (VersionRepeater().run_version(version, 3) == CHECK_FOR_UPDATES):
                check_for_updates = True      
            next_version_to_try -= 1
except RuntimeError as ex:
    sys_operations.logger.error(str(ex))
    print("Run time error: " +str(ex))
except Exception as ex:
    sys_operations.logger.error(str(ex))
    print("Unhandled Exception: " +str(ex))
    traceback.print_exc()
