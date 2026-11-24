from common.src.action_result_logger import ActionResultLogger
from common.src.action_result_recorder_protocol import ActionResultRecorderProtocol


class ActionResultRecorder(ActionResultRecorderProtocol):
    def __init__(self,
                 action_description:str,
                 recorder:ActionResultLogger):
        self._action_description = action_description
        self._recorder = recorder

    def update_status(self, status):
        status = 'Success' if status else 'Failure'
        self._recorder.record_status(
            self._action_description,
            status)