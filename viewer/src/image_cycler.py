
class ImageCycler:
    def __init__(self,
                 system_operations,
                 next_image_selector,
                 cycle_stop_detector,
                 display,
                 sleep_time_seconds):
        self._system_operations = system_operations
        self._next_image_selector = next_image_selector
        self._cycle_stop_detector = cycle_stop_detector
        self._display = display
        self._sleep_time_seconds = sleep_time_seconds

    def cycle_images(self):
        while True:
            if self._cycle_stop_detector.should_stop():
                break
            next_image = self._next_image_selector.select_next_image()
            self._display.show_image(next_image)
            self._system_operations.sleep(self._sleep_time_seconds)