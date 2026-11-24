import unittest

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

    def test_if_pid_not_found_none_is_returned(self):
        output = "\n".join(
            ['pid1 python',
             'pid2 python watev something',
             'pid3 python watev something else'])

        pid = self.out.extract_pid(output)

        self.assertIsNone(pid)

    def setUp(self):
        self.out = PIDRSSExtractor()

