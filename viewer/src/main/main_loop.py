class MainLoop:
    def __init__(self,
                 cycle_stop_detector,
                 next_image_timer,
                 display):
        self._cycle_stop_detector = cycle_stop_detector
        self._next_image_timer = next_image_timer
        self._display = display
        self._current_image = self._next_image_timer.run_if_due()

    def loop(self):
        print('IN NNAONASO NLADLSDJ')
        self._images_shown = 0
        while self._images_shown < 3:
            self.loop_once()
        print('IN NNAONASO NLADLSDJ KLJFJLDJKSFLJ')

    def loop_once(self):
        needs_update = False
        self._cycle_stop_detector.poll()
        new_image = self._next_image_timer.run_if_due()
        if new_image is not None:
            self._current_image = new_image
            needs_update = True
        if needs_update:
            self._display.prepare_screen()
            self._display.show_image(self._current_image)
            #self._menu.render(self._display)
            #self.pause_for_user_input() Uses Sleeper
            self._display.flip()
            self._images_shown += 1
        self._display.tick(60)