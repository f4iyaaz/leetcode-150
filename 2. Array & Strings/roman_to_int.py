class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0
        i = 0
        while i < len(s):
            if s[i] != 'C' and s[i] != 'I' and s[i] != 'X':
                number += roman_to_int[s[i]]
                i += 1
            elif s[i] == 'C':
                if i + 1 < len(s) and s[i + 1] == 'M':
                    number += 900
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == 'D':
                    number += 400
                    i += 2
                else:
                    number += roman_to_int[s[i]]
                    i += 1
            elif s[i] == 'I':
                if i + 1 < len(s) and s[i + 1] == 'V':
                    number += 4
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == 'X':
                    number += 9
                    i += 2
                else:
                    number += roman_to_int[s[i]]
                    i += 1
            elif s[i] == 'X':
                if i + 1 < len(s) and s[i + 1] == 'L':
                    number += 40
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == 'C':
                    number += 90
                    i += 2
                else:
                    number += roman_to_int[s[i]]
                    i += 1
        return number
