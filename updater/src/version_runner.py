from pathlib import Path
import subprocess
import sys
from time import time

class VersionRunner:
    def __init__(self, system_operations, sandbox, parameters):
        self._system_operations = system_operations
        self._sandbox = sandbox
        self._parameters = parameters

    def run_version(self, name):
        release_folder = Path('/home/pi/photoframe/releases/1.2.0')
        release_folder = self._sandbox.get_version_folder(name)
        process = self.launch_viewer(release_folder)
        print('wait or poll process')
        if process.poll() is None:
            print('Viewer is still running')
        else:
            print(f'Viewer exited with code {process.returncode}')

        exit_code = process.wait()
        self._system_operations.log(f'Viewer exited with code {exit_code}')
        print('Trying an earlier version in 5 seconds...')
        time.sleep(5)
        return exit_code

    def launch_viewer(self, release_folder: Path) -> subprocess.Popen:
        print(f'Launch viewer from {release_folder}')
        return subprocess.Popen(
            [
                sys.executable,
                '-m',
                'viewer.viewer_app',
                self._parameters
            ],
            cwd=release_folder,
        )