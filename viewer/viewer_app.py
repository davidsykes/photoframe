from pathlib import Path
import sys
from common.src.system_operations import SystemOperations
from viewer.src.photo_frame_app import DisplayType, PhotoFrameApp
from viewer.src.viewer_exit_exception import ViewerExitException


APP_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = APP_ROOT.parent

def main() -> int:
    print(f"Starting Photo Frame Viewer from {PROJECT_ROOT}")
    system_operations = SystemOperations()
    system_operations.set_logger('viewer', '..')
    system_operations.log('Application Starting')
    try:
        display_type = DisplayType.PI_DISPLAY_VERSION
        if len(sys.argv) > 1:
            if sys.argv[1] == "pc":
                display_type = DisplayType.PC_TEST_VERSION
        app = PhotoFrameApp(display_type)
        result = app.run(system_operations, PROJECT_ROOT)
        return result
    except ViewerExitException as e:
        system_operations.log(f'Exiting due to viewer exit exception {e}')
        return e.exit_code
    except KeyboardInterrupt as e:
        system_operations.log('Exiting due to keyboard interrupt')
        return 1

if __name__ == '__main__':
    raise SystemExit(main())