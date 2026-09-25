class PIDRSSExtractor:
    def extract_pid(self, pid_data):
        pids = pid_data.splitlines()
        for pid in pids:
            if 'viewer_app' in pid:
                return pid.split()[0]

    def extract_rss(self, data):
        data = data.splitlines()[1]
        data = data.split()[1]
        return data