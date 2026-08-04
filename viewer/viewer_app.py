import sys
from viewer.src.photo_frame_app import PhotoFrameApp

def main() -> int:
    try:
        display = None
        if len(sys.argv) > 1:
            if sys.argv[1] == "pc":
                from viewer.src.pcdisplay import PCSystemDisplay
                display = PCSystemDisplay()
        if display is None:
            from viewer.src.pidisplay import PiSystemDisplay
            display = PiSystemDisplay()

        app = PhotoFrameApp(display)
        result = app.run()
        return result
    except KeyboardInterrupt as e:
        print('Exiting due to keyboard interrupt')
        return 1

if __name__ == '__main__':
    raise SystemExit(main())