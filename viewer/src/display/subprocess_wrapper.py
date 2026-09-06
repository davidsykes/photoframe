import subprocess

class SubprocessWrapper:
    def run(self):
        try:
            result = subprocess.run(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr.decode('utf-8')}"

    def run_return_stdout(self, command):
        result = subprocess.run(command,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                check=True)
        return result.stdout.decode('utf-8')