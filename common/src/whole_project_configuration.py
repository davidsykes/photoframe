class WholeProjectConfiguration:
    def __init__(self, config_file_loader):
        self._config_file_loader = config_file_loader
        self._configuration_file_name = 'project_config.json'
        self.load_values()

    def load_values(self):
        config = self._config_file_loader.load_config_file(
            self._configuration_file_name
        )
        self.images_folder = config.get('images_folder')
