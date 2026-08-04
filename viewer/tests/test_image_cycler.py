import unittest
from unittest.mock import Mock, call

from viewer.src.image_cycler import ImageCycler


class ImageCyclerTests(unittest.TestCase):
    def test_images_are_cycled_in_sequence(self):
        self.out.cycle_images()

        self.display.show_image.assert_has_calls(
            [call('one'),
             call('two'),
             call('three')
            ]
        )
        self.system_operations.sleep.assert_has_calls(
            [call(42),
             call(42),
             call(42)
            ]
        )
        
    def test_cycling_stops_when_cycle_stop_detector_indicates_stop(self):
        self.cycle_stop_detector.should_stop.side_effect = [
            False, False, True, True]
        
        self.out.cycle_images()

        self.display.show_image.assert_has_calls(
            [call('one'),
             call('two')
            ]
        )
        self.system_operations.sleep.assert_has_calls(
            [call(42),
             call(42)
            ]
        )

    @classmethod
    def setUp(self):
        self.system_operations = Mock()
        self.system_operations.sleep = Mock()
        self.next_image_selector = Mock()
        self.next_image_selector.select_next_image.side_effect = [
            'one', 'two', 'three', 'four'
        ]
        self.cycle_stop_detector = Mock()
        self.cycle_stop_detector.should_stop.side_effect = [
            False, False, False, True]
        self.display = Mock()
        self.out = ImageCycler(
            self.system_operations,
            self.next_image_selector,
            self.cycle_stop_detector,
            self.display,
            42)
