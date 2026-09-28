class ActionResultRecorder:
    def __init__(self, action_description, recorder):
        self._action_description = action_description
        self._recorder = recorder

    def update_status(self, status):
        status = 'Success' if status else 'Failure'
        self._recorder.record_status(
            self._action_description,
            status)