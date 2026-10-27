class DisplayWrapper:
    def __init__(self,
                 display,
                 display_scaler):
        self._display = display
        self._display_scaler = display_scaler

    def draw_text(self,
                  text,
                  position):
        rendered_text = self._display.render_text(text)
        self._display.draw_rendered_text(
            rendered_text,
            position
        )

    def load_image_from_file_and_scale(self, image_path, size):
        image = self._display.load_image(image_path)
        scaled_size = self._display_scaler.scale(size)
        image = self._display.scale_image(image, scaled_size)
        return image

    def show_image(self, image, position):
        scaled_position = self._display_scaler.scale(position)
        self._display.show_image(image, scaled_position)