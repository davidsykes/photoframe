

class PCSystemDisplay:
    def __init__(self, event_emulator):
        self._event_emulator = event_emulator

    def initialise(self):
        print("Initialising PC System Display")

    def load_image(self, image_path):
        print(f"Loading image on PC: {image_path}")
        return image_path
    
    def prepare_screen(self):
        print('Prep screen')

    def show_image(self, image_path):
        print(f"Showing image on PC: {image_path}")

    def print(self, x, y, s):
        print(f'print({x},{y} {s})')

    def flip(self):
        print('flip')

    def sleep(self, seconds):
        print(f"Sleeping for {seconds} seconds")

    def get_events(self):
        return self._event_emulator.get_events()
