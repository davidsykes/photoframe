from pathlib import Path
import subprocess
import sys

class VersionRunner:
    def __init__(self, sandbox):
        self._sandbox = sandbox

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
        return exit_code

    def launch_viewer(self, release_folder: Path) -> subprocess.Popen:
        print(f'Launch viewer from {release_folder}')
        return subprocess.Popen(
            [
                sys.executable,
                '-m',
                'viewer.viewer_app',
            ],
            cwd=release_folder,
        )