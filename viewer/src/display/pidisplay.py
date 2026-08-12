import time
import pygame # pyright: ignore[reportMissingImports]
from viewer.src.display.pygame_image import PygameImage
from viewer.src.events.uievent import UIEvent
from viewer.src.viewer_exit_exception import ViewerExitException

class PiSystemDisplay:
    def __init__(self, system_operations):
        self.system_operations = system_operations
        self.event_count = 0
        self.last_mouse_pos = 'None yet'

    def initialise(self):
        print("Initialising Pi System Display.")
        pygame.init()
        print('Desktop sizes:', pygame.display.get_desktop_sizes())
        self.screen = pygame.display.set_mode(
            (0,0), pygame.FULLSCREEN)
        print('Pygame surface:', self.screen.get_size())
        pygame.display.set_caption("Pi System Display")
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)

    def load_image(self, image_path):
        try:
            image = pygame.image.load(image_path)
        except pygame.error as e:
            err = f'Unable to load image {image_path}: {e}'
            raise RuntimeError(err)
        image = image.convert()
        iw, ih = image.get_size()
        sw, sh = self.screen.get_size()

        scale = min(
            sw / iw,
            sh / ih
        )

        new_size = (
            int(iw * scale),
            int(ih * scale)
        )

        image = pygame.transform.smoothscale(image, new_size)

        x = (sw - new_size[0]) // 2
        y = (sh - new_size[1]) // 2

        return PygameImage(image, x, y)

    def show_image(self, image):
        self.screen.fill((0, 0, 0))
        self.screen.blit(image.image, (image.x, image.y))

        self.print(10, 10, f'Events: {self.event_count}')
        self.print(20, 30, f'Last mouse position: {self.last_mouse_pos}')

        print(
            'show screen=', self.screen.get_size(),
            'position=', (image.x, image.y),
            'image=', image.image.get_size()
            )
        pygame.display.flip()

    def print(self, x, y, message):
        text_surface = self.my_font.render(message,
                                           True,
                                           (255, 255, 255))
        self.screen.blit(text_surface, (x, y))

    def sleep(self, seconds):
        time_sec = time.time()
        while time.time() - time_sec < seconds:
            self._handle_events()
            time.sleep(0.1)

    
    def get_events(self):
        events = []
        for event in pygame.event.get():
            self.event_count += 1
            if event.type == pygame.QUIT:
                raise ViewerExitException(100, "Quit event received")
            elif event.type == pygame.KEYDOWN:
                ctrl_c = (
                    event.key == pygame.K_c
                    and (event.mod & pygame.KMOD_CTRL)
                    )
                if event.key in (pygame.K_ESCAPE, pygame.K_q) or ctrl_c:
                    if event.key == pygame.K_c:
                        raise ViewerExitException(101, f"Control-C event received")
                    raise ViewerExitException(100, f"Quit event {event.key} received")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.last_mouse_pos = event.pos
                x = event.pos[0]
                y = event.pos[1]
                events.append(UIEvent(
                    UIEvent.MouseDown,
                    x,
                    y
                ))
            elif event.type in [
                pygame.MOUSEMOTION,
                pygame.WINDOWSHOWN,
                pygame.WINDOWMOVED,
                pygame.WINDOWHIDDEN,
                pygame.WINDOWEXPOSED,
                pygame.AUDIODEVICEADDED,
                pygame.WINDOWSIZECHANGED,
                pygame.VIDEOEXPOSE,
                pygame.WINDOWENTER,
                pygame.WINDOWFOCUSGAINED
            ]:
                pass
            else:
                self.system_operations.log(f"Pygame Event: {event}")
        return events

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
                    if event.key == pygame.K_c:
                        raise ViewerExitException(101, f"Control-C event received")
                    raise ViewerExitException(100, f"Quit event {event.key} received")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.last_mouse_pos = event.pos
                x = event.pos[0]
                y = event.pos[1]