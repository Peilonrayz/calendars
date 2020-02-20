import datetime

from calendars import Gregorian, Julian


def test_julian_days():
    # type: () -> None
    for i in range(737424):
        d = Julian.from_days(i)
        assert d.days() == i


def test_julian_date():
    # type: () -> None
    b = datetime.date(1, 1, 1)
    one = datetime.timedelta(1)
    for i in range(1, 737424):
        d = Gregorian.from_days(i)
        assert d._year == b.year and d._month == b.month and d._day == b.day
        b += one


def test_print_julian():
    # type: () -> None
    d = Julian(1582, 10, 5)
    # d = Julian.from_days(1460)
    print(d)
    print(d.days())
    print(Julian.from_days(d.days()))
    assert True


def test_print_gregorian():
    # type: () -> None
    d = Gregorian(1582, 10, 15)
    # d = Gregorian.from_days(1460)
    print(d)
    print(d.days())
    print(Gregorian.from_days(d.days()))
    assert True
