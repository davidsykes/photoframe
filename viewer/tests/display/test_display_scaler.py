import unittest
from unittest.mock import Mock

from viewer.src.display.display_scaler import DisplayScaler
from viewer.src.display.display_wrapper import DisplayWrapper


class DisplayScalerTests(unittest.TestCase):
    def test_percentages_are_converted_into_pixels(self):
        self.display.screen_size.return_value = (1024, 768)

        scaled = self.out.scale((50, 25))

        self.assertEqual((512, 192), scaled)

    def setUp(self):
        self.display = Mock()
        self.out = DisplayScaler(self.display)
