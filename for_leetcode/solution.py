class Solution:
    def __init__(self):
        self.year = 0

    def romanToInt(self, s: str) -> int:
        without_CM = self.find_and_del_cm(s)
        without_CD = self.find_and_del_cd(without_CM)
        without_XC = self.find_and_del_xc(without_CD)
        without_XL = self.find_and_del_xl(without_XC)
        without_IX = self.find_and_del_ix(without_XL)
        without_IV = self.find_and_del_iv(without_IX)
        total = self.total(without_IV)
        return total

    def find_and_del_cm(self, m):
        if "CM" in m:
            self.year += 900
            new_s = m.replace("CM", "")
            return new_s
        else:
            return m

    def find_and_del_cd(self, m):
        if "CD" in m:
            self.year += 400
            new_s = m.replace("CD", "")
            return new_s
        else:
            return m

    def find_and_del_xc(self, m):
        if "XC" in m:
            self.year += 90
            new_s = m.replace("XC", "")
            return new_s
        else:
            return m

    def find_and_del_xl(self, m):
        if "XL" in m:
            self.year += 40
            new_s = m.replace("XL", "")
            return new_s
        else:
            return m

    def find_and_del_ix(self, m):
        if "IX" in m:
            self.year += 9
            new_s = m.replace("IX", "")
            return new_s
        else:
            return m

    def find_and_del_iv(self, m):
        if "IV" in m:
            self.year += 4
            new_s = m.replace("IV", "")
            return new_s
        else:
            return m

    def total(self, m):
        for letter in m:
            if letter == "M":
                self.year += 1000
                continue
            if letter == "D":
                self.year += 500
                continue
            if letter == "C":
                self.year += 100
                continue
            if letter == "L":
                self.year += 50
                continue
            if letter == "X":
                self.year += 10
                continue
            if letter == "V":
                self.year += 5
                continue
            if letter == "I":
                self.year += 1
                continue
        return self.year
