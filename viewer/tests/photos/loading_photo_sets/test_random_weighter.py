from datetime import date, timedelta
import unittest
from viewer.src.photos.loading_photo_sets.random_weighter import RandomWeighter

class RandomWeighterTests(unittest.TestCase):
    def test_photos_less_than_a_week_old_have_priority_8(self):
        self.assertEqual(8, self.out.weigh(self.age(1)))
        self.assertEqual(8, self.out.weigh(self.age(5)))
        self.assertEqual(8, self.out.weigh(self.age(7)))

    def test_photos_more_than_a_week_less_than_a_month_old_have_priority_5(self):
        self.assertEqual(5, self.out.weigh(self.age(8)))
        self.assertEqual(5, self.out.weigh(self.age(18)))
        self.assertEqual(5, self.out.weigh(self.age(30)))

    def test_photos_1_to_3_months_old_have_priority_3(self):
        self.assertEqual(3, self.out.weigh(self.age(31)))
        self.assertEqual(3, self.out.weigh(self.age(61)))
        self.assertEqual(3, self.out.weigh(self.age(90)))

    def test_photos_more_than_3_months_old_have_priority_1(self):
        self.assertEqual(1, self.out.weigh(self.age(91)))
        self.assertEqual(1, self.out.weigh(self.age(161)))
        self.assertEqual(1, self.out.weigh(self.age(1000)))

    def setUp(self):
        self.now = date.fromisoformat('2023-04-07')
        self.out = RandomWeighter(self.now)

    def age(self, days_to_subtract):
        return self.now - timedelta(days=days_to_subtract)