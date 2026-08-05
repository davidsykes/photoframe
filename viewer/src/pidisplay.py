import time

import pygame

class PiSystemDisplay:
    def __init__(self):
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 800

    def initialise(self):
        print("Initialising Pi System Display.")
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption("Pi System Display")

    def show_image(self, image_path):
        try:
            image = pygame.image.load(image_path)
        except pygame.error as e:
            err = f'Unable to load image {image_path}: {e}'
            raise RuntimeError(err)
        image = image.convert()
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

    def sleep(self, seconds):
        time_sec = time.time()
        while time.time() - time_sec < seconds:
            self._handle_events()
            time.sleep(0.1)

    def _handle_events(self):
        for event in pygame.event.get():
            print(f"Event: {event}")
            if event.type == pygame.QUIT:
                running = False
                raise SystemExit("Quit event received")

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    running = False
                raise SystemExit("Quit event received")