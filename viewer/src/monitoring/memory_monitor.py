class MemoryMonitor:
    def __init__(self,
                 subprocess_wrapper,
                 status_updater):
        self._subprocess_wrapper = subprocess_wrapper
        self._status_updater = status_updater

    def check_memory_usage(self):
        command = 'pgrep -af python'
        try:
            output = self._subprocess_wrapper.run_return_stdout(command)
            output = output.splitlines()
            self._status_updater.update_status('pgrep 0', 'Begin')
            for o in range(len(output)):
                self._status_updater.update_status(f'pgrep {o+1}', output[o])
                print(f'SADSJALDJSLAJDLSJADJ {output[o]}')
        except Exception as e:
            self._status_updater.update_status('pgrep error', f'{command} {e}')