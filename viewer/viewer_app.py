import sys
from viewer.src.photo_frame_app import PhotoFrameApp

def main() -> int:
    display = None
    if len(sys.argv) > 1:
        if sys.argv[1] == "pc":
            from viewer.src.pcdisplay import PCSystemDisplay
            display = PCSystemDisplay()
    if display is None:
        from viewer.src.pidisplay import PiSystemDisplay
        display = PiSystemDisplay()

    display.initialise()
    app = PhotoFrameApp(display)
    result = app.run()
    return result


if __name__ == '__main__':
    raise SystemExit(main())