import time
from viewer.src.display.pygame_image import PygameImage


class PCSystemDisplay:
    def __init__(self, event_emulator):
        self._event_emulator = event_emulator
        self.COLOUR_WHITE = 'White colour'
        self.COLOUR_LIGHT = 'Light colour'

    def initialise_display(self):
        print("Initialising PC System Display")

    def load_image(self, image_path):
        return PygameImage(image_path, image_path, 1, 1)
    
    def prepare_screen(self):
        print('Prep screen')

    def show_image(self, image):
        print(f"Showing image on PC: {image.image_path}")

    def print(self, s):
        print(f'print({s})')

    def flip(self):
        print('flip')

    def sleep(self, seconds):
        print(f"Sleeping for {seconds} seconds")

    def get_events(self):
        return self._event_emulator.get_events()

    def tick(self, v):
        time.sleep(1)

    def draw_button(self):
        print('Draw button')

    def draw_rectangle(self, colour, position):
        print(f'Draw {colour} rectangle {position}')

    def draw_text(self, text, colour, position):
        print(f'Draw text {text} in {colour} at {position}')