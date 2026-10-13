import re


class SetNameOnFrameDiskUpdater:
    def __init__(self):
        self._reg = re.compile(r'^(.*?)(\d+)$')

    def update_name(self, name):
        match = self._reg.fullmatch(name)
        if match:
            prefix = match.group(1)
            number = int(match.group(2))
            return f'{prefix}{number+1}'
        return name + '-1'