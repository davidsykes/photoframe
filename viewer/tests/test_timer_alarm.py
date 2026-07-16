import sys
sys.path.append('src')
import unittest
from timer_alarm import TimerAlarm

class MockSystem:
    def __init__(self, data):
        pass

class AnAlarmGoesOffAtTheCorrectTime(unittest.TestCase):
    def test_load(self):
        mock_system = MockSystem()
        timer_alarm = TimerAlarm(mock_system, 100)

        # Start the timer alarm
        timer_alarm.start()

        # Wait for 2 seconds to ensure the alarm goes off
        import time
        time.sleep(2)

        # Check if the alarm has gone off
        self.assertTrue(timer_alarm.alarm_triggered)

if __name__ == "__main__":
    unittest.main()