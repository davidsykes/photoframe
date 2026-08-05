import sys
from viewer.src.photo_frame_app import DisplayType, PhotoFrameApp

def main() -> int:
    try:
        display_type = DisplayType.PI_DISPLAY_VERSION
        if len(sys.argv) > 1:
            if sys.argv[1] == "pc":
                display_type = DisplayType.PC_TEST_VERSION
        app = PhotoFrameApp(display_type)
        result = app.run()
        return result
    except KeyboardInterrupt as e:
        print('Exiting due to keyboard interrupt')
        return 1

if __name__ == '__main__':
    raise SystemExit(main())