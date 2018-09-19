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

literals = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
numbers = (1, 5, 10, 50, 100, 500, 1000)
@pytest.mark.parametrize('arabic,roman', zip(numbers, literals))
def test_basic_literal(arabic, roman):
    RomanNumber.from_arabic(1) == 'i'
