import unittest
from unittest.mock import Mock

from viewer.src.monitoring.rss_extractor import RSSExtractor

class RSSExtractorTests(unittest.TestCase):
    def test_simple_extraction(self):
        output = "\n".join(
            ['PID RSS VSZ etc',
             'pid rss vsz etc'])

        result = self.out.extract_rss(output)

        self.assertEqual(result, 'rss')

    def setUp(self):
        self.out = RSSExtractor()

