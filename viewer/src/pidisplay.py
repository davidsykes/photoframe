import time
import pygame
from viewer.src.viewer_exit_exception import ViewerExitException

class PiSystemDisplay:
    def __init__(self, system_operations):
        self.system_operations = system_operations
        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 800
        self.event_count = 0

    def initialise(self):
        print("Initialising Pi System Display.")
        pygame.init()
        print('Desktop sizes:', pygame.display.get_desktop_sizes())
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)
        print('Configured:', self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        print('Pygame surface:', self.screen.get_size())
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.screen.get_size()

        pygame.display.set_caption("Pi System Display")
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)

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

        text_surface = self.my_font.render(f'Events: {self.event_count}',
                                           True,
                                           (255, 255, 255))
        self.screen.blit(text_surface, (10, 10))

        pygame.display.flip()

    def sleep(self, seconds):
        time_sec = time.time()
        while time.time() - time_sec < seconds:
            self._handle_events()
            time.sleep(0.1)

    def _handle_events(self):
        for event in pygame.event.get():
            self.event_count += 1
            self.system_operations.log(f"Pygame Event: {event}")
            if event.type == pygame.QUIT:
                raise ViewerExitException(100, "Quit event received")

            elif event.type == pygame.KEYDOWN:
                ctrl_c = (
                    event.key == pygame.K_c
                    and (event.mod & pygame.KMOD_CTRL)
                    )
                if event.key in (pygame.K_ESCAPE, pygame.K_q) or ctrl_c:
                    raise ViewerExitException(100, f"Quit event {event.key} received")