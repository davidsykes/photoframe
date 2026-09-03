class AwakeDecider:
    def __init__(self, awake_schedule):
        self._awake_schedule = awake_schedule
        self._awake = True
        self._timer_awake = True

    def are_we_awake(self):
        timer_awake = self._awake_schedule.are_we_awake()
        if timer_awake != self._timer_awake:
            self._timer_awake = timer_awake
            self._awake = timer_awake
        return self._awake

    def go_to_sleep(self):
        self._awake = False

    def wake_up(self):
        self._awake = True