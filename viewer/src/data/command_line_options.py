from viewer.src.photo_frame_app import DisplayType


class CommandLineOptions:
    def __init__(self, argv):
        self.display_type = DisplayType.PI_DISPLAY_VERSION
        self.run_new_code = False
        self.always_awake = False

        for arg in argv:
            if arg == 'pc':
                self.display_type = DisplayType.PC_TEST_VERSION
            if arg == 'new':
                self.run_new_code = True
            if arg == 'awake':
                self.always_awake = True