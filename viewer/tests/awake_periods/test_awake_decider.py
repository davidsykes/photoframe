import unittest
from unittest.mock import Mock

from viewer.src.awake_periods.awake_decider import AwakeDecider
from viewer.src.awake_periods.awake_schedule import AwakeSchedule
from viewer.src.display.display_controller import DisplayController

class AwakeDeciderTests(unittest.TestCase):
    def test_we_are_awake_until_a_menu_selection_says_we_are_not(self):
        self.assertEqual(self.out.are_we_awake(), True)

        self.out.go_to_sleep()
        self.assertEqual(self.out.are_we_awake(), False)

    def test_we_are_asleep_until_a_menu_selection_says_we_are_not(self):
        self.out.go_to_sleep()
        self.assertEqual(self.out.are_we_awake(), False)

        self.out.wake_up()

        self.assertEqual(self.out.are_we_awake(), True)

    def test_we_are_awake_until_it_is_time_to_sleep(self):
        self.assertEqual(self.out.are_we_awake(), True)

        self.sleep_timer.are_we_awake.return_value = False
        self.assertEqual(self.out.are_we_awake(), False)

    def test_menu_option_overrides_sleep_timer_when_it_comes_later(self):
        self.assertEqual(self.out.are_we_awake(), True)

        self.sleep_timer.are_we_awake.return_value = False
        self.assertEqual(self.out.are_we_awake(), False)

        self.out.wake_up()
        self.assertEqual(self.out.are_we_awake(), True)

    def test_timer_option_overrides_menu_when_it_changes(self):
        self.sleep_timer.are_we_awake.return_value = False
        self.assertEqual(self.out.are_we_awake(), False)
        self.out.wake_up()
        self.assertEqual(self.out.are_we_awake(), True)

        self.out.go_to_sleep()
        self.sleep_timer.are_we_awake.return_value = True

        self.assertEqual(self.out.are_we_awake(), True)

    def test_going_to_sleep_turns_the_display_off(self):
        self.assertEqual(self.out.are_we_awake(), True)

        self.out.go_to_sleep()

        self.display_controller.display_off.assert_called_once()

    def test_waking_up_turns_the_display_on(self):
        self.out.go_to_sleep()
        self.display_controller.display_on.assert_not_called()

        self.out.wake_up()

        self.assertEqual(self.out.are_we_awake(), True)
        self.display_controller.display_on.assert_called_once()

    def setUp(self):
        self.sleep_timer = Mock(spec=AwakeSchedule)
        self.sleep_timer.are_we_awake.return_value = True
        self.display_controller = Mock(spec=DisplayController)
        self.out = AwakeDecider(self.sleep_timer, self.display_controller)
