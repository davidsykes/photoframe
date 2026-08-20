from pathlib import Path
import subprocess
import sys
import time

class SubprocessExec:
    def __init__(self, system_operations):
        self._system_operations = system_operations

    def launch_app(self,
                   release_folder: Path,
                   module_name: str,
                   parameters: str,
                   sleep_time: int) -> subprocess.Popen:
        print(f'Launch {module_name} from {release_folder}')
        process = subprocess.Popen(
            [
                sys.executable,
                '-m',
                module_name,
                parameters
            ],
            cwd=release_folder,
        )
        print('wait or poll process')
        if process.poll() is None:
            print('Viewer is still running')
        else:
            print(f'Viewer exited with code {process.returncode}')

        exit_code = process.wait()
        self._system_operations.log(f'{module_name} exited with code {exit_code}')
        self._system_operations.log('--------------')
        if exit_code not in [100,101]:
            print(f'Pausing for {sleep_time} seconds...')
            time.sleep(sleep_time)
        return exit_code
