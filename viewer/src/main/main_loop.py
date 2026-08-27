class MainLoop:
    def __init__(self,
                 cycle_stop_detector,
                 next_image_timer,
                 display,
                 events_handler,
                 menu):
        self._cycle_stop_detector = cycle_stop_detector
        self._next_image_timer = next_image_timer
        self._display = display
        self._events_handler = events_handler
        self._menu = menu
        self._current_image = None

    def loop(self):
        while True:
            self.loop_once()

    def loop_once(self):
        needs_update = False
        self._cycle_stop_detector.poll()
        self._events_handler.handle_events()
        new_image_path = self._next_image_timer.run_if_due()
        if new_image_path is not None:
            self._current_image = self._display.load_image(new_image_path)
            needs_update = True
        if needs_update:
            self._display.prepare_screen()
            self._display.show_image(self._current_image)
            self._menu.render(self._display)
            self._display.flip()
        self._display.tick(60)