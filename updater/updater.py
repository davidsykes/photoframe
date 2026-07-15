
check_for_updates = True
while check_for_updates:
    check_for_updates = False
    config = ConfigFileLoader().load_config('config.json')
    version_list = RemoteVersionsFileRetriever().get_versions(config.get('remote_versions_url'))

    next_version_to_try = version_list.len() - 1

    while check_for_updates is false and next_version_to_try >= 0:
        version = version_list[next_version_to_try]
        if (VersionRepeater().run_version(version, 3) == CHECK_FOR_UPDATES):
            check_for_updates = true      
        next_version_to_try -= 1
