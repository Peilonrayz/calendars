class Gregorian:
    MONTHS = {
        True: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        False: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    }

    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day

    def __str__(self):
        return f'{self._year}:{self._month}:{self._day}'

    @classmethod
    def from_days(cls, days):
        year = int(days // 365.2425) + 1
        days -= cls._days_from_year(year)
        if days == 0:
            year -= 1
        leap_year = (366 if cls._is_leap_year(year) else 365)
        if days == 0:
            days += leap_year
        if days > leap_year:
            year += 1
            days -= leap_year
        for month, m in enumerate(cls.MONTHS[cls._is_leap_year(year)], start=1):
            if days <= m:
                break
            days -= m
        else:
            raise ValueError()
        return cls(year, month, days)

    @classmethod
    def _is_leap_year(cls, year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        return year % 4 == 0

    @staticmethod
    def _days_from_year(year):
        year -= 1
        return (
            year * 365
            + year // 4
            - year // 100
            + year // 400
        )

    def days(self):
        return (
            self._days_from_year(self._year)
            + sum(self.MONTHS[self._is_leap_year(self._year)][:self._month - 1])
            + self._day
        )

