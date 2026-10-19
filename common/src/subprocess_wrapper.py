import subprocess

class SubprocessWrapper:
    def run_return_stdout(self, command):
        result = subprocess.run(command,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                check=True)
        return result.stdout.decode('utf-8')