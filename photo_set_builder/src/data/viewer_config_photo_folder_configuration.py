import re
from dataclasses import dataclass

from photo_set_builder.src.logic.photo_set_builder_exception import PhotoSetBuilderException


@dataclass()
class ViewerConfigPhotoFolderConfiguration:
    name: str
    version: int
    date: str

    def __init__(self, config):
        self._reg = re.compile(r'^(.*?)-(\d+)$')
        self.config = config
        self.initialise_name(config[0])
        if len(config) < 4:
            raise PhotoSetBuilderException(
                f'Invalid viewer config: {config}')
        self.date = config[3]

    def initialise_name(self, versioned_name):
        match = self._reg.fullmatch(versioned_name)
        if match:
            self.name = match.group(1)
            self.version = int(match.group(2))
        else:
            self.name = versioned_name
            self.version = 0

    def update_version(self):
        self.version += 1
        self.config[0] = f'{self.name}-{self.version}'

    def update_date(self, updated_date):
        self.date = updated_date
        self.config[3] = self.date