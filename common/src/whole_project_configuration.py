class WholeProjectConfiguration:
    def __init__(self, config_file_loader):
        self._config_file_loader = config_file_loader
        self._configuration_file_name = 'project_config.json'
        self.load_values()

    def load_values(self):
        config = self._config_file_loader.load_config_file(
            self._configuration_file_name
        )
        self.remote_config_url = config.get('remote_config_url')
        self.images_folder = config.get('images_folder')
        self.sleep_time_seconds = config.get('sleep_time_seconds')
        self.photo_set_filter = config.get_or_default(
            'photo_set_filter',
            'ava')
        self.hide_mouse = config.get_or_default(
            'hide_mouse',
            True)
