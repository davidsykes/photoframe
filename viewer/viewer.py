import sys
from app import PhotoFrameApp
from pcdisplay import PCSystemDisplay
from pidisplay import PiSystemDisplay

print(sys.argv)

if (len(sys.argv) > 1 and sys.argv[1] == "pc"):
    display = PCSystemDisplay()
else:
    display = PiSystemDisplay()

display.initialise()
app = PhotoFrameApp(display)
app.run()