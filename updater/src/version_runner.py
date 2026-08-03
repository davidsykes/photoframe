

class VersionRunner:
    def __init__(self,
                 system_operations,
                 subprocess_exec,
                 sandbox,
                 parameters):
        self._system_operations = system_operations
        self._subprocess_exec = subprocess_exec
        self._sandbox = sandbox
        self._parameters = parameters

    def run_version(self, name):
        release_folder = self._sandbox.get_version_folder(name)
        exit_code = self.launch_app(
            release_folder,
            'synchroniser.synchroniser_main',
            '',
            3)
        exit_code = self.launch_app(
            release_folder,
            'viewer.viewer_app',
            self._parameters,
            10)

    def launch_app(self, release_folder, module_name, parameters, sleep_time):
        return self._subprocess_exec.launch_app(
            release_folder,
            module_name,
            parameters,
            sleep_time)
