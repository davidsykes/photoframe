import sys
sys.path.append('./src')

from app import PhotoFrameApp
from pcdisplay import PCSystemDisplay
from pidisplay import PiSystemDisplay

print(sys.argv)

display = None
if len(sys.argv) > 1:
    if sys.argv[1] == "test":
        from tests import Tests
        tests = Tests()
        tests.run_all_tests()
    elif sys.argv[1] == "pc":
        display = PCSystemDisplay()
if display is None:
    display = PiSystemDisplay()

display.initialise()
app = PhotoFrameApp(display)
app.run()