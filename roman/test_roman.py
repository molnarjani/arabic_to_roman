import pytest

from roman import RomanNumber


def test_zero():
    with pytest.raises(ValueError):
        RomanNumber.from_arabic(0)

def test_negative():
    with pytest.raises(ValueError):
        RomanNumber.from_arabic(-1)

def test_overflow():
    with pytest.raises(ValueError):
        RomanNumber.from_arabic(4000)

arabic = (1, 5, 10, 50, 100, 500, 1000)
roman = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
@pytest.mark.parametrize('arabic,roman', zip(arabic, roman))
def test_basic_literal(arabic, roman):
    assert RomanNumber.from_arabic(arabic) == roman

def test_roman_addition():
    assert RomanNumber.from_arabic(3) == 'III'

def test_roman_subtraction():
    assert RomanNumber.from_arabic(4) == 'IV'

def test_roman_examples():
    assert RomanNumber.from_arabic(2417) == 'MMCDXVII'
    assert RomanNumber.from_arabic(999) == 'CMXCIX'
    assert RomanNumber.from_arabic(290) == 'CCXC'
    assert RomanNumber.from_arabic(1742) == 'MDCCXLII'
    assert RomanNumber.from_arabic(3974) == 'MMMCMLXXIV'

