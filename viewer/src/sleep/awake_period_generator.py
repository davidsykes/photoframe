from datetime import time

from viewer.src.sleep.awake_period import AwakePeriod


class AwakePeriodGenerator:
    def __init__(self, application_status):
        self.application_status = application_status

    def generate_awake_period(self, start_time, end_time):
        start_time = time.fromisoformat(start_time)
        end_time = time.fromisoformat(end_time)
        return AwakePeriod(start_time, end_time)