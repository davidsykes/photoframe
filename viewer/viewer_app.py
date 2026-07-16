from app import PhotoFrameApp
from pcdisplay import PCSystemDisplay
from pidisplay import PiSystemDisplay
import logging

logging.basicConfig(
    filename="logs/viewer.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)
logger = logging.getLogger(__name__)


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