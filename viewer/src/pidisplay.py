import pygame

class PiSystemDisplay:
    def __init__(self):
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 800

    def initialise(self):
        print("Initialising Pi System Display")
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption("Pi System Display")

    def show_image(self, image_path):
        print(f"Showing image on Pi: {image_path}")
        image = pygame.image.load(image_path)
        self.screen.blit(image, (0, 0))
        pygame.display.flip()

    def show_image2(self, image_path):
        image = pygame.image.load(image_path).convert()
        image = pygame.transform.smoothscale(
            image,
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        )
        self.screen.blit(image, (0, 0))
        pygame.display.flip()

    def show_image_resized(self, image_path):
        image = pygame.image.load(image_path).convert()
        iw, ih = image.get_size()

        scale = min(
            self.SCREEN_WIDTH / iw,
            self.SCREEN_HEIGHT / ih
        )

        new_size = (
            int(iw * scale),
            int(ih * scale)
        )

        image = pygame.transform.smoothscale(image, new_size)

        x = (self.SCREEN_WIDTH - new_size[0]) // 2
        y = (self.SCREEN_HEIGHT - new_size[1]) // 2

        self.screen.fill((0, 0, 0))
        self.screen.blit(image, (x, y))
        pygame.display.flip()

