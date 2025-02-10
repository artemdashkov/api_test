ROMAN_NUM = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}

ROMAN_NUM_TWO = {
    "CM": 900,
    "CD": 400,
    "XC": 90,
    "XL": 40,
    "IX": 9,
    "IV": 4
}

class Solution:

    def __init__(self):
        self.year = 0

    def romanToInt(self, s: str) -> int:
        for num in ROMAN_NUM_TWO:
            if num in s:
                self.year += ROMAN_NUM_TWO[num]
                s = s.replace(num, '')
        for num in s:
            self.year += ROMAN_NUM[num]
        return self.year

solution = Solution()
print(solution.__dict__)