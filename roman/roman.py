class RomanNumber(str):
    """ Class to represent roman numerals
        TODO: Implement magic methods for addition, subtraction and comparison
    """
    arabic_numerals = (1, 5, 10, 50, 100, 500, 1000)
    roman_numerals = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
    arabic_to_roman_map = dict(zip(arabic_numerals, roman_numerals))

    def __init__(self, value):
        # TODO: Validate if value is valid roman numeral
        super().__init__()
        self.value = value

    def __repr__(self):
        return f'RomanNumber({self.value})'

    def __str__(self):
        return self.value

    @classmethod
    def from_arabic(cls, arabic_num):
        """ Alternate constructor to create roman number from an arabic
            Algorithm:
                Subtract the highest possible number from arabic value, so that it still stays positive,
                then convert the subtracted value to arabic and append to return value.
                If the value would contain 4 letter that are the same, replace them with
                one bigger roman numeral minus the repeated letter. At the end we replace edge cases
                so DCD becomes CM... etc.
        """
        if not 0 < arabic_num < 4000:
            raise ValueError("Cannot represent number in Roman")

        value = ''
        while arabic_num >= 0:
            subtractable_arabics = list(filter(lambda n: n <= arabic_num, cls.arabic_numerals))
            if len(subtractable_arabics):
                highest_subtractable_arabic = max(subtractable_arabics)
                arabic_num = arabic_num - highest_subtractable_arabic

                numeral = cls.arabic_to_roman_map[highest_subtractable_arabic]
                value += numeral
                if value.count(numeral) > 3:
                    current_index = cls.arabic_numerals.index(highest_subtractable_arabic)
                    next_numeral = cls.roman_numerals[current_index + 1]
                    value = value[:-4] + numeral + next_numeral
                    value = value.replace('DCD', 'CM').replace('LXL', 'XC').replace('VIV', 'IX')
            else:
                return value
