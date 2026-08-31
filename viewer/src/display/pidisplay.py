import pygame # pyright: ignore[reportMissingImports]
from viewer.src.display.pygame_image import PygameImage
from viewer.src.menus.uievent import UIEvent, UIEventType
from viewer.src.viewer_exit_exception import ViewerExitException

class PiSystemDisplay:
    def __init__(self, system_operations, status_updater):
        self.system_operations = system_operations
        self._status_updater = status_updater
        self.event_count = 0
        self._clock = pygame.time.Clock()
        self._flip_count = 0
        self.COLOUR_WHITE = (255,255,255)
        self.COLOUR_LIGHT = (170,170,170)

    def initialise_display(self):
        print("Initialising Pi System Display.")
        pygame.init()
        print('Desktop sizes:', pygame.display.get_desktop_sizes())
        self.screen = pygame.display.set_mode(
            (0,0), pygame.FULLSCREEN)
        print('Pygame surface:', self.screen.get_size())
        pygame.display.set_caption("Pi System Display")
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        pygame.mouse.set_visible(False)

    def load_image(self, image_path):
        self._status_updater.update_status('Current image', image_path)
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

        return PygameImage(image_path, image, x, y)

    def prepare_screen(self):
        self.screen.fill((0, 0, 0))
        self._print_y = 0

    def show_image(self, image):
        self.screen.blit(image.image, (image.x, image.y))
        self._status_updater.update_status('Current image', image.image_path)

    def flip(self):
        pygame.display.flip()
        self._flip_count = self._flip_count + 1
        self._status_updater.update_status('Flip count', self._flip_count)

    def tick(self, v):
        self._clock.tick(v)

    def print(self, message):
        text_surface = self.my_font.render(message,
                                           True,
                                           (255, 255, 255))
        self.screen.blit(text_surface, (8, self._print_y))
        self._print_y += 20
    
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
                x = event.pos[0]
                y = event.pos[1]
                events.append(UIEvent(
                    UIEventType.MOUSE_DOWN,
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
                pygame.WINDOWRESIZED,
                pygame.VIDEORESIZE,
                pygame.VIDEOEXPOSE,
                pygame.WINDOWENTER,
                pygame.WINDOWFOCUSGAINED,
                pygame.ACTIVEEVENT,
                pygame.MOUSEBUTTONUP,
            ]:
                pass
            elif event.type in [
                pygame.WINDOWLEAVE,
                pygame.K_UNKNOWN
            ]:
                self.system_operations.log(f"Pygame Event: {event}")
            else:
                self.system_operations.log(f"Unrecognised Pygame Event: {event}")
        return events

    # def draw_button(self):
    #     line_color = (255, 0, 0)
    #     pygame.draw.line(self.screen, line_color, (60, 80), (130, 100))

    #     play_button = pygame.Rect(300, 300, 140, 50)
    #     quit_button = pygame.Rect(300, 380, 140, 50)

    #     WHITE = (255,255,255)
    #     LIGHT = (170,170,170)
    #     DARK = (100,100,100)
    #     pygame.draw.rect(self.screen, LIGHT, play_button)
    #     pygame.draw.rect(self.screen, DARK, quit_button)

    #     play_text = self.my_font.render("Pause", True, WHITE)
    #     quit_text = self.my_font.render("Resume", True, WHITE)

    #     self.screen.blit(play_text, (335, 305))
    #     self.screen.blit(quit_text, (335, 385))

    def draw_rectangle(self, colour, position):
        rect = pygame.Rect(position[0], position[1],
                         position[2], position[3])

        pygame.draw.rect(self.screen, colour, rect)

    def draw_text(self, text, colour, position):
        pygame_text = self.my_font.render(text, True, colour)
        self.screen.blit(pygame_text, position)
