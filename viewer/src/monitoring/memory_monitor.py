class MemoryMonitor:
    def __init__(self,
                 subprocess_wrapper,
                 status_updater,
                 rss_extractor):
        self._subprocess_wrapper = subprocess_wrapper
        self._status_updater = status_updater
        self._rss_extractor = rss_extractor
        self._rss = ''

    def check_memory_usage(self):
        command = ['pgrep', '-af', 'python']
        try:
            output = self._subprocess_wrapper.run_return_stdout(command)
            output = output.splitlines()
            if len(output) == 1:
                self.process_pgrep_output(output[0])
            else:
                self.status_print(output)
        except Exception as e:
            self._status_updater.update_status('pgrep error', f'{command} {e}')

    def status_print(self, lines):
        self._status_updater.update_status('pgrep 0', f'Begin {len(lines)}')
        for o in range(len(lines)):
            self._status_updater.update_status(f'pgrep {o+1}', lines[o])

    def process_pgrep_output(self, prep_info):
        pid = prep_info.split()[0]
        command = ['ps', '-p', pid, '-o', 'pid,rss,vsz,%mem,cmd']
        output = self._subprocess_wrapper.run_return_stdout(command)
        rss = self._rss_extractor.extract_rss(output)
        self._rss = self._rss + ' ' + rss
        self._status_updater.update_status('RSS', self._rss)