import logging
from common.src.remote_files_retriever import RemoteFilesRetriever
from common.src.config_file_loader import ConfigFileLoader
from common.src.system_operations import SystemOperations

logging.basicConfig(
    filename="C:\\TestData\\PhotoFrame\\Logs\\updater.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)
logger = logging.getLogger(__name__)

sys_operations = SystemOperations()
try:
    config_data = ConfigFileLoader(sys_operations, 'updater/config.json')
    remote_files_local_storage_path = config_data.get('remote_files_local_storage_path')
    remote_files_retriever = RemoteFilesRetriever(remote_files_local_storage_path)
    viewer_config_remote_url = config_data.get('viewer_config_remote_url')

    check_for_updates = True
    while check_for_updates:
        check_for_updates = False
        viewer_config_local_path = remote_files_retriever.download_file(viewer_config_remote_url)
        viewer_config_local = config_data.load_config(viewer_config_local_path)
        version_list = viewer_config_local.get('version_list')

        next_version_to_try = len(version_list) - 1

        while check_for_updates is False and next_version_to_try >= 0:
            version = version_list[next_version_to_try]
            if (VersionRepeater().run_version(version, 3) == CHECK_FOR_UPDATES):
                check_for_updates = True      
            next_version_to_try -= 1
except RuntimeError as ex:
    logger.error(str(ex))
    print("Run time error: " +str(ex))
except Exception as ex:
    logger.error(str(ex))
    print("Unhandled Exception: " +str(ex))
