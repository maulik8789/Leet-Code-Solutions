class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
        }

        result = ''
        keys = list(roman_numerals.keys())
        while num > 0:
            for i in range(len(keys)):
                if roman_numerals[keys[i]] > num:
                    result += keys[i - 1]
                    num -= roman_numerals[keys[i - 1]]
                    break
                elif roman_numerals[keys[-1]] <= num:
                    result += keys[-1]
                    num -= roman_numerals[keys[-1]]
                    break
        return result