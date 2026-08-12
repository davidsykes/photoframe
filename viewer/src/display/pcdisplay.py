from viewer.src.events.uievent import UIEvent


class PCSystemDisplay:
    def __init__(self):
        pass

    def initialise(self):
        print("Initialising PC System Display")

    def load_image(self, image_path):
        print(f"Loading image on PC: {image_path}")
        return image_path

    def show_image(self, image_path):
        print(f"Showing image on PC: {image_path}")

    def sleep(self, seconds):
        print(f"Sleeping for {seconds} seconds")

    def get_events(self):
        events = []
        x = 10
        y = 20
        events.append(UIEvent(
            UIEvent.MouseDown,
            x,
            y
        ))
        return events
