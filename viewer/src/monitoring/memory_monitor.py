class MemoryMonitor:
    def __init__(self,
                 subprocess_wrapper,
                 status_updater,
                 pid_rss_extractor):
        self._subprocess_wrapper = subprocess_wrapper
        self._status_updater = status_updater
        self._pid_rss_extractor = pid_rss_extractor
        self._rss = ''

    def check_memory_usage(self):
        pgrep_command = ['pgrep', '-af', 'python']
        try:
            output = self._subprocess_wrapper.run_return_stdout(pgrep_command)
            pid = self._pid_rss_extractor.extract_pid(output)
            if pid is not None:
                return self.process_pid_rss(pid)
            self.status_print(output.splitlines())
        except Exception as e:
            self._status_updater.update_status('pgrep error', f'{pgrep_command} {e}')

    def status_print(self, lines):
        self._status_updater.update_status('pgrep 0', f'Begin {len(lines)}')
        for o in range(len(lines)):
            self._status_updater.update_status(f'pgrep {o+1}', lines[o])

    def process_pid_rss(self, pid):
        command = ['ps', '-p', pid, '-o', 'pid,rss,vsz,%mem,cmd']
        output = self._subprocess_wrapper.run_return_stdout(command)
        rss = self._rss_extractor.extract_rss(output)
        self._rss = self._rss + ' ' + rss
        self._status_updater.update_status('RSS', self._rss)