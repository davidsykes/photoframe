class AwakeDecider:
    def __init__(self, awake_schedule, display_controller):
        self._awake_schedule = awake_schedule
        self._display_controller = display_controller
        self._awake = True
        self._timer_awake = True

    def are_we_awake(self):
        timer_awake = self._awake_schedule.are_we_awake()
        print(f'AwakeDecider: timer_awake={timer_awake} _timer_awake={self._timer_awake}')
        if timer_awake != self._timer_awake:
            self._timer_awake = timer_awake
            self._awake = timer_awake
            self.turn_on_or_off_display(timer_awake)
        return self._awake

    def go_to_sleep(self):
        self._awake = False
        self.turn_on_or_off_display(self._awake)

    def wake_up(self):
        self._awake = True
        self.turn_on_or_off_display(self._awake)

    def turn_on_or_off_display(self, awake):
        if awake:
            self._display_controller.display_on()
        else:
            self._display_controller.display_off()