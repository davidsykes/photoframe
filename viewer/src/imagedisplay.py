
class ImageDisplay:
    def __init__(self, display):
        self.display = display

    def display_images(self, image_paths):
        # Implementation for displaying images
        for image_path in image_paths:
            print(f"Displaying image: {image_path}")
            self.display.show_image(image_path)