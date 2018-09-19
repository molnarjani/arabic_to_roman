class RomanNumber(str):
    @classmethod
    def from_arabic(cls, num):
        if not 0 < num < 4000:
            raise ValueError("Cannot represent number in Roman")
