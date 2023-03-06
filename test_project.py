from project import check_input, to_julian_day_number, to_julian_date, to_chinese_date,to_hebrew_date


def test_check_input():
    assert check_input('2023-12-12') == (2023, 12, 12)
    assert check_input('2010-10-10') == (2010, 10, 10)
    assert check_input('1833-06-12') == (1833, 6, 12)
    assert check_input('1962-1-1') == (1962, 1, 1)
    assert check_input('1962-32-1') == ('*Wrong month', False, 0)
    assert check_input('1962-3-66') == ('*Wrong day', False, 0)

def test_to_julian_day_number():
    assert to_julian_day_number(2023, 12, 12) == 2460291
    assert to_julian_day_number(2000, 7, 22) == 2451748
    assert to_julian_day_number(12, 12, 12) == 1725789




def test_to_julian_date():
    assert to_julian_date(2460291) == '2023-11(November)-29'
    assert to_julian_date(2451748) == '2000-07(July)-9'
    assert to_julian_date(1725789) == '12-12(December)-14'



def test_to_chinese_date():
    assert to_chinese_date(2023) == '2023 year of the Rabbit'
    assert to_chinese_date(1833) == 'The calculation is possible only after 1900.'
    assert to_chinese_date(2001) == '2001 year of the Snake'
    assert to_chinese_date(2018) == '2018 year of the Dog'


def test_to_hebrew_date():
    assert to_hebrew_date(2019,4,23) == '5779-01(Nisan)-18'
    assert to_hebrew_date(1833,12,30) == '5594-10(Tevet)-18'
    assert to_hebrew_date(1962,3,19) == '5722-13(Adar II)(Leap year)-13'
    assert to_hebrew_date(1532,6,8) == '5292-03(Sivan)-25'


