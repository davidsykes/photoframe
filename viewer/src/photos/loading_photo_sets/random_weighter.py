class RandomWeighter:
    def __init__(self, now):
        self._now = now

    def weigh(self, set_date):
        age = (self._now - set_date).days
        if age <= 7:
            return 8
        if age <= 30:
            return 5
        if age <= 90:
            return 3
        return 1