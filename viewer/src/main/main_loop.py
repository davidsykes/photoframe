class MainLoop:
    def __init__(self,
                 cycle_stop_detector,
                 next_image_timer,
                 image_provider,
                 display,
                 events_handler,
                 menu):
        self._cycle_stop_detector = cycle_stop_detector
        self._next_image_timer = next_image_timer
        self._image_provider = image_provider
        self._display = display
        self._events_handler = events_handler
        self._menu = menu
        self._current_image = None

    def loop(self):
        while True:
            self.loop_once_new()

    def loop_once_new(self):
        self._cycle_stop_detector.poll()
        needs_update = self._events_handler.handle_events()

        image_to_show = self._image_provider.provide_image()
        if image_to_show != self._current_image:
            self._current_image = image_to_show
            needs_update = True

        if needs_update:
            self._display.prepare_screen()
            if self._current_image is not None:
                self._display.show_image(self._current_image)
            self._menu.render(self._display)
            self._display.flip()
        self._display.tick(60)

    # def loop_once(self):
    #     self._cycle_stop_detector.poll()
    #     needs_update = self._events_handler.handle_events()
    #     new_image_path = self._next_image_timer.run_if_due()
    #     if new_image_path is not None:
    #         self._current_image = self._display.load_image(new_image_path)
    #         needs_update = True
    #     if needs_update:
    #         self._display.prepare_screen()
    #         self._display.show_image(self._current_image)
    #         self._menu.render(self._display)
    #         self._display.flip()
    #     self._display.tick(60)