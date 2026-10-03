from common.src.retrying_action import RetryingAction


class RetryingActionDownloader():
    def __init__(self, retrying_action: RetryingAction):
        self._retrying_action = retrying_action

    def download_file_or_return_false(self, *args, **kwargs):
        return self._retrying_action.execute(*args, **kwargs)