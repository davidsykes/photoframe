from typing import Protocol


class ActionResultRecorderProtocol(Protocol):
    def update_status(self, status:bool):
        ...
