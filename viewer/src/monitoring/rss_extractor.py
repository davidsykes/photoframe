class RSSExtractor:
    def extract_rss(self, data):
        data = data.splitlines()[1]
        data = data.split()[1]
        return data