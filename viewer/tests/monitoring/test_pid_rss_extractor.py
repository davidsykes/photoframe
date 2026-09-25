import unittest
from unittest.mock import Mock

from viewer.src.monitoring.pid_rss_extractor import PIDRSSExtractor

class PIDRSSExtractorTests(unittest.TestCase):
    def test_simple_pid_extraction(self):
        output = "\n".join(
            ['pid1 python',
             'pid2 python watev viewer_app',
             'pid3 python watev something else'])

        pid = self.out.extract_pid(output)

        self.assertEqual(pid, 'pid2')

    def test_simple_rss_extraction(self):
        output = "\n".join(
            ['PID RSS VSZ etc',
             'pid rss vsz etc'])

        result = self.out.extract_rss(output)

        self.assertEqual(result, 'rss')

    def setUp(self):
        self.out = PIDRSSExtractor()

